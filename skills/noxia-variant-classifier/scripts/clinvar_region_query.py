#!/usr/bin/env python3
"""
Fetch ClinVar variants by genomic region using NCBI E-utilities API.
Extracts variant nomenclature, clinical classification, and review status.
"""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import json
import csv
import time
import argparse
from typing import List, Dict, Any


def create_session() -> requests.Session:
    """Create a requests session with retry logic."""
    session = requests.Session()
    retry_strategy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def search_clinvar_region(chrom: str, start: int, end: int, retmax: int = 500, session: requests.Session = None) -> List[str]:
    """Search ClinVar for variant IDs in a genomic region."""
    if session is None:
        session = create_session()

    # Remove 'chr' prefix if present
    chrom = chrom.replace('chr', '')

    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "clinvar",
        "term": f"{chrom}[CHR] AND {start}:{end}[CHRPOS]",
        "retmode": "json",
        "retmax": retmax
    }

    response = session.get(base_url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    total_count = int(data["esearchresult"]["count"])
    id_list = data["esearchresult"]["idlist"]

    print(f"Found {total_count} variants in {chrom}:{start}-{end}")

    # Handle pagination if needed
    if total_count > retmax:
        print(f"Fetching all IDs (retmax={retmax} per request)...")
        all_ids = id_list.copy()
        retstart = retmax

        while retstart < total_count:
            params["retstart"] = retstart
            response = session.get(base_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            all_ids.extend(data["esearchresult"]["idlist"])
            retstart += retmax
            time.sleep(0.5)

        return all_ids

    return id_list


def fetch_variant_details(variant_ids: List[str], batch_size: int = 20, session: requests.Session = None) -> List[Dict[str, Any]]:
    """Fetch variant details from ClinVar using esummary."""
    if session is None:
        session = create_session()

    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    all_variants = []

    # Process in batches (smaller batches for reliability)
    for i in range(0, len(variant_ids), batch_size):
        batch = variant_ids[i:i + batch_size]
        print(f"Fetching details for variants {i + 1}-{min(i + batch_size, len(variant_ids))}...")

        params = {
            "db": "clinvar",
            "id": ",".join(batch),
            "retmode": "json"
        }

        try:
            response = session.get(base_url, params=params, timeout=60)
            response.raise_for_status()
            data = response.json()

            # Parse each variant
            result = data.get("result", {})
            for vid in batch:
                if vid in result:
                    variant = result[vid]
                    parsed = parse_variant(variant)
                    all_variants.append(parsed)

        except requests.exceptions.RequestException as e:
            print(f"  Warning: Failed to fetch batch, retrying individually...")
            # Retry each variant individually
            for vid in batch:
                try:
                    time.sleep(0.5)
                    params["id"] = vid
                    response = session.get(base_url, params=params, timeout=30)
                    response.raise_for_status()
                    data = response.json()
                    result = data.get("result", {})
                    if vid in result:
                        parsed = parse_variant(result[vid])
                        all_variants.append(parsed)
                except Exception as e2:
                    print(f"  Error fetching variant {vid}: {e2}")

        # Rate limit - be gentle with NCBI servers
        time.sleep(0.5)

    return all_variants


def parse_variant(variant: Dict[str, Any]) -> Dict[str, Any]:
    """Parse variant data from esummary response."""
    # Get clinical significance - check multiple possible fields
    # ClinVar API uses germline_classification, somatic_clinical_impact, or oncogenicity_classification
    classification = "Not provided"
    review_status = "Not provided"
    last_evaluated = ""

    # Try germline classification first (most common)
    germline = variant.get("germline_classification", {})
    if isinstance(germline, dict) and germline.get("description"):
        classification = germline.get("description", "Not provided")
        review_status = germline.get("review_status", "Not provided")
        last_evaluated = germline.get("last_evaluated", "")

    # Try somatic classification if germline is empty
    if classification == "Not provided":
        somatic = variant.get("somatic_clinical_impact", {})
        if isinstance(somatic, dict) and somatic.get("description"):
            classification = somatic.get("description", "Not provided")
            review_status = somatic.get("review_status", "Not provided")
            last_evaluated = somatic.get("last_evaluated", "")

    # Try oncogenicity classification
    if classification == "Not provided":
        onco = variant.get("oncogenicity_classification", {})
        if isinstance(onco, dict) and onco.get("description"):
            classification = onco.get("description", "Not provided")
            review_status = onco.get("review_status", "Not provided")
            last_evaluated = onco.get("last_evaluated", "")

    # Fallback to legacy clinical_significance field
    if classification == "Not provided":
        clinical_sig = variant.get("clinical_significance", {})
        if isinstance(clinical_sig, dict) and clinical_sig.get("description"):
            classification = clinical_sig.get("description", "Not provided")
            review_status = clinical_sig.get("review_status", "Not provided")
            last_evaluated = clinical_sig.get("last_evaluated", "")

    # Get genomic location
    genes = variant.get("genes", [])
    gene_symbol = genes[0].get("symbol", "") if genes else ""

    # Get variation details
    variation_set = variant.get("variation_set", [])
    hgvs_list = []
    protein_change = ""

    if variation_set:
        var_info = variation_set[0]
        # Get HGVS expressions
        cdna_change = var_info.get("cdna_change", "")
        if cdna_change:
            hgvs_list.append(cdna_change)

        # Get protein change
        protein_change = var_info.get("protein_change", "")

    # Build title/nomenclature
    title = variant.get("title", "")
    accession = variant.get("accession", "")

    # Extract genomic location from variation_set.variation_loc
    # Prefer GRCh38 (current) assembly
    chromosome = ""
    start_pos = ""
    stop_pos = ""

    if variation_set:
        var_info = variation_set[0]
        variation_locs = var_info.get("variation_loc", [])
        for loc in variation_locs:
            if loc.get("assembly_name") == "GRCh38" or loc.get("status") == "current":
                chromosome = loc.get("chr", "")
                start_pos = loc.get("start", "")
                stop_pos = loc.get("stop", "")
                break
        # Fallback to first available location if no GRCh38
        if not chromosome and variation_locs:
            loc = variation_locs[0]
            chromosome = loc.get("chr", "")
            start_pos = loc.get("start", "")
            stop_pos = loc.get("stop", "")

    return {
        "accession": accession,
        "title": title,
        "gene": gene_symbol,
        "hgvs": "; ".join(hgvs_list) if hgvs_list else title,
        "protein_change": protein_change,
        "classification": classification,
        "review_status": review_status,
        "last_evaluated": last_evaluated,
        "chromosome": chromosome,
        "start": start_pos,
        "stop": stop_pos,
    }


def save_to_csv(variants: List[Dict[str, Any]], output_file: str):
    """Save variants to CSV file."""
    if not variants:
        print("No variants to save.")
        return

    fieldnames = [
        "accession", "title", "gene", "hgvs", "protein_change",
        "classification", "review_status", "last_evaluated",
        "chromosome", "start", "stop"
    ]

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(variants)

    print(f"Saved {len(variants)} variants to {output_file}")


def save_to_json(variants: List[Dict[str, Any]], output_file: str):
    """Save variants to JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(variants, f, indent=2)

    print(f"Saved {len(variants)} variants to {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch ClinVar variants by genomic region",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s chr20:44621004-44621201
  %(prog)s chr20:44621004-44621201 -o results.csv
  %(prog)s chr20:44621004-44621201 --format json -o results.json
        """
    )
    parser.add_argument(
        "region",
        help="Genomic region in format chr:start-end (e.g., chr20:44621004-44621201)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file (default: clinvar_variants.csv)",
        default="clinvar_variants.csv"
    )
    parser.add_argument(
        "--format",
        choices=["csv", "json"],
        default="csv",
        help="Output format (default: csv)"
    )

    args = parser.parse_args()

    # Parse region
    try:
        chrom, positions = args.region.split(":")
        start, end = positions.split("-")
        start, end = int(start), int(end)
    except ValueError:
        print(f"Error: Invalid region format '{args.region}'")
        print("Expected format: chr:start-end (e.g., chr20:44621004-44621201)")
        return 1

    # Create session with retry logic
    session = create_session()

    # Search for variants
    print(f"\nSearching ClinVar for variants in {chrom}:{start}-{end}...")
    variant_ids = search_clinvar_region(chrom, start, end, session=session)

    if not variant_ids:
        print("No variants found in this region.")
        return 0

    # Fetch details
    print(f"\nFetching details for {len(variant_ids)} variants...")
    variants = fetch_variant_details(variant_ids, session=session)

    # Save results
    if args.format == "json":
        save_to_json(variants, args.output)
    else:
        save_to_csv(variants, args.output)

    # Print summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Region: {chrom}:{start}-{end}")
    print(f"Total variants: {len(variants)}")

    # Classification breakdown
    classifications = {}
    for v in variants:
        cls = v["classification"]
        classifications[cls] = classifications.get(cls, 0) + 1

    print("\nClassification breakdown:")
    for cls, count in sorted(classifications.items(), key=lambda x: -x[1]):
        print(f"  {cls}: {count}")

    return 0


if __name__ == "__main__":
    exit(main())
