from utils.pdf_extractor import extract_text_from_pdf


def test_pdf_extraction():

    text = extract_text_from_pdf("data/sample.pdf")

    assert isinstance(text, str)


def test_pdf_not_empty():

    text = extract_text_from_pdf("data/sample.pdf")

    assert len(text) > 0


def test_pdf_contains_expected_text():

    text = extract_text_from_pdf("data/sample.pdf")

    assert "Microsoft" in text