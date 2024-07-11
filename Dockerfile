# Stage 1: Build
FROM python:3.11-slim AS build

# Set environment variables to prevent Python from writing .pyc files to disk and to buffer stdout and stderr
ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.4.0 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s "$POETRY_HOME/bin/poetry" /usr/local/bin/poetry

# Set the working directory
WORKDIR /app

# Copy only the dependency-related files first, to leverage Docker layer caching
COPY pyproject.toml poetry.lock ./

# Install project dependencies
RUN poetry install --no-dev --no-root

# Copy the rest of the application code
COPY . .

# Stage 2: Runtime
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files to disk and to buffer stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy installed dependencies from the build stage
COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy application code from the build stage
COPY --from=build /app /app

# Command to run the application (can be adjusted as needed)
CMD ["python", "main.py"]