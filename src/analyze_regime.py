import json
import numpy as np
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import pandas as pd
import re

def calculate_perplexity(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt")
    if inputs["input_ids"].size(1) > 1024:
        return None
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
    return torch.exp(outputs.loss).item()

def calculate_burstiness(text):
    sentences = re.split(r'[.!?]+', text)
    lengths = [len(s.split()) for s in sentences if len(s.split()) > 0]
    if len(lengths) < 2:
        return 0
    return np.std(lengths)

def analyze_regime():
    print("Loading GPT-2 for perplexity...")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    
    with open("results/bullying_results.json", "r") as f:
        results = json.load(f)

    stats = []
    for r in results:
        # Original
        stats.append({
            "Type": "Original",
            "PPL": calculate_perplexity(r["original_text"], model, tokenizer),
            "Burstiness": calculate_burstiness(r["original_text"])
        })
        # Round 5
        stats.append({
            "Type": "Round 5",
            "PPL": calculate_perplexity(r["rounds"][-1]["text"], model, tokenizer),
            "Burstiness": calculate_burstiness(r["rounds"][-1]["text"])
        })
        # Single-Shot
        stats.append({
            "Type": "Single-Shot",
            "PPL": calculate_perplexity(r["single_shot"]["text"], model, tokenizer),
            "Burstiness": calculate_burstiness(r["single_shot"]["text"])
        })

    df = pd.DataFrame(stats)
    summary = df.groupby("Type").agg(["mean", "std"])
    print("\n--- Linguistic Regime Analysis ---")
    print(summary)
    
    # Save to CSV
    df.to_csv("results/regime_stats.csv", index=False)

if __name__ == "__main__":
    analyze_regime()
