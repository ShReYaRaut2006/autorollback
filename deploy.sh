#!/bin/bash

IMAGE=$1
CONTAINER_NAME=my_app

echo " Deploying container $CONTAINER_NAME with image $IMAGE"

# Stop and remove old container if it exists
# docker rm -f $CONTAINER_NAME 2>/dev/null || true

# Run new container in background and expose port
docker run -d --name $CONTAINER_NAME -p 8000:8000 $IMAGE

echo "Container $CONTAINER_NAME deployed."
