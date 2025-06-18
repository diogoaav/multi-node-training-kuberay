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