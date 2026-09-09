# ---------------------------------------------------------
# Dockerfile for student-ml-api
# Uses a specific Python version for reproducibility.
# Follows best practices: layer ordering, no-cache-dir, etc.
# ---------------------------------------------------------

FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file first (for Docker layer caching)
COPY requirements.txt .

# Install Python dependencies without cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code
COPY app.py .
COPY VERSION .

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
