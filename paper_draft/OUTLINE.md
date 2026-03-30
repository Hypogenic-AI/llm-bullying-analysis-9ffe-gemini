# Paper Outline: The Bullying Paradox

## 1. Skeleton
- Title: The Bullying Paradox: Iterative Rejection Triggers a Regime Shift for Detection Evasion in LLMs
- Abstract
- 1. Introduction
- 2. Related Work
- 3. Methodology
- 4. Results
- 5. Discussion
- 6. Conclusion
- References

## 2. Key Points

### Abstract
- **Context**: AI-generated text detection is a critical arms race for safety and integrity.
- **Challenge**: Single-shot instructions to "write like a human" often result in rigid, detectable outputs.
- **Approach**: We examine "iterative bullying"—a feedback loop of repeated rejection as "too AI-sounding."
- **Results**: Round 5 of bullying achieves a 0.93 "Real" score, doubling the effectiveness of single-shot instructions (0.49). This is driven by a regime shift toward higher perplexity and burstiness.
- **Significance**: Simple conversational dynamics can bypass sophisticated detectors by steering models into previously inaccessible stylistic regimes.

### 1. Introduction
- **Hook**: LLMs have a distinct "AI plateau" in latent space that makes them detectable.
- **Importance**: Reliable detection is the foundation of trust in digital content.
- **Gap**: Existing evasion research focuses on manual prompting or complex optimization (SICO, SDA), but lacks analysis of iterative conversational steering.
- **Approach**: We use a systematic "bullying" loop to force models out of the AI plateau.
- **Quantitative Preview**: 93% success rate in Round 5 vs 49% in single-shot; perplexity increase of 20.5% (16.1 to 19.4).
- **Contributions**:
    - Discovery of the "Bullying Paradox": negative feedback outperforms positive instruction.
    - Quantification of the linguistic regime shift (PPL and burstiness).
    - Demonstration of feedback-driven evasion on SOTA-adjacent detectors.

### 2. Related Work
- **Detection Evasion**: SICO (Lu et al., 2023) and Self-Disguise Attack (Zhou et al., 2024).
- **Paraphrase Attacks**: PADBen (Zha et al., 2025) and the laundering region.
- **LLM Psychology**: "Bullying the Machine" (Xu et al., 2025) and persona vulnerability.

### 3. Methodology
- **Victim Model**: GPT-4o-mini as the text generation engine.
- **Detector**: OpenAI's RoBERTa-base detector for real/fake probability.
- **Dataset**: 10 samples from the "AI Human Text Detection" dataset (originally labeled AI).
- **Experiment Design**:
    - Baseline: Zero-shot AI.
    - Single-Shot: Direct "be human" instruction.
    - Bullying: 5 rounds of "This still sounds like AI. Rewrite it."
- **Linguistic Analysis**: Perplexity (GPT-2) and Burstiness (sentence length variation).

### 4. Results
- **Main Findings**: Table comparing Original, Single-Shot, and Round 5.
- **Linguistic Shift**: Plot/Table showing PPL and Burstiness trends.
- **Success Rate**: 93% "Real" probability for Round 5.
- **Statistical significance**: p=0.02 for the performance gap.

### 5. Discussion
- **The "Over-Optimization" Trap**: Why single-shot instructions make models more uniform (reduced burstiness).
- **Latent Space Searching**: Iterative rejection as a "repeller" from the AI plateau.
- **Limitations**: Small sample size (N=10), older detector baseline.
- **Broader Impacts**: Risks of automated AI laundering.

### 6. Conclusion
- Summary of the effectiveness of iterative rejection.
- Key takeaway: Negative constraints are superior to positive goals for stylistic evasion.
- Future work: Probing the residual stream during "bullying" rounds.

## 3. Evidence Mapping
- **Claim**: Bullying > Single-Shot. **Evidence**: 0.93 vs 0.49 score.
- **Claim**: Regime Shift occurs. **Evidence**: PPL 16.1 -> 19.4, Burstiness 5.8 -> 7.26.
- **Claim**: Single-shot reduces variety. **Evidence**: Burstiness drop from 6.99 (Original) to 5.8 (Single-shot).

## 4. Citation Placeholders
- [lu2023sico]: SICO paper.
- [zhou2024selfdisguise]: Self-Disguise Attack.
- [zha2025padben]: PADBen benchmark.
- [xu2025bullying]: Bullying the Machine.
- [openai2019roberta]: RoBERTa detector.

## 5. Figure/Table Planning
- **Table 1**: Main Results (Type, Detection Score, PPL, Burstiness).
- **Figure 1 (Method)**: Diagram of the Bullying Loop.
- **Figure 2**: Plot of Detection Score vs Round Number (showing the "dip" and recovery).
