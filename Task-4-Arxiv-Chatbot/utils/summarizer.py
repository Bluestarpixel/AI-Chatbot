def summarize_text(text, max_sentences=3):
    """
    Simple extractive summarizer.
    Returns the first few sentences of the abstract.
    """

    if not text:
        return "No summary available."

    sentences = text.split(".")

    summary = ". ".join(sentences[:max_sentences]).strip()

    if summary and not summary.endswith("."):
        summary += "."

    return summary