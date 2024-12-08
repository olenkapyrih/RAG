from typing import Generator, List


def chunk_document(
        doc: str,
        desired_chunk_size: int,
        max_chunk_size: int
        ) -> Generator[str, None, None]:
    chunk = ''
    for line in doc.splitlines():
        chunk += line + '\n'
        if len(chunk) >= desired_chunk_size:
            yield chunk[:max_chunk_size]
            chunk = ''
    if chunk:
        yield chunk


def chunk_documents(
        docs: List[str],
        desired_chunk_size: int = 500,
        max_chunk_size: int = 3000
        ) -> List[str]:
    chunks = []
    for doc in docs:
        chunks += list(chunk_document(
            doc=doc,
            desired_chunk_size=desired_chunk_size,
            max_chunk_size=max_chunk_size
            ))
        
    return chunks
