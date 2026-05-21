import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")


def extract_entities_spacy(text):

    doc = nlp(text)

    entities = []

    for ent in doc.ents:

        entities.append({
            "entity": ent.text,
            "label": ent.label_
        })

    return entities