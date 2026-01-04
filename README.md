# 🌱 Plant Disease Detection API

![Docker Image Size (latest)](https://img.shields.io/docker/image-size/saurabhsalve/plant-disease-detection/latest)
![Docker Pulls](https://img.shields.io/docker/pulls/saurabhsalve/plant-disease-detection)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1.0-EE4C2C.svg)

A production-ready, Dockerized REST API for detecting plant diseases from leaf images. Built with **FastAPI** and powered by a fine-tuned **ResNet50** deep learning model.

---

## 🚀 Features

*   **Deep Learning Powered**: Utilizes a robust ResNet50 model fine-tuned for high accuracy.
*   **FastAPI Backend**: High-performance, asynchronous Python web framework.
*   **Dockerized**: Fully containerized for easy deployment anywhere (runs on any system with Docker).
*   **Production Ready**: Uses Gunicorn with Uvicorn workers for stable handling of concurrent requests.
*   **Lightweight**: Optimized build process to keep the Docker image size manageable.

---

## 🛠️ Quick Start

### Method 1: Run with Docker (Recommended)
You can pull the pre-built image directly from Docker Hub and run it in seconds.

```bash
docker run -p 8000:8000 saurabhsalve/plant-disease-detection:latest
```

The API will be available at [http://localhost:8000](http://localhost:8000).

### Method 2: Run with Docker Compose
If you have the source code cloned, you can use Docker Compose.

```bash
docker-compose up -d
```

### Method 3: Local Development (Python)
If you want to run it without Docker (requires Python 3.10+):

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/SAURABHSALVE/plant-disease-detection.git
    cd plant-disease-detection
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the server:**
    ```bash
    uvicorn src.api:app --reload
    ```

---

## 📡 API Documentation

### Health Check
**GET** `/`
Returns the status of the API.

**Response:**
```json
{
  "status": "ok",
  "message": "Plant Disease Detection API running"
}
```

### Detect Disease
**POST** `/predict`
Upload an image of a plant leaf to get a prediction.

**Body:** `multipart/form-data`
- `file`: The image file (JPG, PNG).

**Example using cURL:**
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/path/to/your/leaf_image.jpg"
```

**Response:**
```json
{
  "predicted_class": "Tomato___Early_blight",
  "confidence": 98.45
}
```

---

## 🏗️ Project Structure

```
plant-disease-detection/
├── .github/              # GitHub Actions workflows
├── models/               # Trained PyTorch models
│   └── plant_disease_resnet50_finetuned.pth
├── src/
│   ├── api.py            # FastAPI application entry point
│   ├── model.py          # ResNet50 model definition
│   └── utils.py          # Image preprocessing utilities
├── Dockerfile            # Docker instructions
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/SAURABHSALVE/plant-disease-detection/issues).

## 📜 License
This project is licensed under the MIT License.
