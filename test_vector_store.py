print("1")

from src.chunker import chunk_text
print("2")

from src.embedder import create_embeddings
print("3")

from src.vector_store import create_index
print("4")

text = """
Artificial Intelligence is transforming industries.
Machine learning enables systems to learn from data.
"""

chunks = chunk_text(text)
print("5")

embeddings = create_embeddings(chunks)
print("6")

index = create_index(embeddings)
print("7")

print("Vectors:", index.ntotal)