# 🩺 Hallucination-Aware RAG for Medical Question Answering

## A Confidence-Calibrated Retrieval-Augmented Generation Framework for Hallucination Detection in Large Language Models

---

## 📖 Overview

This project presents a **Hallucination-Aware Retrieval-Augmented Generation (RAG) framework** for answering medical questions related to **Type 2 Diabetes** using trusted medical literature.

Unlike conventional LLM-based question answering systems, the proposed framework combines:

- Semantic Retrieval
- Evidence Aggregation
- Prompt Engineering
- Confidence Calibration
- Hallucination Verification

to generate trustworthy and explainable medical responses.

The system is developed as part of an **M.Tech Dissertation in Artificial Intelligence & Machine Learning**.

---

# Features

- Retrieval-Augmented Generation (RAG)
- FAISS Vector Search
- SentenceTransformer Embeddings
- Gemini LLM Integration
- Confidence Score Calculation
- Hallucination Risk Detection
- Evidence Coverage Analysis
- FastAPI Backend
- React Frontend
- Benchmark Evaluation Framework
- Performance Metrics
- Automatic Chart Generation
- GitHub Actions CI

---

# System Architecture

```
                User

                  │

          React Frontend

                  │

             FastAPI API

                  │

            RAG Pipeline

                  │

      ┌───────────┴────────────┐

      │                        │

 Retriever              Prompt Builder

      │                        │

Evidence Aggregator      Gemini LLM

      │                        │

      └───────────┬────────────┘

                  │

      Confidence Calculator

                  │

 Hallucination Verification

                  │

          Final Response
```

---

# Project Structure

```
Hallucination-Aware-RAG/

│

├── app/
│   ├── main.py
│   ├── routes.py
│   └── schemas.py
│
├── data/
│
├── evaluation/
│   ├── benchmark_questions.csv
│   ├── evaluate.py
│   └── chart_generator.py
│
├── frontend/
│
├── results/
│
├── src/
│   ├── artifacts/
│   ├── confidence/
│   ├── generation/
│   ├── pipeline/
│   ├── retrieval/
│   ├── utils/
│   ├── vectorstore/
│   └── verification/
│
├── vector_db/
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

# Technologies Used

## Backend

- Python 3.11
- FastAPI
- FAISS
- SentenceTransformers
- Google Gemini API
- NumPy
- Pandas

## Frontend

- React
- Vite
- Material UI
- Axios

## Machine Learning

- Sentence Transformers
- FAISS Vector Search
- Retrieval-Augmented Generation (RAG)

---

# Dataset

The knowledge base consists of trusted medical literature including:

- ADA Standards of Care in Diabetes
- ICMR Guidelines
- Wiley Textbook of Diabetes
- Ministry of Health Bhutan Guidelines

These documents are processed into semantic chunks and indexed using FAISS.

---

# Retrieval Pipeline

1. User enters a medical question.
2. SentenceTransformer generates embeddings.
3. FAISS retrieves the most relevant chunks.
4. Evidence Aggregator selects the best evidence.
5. Prompt Builder constructs the LLM prompt.
6. Gemini generates the response.
7. Confidence Calculator computes confidence.
8. Hallucination Verification evaluates evidence coverage.
9. Final answer is returned to the user.

---

# Confidence Calculation

The confidence score is calculated using:

- Semantic Similarity
- Source Reliability
- Document Type Weight
- Source Agreement

Each factor contributes to the overall confidence score.

---

# Hallucination Detection

The framework estimates hallucination risk using:

- Evidence Coverage
- Source Agreement
- Retrieved Context Quality

Hallucination Risk Levels:

- Very Low
- Low
- Medium
- High

---

# Evaluation

The project includes an automated evaluation framework.

Metrics generated:

- Confidence Score
- Evidence Coverage
- Hallucination Risk
- Retrieval Time
- Generation Time
- Total Latency
- Source Usage
- Category-wise Performance

Benchmark questions are located in:

```
evaluation/benchmark_questions.csv
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/Hallucination-Aware-RAG.git

cd Hallucination-Aware-RAG
```

---

Create a virtual environment.

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

Install dependencies.

```bash
pip install -r requirements.txt
```

---

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

# Running the Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Running the Frontend

Move to the frontend directory.

```bash
cd frontend
```

Install packages.

```bash
npm install
```

Run the application.

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# Running the Evaluation

Execute

```bash
python evaluation/evaluate.py
```

Generated files

```
results/

answers.csv

evaluation_report.csv

metrics.json

response_times.csv
```

---

# Generating Charts

```bash
python evaluation/chart_generator.py
```

Charts will be stored in:

```
results/charts/
```

---

# Continuous Integration

GitHub Actions automatically:

- Installs dependencies
- Runs project checks
- Validates the repository

Workflow:

```
.github/workflows/python-ci.yml
```

---

# Future Improvements

- Multi-disease knowledge base
- Multi-language support
- Hybrid Retrieval
- Knowledge Graph Integration
- Local LLM Deployment
- Clinical Decision Support Integration

---

# Author

**Raghav**

M.Tech Artificial Intelligence & Machine Learning

BITS Pilani

---

# License

This project is developed for academic and research purposes.