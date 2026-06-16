import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)



import pandas as pd


from utils.pdf_extractor import extract_text_from_pdf
from utils.spacy_engine import extract_entities_spacy

# Load ground truth labels
labels_df = pd.read_csv("test_set/labels.csv")

entity_types = ["PERSON", "ORG", "LOC", "DATE"]

results = []

for entity_type in entity_types:

    total_expected = 0
    total_found = 0
    correct = 0

    for pdf_name in labels_df["PDF"].unique():

        pdf_path = f"test_set/{pdf_name}.pdf"

        text = extract_text_from_pdf(pdf_path)

        predictions = extract_entities_spacy(text)

        # Normalize GPE -> LOC
        predicted_entities = []

        for p in predictions:

            label = p["label"]

            if label == "GPE":
                label = "LOC"

            predicted_entities.append(
                (
                    p["entity"].strip().lower(),
                    label
                )
            )

        gold_entities = labels_df[
            (labels_df["PDF"] == pdf_name)
            &
            (labels_df["Label"] == entity_type)
        ]

        total_expected += len(gold_entities)

        for _, row in gold_entities.iterrows():

            gold_entity = row["Entity"].strip().lower()

            if (gold_entity, entity_type) in predicted_entities:

                correct += 1

        for entity, label in predicted_entities:

            if label == entity_type:

                total_found += 1

    precision = (
        correct / total_found
        if total_found > 0
        else 0
    )

    recall = (
        correct / total_expected
        if total_expected > 0
        else 0
    )

    f1 = (
        2 * precision * recall /
        (precision + recall)
        if precision + recall > 0
        else 0
    )

    results.append(
        {
            "Entity Type": entity_type,
            "Precision": round(precision, 2),
            "Recall": round(recall, 2),
            "F1 Score": round(f1, 2)
        }
    )

report_df = pd.DataFrame(results)

print(report_df)

report_df.to_csv(
    "evaluation/evaluation_report.csv",
    index=False
)

print("\nEvaluation report saved successfully.")