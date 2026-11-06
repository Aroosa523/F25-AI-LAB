import re

samples = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944 is my course code.",
    "",
    "یہ ایک مثال ہے"
]

for text in samples:
    whitespace_tokens = text.split()

    regex_tokens = re.findall(
        r"\b\w+\b",
        text,
        flags=re.UNICODE
    )

    print("\nOriginal text:", repr(text))
    print("Whitespace tokens:", whitespace_tokens)
    print("Whitespace count:", len(whitespace_tokens))
    print("Regex tokens:", regex_tokens)
    print("Regex count:", len(regex_tokens))

# Optional model tokenizer comparison
try:
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    for text in samples[:2]:
        print("\nModel tokenizer text:", repr(text))
        print("Model tokens:", tokenizer.tokenize(text))

except Exception as error:
    print("\nModel tokenizer unavailable:", error)
    print("Record this as an unsuccessful test.")