# Projected platelet shortage and red-cell supply–demand balance in an ageing China

Reproducible code and data for the manuscript:

**Projected platelet shortage and red-cell supply–demand balance in an ageing China: a compartmental model validated against three city blood centres**

Zhensheng Dai, MD — Department of Hematology, Shanghai Pudong Hospital, Fudan University Pudong Medical Center, Shanghai, China.

## Overview

This repository contains the Python implementation of the DPS-CM (Disease–Population–Supply Compartmental Model) and the complete replication scripts for all figures, tables, and statistics reported in the manuscript. The model couples disease-specific demand (16 disease categories × 6 blood products), demographic projection (Leslie matrix, UN World Population Prospects 2024), and supply capacity with demand-elasticity feedback, and is validated against operational data from the Shanghai, Beijing, and Shenzhen blood centres (2022–2024).

## Contents

| File | Purpose |
|---|---|
| `generate_figures_vox.py` | Generates all four figures (Fig. 1–4) from the actual historical and model data embedded in the script. No hard-coded growth-rate extrapolation — all time series are real recorded statistics. |
| `convert_to_docx_vox.py` | Converts the manuscript source (Markdown) to the submission-ready Word document. |
| `Manuscript_VoxSanguinis.md` | Full manuscript source (Markdown). |
| `Cover_Letter_Vox.md` | Cover letter source. |
| `data_verification.md` | Data provenance ledger: every figure/table value, its source, and the values corrected during review. |
| `figures/Figure1.png` … `Figure4.png` | The four manuscript figures (RGB, 300 dpi). |

## Data sources

All input data are publicly available aggregate statistics: national blood-collection and donation-rate figures (National Health Commission statistical bulletins), demographic projections (UN World Population Prospects 2024), regional operational data from the Shanghai, Beijing, and Shenzhen blood centres, and international comparators (Japan Red Cross, Korean Red Cross, Paul-Ehrlich-Institut). Full provenance and correction history are documented in `data_verification.md`. No individual patient data were used.

## Requirements

- Python 3.9+
- numpy, scipy, pandas, statsmodels, matplotlib

```bash
pip install numpy scipy pandas statsmodels matplotlib
```

## Reproduction

```bash
python generate_figures_vox.py   # regenerates Fig 1–4 as PNG and PDF
python convert_to_docx_vox.py    # rebuilds the manuscript .docx
```

## License

MIT. See `LICENSE`.
