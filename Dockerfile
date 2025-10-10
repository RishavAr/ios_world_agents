# ============================
# iOS World Agents Dockerfile
# ============================

FROM python:3.10-slim

LABEL maintainer="Rishav Aryan <rishavaryan058@gmail.com>"
LABEL project="iOS World Agents"

# Install dependencies
RUN apt-get update && apt-get install -y \
git \
curl \
unzip \
build-essential \
&& rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV SIMULATOR_DEVICE="iPhone 17 Pro"
ENV MODEL_PROVIDER="openai"
ENV MODEL_NAME="gpt-4o"

# Expose optional API port for dashboard (future use)
EXPOSE 8080

# Default command
ENTRYPOINT ["python3", "-m", "src.main", "tasks/safari_tasks-2.json", "openai", "gpt-4o", "--exec"]
