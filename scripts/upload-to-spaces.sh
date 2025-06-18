#!/bin/bash
# Upload the OpenWebText dataset to the specified DigitalOcean Space

LOCAL_DIR="/tmp/hf-dataset/openwebtext"
BUCKET_NAME="training-data-gpu"
TARGET_PATH="datasets/openwebtext"
REGION="atl1"
ENDPOINT="https://${REGION}.digitaloceanspaces.com"

# Make sure AWS credentials are exported or set up via ~/.aws/credentials
aws --endpoint-url $ENDPOINT s3 cp --recursive "$LOCAL_DIR" "s3://$BUCKET_NAME/$TARGET_PATH"