# Model Limitations & Assumptions
**David Pineda | BYU CS MS Thesis**
**Running list — updated as discovered**

---

## How to Use This File

Each limitation has three parts:
1. **What the model assumes** — what we simplified
2. **What reality looks like** — where the assumption breaks down
3. **How to address it** — defense language or future work

---

## 1. All Knowledge Has Potential Value to All Teams

**What the model assumes:**
Every incident has some learning value for every team, modulated by cosine similarity. A frontend team receiving a database incident will have low transformation probability but still participates in the learning pipeline.

**What reality looks like:**
Some knowledge is domain-specific enough that no amount of similarity adjustment matters. A frontend team gains zero from deep database replication internals. The model slightly overstates benefit of sharing truly irrelevant incidents.

**How to address it:**
*"The model assumes incident knowledge has organizational value proportional to team similarity. In practice, some knowledge is domain-specific enough that sharing produces no benefit regardless of similarity. Future work could introduce a hard relevance threshold below which sharing produces zero benefit, testing whether H1 holds when truly irrelevant knowledge is explicitly excluded. We note that most software incident failure patterns — deployment errors, configuration mistakes, cascade effects, capacity failures — are universal across subsystem types, suggesting the majority of cross-team learning is legitimate."*

---

## 2. Scale-Free Property Not Statistically Verifiable at 20 Nodes

**What the model assumes:**
The Barabási-Albert network represents scale-free / hub-spoke topology behavior.

**What reality looks like:**
Proving a power-law degree distribution statistically requires 50-100+ nodes. At 20 teams, you have hub-spoke structure but cannot confirm it follows a true power law.

**How to address it:**
*"At 20 nodes, our BA network exhibits hub-spoke structural behavior rather than a statistically confirmed power-law distribution. We use it as a hub-spoke model, not as a claim of proven scale-free properties. The hub-spoke behavioral effects — peripheral team isolation, bottlenecked diffusion — are observable and measurable at 20 nodes. Testing at 50+ nodes is noted as future work."*

---

## 3. Knowledge Transfer Is Instantaneous Within a Timestep

**What the model assumes:**
When a team acquires knowledge from an incident, that knowledge is available immediately in the same timestep for subsequent calculations.

**What reality looks like:**
Real knowledge transfer has latency. A postmortem written today may not be read and understood for days or weeks. Teams have finite attention and learning bandwidth.

**How to address it:**
*"The model uses discrete daily timesteps where knowledge transfer completes within a single day. This is a simplification — real postmortem review and knowledge integration takes days to weeks. The effect of this assumption is likely to compress the time dynamics (H1 ordering would emerge more slowly in reality) without changing the directional findings."*

---

## 4. Fixed Stage Probabilities — Not Sensitive to Incident Severity

**What the model assumes:**
Acquisition probability (0.9), assimilation (0.7), transformation (gated by cosine similarity), exploitation (0.6) are fixed regardless of incident severity. A P1 outage and a P3 glitch have the same acquisition probability.

**What reality looks like:**
High-severity incidents command more attention. Teams are more likely to read postmortems for outages that cost the company $1M than for minor degradations. Acquisition probability should scale with severity.

**How to address it:**
*"Acquisition probability is fixed at 0.9 regardless of incident severity. In practice, high-severity incidents attract more organizational attention and are more likely to enter the learning pipeline. A severity-weighted acquisition function (p_acquire = base_prob × severity_weight) would more accurately model real org behavior. We treat this as future work — the current model establishes the baseline relationship between sharing scope and reliability before adding severity dynamics."*

---

## 5. Same Coin Tossed Every Day — No Forgetting of Failed Attempts

**What the model assumes:**
If a team fails to acquire knowledge from an incident on day 1, it tries again on day 2 with the same probability. Failed acquisition attempts don't reduce future probability.

**What reality looks like:**
In real orgs, if a team ignores a postmortem for two weeks, it becomes stale and even less likely to be read. The urgency decays. There may be a window of opportunity that closes.

**How to address it:**
*"The model applies a fixed acquisition probability each timestep regardless of how long since the incident occurred. In practice, the relevance and urgency of an incident postmortem decays over time — teams are less likely to engage with old incidents. A time-windowed acquisition probability would better capture this. The current approach may slightly overstate eventual knowledge acquisition rates."*

---

## 6. Teams Are Homogeneous in Size and Capacity

**What the model assumes:**
All 20 teams are identical in size, expertise level, and learning capacity. A team with 3 engineers and a team with 15 engineers have the same probability of acquiring and exploiting knowledge.

**What reality looks like:**
Larger teams have more capacity to dedicate to postmortem review. Senior teams have higher absorptive capacity (Cohen & Levinthal) — they understand new knowledge faster because of deeper prior experience.

**How to address it:**
*"The model treats all teams as homogeneous learning units. Real orgs have teams of varying size, seniority, and domain expertise. Heterogeneous teams would create asymmetric learning rates — some teams accumulate knowledge faster than others. Future work could introduce team-level capacity parameters to study how expertise distribution affects org-level reliability."*

---

## 7. Network Topology Is Static — Does Not Evolve

**What the model assumes:**
The network of connections between teams is fixed at initialization and does not change over 365 days.

**What reality looks like:**
Real org networks evolve. Teams form new relationships through projects. Reorgs change reporting structures. People move between teams. The network topology at day 365 looks different from day 1.

**How to address it:**
*"Network topology is fixed at simulation initialization. Real organizational networks evolve through hiring, reorgs, and project collaboration. Dynamic network evolution could either help (new connections accelerate diffusion) or hurt (broken connections slow it). We treat static topology as a baseline assumption, with dynamic networks as future work."*

---

## 8. Knowledge Decay Is Uniform Across All Teams and Knowledge Types

**What the model assumes:**
All teams forget knowledge at the same rate (default half-life ~2 years). All types of knowledge (prevention, detection, mitigation) decay at the same rate.

**What reality looks like:**
Operational knowledge embedded in runbooks and automated checks doesn't decay — it's codified. Tacit knowledge in engineers' heads decays fast when people leave. Different subsystem knowledge types may have very different retention curves.

**How to address it:**
*"Knowledge decay is modeled as a uniform exponential decay across all teams and knowledge types. In practice, codified knowledge (runbooks, automated checks) is persistent while tacit knowledge decays with team turnover. A two-component decay model (codified + tacit) would better represent real knowledge retention. The decay rate sweep (half-life 2 weeks to 19 years) shows H1 holds across a wide range, suggesting findings are robust to this simplification."*

---

## Summary Table

| # | Limitation | Impact on H1? | Addressed by | Future Work? |
|---|---|---|---|---|
| 1 | All knowledge has value to all teams | Minor overstatement | Cosine similarity filter | Relevance threshold |
| 2 | BA not provably scale-free at 20 nodes | None — behavior measurable | ba_m sweep | Test at 50+ nodes |
| 3 | Instantaneous knowledge transfer | Compresses time dynamics | Time dynamics analysis | Latency model |
| 4 | Fixed acquisition regardless of severity | May understate high-severity learning | — | Severity-weighted acquisition |
| 5 | Same probability every day, no urgency decay | May overstate eventual acquisition | Knowledge decay sweep | Time-windowed acquisition |
| 6 | Homogeneous team sizes | May miss expertise asymmetry | — | Team capacity parameters |
| 7 | Static network topology | Misses reorg effects | — | Dynamic network evolution |
| 8 | Uniform knowledge decay | Misses codified vs tacit distinction | Decay rate sweep | Two-component decay model |

**Key point for defense:** None of these limitations reverse the directional findings. H1 ordering is robust across every parameter variation tested. Limitations affect magnitude, not direction.
