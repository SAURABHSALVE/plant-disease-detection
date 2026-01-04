# Plant Disease Detection — Dockerized (production-ready)

Quick instructions to build and run the production-ready Docker image locally.

Build the image:

```bash
docker build -t plant-disease-api:latest .
```

Run with Docker:

```bash
docker run --rm -p 8000:8000 \
  -v $(pwd)/models:/app/models:ro \
  --name plant-disease-api \
  plant-disease-api:latest
```

Run with Docker Compose (recommended for local prod-ish runs):

```bash
docker-compose up --build -d
```

Health endpoint: `http://localhost:8000/`  — returns a JSON status.

Notes:
- The `models` directory is mounted read-only in `docker-compose.yml`. If you
  want the model baked into the image, remove the volume mapping.
- The image uses `gunicorn` with `uvicorn` workers for production HTTP serving.
- For GPU builds or faster inference, use an appropriate base image and torch
  CUDA wheels (not covered here).

CI / Docker Hub
----------------

To publish images automatically to Docker Hub when you push to `main`/`master`:

- Create a Docker Hub repository named `plant-disease-api` (or pick another name).
- In your GitHub repository, add two repository secrets:
  - `DOCKERHUB_USERNAME` — your Docker Hub username
  - `DOCKERHUB_TOKEN` — a Docker Hub access token (preferred) or password
- The included GitHub Actions workflow will build the image and push two tags:
  - `DOCKERHUB_USERNAME/plant-disease-api:latest`
  - `DOCKERHUB_USERNAME/plant-disease-api:<commit-sha>`

Local manual push
-----------------

Build, tag and push locally (example):

```bash
# build
docker build -t <your-username>/plant-disease-api:latest .

# login (will prompt for password or token)
docker login --username <your-username>

# push
docker push <your-username>/plant-disease-api:latest
```

Verify
------
- After push, confirm the image is visible in your Docker Hub repository and
  run the container as shown in the earlier 'Run with Docker' section.

