from utils.pdf_extractor import extract_text_from_pdf
from utils.ner_engine import extract_entities

import os
import pandas as pd


pdf_folder = "data"

report = []


for file in os.listdir(pdf_folder):

    if file.endswith(".pdf"):

        path = os.path.join(pdf_folder, file)

        try:

            # Extract text
            text = extract_text_from_pdf(path)

            # Extract entities
            entities = extract_entities(text)

            report.append({
                "file": file,
                "status": "Success",
                "entities_found": len(entities)
            })

        except Exception as e:

            report.append({
                "file": file,
                "status": "Failed",
                "error": str(e)
            })


df = pd.DataFrame(report)

print(df)

df.to_csv("test_report.csv", index=False)

print("Test report saved!")