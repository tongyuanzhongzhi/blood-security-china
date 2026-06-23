#!/usr/bin/env python3
"""
Figure 4: RBC deficit probability vs national blood-donation rate (2025-30 scenario curve).

A bounded logistic dose-response curve P(dr) = 1/(1+exp(k*(dr-m))) calibrated to the
two Monte-Carlo anchor scenarios (baseline 11.2‰ -> 18.3%; decline 10.0‰ -> 62.7%).
The recovery scenario (12.0‰ -> 5.5%) is read off the curve. 95% CI band from a
10,000-replicate parametric bootstrap over anchor uncertainty (SE = 4 pp).
The three policy scenarios are marked.
"""
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "/Users/daizhensheng/Desktop/lancet/revised/"
SUB = OUT + "投稿/"
rng = np.random.default_rng(20260623)

# Anchors (donation rate per mille, RBC deficit probability)
dr_anchor = np.array([10.0, 11.2])
p_anchor  = np.array([0.627, 0.183])

def fit_logistic(dr, p):
    z = np.log(p / (1 - p))
    b = (z[1] - z[0]) / (dr[1] - dr[0])
    a = z[0] - b * dr[0]
    return -b, a / (-b)   # k, m

k, m = fit_logistic(dr_anchor, p_anchor)

def logistic(dr, m, k):
    return 1.0 / (1.0 + np.exp(k * (dr - m)))

# Bootstrap for CI band
dr_grid = np.linspace(9.0, 13.0, 200)
N = 10000
se = 0.04
boot = np.empty((N, len(dr_grid)))
for i in range(N):
    pa = np.clip(rng.normal(p_anchor, se), 0.01, 0.99)
    try:
        kb, mb = fit_logistic(dr_anchor, pa)
        boot[i] = logistic(dr_grid, mb, kb)
    except Exception:
        boot[i] = np.nan
ci_lo = np.nanpercentile(boot, 2.5, axis=0)
ci_hi = np.nanpercentile(boot, 97.5, axis=0)

# Scenarios to mark
scenarios = [
    (10.0, 0.627, "Decline\n(10.0‰)", "#C0392B"),
    (11.2, 0.183, "Baseline\n(11.2‰)", "#F39C12"),
    (12.0, 0.055, "Recovery\n(12.0‰)", "#27AE60"),
]

fig, ax = plt.subplots(figsize=(9.5, 6.2))

# CI band
ax.fill_between(dr_grid, ci_lo * 100, ci_hi * 100, color="#5DADE2", alpha=0.25,
                label="95% CI (bootstrap)")
# Curve
ax.plot(dr_grid, logistic(dr_grid, m, k) * 100, color="#2C3E50", lw=2.5,
        label="Logistic dose–response (calibrated to Monte-Carlo anchors)")

# Scenario points
for dr, p, lab, col in scenarios:
    ax.scatter([dr], [p * 100], s=120, color=col, edgecolor="black", lw=1.2, zorder=5)
    ax.annotate(f"{lab}\n{p*100:.1f}%", xy=(dr, p * 100),
                xytext=(dr + 0.15, p * 100 + 8), fontsize=9, fontweight="bold",
                color=col, arrowprops=dict(arrowstyle="-", color=col, lw=0.8))

# 50% threshold
ax.axhline(50, color="gray", ls="--", lw=1.2, alpha=0.7)
ax.text(13.0, 51.5, "50% threshold", fontsize=8, color="gray", ha="right")

# Highlight the policy-relevant range
ax.axvspan(11.2, 12.0, color="#27AE60", alpha=0.08)
ax.text(11.6, 92, "Policy target\nzone", fontsize=8, color="#27AE60",
        ha="center", style="italic")

ax.set_xlabel("National blood-donation rate (per 1,000 population, ‰)", fontsize=11)
ax.set_ylabel("Projected 2030 RBC deficit probability (%)", fontsize=11)
ax.set_title("RBC deficit probability vs donation-rate scenario (2025–30)",
             fontsize=12, fontweight="bold", loc="left")
ax.set_xlim(9.0, 13.0)
ax.set_ylim(0, 100)
ax.grid(alpha=0.3)
ax.legend(loc="upper right", fontsize=9)

# Footnote
ax.text(0.5, -0.16,
        "Curve calibrated to two Monte-Carlo anchor scenarios (baseline 11.2‰ → 18.3%; "
        "decline 10.0‰ → 62.7%); recovery (12.0‰ → 5.5%) read off the curve. "
        "95% CI from 10,000-replicate parametric bootstrap over anchor uncertainty.",
        transform=ax.transAxes, fontsize=7.5, ha="center", style="italic", color="gray")

plt.tight_layout()
os.makedirs(SUB, exist_ok=True)
for path, fname in [(OUT, "figure4_scenario_curve"),
                    (SUB, "07_Figure4_donation_rate_scenario")]:
    plt.savefig(f"{path}/{fname}.pdf", dpi=300, bbox_inches="tight", facecolor="white")
    plt.savefig(f"{path}/{fname}.png", dpi=300, bbox_inches="tight", facecolor="white")
print("Figure 4 saved to revised/ and 投稿/.")
