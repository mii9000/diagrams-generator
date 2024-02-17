#!/bin/bash

# Define your image name
IMAGE_NAME="diagram-generator"

# Build the Docker image
docker build -t $IMAGE_NAME .

# Ensure the output directory exists on the host
mkdir -p ./output

# Run the Docker container, mapping the output directory to the host
docker run --rm -v "$(pwd)/output:/app/output" $IMAGE_NAME
