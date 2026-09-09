# student-ml-api

A simple ML inference API for prediction, built with Flask.

**Author:** Muhammad Tabarak Cheema (23i-0665)

## Overview

This project demonstrates a professional MLOps workflow including:
- Feature branch development with Pull Requests
- Automated CI/CD via GitHub Actions
- Docker containerization
- Versioned image publishing to GitHub Container Registry (GHCR)
- Full traceability from PR → Commit → Git Tag → Docker Image

## API Endpoints

### Health Check
```
GET /health
```
Returns application health status, version, and model metadata.

### Prediction
```
POST /predict
Content-Type: application/json

{"value": 10}
```
Returns a prediction based on the input value.

## Development Workflow

```
feature branch → Pull Request → CI → Review → Merge → Tag → Release → Registry
```

## Quick Start

```bash
# Run locally
pip install -r requirements.txt
python app.py

# Run with Docker
docker build -t student-ml-api:1.0.0 .
docker run -d --name student-ml-api -p 5000:5000 student-ml-api:1.0.0

# Test
curl http://localhost:5000/health
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"value": 10}'
```

## Testing

```bash
pip install pytest
pytest
```
