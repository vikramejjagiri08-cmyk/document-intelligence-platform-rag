# Document Intelligence Platform

A lightweight Retrieval-Augmented Generation (RAG) pipeline for PDF-driven question answering.

This repository demonstrates a minimal document intelligence flow:

- PDF text extraction
- chunking into manageable segments
- embedding text using Sentence Transformers
- indexing embeddings with FAISS
- semantic retrieval of relevant passages
- answer generation through an Ollama-hosted LLM

---

## Table of Contents

- [Features](#features)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Example Pipeline](#example-pipeline)
- [Architecture](#architecture)
- [Extending the Project](#extending-the-project)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features

- Extract PDF text using `src/pdf_loader.py`
- Split long documents into overlapping chunks with `src/chunker.py`
- Create sentence embeddings using `src/embedder.py`
- Build a vector store using FAISS in `src/vector_store.py`
- Retrieve relevant chunks to answer a query in `src/retrieval.py`
- Generate answers from retrieved context using `src/llm.py`

---

## Repository Structure

- `rag_pipeline.py` — end-to-end example pipeline
- `src/loader.py` — PDF loading entry point
- `src/pdf_loader.py` — PDF extraction helper
- `src/chunker.py` — text chunking logic
- `src/embedder.py` — embedding generation
- `src/vector_store.py` — FAISS index creation
- `src/retrieval.py` — semantic retrieval logic
- `src/llm.py` — LLM prompt creation and invocation
- `requirements.txt` — list of dependencies
- `sample.txt` — optional sample content
- `data/pdfs/` — target PDF assets

---

## Requirements

- Python 3.10 or newer
- `pypdf`
- `sentence-transformers`
- `torch`
- `langchain-text-splitters`
- `faiss-cpu` or `faiss`
- `ollama`

> The current `requirements.txt` file may be incomplete. Use the list above for a working installation.

---

## Installation

1. Clone the repository:

```powershell
git clone <repository-url>
cd document-intelligence-platform
```

2. Create a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install runtime dependencies:

```powershell
pip install pypdf sentence-transformers torch langchain-text-splitters faiss-cpu ollama
```

4. (Optional) Save dependencies to `requirements.txt`:

```powershell
pip freeze > requirements.txt
```

---

## Configuration

### PDF input

- Update the path in `rag_pipeline.py` to point to your PDF file.
- Example:

```python
text = load_pdf("sample.pdf")
```

### LLM configuration

`src/llm.py` uses Ollama's `chat()` API with the `llama3` model:

```python
response = chat(model="llama3", messages=[...])
```

Ensure Ollama is installed and running locally before executing the pipeline.

---

## Usage

Run the pipeline script:

```powershell
python rag_pipeline.py
```

When prompted, enter a natural language question about the PDF content.

Example questions:

- "What is the main conclusion of the document?"
- "Summarize the first section."
- "What are the described benefits and limitations?"

---

## Example Pipeline

1. Load the PDF:
   - `src/pdf_loader.py` reads all pages and concatenates extracted text.
2. Chunk the text:
   - `src/chunker.py` splits text into 500-character segments with 100-character overlap.
3. Create embeddings:
   - `src/embedder.py` encodes chunks using the `all-MiniLM-L6-v2` Sentence Transformer.
4. Build the vector index:
   - `src/vector_store.py` creates a FAISS `IndexFlatL2` index.
5. Retrieve relevant chunks:
   - `src/retrieval.py` finds the top `k` matching chunks for the query.
6. Generate the answer:
   - `src/llm.py` sends retrieved context to the LLM and returns the response.

---

## Architecture

The code is organized into modular components so each stage can be replaced or extended independently.

- `loader` / `pdf_loader` — input stage
- `chunker` — preprocessing stage
- `embedder` — vectorization stage
- `vector_store` — indexing stage
- `retrieval` — search stage
- `llm` — generation stage

This design enables easy experimentation with alternate chunking strategies, embedding models, index types, or LLM providers.

---

## Extending the Project

Suggested improvements:

- Add support for additional document formats such as DOCX or TXT
- Persist FAISS indexes to disk
- Add batching for large document collections
- Support other LLM providers (OpenAI, local models, Azure, etc.)
- Add a simple web or API interface for interactive querying

---

## Troubleshooting

- `No chunks were created`: verify that the PDF text extraction succeeds and the input string is non-empty.
- `FAISS import errors`: install `faiss-cpu` for CPU use, or `faiss` if GPU support is required.
- `Ollama errors`: ensure Ollama is installed and the selected model is available.
- `CUDA` not available: the embedding code falls back to CPU if no GPU is detected.

---

## License

This repository does not include a license file. Add a `LICENSE` file if you want to make reuse terms explicit.
