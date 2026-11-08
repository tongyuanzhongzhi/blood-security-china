# Projected platelet shortage and red-cell supply–demand balance in an ageing China: a compartmental model validated against three city blood centres

## Title Page

**Title:** Projected platelet shortage and red-cell supply–demand balance in an ageing China: a compartmental model validated against three city blood centres

**Running title:** Platelet shortage in ageing China

**Author:** Zhensheng Dai

**Affiliation:** Department of Hematology, Shanghai Pudong Hospital, Fudan University Pudong Medical Center, Shanghai, China

**Corresponding author:** Zhensheng Dai, MD. Department of Hematology, Shanghai Pudong Hospital, Fudan University Pudong Medical Center, No. 2800 Gongwei Road, Pudong New District, Shanghai 201399, China. Email: tongyuanzhongzhi@outlook.com. ORCID: 0009-0009-7476-8163.

**Word count:** 2,894 (main text, abstract, references, tables, and figure legends combined).

**Data Availability Statement:** The Python implementation and input data will be made available in a public repository upon acceptance. All input data are publicly available aggregate statistics.

**Funding:** No external funding was received.

**Conflict of Interest:** The author has no conflict of interest to declare.

---

## Abstract

**Background and Objectives:** Population ageing reduces the donor-eligible population while increasing transfusion demand, a structural pressure on blood supply in ageing societies. We quantified the ageing-driven supply–demand gap in China's blood-product system through 2030 and identified the highest-yield corrective interventions.

**Materials and Methods:** We developed the DPS-CM (Disease–Population–Supply Compartmental Model), coupling disease-specific demand (16 disease categories × 6 blood products), demographic projection (Leslie matrix), and supply capacity with demand-elasticity feedback. Forecasting accuracy was assessed by rolling-window cross-validation with Diebold–Mariano tests; Monte Carlo simulation (10,000 iterations) projected 2030 deficit probabilities. The model was validated against operational data from Shanghai, Beijing, and Shenzhen blood centres (2022–2024), with international comparison against Japan, Korea, and Germany.

**Results:** Drift forecasting outperformed the naive benchmark for platelets (Diebold–Mariano statistic 5.041; P = 0.015). The disease matrix captured 40.3% of red-cell demand. Monte Carlo simulation projected a near-certain deficit by 2030 for platelets (91.5%; 95% CI 90.8–92.2) and cryoprecipitate (100%), whereas red-cell adequacy was scenario-dependent (deficit probability 5.5% under donation-rate recovery to 12.0‰, 18.3% at baseline 11.2‰, and 62.7% under decline to 10.0‰). One-step-ahead hindcast errors for 2024 were −1.0% (red cells) and +2.4% (platelets).

**Conclusion:** China faces a near-certain platelet deficit by 2030, driven by a widening donor–patient ageing scissors gap. Extending platelet shelf life from 5 to 7 days, expanding apheresis capacity, and national patient blood management are the highest-priority interventions.

**Keywords:** blood supply; platelet transfusion; population ageing; compartmental model; patient blood management; China

## Highlights

- China faces a near-certain platelet deficit by 2030 (probability 91.5%; 95% CI 90.8–92.2).
- The donor–patient ageing scissors gap—donors ≥45 years rose from 12% to 28% while patients ≥60 years used 42% of blood—is the central structural threat.
- Extending platelet shelf life from 5 to 7 days and expanding apheresis capacity are the highest-yield corrective levers.
- A disease-based demand matrix captured only 40.3% of red-cell demand, exposing a data-infrastructure deficit that a diagnosis-linked registry would close.

---

## Introduction

Blood-product supply security—the reliable availability of safe blood for clinical use—depends on a stable donor population matched to clinical demand. In ageing societies this match is under structural strain: the transfusion-requiring population (aged ≥60 years) grows faster than the donor-eligible population (aged 18–60 years), creating a demographic scissors gap that organisational efficiency alone cannot close [1]. China, whose population aged ≥65 years is projected to exceed 20% by 2030, faces this challenge at a population scale of 1.4 billion.

Three pressures converge in China. First, demand is expanding through population ageing and surgical-volume growth (inpatient surgeries rose from 69.3 million in 2019 to 74.2 million in 2023) [2,3]. Second, supply is vulnerable: the national donation rate declined from 12.2‰ to 11.2‰ in 2024, ending six years of growth, while the proportion of donors aged ≥45 years rose from 12% to 28% over 2010–2023 [2]. Third, the absence of a nationally representative blood-utilisation registry forces demand forecasting to rely on aggregate statistics rather than clinical drivers [4,5].

The 2025 revision of China's Clinical Blood Use Technical Standards mandates patient blood management (PBM), including preoperative anaemia screening and restrictive transfusion triggers (haemoglobin <7 g/dL for stable adults, consistent with international guidelines) [5,6]. Translating this regulatory change into quantified impact requires a model linking disease-specific demand, demographic dynamics, and supply capacity. Previous studies have modelled individual components—disease-specific demand, demographic trends, or supply capacity—but no integrated model linking all three with empirical validation against operational data from multiple cities has been published for China.

We aimed to (i) develop an integrated compartmental model of China's blood supply–demand system; (ii) quantify the ageing-driven supply–demand gap through 2030; (iii) validate projections against operational data from three major Chinese cities; and (iv) identify the highest-yield corrective interventions through international comparison.

## Materials and Methods

### Model structure

We developed the DPS-CM, a three-compartment framework coupling disease demand, population evolution, and supply capacity with demand-elasticity feedback (Fig. 1). Data were drawn from publicly available sources [2,7,8,9,10] with explicit provenance tracking (evidence grades: 1°, direct Chinese clinical data; 2°, Chinese expert consensus). Whole-blood volumes are reported in million units (1 unit = 200 mL whole-blood equivalent); apheresis platelets in million therapeutic doses; donation rates per 1000 population (‰), consistent with WHO convention.

The D compartment computed product-specific demand via the D-BDC matrix: *D*_k(t) = Σ_d *c*_{d,k}·*N*_d(t) + *ε*_k(t), where *c*_{d,k} is the per-patient annual demand coefficient for disease d and product k, *N*_d(t) the number of transfusion-requiring patients, and *ε*_k(t) the residual (unclassified) demand. The matrix covered 16 disease categories and 6 blood products, with coefficient ranges (min, mode, max) for Triangular-distribution sampling (Supplementary Appendix A). The P compartment used Leslie-matrix projection with age-specific fertility and mortality from the United Nations World Population Prospects 2024 [11]. The S compartment projected component blood supply from the 2024 baseline (28.2 million units whole blood; 0.285 million apheresis-platelet doses), adjusted for donation-rate, population, and donor-eligible-proportion changes. A feedback mechanism adjusted demand when supply was constrained, with demand-elasticity coefficients of 0.15 for red cells and 0.05 for platelets, varied by ±50% in sensitivity analysis (Supplementary Appendix C).

### Forecasting and validation

Rolling-window cross-validation (10-fold for red cells, 4-fold for platelets) compared drift, SARIMA, and naive forecasting methods [12]. The Diebold–Mariano test with Newey–West heteroskedasticity- and autocorrelation-consistent variance assessed statistical significance; exact P values are reported owing to the limited number of cross-validation folds on short annual series (n = 7–15). Monte Carlo simulation (10,000 iterations) with Triangular and Poisson sampling for coefficients and disease incidence, respectively, projected 2030 deficit probabilities with bootstrap 95% confidence intervals (1000 resamples). Throughout, "deficit" denotes the model-projected state in which demand exceeds supply under current trends—a theoretical supply–demand gap—not a currently observed shortage in clinical supply.

Regional validation used operational data from Shanghai, Beijing, and Shenzhen blood centres (2022–2024), representing three distinct demographic profiles. Out-of-sample validation used the drift model fitted on 2010–2023 data to project 2024 values (one-step-ahead hindcast). International comparison drew on published models from Japan, Korea, and Germany. Full methods and the complete Python implementation are provided in the supplementary materials and the project repository [13].

### Ethics

The study used only publicly available aggregate data; ethics approval was not required.

## Results

In 2024, China collected 28.2 million units of whole blood, a 2.5% decline from 2023 (Fig. 2). Inter-provincial transfers reached 583,000 units (+35.1% year-on-year), indicating growing regional blood-supply imbalance. Patients aged ≥60 years accounted for 42% of clinical blood utilisation. Donors aged ≥45 years increased from 12% to 28% over 2010–2023, while the 18–25-year donor participation rate remained below 15%—establishing a widening donor–patient ageing scissors gap.

### Forecasting performance

Drift forecasting gave a lower mean absolute percentage error (MAPE) than SARIMA across all six blood-product categories (1.5–7.9% versus 2.8–12.3%). The Diebold–Mariano test confirmed that drift significantly outperformed the naive benchmark for platelets (statistic 5.041; P = 0.015). Drift did not significantly outperform SARIMA for any individual product (red cells: statistic −0.467, P = 0.651; platelets: statistic −0.978, P = 0.400). Drift was adopted as a parsimonious default for projection.

### Disease-specific demand

The expanded D-BDC matrix captured 11.37 million units of red-cell demand (40.3% of total supply). The five largest demand drivers were orthopaedic major surgery (1.50 million units, 13.2% of captured demand), intensive-care critical care (1.20 million, 10.6%), severe aplastic anaemia (1.10 million, 9.7%), severe trauma (1.00 million, 8.8%), and myelodysplastic syndromes (0.96 million, 8.4%) (Table 1). The 59.7% unclassified residual (16.83 million units) is dominated by perioperative demand (38%), chronic-disease transfusion (22%), emergency utilisation (10%), and diagnostic blood sampling (4%), with the remaining 26% of the residual attributed to miscellaneous non-indexed procedures. This unclassified component is the dominant source of forecast uncertainty.

### Deficit projections

Monte Carlo simulation projected three deficit tiers for 2030 (Fig. 3): near-certain deficit for platelets (probability 91.5%; 95% CI 90.8–92.2) and cryoprecipitate (deficit in all 10,000 iterations); scenario-dependent balance for red cells (deficit probability 5.5% [95% CI 1.9–11.3] under recovery to 12.0‰, 18.3% at baseline 11.2‰, 62.7% under decline to 10.0‰); and surplus under current trends for albumin and factor VIII. The platelet confidence interval is narrow (1.4 percentage points) because the projected gap is large relative to parameter uncertainty; the red-cell interval is wide (44.4 percentage points) because red cells sit near a tipping point. A bounded logistic dose–response analysis indicated that raising the donation rate from 11.2‰ to 12.0‰ would reduce the 2030 red-cell deficit probability from 18.3% to 5.5% (Fig. 4). The 2024 one-step-ahead hindcast yielded errors of −1.0% (red cells) and +2.4% (platelets).

### Regional validation

Regional validation confirmed platelet stress across all three cities. Shanghai, whose apheresis-platelet collections reached 104,221 units in 2025, would require 20 years to triple its platelet capacity. Beijing (20.1‰ donation rate) experienced inventory gaps exceeding 30% in summer 2024. Shenzhen (8% annual demand growth) requires 350 daily platelet donations. Mean absolute percentage errors were 4.2% (Shanghai), 3.8% (Beijing), and 6.1% (Shenzhen). Shenzhen's higher error reflects its migrant-population dynamics (57% of residents hold non-local hukou).

### International comparison

International comparison revealed shared structural pressures (Table 2). Germany's modelling demonstrated that extending platelet shelf life from 4 to 7 days reduces shortage rates from 2.8% to 0.2% [14]; China currently permits 5-day storage. Japan's donors aged ≥40 years constitute 62% of donations, a more advanced donor-ageing crisis. Korea's donor base fell by 26% over 2014–2024 despite a donation rate (5.6%) that remains among the highest globally. China's rate of 11.2‰ is the lowest among comparators.

## Discussion

Three findings carry direct implications for transfusion practice and blood-service planning in ageing societies.

First, the donor–patient ageing scissors gap is the central structural threat. Even Beijing, which achieved the highest donation rate nationally (20.1‰) through street-collection-point expansion, requires 72,000 units of inter-provincial transfers annually, demonstrating that donation-rate improvement alone cannot close the gap without structural supply augmentation.

Second, platelets face a near-certain structural deficit by 2030, driven by rising demand (8% per year in first-tier cities) and collection constraints (5-day shelf life, apheresis-donor requirements). Extending platelet shelf life to 7 days through pathogen-reduction technology, as demonstrated in Germany [14], would substantially reduce shortage rates, provided post-transfusion increments are monitored because pathogen-reduction may slightly lower platelet recovery; the equivalent gain for China, which currently permits 5-day storage, corresponds to the 5→7-day extension rather than the 4→7-day benchmark.

Third, the 59.7% demand-capture gap reveals a data-infrastructure deficit. Our bottom-up demand matrix, which captures only 40.3% of red-cell use, directly quantifies the scale of China's missing transfusion-utilisation data—a gap that a national blood-utilisation database linking diagnosis codes to transfusion episodes for China's 1876 tertiary hospitals would largely close (to approximately 85% capture). The 2025 Clinical Blood Use Technical Standards provide the regulatory foundation for such a registry [5].

Patient blood management is the most immediately actionable lever. Fuwai Hospital's programme reduced cardiac-surgery transfusion rates from approximately 70% to 33% [15], and national scaling could save 0.6–0.9 million red-cell units annually. We propose three corrective levers, ordered by feasibility: (i) expand apheresis-platelet capacity and establish inter-provincial allocation networks; (ii) deploy nationwide PBM targeting 10–15% perioperative demand reduction and extend platelet shelf life to 7 days; and (iii) develop a diagnosis-linked blood-utilisation registry and, in the longer term, invest in iPSC-derived platelet technology—the first-in-human trial was completed in Shanghai in 2025.

Several limitations apply. The 59.7% unclassified-demand component limits bottom-up accuracy; the D-BDC coefficients derive from published studies and guidelines [16,17,18,19,20] rather than patient-level data (a simulated-cohort internal-consistency check is described in Supplementary Appendix G); the 2024 hindcast covers a single year, because 2025 national statistics were not yet available at the time of analysis (2025 city-level data were used only for regional validation); and the three-city validation represents China's most developed regions. The demand-elasticity coefficients (0.15 for red cells, 0.05 for platelets) are judgement-based, though sensitivity analysis shifted the platelet deficit probability by less than 2 percentage points. The higher red-cell elasticity reflects the compressibility of red-cell use under restrictive patient-blood-management thresholds, whereas the lower platelet elasticity reflects the rigidity of platelet transfusion in patients undergoing chemotherapy or stem-cell transplantation, in whom prophylactic platelet thresholds are difficult to relax. The model does not incorporate potential technological disruptions (iPSC-derived products, synthetic blood substitutes) that could alter the supply–demand trajectory beyond 2030. We frame all findings as structural associations within a forecasting model and do not claim causal effects of any intervention. Nonetheless, the convergence of Monte Carlo simulation, three-city validation, and international comparison provides consistent evidence for the projected platelet deficit.

China must simultaneously manage a declining donation rate from an already low baseline, rising demand from expanding clinical access, and a structural platelet deficit—at a population scale 10–30 times larger than any comparator nation. The corrective levers—expanded apheresis capacity, platelet shelf-life extension to 7 days, nationwide patient blood management, and a diagnosis-linked registry—are transferable to other ageing societies. Without structural responses, the blood-supply gap is projected to widen as China's population aged ≥65 years exceeds 20% by 2030.

## Acknowledgements

The author thanks the Shanghai, Beijing, and Shenzhen blood centres for making their operational data publicly available. During the preparation of this work, a large language model was used as an assistance tool for literature organisation, statistical scripting, and language editing. All analyses were designed and independently verified by the author. No AI tool was used to generate primary data or draw scientific conclusions.

## References

1. World Health Organization. Global status report on blood safety and availability 2021. Geneva: WHO; 2022.
2. National Health Commission of China. Statistical Bulletin on the Development of Health Care in China 2024. Beijing; 2025.
3. Chinese Society of Extracorporeal Circulation. Chinese Cardiovascular Surgery White Paper 2024. Beijing; 2024.
4. UK Blood Transfusion and Tissue Transplantation Services. Annual SHOT Report 2023. Manchester: SHOT; 2024.
5. National Health Commission of China. Clinical Blood Use Technical Standards (2025 Edition). Beijing; 2025.
6. Carson JL, Brooks MM, Abbott JD, et al. Restrictive versus liberal transfusion thresholds for patients with acute myocardial infarction. JAMA. 2023;330:1152–62.
7. Shanghai Blood Centre. Annual operational data 2022–2024. https://www.shblood.org.cn (accessed 23 June 2026).
8. Beijing Red Cross Blood Centre. Annual operational data 2022–2024. https://wjw.beijing.gov.cn/sjfb/ (accessed 23 June 2026).
9. Shenzhen Blood Centre. Annual operational data 2022–2025. https://wjw.sz.gov.cn/szsxyzx/ (accessed 23 June 2026).
10. Japanese Red Cross Society. Blood service statistics 2024. https://www.jrc.or.jp/english/blood/ (accessed 23 June 2026).
11. United Nations, Department of Economic and Social Affairs, Population Division. World Population Prospects 2024. New York: United Nations; 2024.
12. Makridakis S, Spiliotis E, Assimakopoulos V. The M4 competition: 100,000 time series and 61 forecasting methods. Int J Forecast. 2020;36:54–74.
13. Dai Z. DPS-CM blood security model: reproducible code and data. GitHub; 2026. (repository to be made public upon acceptance)
14. Brixner V, Cardoso M, Spaepen E, Seifried E. Impact of shelf-life extension on platelet availability: results from an inventory management modelling study. Transfus Med Hemother. 2024;51(6):393–401.
15. Yao YT, Yuan X, He LX, et al. Patient blood management: single center evidence and practice at Fuwai Hospital. Chin Med Sci J. 2022;37(3):246–60.
16. Kidney Disease: Improving Global Outcomes (KDIGO) Anemia Work Group. KDIGO 2026 Clinical Practice Guideline for the Management of Anemia in Chronic Kidney Disease. Kidney Int. 2026;109(1S):S1–99.
17. Chinese Medical Association, Society of Blood Transfusion. Chinese guidelines for clinical blood transfusion (2022 revision). Chin J Blood Transfus. 2022;35(1):1–14.
18. Chinese Society of Nephrology. CKD anaemia management guidelines (2024 revision). Chin J Nephrol. 2024;40(3):185–212.
19. Chinese Society of Clinical Oncology. Clinical guidelines for cancer-related anaemia management 2024. Beijing; 2024.
20. Chinese Society of Blood Transfusion; Chinese Medical Association, Perinatal Medicine Branch. Expert consensus on obstetric blood transfusion therapy. Chin J Obstet Gynecol. 2024;59:257–71.

---

## Table 1. Disease-specific red-cell demand from the D-BDC matrix, 2024 baseline

| Disease category | Demand (million units) | % of captured | Evidence grade |
|---|---|---|---|
| Orthopaedic major surgery | 1.50 | 13.2 | 2° |
| ICU critical care (non-trauma) | 1.20 | 10.6 | 2° |
| Severe aplastic anaemia | 1.10 | 9.7 | 1° |
| Severe trauma | 1.00 | 8.8 | 1° |
| Myelodysplastic syndromes | 0.96 | 8.4 | 2° |
| Thoracic/oncologic surgery | 0.84 | 7.4 | 2° |
| Postpartum haemorrhage | 0.80 | 7.0 | 1° |
| Gastrointestinal bleeding | 0.80 | 7.0 | 2° |
| Cancer-related anaemia | 0.75 | 6.6 | 2° |
| Acute leukaemia | 0.65 | 5.7 | 1° |
| Cardiovascular surgery | 0.63 | 5.5 | 1° |
| Peripartum anaemia (non-PPH) | 0.54 | 4.7 | 2° |
| CKD anaemia | 0.50 | 4.4 | 2° |
| Haemophilia A (on-demand) | 0.06 | 0.5 | 1° |
| Liver transplantation | 0.06 | 0.5 | 1° |
| Haemophilia A (prophylaxis) | 0.00 | 0.0 | 1° |
| Captured total | 11.37 | 100.0 | — |
| Unclassified residual | 16.83 | — | — |
| Total red-cell supply 2024 | 28.20 | — | — |

1°, direct Chinese clinical data; 2°, Chinese expert consensus.

## Table 2. International comparison of ageing-driven blood supply–demand challenges

| Country | Population ≥65 years, % | Donation rate, ‰ | Key challenge | Policy response applicable to China |
|---|---|---|---|---|
| China | 15.9 (2025) | 11.2 (2024) | Three-fold pressure at 1.4B scale | National registry; PBM; apheresis expansion |
| Japan | 29.3 (2024) | ~40 (2024) | Donors ≥40 years: 62% | Structural supply augmentation |
| Korea | 19.2 (2024) | ~56 (2024) | Donors fell 26% over 2014–2024 | Donation-rate decline precedent |
| Germany | 22.8 (2024) | ~43 (2024) | Platelet shelf-life constraint | 4→7 days: shortage 2.8%→0.2% |

PBM: patient blood management. Population aged ≥65 years figures are the latest official census or UN projection available for each comparator (China 2025; Japan, Korea, Germany 2024).

## Figure Legends

**Fig. 1. DPS-CM framework architecture.** Three-compartment model coupling disease demand (16 categories × 6 products), population evolution (Leslie matrix), and supply capacity with elasticity feedback.

**Fig. 2. Historical blood collection and donation rate, China 2015–2024, with 2024 model validation.** (A) Total annual whole-blood collection volumes. (B) National annual blood donation rates per 1,000 population. (C) One-step-ahead hindcast percentage errors for red-cell supply and platelet demand.

**Fig. 3. 2030 deficit probabilities.** Monte Carlo simulation (10,000 iterations): near-certain platelet deficit (91.5%), scenario-dependent red cells (baseline 18.3%).

**Fig. 4. Red-cell deficit probability vs. donation rate, 2025–2030.** Logistic dose–response: rate increase from 11.2‰ to 12.0‰ reduces deficit probability from 18.3% to 5.5%.
