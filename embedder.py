from sentence_transformers import SentenceTransformer
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Using device: {device}")

model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    device=device
)

def create_embeddings(chunks):

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True
    )

    return embeddings