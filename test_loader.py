from src.loader import load_pdf

text = load_pdf("data/pdfs/vikram_ejjagiri_cv.pdf")

print(text[:1000])