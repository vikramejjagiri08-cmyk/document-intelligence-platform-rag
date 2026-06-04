from src.chunker import chunk_text
from src.embedder import create_embeddings
from src.vector_store import create_index
from src.retrieval import retrieve
text = """
Artificial Intelligence is transforming industries.

Machine learning enables systems to learn from data.

Deep learning is a subset of machine learning.

Natural Language Processing helps computers understand text.

Hospitals use AI systems to analyze medical records and improve procurement workflows.
"""

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

index = create_index(embeddings)

query = "How is AI used in hospitals?"

results = retrieve(
    query,
    index,
    chunks,
    k=3
)

print("\nTop Results:\n")

for i, result in enumerate(results, start=1):
    print(f"Result {i}:")
    print(result)
    print("-" * 50)