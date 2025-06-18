# multi-node-training-kuberay
Multi-Node GPU training using Kuberay

Target Setup Overview
	•	Hardware: 4x AMD MI300Xx8 (i.e., 32 GPUs total)
	•	Orchestration: Kubernetes on DigitalOcean
	•	Distributed Training Framework: KubeRay
	•	Dataset Source: Hugging Face (e.g., via datasets library)
	•	Storage
	•	Raw data: DigitalOcean Spaces
	•	Shared FS: JuiceFS mounted across GPU pods


 
