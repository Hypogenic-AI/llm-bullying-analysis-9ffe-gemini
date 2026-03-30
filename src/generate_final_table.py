import pandas as pd
import json

def generate_final_table():
    with open("results/bullying_results.json", "r") as f:
        results = json.load(f)
    
    # Aggregating Detection Scores
    rows = []
    for r in results:
        rows.append({"Type": "Original", "Score": r["original_score"]})
        rows.append({"Type": "Round 1", "Score": r["rounds"][0]["score"]})
        rows.append({"Type": "Round 5", "Score": r["rounds"][-1]["score"]})
        rows.append({"Type": "Single-Shot", "Score": r["single_shot"]["score"]})
    
    df_scores = pd.DataFrame(rows)
    summary_scores = df_scores.groupby("Type")["Score"].agg(["mean", "std"]).reset_index()

    # Loading Regime Stats
    df_regime = pd.read_csv("results/regime_stats.csv")
    summary_regime = df_regime.groupby("Type").agg(["mean", "std"]).reset_index()
    # Flatten multi-index
    summary_regime.columns = ['Type', 'PPL_mean', 'PPL_std', 'Burstiness_mean', 'Burstiness_std']

    # Merge
    final = pd.merge(summary_scores, summary_regime, on="Type", how="outer")
    print(final)
    final.to_csv("results/final_summary.csv", index=False)

if __name__ == "__main__":
    generate_final_table()
