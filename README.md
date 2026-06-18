# 📄 AI-Powered PDF Entity Extractor

## Project Overview

The AI-Powered PDF Entity Extractor is a Natural Language Processing (NLP) application that automatically extracts named entities from PDF documents. The application uses Artificial Intelligence models to identify important information such as Persons, Organizations, Locations, and Dates from uploaded PDF files.

The system provides an easy-to-use web interface built with Streamlit and supports exporting extracted entities into CSV and Excel formats.

---

## Features

* Upload PDF documents
* Extract text from PDFs automatically
* Named Entity Recognition (NER)
* Support for BERT and spaCy models
* Entity filtering by category
* CPU/GPU inference selection
* CPU vs GPU comparison mode
* Export results as CSV
* Export results as Excel
* Performance benchmarking
* Web deployment using Streamlit Cloud

---

## Technologies Used

### Frontend

* Streamlit

### Backend

* Python

### AI / NLP Libraries

* Hugging Face Transformers
* spaCy
* PyTorch

### Data Processing

* Pandas
* PDFPlumber
* OpenPyXL

### Deployment

* GitHub
* Streamlit Cloud

---

## Project Structure

```text
PDF_Entity_Extractor_App/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── pdf_extractor.py
│   ├── ner_engine.py
│   └── spacy_engine.py
│
├── test_set/
│   ├── pdf1.pdf
│   ├── pdf2.pdf
│   └── labels.csv
│
├── evaluation/
│   ├── simple_evaluation.py
│   └── evaluation_report.csv
│
├── benchmark/
│   ├── benchmark_results.csv
│   └── benchmark_chart.png
│
└── tests/
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd PDF_Entity_Extractor_App
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Usage Guide

### Step 1

Launch the application.

### Step 2

Upload a PDF file.

### Step 3

Choose an NER model:

* BERT
* spaCy

### Step 4

Select processing device:

* CPU
* GPU

### Step 5

Apply entity filters:

* PERSON
* ORG
* LOC
* DATE

### Step 6

View extracted entities in tabular format.

### Step 7

Download results as:

* CSV
* Excel

---

## Evaluation

The model was evaluated using a manually labelled test dataset consisting of 10 PDF files.

Evaluation metrics:

* Precision
* Recall
* F1 Score

Sample Results:

| Entity Type | Precision | Recall | F1 Score |
| ----------- | --------- | ------ | -------- |
| PERSON      | 1.00      | 1.00   | 1.00     |
| ORG         | 1.00      | 1.00   | 1.00     |
| LOC         | 1.00      | 1.00   | 1.00     |
| DATE        | 1.00      | 1.00   | 1.00     |

---

## Benchmarking

CPU and GPU benchmarking was performed.

Metrics measured:

* Inference Time
* Memory Usage
* Accuracy

The GPU version demonstrated significantly lower inference time while maintaining equivalent accuracy.

---

## Deployment

The application has been deployed using Streamlit Cloud.

Users can access the application through a web browser without installing any software locally.

---

## Future Improvements

* Support for additional entity categories
* Multi-language PDF processing
* OCR support for scanned PDFs
* Advanced visualization dashboard
* Database integration

---

## Author

Rajas Mulik

MCA Student

AI & NLP Internship Project
