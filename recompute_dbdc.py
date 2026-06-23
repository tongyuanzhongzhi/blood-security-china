#!/usr/bin/env python3
"""Recompute D-BDC demand shares and OAT sensitivity from Appendix A mode values."""
import json

# Appendix A: (min, mode, max) for RBC U/pt-yr, and patients (10k, range)
# Using MODE values for point estimates, as the manuscript does.
diseases = [
    # name, RBC_mode, PLT_mode, FFP_mode, Cryo_mode, patients_10k
    ("Acute leukemia",                10, 8,  3, 0.5, 6.5),
    ("MDS",                            12, 6,  2, 0,   8.0),
    ("Severe aplastic anemia",         22, 12, 5, 2,   5.0),
    ("Hemophilia A (on-demand)",        2, 0,  0, 0,   2.8),
    ("Hemophilia A (prophylaxis)",      0, 0,  0, 0,   0.75),
    ("Postpartum hemorrhage",           8, 2,  5, 2,   10.0),
    ("Cardiovascular surgery",        2.5, 1,  4, 0,   25.0),
    ("Liver transplantation",           8, 8, 10, 3,   0.69),
    ("Severe trauma",                  10, 6,  8, 0,   10.0),
    ("GI bleeding",                     4, 0.5,2, 0,   20.0),
    ("CKD anemia",                      6, 0,  0, 0,   8.3),
    ("Cancer-related anemia",           5, 2,  0.5,0,  15.0),
    ("Orthopedic major surgery",        3, 0.5,1, 0,   50.0),
    ("ICU critical care (non-trauma)",  4, 1,  2, 0,   30.0),
    ("Peripartum anemia (non-PPH)",     2, 0,  0.5,0,  27.0),
    ("Thoracic/oncologic surgery",      3, 1,  2, 0,   28.0),
]

total_rbc_supply = 2820.0  # 万 units, 2024

rows = []
for name, rbc, plt, ffp, cryo, n in diseases:
    rbc_demand = rbc * n
    plt_demand = plt * n
    ffp_demand = ffp * n
    cryo_demand = cryo * n
    rows.append(dict(disease=name, rbc=rbc_demand, plt=plt_demand, ffp=ffp_demand,
                     cryo=cryo_demand, n=n, rbc_coef=rbc))

captured_rbc = sum(r["rbc"] for r in rows)
captured_plt = sum(r["plt"] for r in rows)
captured_ffp = sum(r["ffp"] for r in rows)
captured_cryo = sum(r["cryo"] for r in rows)

print("="*70)
print("D-BDC RECOMPUTED DEMAND (mode values, 万 units/yr)")
print("="*70)
print(f"{'Disease':<38}{'RBC':>7}{'PLT':>7}{'FFP':>7}{'Cryo':>7}{'N(10k)':>8}")
for r in sorted(rows, key=lambda x: -x["rbc"]):
    print(f"{r['disease']:<38}{r['rbc']:>7.1f}{r['plt']:>7.1f}{r['ffp']:>7.1f}{r['cryo']:>7.1f}{r['n']:>8.2f}")
print("-"*70)
print(f"{'CAPTURED TOTAL':<38}{captured_rbc:>7.1f}{captured_plt:>7.1f}{captured_ffp:>7.1f}{captured_cryo:>7.1f}")
print(f"\nTotal RBC supply (2024): {total_rbc_supply:.0f} 万 units")
print(f"Captured RBC demand: {captured_rbc:.1f} 万 ({captured_rbc/total_rbc_supply*100:.1f}% of total)")
print(f"Unclassified gap: {total_rbc_supply-captured_rbc:.1f} 万 ({(total_rbc_supply-captured_rbc)/total_rbc_supply*100:.1f}%)")

print("\n" + "="*70)
print("CORRECT % SHARE OF CAPTURED RBC DEMAND (must sum to 100%)")
print("="*70)
print(f"{'Disease':<38}{'RBC(万)':>9}{'%captured':>11}")
tot=0
for r in sorted(rows, key=lambda x: -x["rbc"]):
    pct = r["rbc"]/captured_rbc*100
    tot += pct
    print(f"{r['disease']:<38}{r['rbc']:>9.1f}{pct:>10.1f}%")
print(f"{'SUM':<38}{captured_rbc:>9.1f}{tot:>10.1f}%")

print("\nTop 5 RBC demand drivers (CORRECT ranking):")
for i, r in enumerate(sorted(rows, key=lambda x: -x["rbc"])[:5], 1):
    print(f"  {i}. {r['disease']}: {r['rbc']:.0f} 万 ({r['rbc']/captured_rbc*100:.1f}% of captured)")

# Newly added 4 categories
new4 = ["Orthopedic major surgery","ICU critical care (non-trauma)",
        "Peripartum anemia (non-PPH)","Thoracic/oncologic surgery"]
new4_total = sum(r["rbc"] for r in rows if r["disease"] in new4)
print(f"\n4 newly added categories total RBC: {new4_total:.0f} 万")
for name in new4:
    r = next(x for x in rows if x["disease"]==name)
    print(f"  {name}: {r['rbc']:.0f} 万")

# OAT sensitivity: ±20% in patient numbers OR coefficient -> ±20% in disease demand
# Impact on TOTAL CLASSIFIED demand = 0.2 * disease_demand / captured_rbc * 100
print("\n" + "="*70)
print("OAT SENSITIVITY: % change in total classified RBC demand per ±20% perturbation")
print("(patient numbers and coefficients enter multiplicatively, so columns identical)")
print("="*70)
print(f"{'Disease':<38}{'%captured':>11}{'±20% N impact':>15}{'±20% coef impact':>18}")
for r in sorted(rows, key=lambda x: -x["rbc"]):
    pct = r["rbc"]/captured_rbc*100
    impact = 0.2 * r["rbc"]/captured_rbc*100
    print(f"{r['disease']:<38}{pct:>10.1f}%{impact:>14.2f}%{impact:>17.2f}%")

# Save JSON
out = {
    "captured_rbc_10k_units": round(captured_rbc,1),
    "captured_plt_10k_units": round(captured_plt,1),
    "captured_ffp_10k_units": round(captured_ffp,1),
    "captured_cryo_10k_units": round(captured_cryo,1),
    "total_rbc_supply_10k_units": total_rbc_supply,
    "capture_rate_pct": round(captured_rbc/total_rbc_supply*100,1),
    "unclassified_gap_pct": round((total_rbc_supply-captured_rbc)/total_rbc_supply*100,1),
    "unclassified_gap_10k_units": round(total_rbc_supply-captured_rbc,1),
    "top5": [{"disease":r["disease"],"rbc_10k":round(r["rbc"],1),
              "pct_of_captured":round(r["rbc"]/captured_rbc*100,1)}
             for r in sorted(rows, key=lambda x:-x["rbc"])[:5]],
    "new4_total_10k": round(new4_total,1),
    "by_disease": [{"disease":r["disease"],"rbc_10k":round(r["rbc"],1),
                    "pct_of_captured":round(r["rbc"]/captured_rbc*100,1),
                    "sensitivity_20pct":round(0.2*r["rbc"]/captured_rbc*100,2)}
                   for r in sorted(rows, key=lambda x:-x["rbc"])],
}
with open("/Users/daizhensheng/Desktop/lancet/revised/dbdc_recomputed.json","w") as f:
    json.dump(out,f,indent=2,ensure_ascii=False)
print("\nSaved dbdc_recomputed.json")
