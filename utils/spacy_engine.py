import spacy

try:
    nlp = spacy.load("en_core_web_sm")

except Exception:
    raise Exception(
        "spaCy model 'en_core_web_sm' is not installed."
    )


def extract_entities_spacy(text):

    doc = nlp(text)

    entities = []

    for ent in doc.ents:

        entities.append({
            "entity": ent.text,
            "label": ent.label_
        })

    return entities