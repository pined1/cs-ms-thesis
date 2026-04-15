# Experiments Reference
**David Pineda | BYU Computer Science MS**
**Last updated: March 27, 2026**

---

## Critical Model Change — Read First

**`use_inverted_u` changed from `True` → `False` (default)**

All experiments now run with **linear similarity** (`cognitive_factor = similarity`) for assimilation and transformation stages.

- **Before:** Nooteboom inverted-U — suppressed learning between similar teams (wrong for incident learning)
- **After:** Cohen & Levinthal linear — similar teams assimilate more easily (correct direction)
- **Impact:** All experiments that involve cross-team learning are affected. Any pilot results from before this change used the wrong cognitive model. Re-run everything.

---

## How to Run

```bash
python run_experiments.py                  # All 13 experiments (100 seeds each)
python run_experiments.py --experiment 1   # Single experiment by number
python run_experiments.py --quick          # 5 seeds — fast sanity check
```

Results saved to `thesis_results/` as timestamped JSON files.

---

## Tier 1 — Core Hypothesis Experiments

These directly answer H1–H4 from the proposal. Every figure in the main results chapter comes from one of these.

---

### Experiment 1 → H1: Learning Strategy Comparison

**Hypothesis:** Broader sharing reduces total incidents: GLOBAL < NEIGHBOR < LOCAL < NONE
**Rejection criterion:** If ordering fails in >80% of parameter configurations

**Parameters:**
- 20 teams, Watts-Strogatz network, 365 days
- 100 seeds
- `base_incident_rate=0.05`, `deployment_rate=0.1`

**What to look for:**
- Bar chart: NONE > LOCAL > NEIGHBOR > GLOBAL in mean incident count
- 95% confidence intervals must not overlap between adjacent bars
- If ordering fails → investigate incident generation or learning pipeline

**Output file:** `exp1_learning_scenarios_*.json`

---

### Experiment 4 → H2: Deployment Rate

**Hypothesis:** Incident count increases monotonically with deployment rate — every step up in rate produces more incidents, for both GLOBAL and LOCAL

**Parameters:**
- Deployment rates: `[0.05, 0.1, 0.2, 0.3, 0.5]`
- GLOBAL and LOCAL scenarios compared
- 20 teams, Watts-Strogatz, 100 seeds

**What to look for:**
- Incident count rises at every step of the sweep (monotonic ordering)
- A dip at 5 seeds is likely noise — at 100 seeds ordering should hold
- Output now prints explicit PASS/FAIL monotonicity check
- If ordering breaks consistently → investigate deployment_risk_multiplier

**Output file:** `exp4_deployment_velocity_*.json`

---

### Experiment 3 → H3: Diminishing Returns on Learning Investment

**Hypothesis:** The relationship between learning effectiveness and reliability improvement is sublinear — marginal gains decrease beyond moderate effectiveness levels

**Parameters:**
- Sweeps `prevention_effect`: `[0.0, 0.01, 0.02, 0.05, 0.1]`
- NEIGHBOR scenario, Watts-Strogatz, 20 teams, 100 seeds

**What to look for:**
- Plot incident count vs prevention_effect — curve should flatten at higher values
- If linear or accelerating → learning mechanism may be misconfigured
- Check both incident count AND availability to confirm

**Output file:** `exp3_exploitation_effectiveness_*.json`

---

### Experiment 2 → H4: Network Density Accelerates Knowledge Spread

**Hypothesis:** Complete/dense networks show faster knowledge accumulation than sparse networks, measured at simulation midpoint (day 182)

**Parameters:**
- Topologies: `erdos_renyi`, `complete`, `watts_strogatz`, `barabasi_albert`, `star`
- NEIGHBOR scenario, 20 teams, 100 seeds
- Midpoint knowledge measured at step index 182

**What to look for:**
- `midpoint_prevention_knowledge` should be highest for `complete`, lowest for sparse topologies
- If dense networks do not show faster accumulation → investigate propagation mechanism
- Also note final knowledge and incident counts across topologies

**Output file:** `exp2_network_topology_*.json`

---

## Tier 2 — Robustness Experiments

Verify results hold across configurations. Required before trusting Tier 1 findings.

---

### Experiment 9: Robustness — Team Count

**Purpose:** Confirm H1 ordering holds at 6, 20, and 50 teams (not an artifact of the 20-team default)

**Parameters:**
- Team counts: `[6, 20, 50]`
- All 4 scenarios, Watts-Strogatz, 100 seeds each

**What to look for:**
- H1 ordering (NONE > LOCAL > NEIGHBOR > GLOBAL) holds at all three team counts
- If ordering breaks at extreme sizes → document as an edge case, investigate why

**Output file:** `exp9_robustness_team_count_*.json`

---

### Experiment 10: Robustness — Deployment × Learning Cross-Sweep

**Purpose:** Confirm H2 finding is not sensitive to a specific exploitation probability setting

**Parameters:**
- Deployment rates: `[0.05, 0.1, 0.3]`
- Exploitation probabilities: `[0.2, 0.6, 0.9]`
- NEIGHBOR scenario, 20 teams, 100 seeds → 9 conditions

**What to look for:**
- Incident count increases with deployment rate across all exploitation levels
- Effect should be consistent — not only visible at one exploitation setting

**Output file:** `exp10_robustness_deployment_learning_*.json`

---

### Experiment 8: NEIGHBOR ≈ GLOBAL Org Conditions

**Purpose:** Identify under which org sizes and network types NEIGHBOR captures ≥80% of GLOBAL's reliability benefit
*(Note: this was the old H3. In the current proposal it is a robustness observation, not a named hypothesis — but it is the most actionable finding for practitioners)*

**Parameters:**
- Team counts: `[6, 10, 20, 35, 50]`
- Topologies: `watts_strogatz`, `erdos_renyi`, `barabasi_albert`
- Scenarios: NONE, NEIGHBOR, GLOBAL
- 100 seeds → 4,500 total runs (heaviest experiment)

**Metric computed:**
```
benefit_ratio = (NONE_incidents − NEIGHBOR_incidents) / (NONE_incidents − GLOBAL_incidents)
ratio ≥ 0.8 → NEIGHBOR is "good enough"
```

**What to look for:**
- Matrix of ratios: rows = team count, columns = topology
- Stars (*) mark cells where NEIGHBOR ≥ 0.8 — note the pattern
- Smaller orgs with denser topologies expected to have more stars

**Output file:** `exp8_h3_org_conditions_neighbor_global_*.json`

---

## Tier 3 — Ablation Experiments

Verify each model component earns its place. Required under Sargent (2020) validation framework.

---

### Experiment 11: Ablation — No Knowledge Decay

**Purpose:** Confirm knowledge decay (δ=0.001) is a meaningful component, not cosmetic

**Parameters:**
- All 4 scenarios, `disable_knowledge_decay=True` vs default
- 20 teams, Watts-Strogatz, 100 seeds

**What to look for:**
- No-decay runs should show lower incident counts (teams retain knowledge longer)
- If results are identical → decay parameter is dead weight, remove or justify
- If diverge → decay component is meaningful, document the difference

**Output file:** `exp11_ablation_no_decay_*.json`

---

### Experiment 12: Ablation — No Source-Team Asymmetry

**Purpose:** Confirm the source-team learning shortcut (bypassing the pipeline) changes outcomes

**Parameters:**
- All 4 scenarios, `disable_source_asymmetry=True` vs default
- 20 teams, Watts-Strogatz, 100 seeds

**What to look for:**
- Disabling asymmetry should reduce LOCAL learning benefit (source team no longer has advantage)
- GLOBAL gap to NONE should narrow if source team's direct learning is removed
- If results unchanged → asymmetry assumption is unjustified, reconsider

**Output file:** `exp12_ablation_no_asymmetry_*.json`

---

### Experiment 13: Ablation — No Learning Cost

**Purpose:** Confirm cost structure affects strategy choice conclusions

**Parameters:**
- All 4 scenarios, `learning_cost=0` + `engineering_cost_base=0` vs default
- 20 teams, Watts-Strogatz, 100 seeds

**What to look for:**
- Incident counts should be identical (cost doesn't affect reliability outcomes)
- Engineering cost totals should differ — confirms cost model is tracking correctly
- If GLOBAL looks worse with cost included → that is the point, document it

**Output file:** `exp13_ablation_no_cost_*.json`

---

## Tier 4 — Supplementary Experiments

Not core findings. Run if time allows. Put in appendix. Do not present as thesis hypotheses.

---

### Experiment 5: Documentation Quality Effect

**Purpose:** Compare low (0.1) vs high (0.9) documentation quality under LOCAL and GLOBAL

**What to look for:** Poor postmortem quality cripples even the best sharing strategy

**Output file:** `exp5_baseline_comparison_*.json`

---

### Experiment 6: Transformation Stage Sensitivity

**Purpose:** Sweep `transformation_probability` 0.0→1.0 — validates Stage 3 is the bottleneck

**What to look for:** Steep curve = transformation is the key lever. Flat = it doesn't matter

**Output file:** `exp6_transformation_sensitivity_*.json`

---

### Experiment 7: Transformation Mode (MINIMAL vs TIME-BASED)

**Purpose:** Compare single probability check vs multi-timestep effort accumulation

**What to look for:** Does learning dynamics change? Does strategy ordering change?

**Output file:** `exp7_transformation_modes_*.json`

---

## Summary Table

| # | Function | Hypothesis | Tier | Seeds × Conditions | Status |
|---|---|---|---|---|---|
| 1 | `experiment_1_learning_scenarios` | H1 | Core | 100 × 4 = 400 | ☐ |
| 4 | `experiment_4_deployment_velocity` | H2 | Core | 100 × 10 = 1,000 | ☐ |
| 3 | `experiment_3_exploitation_effectiveness` | H3 | Core | 100 × 5 = 500 | ☐ |
| 2 | `experiment_2_network_topology` | H4 | Core | 100 × 5 = 500 | ☐ |
| 9 | `experiment_robustness_team_count` | Robustness | Required | 100 × 12 = 1,200 | ☐ |
| 10 | `experiment_robustness_deployment_learning` | Robustness | Required | 100 × 9 = 900 | ☐ |
| 8 | `experiment_h3_knowledge_threshold_sweep` | NEIGHBOR≈GLOBAL | Required | 100 × 45 = 4,500 | ☐ |
| 11 | `experiment_ablation_no_decay` | Ablation | Required | 100 × 8 = 800 | ☐ |
| 12 | `experiment_ablation_no_asymmetry` | Ablation | Required | 100 × 8 = 800 | ☐ |
| 13 | `experiment_ablation_no_cost` | Ablation | Required | 100 × 8 = 800 | ☐ |
| 5 | `experiment_5_baseline_comparison` | — | Appendix | 100 × 5 = 500 | ☐ |
| 6 | `experiment_6_transformation_sensitivity` | — | Appendix | 100 × 6 = 600 | ☐ |
| 7 | `experiment_7_transformation_modes` | — | Appendix | 100 × 4 = 400 | ☐ |

**Total: ~12,900 simulation runs**
**Heaviest: Experiment 8 (4,500 runs)**

---

## What to Check in Every Experiment

1. **95% CI bands** — do they overlap? Overlapping CIs = finding is not statistically clean
2. **H1 ordering** — in any experiment running all 4 scenarios, NONE > LOCAL > NEIGHBOR > GLOBAL should hold
3. **Availability vs incident count** — should move together. If they diverge, check MTBF/MTTR calculation
4. **Prevention knowledge** — should be highest for GLOBAL, lowest for NONE. If not, check learning pipeline
5. **Transformation rate** — should be non-zero for learning scenarios. If 0% → stage 3 is blocking everything

---

## Known Issues / Decisions Made

| Date | Decision |
|---|---|
| 2026-03-27 | `use_inverted_u` changed to `False` — linear similarity replaces Nooteboom inverted-U. Grounded in Cohen & Levinthal (1990): prior related knowledge aids absorption linearly. All prior pilot runs used the inverted-U and are invalid. |
| Pre-defense | MTBF unit fix applied in `model.py` — MTBF converted from days to hours before availability calculation |

---
