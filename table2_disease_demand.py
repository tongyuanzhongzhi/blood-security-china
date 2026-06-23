#!/usr/bin/env python3
"""Build Table 2: disease-specific RBC demand breakdown for main text.
Extends dbdc_recomputed with evidence grade and source per disease."""
import json

# disease -> (rbc_mode_coef, patients_10k, evidence_grade, primary_source)
# evidence grade: 1° direct Chinese clinical data; 2° Chinese expert consensus;
#                 3° international data with Chinese adjustment; 4° expert elicitation
data = [
    ("Orthopaedic major surgery",        3.0, 50.0, "2°", "Chinese Orthopedic Association 2024"),
    ("ICU critical care (non-trauma)",   4.0, 30.0, "2°", "Wang Y et al. Chin Crit Care Med 2023"),
    ("Severe aplastic anaemia",         22.0,  5.0, "1°", "Chinese registry data"),
    ("Severe trauma",                   10.0, 10.0, "1°", "Chinese trauma registries"),
    ("MDS",                             12.0,  8.0, "2°", "Chinese expert consensus"),
    ("Thoracic/oncologic surgery",       3.0, 28.0, "2°", "Chinese clinical studies"),
    ("Postpartum haemorrhage",           8.0, 10.0, "1°", "Chin J Obstet Gynecol 2024"),
    ("GI bleeding",                      4.0, 20.0, "2°", "Chinese clinical studies"),
    ("Cancer-related anaemia",           5.0, 15.0, "2°", "CSCO guidelines 2024"),
    ("Acute leukemia",                  10.0,  6.5, "1°", "Chinese registry data"),
    ("Cardiovascular surgery",           2.5, 25.0, "1°", "CV Surgery White Paper 2024"),
    ("Peripartum anaemia (non-PPH)",     2.0, 27.0, "2°", "Chin J Obstet Gynecol 2024"),
    ("CKD anaemia",                      6.0,  8.3, "2°", "Chinese Society of Nephrology 2024"),
    ("Liver transplantation",            8.0,  0.69,"1°", "National Liver Transplant QC Centre 2023"),
    ("Haemophilia A (on-demand)",        2.0,  2.8, "1°", "Chinese registry data"),
    ("Haemophilia A (prophylaxis)",      0.0,  0.75,"1°", "Chinese registry data"),
]

total_supply = 2820.0  # 万 units
rows = [(name, coef*n, coef, n, grade, src) for (name, coef, n, grade, src) in data]
rows.sort(key=lambda r: -r[1])
captured = sum(r[1] for r in rows)
gap = total_supply - captured

print(f"{'Disease':<36}{'RBC万':>8}{'M units':>9}{'%cap':>7}{'%tot':>7}  {'Gr':<3} {'Source'}")
print("-"*120)
for name, dem, coef, n, grade, src in rows:
    print(f"{name:<36}{dem:>8.1f}{dem/100:>9.2f}{dem/captured*100:>6.1f}%{dem/total_supply*100:>6.1f}%  {grade:<3} {src}")
print("-"*120)
print(f"{'CAPTURED TOTAL':<36}{captured:>8.1f}{captured/100:>9.2f}{100.0:>6.1f}%{captured/total_supply*100:>6.1f}%")
print(f"{'UNCLASSIFIED GAP':<36}{gap:>8.1f}{gap/100:>9.2f}{'—':>7}{gap/total_supply*100:>6.1f}%")
print(f"{'TOTAL SUPPLY 2024':<36}{total_supply:>8.1f}{total_supply/100:>9.2f}{'—':>7}{100.0:>6.1f}%")

# Save for docx builder
out = {
    "rows": [{"disease":n, "demand_wan":round(d,1), "demand_M":round(d/100,2),
              "pct_captured":round(d/captured*100,1), "pct_total":round(d/total_supply*100,1),
              "grade":g, "source":s}
             for n,d,c,n2,g,s in rows],
    "captured_wan": round(captured,1),
    "captured_M": round(captured/100,2),
    "gap_wan": round(gap,1),
    "gap_M": round(gap/100,2),
    "total_supply_wan": total_supply,
    "capture_rate_pct": round(captured/total_supply*100,1),
    "gap_rate_pct": round(gap/total_supply*100,1),
}
with open("/Users/daizhensheng/Desktop/lancet/revised/table2_data.json","w") as f:
    json.dump(out,f,indent=2,ensure_ascii=False)
print("\nSaved table2_data.json")
