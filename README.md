# 🌱 Plant Disease Detection API

*A Production-Grade Deep Learning System for Precision Agriculture*

![Docker Image Size (latest)](https://img.shields.io/docker/image-size/saurabhsalve/plant-disease-detection/latest)
![Docker Pulls](https://img.shields.io/docker/pulls/saurabhsalve/plant-disease-detection)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1.0-EE4C2C.svg)

A **production-ready, Dockerized REST API** for detecting plant diseases from leaf images using deep learning.
This system is designed as an **end-to-end machine learning solution**, covering model training, inference, API serving, containerization, and deployment readiness.

Built with **FastAPI**, powered by a **fine-tuned ResNet50**, and engineered with **real-world production practices**.

---

## 📄 Project Report (Detailed Documentation)

A **complete academic + industry-style project report** is available, covering:

* Problem formulation and real-world agricultural impact
* Dataset analysis and preprocessing
* Deep learning architecture (ResNet50 fine-tuning)
* Training strategy, evaluation metrics, and results
* System architecture and API design
* Dockerization and deployment strategy
* Limitations, scalability considerations, and future scope

📘 **Access the full project report here:**
👉 **Google Drive Report:**
[https://drive.google.com/file/d/1I4tcS0TFvWkNmIFmoU0DFBb7MxQ8i4TV/view?usp=drive_link](https://drive.google.com/file/d/1I4tcS0TFvWkNmIFmoU0DFBb7MxQ8i4TV/view?usp=drive_link)


## 🚀 Key Features

* **Deep Learning Powered**
  Fine-tuned **ResNet50 CNN** trained on plant leaf disease images for high-accuracy classification.

* **FastAPI Backend**
  Asynchronous, high-performance REST API designed for ML inference workloads.

* **Production-Grade Deployment**
  Uses **Gunicorn with Uvicorn workers** to handle concurrent inference requests reliably.

* **Dockerized & Portable**
  Fully containerized application—runs identically across local machines, servers, and cloud platforms.

* **Scalable Design**
  Modular code structure allows easy model upgrades, batch inference, and cloud scaling.

---

## 🛠️ Quick Start

### Method 1: Run with Docker (Recommended)

Pull the pre-built image from Docker Hub:

```bash
docker run -p 8000:8000 saurabhsalve/plant-disease-detection:latest
```

API will be live at:
👉 [http://localhost:8000](http://localhost:8000)

---

### Method 2: Run with Docker Compose

```bash
docker-compose up -d
```

---

### Method 3: Local Development (Without Docker)

**Requirements:** Python 3.10+

1. Clone the repository:

```bash
git clone https://github.com/SAURABHSALVE/plant-disease-detection.git
cd plant-disease-detection
```

2. Create & activate virtual environment:

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the API:

```bash
uvicorn src.api:app --reload
```

---

## 📡 API Endpoints

### Health Check

**GET /**

```json
{
  "status": "ok",
  "message": "Plant Disease Detection API running"
}
```

---

### Disease Prediction

**POST /predict**

**Request:**

* Content-Type: `multipart/form-data`
* Field: `file` (leaf image – JPG/PNG)

**cURL Example:**

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "accept: application/json" \
     -F "file=@leaf_image.jpg"
```

**Response:**

```json
{
  "predicted_class": "Tomato___Early_blight",
  "confidence": 98.45
}
```

---

## 🏗️ System Architecture & Project Structure

```
plant-disease-detection/
├── .github/              # CI/CD workflows
├── models/               # Trained PyTorch model files
│   └── plant_disease_resnet50_finetuned.pth
├── src/
│   ├── api.py            # FastAPI application
│   ├── model.py          # ResNet50 model definition
│   └── utils.py          # Image preprocessing & helpers
├── Dockerfile            # Production Docker build
├── docker-compose.yml    # Multi-container orchestration
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

---

## 🎯 Use Cases

* Smart farming & precision agriculture
* Early disease detection for crop yield improvement
* AgriTech platforms & research prototypes
* ML system design demonstration for interviews

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.
Feel free to open an issue or submit a pull request.

🔗 Issues:
[https://github.com/SAURABHSALVE/plant-disease-detection/issues](https://github.com/SAURABHSALVE/plant-disease-detection/issues)

---

## 📜 License

This project is licensed under the **MIT License**.

---


