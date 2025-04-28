from sentence_transformers import SentenceTransformer

# Download and load the model (automatically caches locally)
# The model will be saved in: ~/.cache/torch/sentence_transformers

#model = SentenceTransformer('all-MiniLM-L6-v2')
#model = SentenceTransformer('paraphrase-MiniLM-L3-v2')
# model = SentenceTransformer('BAAI/bge-small-en-v1.5')
model = SentenceTransformer('all-mpnet-base-v2')

# Generate embeddings
embeddings = model.encode("Your text goes here")
print("Embeddings shape:")
# The output will be a 384-dimensional vector
print(embeddings.shape)  # Output: (384,) - 384-dimensional vector