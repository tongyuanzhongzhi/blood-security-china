#!/usr/bin/env python3
"""
Generate 4 figures for Vox Sanguinis submission.
All data from real source files (no fabricated projections).

Fig 1: DPS-CM framework (schematic, 3 compartments)
Fig 2: Historical blood collection & donation rate 2015-2024 + 2024 hindcast (REAL data)
Fig 3: 2030 deficit probabilities (Monte Carlo, real)
Fig 4: RBC deficit probability vs donation rate (logistic, real anchors)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans'],
    'font.size': 10,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.unicode_minus': False,
})

OUT = ""

# Okabe-Ito palette
BLUE   = "#0072B2"
ORANGE = "#D55E00"
GREEN  = "#009E73"
RED    = "#CC0000"
YELLOW = "#E69F00"
SKY    = "#56B4E9"
GREY   = "#555555"

def save(fig, name):
    for ext in ['png', 'pdf']:
        fig.savefig(f"{OUT}{name}.{ext}", dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"Saved {name}.png/.pdf")

# ============ Fig 1: DPS-CM framework ============
def fig1():
    fig, ax = plt.subplots(figsize=(10, 5.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.2); ax.axis('off')

    def box(x, y, w, h, title, body, color):
        ax.add_patch(mpatches.Rectangle((x, y), w, h, fc=color, ec='black', lw=1.2))
        ax.text(x+w/2, y+h-0.25, title, ha='center', va='top', fontsize=10.5, fontweight='bold')
        ax.text(x+w/2, y+h/2-0.1, body, ha='center', va='center', fontsize=8.5)

    def arrow(x1, y1, x2, y2, color='black'):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='-|>', color=color, lw=2.0, mutation_scale=18))

    box(0.4, 3.2, 2.9, 1.6, "D: Disease demand", "16 categories \u00d7 6 products\nD-BDC matrix\nD_k(t) = \u03a3 c_{d,k}\u00b7N_d(t) + \u03b5_k(t)", SKY)
    box(3.7, 3.2, 2.5, 1.6, "P: Population", "population ageing projection\n65+ share 15.9% \u2192 20%\n(UN WPP 2024)", GREEN)
    box(6.6, 3.2, 3.0, 1.6, "S: Supply capacity", "2024 baseline\n28.2 M units whole blood\n0.285 M platelet doses", ORANGE)
    box(3.7, 0.6, 5.9, 1.5, "Elasticity feedback", "\u03b7 = 0.15 (red cells), 0.05 (platelets)\ndemand adjusted when supply constrained", "#DDDDDD")

    arrow(3.3, 4.0, 3.7, 4.0)   # D -> P
    arrow(6.2, 4.0, 6.6, 4.0)   # P -> S
    arrow(8.1, 3.2, 6.9, 2.1)   # S -> feedback (down)
    arrow(3.7, 2.1, 2.0, 3.2)   # feedback -> D (back up)
    ax.text(7.6, 2.45, "constraint", fontsize=8, color=GREY, style='italic',
            ha='center', bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.9))

    ax.text(0.4, 0.15, "Fig. 1. DPS-CM framework: disease demand (D), population ageing projection (P), and supply capacity (S)\ncoupled with demand-elasticity feedback.", fontsize=8.5, style='italic', color=GREY)
    save(fig, "Fig1_DPS-CM_framework")

# ============ Fig 2: Historical trends + hindcast ============
def fig2():
    years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
    collection = np.array([22.20, 23.60, 24.78, 25.60, 26.40, 25.50, 28.56, 27.60, 28.92, 28.20])  # million units
    rate = np.array([9.6, 10.1, 10.5, 10.9, 11.2, 10.7, 12.0, 11.4, 12.2, 11.2])  # per mille

    fig, axes = plt.subplots(1, 3, figsize=(13, 4.2))

    # Panel A: collection
    ax = axes[0]
    ax.plot(years, collection, 'o-', color=BLUE, lw=2, ms=5)
    ax.set_title("(A) Whole-blood collection", fontweight='bold', loc='left', fontsize=10)
    ax.set_xlabel("Year"); ax.set_ylabel("Million units")
    ax.annotate("2023 peak\n28.92", xy=(2023, 28.92), xytext=(2021.0, 29.0),
                fontsize=8, arrowprops=dict(arrowstyle='->', color=GREY, lw=0.8),
                bbox=dict(boxstyle='round,pad=0.25', fc='white', ec='grey', lw=0.5, alpha=0.95))
    ax.annotate("2024: \u22122.5%", xy=(2024, 28.20), xytext=(2020.6, 26.4),
                fontsize=8, color=RED, arrowprops=dict(arrowstyle='->', color=RED, lw=0.8),
                bbox=dict(boxstyle='round,pad=0.25', fc='white', ec='none', alpha=0.95))
    ax.set_xticks([2015, 2017, 2019, 2021, 2023]); ax.grid(alpha=0.3)

    # Panel B: donation rate
    ax = axes[1]
    ax.plot(years, rate, 's-', color=GREEN, lw=2, ms=5)
    ax.set_title("(B) Donation rate", fontweight='bold', loc='left', fontsize=10)
    ax.set_xlabel("Year"); ax.set_ylabel("Per 1,000 population (\u2030)")
    ax.annotate("12.2\u2030 (2023)", xy=(2023, 12.2), xytext=(2021.0, 12.3),
                fontsize=8, arrowprops=dict(arrowstyle='->', color=GREY, lw=0.8),
                bbox=dict(boxstyle='round,pad=0.25', fc='white', ec='grey', lw=0.5, alpha=0.95))
    ax.annotate("11.2\u2030 (2024)\nlowest among\ncomparators", xy=(2024, 11.2), xytext=(2020.1, 10.2),
                fontsize=8, color=RED, arrowprops=dict(arrowstyle='->', color=RED, lw=0.8),
                bbox=dict(boxstyle='round,pad=0.25', fc='white', ec='none', alpha=0.95))
    ax.set_xticks([2015, 2017, 2019, 2021, 2023]); ax.grid(alpha=0.3)

    # Panel C: hindcast
    ax = axes[2]
    labels = ["Red cells\n(supply)", "Platelets\n(demand)"]
    errors = [-1.0, 2.4]
    colors = [BLUE, ORANGE]
    bars = ax.bar(labels, errors, color=colors, edgecolor='black', lw=0.8, width=0.5)
    ax.axhline(0, color='black', lw=0.8)
    ax.axhline(5, color=RED, ls='--', lw=1, alpha=0.7)
    ax.axhline(-5, color=RED, ls='--', lw=1, alpha=0.7)
    ax.set_title("(C) 2024 one-step-ahead\nhindcast error", fontweight='bold', loc='left', fontsize=10)
    ax.set_ylabel("Error (%)")
    ax.set_ylim(-6, 6)
    for b, e in zip(bars, errors):
        ax.text(b.get_x()+b.get_width()/2, e+0.3 if e>=0 else e-0.6, f"{e:+.1f}%",
                ha='center', fontsize=10, fontweight='bold')
    ax.grid(alpha=0.3, axis='y')

    fig.suptitle("Historical blood collection and donation rate, China 2015\u20132024, with 2024 hindcast validation",
                 fontsize=11.5, fontweight='bold', y=1.02)
    fig.tight_layout()
    save(fig, "Fig2_historical_trends")

# ============ Fig 3: 2030 deficit probabilities ============
def fig3():
    fig, ax = plt.subplots(figsize=(9, 5.8))
    labels = ["Red blood cells", "Platelets", "Cryoprecipitate"]
    probs = [18.3, 91.5, 100.0]
    colors = [YELLOW, RED, "#A04040"]
    rbc_lo, rbc_hi = 5.5, 62.7

    x = np.arange(len(labels))
    bars = ax.bar(x, probs, 0.52, color=colors, edgecolor='#333333', linewidth=0.7, zorder=3)

    ax.errorbar(x[0], probs[0], yerr=[[probs[0]-rbc_lo], [rbc_hi-probs[0]]],
                fmt='none', ecolor='#333333', capsize=10, capthick=1.8, lw=2.2, zorder=5)

    ax.text(x[0]-0.35, probs[0]+1.5, '18.3%', ha='center', va='bottom', fontsize=13, fontweight='bold', color='#333333')
    ax.text(x[1], probs[1]+3, '91.5%', ha='center', va='bottom', fontsize=13, fontweight='bold', color='#333333')
    ax.text(x[2], 72, '100%', ha='center', va='center', fontsize=12, fontweight='bold', color='white')

    ax.text(x[1], -14, '95% CI 90.8\u201392.2', ha='center', va='center', fontsize=8.5, color=GREY)
    ax.text(x[2], -14, '100% (95% CI 99.97\u2013100%)', ha='center', va='center', fontsize=8.5, color=GREY)
    ax.text(x[0], -14, 'baseline 11.2\u2030;\nrange 5.5\u201362.7%', ha='center', va='center', fontsize=8.5, color=GREY)

    ax.axhline(y=50, color='#888888', linestyle='--', linewidth=1.0, alpha=0.6, zorder=1)
    ax.text(-0.45, 52, '50%', fontsize=8.5, color='#888888', ha='left', va='bottom')

    ax.text(x[1], 107, 'Near-certain deficit', ha='center', va='bottom', fontsize=8, style='italic', color='#C0392B')
    ax.text(x[2], 107, 'Certain deficit', ha='center', va='bottom', fontsize=8, style='italic', color='#A04040')
    ax.text(x[0], 107, 'Scenario-dependent', ha='center', va='bottom', fontsize=8, style='italic', color='#D35400')

    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=11)
    ax.set_ylabel('2030 deficit probability (%)', fontsize=12, fontweight='bold')
    ax.set_ylim(0, 112); ax.set_xlim(-0.65, 2.65)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.2, zorder=0)

    ax.set_title('2030 deficit-probability projections\n(Monte Carlo simulation, 10,000 iterations)',
                 fontsize=13, fontweight='bold', loc='left', pad=14)

    fig.text(0.5, 0.02, 'RBC baseline 11.2\u2030; range 5.5\u201362.7% across donation-rate scenarios (recovery 12.0\u2030 to decline 10.0\u2030). '
             'Albumin and FVIII adequate under current trends (not shown).',
             ha='center', fontsize=7.5, style='italic', color='#777777')
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    save(fig, "Fig3_deficit_probabilities")

# ============ Fig 4: RBC deficit probability vs donation rate ============
def fig4():
    rng = np.random.default_rng(20260623)
    dr_anchor = np.array([10.0, 11.2])
    p_anchor  = np.array([0.627, 0.183])

    def fit_logistic(dr, p):
        z = np.log(p / (1 - p))
        b = (z[1] - z[0]) / (dr[1] - dr[0])
        a = z[0] - b * dr[0]
        return -b, a / (-b)

    k, m = fit_logistic(dr_anchor, p_anchor)
    def logistic(dr, m, k):
        return 1.0 / (1.0 + np.exp(k * (dr - m)))

    dr_grid = np.linspace(9.0, 13.0, 200)
    N = 10000; se = 0.04
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

    scenarios = [
        (10.0, 0.627, "Decline\n(10.0\u2030)", RED),
        (11.2, 0.183, "Baseline\n(11.2\u2030)", YELLOW),
        (12.0, 0.055, "Recovery\n(12.0\u2030)", GREEN),
    ]

    fig, ax = plt.subplots(figsize=(9.5, 6.2))
    ax.fill_between(dr_grid, ci_lo*100, ci_hi*100, color=SKY, alpha=0.25, label='95% CI (bootstrap)')
    ax.plot(dr_grid, logistic(dr_grid, m, k)*100, color='#2C3E50', lw=2.5,
            label='Logistic dose\u2013response (calibrated to Monte-Carlo anchors)')

    for dr, p, lab, col in scenarios:
        ax.scatter([dr], [p*100], s=120, color=col, edgecolor='black', lw=1.2, zorder=5)
        ax.annotate(f"{lab}\n{p*100:.1f}%", xy=(dr, p*100), xytext=(dr+0.15, p*100+8),
                    fontsize=9, fontweight='bold', color=col,
                    arrowprops=dict(arrowstyle='-', color=col, lw=0.8))

    ax.axhline(50, color='gray', ls='--', lw=1.2, alpha=0.7)
    ax.text(13.0, 51.5, '50% threshold', fontsize=8, color='gray', ha='right')
    ax.axvspan(11.2, 12.0, color=GREEN, alpha=0.12)
    ax.text(11.6, 92, 'Donation recovery corridor\n(11.2\u201312.0\u2030)', fontsize=8.5, color='#00663d',
            ha='center', style='italic', fontweight='bold')

    ax.set_xlabel('National blood-donation rate (per 1,000 population, \u2030)', fontsize=11)
    ax.set_ylabel('Projected 2030 RBC deficit probability (%)', fontsize=11)
    ax.set_title('RBC deficit probability vs donation-rate scenario (2025\u201330)',
                 fontsize=12, fontweight='bold', loc='left')
    ax.set_xlim(9.0, 13.0); ax.set_ylim(0, 100)
    ax.grid(alpha=0.3); ax.legend(loc='lower left', fontsize=9)

    ax.text(0.5, -0.16,
            'Curve calibrated to two Monte-Carlo anchor scenarios (baseline 11.2\u2030 \u2192 18.3%; decline 10.0\u2030 \u2192 62.7%); '
            'recovery (12.0\u2030 \u2192 5.5%) read off the curve. 95% CI from 10,000-replicate parametric bootstrap.',
            transform=ax.transAxes, fontsize=7.5, ha='center', style='italic', color='gray')
    plt.tight_layout()
    save(fig, "Fig4_donation_rate_scenario")

if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    fig4()
    print("All 4 figures generated.")
