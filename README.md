# LLM-Based Text Summarization Application

## Overview

This project presents an end-to-end text summarization application built using a pretrained transformer model via the HuggingFace Inference API. The system allows users to input long-form text and generate concise summaries at varying levels of detail (Short, Medium, Detailed).

The application is designed with a focus on practical understanding of LLM-based workflows, prompt engineering, API integration, and evaluation using standard NLP metrics.

---

## Features

* Text summarization using a pretrained BART model
* Multiple summary levels: Short, Medium, Detailed
* Chunk-based processing for long inputs
* Two-stage summarization pipeline for improved coherence
* Streamlit-based user interface
* Copy-friendly output display
* Evaluation using ROUGE and BLEU metrics

---

## How It Works

### 1. Input Processing

* User enters text via the Streamlit interface
* Input is split into smaller chunks to handle long sequences

### 2. First Pass Summarization

* Each chunk is summarized independently using the BART model
* Ensures extraction of key information from all parts of the input

### 3. Second Pass Refinement

* Combined summaries are rewritten using prompt-based refinement
* Improves coherence and readability

### 4. Output Generation

* Final summary is displayed in the UI based on the selected summary type

---

## Evaluation

The generated summaries are evaluated using:

* ROUGE-1, ROUGE-2, ROUGE-L
* BLEU score

Evaluation is performed by comparing generated summaries with reference summaries using the evaluation script.

---

## Sample Results

| Metric  | Score Range |
| ------- | ----------- |
| ROUGE-1 | 0.60 – 0.66 |
| ROUGE-2 | 0.58 – 0.62 |
| ROUGE-L | 0.57 – 0.61 |
| BLEU    | 0.23 – 0.36 |

These results indicate strong content overlap and coherence, with moderate abstraction.

---

## Key Learnings

* Understanding limitations of extractive summarization models
* Designing multi-stage NLP pipelines
* Handling API-based model inference
* Improving output quality using prompt engineering
* Evaluating NLP systems using standard metrics

---

## Limitations

* Model tends to produce partially extractive summaries
* Output quality depends on API availability and latency
* Limited abstraction compared to instruction-tuned models
