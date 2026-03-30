# LLM Bullying: Iterative Rejection for Detection Evasion

This research investigates the "Bullying Paradox"—why iterative rejection of LLM outputs as "too AI-sounding" is more effective for passing AI detectors than single-shot instructions.

## Key Findings
- **Superior Evasion**: Iterative rejection (Round 5) achieved a **93% human probability score**, compared to **49%** for single-shot instructions.
- **Regime Shift**: The "bullying" process triggers a shift to a **higher-perplexity regime** (PPL 19.4 vs 16.1), using less predictable token sequences.
- **Burstiness Recovery**: Iterative rejection restored and improved sentence length variation (Burstiness 7.2 vs 5.8 in single-shot), a hallmark of human-like writing.

## Reproducing the Results

1.  **Environment Setup**:
    ```bash
    uv venv
    source .venv/bin/activate
    uv pip install -r requirements.txt (or use the commands in the next section)
    ```

2.  **Dependencies**:
    ```bash
    uv pip install torch transformers openai pandas matplotlib seaborn scipy
    ```

3.  **Run Experiments**:
    ```bash
    # Run the main bullying loop
    python src/experiment_bullying.py
    
    # Run analysis scripts
    python src/analyze_results.py
    python src/analyze_regime.py
    python src/generate_final_table.py
    ```

## File Structure
- `src/`: Core experiment and analysis scripts.
- `results/`: JSON and CSV outputs of experiments.
- `figures/`: Plots showing detection trends.
- `REPORT.md`: Comprehensive research report.
- `datasets/`: Pre-downloaded datasets used for evaluation.
- `papers/`: Literature review source material.

## Conclusion
"Bullying" LLMs through conversational rejection provides a more powerful steering signal than explicit task-based instructions, effectively "repelling" the model from its default AI-generation mode into a more human-like latent regime.

For more details, see [REPORT.md](./REPORT.md).
