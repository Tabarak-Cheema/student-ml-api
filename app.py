"""
student-ml-api: A simple ML inference API for predictions.
Author: Muhammad Tabarak Cheema (23i-0665)
"""

import os
from flask import Flask, request, jsonify


app = Flask(__name__)


def get_version():
    """Read the application version from the VERSION file."""
    version_file = os.path.join(os.path.dirname(__file__), "VERSION")
    try:
        with open(version_file, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "unknown"


def predict(value):
    """
    Simple prediction function.
    Applies a linear transformation: prediction = 2 * value.
    In a real MLOps scenario, this would load and run a trained model.
    """
    return value * 2


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint. Returns application status and version."""
    return jsonify({
        "status": "healthy",
        "application": "student-ml-api",
        "version": get_version()
    }), 200


@app.route("/predict", methods=["POST"])
def predict_endpoint():
    """
    Prediction endpoint.
    Expects JSON body with a numeric 'value' field.
    Returns the input and the prediction result.
    """
    data = request.get_json()

    # Validate that JSON body was provided
    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    # Validate that 'value' key exists
    if "value" not in data:
        return jsonify({"error": "Missing required field: 'value'"}), 400

    value = data["value"]

    # Validate that 'value' is numeric
    if not isinstance(value, (int, float)):
        return jsonify({"error": "Field 'value' must be a number"}), 400

    result = predict(value)

    return jsonify({
        "input": value,
        "prediction": result
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
