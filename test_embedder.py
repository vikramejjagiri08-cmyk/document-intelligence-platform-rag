from src.loader import load_pdf
from src.chunker import chunk_text
from src.embedder import create_embeddings

text = load_pdf("data/pdfs/VIKRAM_EJJAGIRI_CV.pdf")

chunks = chunk_text(text)

embeddings = create_embeddings(chunks)

print("Number of chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)

print("\nFirst 5 values of first embedding:")
print(embeddings[0][:5])