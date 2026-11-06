import json
from pathlib import Path

rows = [
    (
        "late",
        "Late submission is normally penalized. Illness extensions require medical evidence before the deadline.",
        "Illness extensions require medical evidence before the deadline."
    ),
    (
        "password",
        "Reset a forgotten password using the recovery link. Never share recovery codes.",
        "Reset a forgotten password using the recovery link."
    ),
    (
        "assignment",
        "Upload assignments through the learning portal. Submit the final file as a PDF.",
        "Upload assignments through the learning portal."
    ),
    (
        "contractor",
        "Contractors can work remotely only if the signed contract permits it. Employee rules do not apply to contractors.",
        "Contractors can work remotely only if the signed contract permits it."
    ),
    (
        "printer",
        "For blank printer pages, check ink levels and run the cleaning utility. Print a test page afterwards.",
        "For blank printer pages, check ink levels and run the cleaning utility."
    )
]

docs = {
    doc: text
    for doc, text, evidence_text in rows
}

evidence = {
    doc: evidence_text
    for doc, text, evidence_text in rows
}

questions = [
    ("What is required for illness extensions?", "late", "dev"),
    ("How do I reset a forgotten password?", "password", "dev"),
    ("Where do I upload assignments?", "assignment", "dev"),
    ("Can contractors work remotely?", "contractor", "dev"),
    ("What do I do for blank printer pages?", "printer", "test"),
    ("How can I recover my login access?", "password", "test"),
    ("How should I hand in my coursework?", "assignment", "test"),
    ("What proof is needed when I was ill?", "late", "test"),
    ("What are tomorrow's flight prices?", None, "test"),
    ("Who won the football match?", None, "test")
]

queries = [
    {
        "query": q,
        "doc": doc,
        "evidence": evidence[doc] if doc is not None else None,
        "split": split
    }
    for q, doc, split in questions
]

for name, data in [
    ("corpus.json", docs),
    ("queries.json", queries)
]:
    if Path(name).exists():
        raise FileExistsError(
            "File already exists: " + name
            + ". No files were overwritten."
        )

    Path(name).write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

print("Created corpus.json and queries.json")