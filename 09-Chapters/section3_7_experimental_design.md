# Section 3.7: Experimental Design

The simulation experiments follow a one-factor-at-a-time logic: each experimental condition isolates one variable of interest by holding all others at fixed baseline values. This design choice prioritizes interpretability over efficiency. Factorial designs would have required fewer total runs to cover the same parameter space, but they conflate main effects with interactions and make it difficult to attribute observed differences to a single cause. Because the primary goal of this study is mechanistic explanation rather than predictive surface-fitting, clean isolation of each variable is more valuable than economy of runs. Nine primary experimental conditions — designated exp01 through exp13, with some numbers reserved for pilot and discarded runs — test hypotheses H1 through H4 along with ablation and robustness analyses. Table 3.4 presents the complete condition inventory.

## 3.7.1 Seeds and the Logic of Replicated Stochastic Runs

Each experimental condition was executed across 100 independent random seeds, with the exception of the H3 validation rerun, which used 500 seeds. A seed controls all stochastic elements of a simulation run: which subsystems fail during a given time step, the severity of each failure, the random component of an agent's learning uptake, and the timing of knowledge decay events. Because these elements are drawn from probability distributions, no two seeds produce identical incident histories — even when all model parameters are identical. Running 100 seeds is equivalent to conducting the same experiment in 100 parallel universes with identical starting conditions. The result is a distribution of outcomes rather than a single summary number, which enables rigorous statistical comparison between conditions using standard two-sample tests.

The choice of 100 seeds per condition reflects a power calculation targeting the ability to detect effect sizes of Cohen's d ≥ 0.5 at p < 0.001 with power β ≥ 0.95. Pilot runs confirmed that 100 seeds produce stable mean estimates — the coefficient of variation for mean incident counts across 100-seed batches was consistently below 3% across all tested conditions.

The H3 validation rerun required 500 seeds because the effect being tested — diminishing returns on prevention effectiveness — is a second-order, nonlinear phenomenon. The first derivative of incident reduction with respect to prevention_effect is small in the region of interest (0.2–0.5), and detecting statistically significant curvature rather than a straight-line relationship requires substantially more power than detecting a simple between-group difference. Five hundred seeds provided the distributional resolution necessary to fit and test a quadratic relationship against a linear null.

## 3.7.2 Duration Rationale: 365 Simulated Days

Each simulation run spans 365 simulated days — one organizational year. This duration was selected for two reasons. First, it is long enough for knowledge dynamics to reach meaningful expression: knowledge must be acquired, assimilate through the pipeline, accumulate in agent memory, and decay to levels that permit a second learning event from the same failure pattern. Full traversal of this cycle requires on the order of 60–90 days at baseline parameters, meaning that a 365-day horizon allows at least three to four full learning cycles for the fastest-sharing conditions. Second, 365 days is computationally tractable: each run completes in under 40 seconds on standard hardware, and 100-seed batches can be executed overnight.

Sensitivity analysis on duration confirmed that the primary findings are not artifacts of this choice. The H1 ordering (NONE > LOCAL > NEIGHBOR > GLOBAL) holds at 180, 365, 730, and 1,095 simulated days, with effect sizes that grow monotonically with duration as cumulative learning advantages compound. Varying duration compresses or amplifies the magnitude of differences between conditions but does not reverse or eliminate them.

## 3.7.3 Experimental Conditions

**Table 3.4: Experimental Conditions**

| Experiment | Hypothesis | What Varies | What's Fixed | Seeds |
|---|---|---|---|---|
| exp01–03 | H1 | Sharing scenario (NONE / LOCAL / NEIGHBOR / GLOBAL) | Watts–Strogatz topology, base_rate = 0.05 | 100 |
| exp04 | H2 | Deployment rate (0.05, 0.10, 0.20, 0.30, 0.50) | GLOBAL and LOCAL scenarios | 100 |
| exp05 | H3 (initial) | prevention_effect (0.0–0.3) | GLOBAL scenario | 100 |
| exp07 | H4 | Network topology (5 types) | NEIGHBOR scenario | 100 |
| exp10 | H2 × H3 | deployment_rate × exploitation_effect (3 × 3 grid) | GLOBAL scenario | 100 |
| exp11 | Ablation | decay_rate = 0 (no decay) | All 4 scenarios | 100 |
| exp12 | Ablation | source_asymmetry = False | All 4 scenarios | 100 |
| exp13 | Ablation | learning_cost tracking | GLOBAL scenario | 100 |
| H3 rerun | H3 (validation) | prevention_effect (0.0–0.5, extended range) | GLOBAL scenario | 500 |

## 3.7.4 Hypothesis-to-Experiment Mapping

**H1 — Sharing scope and incident rates (exp01–03).** Experiments 01 through 03 implement the four sharing scenarios — NONE, LOCAL, NEIGHBOR, and GLOBAL — described in Section 3.5 against a fixed Watts–Strogatz small-world topology and a baseline incident rate of 0.05 events per team per day. All other parameters are held at their calibrated default values. The predicted ordering is NONE > LOCAL > NEIGHBOR > GLOBAL: the more broadly a team can share and receive incident knowledge, the fewer recurrent failures it will experience. This is the central hypothesis of the study, and exp01–03 constitute its direct test. The simulation answer to the question "Does sharing scope causally affect incident rates?" emerges from comparing the mean incident distributions across these four conditions.

**H2 — Deployment rate and incident rates (exp04).** Experiment 04 varies the deployment rate — the number of code changes introduced to the system per simulated day — across five levels (0.05, 0.10, 0.20, 0.30, 0.50) within the GLOBAL and LOCAL sharing scenarios. Faster deployment introduces more novel failure opportunities and raises the baseline hazard. The predicted relationship is monotonic: each increment in deployment rate should produce a corresponding increment in mean incidents. This experiment tests whether the model faithfully represents the empirical finding that velocity is a risk factor for reliability — a relationship documented in DevOps research and used as one calibration anchor for the model (see Section 3.8).

**H3 — Diminishing returns on prevention effectiveness (exp05 and H3 rerun).** Experiments 05 and the H3 rerun vary the prevention_effect parameter, which governs how much each unit of accumulated incident knowledge reduces the probability of a recurrent failure. The initial run (exp05) explored the range 0.0 to 0.3; the validation rerun extended coverage to 0.5 with five times as many seeds. The predicted relationship is sublinear: early increments in prevention_effect produce large reductions in incident rates, but each successive increment yields diminishing marginal returns as the most preventable failure modes are eliminated and the remaining incidents are driven by novel or low-probability events that prior knowledge cannot address. Confirming this nonlinearity required the extended parameter range and increased seed count of the H3 rerun.

**H4 — Network topology and incident rates (exp07).** Experiment 07 holds the sharing scenario constant at NEIGHBOR — the condition in which knowledge propagates one step through the network — while varying the network topology across five types: Watts–Strogatz small-world, Barabási–Albert scale-free, Erdős–Rényi random, ring lattice, and complete graph. The predicted direction is that denser and more evenly connected topologies produce fewer incidents, because knowledge reaches more teams per propagation step and the probability that a failure pattern known to one team goes unrecognized by others declines. This hypothesis addresses whether the topology is an independent variable for reliability or merely an enabling condition for the sharing scenario.

**Interaction experiment (exp10).** Experiment 10 crosses three levels of deployment_rate with three levels of exploitation_effect in a 3 × 3 factorial grid, holding the sharing scenario fixed at GLOBAL. This experiment was not associated with a primary hypothesis but was included to characterize the interaction surface between knowledge exploitation capacity and change velocity — specifically, to determine whether high deployment rates can overwhelm the protective effect of knowledge exploitation. The results inform the boundary conditions of H2 and H3.

**Ablation experiments (exp11–13).** Three ablation experiments isolate the contribution of specific model assumptions. Experiment 11 removes knowledge decay (decay_rate = 0) across all four sharing scenarios, testing whether the learning curves and scenario ordering are artifacts of the decay parameter or are robust to its removal. Experiment 12 disables source asymmetry — the design assumption that the originating team does not re-enter the learning pipeline for knowledge it already generated — across all four scenarios. This tests whether LOCAL's near-zero transformation rate is a real modeling finding or an artifact of the asymmetry assumption. Experiment 13 activates learning_cost tracking in the GLOBAL scenario, attributing a computational overhead to each cross-boundary knowledge transmission, to assess whether coordination costs materially reduce the net benefit of global sharing.

## 3.7.5 Statistical Approach

The primary comparison metric is mean incidents over 365 simulated days, averaged across all 20 teams and all runs within a seed batch. Two-sample t-tests are used for all pairwise condition comparisons. The significance threshold is p < 0.001, chosen to be conservative given the large number of pairwise comparisons performed across all experiments. Effect sizes are reported as Cohen's d, computed as the difference in condition means divided by the pooled standard deviation of seed-level outcomes. Reporting effect sizes alongside p-values follows the recommendation that statistical significance alone is insufficient for interpreting simulation experiments, where large seed counts make it trivially easy to achieve p < 0.05 for effects that are substantively negligible (Sargent, 2020).

## 3.7.6 A Note on exp12: The Source Asymmetry Ablation

The source asymmetry assumption in the baseline model holds that the team which generated an incident report does not receive that same report back through the sharing pipeline — because the knowledge is already encoded in the source team's memory. Without this assumption, the source team would receive its own knowledge as an incoming transmission, inflating its apparent learning rate and producing an artifact in which LOCAL sharing appears more effective than it would otherwise be. Experiment 12 tests whether this design choice meaningfully affects the results. With source_asymmetry = False, the LOCAL condition degrades by approximately 7.7% in mean incident reduction — a non-trivial effect, confirming that the assumption matters. However, the H1 ordering (NONE > LOCAL > NEIGHBOR > GLOBAL) is preserved under both conditions, indicating that the asymmetry assumption shapes the magnitude of LOCAL's performance but not the qualitative finding that broader sharing produces better outcomes.

---

## Citation Checklist

- [ ] Sargent (2020) — Section 3.7.5, final sentence: "...Sargent (2020)" — for the principle that effect sizes should accompany p-values in simulation experiments, and for the one-factor-at-a-time design justification in the opening paragraph (optional but supportable).

## Committee Watch

1. **"Why one-factor-at-a-time instead of a full factorial?"** The opening paragraph addresses this directly: the goal is mechanistic explanation, not response surface estimation. A full factorial would confound interactions with main effects and make it harder to attribute findings to specific mechanisms. Be prepared to add: the exp10 interaction experiment shows the study is not blind to interaction effects — it simply addresses them deliberately rather than structurally.

2. **"Why 100 seeds and not 1,000?"** The power calculation answer (Section 3.7.1) is the correct response. Be prepared to show the pilot data confirming that 100-seed coefficient of variation was below 3%. The committee may accept this if pressed; if not, note that 1,000 seeds per condition would have increased total compute time by 10× for marginal reduction in standard error.

3. **"Why 365 days?"** Two reasons: (a) the sensitivity analysis shows ordering stability across 180–1,095 days; (b) 365 is a natural unit that corresponds to the organizational planning horizon most practitioners think in. The first answer is the scientific one; the second is a communication choice.

4. **"What justifies the p < 0.001 threshold?"** Multiple comparisons. With 9 primary conditions and several pairwise tests per condition, a standard p < 0.05 threshold would inflate the family-wise error rate substantially. The conservative threshold is a pre-registered design choice, not a post-hoc adjustment. Be prepared to note that all reported effects in Chapter 4 exceed this threshold comfortably.

5. **"Isn't the exp12 finding a threat to your LOCAL result?"** The honest answer: yes, it shows that the asymmetry assumption partially drives LOCAL's performance level, and the 7.7% degradation is real. The committee may press on whether this means the LOCAL finding is fragile. The response is that H1 does not stand or fall on the magnitude of LOCAL's advantage — only on the ordering — and the ordering is robust across both asymmetry conditions.
