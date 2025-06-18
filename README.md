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
output_dir = "/tmp/hf-dataset/openwebtext"
os.makedirs(output_dir, exist_ok=True)

# Load and save the raw dataset
print("Downloading openwebtext from Hugging Face...")
ds = load_dataset("openwebtext")
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
   ./scripts/upload-to-spaces.sh /tmp/hf-dataset/openwebtext your-bucket-name datasets/openwebtext
   ```


## ⚙️ Provision CPU-Only Kubernetes Cluster for Tokenization

First, create a Kubernetes cluster with a **CPU-optimized node pool** in the Atlanta region using `doctl`:

```bash
doctl kubernetes cluster create llm-training-cpu \
  --region atl1 \
  --count 3 \
  --size c-8-intel \
  --auto-upgrade=false
```

This will:
- Create a new cluster named `llm-training-cpu`
- Use 3× `c-8-intel` nodes (8 vCPU, 16GB RAM)
- Deploy to the `atl1` region


After creation, authenticate:

```bash
doctl kubernetes cluster kubeconfig save llm-training-cpu
```

### Manually Label Nodes for Tokenizer Workload

To label the nodes for the tokenizer workload, first list your nodes and then apply the label:

```bash
kubectl get nodes
kubectl label node <node-name> workload=tokenizer
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