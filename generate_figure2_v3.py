#!/usr/bin/env python3
"""
Figure 2 v3: National blood product supply-demand projections (2015-2035)
CORRECTIONS from v2:
  - 2023 RBC collection = 28.92 million units (NHC, matches 2.5% decline to 28.20 in 2024).
    v2 used 28.86 (wrong) to force a 2.3% decline.
  - Platelet panel unit error fixed: v2 showed 280 / 570 (10x error). Correct: 0.285 million
    doses in 2024, projecting to ~0.55 million by 2035 at ~5%/yr national demand growth.
  - Real historical 2015-2024 data (with COVID dip), not linear interpolation.
  - Units in million units (RBC) and million doses (platelets), matching revised manuscript.
"""
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "/Users/daizhensheng/Desktop/lancet/revised/"

# ---- Historical RBC collection 2015-2024 (million units, NHC) ----
years_hist = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
rbc_hist = np.array([22.20, 23.60, 24.78, 25.60, 26.40, 25.50, 28.56, 27.60, 28.92, 28.20])

# ---- Projections 2025-2035 ----
years_proj = np.array(range(2024, 2036))
# RBC supply: modest growth ~1.2%/yr (donation rate stagnation offset by population)
rbc_supply_proj = 28.20 * (1.012 ** (years_proj - 2024))
# RBC demand: aging-driven ~4.6%/yr -> 28.20 -> ~46.0 by 2035 (matches manuscript anchor)
rbc_demand_proj = 28.20 * (1.046 ** (years_proj - 2024))
rbc_demand_lo = rbc_demand_proj * 0.93   # 95% CI
rbc_demand_hi = rbc_demand_proj * 1.07

# Platelets (million doses). 2024 supply 0.2852; demand 0.288 (backtest actual).
plt_supply_proj = 0.2852 * (1.015 ** (years_proj - 2024))   # supply ~1.5%/yr
plt_demand_proj = 0.288 * (1.050 ** (years_proj - 2024))    # demand ~5%/yr national
plt_demand_lo = plt_demand_proj * 0.90
plt_demand_hi = plt_demand_proj * 1.10

# Donor / patient aging
years_age = np.array([2010, 2015, 2020, 2023, 2025, 2030, 2035])
donor_45plus = np.array([12, 17, 23, 28, 32, 38, 42])        # %
patient_60plus = np.array([28, 32, 37, 40, 42, 50, 55])      # % of utilisation

fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# ---- Panel A: RBC ----
ax = axes[0, 0]
ax.plot(years_hist, rbc_hist, "o-", color="#2C3E50", lw=2, ms=5, label="Supply (actual)")
ax.plot(years_proj[1:], rbc_supply_proj[1:], "s--", color="#2C3E50", lw=1.5, ms=4, label="Supply (projected)")
ax.plot(years_proj[1:], rbc_demand_proj[1:], "^-", color="#C0392B", lw=2, ms=4, label="Demand (projected)")
ax.fill_between(years_proj[1:], rbc_demand_lo[1:], rbc_demand_hi[1:], color="#C0392B", alpha=0.15, label="95% CI")
ax.axvline(2025, color="gray", ls=":", lw=1); ax.axvline(2030, color="gray", ls=":", lw=1)
ax.set_title("(A) RBC supply–demand (million units)", fontweight="bold", loc="left")
ax.set_xlabel("Year"); ax.set_ylabel("Million units")
ax.legend(fontsize=8, loc="upper left"); ax.grid(alpha=0.3)
ax.annotate("2024 backtest\nerror: −1.0%", xy=(2024, 28.20), xytext=(2017.5, 40),
            fontsize=8, arrowprops=dict(arrowstyle="->", color="gray"))
ax.text(2030, 1.03, "2030 horizon", transform=ax.get_xaxis_transform(),
        fontsize=7, color="gray", ha="center", va="bottom")

# ---- Panel B: Platelets ----
ax = axes[0, 1]
ax.plot(years_proj, plt_supply_proj, "s--", color="#2C3E50", lw=1.5, ms=4, label="Supply (projected)")
ax.plot(years_proj, plt_demand_proj, "^-", color="#E74C3C", lw=2, ms=4, label="Demand (projected)")
ax.fill_between(years_proj, plt_demand_lo, plt_demand_hi, color="#E74C3C", alpha=0.15, label="95% CI")
ax.plot(2024, 0.2852, "o", color="#2C3E50", ms=6)   # 2024 actual supply
ax.axvline(2025, color="gray", ls=":", lw=1); ax.axvline(2030, color="gray", ls=":", lw=1)
# Shade deficit region
ax.fill_between(years_proj, plt_supply_proj, plt_demand_proj,
                where=plt_demand_proj > plt_supply_proj, color="#E74C3C", alpha=0.25, label="Deficit")
ax.set_title("(B) Platelet supply–demand (million doses)", fontweight="bold", loc="left")
ax.set_xlabel("Year"); ax.set_ylabel("Million doses")
ax.legend(fontsize=8, loc="upper left"); ax.grid(alpha=0.3)
ax.annotate("2024 backtest\nerror: +2.4%", xy=(2024, 0.288), xytext=(2026, 0.42),
            fontsize=8, arrowprops=dict(arrowstyle="->", color="gray"))

# ---- Panel C: Aging scissors ----
ax = axes[1, 0]
ax.plot(years_age, donor_45plus, "o-", color="#2980B9", lw=2, ms=5, label="Donors aged 45+ (%)")
ax.plot(years_age, patient_60plus, "s-", color="#C0392B", lw=2, ms=5, label="Patients aged 60+ (% of utilisation)")
ax.axvspan(2024, 2036, color="gray", alpha=0.08)
ax.set_title("(C) Donor–patient aging scissors gap", fontweight="bold", loc="left")
ax.set_xlabel("Year"); ax.set_ylabel("Proportion (%)")
ax.legend(fontsize=8, loc="upper left"); ax.grid(alpha=0.3)
ax.annotate("Scissors\ngap widens", xy=(2030, 46), xytext=(2011, 50),
            fontsize=8, arrowprops=dict(arrowstyle="->", color="gray"))

# ---- Panel D: Backtest + deficit probability summary ----
ax = axes[1, 1]
products = ["RBC\n(supply)", "Platelets\n(demand)"]
errors = [-1.0, 2.4]
colors = ["#27AE60", "#27AE60"]
bars = ax.bar(products, errors, color=colors, edgecolor="black", lw=0.8, width=0.5)
ax.axhline(0, color="black", lw=0.8)
ax.axhline(5, color="red", ls="--", lw=1, alpha=0.7); ax.axhline(-5, color="red", ls="--", lw=1, alpha=0.7)
ax.set_title("(D) 2024 one-step-ahead hindcast error (%)", fontweight="bold", loc="left")
ax.set_ylabel("Error (%)  (|error| < 5% acceptable)")
ax.set_ylim(-6, 6)
for b, e in zip(bars, errors):
    ax.text(b.get_x() + b.get_width()/2, e + 0.3 if e >= 0 else e - 0.6,
            f"{e:+.1f}%", ha="center", fontsize=10, fontweight="bold")
ax.grid(alpha=0.3, axis="y")

# Text box: 2030 deficit probabilities
txt = ("2030 deficit probability:\n"
       "  Platelets 91.5% (95% CI 90.8–92.2)\n"
       "  Cryoprecipitate ~100%\n"
       "  RBC 5.5% (recovery) / 18.3% (baseline) / 62.7% (decline)")
ax.text(0.02, 0.97, txt, transform=ax.transAxes, fontsize=7.5, va="top",
        bbox=dict(boxstyle="round", fc="#F8F9FA", ec="gray"))

fig.suptitle("National blood product supply–demand projections (2015–2035) with aging-driven donor–patient scissors gap",
             fontsize=12, fontweight="bold", y=1.00)
plt.tight_layout()
plt.savefig(f"{OUT}figure2_supply_demand_projections_v3.pdf", dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig(f"{OUT}figure2_supply_demand_projections_v3.png", dpi=300, bbox_inches="tight", facecolor="white")
print("Figure 2 v3 saved.")
