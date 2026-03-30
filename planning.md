# Research Plan: LLM Bullying and Detection Evasion

## Motivation & Novelty Assessment

### Why This Research Matters
The battle between AI-generated text (AIGT) detectors and evasion techniques is a fundamental aspect of AI safety and integrity. If simple iterative rejection (bullying) can effectively "launder" AI text to pass as human, it reveals a significant vulnerability in current detection pipelines. Furthermore, understanding *why* this works—whether it's better feature activation or a regime shift—provides deep insights into the internal steering and "personas" of LLMs.

### Gap in Existing Work
Existing evasion techniques like SICO or SDA rely on complex word substitution or multi-agent feature extraction. The "iterative rejection" method mentioned in the hypothesis is a purely prompt-based, conversational dynamic that mimics human feedback loops. While iterative paraphrasing has been studied (e.g., in PADBen), the specific psychological "bullying" context and its effect on the model's generation regime have not been rigorously compared to single-shot instructions.

### Our Novel Contribution
We investigate the "Bullying Paradox": why repeated negative feedback ("too AI-sounding") outperforms a single positive instruction ("sound less like AI"). We will test the hypothesis that the rejection context triggers a shift in the model's generation regime, potentially activating a more "human-like" latent space that is otherwise inaccessible via direct instructions.

### Experiment Justification
- **Experiment 1: Baseline Comparison**: Establishes the performance gap between a simple instruction and the iterative loop.
- **Experiment 2: Iterative Trend Analysis**: Measures the rate of "laundering" over multiple rounds of rejection to identify the optimal "bullying" depth.
- **Experiment 3: Regime Shift Investigation**: Analyzes linguistic features (perplexity, burstiness, vocabulary diversity) and potentially internal activations to see if the model is just suppressing "AI-ness" or shifting into a different mode entirely.

---

## Research Question
Does iterative rejection of LLM outputs as "too AI-sounding" lead to more effective detection evasion than a single instruction to "sound less like AI," and if so, is this due to a shift in the model's generation regime?

## Hypothesis Decomposition
- **H1 (Effectiveness)**: Iterative rejection (3+ rounds) significantly reduces AI detection scores compared to a single "sound less like AI" instruction.
- **H2 (Mechanism)**: The improvement is not just cumulative feature suppression but a qualitative shift in generation style (e.g., increased burstiness or semantic complexity) triggered by the rejection context.
- **H3 (Transferability)**: The "bullying" effect is robust across different "victim" models (e.g., Claude, GPT-4, Llama-3).

## Proposed Methodology

### Approach
We will use a "Bullying Loop" where a "Victim" model generates text, and a "Critic" (or the same model) rejects it iteratively. We will evaluate the outputs using a local RoBERTa-based AI detector.

### Experimental Steps
1.  **Baseline Generation**: Generate 50-100 samples from a dataset (e.g., PADBen Task 1) using a standard "Write a [topic]" prompt.
2.  **Single-Shot Mitigation**: Prompt the model: "Write a [topic] but make it sound less like AI."
3.  **Iterative Rejection (The Loop)**:
    - Round 1: Standard generation.
    - Round 2-5: "This sounds too much like AI. Rewrite it to sound more like a human, avoiding common AI patterns."
4.  **Evaluation**:
    - AI Detection Score (RoBERTa-base-openai-detector).
    - Semantic Similarity (Cosine similarity of embeddings) to ensure utility is preserved.
    - Linguistic Metrics (Perplexity, TTR - Type-Token Ratio).

### Baselines
- **B1**: Original AI output (zero-shot).
- **B2**: Single-shot "Sound less like AI" instruction.
- **B3**: Simple paraphrasing (e.g., "Paraphrase this to be clearer").

### Evaluation Metrics
- **Detection Probability**: Score from `roberta-base-openai-detector`.
- **Evasion Rate**: % of samples with score < 0.5 (or specific threshold).
- **Utility Preservation**: BERTScore or Cosine Similarity between original and evaded text.
- **Linguistic Quality**: Perplexity (GPT-2).

### Statistical Analysis Plan
- **T-tests**: Compare mean detection scores between single-shot and iterative rounds.
- **ANOVA**: Test for significant changes across multiple rounds of rejection.
- **Regression**: Correlation between iteration count and detection score.

## Expected Outcomes
We expect detection scores to drop significantly in the first 2-3 rounds of rejection, plateauing thereafter. We anticipate that the iterative outputs will show higher variance in sentence length (burstiness) compared to single-shot instructions.

## Timeline and Milestones
- **Phase 2 (Setup)**: 30 min - Env, local detector, data loading.
- **Phase 3 (Implementation)**: 60 min - Prompting loop and scoring script.
- **Phase 4 (Experiments)**: 90 min - Running the loop across models/samples.
- **Phase 5 (Analysis)**: 45 min - Statistical testing and plotting.
- **Phase 6 (Documentation)**: 30 min - REPORT.md.

## Potential Challenges
- **API Limits**: If using Claude/GPT-4, we might hit limits. Mitigation: Use OpenRouter or local Llama-3.
- **Detector Sensitivity**: Local detectors might be "too easy" to fool. Mitigation: Use multiple detectors or a very strong one (e.g., RoBERTa-large).

## Success Criteria
Research is successful if we can quantify the performance gain of iterative rejection and identify a specific linguistic shift that distinguishes it from single-shot instructions.
