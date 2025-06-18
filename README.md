# Multi-Node Training with KubeRay

This project scaffolds a distributed LLM training environment using:

- 🧠 **KubeRay** for orchestrating distributed training across multiple nodes
- 🧊 **JuiceFS** backed by DigitalOcean Spaces for shared dataset storage
- 🤗 **Hugging Face Datasets** for raw language modeling data
- ⚙️ **Kubernetes** with AMD MI300X GPU nodes (or similar)

## 🔧 Prerequisites

- A Kubernetes cluster with GPU nodes
- `kubectl` configured
- `awscli` for uploading to DigitalOcean Spaces
- Your Spaces credentials exported:
  ```bash
  export AWS_ACCESS_KEY_ID=your_key
  export AWS_SECRET_ACCESS_KEY=your_secret
  ```

## 📦 Dataset Preparation & Upload

### Dataset Loader Script

```python
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
```

### Upload Script

```bash
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
```

## 🚀 Getting Started

1. Run dataset loader:
   ```bash
   python data/dataset-loader.py
   ```

2. Upload to DigitalOcean Spaces:
   ```bash
   ./scripts/upload-to-spaces.sh /tmp/hf-dataset/wikitext-103-raw-v1 your-bucket-name datasets/wikitext
   ```

## 📁 Project Structure

```
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
```

## 🛠️ Coming Soon

- Fine-tuning GPT models with Ray Train
- Integration with Hugging Face Transformers
- Tokenized dataset preprocessing