from utils.ner_engine import extract_entities


sample_text = """
Alice Smith works at Microsoft in London.
"""


def test_entities_return_list():

    entities = extract_entities(sample_text)

    assert isinstance(entities, list)


def test_entities_not_empty():

    entities = extract_entities(sample_text)

    assert len(entities) > 0


def test_person_entity_detected():

    entities = extract_entities(sample_text)

    labels = [e["label"] for e in entities]

    assert "PER" in labels