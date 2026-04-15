# Section 6: Ablation Tests — exp11 and exp12

## 6.1 What Is an Ablation Test?

A simulation model is composed of design decisions — assumptions encoded as parameters, pipeline stages, and behavioral rules. Some of those decisions are *load-bearing*: remove them, and the model's behavior changes in important ways. Others are *robust assumptions*: remove them, and the results barely shift. An ablation test is how you tell the difference.

The engineering analogy is straightforward. Building a car, you can remove one component at a time and observe what breaks. Remove the engine — the car stops. Remove the cup holder — the car is fine. Each removal teaches you something about which components are structural and which are incidental. Neither answer is wrong; the point is knowing which is which.

In simulation, the same logic applies. You disable one model component, re-run the full experiment under identical conditions, and compare the output to the default. If the results shift dramatically, that component is doing real explanatory work and must be justified carefully. If the results barely move, you have evidence that the model is robust to that assumption — it is not a fragile crutch the conclusions depend on.

Experiments 11 and 12 each target a different component of the H1 learning model. Both were run under the same conditions as the primary H1 experiment: **20 teams, Watts-Strogatz small-world network, 365 simulated days, 100 independent random seeds, all four scenarios (NONE, LOCAL, NEIGHBOR, GLOBAL)**. The default results serve as the baseline against which each ablation is compared.

---

## 6.2 exp11 — Removing Knowledge Decay

### 6.2.1 What Knowledge Decay Models

In the default simulation, prevention knowledge is not permanent. Knowledge earned by a team on day 10 slowly erodes by day 200 if it is not reinforced through additional incidents or cross-team learning. The rate of erosion follows an exponential decay function with a half-life of approximately two years (decay rate = 0.001 per timestep).

This models a well-documented organizational reality. Engineers leave teams, taking their experience with them. Runbooks go stale when the systems they describe are quietly refactored. On-call rotations cycle, and the institutional memory of a particular failure mode fades when the people who lived through it are no longer in the rotation. The knowledge is not destroyed — it is simply no longer maintained, and maintenance requires active reinforcement.

The empirical grounding for this choice is Darr, Argote, and Epple's (1994) study of organizational forgetting in the pizza franchise industry, published in *Management Science*. They tracked production knowledge across franchise locations and found that knowledge accumulated during active periods decayed measurably when production paused — and that some knowledge transferred between locations while some did not. A half-life of two years is a conservative, plausible estimate for a software engineering organization that runs incidents regularly enough to provide some natural reinforcement.

### 6.2.2 What exp11 Turns Off

In exp11, the knowledge decay rate is set to **0.0**. Knowledge earned at any point in the simulation is retained at full strength indefinitely. There is no forgetting. All other model parameters and conditions are identical to the H1 default.

The question exp11 answers is: does the two-year decay assumption materially influence the findings, or does H1's ordering hold regardless of whether teams forget?

### 6.2.3 Results

| Scenario | Default (decay on) | No Decay (exp11) | Difference |
|----------|--------------------|------------------|------------|
| NONE | 484.3 | 484.3 | 0.0 |
| LOCAL | 406.4 | 398.5 | -7.9 fewer |
| NEIGHBOR | 336.0 | 323.0 | -13.0 fewer (3.9%) |
| GLOBAL | 265.6 | 263.3 | -2.3 fewer |

Lower incident counts are better. A negative difference means the scenario performs better when decay is removed.

### 6.2.4 Why NEIGHBOR Benefits Most

NEIGHBOR accumulates knowledge slowly, building outward from source teams one hop at a time over many months. Because that accumulation is gradual and spread across many teams at moderate levels, decay chips away at it continuously before it ever reaches a self-reinforcing peak. When decay is turned off, all that slowly-built knowledge is preserved in full — and NEIGHBOR sees the largest gain (13 fewer incidents) as a result.

GLOBAL, by contrast, rapidly saturates organizational knowledge. By approximately day 90, the GLOBAL scenario reaches K = 0.992 — meaning 99.2% of maximum possible prevention knowledge is already in place. At that level, every new incident immediately reinforces what teams already know, so the organization is effectively re-learning the same lessons constantly. Decay has almost nothing to act on: knowledge that is being actively replenished each day barely erodes. This is why removing decay changes GLOBAL's result by only 2.3 incidents — there was almost nothing for decay to take away in the first place.

LOCAL shows a modest improvement (7.9 fewer incidents) because its knowledge accumulation, while real (K = 0.555), is moderate and limited to a single team per incident. Removing decay benefits it more than GLOBAL but less than NEIGHBOR, consistent with its intermediate knowledge level.

NONE does not change at all. With no learning pipeline active, there is no knowledge to decay.

### 6.2.5 Verdict

The H1 ordering — GLOBAL > NEIGHBOR > LOCAL > NONE — is preserved in both conditions. Removing decay modestly improves all learning scenarios, with the largest effect on NEIGHBOR. The directional finding is unchanged.

Knowledge decay is a **meaningful, well-grounded component**: it is empirically motivated, it affects results in the expected direction, and its removal produces interpretable changes consistent with the model's internal logic. But it is not a result-generating assumption — the core conclusion does not depend on it. The model is robust to this design choice.

---

## 6.3 exp12 — Removing Source Asymmetry

### 6.3.1 What Source Asymmetry Models — and Why It Exists

Source asymmetry is one of the more structurally important design decisions in the learning pipeline, and it requires careful explanation.

When an incident occurs at Team A — the *source team* — Team A is skipped in stages 2 through 4 of the post-incident learning pipeline. The rationale is that Team A *owns* the affected subsystem and has just lived through the incident in real time. Routing Team A back through the standard learner pipeline for its own incident would artificially double-count its learning: the team would receive knowledge credit both from direct experience and from the pipeline designed for teams that heard about the incident secondhand.

All other teams that fall within the learning scope — neighbors in NEIGHBOR, or everyone in GLOBAL — proceed through the full four-stage pipeline. The source team is treated *asymmetrically* from every other learner. This distinction is not arbitrary; it reflects a real organizational difference between the team that owns a failure and the teams that are learning from someone else's failure.

### 6.3.2 Why Asymmetry Is Especially Consequential for LOCAL

In the LOCAL scenario, the *only* learner after an incident is the source team itself — no neighbors, no broader organization. The pipeline is structurally defined as: "inform the team that owns this subsystem." But because source asymmetry skips the source team from stages 2–4, and the source team is the only team in scope, the full cross-team pipeline never fires. The source team receives implicit learning credit from the incident itself, but no team undergoes the standard multi-stage knowledge transformation process for cross-team incidents.

This is the mechanistic explanation for LOCAL's 0% transformation rate (reported in Section 2). It is not a bug or a calibration artifact — it is the direct consequence of the source asymmetry rule interacting with LOCAL's narrow learning scope.

### 6.3.3 What exp12 Turns Off

In exp12, the source team skip is removed. The source team now proceeds through all four pipeline stages for its own incident, exactly like any other learner. All other parameters are unchanged.

The question exp12 answers is: what happens to learning efficiency — particularly LOCAL's — when the source team is no longer treated differently from other learners?

### 6.3.4 Results

| Scenario | Default (asymmetry on) | No Asymmetry (exp12) | Difference |
|----------|------------------------|----------------------|------------|
| NONE | 484.3 | 484.3 | 0.0 |
| LOCAL | 406.4 | 437.6 | +31.2 more (+7.7%) |
| NEIGHBOR | 336.0 | 348.6 | +12.6 more (+3.7%) |
| GLOBAL | 265.6 | 265.2 | ~0 |

Higher incident counts are worse. A positive difference means the scenario performs worse when asymmetry is removed.

### 6.3.5 Interpreting the Results

**LOCAL gets substantially worse (+7.7%).** This is the most important finding in exp12. In the default model, the source team's asymmetric treatment is not simply a skip — it is also the pathway through which LOCAL does its learning. The source team, as the sole learner, receives an efficient direct learning credit from living through the incident. When exp12 forces the source team through the standard probability-weighted pipeline instead — a pipeline designed for teams learning at one remove from the failure — that direct efficiency is replaced by a lower-probability knowledge acquisition process. LOCAL loses its primary learning mechanism and produces 31 more incidents as a result.

This finding reveals a structural weakness in LOCAL learning. In a LOCAL-only organization, the only team that ever learns from an incident is the team that experienced it. All of LOCAL's learning benefit depends on exactly one mechanism: the source team learning directly from its own failure. There is no backup, no distributed safety net, no organizational memory that outlives that single team's experience. When exp12 disrupts that one mechanism — by forcing the source team through a lower-probability pipeline designed for secondhand learners — LOCAL has nothing to fall back on, and incident counts rise substantially. It is like a company where the only person who documents lessons learned is the person who made the mistake. If that person leaves, or is too busy, the organization loses everything it could have learned.

**NEIGHBOR drops moderately (+3.7%).** The source team is one of several learners in NEIGHBOR. Removing its efficient direct-learning path hurts, but the neighboring teams still receive knowledge through the standard pipeline and partially compensate for the loss. The effect is real but absorbed across the broader learning network.

**GLOBAL barely changes (~0 incidents).** With 20 teams learning from every incident, the difference attributable to one team's pipeline path is diluted to near-zero by the volume of other learners. GLOBAL's strength is precisely this redundancy — no single team's learning efficiency determines the organizational outcome.

**NONE does not change.** No learning pipeline means no asymmetry to remove.

### 6.3.6 Connection to LOCAL's Knowledge Ceiling

This mechanistic explanation directly corroborates the knowledge-level finding from Section 2. LOCAL's prevention K of 0.555 — less than half of GLOBAL's 0.992 — is not simply a consequence of lower sharing breadth. It is a consequence of structural isolation: the only knowledge that accumulates in LOCAL belongs to the team that experienced each specific failure. That knowledge is not cross-pollinated, not validated against other teams' experiences, not compounded across organizational boundaries. Removing source asymmetry exposes exactly this fragility — when LOCAL's one efficient learning path is disrupted, the scenario has no fallback.

### 6.3.7 Verdict

Source asymmetry is the **most structurally revealing ablation** in this study. It does not simply adjust a parameter — it removes a design decision that turns out to be mechanistically central to LOCAL's behavior. The 7.7% degradation in LOCAL when asymmetry is removed exposes the fragility of narrow, source-centric learning: a model that depends entirely on the incident-owning team to carry organizational knowledge forward.

The H1 ordering — GLOBAL > NEIGHBOR > LOCAL > NONE — is preserved in both conditions. This matters: even with asymmetry removed and LOCAL performing worse, it still outperforms NONE. The directional finding holds. But the margin of LOCAL's advantage narrows, and the structural reason for that narrowing is now precisely understood.

---

## 6.4 Combined Conclusion: What exp11 and exp12 Together Establish

Two ablations were run. Each targeted a different component. Each produced coherent, interpretable results. Together, they accomplish three things.

**First, they strengthen confidence in model validity.** When components are removed and results change in the direction and magnitude the model's logic predicts — NEIGHBOR benefiting most from removing decay, LOCAL degrading most from removing source asymmetry — that is evidence the model is behaving consistently with its own internal structure. The components are doing what they were designed to do.

**Second, they demonstrate robustness to design choices.** Neither ablation reverses H1. Neither ablation changes which scenario ranks best or worst. The ordering is not an artifact of decay rates or pipeline asymmetry — it is a property of knowledge flow structure, which is what the hypothesis is actually about.

**Third, they provide mechanistic insight beyond the primary results.** Exp12 in particular does not merely confirm H1 — it explains *why* LOCAL has zero transformation events and a knowledge ceiling far below NEIGHBOR and GLOBAL. The source asymmetry result is not a sensitivity check; it is a diagnostic tool that reveals the structural fragility of local-only learning architectures. That finding is an independent contribution to the model's interpretive value, independent of whether H1 is confirmed.

The simulation's components are individually justified and collectively robust. Decay captures organizational forgetting. Source asymmetry captures the real difference between learning from your own failure and learning from someone else's. Both are grounded in the literature. Both affect results in interpretable ways. Neither is a crutch the primary conclusions depend on.
