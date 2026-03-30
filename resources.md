# Resources Catalog: LLM Bullying and Detection Evasion

## Summary
This document catalogs all resources gathered for the research project, including papers, datasets, and code repositories.

## Papers
Total papers downloaded: 5

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| Bullying the Machine | Ziwei Xu et al. | 2025 | papers/2505.12692_Bullying_the_Machine.pdf | Psychological pressure and personas. |
| PADBen | Yiwei Zha et al. | 2025 | papers/2511.00416_PADBen.pdf | Paraphrase attack benchmark. |
| SICO | Ning Lu et al. | 2023 | papers/2305.10847_SICO.pdf | Prompt optimization for evasion. |
| Detection Avoidance | Sinclair Schneider et al. | 2025 | papers/2503.07595_Detection_Avoidance.pdf | Paraphrasing/RL for evasion. |
| Self-Disguise Attack | Yinghan Zhou et al. | 2024 | papers/2412.19437_Self_Disguise_Attack.pdf | Guided generation for evasion. |

## Datasets
Total datasets sampled: 2

| Name | Source | Task | Location | Notes |
|------|--------|------|----------|-------|
| AI Human Text Detection | silentone0725 | Binary Classification | datasets/ai_human_text_samples.json | Sample of 100 records. |
| PADBen Samples | JonathanZha | Paraphrase Evaluation | datasets/padben_exhaustive-task1_samples.json | Task 1 and 5 extremes. |

## Code Repositories
Total repositories cloned: 3

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| SICO | ColinLu50/Evade-GPT-Detector | Prompt optimization | code/SICO/ | Useful for iterative optimization. |
| PADBen | JonathanZha47/PadBen | Benchmark code | code/PADBen/ | Key for evaluation. |
| SDA | CAU-ISS-Lab/AIGT-Detection-Evade-Detection | Guided generation | code/SDA/ | Self-disguise techniques. |

## Recommendations for Experiment Design
1. **Model to Test**: Evaluate across multiple models (e.g., GPT-3.5, GPT-4, and open-source models like Llama-3 or Mistral).
2. **Iteration Strategy**: Implement a "Bullying Loop" that rejects output as "too AI-sounding" iteratively.
3. **Control**: Single-instruction baseline ("Write this to sound less like AI").
4. **Evaluation**: Use detectors from the `code/SICO` and `code/PADBen` repositories.
