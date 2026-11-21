# Agentic AI for Personalized Intravesical BCG Schedule Optimization

This repository contains the SA-COG-RL research package for month-level intravesical BCG schedule optimization in high-risk NMIBC. The package implements the five-agent decision pathway: state encoding, schedule action selection, conformal safety verification, fairness auditing, and threshold-rule reporting.

## Installation

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

Conda users can create the pinned environment with:

```bash
conda env create -f environment.yml
conda activate sacogrl-bcg
```

Docker users can build the CUDA 12.1 image with:

```bash
docker build -t sacogrl-bcg .
```

## Data

Dataset URLs are listed in `dataset_links.txt`. SEER requires approval under the NCI SEER Research Data Use Agreement. TCGA-BLCA open-access clinical and aggregate RNA-seq files are available through the NIH GDC portal. Private clinical cohort data are not distributed here.

Expected processed inputs are CSV files under `data/processed/` with patient-month rows, SEER-derived registry covariates, TCGA-BLCA molecular-axis fields when present, action labels, outcomes, and censoring metadata.

## Training

```bash
python -m sacogrl.cli.train --config configs/base.yaml
```

The reported full-pipeline profile is one NVIDIA A100 40GB GPU, 14.0 hours per seed, and 180000 CQL-dominated gradient steps. Local pipeline checks can use:

```bash
python -m sacogrl.cli.train --config configs/local_check.yaml
```

## Evaluation

```bash
python -m sacogrl.cli.evaluate --config configs/base.yaml --checkpoint checkpoints/latest.pt
```

Primary reported targets are 5-year RFS 0.520 +/- 0.011 on the SEER 2021 temporal holdout, +7.0 pp over AUA/EAU 2024 SOC, conformal lower bound +5.2 pp at alpha 0.10, post-mitigation race/ethnicity AUROC gap 0.038, and aggregate conformal coverage 0.904.

## Compute Budget

The full run uses batch size 256, history length 24 months, horizon 36 months, latent dimension 32, transformer width 128, six transformer layers, eight attention heads, CQL alpha 5.0, gamma 0.95, and learning rate 1e-4. Checkpoints are written atomically with the seed and optimizer state.
