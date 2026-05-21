import streamlit as st
import tempfile

from utils.pdf_extractor import extract_text_from_pdf


# Page title
st.title("📄 AI-Powered PDF Entity Extractor")


# Upload PDF
uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)


# Process uploaded file
if uploaded_file is not None:

    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:

        temp_file.write(uploaded_file.read())

        temp_path = temp_file.name

    # Extract text
    extracted_text = extract_text_from_pdf(temp_path)

    # Display success message
    st.success("PDF processed successfully!")

    # Show extracted text
    st.subheader("📜 Extracted Text Preview")

    st.text_area(
        "Raw Text",
        extracted_text,
        height=300
    )