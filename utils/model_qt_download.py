from transformers import AutoModel, BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(load_in_8bit=True)
model = AutoModel.from_pretrained(
    'sentence-transformers/all-MiniLM-L6-v2',
    quantization_config=bnb_config
)

# Generate embeddings
embeddings = model.encode("Your text goes here")
print("Embeddings shape:")

print(embeddings.shape)