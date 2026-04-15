# Section 10: Limitations, Future Work & Conclusion

---

## Part A: Model Limitations

Every simulation model is a simplification of reality. The following limitations are acknowledged honestly — none reverse the directional findings, but all represent opportunities to strengthen the model for journal submission.

### 1. All Knowledge Has Potential Value to All Teams

**Model assumes:** Incident knowledge has value to all teams proportional to cosine similarity between the incident's subsystem embedding and the receiving team's knowledge profile.

**Reality:** Some knowledge is domain-specific enough that cross-team exposure produces zero benefit regardless of measured similarity. A frontend team genuinely does not need database replication internals, even if embedding geometry suggests modest overlap.

**Effect on findings:** Slight overstatement of cross-team benefit. Cosine similarity already partially handles this — teams with low similarity have correspondingly low transformation probability — but the model does not enforce a hard relevance floor.

**Future work:** Introduce a hard relevance threshold below which sharing produces zero benefit, and re-run H1 comparisons to quantify the overstatement magnitude.

---

### 2. Scale-Free Property Not Statistically Verifiable at 20 Nodes

**Model assumes:** The Barabási–Albert (BA) network represents hub-spoke or scale-free organizational behavior.

**Reality:** Verifying a power-law degree distribution requires 50–100+ nodes. At 20 nodes, the distributional shape is suggestive but not statistically confirmable.

**Effect on findings:** Hub-spoke behavioral effects are observable and meaningful at 20 nodes. The mathematical scale-free property, strictly defined, is unverifiable at this scale. The ba_m parameter sweep addresses this by varying connectivity rather than relying on the label alone.

**Future work:** Re-run H4 topology comparisons at 50+ nodes to confirm scale-free property and assess whether the relative network ordering persists.

---

### 3. Fixed Stage Probabilities Regardless of Incident Severity

**Model assumes:** The same acquisition probability (p_acquire = 0.9) applies to P1 outages and P3 minor degradations alike.

**Reality:** High-severity incidents command disproportionate organizational attention. Teams are far more likely to read and discuss a postmortem for a $1M revenue-loss outage than a brief, low-impact degradation.

**Effect on findings:** The model may understate learning from high-severity incidents. Because all incidents carry equal acquisition weight, the simulation likely underestimates the reliability benefit from the most consequential failures.

**Future work:** Implement severity-weighted acquisition (p_acquire = base × severity_weight) and evaluate whether high-severity incident learning produces nonlinear reliability gains.

---

### 4. Same Probability Retried Every Day — No Urgency Decay

**Model assumes:** A team that fails to acquire incident knowledge on day 1 retries with identical probability on day 50.

**Reality:** Incident postmortems lose organizational urgency over time. A two-week-old postmortem is less likely to be read than a fresh one published yesterday.

**Effect on findings:** May slightly overstate eventual acquisition rates across the 365-day window. This mechanism also explains why the assimilation and exploitation probability sweeps showed low sensitivity — the retry loop allows time to compensate for processing failures, masking what would be a tighter constraint under a time-bounded regime.

**Future work:** Implement a time-windowed acquisition probability that decays with elapsed time since incident publication.

---

### 5. Homogeneous Team Sizes and Expertise

**Model assumes:** All 20 teams are identical in size, seniority, and learning capacity.

**Reality:** A 15-person platform team has substantially more absorptive capacity than a 3-person feature team. Senior teams with deep institutional knowledge process new incidents differently than junior teams encountering novel failure modes.

**Effect on findings:** The model misses expertise asymmetry and the concentration effects that arise when high-capacity teams disproportionately drive organizational reliability.

**Future work:** Introduce team-level capacity parameters (team_size, seniority_factor) and evaluate whether expertise concentration changes the relative ordering of sharing strategies.

---

### 6. Static Network Topology

**Model assumes:** Team connections are fixed at initialization and remain unchanged for all 365 simulation days.

**Reality:** Organizations reorganize. Teams form new relationships through cross-functional projects. Engineers move between teams, carrying knowledge and creating new informal channels.

**Effect on findings:** The model cannot capture the reliability effects of reorganization — whether structural changes accelerate or disrupt knowledge diffusion. Static topology is a standard simulation assumption, but it limits applicability to organizations with stable team structures.

**Future work:** Implement dynamic network evolution, including edge formation, dissolution, and team membership changes over the simulation horizon.

---

### 7. Uniform Knowledge Decay

**Model assumes:** All teams forget at the same rate, and all knowledge types decay equally over time.

**Reality:** Codified knowledge — runbooks, automated checks, documented incident patterns — persists and may be essentially permanent. Tacit knowledge decays with team turnover and cognitive displacement. Different subsystems may have different retention curves depending on incident frequency and documentation culture.

**Effect on findings:** The model conflates codified and tacit knowledge into a single decay parameter, potentially misrepresenting organizations where codification practices differ substantially across teams.

**Future work:** Implement a two-component decay model separating codified retention (near-zero decay) from tacit retention (standard decay), and validate against organizations with varying documentation maturity.

---

### 8. Per-Stage Developer Hours Not Yet Tracked

**Model assumes:** Aggregate learning cost of 2 hours per learning event, applied uniformly.

**Reality:** Developer hours should be tracked per pipeline stage to identify where investment is consumed and where the pipeline fails. This would enable cost attribution: how much time was spent in acquisition that never reached exploitation?

**Effect on findings:** Cannot currently answer stage-level ROI questions. This is not a model gap in the current results — the aggregate cost estimate is valid for the thesis findings — but it is a priority enhancement for journal submission.

**Status:** Identified as a paper enhancement per advisor request. Implementation is planned and straightforward.

---

### Summary: Limitations Do Not Reverse Directional Findings

None of the above limitations alter the directional conclusions. H1 ordering — GLOBAL > NEIGHBOR > NONE — held across every robustness test, 9 experimental conditions, and 100–500 seeds per condition. The limitations affect the estimated magnitude of effects, not their direction or relative ordering. They are documented here as honest acknowledgment and as a roadmap for the journal submission cycle.

---

## Part B: Future Work

### Near-Term (Paper Submission Preparation)

| Priority | Item | Rationale |
|---|---|---|
| 1 | Per-stage developer hour tracking | Advisor request; required for journal-level cost analysis |
| 2 | Severity-weighted acquisition probability | Addresses Limitation 3; likely improves model fidelity |
| 3 | BA topology test at 50+ nodes | Confirms scale-free property claim in H4 |
| 4 | ODD protocol document | Required for JASSS submission standard |

### Medium-Term

- Dynamic network topology to capture organizational restructuring and relationship formation
- Heterogeneous team sizes and expertise levels to model absorptive capacity asymmetry
- Subsystem assignment randomization sensitivity test to verify subsystem mapping does not drive results
- Erdos-Renyi er_p parameter sweep to more fully characterize the ER topology space

### Long-Term

- Empirical calibration against real incident data from industry partners, using postmortem archives as ground truth for acquisition and assimilation rates
- Extension of the model to other organizational learning contexts — medical adverse events, aviation safety incidents — where the same absorptive capacity pipeline applies
- Integration with existing DevOps tooling (incident management platforms, postmortem databases) to enable real-time simulation and organizational decision support

---

## Part C: Cross-Cutting Finding

The most important pattern to emerge across all nine experiments is consistent and theoretically meaningful:

> **The model has one sensitive axis: information exposure.**

Getting knowledge in front of teams — through sharing scope, acquisition probability, or prior knowledge — is the primary driver of reliability. Once knowledge reaches a team, processing it is naturally robust. The pipeline bottleneck is not effort or processing intensity; it is exposure.

| Variable | Reliability Effect | Classification |
|---|---|---|
| Sharing scope (H1) | 45% incident reduction | DOMINANT |
| Deployment risk (H2) | Significant; absorbed by GLOBAL | Significant |
| Prior knowledge — warm start | 22% rate difference | Moderate |
| Network topology (H4) | 28% range across topologies | Significant |
| Acquisition probability | 11% range across sweep | Moderate |
| Exploitation effectiveness (H3) | 30% at extreme values | Modest |
| Assimilation probability | 1.7% range | Negligible |
| Exploitation probability | 0.7% range | Negligible |
| Signal decay (NEIGHBOR condition) | 0% — parameter is dormant | Negligible |

The negligible effect of assimilation and exploitation probability sweeps is not a null result — it is a finding. It means that once teams are exposed to incident knowledge, they will eventually process it. Time compensates for processing failures. The retry mechanism is robust. What time cannot compensate for is knowledge that was never shared in the first place.

**Theoretical contribution:** Organizational reliability in software systems is determined primarily by information exposure — specifically, the scope of incident knowledge sharing across teams. Processing capacity (how intensively teams work to learn) is not the bottleneck. This result aligns directly with Cohen & Levinthal (1990): absorptive capacity is primarily a function of prior knowledge and exposure to new knowledge, not processing intensity. The simulation provides controlled, systematic evidence for this theoretical claim in a software engineering organizational context.

---

## Part D: Conclusion

### What Was Built

This thesis developed an agent-based simulation of 20 software engineering teams sharing incident knowledge through a four-stage absorptive capacity pipeline — acquisition, assimilation, transformation, and exploitation — grounded in Zahra & George (2002). Teams operate across five network topologies (NONE, NEIGHBOR, GLOBAL, Erdos-Renyi, Barabási–Albert), encounter incidents drawn from a realistic subsystem distribution, and produce incidents as a function of knowledge gaps. The simulation was validated across nine publication-level experimental conditions with 100–500 seeds per condition and a 365-day horizon.

### What Was Found

**H1 — CONFIRMED.** Global incident knowledge sharing reduces incidents by 45% relative to no sharing. The GLOBAL > NEIGHBOR > NONE ordering holds from simulation day 1, persists through all robustness tests, and is not reversed by any parameter variation tested.

**H2 — CONFIRMED.** Deployment rate increases incidents monotonically, but global sharing absorbs this risk substantially. A 10× increase in deployments produces only a 24% increase in incidents under GLOBAL sharing — evidence that knowledge diffusion can buffer the reliability cost of deployment velocity.

**H3 — CONFIRMED** (500 seeds, extended exploitation range). Exploitation effectiveness shows diminishing returns: gains become marginal as exploitation probability exceeds 0.6. Critically, sharing scope (H1) dominates exploitation quality (H3) across the full parameter range. Who you share with matters more than how hard you try to learn.

**H4 — CONFIRMED.** Denser, more evenly connected networks accumulate incident knowledge faster and produce lower incident rates. Scale-free networks (BA) require sufficient hub connectivity (ba_m ≥ 3) to realize their advantage; extreme centralization (star topology) traps knowledge at the hub and underperforms ring and random networks.

### Practical Recommendations for Engineering Leaders

1. **Invest in global incident knowledge sharing platforms before investing in exploitation training.** The ROI differential is large: 45% incident reduction from sharing scope vs. 30% at the extreme end of exploitation improvement, with exploitation gains subject to diminishing returns.
2. **Avoid extreme centralization.** Star topologies trap knowledge at the hub. Even when hubs are highly capable, the bottleneck limits organizational learning speed.
3. **Hub-spoke organizations underperform unless hubs are well-connected.** BA networks require ba_m ≥ 3 — each hub must maintain multiple cross-team links to realize the scale-free advantage.
4. **Imperfect postmortem quality does not cancel the benefit of wider sharing.** Exploitation probability sweeps show that even poor documentation quality under GLOBAL sharing outperforms high-quality exploitation under NONE or NEIGHBOR sharing.
5. **The quantified ROI on global sharing:** 781 engineering hours saved per year per 20-team organization, representing a 2.3× return on the learning investment required to maintain a global incident knowledge sharing practice.

### Final Statement

This simulation provides the first controlled, systematic study of how knowledge sharing scope affects software organizational reliability. The findings are unambiguous: broader sharing produces fewer failures, and this effect is robust across team size, simulation duration, incident frequency, network topology, documentation quality, and knowledge decay rate. The recommendation to engineering leaders is clear — structure your organization to maximize incident knowledge exposure, not just knowledge processing intensity.
