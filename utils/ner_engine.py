"""
ner_engine.py

Module for Named Entity Recognition using Hugging Face models.
"""

from transformers import pipeline
import torch
import streamlit as st

@st.cache_resource
def load_model(device_choice):
    """
    Load NER model on selected device.
    """

    if device_choice == "GPU" and torch.cuda.is_available():

        device = 0

    else:

        device = -1

    ner_pipeline = pipeline(
        "ner",
        model="dslim/bert-base-NER",
        aggregation_strategy="simple",
        device=device
    )

    return ner_pipeline


def extract_entities(text, device_choice):
    """
    Extract named entities from text.

    Args:
        text (str):
            Input text.

        device_choice (str):
            CPU or GPU

    Returns:
        list:
            List of extracted entities.
    """

    ner_pipeline = load_model(device_choice)

    results = ner_pipeline(text)

    entities = []

    for item in results:

        entities.append({
            "entity": item["word"],
            "label": item["entity_group"]
        })

    return entities