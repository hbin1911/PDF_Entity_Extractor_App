"""
pdf_extractor.py

Module for extracting text from PDF documents.
"""

import pdfplumber


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.

    Args:
        pdf_path (str):
            Path to the PDF document.

    Returns:
        str:
            Extracted text from all pages.
    """

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    return text