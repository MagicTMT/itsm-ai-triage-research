# Use explicit Python 3.11 Debian-slim image for deterministic builds
FROM python:3.11-slim-bookworm

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DEBIAN_FRONTEND=noninteractive

# Install essential system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set repository working directory
WORKDIR /app

# Copy dependency definition first for Docker layer caching
COPY requirements.txt /app/requirements.txt

# Install pinned Python packages
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# Copy complete project context
COPY . /app/

# Install local package in editable mode
RUN pip install -e .

# Expose JupyterLab default port
EXPOSE 8888

# Command to launch JupyterLab server
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--ServerApp.token=''"]
