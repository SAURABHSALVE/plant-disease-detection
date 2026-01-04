FROM python:3.10-slim

# Metadata and immutability settings
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt ./

# Install system dependencies required for image processing and wheel builds
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		build-essential \
		libjpeg-dev \
		zlib1g-dev \
		libgl1 \
		curl \
	&& rm -rf /var/lib/apt/lists/*

# Upgrade pip tooling then install Python deps. PyTorch CPU wheels are installed
# from the official extra index to ensure binary wheels on slim images.
RUN pip install --upgrade pip setuptools wheel \
	&& grep -vE "torch|torchvision" requirements.txt > requirements.tmp \
	&& pip install --no-cache-dir -r requirements.tmp \
	&& rm requirements.tmp \
	&& pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu "torch==2.1.0+cpu" "torchvision==0.16.0+cpu" -f https://download.pytorch.org/whl/torch_stable.html

# Copy application sources and model artifacts
COPY src/ src/
COPY models/ models/

# Create a non-root user for safer containers
RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

# Basic HTTP healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

# Use Gunicorn with Uvicorn workers for production readiness
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "src.api:app", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120"]
