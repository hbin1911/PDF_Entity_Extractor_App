from utils.pdf_extractor import extract_text_from_pdf
from utils.spacy_engine import extract_entities_spacy

text = extract_text_from_pdf("test_set/pdf1.pdf")

print("TEXT:")
print(text)

print("\nENTITIES:")
print(extract_entities_spacy(text))