
# AI Lab 6: Document Retrieval Chatbot

## Overview

This project demonstrates text tokenization, document chunking, and keyword-based document retrieval.

## Project Files

- `task1_tokens.py` - Tokenization and FAQ chatbot.
- `task2_chunks.py` - Word-based and sentence-aware chunking.
- `corpus.json` - Collection of documents.
- `queries.json` - Development and test queries.
- `task3_retrieval.py` - Document retrieval and evaluation.
- `retrieval_log.csv` - Saved retrieval evaluation results.
- `requirements.txt` - Project dependency information.

## Requirements

Python 3.14 or another compatible Python 3 version.

The current implementation uses Python standard-library modules.

## How to Run

Run Task 1:

```bash
python task1_tokens.py
```

Run Task 2:

```bash
python task2_chunks.py
```

Run Task 3:

```bash
python task3_retrieval.py
```

Task 3 reads `corpus.json` and `queries.json`, evaluates retrieval results, saves `retrieval_log.csv`, and starts an interactive chatbot.

## Evaluation

The initial dataset contains five documents and ten queries. The queries include answerable questions and questions without a relevant document.

The initial retrieval evaluation achieved 100% accuracy on the four answerable development queries and 100% accuracy on the four answerable test queries. Both no-answer test queries were correctly rejected after improving tokenization.

## Limitations

The current retriever uses keyword overlap and inverse document frequency. It does not yet use semantic embeddings, so questions phrased very differently from the stored documents may not retrieve the best result.