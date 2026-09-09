"""
Unit tests for the student-ml-api Flask application.
Tests cover: health endpoint, successful prediction, missing input, invalid input.
"""

import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    """Test that /health returns status healthy, correct app name, and model metadata."""
    response = client.get("/health")
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "healthy"
    assert data["application"] == "student-ml-api"
    assert "application_version" in data
    assert data["application_version"] == "1.1.0"
    assert data["model_version"] == "model-1"


def test_predict_success(client):
    """Test that /predict returns correct prediction for valid input."""
    response = client.post("/predict", json={"value": 10})
    data = response.get_json()

    assert response.status_code == 200
    assert data["input"] == 10
    assert data["prediction"] == 20


def test_predict_missing_value(client):
    """Test that /predict returns 400 when 'value' field is missing."""
    response = client.post("/predict", json={"wrong_key": 10})
    data = response.get_json()

    assert response.status_code == 400
    assert "error" in data
    assert "Missing required field" in data["error"]


def test_predict_invalid_value(client):
    """Test that /predict returns 400 when 'value' is not a number."""
    response = client.post("/predict", json={"value": "not_a_number"})
    data = response.get_json()

    assert response.status_code == 400
    assert "error" in data
    assert "must be a number" in data["error"]


def test_predict_no_body(client):
    """Test that /predict returns an error when no JSON body is provided."""
    response = client.post("/predict", json={})
    data = response.get_json()

    assert response.status_code == 400
    assert "error" in data


def test_predict_float_value(client):
    """Test that /predict handles float input correctly."""
    response = client.post("/predict", json={"value": 3.5})
    data = response.get_json()

    assert response.status_code == 200
    assert data["input"] == 3.5
    assert data["prediction"] == 7.0


def test_predict_negative_value(client):
    """Test that /predict handles negative input correctly."""
    response = client.post("/predict", json={"value": -5})
    data = response.get_json()

    assert response.status_code == 200
    assert data["input"] == -5
    assert data["prediction"] == -10


def test_predict_zero(client):
    """Test that /predict handles zero input correctly."""
    response = client.post("/predict", json={"value": 0})
    data = response.get_json()

    assert response.status_code == 200
    assert data["input"] == 0
    assert data["prediction"] == 0
