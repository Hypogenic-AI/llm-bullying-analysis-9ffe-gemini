# Downloaded Datasets

This directory contains samples of datasets for the research project. Data files are NOT committed to git due to size. Follow the download instructions below.

## Dataset 1: AI Human Text Detection (v1)
### Overview
- **Source**: [silentone0725/ai-human-text-detection-v1](https://huggingface.co/datasets/silentone0725/ai-human-text-detection-v1)
- **Task**: Binary classification (AI vs Human)
- **Samples**: `ai_human_text_samples.json`
- **Why relevant**: Comprehensive dataset for training and testing AI detectors.

### Download Instructions
```python
from datasets import load_dataset
ds = load_dataset('silentone0725/ai-human-text-detection-v1')
```

## Dataset 2: PADBen (Paraphrase Attack Benchmark)
### Overview
- **Source**: [JonathanZha/PADBen](https://huggingface.co/datasets/JonathanZha/PADBen)
- **Task**: Paraphrase attack evaluation (Types 1 to 5)
- **Samples**: `padben_exhaustive-task1_samples.json`, `padben_exhaustive-task5_samples.json`
- **Why relevant**: Investigates the "Intermediate Laundering Region" and deep laundering (Task 5).

### Download Instructions
```python
from datasets import load_dataset
# Example: Load Task 5 (Hardest - Plagiarism Evasion)
ds = load_dataset('JonathanZha/PADBen', 'exhaustive-task5')
```

## Dataset .gitignore
Datasets are excluded from git. See .gitignore for details.
