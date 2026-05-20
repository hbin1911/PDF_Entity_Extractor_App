from utils.pdf_extractor import extract_text_from_pdf

pdf_path = "data/sample.pdf"

text = extract_text_from_pdf(pdf_path)

print(text[:1000])