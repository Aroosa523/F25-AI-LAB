
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer


class Retriever:
    def __init__(self, records, backend="tfidf"):
        self.records = records
        self.backend = backend

        self.texts = [record["text"] for record in records]

        if not self.texts:
            raise ValueError("No chunk records provided.")

        if backend == "tfidf":
            self.vectorizer = TfidfVectorizer()
            self.chunk_vectors = self.vectorizer.fit_transform(
                self.texts
            )

        elif backend == "embedding":
            self.model = SentenceTransformer(
                "sentence-transformers/all-MiniLM-L6-v2",
                device="cpu"
            )
            self.chunk_vectors = self.model.encode(
                self.texts,
                normalize_embeddings=True
            )

        else:
            raise ValueError(
                "Backend must be 'tfidf' or 'embedding'."
            )

    def search(self, query, k=3):
        if not query.strip():
            return []

        if self.backend == "tfidf":
            query_vector = self.vectorizer.transform([query])
            scores = (
                query_vector @ self.chunk_vectors.T
            ).toarray()[0]

        else:
            query_vector = self.model.encode(
                [query],
                normalize_embeddings=True
            )
            scores = (
                query_vector @ self.chunk_vectors.T
            )[0]

        indices = np.argsort(-scores, kind="stable")[:k]

        return [
            (self.records[i], float(scores[i]))
            for i in indices
            if scores[i] > 0
        ]


def show_hits(hits):
    for rank, (record, score) in enumerate(hits, start=1):
        print(f"\nRank {rank}")
        print(f"Chunk ID: {record.get('id', 'unknown')}")
        print(f"Document: {record.get('doc', 'unknown')}")
        print(f"Score: {score:.4f}")
        print(f"Offsets: {record.get('start')} - {record.get('end')}")
        print(f"Evidence: {record['text']}")