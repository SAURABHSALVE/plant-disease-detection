import torch
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io

from .model import load_model
from .utils import preprocess_image

app = FastAPI(title="Plant Disease Detection API")

DEVICE = torch.device("cpu")
MODEL_PATH = "models/plant_disease_resnet50_finetuned.pth"

# Load model once at startup
checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)
NUM_CLASSES = len(checkpoint["class_names"])

model, class_names = load_model(
    num_classes=NUM_CLASSES,
    model_path=MODEL_PATH,
    device=DEVICE
)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Plant Disease Detection API running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    image_tensor = preprocess_image(image).to(DEVICE)

    with torch.no_grad():
        outputs = model(image_tensor)
        probs = torch.softmax(outputs, dim=1)
        confidence, predicted_idx = torch.max(probs, 1)

    return {
        "predicted_class": class_names[predicted_idx.item()],
        "confidence": round(confidence.item() * 100, 2)
    }
