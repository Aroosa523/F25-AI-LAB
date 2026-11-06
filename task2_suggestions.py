
import re
import math
from collections import Counter


def tokenize(text):
    return re.findall(r"\b[a-z0-9]+\b", text.lower())


def build_tfidf(texts):
    tokenized = [tokenize(text) for text in texts]
    total_docs = len(texts)
    document_frequency = Counter()

    for tokens in tokenized:
        document_frequency.update(set(tokens))

    vectors = []

    for tokens in tokenized:
        counts = Counter(tokens)
        vector = {}

        for word, count in counts.items():
            tf = count / len(tokens) if tokens else 0

            idf = math.log(
                (1 + total_docs) /
                (1 + document_frequency[word])
            ) + 1

            vector[word] = tf * idf

        vectors.append(vector)

    return vectors


def cosine_similarity(first, second):
    common = set(first) & set(second)

    dot_product = sum(
        first[word] * second[word] for word in common
    )

    norm_first = math.sqrt(
        sum(value * value for value in first.values())
    )

    norm_second = math.sqrt(
        sum(value * value for value in second.values())
    )

    if norm_first == 0 or norm_second == 0:
        return 0.0

    return dot_product / (norm_first * norm_second)


if __name__ == "__main__":
    chunks = [
        "Tokenization divides text into smaller units called tokens.",
        "Chunking divides long documents into smaller sections.",
        "Overlapping chunks preserve context between sections.",
        "Retrieval systems find relevant information in documents.",
        "Sentence-aware chunking tries to keep complete sentences together."
    ]

    query = "How can I divide a document into smaller parts?"

    vectors = build_tfidf(chunks + [query])
    query_vector = vectors[-1]

    results = []

    for index, chunk in enumerate(chunks):
        score = cosine_similarity(query_vector, vectors[index])
        results.append((score, chunk))

    results.sort(key=lambda item: item[0], reverse=True)

    print("TASK 2: TF-IDF CHUNK SUGGESTIONS")
    print("Query:", query)
    print("\nRanked chunks:")

    for rank, (score, chunk) in enumerate(results, start=1):
        print(f"\nRank {rank}")
        print(f"Similarity: {score:.4f}")
        print("Text:", chunk)

    print("\nTask 2 suggestions finished.")