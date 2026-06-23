#!/usr/bin/env python3
"""
Figure 3 v5: 2030 deficit-probability projections (single full-width panel).
v5 removes the cramped international-comparison table (former Panel B), which
duplicated Table 2 and whose 6-column text did not fit the subplot. The
international comparison now lives solely in Table 2 (manuscript). Figure 3
is a clean, full-width deficit-probability bar chart.
"""
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = "/Users/daizhensheng/Desktop/lancet/revised/"

fig, ax = plt.subplots(figsize=(10, 6.5))

categories = ["RBC\n(scenario-dependent)", "Platelets", "Cryoprecipitate"]
probabilities = [18.3, 91.5, 100.0]
rbc_lo, rbc_hi = 5.5, 62.7
colors = ["#F39C12", "#E74C3C", "#C0392B"]

bars = ax.bar(categories, probabilities, color=colors, edgecolor="black",
              linewidth=0.9, width=0.50)

# RBC error bar spanning the scenario range
ax.errorbar(0, 18.3, yerr=[[18.3 - rbc_lo], [rbc_hi - 18.3]], fmt="none",
            ecolor="black", capsize=12, lw=2, zorder=5)

# RBC annotation in the top-left corner (boxed), clear of all bars.
ax.annotate("Baseline 18.3%\n(range 5.5–62.7% across\ndonation-rate scenarios)",
            xy=(0, 62.7), xytext=(0.015, 0.93), textcoords="axes fraction",
            fontsize=9.5, fontweight="bold", ha="left", va="top",
            arrowprops=dict(arrowstyle="-", color="gray", lw=0.8,
                            connectionstyle="arc3,rad=-0.2"),
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="#F39C12", lw=0.9))

# Platelets label above its bar.
ax.text(1, 91.5 + 3, "91.5%\n(95% CI 90.8–92.2)", ha="center", va="bottom",
        fontsize=10, fontweight="bold")

# Cryoprecipitate inside the bar (white).
ax.text(2, 92, "10,000 / 10,000\niterations", ha="center", va="top",
        fontsize=10, fontweight="bold", color="white")

# 50% threshold line
ax.axhline(y=50, color="gray", linestyle="--", linewidth=1.3, alpha=0.7)
ax.text(-0.55, 51.5, "50% threshold", fontsize=8.5, color="gray", ha="left", va="bottom")

# Tier captions (right margin, boxed, clear of bars).
ax.text(2.62, 100, "Near-certain\ndeficit", fontsize=9, ha="left", va="top",
        color="#C0392B", style="italic",
        bbox=dict(boxstyle="round,pad=0.3", fc="#FDEDEC", ec="#C0392B", lw=0.6))
ax.text(2.62, 55, "Scenario-\ndependent", fontsize=9, ha="left", va="top",
        color="#D35400", style="italic",
        bbox=dict(boxstyle="round,pad=0.3", fc="#FEF5E7", ec="#D35400", lw=0.6))

ax.set_ylabel("Deficit probability (%)", fontsize=12, fontweight="bold")
ax.set_ylim(0, 115)
ax.set_xlim(-0.6, 3.4)
ax.set_title("2030 deficit-probability projections (Monte Carlo, 10,000 iterations)",
             fontsize=13, fontweight="bold", loc="left", pad=10)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(axis="x", labelsize=11)
ax.tick_params(axis="y", labelsize=10)
ax.grid(axis="y", alpha=0.25)

ax.text(0.5, -0.12,
        "Albumin and FVIII adequate under current trends (not shown). "
        "RBC bar = baseline scenario (11.2‰); error bar spans recovery (12.0‰, 5.5%) to decline (10.0‰, 62.7%). "
        "International comparison data are tabulated in Table 2.",
        transform=ax.transAxes, fontsize=8, ha="center", style="italic", color="gray")

plt.tight_layout()

# Save to revised/ and both submission folders.
targets = [
    (OUT, "figure3_deficit_international_v5"),
    (OUT + "投稿/", "06_Figure3_deficit_international"),
    ("/Users/daizhensheng/Desktop/IJHPM/", "Figure3_deficit_international"),
]
for path, fname in targets:
    plt.savefig(f"{path}{fname}.pdf", dpi=300, bbox_inches="tight", facecolor="white")
    plt.savefig(f"{path}{fname}.png", dpi=300, bbox_inches="tight", facecolor="white")
print("Figure 3 v5 (single panel) saved to revised/, 投稿/, and IJHPM/.")
