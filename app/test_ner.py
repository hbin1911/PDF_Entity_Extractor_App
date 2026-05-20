from utils.pdf_extractor import extract_text_from_pdf
from utils.ner_engine import extract_entities


pdf_path = "data/sample.pdf"

text = extract_text_from_pdf(pdf_path)

entities = extract_entities(text)

print(entities)