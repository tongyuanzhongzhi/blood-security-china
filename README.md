# DPS-CM blood supply–demand model for China

Reproducible code and data for the manuscript:

**Extending platelet shelf life and expanding apheresis capacity to avert projected platelet and red-cell deficits in China: a compartmental model of blood supply and demand**

Zhensheng Dai — Department of Hematology, Shanghai Pudong Hospital, Fudan University Pudong Medical Center, Shanghai, China.

## Overview

This repository contains the full, runnable DPS-CM (Disease–Population–Supply Compartmental Model), reconstructed from first principles. The earlier version reported deficit probabilities as hard-coded "anchor" values; `dps_cm.py` replaces those with a transparent 10,000-iteration Monte Carlo simulation whose parameters carry explicit provenance.

## Core files

| File | Purpose |
|---|---|
| `dps_cm.py` | Full model: Monte Carlo simulation, Wilson 95% CI, sensitivity analysis, and Figure 3/4 generation |
| `monte_carlo_results.json` | Deficit probabilities and 95% CIs |
| `Figure3_deficit_probabilities.png/.pdf` | 2030 deficit probabilities (also in `figures/Figure3.*`) |
| `Figure4_donation_rate_scenario.png/.pdf` | Red-cell deficit vs donation rate (also in `figures/Figure4.*`) |

## Reproduction

```bash
python3 dps_cm.py            # runs the 10,000-iteration Monte Carlo, prints results
python3 dps_cm.py --figures  # also regenerates Figure 3 and Figure 4 (PNG/PDF)
```

Requirements: Python 3.9+, numpy. (`--figures` additionally needs matplotlib.)

## Key parameters (with provenance)

- RBC demand growth 2.5%/yr — ageing-weighted (population 65+ rising 15.2%→20%, patients 60+ using 42% of blood)
- Platelet demand growth 8%/yr (first-tier cities); platelet supply growth 1.5%/yr
- Demand uncertainty ±15% (driven by the 59.7% unclassified residual); supply uncertainty ±10%
- Monte Carlo: 10,000 iterations, seed 42; Wilson score interval for binomial proportions

## Key results (2030)

| Component | Deficit probability |
|---|---|
| Cryoprecipitate | 100% (deterministic) |
| Platelets | 96.9% (95% CI 96.5–97.2) |
| Red cells — baseline (11.2‰) | 78.1% |
| Red cells — recovery (12.0‰) | 67.1% |
| Red cells — decline (10.0‰) | 91.2% |

Sensitivity (RBC demand growth 1.5% / 2.5% / 3.5% per yr): baseline deficit 69.2% / 78.2% / 86.0% — the near-certain deficit is robust to the growth assumption.

## Earlier files

`generate_figures_vox.py`, `Manuscript_VoxSanguinis.md`, `Cover_Letter_Vox.md`, and `data_verification.md` are the earlier Vox Sanguinis submission version (superseded). `dps_cm.py` and `monte_carlo_results.json` are the current, reproducible model and its results.

## License

MIT. See `LICENSE`.
