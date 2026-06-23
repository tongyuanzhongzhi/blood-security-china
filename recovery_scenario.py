#!/usr/bin/env python3
"""
Derive the recovery-scenario RBC deficit probability.

The original Monte Carlo produced two documented anchor points:
  - baseline 11.2 per mille -> 18.3% deficit probability
  - decline  10.0 per mille -> 62.7% deficit probability
The recovery scenario (12.0 per mille) was not reported in v5.

We fit a bounded logistic dose-response curve (deficit probability vs
donation rate) to the two anchors and read off P(12.0). A logistic is the
standard monotonic dose-response shape and is bounded in [0,1], unlike the
linear extrapolation used in v6 draft (which gave a nonsensical 3.2% near
the boundary). 95% CI from a 10,000-replicate parametric bootstrap over
anchor uncertainty (anchor SE = 4 percentage points, reflecting the wide
RBC uncertainty interval).
"""
import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm

rng = np.random.default_rng(20260622)

# Anchors
dr_anchor = np.array([10.0, 11.2])
p_anchor  = np.array([0.627, 0.183])

def logistic(dr, m, k):
    return 1.0 / (1.0 + np.exp(k * (dr - m)))

def fit_logistic(dr, p):
    """Solve for midpoint m and slope k from two points.
    P = 1/(1+exp(k*(dr-m)))  =>  logit(P) = -k*(dr-m) = k*m - k*dr
    So logit(P) = a + b*dr with b=-k, a=k*m. Two points -> exact line."""
    z = np.log(p / (1 - p))          # logit
    # linear fit z = a + b*dr
    b = (z[1] - z[0]) / (dr[1] - dr[0])
    a = z[0] - b * dr[0]
    k = -b
    m = a / k
    return m, k

m, k = fit_logistic(dr_anchor, p_anchor)
print(f"Logistic fit: midpoint m = {m:.4f} per mille, slope k = {k:.4f}")
print(f"  Check P(10.0) = {logistic(10.0, m, k):.4f}  (target 0.627)")
print(f"  Check P(11.2) = {logistic(11.2, m, k):.4f}  (target 0.183)")

recovery_dr = 12.0
p_recovery = logistic(recovery_dr, m, k)
print(f"\nRecovery scenario (12.0 per mille): P(deficit) = {p_recovery:.4f} = {p_recovery*100:.1f}%")

# Parametric bootstrap: perturb anchors within SE, refit, get CI
N = 10000
se = 0.04   # 4 percentage-point SE per anchor
boot = np.empty(N)
for i in range(N):
    pa = np.clip(rng.normal(p_anchor, se), 0.01, 0.99)
    try:
        mb, kb = fit_logistic(dr_anchor, pa)
        boot[i] = logistic(recovery_dr, mb, kb)
    except Exception:
        boot[i] = np.nan
boot = boot[~np.isnan(boot)]
ci_lo, ci_hi = np.percentile(boot, [2.5, 97.5])
print(f"  95% CI (bootstrap, N={N}): {ci_lo*100:.1f}% – {ci_hi*100:.1f}%")

# Also report the full three-scenario curve
print("\nFull dose-response (donation rate -> RBC deficit probability):")
for dr in [9.0, 9.5, 10.0, 10.5, 11.0, 11.2, 11.5, 12.0, 12.5, 13.0]:
    print(f"  {dr:.1f} per mille -> {logistic(dr, m, k)*100:5.1f}%")

print(f"\nFINAL: recovery (12.0 per mille) = {p_recovery*100:.1f}% (95% CI {ci_lo*100:.1f}-{ci_hi*100:.1f})")
