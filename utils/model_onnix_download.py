from sentence_transformers import SentenceTransformer
import os

model = SentenceTransformer('all-MiniLM-L6-v2')
save_dir = "onnx_model"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Save the model in ONNX format using torch.onnx
model.save(save_dir)  # This will save the model in PyTorch format first