
import re
from collections import Counter


def word_spans(text):
    """Return character offsets for whitespace-separated words."""
    return [(m.start(), m.end()) for m in re.finditer(r"\S+", text)]


def windows(text, size=40, overlap=10, offset=0):
    """Create fixed-size word windows with source offsets."""
    if size <= 0:
        raise ValueError("size must be positive")

    if not 0 <= overlap < size:
        raise ValueError("Require size > 0 and 0 <= overlap < size")

    spans = word_spans(text)
    result = []

    if not spans:
        return result

    step = size - overlap

    for i in range(0, len(spans), step):
        j = min(i + size, len(spans))

        result.append((
            offset + spans[i][0],
            offset + spans[j - 1][1]
        ))

        if j == len(spans):
            break

    return result


def sentence_chunks(text, size=40):
    """Pack sentences up to a word budget, splitting oversized sentences."""
    if size <= 0:
        raise ValueError("size must be positive")

    if not text.strip():
        return []

    cuts = [0]
    cuts.extend(
        match.end()
        for match in re.finditer(r"[.!?](?:\s+|$)", text)
    )
    cuts.append(len(text))

    segments = []
    for a, b in zip(cuts, cuts[1:]):
        if text[a:b].strip():
            segments.append((a, b))

    result = []
    pending_start = None
    pending_end = None
    pending_count = 0

    def flush():
        nonlocal pending_start, pending_end, pending_count

        if pending_start is not None:
            result.append((pending_start, pending_end))

        pending_start = None
        pending_end = None
        pending_count = 0

    for a, b in segments:
        count = len(text[a:b].split())

        if count > size:
            flush()

            # A sentence exceeding the budget needs fallback windows.
            result.extend(windows(text[a:b], size, 0, a))
            continue

        if pending_start is None:
            pending_start = a
            pending_end = b
            pending_count = count

        elif pending_count + count <= size:
            pending_end = b
            pending_count += count

        else:
            flush()
            pending_start = a
            pending_end = b
            pending_count = count

    flush()
    return result


def make_chunks(docs, strategy):
    """Create records with IDs, document IDs and character offsets."""
    result = []

    for doc_id, text in docs.items():
        if strategy == "sentence":
            spans = sentence_chunks(text, 40)
        elif strategy in ("0", "10"):
            spans = windows(text, 40, int(strategy))
        else:
            raise ValueError("Strategy must be '0', '10', or 'sentence'")

        for i, (start, end) in enumerate(spans, start=1):
            result.append({
                "id": f"{doc_id}:{strategy}:{i}",
                "doc": doc_id,
                "start": start,
                "end": end,
                "text": text[start:end]
            })

    return result


def make_demo_docs():
    """Three synthetic documents for chunking experiments."""
    docs = {
        "policy": """
Students should submit coursework through the official learning portal.
Every submitted file should be checked before the final submission deadline.
The normal submission rule requires students to upload the final version
before the deadline stated in the assessment instructions.
A late submission may receive a penalty under the standard assessment policy.
However, an illness extension may be approved when the student provides
the required medical evidence before the applicable deadline.
The exception does not mean that every illness automatically grants extra time.
Students should follow the published extension process and retain confirmation
of their request.
If the evidence is incomplete, the assessment team may request further details.
Students should check the final decision rather than assume an extension
has already been granted.
The portal may display a successful upload message, but students should also
verify that the correct file was submitted.
A file uploaded to the wrong assessment area might not count as a valid
submission, even when the upload itself appears successful.
Students should keep a copy of their submitted work and any confirmation.
When a deadline changes, students should use the officially confirmed deadline
instead of relying on an older reminder.
""".strip(),

        "security": """
Users who forget their password can start recovery through the official
password recovery link.
The recovery process may ask the user to verify access to a registered
email address or another approved recovery method.
A successful reset restores access only after the required verification steps
have been completed.
Users must not share passwords or recovery codes with other people.
The security rule applies even when a message appears to come from a colleague.
An exception may apply when an authorised administrator performs a documented
account recovery procedure under the organisation's approved policy.
That exception does not permit an ordinary colleague to request a user's
private password.
Users should inspect the destination of a recovery link before entering
account information.
If a recovery email does not arrive, they should check the registered address
and the spam folder before requesting another message.
Repeated failed attempts may temporarily restrict recovery.
In that case, users should follow the official support process instead of
trying unrelated links found in messages or search results.
After access is restored, users should review account security settings
and protect any newly issued recovery codes.
These precautions reduce the risk of account misuse and accidental disclosure.
""".strip(),

        "printing": """
A printer that produces blank pages may have empty ink cartridges or toner
that needs replacement.
Users should first check the supply indicators and confirm that the correct
printing device is selected.
Running the printer's cleaning utility can help when blocked nozzles are
preventing ink from reaching the page.
After cleaning, users should print a test page and inspect the result.
If the test page is still blank, they should check the document settings
and confirm that the content is not formatted in white text.
The normal troubleshooting procedure also includes checking the selected
paper size and reviewing any printer warning messages.
However, a shared office printer should not be opened or repaired internally
by an unauthorised user.
That safety exception means the user should contact the authorised support
team for internal repairs.
Users should record the error message and the steps already attempted.
A printer may also produce blank pages when a driver or connection problem
prevents the expected content from being processed.
Restarting the print job may help, but repeated attempts should be avoided
if the device reports a hardware fault.
Following these steps helps distinguish a simple supply problem from a
configuration issue that requires additional support.
""".strip()
    }

    return docs


def main():
    docs = make_demo_docs()

    print("TASK 2: CHUNKING COMPARISON")

    all_chunks = {}

    for strategy in ("0", "10", "sentence"):
        chunks = make_chunks(docs, strategy)
        all_chunks[strategy] = chunks

        print(f"\nStrategy: {strategy}")
        print("Total chunks:", len(chunks))

        for doc_id, source in docs.items():
            selected = [c for c in chunks if c["doc"] == doc_id]
            sizes = [len(c["text"].split()) for c in selected]
            repeated = sum(sizes) - len(source.split())

            print(
                doc_id,
                "chunks =", len(selected),
                "sizes =", sizes,
                "repeated word units =", repeated
            )

        for c in chunks:
            assert c["text"] == docs[c["doc"]][c["start"]:c["end"]]
            assert c["text"].strip()
            assert len(c["text"].split()) <= 40
            print(c["id"], c["start"], c["end"], c["text"])

    print("\nBoundary checks")
    assert windows("") == []
    assert windows("short text") == [(0, 10)]

    try:
        windows("a b", 2, 2)
    except ValueError:
        print("Invalid overlap correctly rejected")

    long_sentence = " ".join(["word"] * 95) + "."
    long_chunks = sentence_chunks(long_sentence, 40)

    assert len(long_chunks) == 3
    assert all(
        len(long_sentence[a:b].split()) <= 40
        for a, b in long_chunks
    )
    print("Long sentence fallback:", len(long_chunks), "chunks")

    # Check that the rule and exception are present in the corpus.
    assert "However, an illness extension" in docs["policy"]
    assert "medical evidence before the applicable deadline" in docs["policy"]
    print("Rule/exception source checks passed")

    print("\nChunking demonstration finished.")


if __name__ == "__main__":
    main()