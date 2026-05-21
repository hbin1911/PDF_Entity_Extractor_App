import streamlit as st
import tempfile

from utils.pdf_extractor import extract_text_from_pdf
from utils.ner_engine import extract_entities


# Streamlit page title
st.title("📄 AI-Powered PDF Entity Extractor")


# Upload PDF
uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)


if uploaded_file is not None:

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:

        temp_file.write(uploaded_file.read())

        temp_path = temp_file.name

    # Extract text
    extracted_text = extract_text_from_pdf(temp_path)

    # Extract entities
    entities = extract_entities(extracted_text)

    # Success message
    st.success("PDF processed successfully!")

    # Show extracted text
    st.subheader("📜 Extracted Text Preview")

    st.text_area(
        "Raw Text",
        extracted_text,
        height=250
    )

    # Show entities
    st.subheader("🎯 Extracted Entities")

    # Color mapping
    colors = {
        "PER": "#FF4B4B",
        "ORG": "#1E90FF",
        "LOC": "#32CD32",
        "DATE": "#FFA500"
    }

    # Display highlighted entities
    for entity in entities:

        label = entity["label"]
        word = entity["entity"]

        color = colors.get(label, "#808080")

        st.markdown(
            f"""
            <span style="
                background-color:{color};
                padding:6px;
                border-radius:6px;
                color:white;
                margin-right:5px;
                display:inline-block;
            ">
                {word} ({label})
            </span>
            """,
            unsafe_allow_html=True
        )