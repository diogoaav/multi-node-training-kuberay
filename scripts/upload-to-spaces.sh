#!/bin/bash
# Usage: ./upload-to-spaces.sh <local-folder> <bucket-name> <target-path>

LOCAL_DIR=$1
BUCKET_NAME=$2
TARGET_PATH=$3
REGION="nyc3"
ENDPOINT="https://${REGION}.digitaloceanspaces.com"

# Make sure AWS credentials are exported or set up via ~/.aws/credentials
aws --endpoint-url $ENDPOINT s3 cp --recursive "$LOCAL_DIR" "s3://$BUCKET_NAME/$TARGET_PATH"