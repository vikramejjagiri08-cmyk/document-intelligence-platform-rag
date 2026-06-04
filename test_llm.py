from src.llm import generate_answer

context = """
Hospitals use AI systems to analyze medical records
and improve procurement workflows.
"""

question = "How is AI used in hospitals?"

answer = generate_answer(
    context,
    question
)

print(answer)