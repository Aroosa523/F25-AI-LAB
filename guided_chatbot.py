from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_faqs():
    file_path = Path(__file__).with_name("it_help.txt")
    content = file_path.read_text(encoding="utf-8")

    blocks = content.strip().split("\n\n")
    faqs = []

    for block in blocks:
        item = {}

        for line in block.splitlines():
            if line.startswith("Q: "):
                item["question"] = line[3:].strip()

            elif line.startswith("A: "):
                item["answer"] = line[3:].strip()

            elif line.startswith("Source: "):
                item["source"] = line[8:].strip()

        if all(key in item for key in
               ("question", "answer", "source")):
            faqs.append(item)

    return faqs


def build_bot():
    faqs = load_faqs()

    if not faqs:
        raise ValueError(
            "No valid FAQs found. Check it_help.txt."
        )

    vectorizer = TfidfVectorizer()

    question_matrix = vectorizer.fit_transform(
        [faq["question"] for faq in faqs]
    )

    return faqs, vectorizer, question_matrix


def reply(engine, question):
    if not question.strip():
        return "Please enter a question."

    faqs, vectorizer, question_matrix = engine

    cleaned_question = question.strip().casefold()

    # 1. Check for an exact FAQ question first.
    for faq in faqs:
        if cleaned_question == faq["question"].casefold():
            return (
                f"Answer: {faq['answer']}\n"
                f"Source: {faq['source']}"
            )

    # 2. Use TF-IDF to find possible matches.
    query_vector = vectorizer.transform([question])

    scores = cosine_similarity(
        query_vector, question_matrix
    )[0]

    best_index = scores.argmax()
    best_score = scores[best_index]

    # 3. Suggest candidates for a nonexact question.
    if best_score > 0:
        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )

        lines = [
            "Possible matches. Please confirm:"
        ]

        for index in ranked_indices[:3]:
            if scores[index] <= 0:
                continue

            faq = faqs[index]
            lines.append(
                f"- {faq['question']} "
                f"(score: {scores[index]:.3f})"
            )

        return "\n".join(lines)

    # 4. Handle unsupported questions.
    return (
        "No matching FAQ. "
        "Please rephrase your question."
    )


if __name__ == "__main__":
    engine = build_bot()

    print("FAQ Chatbot. Type 'exit' to stop.")

    while True:
        try:
            question = input("\nQuestion: ")
        except (EOFError, KeyboardInterrupt):
            print("\nChatbot stopped.")
            break

        if question.strip().casefold() == "exit":
            break

        print(reply(engine, question))