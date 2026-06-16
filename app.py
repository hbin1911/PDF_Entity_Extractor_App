import streamlit as st
import tempfile
import pandas as pd
import torch
import time

from openpyxl.styles import Font, Border, Side, Alignment

from utils.pdf_extractor import extract_text_from_pdf
from utils.ner_engine import extract_entities
from utils.spacy_engine import extract_entities_spacy


# ---------------- PAGE TITLE ---------------- #

st.title("📄 AI-Powered PDF Entity Extractor")


# ---------------- SIDEBAR ---------------- #

st.sidebar.title("⚙ Filters & Settings")

# Model selection
model_choice = st.sidebar.selectbox(
    "Choose NER Model",
    ["BERT", "spaCy"]
)

# Device selection
device_choice = st.sidebar.radio(
    "Select Device",
    ["CPU", "GPU"]
)

# Comparison mode
compare_mode = st.sidebar.checkbox(
    "Compare CPU vs GPU"
)

# GPU availability check
if device_choice == "GPU":

    if torch.cuda.is_available():

        st.sidebar.success(
            f"GPU Detected: {torch.cuda.get_device_name(0)}"
        )

    else:

        st.sidebar.warning(
            "GPU not detected. Running on CPU."
        )

        device_choice = "CPU"

# Entity filters
show_per = st.sidebar.checkbox("PERSON", value=True)
show_org = st.sidebar.checkbox("ORG", value=True)
show_loc = st.sidebar.checkbox("LOC", value=True)
show_date = st.sidebar.checkbox("DATE", value=True)


# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)


# ---------------- MAIN PROCESSING ---------------- #

if uploaded_file is not None:

    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:

        temp_file.write(uploaded_file.read())

        temp_path = temp_file.name

    # Extract text from PDF
    extracted_text = extract_text_from_pdf(temp_path)

    start_time = time.time()

    with st.spinner("Loading model and extracting entities..."):

        # Select NER model
        if model_choice == "BERT":

            entities = extract_entities(
                extracted_text,
                device_choice
            )

        else:

            entities = extract_entities_spacy(extracted_text)

        end_time = time.time()

        inference_time = round(
            end_time - start_time,
            2
        )

    

    # ---------------- COMPARISON PANEL ---------------- #
    if compare_mode and model_choice == "spaCy":

        st.warning(
            "⚠ spaCy model currently does not support GPU benchmarking in this application. CPU vs GPU comparison is available only for the BERT model."
        )

    comparison_results = []

    if compare_mode and model_choice == "BERT":

        # CPU Benchmark
        cpu_start = time.time()

        extract_entities(
            extracted_text,
            "CPU"
        )

        cpu_end = time.time()

        cpu_time = round(
            cpu_end - cpu_start,
            2
        )

        comparison_results.append(
            {
                "Device": "CPU",
                "Inference Time (sec)": cpu_time
            }
        )

        # GPU Benchmark
        if torch.cuda.is_available():

            gpu_start = time.time()

            extract_entities(
                extracted_text,
                "GPU"
            )

            gpu_end = time.time()

            gpu_time = round(
                gpu_end - gpu_start,
                2
            )

            comparison_results.append(
                {
                    "Device": "GPU",
                    "Inference Time (sec)": gpu_time
                }
            )

        else:

            comparison_results.append(
                {
                    "Device": "GPU",
                    "Inference Time (sec)": "Not Available"
                }
            )

    # Success message
    st.success("PDF processed successfully!")
    st.metric(
        "Inference Time",
        f"{inference_time} sec"
    )
    st.caption(
        f"Device Used: {device_choice}"
    )


    # ---------------- COMPARISON TABLE ---------------- #
    

    if compare_mode and comparison_results:

        st.subheader(
            "⚡ CPU vs GPU Comparison"
        )

        comparison_df = pd.DataFrame(
            comparison_results
        )

        st.table(
            comparison_df
        )

    # ---------------- TEXT PREVIEW ---------------- #

    st.subheader("📜 Extracted Text Preview")

    st.text_area(
        "Raw Text",
        extracted_text,
        height=250
    )

    # ---------------- ENTITY FILTERING ---------------- #

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

    # ---------------- ENTITY TABLE ---------------- #

    st.subheader("📋 Extracted Entities Table")

    if filtered_entities:

        # Convert to DataFrame
        df = pd.DataFrame(filtered_entities)

        # Rename columns
        df.columns = ["Entity", "Label"]

        # Convert values to string
        df = df.astype(str)

        # Display Streamlit table
        st.dataframe(
            df,
            use_container_width=True
        )

        # ---------------- CSV EXPORT ---------------- #

        st.download_button(
            label="⬇ Download as CSV",
            data=df.to_csv(index=False),
            file_name="entities_output.csv",
            mime="text/csv"
        )

        # ---------------- EXCEL EXPORT ---------------- #

        excel_file = "entities_output.xlsx"

        with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:

            df.to_excel(
                writer,
                index=False,
                sheet_name="Entities"
            )

            worksheet = writer.sheets["Entities"]

            worksheet.column_dimensions["A"].width = 35
            worksheet.column_dimensions["B"].width = 20

            thin_border = Border(
                left=Side(style="thin"),
                right=Side(style="thin"),
                top=Side(style="thin"),
                bottom=Side(style="thin")
            )

            for row in worksheet.iter_rows():

                for cell in row:

                    cell.border = thin_border

                    cell.alignment = Alignment(
                        horizontal="center",
                        vertical="center"
                    )

            for cell in worksheet[1]:

                cell.font = Font(bold=True)

        with open(excel_file, "rb") as file:

            st.download_button(
                label="⬇ Download as Excel",
                data=file,
                file_name="entities_output.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    else:

        st.warning("No entities found for selected filters.")