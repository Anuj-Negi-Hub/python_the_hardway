import lmstudio as lms

# Load the downloaded embedding model
embedder = lms.embedding_model("text-embedding-nomic-embed-text-v1.5")

# Generate vector embedding for input text
embedding = embedder.embed("What is the meaning of life?")
print(f"Embedding dimensions: {len(embedding)}")
