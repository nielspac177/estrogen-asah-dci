# Menopausal state and delayed cerebral ischaemia after aneurysmal subarachnoid haemorrhage: a reproducible multi-database intensive-care pilot

**Authors.** N. Pacheco (and collaborators, TBD).

**Target reporting standard.** STROBE / RECORD-RWE (see `strobe_checklist.md`).

---

## Abstract

**Background.** Experimental subarachnoid-haemorrhage models indicate that
oestradiol attenuates cerebral vasospasm and delayed cerebral ischaemia (DCI),
and human cerebral endothelium expresses oestrogen receptors. Whether endogenous
oestrogen state modifies DCI risk after aneurysmal subarachnoid haemorrhage
(aSAH) has not been examined in humans, whereas the adjacent question of
sex-hormone genetics and aneurysm formation has already been addressed by
Mendelian randomisation.

**Methods.** We assembled a harmonised aSAH cohort from two intensive-care
databases, MIMIC-IV v3.1 and eICU-CRD v2.0, using version-controlled phenotype
codelists. The exposure was a menopausal-state proxy (premenopausal, age <51,
versus postmenopausal, ≥51) among women, with men retained as a reference. The
primary outcome was a DCI/vasospasm composite (coded cerebral vasospasm, rescue
cerebral angioplasty/intra-arterial vasodilator, or delayed cerebral
infarction). We fitted logistic regression with cluster-robust standard errors,
assessed covariate balance by inverse-probability weighting, pooled sources by
random-effects meta-analysis, and quantified unmeasured confounding with
E-values.

**Results.** Of 1,771 aSAH admissions (1,105 women — 313 premenopausal, 792
postmenopausal — and 666 men), 221 (12.5%) met the DCI composite. Crude DCI was
higher in premenopausal (16.3%) than postmenopausal women (10.4%), but
postmenopausal women also had higher in-hospital mortality (14.8% vs 7.7%),
consistent with a competing-risk effect on outcome ascertainment. After
adjustment, the odds of DCI for postmenopausal versus premenopausal women were
0.86 (95% CI 0.58–1.28; E-value 1.54, CI bound 1.0). The male-versus-female
estimate was 1.13 (0.97–1.31). Sources were directionally discordant (eICU 1.56,
MIMIC-IV 0.73; random-effects pooled 0.89, 0.46–1.73). An exploratory
in-hospital HRT-exposure analysis showed a positive association (OR 3.39,
1.70–6.76) most plausibly attributable to confounding by indication and
immortal-time bias.

**Conclusions.** In this underpowered pilot we found no significant association
between menopausal state and DCI after aSAH; the a priori oestrogen-protective
hypothesis was not supported. The analysis is limited by exposure misclassification,
competing mortality, source heterogeneity, and residual confounding, and should
be read as hypothesis-generating. It motivates a new-user registry target-trial
emulation and a triangulating Mendelian-randomisation analysis.

---

## Introduction

Delayed cerebral ischaemia is a leading determinant of outcome after aneurysmal
subarachnoid haemorrhage. Preclinical evidence has long suggested that oestrogen
is vasoprotective in this setting: ovariectomised animals rupture and infarct
more often, and 17β-oestradiol modulates endothelial nitric-oxide signalling and
endothelin-1 in SAH models. Human cerebral vessels express ERβ and GPER1,
providing a plausible substrate. Epidemiologically, aSAH incidence rises around
the menopausal transition, and reproductive-timing markers of lower lifetime
oestrogen exposure have been associated with higher aSAH risk in cohort studies.

Despite this rationale, the specific question of whether endogenous oestrogen
state alters the risk of DCI *after* aSAH has not, to our knowledge, been tested
in humans. The neighbouring causal question — whether genetically-proxied sex
hormones influence aneurysm formation or rupture — has already been examined by
at least two Mendelian-randomisation studies, which disagree on the direction of
the sex-hormone-binding-globulin effect. Intensive-care databases cannot emulate
a chronic-exposure target trial, but they capture acute, in-hospital neurological
outcomes in detail, and the mechanistically relevant exposure for DCI is
oestrogen *state* rather than cumulative use. We therefore conducted a
reproducible, multi-database pilot to estimate the association between menopausal
state and DCI after aSAH, and to build the analytical infrastructure for a
definitive study.

## Methods

### Data sources and study design

We used two publicly available, credentialed intensive-care databases, MIMIC-IV
v3.1 (a single US academic centre) and the multicentre eICU Collaborative
Research Database v2.0. The design is a pooled, cross-source cohort with source
treated as a clustering and stratification variable rather than an ignorable
covariate (see `docs/adr/0002-pooling-method.md`).

### Participants

Eligible admissions were adults with aneurysmal SAH. In MIMIC-IV this required a
nontraumatic SAH diagnosis (ICD-9 430; ICD-10 I60*) together with evidence of an
aneurysm — a cerebral-aneurysm diagnosis or an aneurysm-securing procedure
(surgical clipping or endovascular coiling). In eICU we used the APACHE admission
diagnosis "Subarachnoid haemorrhage/intracranial aneurysm" (with or without
surgery) or a haemorrhagic-stroke SAH diagnosis string, especially "from ruptured
berry aneurysm". Traumatic SAH and arteriovenous-malformation SAH were excluded.
eICU records were deduplicated to the first qualifying unit stay per person. All
phenotype definitions are version-controlled codelists (`config/codelists/`).

### Exposure, outcome, covariates

The primary exposure was a menopausal-state proxy among women — premenopausal
(age <51) versus postmenopausal (age ≥51), the threshold approximating the median
age at natural menopause. Men were retained as a reference for a secondary
sex-difference analysis. A secondary, exploratory exposure was in-hospital HRT.

The primary outcome was a DCI/vasospasm composite (any of: coded cerebral
vasospasm; rescue cerebral angioplasty or intra-arterial vasodilator; delayed
cerebral infarction). Nimodipine, being standard of care for all aSAH, was not
counted as a marker. Secondary outcomes were in-hospital mortality, poor
discharge disposition, and intensive-care length of stay. Covariates were age,
hypertension, current/former smoking, diabetes, aneurysm-treatment modality, and,
in eICU, APACHE severity.

### Statistical methods

The primary analysis was logistic regression of the DCI composite on menopausal
state, adjusted for measured confounders, with cluster-robust standard errors by
hospital. Because menopausal state is defined by an age threshold, age is
collinear with the exposure and was not used in the propensity model; balance on
the remaining confounders was assessed by inverse-probability weighting and
standardised mean differences. Source-specific estimates were pooled by
random-effects meta-analysis. Sensitivity analyses varied the composite
definition, examined the sex difference and HRT exposure, and quantified
unmeasured confounding with E-values. All analyses are scripted and reproducible
from a synthetic fixture without access to the source data.

## Results

The pooled cohort comprised 1,771 aSAH admissions: 1,105 women (313
premenopausal, 792 postmenopausal) and 666 men. DCI occurred in 221 (12.5%).
Baseline characteristics by stratum are shown in Table 1. Crude DCI was higher
among premenopausal (16.3%) than postmenopausal women (10.4%) and intermediate in
men (13.2%); however, postmenopausal women had markedly higher in-hospital
mortality (14.8% vs 7.7%), so that a competing-risk effect plausibly depresses
DCI ascertainment in the older, higher-oestrogen-deficit group.

After adjustment, the odds ratio for DCI in postmenopausal versus premenopausal
women was 0.86 (95% CI 0.58–1.28). The corresponding E-value was 1.54 with a
confidence-interval bound of 1.0, indicating that only modest unmeasured
confounding could account for the point estimate and that the interval already
includes the null. The secondary male-versus-female estimate was 1.13
(0.97–1.31). Inverse-probability weighting achieved good balance on measured
confounders (all |SMD| < 0.01 after weighting; e.g. hypertension 0.22 → 0.002).

The two sources were directionally discordant — eICU 1.56 and MIMIC-IV 0.73 —
although formal heterogeneity was limited (τ² ≈ 0.006); the random-effects pooled
estimate was 0.89 (0.46–1.73). The exploratory in-hospital HRT analysis showed a
strong positive association with DCI (OR 3.39, 1.70–6.76) that we do not
interpret causally: in-hospital hormone exposure is captured only during
admission and is subject to confounding by indication and immortal-time bias.

### Robustness and specification-curve analyses

Because the goal of recovering a positive finding invites analytical flexibility,
we ran a pre-specified specification curve (`multiverse.spec_curve`) spanning six
menopause age-cutoffs, two covariate sets, two outcome operationalisations, and
three source subsets (72 forks; ADR-0004/0005). Of 71 converging specifications,
41 were statistically significant — and **all 41 lay in the direction opposite to
the mechanistic hypothesis** (postmenopausal lower DCI); no significant fork
favoured the hypothesis. The one design that structurally separates menopause
from ageing, an age×sex restricted-cubic-spline difference-in-differences with men
as a chronological-ageing reference (`multiverse.age_sex_did`), was null
(OR-ratio for a female-specific rise in DCI odds across the transition 1.04, 95%
CI 0.62–1.76). Competing-mortality sensitivities (survivor restriction,
outcome-component variants) were reported but are interpreted only as concordance
checks, as each can move the estimate mechanically.

## Discussion

In this reproducible multi-database pilot we found no significant association
between menopausal state and DCI after aSAH, and the a priori oestrogen-protective
hypothesis was not supported in any defensible analysis. An independent adversarial
methodological audit (`docs/audit/`) identified the dominant threat not as
competing mortality but as **non-identifiability**: because menopausal state is a
deterministic function of age in these data, there is no age overlap across strata,
and age has a direct effect on vasospasm (younger patients have more) that is
collinear with the exposure and runs opposite to the hypothesis. The crude
"premenopausal-excess" pattern is therefore most parsimoniously a chronological-
ageing and differential-ascertainment signal rather than evidence of an oestrogen
effect masked by survival bias. Consistent with this, the specification curve
yielded significant results exclusively in the anti-hypothesis direction, and the
age×sex difference-in-differences — the only estimand that nets out shared ageing —
was null.

Several limitations dominate interpretation. First, exposure is a coarse
age-based proxy for oestrogen state, and age and menopause cannot be fully
disentangled. Second, the DCI composite depends on coding that is insensitive in
the ICD-9 era, and the two sources code vasospasm differently, producing the
observed heterogeneity. Third, in-hospital mortality competes with DCI
ascertainment. Fourth, the cohort is modest and the analysis is underpowered for
the stratified contrasts of interest. Finally, the HRT signal illustrates rather
than resolves the confounding that motivates a stronger design.

These findings should be read as hypothesis-generating. They motivate two
complementary next steps that are robust to the biases seen here: a new-user,
active-comparator target-trial emulation of hormone therapy in longitudinal
registry data, and a triangulating Mendelian-randomisation analysis using public
GWAS summary statistics. The pipeline and phenotype definitions developed here
are released to support both.

## Data and code availability

All code, phenotype codelists, and a synthetic fixture that reproduces the full
pipeline without credentialed data are available at the project repository. No
patient-level data are included; MIMIC-IV and eICU-CRD require PhysioNet
credentialing.

*Note: numeric results above were produced by the analysis pipeline on the local
credentialed data (`outputs/`, git-ignored); rerun `make all` with
`config/paths.yaml` set to regenerate.*
