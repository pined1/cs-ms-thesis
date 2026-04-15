# Remaining Tests — Priority Order
**For publication-level rigor | David Pineda BYU CS MS**
**Created: 2026-03-30 | Updated: 2026-03-31**
**Status: All CRITICAL + IMPORTANT items complete ✅**

---

## How to Use This File

Work top to bottom. Items marked **CRITICAL** will draw reviewer rejection.
Items marked **IMPORTANT** separate a strong paper from a weak one.
Items marked **NICE TO HAVE** are for journal submission, not required for thesis defense.

---

## CRITICAL — Reviewer Will Reject Without These

---

### 1. Time Dynamics Analysis ✅ COMPLETE (2026-03-31)
**What:** Extract time-series data from existing JSON results and plot mean incident
rate per 30-day window for all 4 scenarios (NONE, LOCAL, NEIGHBOR, GLOBAL).

**Why:** Every result we have is an end-state (day 365). Reviewers will ask:
*when does H1 ordering emerge? Day 30? Day 100? Does LOCAL look identical to NONE
for the first 90 days?* The learning onset question is fundamental to the thesis claim.

**How:** Load `exp1_learning_scenarios_20260330_*.json` → extract `time_series` →
compute 30-day rolling windows → plot divergence curves.

**Deliverable:** Figure showing when each scenario diverges from NONE baseline.

---

### 2. Simulation Duration Sensitivity ✅ COMPLETE (2026-03-31)
**What:** Run H1 experiment (all 4 scenarios) at 4 time horizons: 180, 365, 730, 1095 days.

**Why:** Is 365 days in the transient or steady-state regime? If you ran 730 days,
would GLOBAL knowledge saturate and the ordering collapse? ABM reviewers (JASSS) always ask this.

**Command to add to sensitivity script:**
```
steps sweep: [180, 365, 730, 1095]
scenarios: all 4
seeds: 100
```

**What to look for:**
- Does H1 ordering hold at all durations?
- At what step count does prevention knowledge plateau for each scenario?
- Does LOCAL ever catch up to NEIGHBOR given enough time?

---

### 3. Barabási-Albert `ba_m` Parameter Sweep ✅ COMPLETE (2026-03-31)
**What:** Sweep `ba_m` (edges per new node) = [1, 2, 3, 4, 6] with NEIGHBOR scenario.

**Why:** `ba_m=2` is the only BA configuration ever tested. This directly answers the
committee's question: *"how large does the network need to be for scale-free?"*
The real answer is ba_m controls density, not just node count. At ba_m=4, does BA
finally outperform Watts-Strogatz?

**Command:**
```
network_topology: barabasi_albert
ba_m sweep: [1, 2, 3, 4, 6]
num_teams: 20
seeds: 100
```

**What to look for:**
- At what ba_m does BA performance match or exceed Watts-Strogatz?
- Does higher ba_m rescue BA from its H4 underperformance?

---

### 4. Watts-Strogatz `ws_k` Parameter Sweep ✅ COMPLETE (2026-03-31)
**What:** Sweep `ws_k` (number of neighbors) = [2, 4, 6, 8, 10] with NEIGHBOR scenario.

**Why:** ws_k=4 is the only Watts-Strogatz configuration tested. This controls how
many direct neighbors each team has — the primary driver of NEIGHBOR learning reach.
A reviewer will ask: is your result sensitive to this structural assumption?

**Command:**
```
network_topology: watts_strogatz
ws_k sweep: [2, 4, 6, 8, 10]
num_teams: 20
seeds: 100
```

---

### 5. Knowledge Decay Rate Sweep ✅ COMPLETE (2026-03-31)
**What:** Sweep `knowledge_decay` = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05]

**Why:** The ablation only tested on vs off. The 0.001 default comes from Darr et al.
(half-life ~2 years) but was never validated against a range. Reviewers will ask:
how sensitive are findings to this specific calibration? If decay=0.05 (1-month half-life),
does H1 still hold?

**Half-life reference:**
- 0.0001 → ~19 years
- 0.001  → ~2 years (current default, Darr et al.)
- 0.005  → ~5 months
- 0.01   → ~2.5 months
- 0.05   → ~2 weeks

**What to look for:**
- At what decay rate does knowledge accumulation break down?
- Does H1 ordering survive aggressive decay (0.01, 0.05)?

---

## IMPORTANT — Strong Paper vs Weak Paper

---

### 6. Effect Sizes (Cohen's d) ✅ COMPLETE (2026-03-31)
**What:** Compute Cohen's d for all key pairwise comparisons:
- GLOBAL vs NONE (main finding)
- GLOBAL vs NEIGHBOR (cost of imperfect sharing)
- NEIGHBOR vs LOCAL (value of cross-team exposure)
- With decay vs without decay
- With asymmetry vs without asymmetry

**Why:** 95% CI bands show direction but not magnitude. Reviewers at SE and management
venues expect standardized effect sizes. Cohen's d < 0.2 = small, 0.5 = medium, 0.8 = large.

**How:** Compute from existing result JSON files. Pure analysis, no new simulations.

**Formula:** d = (mean1 - mean2) / pooled_std

---

### 7. 500-Seed Rerun of H3 ✅ COMPLETE (2026-03-31)
**What:** Re-run exp3 (exploitation effectiveness / prevention_effect sweep) with 500 seeds.

**Why:** H3 showed only 6-incident variation across the full 0.0→0.1 range — a very
small effect. At 100 seeds, this could be noise masking a weak sublinear signal.
500 seeds will either confirm the linear finding definitively or reveal a subtle
diminishing-returns curve we missed.

**Command:**
```
python run_experiments.py --experiment 3
(change NUM_SEEDS to 500 temporarily)
```

---

### 8. Documentation Quality × Sharing Scope Interaction ✅ COMPLETE (2026-03-31)
**What:** Full 3×4 sweep: doc_quality=[0.1, 0.5, 0.9] × all 4 scenarios.

**Why:** exp5 only compared low vs high doc quality for LOCAL and GLOBAL.
The interaction question is: *does poor postmortem quality cancel out the benefit
of global sharing?* This is the most actionable practitioner finding possible —
"even GLOBAL sharing fails if your postmortems are bad."

**What to look for:**
- At doc_quality=0.1, does GLOBAL still outperform LOCAL significantly?
- Is there a doc quality threshold below which sharing scope doesn't matter?

---

### 9. base_incident_rate Sweep ✅ COMPLETE (2026-03-31)
**What:** Sweep `base_incident_rate` = [0.01, 0.02, 0.05, 0.1, 0.2]

**Why:** The default 0.05 (5% chance of incident per subsystem per day) was never
varied outside of deployment rate experiments. Low incident rate means slow learning
— does H1 hold when teams rarely see incidents? High rate means fast learning —
does GLOBAL's advantage shrink when everyone learns quickly anyway?

---

## NICE TO HAVE — Journal Submission (not required for thesis)

---

### 10. ODD Protocol Document
**What:** Write the Overview, Design concepts, Details (ODD) protocol for the model.

**Why:** Mandatory for any ABM paper submitted to JASSS, AAMAS, or similar.
Not a simulation — a structured description of the model in a standardized format.
~4–6 pages. See Grimm et al. (2020) for the ODD+D template.

---

### 11. Subsystem Assignment Sensitivity
**What:** Run H1 with randomized subsystem assignment (shuffle instead of round-robin).

**Why:** Teams are currently assigned subsystems deterministically (DATABASE, PAYMENT,
AUTH, FRONTEND, API, CACHE, DATABASE...). This is a structural assumption that
could affect which teams learn from which incidents (via relevance scores).
Randomizing and confirming findings hold removes a potential confound.

---

### 12. Two-Way Interaction: Team Count × Topology
**What:** Run H1 across [6, 20, 50] teams × [watts_strogatz, erdos_renyi, barabasi_albert].

**Why:** exp8 shows benefit ratios but not H1 incident counts by team×topology combination.
A reviewer might ask whether the GLOBAL advantage is consistent across all
team count / topology combinations, not just at the default 20-team Watts-Strogatz.

---

### 13. Erdos-Renyi `er_p` Parameter Sweep
**What:** Sweep `er_p` (edge probability) = [0.1, 0.2, 0.3, 0.5, 0.7, 1.0]

**Why:** er_p=0.3 is the only configuration tested. At er_p=1.0, ER becomes a complete
graph. At er_p=0.1, it may be disconnected at 20 nodes. Understanding where the
performance inflection point is for random networks strengthens the H4 topology finding.

---

## Summary Table

| # | Test | Status | Priority |
|---|---|---|---|
| 1 | Time dynamics (learning onset) | ✅ DONE | CRITICAL |
| 2 | Simulation duration (180/365/730/1095) | ✅ DONE | CRITICAL |
| 3 | ba_m sweep (Barabási-Albert density) | ✅ DONE | CRITICAL |
| 4 | ws_k sweep (Watts-Strogatz neighbors) | ✅ DONE | CRITICAL |
| 5 | Knowledge decay rate sweep | ✅ DONE | CRITICAL |
| 6 | Effect sizes (Cohen's d) | ✅ DONE | IMPORTANT |
| 7 | 500-seed H3 rerun | ✅ DONE | IMPORTANT |
| 8 | Doc quality × scenario interaction | ✅ DONE | IMPORTANT |
| 9 | base_incident_rate sweep | ✅ DONE | IMPORTANT |
| 10 | ODD Protocol document | ⬜ TODO | NICE TO HAVE |
| 11 | Subsystem assignment randomization | ⬜ TODO | NICE TO HAVE |
| 12 | Team count × topology 2-way | ⬜ TODO | NICE TO HAVE |
| 13 | er_p sweep | ⬜ TODO | NICE TO HAVE |

**All CRITICAL + IMPORTANT items complete as of 2026-03-31.**
Remaining items (10–13) are for journal submission, not required for thesis.

---

## Recommended Run Order

Run items 2–5 in parallel (all launch independently).
Items 1 and 6 require no new simulations — do those as analysis work.
Items 7–9 can run while writing.
Items 10–13 are post-defense / journal revision work.
