
import time
from task2_chunks import make_demo_docs, make_chunks
from lab6_search import Retriever, show_hits


def main():
    docs = make_demo_docs()

    queries = [
        "How can I get extra time when I am sick?",
        "How can I regain access after losing my login password?",
        "What should I do if my printer produces empty pages?"
    ]

    # Sentence-aware chunks ko pehle baseline ke taur par test karte hain.
    records = make_chunks(docs, "sentence")

    print("TASK 2: TF-IDF VS REAL SENTENCE EMBEDDINGS")
    print("Chunk count:", len(records))

    for backend in ("tfidf", "embedding"):
        print("\n" + "=" * 55)
        print("BACKEND:", backend)

        start = time.perf_counter()
        engine = Retriever(records, backend)
        setup_seconds = time.perf_counter() - start

        print(f"Setup/encoding seconds: {setup_seconds:.4f}")

        for query in queries:
            print("\nQuery:", query)
            hits = engine.search(query, k=3)
            show_hits(hits)

    print("\nSemantic comparison finished.")


if __name__ == "__main__":
    main()