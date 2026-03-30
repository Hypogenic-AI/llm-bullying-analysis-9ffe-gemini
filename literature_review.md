# Literature Review: LLM Bullying and Detection Evasion

## Research Area Overview
The field of AI-generated text (AIGT) detection is in a constant arms race. While detectors can achieve high accuracy on direct LLM outputs, they are highly vulnerable to adversarial attacks, specifically those involving iterative modification, "bullying" tactics, or self-disguise. Recent research has identified a "laundering region" where AI text becomes statistically indistinguishable from human text while maintaining semantic coherence.

## Key Papers

### 1. Bullying the Machine: How Personas Increase LLM Vulnerability
- **Authors**: Ziwei Xu, Udit Sanghi, Mohan Kankanhalli
- **Year**: 2025
- **Key Contribution**: Investigates how psychological pressure ("bullying") can wear down LLM safety guardrails.
- **Methodology**: Uses an Attacker LLM to apply psychologically grounded tactics (gaslighting, ridicule) to a Victim LLM with specific Big Five personality traits.
- **Results**: Certain persona configurations (e.g., Low Agreeableness, Low Conscientiousness) are significantly more vulnerable.
- **Relevance**: Directly relates to the "iterative rejection" or "bullying" aspect of the hypothesis, suggesting that persistent pressure (even if not toxic) can change the model's generation regime.

### 2. PADBen: A Comprehensive Benchmark for Evaluating AI Text Detectors Against Paraphrase Attacks
- **Authors**: Yiwei Zha, Rui Min, Shanu Sushmita
- **Year**: 2025
- **Key Contribution**: Identifies the "Intermediate Laundering Region" where text evades detectors but preserves AI patterns.
- **Methodology**: Introduces a five-type taxonomy (from human original to deeply laundered text).
- **Results**: Detectors fail significantly on "Authorship Obfuscation" (Type 4) and "Deep Laundering" (Type 5).
- **Relevance**: Supports the idea that iterative paraphrasing (which iterative rejection essentially forces the model to do) creates a laundering effect.

### 3. SICO: Large Language Models can be Guided to Evade AI-Generated Text Detection
- **Authors**: Ning Lu, Shengcai Liu, Ruidan He, Ke Tang
- **Year**: 2023
- **Key Contribution**: Proposes Substitution-based In-Context example Optimization (SICO).
- **Methodology**: Optimizes prompts by substituting words/sentences in in-context examples to minimize detection.
- **Results**: Enabled GPT-3.5 to evade six major detectors (GPTZero, DetectGPT, etc.).
- **Relevance**: Demonstrates that prompt optimization (which can be seen as a form of "instruction-based bullying") is a powerful evasion tool.

### 4. Self-Disguise Attack: Induce the LLM to disguise itself for AIGT detection evasion
- **Authors**: Yinghan Zhou et al.
- **Year**: 2024
- **Key Contribution**: Guides LLMs to actively disguise their output during generation.
- **Methodology**: Uses an adversarial feature extractor and retrieval-based context examples.
- **Relevance**: Shows that "sounding less like AI" can be achieved more effectively through guided generation than simple post-hoc rephrasing.

## Gaps and Opportunities
- **Iterative Rejection Dynamics**: While iterative paraphrasing is studied, the specific psychological or "instructional" pressure of rejecting output as "too AI-sounding" (bullying) is less explored in the context of detection evasion.
- **Feature Activation**: The hypothesis that bullying activates different model features or generation regimes is a novel angle that requires mechanistic investigation (e.g., residual stream analysis).

## Recommendations for Our Experiment
1. **Primary Dataset**: Use PADBen (Task 1 and Task 5) as the evaluation benchmark.
2. **Baselines**: Compare "Single Instruction (Sound less like AI)" against "Iterative Rejection (Bullying loop)".
3. **Metrics**: Use standard detector scores (e.g., RADAR, GPTZero, DetectGPT) and semantic similarity (to ensure utility is preserved).
4. **Tools**: Adapt code from PADBen and SICO for the iterative loop implementation.
