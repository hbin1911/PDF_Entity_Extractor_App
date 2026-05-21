import streamlit as st
import tempfile
import pandas as pd

from utils.pdf_extractor import extract_text_from_pdf
from utils.ner_engine import extract_entities
from utils.spacy_engine import extract_entities_spacy


# Page title
st.title("📄 AI-Powered PDF Entity Extractor")


# ---------------- SIDEBAR ---------------- #

st.sidebar.title("⚙ Filters & Settings")

# Model selection
model_choice = st.sidebar.selectbox(
    "Choose NER Model",
    ["BERT", "spaCy"]
)

# Entity filters
show_per = st.sidebar.checkbox("PERSON", value=True)
show_org = st.sidebar.checkbox("ORG", value=True)
show_loc = st.sidebar.checkbox("LOC", value=True)
show_date = st.sidebar.checkbox("DATE", value=True)


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

    # Select model
    if model_choice == "BERT":

        entities = extract_entities(extracted_text)

    else:

        entities = extract_entities_spacy(extracted_text)

    # Success
    st.success("PDF processed successfully!")

    # Show extracted text
    st.subheader("📜 Extracted Text Preview")

    st.text_area(
        "Raw Text",
        extracted_text,
        height=250
    )

    # Entity section
    st.subheader("🎯 Extracted Entities")

    # Colors
    colors = {
        "PER": "#FF4B4B",
        "PERSON": "#FF4B4B",

        "ORG": "#1E90FF",

        "LOC": "#32CD32",
        "GPE": "#32CD32",

        "DATE": "#FFA500"
    }

    # Filter entities
    filtered_entities = []

    for entity in entities:

        label = entity["label"]

        if label in ["PER", "PERSON"] and show_per:
            filtered_entities.append(entity)

        elif label == "ORG" and show_org:
            filtered_entities.append(entity)

        elif label in ["LOC", "GPE"] and show_loc:
            filtered_entities.append(entity)

        elif label == "DATE" and show_date:
            filtered_entities.append(entity)

        # Display entities
    for entity in filtered_entities:

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

    # ---------------- CSV EXPORT ---------------- #

    if filtered_entities:

        # Convert entities to DataFrame
        df = pd.DataFrame(filtered_entities)

        # CSV download button
        st.download_button(
            label="⬇ Download Entities as CSV",
            data=df.to_csv(index=False),
            file_name="entities_output.csv",
            mime="text/csv"
        )

