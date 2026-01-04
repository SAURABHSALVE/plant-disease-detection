import torch
try:
    # When running as a module (python -m src.predictor)
    from .model import load_model
    from .utils import preprocess_image
except Exception:
    # When running as a script (python src/predictor.py)
    from model import load_model
    from utils import preprocess_image

DEVICE = torch.device("cpu")

MODEL_PATH = "models/plant_disease_resnet50_finetuned.pth"
IMAGE_PATH = "test_image.jpg"

def main():
    # Load model
    checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)
    num_classes = len(checkpoint["class_names"])

    model, class_names = load_model(
        num_classes=num_classes,
        model_path=MODEL_PATH,
        device=DEVICE
    )

    # Preprocess image
    image = preprocess_image(IMAGE_PATH).to(DEVICE)

    # Predict
    with torch.no_grad():
        outputs = model(image)
        probs = torch.softmax(outputs, dim=1)
        confidence, predicted_idx = torch.max(probs, 1)

    print("✅ Prediction Result")
    print("-------------------")
    print("Class:", class_names[predicted_idx.item()])
    print("Confidence:", round(confidence.item() * 100, 2), "%")

if __name__ == "__main__":
    main()
