from src.chunker import chunk_text
from src.embedder import create_embeddings
from src.vector_store import create_index
from src.retrieval import retrieve
from src.llm import generate_answer

# Load document
from src.pdf_loader import load_pdf

text = load_pdf("sample.pdf")
print("Characters extracted:", len(text))
print(text[:500])

print("\n=== DOCUMENT LOADED ===")
print(text[:200])

# Chunking
chunks = chunk_text(text)

print("\n=== CHUNKING ===")
print("Number of chunks:", len(chunks))

if len(chunks) == 0:
    raise ValueError("No chunks were created. Check sample.txt")

# Embeddings
embeddings = create_embeddings(chunks)

print("\n=== EMBEDDINGS ===")
print("Shape:", embeddings.shape)

# Vector Store
index = create_index(embeddings)

print("\n=== VECTOR STORE ===")
print("Vectors in index:", index.ntotal)

# User Question
question = input("\nAsk a question: ")

# Retrieval
results = retrieve(
    question,
    index,
    chunks,
    k=min(3, len(chunks))
)

print("\n=== RETRIEVED CHUNKS ===")

for i, chunk in enumerate(results, start=1):
    print(f"\nChunk {i}:")
    print(chunk[:200])

context = "\n\n".join(results)

# LLM Answer
answer = generate_answer(
    context,
    question
)

print("\n=== ANSWER ===\n")
print(answer)