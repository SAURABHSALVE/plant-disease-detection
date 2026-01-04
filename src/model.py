import torch
import torch.nn as nn
from torchvision import models
from torchvision.models import ResNet50_Weights

def load_model(num_classes, model_path, device):
    # Use the new `weights` argument to avoid deprecation warnings.
    # We don't load ImageNet weights here because we'll load a checkpoint.
    model = models.resnet50(weights=None)

    model.fc = nn.Sequential(
        nn.Linear(model.fc.in_features, 512),
        nn.ReLU(),
        nn.Dropout(0.4),
        nn.Linear(512, num_classes)
    )

    checkpoint = torch.load(model_path, map_location=device)

    model.load_state_dict(checkpoint["model_state"])
    model.eval()
    model.to(device)

    class_names = checkpoint["class_names"]

    return model, class_names
