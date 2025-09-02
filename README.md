# Finetuned Mistral-7B for Medical Multiple-Choice Questions

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Hugging Face Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-yellow)](https://huggingface.co/Tejas1615/medical-mstrl7b-lora_adapters_final_16b)

This repository contains the code and resources to finetune the `mistralai/Mistral-7B-v0.1` model on a clinical/medical multiple-choice question (MCQ) dataset using QLoRA for efficient, low-resource training.

## Features
-   **High Performance:** Leverages the powerful Mistral-7B base model.
-   **Efficient Training:** Uses QLoRA via the `unsloth` library for fast finetuning on a single consumer GPU (like a T4 or RTX 3090).
-   **Task-Specific:** Specifically trained to understand and answer medical multiple-choice questions in an instruction format.
-   **Generalizable:** The training format is designed to handle questions with a variable number of options (4 to 10).

---

## 🚀 Trained Model

The finetuned LoRA adapters for this model are publicly available on the Hugging Face Hub. You can load them directly for inference without needing to retrain.

* **Hugging Face Repository:** [**Tejas1615/medical-mstrl7b-lora_adapters_final_16b**](https://huggingface.co/Tejas1615/medical-mstrl7b-lora_adapters_final_16b)

---

## 📦 Dataset

The model was trained on a private medical MCQ dataset ( containing a mixture of questions from - **MedQA , MedMcqa , PubMed**) in `.jsonl` format. Each line follows this structure:
```json
{"input": "Question text...\nA. Option A\nB. Option B...", "output": "A. Option A is the correct answer."}
```
The data was pre-processed into an instruction format suitable for Mistral-7B-Instruct.

You can find the train and test data here : [Kaggle_data](https://www.kaggle.com/datasets/bstejas/godel-data-2)

* [Mistral AI](https://mistral.ai/) for the base model.
* The `unsloth` team for their memory-efficient training library.
* The Hugging Face ecosystem.
