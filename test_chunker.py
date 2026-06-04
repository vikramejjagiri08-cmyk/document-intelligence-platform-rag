from src.loader import load_pdf
from src.chunker import chunk_text

text = load_pdf("data/pdfs/VIKRAM_EJJAGIRI_CV.pdf")

chunks = chunk_text(text)

print("Number of chunks:", len(chunks))