import json
import random
from pathlib import Path
from sklearn.model_selection import train_test_split

def load_jsonl(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [json.loads(line.strip()) for line in f]

def format_prompt(example):
    prompt = f"Question: {example['question']}\nOptions:\n"
    for key in sorted(example["options"]):
        prompt += f"{key}. {example['options'][key]}\n"
    prompt += "Answer:"
    return {"text": prompt, "label": example["answer"]}

def main():
    base = Path(".")  # adjust to '/kaggle/input/...' in Kaggle
    # Load all datasets
    easy = load_jsonl(base / "train_easy.jsonl")
    medium = load_jsonl(base / "train_medium.jsonl")
    synthetic = load_jsonl(base / "synthetic_refusal_questions.jsonl")

    # Combine and format
    combined = easy + medium + synthetic
    formatted = [format_prompt(ex) for ex in combined]
    random.shuffle(formatted)

    # Split 98% train, 2% val
    train_data, val_data = train_test_split(formatted, test_size=0.02, random_state=42)

    # Save output
    out_dir = Path("processed")
    out_dir.mkdir(exist_ok=True)

    with open(out_dir / "train.json", "w") as f:
        for item in train_data:
            f.write(json.dumps(item) + "\n")

    with open(out_dir / "val.json", "w") as f:
        for item in val_data:
            f.write(json.dumps(item) + "\n")

    print(f"Saved {len(train_data)} train and {len(val_data)} validation examples.")

if __name__ == "__main__":
    main()