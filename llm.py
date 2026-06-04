from ollama import chat


def generate_answer(context, question):

    prompt = f"""
Context:
{context}

Question:
{question}

Answer only using the provided context.
"""

    response = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]