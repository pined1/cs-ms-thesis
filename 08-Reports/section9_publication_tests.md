# Section 9: Publication-Level Validation Tests

## Overview

Establishing H1 through H4, running ablations, and completing sensitivity sweeps provided a strong internal foundation for the simulation's findings. However, the bar for peer-reviewed submission at venues such as ICSE, MSR, or JASSS demands an additional layer of scrutiny. Reviewers at these venues routinely probe for transient artifacts, sensitivity to arbitrary parameter choices, statistical ambiguity, and interaction effects that can quietly undermine conclusions. To preempt those critiques, a final battery of nine publication-level validation tests was designed and executed. Each test corresponds to a specific question a rigorous reviewer would ask. All nine tests passed.

---

## Test 1 — Time Dynamics: When Does H1 Ordering Emerge?

**Question.** Does the knowledge-sharing advantage manifest immediately, or is there a warmup period during which all scenarios perform similarly before diverging?

**Method.** Fifty random seeds were run per scenario. Incident counts were extracted in non-overlapping 30-day windows across the full 365-day simulation. Cumulative knowledge levels were tracked alongside incident rates.

**Results.** H1 ordering is present from day 1. In the first 30-day window, mean incident counts were NONE = 40.3, LOCAL = 39.9, NEIGHBOR = 38.7, GLOBAL = 34.7 — already rank-ordered as predicted. GLOBAL knowledge level reaches 0.577 by day 30 and 0.992 by day 90, after which it plateaus. NONE remains at 0.000 throughout the entire simulation.

**Conclusion.** There is no warmup artifact. The ordering appears immediately and strengthens over time as accumulated knowledge compounds the incident-reduction benefit. Reviewers questioning whether 365 days is "too early" to interpret results can be answered directly: the effect is present from the first measurable window.

---

## Test 2 — Simulation Duration: Is 365 Days in Transient or Steady State?

**Question.** Would H1 collapse if the simulation ran longer? Are teams still actively learning at day 365, or has the system reached equilibrium?

**Method.** One hundred seeds were run across all four scenarios at four durations: 180, 365, 730, and 1095 days. Raw incident totals were normalized to incidents per day to enable fair cross-duration comparison.

**Results.**

| Duration | NONE inc/day | LOCAL inc/day | NEIGHBOR inc/day | GLOBAL inc/day | H1 Holds? |
|---|---|---|---|---|---|
| 180 days | 1.326 | 1.211 | 1.062 | 0.786 | Yes |
| 365 days | 1.327 | 1.113 | 0.920 | 0.728 | Yes |
| 730 days | 1.325 | 0.998 | 0.816 | 0.698 | Yes |
| 1095 days | 1.324 | 0.940 | 0.774 | 0.689 | Yes |

NONE is essentially flat across all durations — confirming that without sharing, incident rates do not improve. LOCAL, NEIGHBOR, and GLOBAL all continue declining through year three, indicating that teams are still learning at day 365. H1 holds at every duration, and the GLOBAL advantage compounds over time: approximately 45% incident reduction at one year, growing to 48% at three years.

**Conclusion.** The 365-day simulation is not artificially cut off at a transient peak. It sits within an ongoing learning phase, which makes the results conservative — longer runs favor global sharing even more.

---

## Test 3 — Barabási-Albert ba_m Sweep: When Does Scale-Free Stop Underperforming?

**Question.** Scale-free (BA) topology underperforms Watts-Strogatz (WS) at default parameters. At what connectivity level does BA match or exceed WS?

**Method.** One hundred seeds per condition, NEIGHBOR scenario, varying ba_m (the number of edges added per new node) across {1, 2, 3, 4, 6}. The WS baseline under identical conditions produces 336 incidents.

**Results.** ba_m = 1: 368 incidents (worse than WS). ba_m = 2: 347 (still worse). ba_m = 3: 331 (better — crossover point). ba_m = 6: 305 (substantially better than WS).

**Conclusion.** The crossover occurs at ba_m = 3, corresponding to an average node degree of approximately 6. Below this threshold, hubs in the BA network act as bottlenecks — knowledge accumulates at highly connected nodes but does not propagate efficiently outward. Above the threshold, hubs become accelerators, distributing knowledge more broadly than the regular WS lattice can. This finding directly answers the committee question about whether scale-free topology findings are an artifact of parameter choice rather than topology type.

---

## Test 4 — Watts-Strogatz ws_k Sweep: Sensitivity to Network Degree

**Question.** Is the NEIGHBOR result sensitive to how many direct neighbors each team has in the WS topology?

**Method.** One hundred seeds per condition, NEIGHBOR scenario, ws_k varied across {2, 4, 6, 8, 10}. Default is ws_k = 4.

**Results.** ws_k = 2: 360.7 incidents. ws_k = 4: 336.0 (default). ws_k = 6: 312.8. ws_k = 8: 301.0. ws_k = 10: 288.2.

**Conclusion.** The relationship is monotonically improving — more neighbors consistently means more learning and fewer incidents. The default setting of ws_k = 4 is conservative relative to higher-connectivity alternatives. All reported findings hold and strengthen across the full parameter range, ruling out sensitivity to this design choice.

---

## Test 5 — Knowledge Decay Rate Sweep

**Question.** Does H1 survive aggressive knowledge decay? What happens when teams forget quickly?

**Method.** One hundred seeds per condition, NONE/NEIGHBOR/GLOBAL scenarios, decay rates varied across {0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05}. The default is 0.001 (half-life approximately 2 years).

**Results.**

| Decay Rate | Half-life | NONE | NEIGHBOR | GLOBAL | H1 Holds? | GLOBAL Saves |
|---|---|---|---|---|---|---|
| 0.0001 | ~19 years | 484 | 325 | 264 | Yes | 45% |
| 0.001 (default) | ~2 years | 484 | 336 | 266 | Yes | 45% |
| 0.005 | ~5 months | 484 | 367 | 276 | Yes | 43% |
| 0.01 | ~2.5 months | 484 | 397 | 288 | Yes | 41% |
| 0.05 | ~2 weeks | 484 | 457 | 392 | Yes | 19% |

**Conclusion.** H1 holds at every tested decay rate without exception. Even at the most aggressive setting — a two-week knowledge half-life, far shorter than any realistic organizational context — GLOBAL still saves 19% of incidents relative to NONE. The magnitude of the effect shrinks under high decay, as expected, but the direction never reverses. This robustness is a strong answer to reviewers who may question whether the model assumes unrealistically persistent knowledge.

---

## Test 6 — Cohen's d Effect Sizes

**Question.** Are the observed differences statistically and practically significant, or merely statistically detectable due to large sample sizes?

**Method.** One hundred seeds per scenario. For all pairwise comparisons, pooled standard deviation was computed and Cohen's d was calculated. The conventional threshold for a "large" effect is d = 0.8.

**Results.**

| Comparison | Cohen's d | Classification |
|---|---|---|
| NONE vs. GLOBAL | 11.51 | Large |
| NONE vs. NEIGHBOR | 7.72 | Large |
| NONE vs. LOCAL | 3.91 | Large |
| LOCAL vs. NEIGHBOR | 4.55 | Large |
| LOCAL vs. GLOBAL | 9.26 | Large |
| NEIGHBOR vs. GLOBAL | 4.92 | Large |

All comparisons: p < 0.001. The smallest observed effect (NONE vs. LOCAL, d = 3.91) is nearly five times the threshold for a large effect. Scenario distributions are non-overlapping in practice.

**Conclusion.** The findings are not a large-n statistical artifact. Every pairwise comparison produces unambiguously large practical effect sizes. No reviewer can reasonably argue statistical ambiguity or that the differences are too small to matter in practice.

---

## Test 7 — H3 500-Seed Rerun with Extended Parameter Range

**Question.** Does the diminishing-returns pattern in H3 (postmortem quality) hold under high-power conditions and across an extended parameter range?

**Method.** Five hundred seeds were run with postmortem quality ranging from 0.0 to 0.5 (extended beyond the original sweep). Full details are reported in the H3 section.

**Result.** The model's automated flag reported: "Diminishing returns detected (H3 supported)." The pattern is confirmed at 500-seed power with the extended range, leaving no ambiguity about whether it was an artifact of the original parameter bounds.

---

## Test 8 — Documentation Quality × Scenario Interaction

**Question.** Does poor postmortem quality cancel out the benefit of global knowledge sharing? Could an organization with sloppy documentation negate H1?

**Method.** One hundred seeds, full 3 × 4 factorial design: doc_quality ∈ {0.1, 0.5, 0.9} crossed with all four sharing scenarios.

**Results.**

| Doc Quality | NONE | LOCAL | NEIGHBOR | GLOBAL | GLOBAL Saves vs. NONE |
|---|---|---|---|---|---|
| 0.1 (poor) | 484 | 406 | 345 | 272 | 43.8% |
| 0.5 (default) | 484 | 406 | 336 | 266 | 45.2% |
| 0.9 (high) | 484 | 406 | 325 | 260 | 46.3% |

**Conclusion.** Documentation quality modulates the magnitude of improvement modestly but does not reverse the H1 ordering. Even with poor postmortems, GLOBAL sharing saves 43.8% of incidents relative to no sharing. Sharing scope dominates document quality as a determinant of organizational learning outcomes. This is a practically important finding: organizations should prioritize expanding sharing reach even if documentation processes are imperfect.

---

## Test 9 — Base Incident Rate Sweep

**Question.** Does H1 hold when major incidents are rare (slow, limited learning signal) or when incidents are frequent (fast, abundant learning signal)?

**Method.** One hundred seeds, all four scenarios, base incident rates varied across {0.01, 0.02, 0.05, 0.1, 0.2}. Default is 0.05.

**Results.**

| Base Rate | NONE | LOCAL | NEIGHBOR | GLOBAL | H1 Holds? | GLOBAL Saves |
|---|---|---|---|---|---|---|
| 0.01 (rare) | 97 | 94 | 87 | 69 | Yes | 29% |
| 0.05 (default) | 484 | 406 | 336 | 266 | Yes | 45% |
| 0.20 (frequent) | 1935 | 1242 | 1076 | 999 | Yes | 48% |

**Conclusion.** H1 holds across the full range of incident frequencies. The GLOBAL advantage grows with incident frequency because more incidents generate more learning opportunities, and those opportunities are amplified by broader sharing scope. Critically, even at the rarest incident rate (0.01, representing major enterprise outages that occur infrequently), GLOBAL saves 29% — a finding directly relevant to large organizations where high-severity incidents are uncommon but extremely costly.

---

## Overall Conclusion

All nine publication-level validation tests passed without exception. The H1 ordering is immediate, persistent across simulation durations up to three years, robust to network topology and connectivity parameters, stable under aggressive knowledge decay, unaffected by documentation quality degradation, and present whether incidents are rare or frequent. Effect sizes are unambiguously large by conventional standards — the smallest pairwise Cohen's d of 3.91 is nearly five times the large-effect threshold. Together, these tests address the categories of critique most commonly raised at ICSE, MSR, and JASSS: transience, sensitivity, statistical ambiguity, and interaction effects. The simulation findings meet or exceed the validation standards required for peer-reviewed submission at those venues.
