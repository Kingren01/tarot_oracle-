"""PDF generation for Agilisium Competitive Intelligence reports.

Uses only the built-in Helvetica font (Latin-1 subset), so all incoming
text must be stripped to printable ASCII before rendering.
"""
import unicodedata
from fpdf import FPDF


# --------------------------------------------------------------------------- #
#  Text sanitization — guarantee pure ASCII output                            #
# --------------------------------------------------------------------------- #

_REPLACEMENTS = {
    # Common typographic characters that are NOT in ASCII
    "\u2013": "-",   # en-dash
    "\u2014": "-",   # em-dash
    "\u2012": "-",   # figure dash
    "\u2015": "-",   # horizontal bar
    "\u2212": "-",   # minus sign
    "\u2018": "'",   # left single quote
    "\u2019": "'",   # right single quote / apostrophe
    "\u201a": ",",   # single low-9 quotation mark
    "\u201c": '"',   # left double quote
    "\u201d": '"',   # right double quote
    "\u201e": '"',   # double low-9 quotation mark
    "\u2026": "...", # horizontal ellipsis
    "\u2022": "*",   # bullet
    "\u00b7": "*",   # middle dot
    "\u2122": "(TM)",
    "\u00ae": "(R)",
    "\u00a9": "(c)",
    "\u00a0": " ",   # non-breaking space
    "\u00ad": "-",   # soft hyphen
}


def sanitize_text(text: str) -> str:
    """Return a clean ASCII string safe for Helvetica / Latin-1 FPDF."""
    if not isinstance(text, str):
        text = str(text) if text is not None else ""

    # Step 1: explicit replacements for common problem characters
    for bad, good in _REPLACEMENTS.items():
        text = text.replace(bad, good)

    # Step 2: NFKD decomposition (converts accented letters to base + combining)
    text = unicodedata.normalize("NFKD", text)

    # Step 3: nuclear option — encode to ASCII, replace anything that fails
    text = text.encode("ascii", errors="replace").decode("ascii")

    return text


# --------------------------------------------------------------------------- #
#  PDF document class                                                          #
# --------------------------------------------------------------------------- #

class DisplacementPDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        self.cell(0, 10, "Agilisium Competitive Intelligence Report", 0, 1, "C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")


def _section(pdf: FPDF, heading: str, body: str) -> None:
    """Write a heading + body block to the PDF."""
    pdf.set_font("helvetica", "B", 14)
    pdf.cell(0, 10, sanitize_text(heading), 0, 1)
    pdf.set_font("helvetica", "", 11)
    pdf.multi_cell(0, 7, sanitize_text(body))
    pdf.ln(5)


# --------------------------------------------------------------------------- #
#  Public API                                                                  #
# --------------------------------------------------------------------------- #

def generate_displacement_pdf(
    account_name: str,
    competitor_name: str,
    pdf_data: dict,
) -> bytes:
    """Generate a PDF report and return it as a bytes object."""
    pdf = DisplacementPDF()
    pdf.add_page()

    # Cover info
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 10, sanitize_text(f"Target: {account_name}"), 0, 1)
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, sanitize_text(f"Incumbent: {competitor_name}"), 0, 1)
    pdf.ln(10)

    # Section order
    sections = [
        ("Table of Contents",       pdf_data.get("table_of_contents", "")),
        ("Executive Summary",       pdf_data.get("executive_summary", "")),
        ("Detailed Findings",       pdf_data.get("detailed_findings", "")),
        ("Solution Mapping",        pdf_data.get("solution_mapping", "")),
        ("Implementation Roadmap",  pdf_data.get("implementation_roadmap", "")),
        ("Methodology",             pdf_data.get("methodology", "")),
        ("Appendices",              pdf_data.get("appendices", "")),
    ]

    for heading, body in sections:
        if body:
            _section(pdf, heading, body)

    raw = pdf.output(dest="S")
    return bytes(raw) if not isinstance(raw, bytes) else raw
