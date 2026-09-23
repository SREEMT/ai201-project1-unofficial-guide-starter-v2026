"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split documents into chunks. ⚠️ REPLACE THE BODY OF THIS IN MILESTONE 3.

    Right now it just calls the fallback. That is the plain, generic behaviour
    the brief is talking about.

    When you write your own strategy, set `produced_by` to
    "chunker.py::split_documents" so your README's Sample Chunks section names
    the right function. `app.py chunks` prints that string for you.

    Things worth thinking about before you write any code:
      - Are your documents short posts or long guides?
      - Is the useful information in one sentence, or spread over a paragraph?
      - Would splitting on paragraph breaks keep more thoughts intact than
        splitting on a character count?
    """
    """
    max_chars = 700
    chunks: list[Chunk] = []
    for doc in documents:
        parts = [part.strip() for part in doc.text.split("\n\n") if part.strip()]

        current_parts: list[str] = []
        current_length = 0
        index = 0

        for part in parts:
            added_length = len(part) if not current_parts else len(part) + 2
            if current_parts and current_length + added_length > max_chars:
                chunks.append(
                    Chunk(
                        text = "\n\n".join(current_parts),
                        source = doc.source,
                        index = index,
                        produced_by = "chunker.py::split_documents",
                    )
                )
                index += 1
                current_parts = []
                current_length = 0
            current_parts.append(part)
            current_length += len(part) if current_length == 0 else len(part) + 2

        if current_parts:
            chunks.append(
                Chunk(
                    text = "\n\n".join(current_parts),
                    source = doc.source,
                    index = index,
                    produced_by = "chunker.py::split_documents",
                )
            )

    #return fallback_split(documents)
    return chunks
    """

    max_chars = 700
    chunks: list[Chunk] = []

    for doc in documents:
        lines = doc.text.splitlines()

        # Build sections: each heading stays with the text underneath it.
        sections: list[str] = []
        current: list[str] = []

        for line in lines:
            if line.strip().startswith("#"):
                if current:
                    section = "\n".join(current).strip()
                    if section:
                        sections.append(section)
                current = [line]
            else:
                current.append(line)

        if current:
            section = "\n".join(current).strip()
            if section:
                sections.append(section)

        index = 0
        current_parts: list[str] = []
        current_length = 0

        for section in sections:
            # Keep very long sections for paragraph-level splitting below.
            if len(section) > max_chars:
                # Flush anything already being combined.
                if current_parts:
                    chunks.append(
                        Chunk(
                            text="\n\n".join(current_parts),
                            source=doc.source,
                            index=index,
                            produced_by="chunker.py::split_documents",
                        )
                    )
                    index += 1
                    current_parts = []
                    current_length = 0

                # Split the long section by paragraphs.
                paragraphs = [
                    p.strip()
                    for p in section.split("\n\n")
                    if p.strip()
                ]

                long_parts: list[str] = []
                long_length = 0

                for paragraph in paragraphs:
                    added = (
                        len(paragraph)
                        if not long_parts
                        else len(paragraph) + 2
                    )

                    if long_parts and long_length + added > max_chars:
                        chunks.append(
                            Chunk(
                                text="\n\n".join(long_parts),
                                source=doc.source,
                                index=index,
                                produced_by="chunker.py::split_documents",
                            )
                        )
                        index += 1
                        long_parts = []
                        long_length = 0

                    long_parts.append(paragraph)
                    long_length += (
                        len(paragraph)
                        if long_length == 0
                        else len(paragraph) + 2
                    )

                if long_parts:
                    chunks.append(
                        Chunk(
                            text="\n\n".join(long_parts),
                            source=doc.source,
                            index=index,
                            produced_by="chunker.py::split_documents",
                        )
                    )
                    index += 1

                continue

            # Combine short sections so we don't create tiny chunks.
            added = (
                len(section)
                if not current_parts
                else len(section) + 2
            )

            if current_parts and current_length + added > max_chars:
                chunks.append(
                    Chunk(
                        text="\n\n".join(current_parts),
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::split_documents",
                    )
                )
                index += 1
                current_parts = []
                current_length = 0

            current_parts.append(section)
            current_length += (
                len(section)
                if current_length == 0
                else len(section) + 2
            )

        # Flush the final combined chunk.
        if current_parts:
            chunks.append(
                Chunk(
                    text="\n\n".join(current_parts),
                    source=doc.source,
                    index=index,
                    produced_by="chunker.py::split_documents",
                )
            )

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
