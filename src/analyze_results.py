import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_rel

def analyze():
    with open("results/bullying_results.json", "r") as f:
        results = json.load(f)

    # Prepare data for plotting
    data = []
    for r in results:
        # Original
        data.append({"Sample": r["id"], "Round": 0, "Type": "Iterative", "Score": r["original_score"]})
        # Rounds
        for round_data in r["rounds"]:
            data.append({"Sample": r["id"], "Round": round_data["round"], "Type": "Iterative", "Score": round_data["score"]})
        # Single-Shot
        data.append({"Sample": r["id"], "Round": 1, "Type": "Single-Shot", "Score": r["single_shot"]["score"]})

    df = pd.DataFrame(data)

    # Average scores
    summary = df.groupby(["Round", "Type"])["Score"].agg(["mean", "std"]).reset_index()
    print("--- Summary Results ---")
    print(summary)

    # Statistical Test: Single-Shot vs Round 5
    single_shot_scores = [r["single_shot"]["score"] for r in results]
    round_5_scores = [r["rounds"][-1]["score"] for r in results]
    
    t_stat, p_val = ttest_rel(single_shot_scores, round_5_scores)
    print(f"\nT-test (Single-Shot vs Round 5): t={t_stat:.4f}, p={p_val:.4f}")

    # Statistical Test: Round 1 vs Round 5
    round_1_scores = [r["rounds"][0]["score"] for r in results]
    t_stat_iter, p_val_iter = ttest_rel(round_1_scores, round_5_scores)
    print(f"T-test (Round 1 vs Round 5): t={t_stat_iter:.4f}, p={p_val_iter:.4f}")

    # Plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df[df["Type"] == "Iterative"], x="Round", y="Score", marker="o", label="Iterative Bullying")
    # Add Single-Shot as a point or horizontal line (at x=1 for comparison)
    plt.scatter([1], [summary[(summary["Type"] == "Single-Shot") & (summary["Round"] == 1)]["mean"].iloc[0]], 
                color="red", zorder=5, label="Single-Shot Control")
    
    plt.title("AI Detection Score Over Iterative Rejection Rounds")
    plt.ylabel("AI Probability (Detector Score)")
    plt.xlabel("Round (0=Original)")
    plt.ylim(0, 1.1)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.savefig("figures/bullying_trend.png")
    print("\nPlot saved to figures/bullying_trend.png")

    # Final Conclusion
    avg_ss = summary[(summary["Type"] == "Single-Shot") & (summary["Round"] == 1)]["mean"].iloc[0]
    avg_r5 = summary[(summary["Type"] == "Iterative") & (summary["Round"] == 5)]["mean"].iloc[0]
    improvement = (avg_ss - avg_r5) / avg_ss * 100
    print(f"\nFinal Analysis: Round 5 reduced detection by {improvement:.2f}% relative to Single-Shot.")

if __name__ == "__main__":
    analyze()
