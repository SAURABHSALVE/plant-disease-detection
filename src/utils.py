from PIL import Image
from torchvision import transforms

def preprocess_image(image):
    # Accept a PIL Image, a file path, or a file-like object
    if isinstance(image, (str, bytes, bytearray)):
        image = Image.open(image).convert("RGB")
    elif hasattr(image, "read"):
        image = Image.open(image).convert("RGB")

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    image = transform(image).unsqueeze(0)
    return image
