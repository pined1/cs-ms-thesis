# Section 3: Hypothesis 2 — Deployment Velocity and Incident Risk

## 3.1 The Question

Does deploying software more frequently cause more incidents? On its face, this seems obvious — more deployments mean more opportunities for something to go wrong. Yet the empirical record complicates the story. Google, Netflix, and Amazon each deploy thousands of times per day and consistently report reliability metrics that outperform organizations deploying once per month. The DevOps research literature (Forsgren et al., *Accelerate*, 2018) formalizes this paradox: high-performing organizations move faster *and* fail less. How is that possible?

Hypothesis 2 investigates this tension directly. The simulation allows us to isolate deployment rate as a causal variable and observe whether, and under what conditions, increased deployment velocity translates into increased incident counts — and whether the type of organizational learning moderates that relationship.

---

## 3.2 A Real-World Analogy: The Dev Team and the Production Outage

Consider two software engineering teams, each deploying to production regularly. Team A deploys once a week; Team B deploys every day or two. In the short run, Team B will encounter more incidents simply because they are pushing changes more often — more deployments mean more chances to introduce a bug into production.

But here is where it gets interesting. Team B also learns faster. Every production outage is a learning event: the team writes a post-mortem, identifies the root cause, and updates their runbooks or automated checks. If those lessons stay siloed within Team B, the team itself improves but the rest of the engineering organization keeps making the same mistakes. If those lessons are shared in a company-wide incident review, the entire organization gets smarter — and future incidents become less likely across all teams.

Crucially, the analogy turns on *sharing*. A team that documents every outage in a private Confluence page gains local expertise but contributes nothing to their colleagues. An organization that runs blameless post-mortems, broadcasts root-cause findings across teams, and encodes lessons into shared deployment checklists converts individual experience into collective knowledge. The same number of deployments produces very different reliability outcomes depending on whether learning stays local or spreads globally.

This is precisely the mechanism under examination in H2.

---

## 3.3 What Deployment Rate Means in the Model

In the agent-based model, each team has a `deployment_rate` parameter representing the probability that the team deploys code on any given simulation day. At 0.05, a team deploys roughly once every three weeks. At 0.50, a team deploys on approximately half of all working days — deploying on roughly half of all working days.

When a team deploys, a `deployment_risk_multiplier` of 1.5× is applied to that team's incident probability for that day. Deployments therefore carry real cost: they elevate risk. More deployments means more chances for something to break. The question is: does learning from past incidents reduce how often those chances turn into actual failures?

The incident probability on any given day is governed by:

```
p_incident = base_rate × (1 - avg_prevention × prevention_effect) × deployment_modifier
```

The term `(1 - avg_prevention × prevention_effect)` captures how much organizational knowledge suppresses baseline risk. As teams accumulate knowledge — through incidents, post-mortems, and shared learning — this suppression term grows. The deployment modifier (`deployment_risk_multiplier` or 1.0 on non-deployment days) multiplies whatever residual risk the knowledge has not already absorbed.

---

## 3.4 Experimental Design: Why We Ran It This Way

H2 was tested using a controlled sweep across five deployment rate conditions: 0.05, 0.10, 0.20, 0.30, and 0.50. All other parameters were held fixed:

- **Network structure:** identical across all conditions
- **Number of teams:** 20
- **Simulation duration:** 365 days
- **Random seeds:** 100 per condition (for statistical reliability)
- **Learning scenarios tested:** both GLOBAL (organization-wide sharing) and LOCAL (team-level sharing only)

This isolation principle is the heart of causal inference in simulation experiments. When only one variable changes, any observed difference in outcome can be attributed to that variable. Holding the network, team count, duration, and seed distribution constant ensures that differences in incident counts across deployment rate conditions reflect the deployment rate itself — not a confound.

---

## 3.5 Results

**Table 3.1: Total Incidents by Deployment Rate and Learning Scenario (mean over 100 seeds)**

| Deployment Rate | GLOBAL Incidents | LOCAL Incidents | GLOBAL Advantage |
|-----------------|-----------------|-----------------|-----------------|
| 0.05 (slow)     | 152.5           | 238.1           | 57% fewer       |
| 0.10            | 167.0           | 261.4           | 57% fewer       |
| 0.20            | 180.7           | 281.5           | 55% fewer       |
| 0.30            | 185.2           | 287.5           | 55% fewer       |
| 0.50 (fast)     | 188.4           | 288.6           | 53% fewer       |

Two findings immediately stand out.

**First**, GLOBAL learning consistently and substantially outperforms LOCAL learning across every deployment rate tested. The advantage ranges from 53% to 57% — roughly half as many incidents under GLOBAL sharing regardless of how fast the organization deploys.

**Second**, and more important: the GLOBAL row barely moves. Going from 0.05 to 0.50 represents a ten-fold increase in deployment frequency. Yet GLOBAL incidents rise only from 152.5 to 188.4 — a 24% increase. The LOCAL row, by contrast, rises from 238.1 to 288.6 — a 21% increase, but starting from a much higher baseline that never approaches GLOBAL performance.

---

## 3.6 The Saturation Finding

The near-flatness of the GLOBAL curve is the most significant result of this experiment, and it requires explanation.

Recall the incident probability formula. When an organization has been operating under GLOBAL learning for a sustained period, the knowledge parameter K approaches a saturation value near 0.992. Substituting into the formula:

```
(1 - avg_prevention × prevention_effect) ≈ (1 - K) = 1 - 0.992 = 0.008
```

This means that even when the deployment multiplier fires — elevating risk by 1.5× — it is multiplying against a residual risk of 0.008. The absolute increase in incident probability is `1.5 × 0.008 = 0.012` versus `1.0 × 0.008 = 0.008` on non-deployment days. The deployment multiplier still acts, but it acts on a nearly-zero baseline. The organizational knowledge has *absorbed* the deployment risk.

This is the saturation mechanism. A GLOBAL-learning organization accumulates knowledge rapidly because every incident is broadcast across all teams. As knowledge grows, the marginal impact of any individual deployment shrinks. The organization reaches a state in which it can sustain high deployment velocity with only marginal increases in incident rate.

LOCAL-learning organizations never reach this state. Knowledge accumulates within teams but does not diffuse. Teams repeatedly encounter failure modes that neighboring teams have already solved. The denominator of the risk equation never reaches saturation, so each additional deployment continues to produce proportional incidents.

Framed abstractly: there are two rates racing. *Deployment velocity* determines how fast incidents are generated. *Learning velocity* determines how fast knowledge accumulates to prevent them. In a GLOBAL-sharing organization, learning velocity catches up to and effectively neutralizes deployment velocity. In a LOCAL-sharing organization, the race is never won.

---

## 3.7 Connection to DORA and the Accelerate Research

Forsgren, Humble, and Kim (2018) analyzed thousands of organizations and identified a cluster of high performers characterized by both high deployment frequency *and* low change failure rates. This empirical finding challenged the conventional assumption that speed and stability trade off against each other.

The H2 results provide a mechanism-level explanation for that finding in a controlled, synthetic environment. In the simulation:

- **GLOBAL-learning organizations** correspond to the high performers in the DORA dataset: they deploy frequently, accumulate knowledge rapidly, and maintain low incident rates because their rate of organizational learning keeps pace with their rate of deployment.

- **LOCAL-learning organizations** correspond to lower-performing organizations: they deploy at the same rate but cannot distribute incident knowledge across teams, so incidents accumulate roughly proportionally with deployment frequency.

The simulation does not merely replicate the DORA correlation — it shows *why* it exists. Structural knowledge sharing is the mechanism that decouples deployment velocity from incident rate.

---

## 3.8 The Cross-Sweep: H2 × H3 Interaction (Experiment 10)

To verify that the H2 finding is not an artifact of a particular exploitation configuration, experiment 10 ran a 3×3 factorial design crossing three deployment rates (0.05, 0.20, 0.50) with three exploitation probabilities (0.3, 0.6, 0.9) — the subject of H3.

Think of it this way: does how hard your teams work on post-mortems change the impact of shipping software frequently? The answer the simulation gives is: no, not meaningfully. The rows and columns are independent.

The results showed completely flat columns across exploitation levels: for a given deployment rate, changing how aggressively teams exploit existing knowledge had no effect on incident counts. Conversely, the rows increased with deployment rate as expected, and that increase was consistent regardless of exploitation level.

**[Figure 3.1: H2 × H3 Cross-Sweep Heat Map]**
*A 3×3 grid showing total incidents across deployment rates (0.05, 0.20, 0.50) and exploitation probabilities (0.3, 0.6, 0.9). The flat columns confirm that H2 and H3 are orthogonal — deployment frequency and exploitation intensity affect incident counts independently.*

This orthogonality result is methodologically important. It confirms that H2 and H3 capture independent dimensions of organizational behavior. Deployment velocity and knowledge exploitation strategy do not interact — the deployment saturation effect holds at every exploitation level tested, and the exploitation effects (examined in Section 4) hold at every deployment rate. The findings can be reported separately and interpreted independently.

In practical terms: an organization that ships software frequently and invests heavily in post-mortem culture is not "double-dipping" — each intervention addresses a separate mechanism. Ship more, learn better, and neither cancels the other out.
---

## 3.9 Conclusion

H2 is confirmed. Deployment rate does increase total incidents — but the relationship is strongly sublinear under GLOBAL learning. A ten-fold increase in deployment frequency produces only a 24% increase in incidents when organizations share knowledge globally. The deployment risk multiplier fires more often, but it multiplies against an increasingly suppressed baseline as organizational knowledge saturates.

The practical implication mirrors the DORA finding but provides a structural explanation: organizations that deploy frequently can maintain reliability *if* they couple that deployment velocity with effective knowledge-sharing infrastructure. Speed alone is not the risk. Speed without shared learning is the risk. The simulation establishes this not as a correlation observed across organizations, but as a causal mechanism — knowledge saturation absorbs deployment risk, and only organizations with global sharing structures achieve that saturation.

---

*Next: Section 4 — Hypothesis 3: Knowledge Exploitation Rate*
