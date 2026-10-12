# AI-Enabled Incident Triage and IT Service Management (ITSM)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Build Status](https://img.shields.io/badge/Status-Active%20Research-green.svg)](#)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)

**Authors:** Aimara Temresheva, Kirill Dolgopolov  
**Domain:** IT Service Management (ITSM) Automation & Human-in-the-Loop MLOps  

---

## 1. Project Overview & Research Aim

This repository contains the experimental framework and code for evaluating **AI-enabled incident triage mechanisms** in operational IT Service Management (ITSM) environments. The research investigates how automated ticket classification and routing alter operational decision-making speed, routing accuracy, and resolution bottlenecks while establishing dynamic human oversight protocols.

### Research Questions
* **RQ1:** How are AI-enabled incident triage mechanisms currently structured and integrated into operational IT Service Management (ITSM) workflows?
* **RQ2:** How do AI-driven incident triage mechanisms optimize operational resolution pathways and reduce response bottlenecks?
* **RQ3:** How are human oversight frameworks and escalation protocols structured to balance algorithmic decision autonomy with managerial intervention in enterprise ITSM operations?

### Core Hypothesis
Integrating lightweight NLP classification models with dynamic escalation thresholding reduces mean ticket triage latency by over **40%** and routing misclassification rates by **30%**, without increasing unverified automated escalation errors.

---

## 2. Repository Structure

```text
itsm-ai-triage-research/
├── configs/          # Experiment & pipeline hyperparameter configurations
├── data/             # Raw, processed, and synthetic ITSM incident logs
├── models/           # Serialized model artifacts & baseline checkpoints
├── notebooks/        # Jupyter notebooks for EDA, modeling, and simulation
├── outputs/          # Publication-ready plots, figures, and benchmark metrics
├── scripts/          # Execution scripts for training, evaluation, and simulation
├── src/              # Core modular Python package (data, models, oversight)
├── Dockerfile        # CPU-optimized Python 3.11 container definition
├── docker-compose.yml# Container orchestration service configuration
└── README.md         # Primary academic repository documentation
```

---

## 3. System Requirements & Prerequisites

* **Operating System:** Linux (Ubuntu 22.04 LTS recommended), macOS, or Windows 11 (via WSL2).
* **Hardware Requirements:** x86_64 or ARM64 multi-core CPU (4+ cores recommended), 8 GB RAM minimum.
* **Software Dependencies:**
  * Python >= 3.11
  * Docker Engine >= 24.0 & Docker Compose v2
  * Git >= 2.30

---

## 4. Quickstart & Reproducibility Guide

Run the full experimental pipeline end-to-end in 3 commands:

```bash
# 1. Clone the repository
git clone https://github.com/MagicTMT/itsm-ai-triage-research.git && cd itsm-ai-triage-research

# 2. Build and launch the reproducible CPU environment
docker compose up --build -d

# 3. Execute baseline evaluation and routing simulation
docker exec -it itsm_triage_app python scripts/run_simulation.py
```


---

## 5. Expected Results & Benchmark Table

Below are benchmark evaluation metrics produced across baseline rule-based systems and the proposed AI-enabled triage framework under CPU execution.

| Model / Strategy | Precision | Recall | F1-Score | Avg Triage Latency (ms) | Bottleneck Reduction (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Rule-Based Baseline** | 0.64 | 0.58 | 0.61 | 1,420.0 | — |
| **TF-IDF + Logistic Reg.** | 0.78 | 0.76 | 0.77 | 12.4 | 18.5% |
| **DistilBERT (CPU Inference)** | 0.89 | 0.88 | 0.88 | 48.2 | 41.2% |
| **Proposed Hybrid + Oversight** | **0.93** | **0.91** | **0.92** | **35.1** | **46.8%** |

---

## 6. Citation & License

If you use this framework, dataset pipeline, or research code in your work, please cite it:

```bibtex
@article{temresheva2026itsm,
  title={AI-Enabled Incident Triage and IT Service Management (ITSM)},
  author={Temresheva, Aimara and Dolgopolov, Kirill},
  journal={Repository of IT Service Management Research},
  year={2026},
  publisher={GitHub Repository},
  url={https://github.com/your-org/itsm-ai-triage-research}
}
```

This project is licensed under the **MIT License** — see the `LICENSE` file for details.
