
import json
import re
import math
import csv
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CORPUS_FILE = BASE_DIR / "corpus.json"
QUERIES_FILE = BASE_DIR / "queries.json"
LOG_FILE = BASE_DIR / "retrieval_log.csv"


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)



def tokenize(text):
    stop_words = {
        "a", "an", "the", "is", "are", "was", "were",
        "what", "who", "where", "when", "how", "why",
        "do", "does", "did", "i", "we", "you", "they",
        "he", "she", "it", "my", "your", "our", "their",
        "for", "to", "of", "in", "on", "and", "or",
        "can", "could", "should", "would", "be", "been",
        "have", "has", "had", "with", "if", "only"
    }

    tokens = re.findall(r"\b[a-z0-9]+\b", text.lower())

    normalized = []
    for token in tokens:
        if token in stop_words:
            continue

        if token == "ill":
            token = "illness"
        elif token in {"needed", "needs"}:
            token = "need"

        normalized.append(token)

    return normalized


def build_idf(documents):
    total_docs = len(documents)
    document_frequency = Counter()

    for doc in documents:
        terms = set(tokenize(doc["title"] + " " + doc["text"]))
        document_frequency.update(terms)

    return {
        term: math.log((1 + total_docs) / (1 + frequency)) + 1
        for term, frequency in document_frequency.items()
    }


def score_document(query, document, idf):
    query_terms = Counter(tokenize(query))
    doc_terms = Counter(
        tokenize(document["title"] + " " + document["text"])
    )

    score = 0.0

    for term, query_count in query_terms.items():
        if term in doc_terms:
            score += (
                query_count
                * doc_terms[term]
                * idf.get(term, 0.0)
            )

    return score


def retrieve(query, documents, idf):
    ranked = []

    for document in documents:
        score = score_document(query, document, idf)
        ranked.append((score, document))

    ranked.sort(key=lambda item: item[0], reverse=True)

    if not ranked or ranked[0][0] <= 0:
        return None, 0.0

    return ranked[0][1], ranked[0][0]


def evaluate(queries, documents, idf):
    results = []

    for item in queries:
        predicted_doc, score = retrieve(
            item["query"], documents, idf
        )

        expected_doc = item["doc"]
        predicted_id = (
            predicted_doc["doc_id"] if predicted_doc else None
        )

        correct = predicted_id == expected_doc

        results.append({
            "query": item["query"],
            "split": item["split"],
            "expected_doc": expected_doc or "",
            "predicted_doc": predicted_id or "",
            "score": round(score, 4),
            "correct": correct,
            "evidence": item["evidence"] or ""
        })

    return results


def save_csv(results):
    fieldnames = [
        "query",
        "split",
        "expected_doc",
        "predicted_doc",
        "score",
        "correct",
        "evidence"
    ]

    with LOG_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def print_metrics(results, split_name):
    selected = [
        result for result in results
        if result["split"] == split_name
    ]

    if not selected:
        print(f"\nNo queries found for {split_name}.")
        return

    # Only questions with a known relevant document count
    # toward document-retrieval accuracy.
    answerable = [
        result for result in selected
        if result["expected_doc"]
    ]

    correct = sum(result["correct"] for result in answerable)

    accuracy = correct / len(answerable) if answerable else 0.0

    print(f"\n{split_name.upper()} RESULTS")
    print(f"Total queries: {len(selected)}")
    print(f"Answerable queries: {len(answerable)}")
    print(f"Correct document retrievals: {correct}")
    print(f"Retrieval accuracy: {accuracy:.2%}")

    no_answer = [
        result for result in selected
        if not result["expected_doc"]
    ]

    if no_answer:
        rejected = sum(
            not result["predicted_doc"] for result in no_answer
        )
        print(
            f"No-answer questions correctly rejected: "
            f"{rejected}/{len(no_answer)}"
        )


def interactive_chat(documents, idf):
    print("\nInteractive document retrieval chatbot")
    print("Type 'exit' to stop.")

    while True:
        question = input("\nYour question: ").strip()

        if question.lower() in {"exit", "quit"}:
            break

        if not question:
            print("Please enter a question.")
            continue

        document, score = retrieve(question, documents, idf)

        if document is None:
            print("No relevant document found.")
        else:
            print(f"Document: {document['title']}")
            print(f"Answer evidence: {document['text']}")
            print(f"Retrieval score: {score:.4f}")


def main():
    documents = load_json(CORPUS_FILE)
    queries = load_json(QUERIES_FILE)

    if not documents:
        raise ValueError("corpus.json contains no documents.")

    idf = build_idf(documents)
    results = evaluate(queries, documents, idf)

    print("TASK 3: DOCUMENT RETRIEVAL EVALUATION")

    for result in results:
        print(
            f"\nQuery: {result['query']}\n"
            f"Expected: {result['expected_doc'] or 'No answer'}\n"
            f"Retrieved: {result['predicted_doc'] or 'No document'}\n"
            f"Correct: {result['correct']}"
        )

    print_metrics(results, "dev")
    print_metrics(results, "test")

    save_csv(results)
    print(f"\nEvaluation log saved to: {LOG_FILE.name}")

    interactive_chat(documents, idf)


if __name__ == "__main__":
    main()