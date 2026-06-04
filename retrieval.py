from src.embedder import model


def retrieve(query, index, chunks, k=3):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return results