# blood-security-china

Reproducible code and data for the manuscript:

**Blood security in an aging China: a demand–supply compartmental model with three-city validation and international comparison**

Zhensheng Dai, Pudong Hospital, Fudan University, Shanghai, China.

This repository contains the Python implementation of the DPS-CM (Disease–Population–Supply Compartmental Model) and all replication scripts for the figures, tables, and statistics reported in the manuscript and supplementary materials.

## Requirements

- Python 3.9+
- numpy, scipy, pandas, statsmodels, matplotlib

```bash
pip install numpy scipy pandas statsmodels matplotlib
```

## Contents

| File | Purpose | Reproduces |
|---|---|---|
| `recompute_dbdc.py` | Recomputes the D-BDC disease-specific red-cell demand shares and OAT sensitivity from Appendix A mode coefficients | Table 1; Appendix A, D; `dbdc_recomputed.json` |
| `dbdc_recomputed.json` | Recomputed demand shares (output of `recompute_dbdc.py`) | — |
| `table2_disease_demand.py` | Builds Table 1 (disease-specific RBC demand with evidence grade) | Table 1; `table2_data.json` |
| `table2_data.json` | Table 1 data (output of `table2_disease_demand.py`) | — |
| `recovery_scenario.py` | Derives the recovery-scenario RBC deficit probability via a logistic dose–response calibrated to the two Monte-Carlo anchors; bootstrap 95% CI | Figure 4; Appendix C recovery derivation |
| `generate_figure2_v3.py` | National blood-product supply–demand projections (2015–2035), 4 panels | Figure 2 |
| `generate_figure3.py` | 2030 deficit-probability projections (Monte Carlo, single panel) | Figure 3 |
| `generate_figure4.py` | RBC deficit probability vs donation-rate scenario curve with 95% CI band | Figure 4 |

## Reproduction

To reproduce every figure and table:

```bash
python3 recompute_dbdc.py          # Table 1 shares + Appendix D sensitivity
python3 table2_disease_demand.py   # Table 1 with evidence grades
python3 recovery_scenario.py       # recovery-scenario RBC probability + CI
python3 generate_figure2_v3.py     # Figure 2
python3 generate_figure3.py        # Figure 3
python3 generate_figure4.py        # Figure 4
```

Each script is self-contained and prints the key numbers to stdout; figure scripts also write PDF/PNG to the working directory.

## Key results reproduced

- Captured RBC demand: 11.37 million units (40.3% of 28.2 million 2024 supply); unclassified residual 16.83 million units (59.7%).
- Top-5 RBC demand drivers: orthopaedic major surgery (1.50 M, 13.2%), ICU critical care (1.20 M, 10.6%), severe aplastic anaemia (1.10 M, 9.7%), severe trauma (1.00 M, 8.8%), MDS (0.96 M, 8.4%).
- 2030 platelet deficit probability: 91.5% (95% CI 90.8–92.2).
- 2030 RBC deficit probability: 5.5% (recovery, 12.0‰), 18.3% (baseline, 11.2‰), 62.7% (decline, 10.0‰).

## Data sources

All input data are from publicly available sources cited in the manuscript: National Health Commission of China statistical bulletins (2010–2024), Shanghai/Beijing/Shenzhen blood-centre operational data, Japanese Red Cross / Korean Red Cross / Statistics Korea / Paul-Ehrlich-Institut, and published literature (Brixner et al. 2024; Yao et al. 2022; KDIGO 2026). No individual patient data were used.

## License

MIT License. Code is provided to enable independent verification of the manuscript's results.

## Contact

Zhensheng Dai — Tongyuanzhongzhi@outlook.com
