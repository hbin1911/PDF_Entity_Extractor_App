"""
ner_engine.py

Module for Named Entity Recognition using Hugging Face models.
"""

from transformers import pipeline


# Load NER model
ner_pipeline = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple",
    device=-1
)


def extract_entities(text):
    """
    Extract named entities from text.

    Args:
        text (str):
            Input text.

    Returns:
        list:
            List of extracted entities.
    """

    results = ner_pipeline(text)

    entities = []

    for item in results:

        entities.append({
            "entity": item["word"],
            "label": item["entity_group"]
        })

    return entities