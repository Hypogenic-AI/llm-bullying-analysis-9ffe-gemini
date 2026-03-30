import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import pandas as pd
import json
import os

def verify():
    print("--- Verification ---")
    
    # 1. GPU
    print(f"CUDA Available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"Device: {torch.cuda.get_device_name(0)}")
    
    # 2. Detector
    detector_name = "roberta-base-openai-detector" # HuggingFace model for AI detection
    try:
        tokenizer = AutoTokenizer.from_pretrained(detector_name)
        model = AutoModelForSequenceClassification.from_pretrained(detector_name)
        print(f"Successfully loaded detector: {detector_name}")
    except Exception as e:
        print(f"Error loading detector: {e}")

    # 3. Datasets
    datasets_dir = "datasets"
    files = [f for f in os.listdir(datasets_dir) if f.endswith('.json')]
    print(f"Datasets found: {files}")
    
    for f in files:
        path = os.path.join(datasets_dir, f)
        with open(path, 'r') as j:
            data = json.load(j)
            print(f"  {f}: {len(data)} records")

if __name__ == "__main__":
    verify()
