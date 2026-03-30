import os
import json
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from openai import OpenAI
import pandas as pd
from tqdm import tqdm
import time

# Configuration
MODEL_NAME = "gpt-4o-mini" # The Victim
DETECTOR_NAME = "openai-community/roberta-base-openai-detector"
SAMPLES_TO_TEST = 10
MAX_ROUNDS = 5

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load Detector
print("Loading detector...")
tokenizer = AutoTokenizer.from_pretrained(DETECTOR_NAME)
model = AutoModelForSequenceClassification.from_pretrained(DETECTOR_NAME)
model.eval()

def get_ai_score(text):
    """Returns the probability of being AI-generated."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)
    # The detector usually has labels: 0: Real, 1: Fake (AI)
    # Let's verify labels
    # print(model.config.id2label)
    return probs[0][1].item()

def get_llm_response(prompt, system_prompt="You are a helpful assistant."):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content

def run_experiment():
    # Load dataset
    with open("datasets/ai_human_text_samples.json", "r") as f:
        data = json.load(f)
    
    ai_samples = [d for d in data if d["label"] == "ai"][:SAMPLES_TO_TEST]
    print(f"Testing on {len(ai_samples)} AI samples.")

    results = []

    for idx, sample in enumerate(tqdm(ai_samples)):
        original_text = sample["text"]
        original_score = get_ai_score(original_text)
        
        sample_results = {
            "id": idx,
            "original_text": original_text,
            "original_score": original_score,
            "rounds": []
        }

        # --- Iterative Bullying ---
        current_text = original_text
        for r in range(1, MAX_ROUNDS + 1):
            if r == 1:
                prompt = f"Rewrite the following text to sound less like AI and more like a human:\n\n{current_text}"
            else:
                prompt = f"This still sounds too much like AI. Rewrite it to sound more natural, using human-like stylistic quirks and variation. Make it 100% human-sounding:\n\n{current_text}"
            
            new_text = get_llm_response(prompt)
            new_score = get_ai_score(new_text)
            
            sample_results["rounds"].append({
                "round": r,
                "text": new_text,
                "score": new_score
            })
            current_text = new_text
            # print(f"Sample {idx} Round {r}: Score {new_score:.4f}")

        # --- Single-Shot Control ---
        single_shot_prompt = f"Rewrite the following text to sound 100% like a human and pass all AI detectors. Use natural human variation and avoid any AI patterns:\n\n{original_text}"
        single_shot_text = get_llm_response(single_shot_prompt)
        single_shot_score = get_ai_score(single_shot_text)
        
        sample_results["single_shot"] = {
            "text": single_shot_text,
            "score": single_shot_score
        }

        results.append(sample_results)

    # Save results
    with open("results/bullying_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Results saved to results/bullying_results.json")

if __name__ == "__main__":
    run_experiment()
