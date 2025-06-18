# multi-node-training-kuberay

This project scaffolds a distributed LLM training environment using:

- 🧠 **KubeRay** for orchestrating distributed training across multiple nodes
- 🧊 **JuiceFS** backed by DigitalOcean Spaces for shared dataset storage
- 🤗 **Hugging Face Datasets** for raw language modeling data
- ⚙️ **Kubernetes** with AMD MI300X GPU nodes (or similar)

---

## 🔧 Prerequisites

- A Kubernetes cluster with GPU nodes
- `kubectl` configured
- `awscli` for uploading to DigitalOcean Spaces
- Your Spaces credentials exported:
  ```bash
  export AWS_ACCESS_KEY_ID=your_key
  export AWS_SECRET_ACCESS_KEY=your_secret