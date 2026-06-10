#!/usr/bin/env python3
"""
Paper Fetcher - Extract raw verbatim content from PubMed/PMC articles.

Usage:
    # Preview metadata only (lightweight)
    python paper_fetcher.py <pmid> [pmid2 ...] --metadata-only

    # Fetch full content
    python paper_fetcher.py <pmid> [pmid2 ...] --output-dir <dir>

Examples:
    # Preview what's available before heavy scraping
    python paper_fetcher.py 30128536 27720647 --metadata-only

    # Fetch full content for selected articles
    python paper_fetcher.py 30128536 --output-dir ./papers
"""

import argparse
import os
import re
import sys
import time
from dataclasses import dataclass, field
from typing import Optional, List, Dict

import requests
from bs4 import BeautifulSoup, Tag


@dataclass
class ArticleData:
    """Container for article data."""
    pmid: str
    pmcid: Optional[str] = None
    doi: Optional[str] = None
    title: str = ""
    authors: List[str] = field(default_factory=list)
    journal: str = ""
    year: str = ""
    abstract: str = ""
    keywords: List[str] = field(default_factory=list)
    sections: List[Dict[str, str]] = field(default_factory=list)
    tables: List[Dict[str, str]] = field(default_factory=list)
    figures: List[Dict[str, str]] = field(default_factory=list)
    references: List[str] = field(default_factory=list)
    has_full_text: bool = False
    error: Optional[str] = None


class PubMedScraper:
    """Scrape article metadata and abstract from PubMed."""

    BASE_URL = "https://pubmed.ncbi.nlm.nih.gov"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }

    def fetch(self, pmid: str) -> ArticleData:
        """Fetch article data from PubMed."""
        article = ArticleData(pmid=pmid)
        url = f"{self.BASE_URL}/{pmid}/"

        try:
            response = requests.get(url, headers=self.HEADERS, timeout=30)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            article.title = self._get_title(soup)
            article.authors = self._get_authors(soup)
            article.journal = self._get_journal(soup)
            article.year = self._get_year(soup)
            article.doi = self._get_doi(soup)
            article.pmcid = self._get_pmcid(soup)
            article.abstract = self._get_abstract(soup)
            article.keywords = self._get_keywords(soup)

        except requests.exceptions.RequestException as e:
            article.error = f"Failed to fetch PubMed: {str(e)}"

        return article

    def _get_title(self, soup: BeautifulSoup) -> str:
        """Extract article title."""
        title_elem = soup.find('h1', class_='heading-title')
        if title_elem:
            return title_elem.get_text(strip=True)
        return ""

    def _get_authors(self, soup: BeautifulSoup) -> List[str]:
        """Extract author names."""
        authors = []
        authors_div = soup.find('div', class_='authors-list')
        if authors_div:
            for author in authors_div.find_all('a', class_='full-name'):
                authors.append(author.get_text(strip=True))
        return authors

    def _get_journal(self, soup: BeautifulSoup) -> str:
        """Extract journal name."""
        journal_elem = soup.find('button', class_='journal-actions-trigger')
        if journal_elem:
            return journal_elem.get_text(strip=True)
        # Fallback
        cit = soup.find('span', class_='cit')
        if cit:
            return cit.get_text(strip=True).split('.')[0]
        return ""

    def _get_year(self, soup: BeautifulSoup) -> str:
        """Extract publication year."""
        cit = soup.find('span', class_='cit')
        if cit:
            text = cit.get_text(strip=True)
            match = re.search(r'(\d{4})', text)
            if match:
                return match.group(1)
        return ""

    def _get_doi(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract DOI."""
        doi_elem = soup.find('a', class_='id-link', attrs={'data-ga-action': 'DOI'})
        if doi_elem:
            return doi_elem.get_text(strip=True)
        return None

    def _get_pmcid(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract PMCID if available."""
        pmc_link = soup.find('a', class_='id-link', attrs={'data-ga-action': 'PMCID'})
        if pmc_link:
            text = pmc_link.get_text(strip=True)
            match = re.search(r'PMC\d+', text)
            if match:
                return match.group(0)
        return None

    def _get_abstract(self, soup: BeautifulSoup) -> str:
        """Extract raw abstract text."""
        abstract_div = soup.find('div', class_='abstract-content')
        if not abstract_div:
            # Try alternative selectors
            abstract_div = soup.find('div', id='abstract')
            if abstract_div:
                abstract_div = abstract_div.find('div', class_='abstract-content')

        if abstract_div:
            # Handle structured abstracts (with headings like BACKGROUND, METHODS, etc.)
            parts = []
            for child in abstract_div.children:
                if isinstance(child, Tag):
                    if child.name == 'strong':
                        # Section heading
                        parts.append(f"\n**{child.get_text(strip=True)}**\n")
                    elif child.name == 'p':
                        parts.append(child.get_text(strip=True))
                    else:
                        text = child.get_text(strip=True)
                        if text:
                            parts.append(text)

            if parts:
                return '\n'.join(parts).strip()

            # Fallback to simple text extraction
            return abstract_div.get_text(strip=True)

        return ""

    def _get_keywords(self, soup: BeautifulSoup) -> List[str]:
        """Extract keywords."""
        keywords = []
        kw_section = soup.find('div', class_='keywords-section')
        if kw_section:
            for kw in kw_section.find_all('button', class_='keyword-actions-trigger'):
                keywords.append(kw.get_text(strip=True))
        return keywords


class PMCScraper:
    """Scrape full article content from PMC."""

    BASE_URL = "https://pmc.ncbi.nlm.nih.gov/articles"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }

    def fetch(self, pmcid: str, article: ArticleData) -> ArticleData:
        """Fetch full article from PMC and update ArticleData."""
        url = f"{self.BASE_URL}/{pmcid}/"

        try:
            response = requests.get(url, headers=self.HEADERS, timeout=30)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Update with PMC data (may have more complete info)
            pmc_abstract = self._get_abstract(soup)
            if pmc_abstract and len(pmc_abstract) > len(article.abstract):
                article.abstract = pmc_abstract

            article.keywords = self._get_keywords(soup) or article.keywords
            article.sections = self._get_sections(soup)
            article.tables = self._get_tables(soup)
            article.figures = self._get_figures(soup)
            article.references = self._get_references(soup)
            article.has_full_text = bool(article.sections)

        except requests.exceptions.RequestException as e:
            # Don't overwrite existing error, just note PMC failed
            if not article.error:
                article.error = f"PubMed OK, but PMC fetch failed: {str(e)}"

        return article

    def _get_abstract(self, soup: BeautifulSoup) -> str:
        """Extract abstract from PMC."""
        abstract_section = soup.find('section', class_='abstract')
        if abstract_section:
            # Remove heading
            heading = abstract_section.find(['h2', 'h3'])
            if heading:
                heading.decompose()

            parts = []
            for elem in abstract_section.find_all(['p', 'h4', 'strong']):
                if elem.name in ['h4', 'strong']:
                    parts.append(f"\n**{elem.get_text(strip=True)}**\n")
                else:
                    parts.append(elem.get_text(strip=True))

            if parts:
                return '\n'.join(parts).strip()
            return abstract_section.get_text(strip=True)
        return ""

    def _get_keywords(self, soup: BeautifulSoup) -> List[str]:
        """Extract keywords from PMC."""
        keywords = []
        kw_section = soup.find('section', class_='kwd-group')
        if kw_section:
            for kw in kw_section.find_all('span', class_='kwd'):
                keywords.append(kw.get_text(strip=True))
        return keywords

    def _get_sections(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        """Extract article sections."""
        sections = []

        # Find article element
        article = soup.find('article')
        if not article:
            article = soup

        # Try multiple patterns for section IDs
        section_patterns = [
            r'^(sec|s)\d+',           # sec1, sec2, s1, s2
            r'^H\d+-\d+',              # H1-1-XXX (JAMA style)
            r'^(introduction|methods|results|discussion|conclusion)',  # Named sections
        ]

        found_sections = set()
        for pattern in section_patterns:
            for section in article.find_all('section', id=re.compile(pattern, re.IGNORECASE)):
                if section not in found_sections:
                    section_data = self._extract_section(section)
                    if section_data['title'] or section_data['content']:
                        sections.append(section_data)
                        found_sections.add(section)

        # If still no sections, try finding by heading content
        if not sections:
            for heading in article.find_all(['h2', 'h3'], class_=re.compile(r'(title|head)')):
                text = heading.get_text(strip=True).lower()
                if any(kw in text for kw in ['introduction', 'method', 'result', 'discussion', 'conclusion', 'background']):
                    parent_section = heading.find_parent('section')
                    if parent_section and parent_section not in found_sections:
                        section_data = self._extract_section(parent_section)
                        if section_data['title'] or section_data['content']:
                            sections.append(section_data)
                            found_sections.add(parent_section)

        # Fallback: look for div.body or any main content area
        if not sections:
            body = soup.find('div', class_='body')
            if body:
                for section in body.find_all('section', recursive=False):
                    section_data = self._extract_section(section)
                    if section_data['title'] or section_data['content']:
                        sections.append(section_data)

        return sections

    def _extract_section(self, section: Tag) -> Dict[str, str]:
        """Extract content from a section element."""
        # Make a copy to avoid modifying original
        section_copy = BeautifulSoup(str(section), 'html.parser').find('section') or section

        # Get title
        title = ""
        heading = section_copy.find(['h2', 'h3', 'h4', 'h5'])
        if heading:
            title = heading.get_text(strip=True)
            heading.decompose()

        # Get all paragraphs (including nested)
        paragraphs = []

        # Direct paragraphs
        for p in section_copy.find_all('p'):
            text = self._clean_text(p)
            if text and len(text) > 20:  # Skip very short fragments
                paragraphs.append(text)

        # If no paragraphs found, try getting all text
        if not paragraphs:
            # Remove nested sections to avoid duplication
            for nested in section_copy.find_all('section'):
                nested.decompose()
            text = section_copy.get_text(strip=True)
            text = re.sub(r'\s+', ' ', text)
            if text and len(text) > 50:
                paragraphs.append(text)

        return {
            'title': title,
            'content': '\n\n'.join(paragraphs)
        }

    def _clean_text(self, elem: Tag) -> str:
        """Clean text from element, handling inline formatting."""
        # Replace em/i/b/strong with text
        for tag in elem.find_all(['em', 'i', 'b', 'strong', 'sup', 'sub']):
            tag.replace_with(f" {tag.get_text()} ")

        # Remove citation links but keep text readable
        for xref in elem.find_all('a', class_='xref-bibr'):
            xref.replace_with(f"[{xref.get_text()}]")

        text = elem.get_text()
        # Clean up whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def _get_tables(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        """Extract tables."""
        tables = []

        for table_wrap in soup.find_all(['div', 'section'], class_=re.compile(r'(table-wrap|tw)')):
            table_data = {
                'id': table_wrap.get('id', ''),
                'title': '',
                'caption': '',
                'content': ''
            }

            # Get title
            title_elem = table_wrap.find(['h3', 'h4', 'strong'], class_=re.compile(r'(title|label|head)'))
            if title_elem:
                table_data['title'] = title_elem.get_text(strip=True)

            # Get caption
            caption_elem = table_wrap.find(['figcaption', 'div', 'p'], class_=re.compile(r'caption'))
            if caption_elem:
                table_data['caption'] = caption_elem.get_text(strip=True)

            # Convert table to text
            table_elem = table_wrap.find('table')
            if table_elem:
                table_data['content'] = self._table_to_markdown(table_elem)

            if table_data['title'] or table_data['content']:
                tables.append(table_data)

        return tables

    def _table_to_markdown(self, table: Tag) -> str:
        """Convert HTML table to markdown."""
        rows = []

        # Get header
        thead = table.find('thead')
        if thead:
            header_cells = []
            for cell in thead.find_all(['th', 'td']):
                header_cells.append(cell.get_text(strip=True))
            if header_cells:
                rows.append('| ' + ' | '.join(header_cells) + ' |')
                rows.append('| ' + ' | '.join(['---'] * len(header_cells)) + ' |')

        # Get body
        tbody = table.find('tbody') or table
        for tr in tbody.find_all('tr'):
            cells = []
            for cell in tr.find_all(['th', 'td']):
                cells.append(cell.get_text(strip=True).replace('|', '\\|'))
            if cells:
                rows.append('| ' + ' | '.join(cells) + ' |')

        return '\n'.join(rows)

    def _get_figures(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        """Extract figures and captions."""
        figures = []

        for fig in soup.find_all(['figure', 'div'], class_=re.compile(r'fig')):
            fig_data = {
                'id': fig.get('id', ''),
                'title': '',
                'caption': ''
            }

            title_elem = fig.find(['h3', 'h4', 'strong'], class_=re.compile(r'(title|label|head)'))
            if title_elem:
                fig_data['title'] = title_elem.get_text(strip=True)

            caption_elem = fig.find('figcaption')
            if caption_elem:
                fig_data['caption'] = caption_elem.get_text(strip=True)

            if fig_data['title'] or fig_data['caption']:
                figures.append(fig_data)

        return figures

    def _get_references(self, soup: BeautifulSoup) -> List[str]:
        """Extract references."""
        references = []

        ref_section = soup.find('section', class_='ref-list')
        if ref_section:
            for ref in ref_section.find_all('li'):
                text = ref.get_text(strip=True)
                text = re.sub(r'\s+', ' ', text)  # Clean whitespace
                if text:
                    references.append(text)

        return references


class PaperFetcher:
    """Main class to fetch papers by PMID."""

    def __init__(self):
        self.pubmed = PubMedScraper()
        self.pmc = PMCScraper()

    def fetch_metadata(self, pmid: str) -> ArticleData:
        """Fetch only metadata and abstract from PubMed (lightweight)."""
        return self.pubmed.fetch(pmid)

    def fetch_metadata_multiple(self, pmids: List[str], delay: float = 0.3) -> List[ArticleData]:
        """Fetch metadata only for multiple articles (lightweight preview)."""
        results = []

        for i, pmid in enumerate(pmids):
            pmid = pmid.strip()
            if not pmid:
                continue

            print(f"[{i+1}/{len(pmids)}] Fetching metadata for PMID {pmid}...", file=sys.stderr)

            article = self.fetch_metadata(pmid)
            results.append(article)

            if article.error:
                print(f"  Error: {article.error}", file=sys.stderr)
            else:
                pmc_status = "PMC available" if article.pmcid else "No PMC"
                print(f"  {article.title[:50]}... [{pmc_status}]", file=sys.stderr)

            # Rate limiting (shorter delay for metadata-only)
            if i < len(pmids) - 1:
                time.sleep(delay)

        return results

    def fetch(self, pmid: str) -> ArticleData:
        """Fetch article by PMID (metadata + full text if available)."""
        # Step 1: Get metadata and abstract from PubMed
        article = self.pubmed.fetch(pmid)

        if article.error:
            return article

        # Step 2: If PMCID exists, get full text from PMC
        if article.pmcid:
            article = self.pmc.fetch(article.pmcid, article)

        return article

    def fetch_multiple(self, pmids: List[str], delay: float = 0.5) -> List[ArticleData]:
        """Fetch multiple articles with rate limiting."""
        results = []

        for i, pmid in enumerate(pmids):
            pmid = pmid.strip()
            if not pmid:
                continue

            print(f"[{i+1}/{len(pmids)}] Fetching PMID {pmid}...", file=sys.stderr)

            article = self.fetch(pmid)
            results.append(article)

            if article.error:
                print(f"  Error: {article.error}", file=sys.stderr)
            else:
                status = "FULL TEXT" if article.has_full_text else "ABSTRACT ONLY"
                print(f"  {article.title[:50]}... [{status}]", file=sys.stderr)

            # Rate limiting
            if i < len(pmids) - 1:
                time.sleep(delay)

        return results


def article_to_markdown(article: ArticleData) -> str:
    """Convert ArticleData to markdown format."""
    lines = []

    # Title
    lines.append(f"# {article.title}")
    lines.append("")

    # Metadata
    lines.append(f"**PMID:** {article.pmid}")
    if article.pmcid:
        lines.append(f"**PMCID:** {article.pmcid}")
    if article.doi:
        lines.append(f"**DOI:** {article.doi}")
    if article.authors:
        author_str = ', '.join(article.authors[:10])
        if len(article.authors) > 10:
            author_str += ' et al.'
        lines.append(f"**Authors:** {author_str}")
    if article.journal:
        lines.append(f"**Journal:** {article.journal}" + (f" ({article.year})" if article.year else ""))

    lines.append("")
    lines.append("---")
    lines.append("")

    # Keywords
    if article.keywords:
        lines.append(f"**Keywords:** {', '.join(article.keywords)}")
        lines.append("")

    # Abstract
    if article.abstract:
        lines.append("## Abstract")
        lines.append("")
        lines.append(article.abstract)
        lines.append("")

    # Full text sections
    if article.sections:
        lines.append("---")
        lines.append("")
        lines.append("## Full Text")
        lines.append("")

        for section in article.sections:
            if section['title']:
                lines.append(f"### {section['title']}")
                lines.append("")
            if section['content']:
                lines.append(section['content'])
                lines.append("")

    # Tables
    if article.tables:
        lines.append("---")
        lines.append("")
        lines.append("## Tables")
        lines.append("")

        for table in article.tables:
            if table['title']:
                lines.append(f"### {table['title']}")
            if table['caption']:
                lines.append(f"*{table['caption']}*")
            if table['content']:
                lines.append("")
                lines.append(table['content'])
            lines.append("")

    # Figures
    if article.figures:
        lines.append("---")
        lines.append("")
        lines.append("## Figures")
        lines.append("")

        for fig in article.figures:
            if fig['title']:
                lines.append(f"### {fig['title']}")
            if fig['caption']:
                lines.append(fig['caption'])
            lines.append("")

    # References
    if article.references:
        lines.append("---")
        lines.append("")
        lines.append("## References")
        lines.append("")

        for i, ref in enumerate(article.references, 1):
            lines.append(f"{i}. {ref}")
        lines.append("")

    # Footer
    if not article.has_full_text:
        lines.append("---")
        lines.append("*Full text not available in PMC. Abstract only.*")

    return '\n'.join(lines)


def save_article(article: ArticleData, output_dir: str) -> str:
    """Save article to markdown file."""
    os.makedirs(output_dir, exist_ok=True)

    filename = f"PMID_{article.pmid}.md"
    filepath = os.path.join(output_dir, filename)

    content = article_to_markdown(article)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath


def print_metadata_summary(articles: List[ArticleData]):
    """Print metadata preview summary (lightweight mode)."""
    print("\n" + "=" * 90)
    print("METADATA PREVIEW")
    print("=" * 90)

    # Table header
    print(f"\n{'PMID':<12} {'PMC':<6} {'Year':<6} {'Title':<50}")
    print("-" * 90)

    for article in articles:
        if article.error:
            print(f"{article.pmid:<12} {'ERR':<6} {'':<6} {article.error[:50]}")
            continue

        pmc = "Yes" if article.pmcid else "No"
        year = article.year or "?"
        title = article.title[:48] + ".." if len(article.title) > 50 else article.title

        print(f"{article.pmid:<12} {pmc:<6} {year:<6} {title:<50}")

    print("-" * 90)

    # Detailed info
    print("\nDETAILED METADATA:")
    print("-" * 90)

    for article in articles:
        if article.error:
            print(f"\n[PMID {article.pmid}] ERROR: {article.error}")
            continue

        print(f"\n[PMID {article.pmid}]")
        print(f"  Title:    {article.title}")
        if article.authors:
            author_str = ", ".join(article.authors[:5])
            if len(article.authors) > 5:
                author_str += f" (+{len(article.authors) - 5} more)"
            print(f"  Authors:  {author_str}")
        print(f"  Journal:  {article.journal} ({article.year})")
        if article.doi:
            print(f"  DOI:      {article.doi}")
        print(f"  PMCID:    {article.pmcid or 'Not available (no full text)'}")
        if article.keywords:
            print(f"  Keywords: {', '.join(article.keywords[:5])}")
        if article.abstract:
            abstract_preview = article.abstract[:200].replace('\n', ' ')
            if len(article.abstract) > 200:
                abstract_preview += "..."
            print(f"  Abstract: {abstract_preview}")

    # Summary stats
    print("\n" + "=" * 90)
    total = len(articles)
    found = sum(1 for a in articles if not a.error)
    with_pmc = sum(1 for a in articles if a.pmcid)
    with_abstract = sum(1 for a in articles if a.abstract)

    print(f"Total: {total} | Found: {found} | With PMC (full text available): {with_pmc} | With abstract: {with_abstract}")
    print("=" * 90)

    if with_pmc > 0:
        pmc_pmids = [a.pmid for a in articles if a.pmcid]
        print(f"\nTo fetch full content for articles with PMC:")
        print(f"  python paper_fetcher.py {' '.join(pmc_pmids)} --output-dir ./papers")


def print_summary(articles: List[ArticleData], filepaths: List[str]):
    """Print summary of fetched articles."""
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    for article, filepath in zip(articles, filepaths):
        status = "FOUND" if not article.error else "ERROR"
        content = "FULL TEXT" if article.has_full_text else "ABSTRACT ONLY"
        if article.error:
            content = article.error[:40]

        title = article.title[:45] + "..." if len(article.title) > 45 else article.title

        print(f"\nPMID {article.pmid}: {status}")
        print(f"  Title: {title}")
        print(f"  Content: {content}")
        if filepath:
            print(f"  File: {filepath}")

    print("\n" + "=" * 70)
    total = len(articles)
    found = sum(1 for a in articles if not a.error)
    full_text = sum(1 for a in articles if a.has_full_text)
    print(f"Total: {total} | Found: {found} | Full text: {full_text} | Abstract only: {found - full_text}")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch PubMed articles and extract raw content",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Preview metadata only (lightweight, fast)
  python paper_fetcher.py 30128536 27720647 --metadata-only

  # Fetch full content and save to files
  python paper_fetcher.py 30128536 --output-dir ./papers

Workflow:
  1. Use --metadata-only to preview available articles
  2. Review the output to see which have PMC full text
  3. Run again without --metadata-only for selected PMIDs
        """
    )
    parser.add_argument(
        'pmids',
        nargs='+',
        help="One or more PMIDs to fetch"
    )
    parser.add_argument(
        '--metadata-only', '-m',
        action='store_true',
        help="Fetch only metadata and abstract (lightweight preview, no full text scraping)"
    )
    parser.add_argument(
        '--output-dir', '-o',
        default='./papers',
        help="Output directory for saved papers (default: ./papers)"
    )
    parser.add_argument(
        '--delay', '-d',
        type=float,
        default=None,
        help="Delay between requests in seconds (default: 0.3 for metadata, 0.5 for full)"
    )

    args = parser.parse_args()

    fetcher = PaperFetcher()

    if args.metadata_only:
        # Lightweight metadata-only mode
        delay = args.delay if args.delay is not None else 0.3
        articles = fetcher.fetch_metadata_multiple(args.pmids, delay=delay)
        print_metadata_summary(articles)
    else:
        # Full content mode
        delay = args.delay if args.delay is not None else 0.5
        articles = fetcher.fetch_multiple(args.pmids, delay=delay)

        filepaths = []
        for article in articles:
            if not article.error:
                filepath = save_article(article, args.output_dir)
                filepaths.append(filepath)
            else:
                filepaths.append(None)

        print_summary(articles, filepaths)


if __name__ == "__main__":
    main()
