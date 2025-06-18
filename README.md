repo/
├── manifests/
│   ├── k8s-juiceds-pvc.yaml
│   ├── ray-cluster.yaml
│   └── juiceds-runtimeclass.yaml
├── ray/
│   ├── train_gpt2_ray.py
│   └── requirements.txt
├── data/
│   └── dataset-loader.py
├── scripts/
│   └── upload-to-spaces.sh
├── README.md
└── .gitignore

# data/dataset-loader.py
from datasets import load_dataset
import os

# Output directory for saving the raw dataset
output_dir = "/tmp/hf-dataset/wikitext-103-raw-v1"
os.makedirs(output_dir, exist_ok=True)

# Load and save the raw dataset
print("Downloading wikitext-103-raw-v1 from Hugging Face...")
ds = load_dataset("wikitext", "wikitext-103-raw-v1")
ds.save_to_disk(output_dir)

print(f"Dataset saved to: {output_dir}")

# scripts/upload-to-spaces.sh
#!/bin/bash
# Usage: ./upload-to-spaces.sh <local-folder> <bucket-name> <target-path>

LOCAL_DIR=$1
BUCKET_NAME=$2
TARGET_PATH=$3
REGION="nyc3"
ENDPOINT="https://${REGION}.digitaloceanspaces.com"

# Make sure AWS credentials are exported or set up via ~/.aws/credentials
aws --endpoint-url $ENDPOINT s3 cp --recursive "$LOCAL_DIR" "s3://$BUCKET_NAME/$TARGET_PATH"
