# pyrefly: ignore [missing-import]
import lmstudio as lms

model = lms.llm("google/gemma-4-e2b")
result = model.respond("What is the meaning of life?")

print(result)