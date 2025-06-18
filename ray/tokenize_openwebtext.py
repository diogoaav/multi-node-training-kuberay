import os
from datasets import load_from_disk
from transformers import AutoTokenizer

# Configurable shard params
shard_index = int(os.environ.get("SHARD_INDEX", "0"))
shard_count = int(os.environ.get("SHARD_COUNT", "1"))

# Dataset and tokenizer setup
DATASET_PATH = "/mnt/juicefs/openwebtext"
OUTPUT_DIR = f"/mnt/juicefs/openwebtext-tokenized/shard-{shard_index}"

tokenizer = AutoTokenizer.from_pretrained("gpt2")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load, shard, and tokenize dataset
print(f"Loading dataset from {DATASET_PATH}...")
ds = load_from_disk(DATASET_PATH)
shard = ds.shard(num_shards=shard_count, index=shard_index)

print(f"Tokenizing shard {shard_index}/{shard_count}...")
tokenized = shard.map(lambda x: tokenizer(x["text"]), batched=True, remove_columns=["text"])
tokenized.save_to_disk(OUTPUT_DIR)

print(f"Tokenized shard saved to {OUTPUT_DIR}")