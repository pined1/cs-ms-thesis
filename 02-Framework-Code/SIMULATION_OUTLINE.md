# Simulation Outline for the Thesis
**David Pineda | BYU Computer Science MS**

13 experiments are implemented in `run_experiments.py`. This document maps each one to its role in the thesis.

---

## Tier 1 — Core Findings
*Chapter: Results (main section)*

These 4 experiments directly answer the thesis hypotheses. Every figure and table in the main results chapter comes from one of these.

---

### Experiment 1 — Learning Strategy Comparison *(H1)*

> Does broader knowledge sharing reduce incidents? Does the ordering GLOBAL < NEIGHBOR < LOCAL < NONE hold?

- **What it does:** Runs all 4 scenarios (NONE, LOCAL, NEIGHBOR, GLOBAL) with 20 teams, Watts-Strogatz network, 365 days, 100 seeds each
- **Output:** Mean total incidents + 95% CI per scenario — one bar chart, four bars
- **Note:** This is the central finding of the thesis. Everything else builds on it.

---

### Experiment 4 — Deployment Rate Sensitivity *(H2)*

> As teams deploy more frequently, does broader sharing mitigate the increased risk?

- **What it does:** Crosses 5 deployment rates (5%, 10%, 20%, 30%, 50%) × GLOBAL vs LOCAL — 10 conditions × 100 seeds
- **Output:** Line chart with two lines (GLOBAL, LOCAL) diverging as deployment rate rises. The gap is the "value of sharing under pressure"
- **Grounded in:** Forsgren et al. (2018) *Accelerate* — high deployment frequency is a real DevOps condition

---

### Experiment 8 — Organizational Conditions for NEIGHBOR ≈ GLOBAL *(H3)*

> At what org size and network connectivity does NEIGHBOR sharing stop being "good enough" (capturing ≥80% of GLOBAL's benefit)?

- **What it does:** Sweeps 5 team counts (6, 10, 20, 35, 50) × 3 topologies (Watts-Strogatz, Erdős-Rényi, Barabási-Albert) — 15 combinations × 3 scenarios (NONE, NEIGHBOR, GLOBAL) × 100 seeds
- **Output:** A 5×3 matrix of `benefit_ratio` values. Cells marked `*` where NEIGHBOR is good enough (ratio ≥ 0.8)
- **Note:** The novel, actionable finding. Tells a manager: if your org is under ~X teams with Y topology, you don't need company-wide broadcasts.

---

### Experiment 9 — Robustness Sweep *(H4)*

> Does the H1 ordering (GLOBAL < NEIGHBOR < LOCAL < NONE) hold across org sizes of 6, 20, and 50 teams?

- **What it does:** Runs all 4 scenarios × 3 team counts (6, 20, 50) with Watts-Strogatz — 12 conditions × 100 seeds
- **Output:** A 3-row table showing the H1 ordering replicates regardless of org size
- **Purpose:** Prevents the finding from being dismissed as specific to one org size

---

## Tier 2 — Validation Experiments
*Chapter: Results, subsection "Model Verification"*

Required under Sargent's (2020) simulation validation framework. Not additional findings — they confirm each model component contributes meaningfully before trusting the core results.

---

### Experiment 11 — Ablation: No Knowledge Decay

> If teams never forget what they learned, does reliability improve uniformly across all scenarios?

- **What it does:** Re-runs all 4 scenarios with `disable_knowledge_decay=True` vs default decay (`δ=0.001`)
- **Output:** Side-by-side table — incident counts with decay vs without decay per scenario
- **Confirms:** Decay is a meaningful model component. If results are identical, the parameter is dead weight. If they diverge, decay matters.

---

### Experiment 12 — Ablation: No Source-Team Advantage

> If the team that experienced an incident has no learning advantage over others, do outcomes change?

- **What it does:** Re-runs all 4 scenarios with `disable_source_asymmetry=True` vs default (source team learns directly, bypassing the 4-stage pipeline)
- **Output:** Side-by-side table — incident counts with asymmetry vs without
- **Confirms:** The source-team learning shortcut is a meaningful design assumption, not a cosmetic one

---

### Experiment 13 — Ablation: No Learning Cost

> If knowledge sharing were free (zero engineer-hours), does the optimal strategy change?

- **What it does:** Re-runs all 4 scenarios with `learning_cost=0` and `engineering_cost_base=0`
- **Output:** Side-by-side table of incident counts and total costs
- **Confirms:** Cost structure affects strategy choice — if GLOBAL and NEIGHBOR have the same incident count but different cost profiles, that matters for the H3 finding

---

## Tier 3 — Exploratory / Sensitivity
*Appendix, or 1–2 sentences in Results pointing to the appendix*

These 6 experiments enrich the story but are not core findings. Run them if time allows; they do not need to be in the main results chapter.

---

### Experiment 2 — Network Topology Effect

Compares 5 topologies (Erdős-Rényi, complete, Watts-Strogatz, Barabási-Albert, star) under NEIGHBOR scenario. Denser networks spread knowledge faster. Validates that the Watts-Strogatz choice in Experiment 1 is representative, not cherry-picked.

---

### Experiment 3 — Exploitation Effectiveness

Sweeps `prevention_effect` from 0.0 to 0.1. Shows how sensitive total incidents are to how much knowledge actually reduces incident rate. Validates that the `prevention_effect=0.5` default is in a meaningful range, not at a cliff edge.

---

### Experiment 5 — Documentation Quality Effect

Compares LOW (0.1) vs HIGH (0.9) documentation quality crossed with LOCAL and GLOBAL scenarios. Shows that poor postmortem quality cripples even the best sharing strategy. Relevant to practitioners but not a core thesis finding.

---

### Experiment 6 — Transformation Stage Sensitivity

Sweeps `transformation_probability` from 0.0 to 1.0. Validates that Stage 3 (the hardest cognitive step) is the bottleneck in the learning pipeline. If the curve is flat, transformation doesn't matter. If steep, it is the key lever.

---

### Experiment 7 — Transformation Mode (MINIMAL vs TIME-BASED)

Compares the default single-probability check against a multi-timestep effort accumulation model. Tests whether transformation dynamics (fast vs slow learning) change the strategy ordering. Primarily a model robustness check.

---

### Experiment 10 — Deployment × Learning Effectiveness Cross-Sweep

A 3×3 grid: 3 deployment rates × 3 exploitation probabilities under NEIGHBOR scenario. Validates that Experiment 4's findings are not dependent on a specific exploitation setting.

---

## Summary Table

| # | Name | Hypothesis | Tier | Seeds × Conditions |
|---|---|---|---|---|
| 1 | Learning Strategy Comparison | H1 | Core | 100 × 4 = 400 runs |
| 4 | Deployment Rate Sensitivity | H2 | Core | 100 × 10 = 1,000 runs |
| 8 | Org Conditions NEIGHBOR≈GLOBAL | H3 | Core | 100 × 45 = 4,500 runs |
| 9 | Robustness — Team Count | H4 | Core | 100 × 12 = 1,200 runs |
| 11 | Ablation: No Decay | Validation | Required | 100 × 8 = 800 runs |
| 12 | Ablation: No Asymmetry | Validation | Required | 100 × 8 = 800 runs |
| 13 | Ablation: No Cost | Validation | Required | 100 × 8 = 800 runs |
| 2 | Network Topology Effect | — | Appendix | 100 × 5 = 500 runs |
| 3 | Exploitation Effectiveness | — | Appendix | 100 × 5 = 500 runs |
| 5 | Documentation Quality | — | Appendix | 100 × 5 = 500 runs |
| 6 | Transformation Sensitivity | — | Appendix | 100 × 6 = 600 runs |
| 7 | Transformation Mode | — | Appendix | 100 × 4 = 400 runs |
| 10 | Deployment × Exploitation | — | Appendix | 100 × 9 = 900 runs |

**Total: ~12,900 simulation runs.**

Experiment 8 is the heaviest (4,500 runs) because of the 5×3 org condition sweep. It also produces the most novel result.

---

## Mapping to Committee-Approved Scope

The 7 experiments in `PROPOSAL_DEFENSE_SCOPE.md` map directly to:

| Scope doc label | Experiment # |
|---|---|
| Core: Learning Strategy Comparison | Experiment 1 |
| Core: Deployment Rate Sensitivity | Experiment 4 |
| Core: Org Conditions for NEIGHBOR≈GLOBAL | Experiment 8 |
| Core: Robustness Sweep | Experiment 9 |
| Ablation: No Knowledge Decay | Experiment 11 |
| Ablation: No Source-Team Advantage | Experiment 12 |
| Ablation: No Learning Cost | Experiment 13 |

Experiments 2, 3, 5, 6, 7, and 10 are implemented and working but were not included in the proposal scope document. They are bonus material — run them if time allows, put them in an appendix, and do not present them as core findings at the defense.
