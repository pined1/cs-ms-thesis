# Section 2: H1 — Learning Strategy Comparison

## 2.1 The Central Question

Does sharing incident knowledge more broadly reduce system failures? Intuitively, we might expect the answer to be yes — but the simulation allows us to ask a more precise version of this question: does *who* you share knowledge with determine how reliably your system performs, and does the relationship hold monotonically? That is, the more teams you share with after an incident, the fewer incidents occur in the future?

H1 states: **GLOBAL > NEIGHBOR > LOCAL > NONE**, where "greater" means fewer incidents and higher availability. This section presents the evidence for that ordering and examines how robust it is across a wide range of conditions.

---

## 2.2 A Real-World Analogy: The Postmortem Sharing Decision

Consider how software organizations handle a production outage. When a deployment causes a service failure, the on-call team investigates, resolves the incident, and writes a postmortem. That postmortem contains lessons — about what configuration was wrong, what monitoring was missing, what the cascade looked like. The question is what happens next.

If the postmortem stays in the owning team's private Confluence space, that is *local learning* — the knowledge is isolated to the team that lived through the failure. If the team posts it in a shared Slack channel that adjacent teams follow, that is *neighbor-level learning* — the signal reaches teams close in the org graph. If the team presents findings in a company-wide incident review attended by all engineering teams, that is *global learning* — every team hears it and can update their own runbooks and practices accordingly.

The outcome metric in all cases is the same: how many similar incidents does the organization experience going forward? The mechanism is the same: team-level knowledge accumulation driven by exposure to incident findings. The only variable is the structural reach of that knowledge after each incident occurs.

Our simulation uses the same logic. The organization is the unit of measurement. The mechanism is agent-level knowledge accumulation that reduces future incident probability. The variable under test is the boundary of knowledge dissemination.

---

## 2.3 The Four Scenarios

Each scenario holds everything constant — team count, network topology, incident rates, simulation duration, random seed distribution — and varies only who receives knowledge after an incident occurs.

| Scenario | Who Learns After an Incident |
|----------|------------------------------|
| **NONE** | No one. Incidents occur, nothing is updated. Pure baseline. |
| **LOCAL** | Only the team that owns the affected subsystem. Like an on-call engineer who fixes the outage, jots down notes in a private doc, and never shares them with anyone else. |
| **NEIGHBOR** | The source team plus all teams directly connected to it in the network. Like posting a postmortem in a shared Slack channel that adjacent teams follow. |
| **GLOBAL** | Every team in the organization, regardless of proximity. Like a mandatory company-wide incident review where all engineering teams attend and update their own runbooks. |

NONE establishes the floor: what does an organization look like when it treats every incident as a one-off, learns nothing, and repeats the same failures? The other three scenarios measure how far you can move away from that floor by changing information flow structure alone.

---

## 2.4 Experimental Setup

The simulation modeled an organization of **20 teams** connected via a **Watts-Strogatz small-world network** — a topology chosen because it balances local clustering with short average path lengths, which is characteristic of how real engineering organizations tend to be structured (tightly-knit sub-groups with a few cross-cutting connections).

Each scenario ran for **365 simulated days** across **100 independent random seeds**. A "seed" controls all stochastic elements of the simulation — which subsystems fail, when, and by how much. Running 100 seeds is equivalent to running the same organizational experiment in 100 parallel universes with the same starting conditions. This gives us a distribution of outcomes rather than a single number, which allows for rigorous statistical comparison and ensures results are not artifacts of a lucky (or unlucky) random draw.

Everything except the learning scenario was held constant across all four conditions.

---

## 2.5 Core Results

| Scenario | Mean Incidents | Availability | Prevention K | Transform % |
|----------|---------------|--------------|--------------|-------------|
| NONE | 484.3 | 98.29% | 0.000 | 0.0% |
| LOCAL | 406.4 | 98.66% | 0.555 | 0.0% |
| NEIGHBOR | 336.0 | 98.97% | 0.890 | 14.0% |
| GLOBAL | 265.6 | 99.26% | 0.992 | 89.5% |

**Mean Incidents** is the total number of system failures the organization experienced over 365 days, averaged across 100 seeds. Lower is better.

**Availability** is the percentage of time the system was operating normally. It is the primary reliability metric from an end-user perspective — the number a service-level agreement would reference. The differences here (98.29% to 99.26%) may look small in absolute terms, but at organizational scale they translate to meaningfully different amounts of downtime. Moving from NONE to GLOBAL represents roughly 45 minutes less downtime per week per team. [  --- NOTE -- May wan to explain how we measure this more clearly and why ]

**Prevention K** is the organization's mean knowledge capital at simulation end, measured on a 0–1 scale. K captures how much relevant incident-prevention knowledge has accumulated across teams. A K of 0.000 means teams carry no accumulated knowledge; a K of 0.992 means teams are operating near the maximum of what the knowledge model permits. Prevention K is the mechanism: it is *how* learning reduces incidents. [ -- NOTE -- talk about in detail how we got this and why? ]

**Transform %** is the percentage of incidents that triggered a *knowledge transformation event* — a moment when a team's accumulated knowledge crossed a cosine-similarity threshold high enough to unlock structural changes to how they handle that class of incident (analogous to updating a runbook or changing an architecture pattern, rather than just absorbing information). Transformations represent deep organizational change, not just marginal improvement. [ --- NOTE -- I think we can simplify the language here]

---

## 2.6 The Transformation Rate Jump: Source Asymmetry

The 0% transformation rate for LOCAL requires explanation, because LOCAL does accumulate knowledge (K=0.555). The mechanism is what we call *source asymmetry*: in the simulation, the team that owns the affected subsystem is designated the incident source and is skipped in the post-incident learning pipeline — it is assumed to have learned implicitly by experiencing the failure. Under LOCAL, no other teams are in the learning pipeline. This means the cross-team pipeline never fires, and transformation events — which require cross-team knowledge diffusion to accumulate sufficient cosine similarity — never occur.

NEIGHBOR breaks this by introducing at least one non-source team into every learning event. The 14% transformation rate reflects that cosine similarity now accumulates across team boundaries, but slowly — neighbors are few, and knowledge must travel through multiple hops to reach teams where it compounds.

GLOBAL reaches 89.5% because every team receives every incident's knowledge immediately. Cosine similarity rises quickly across the full organization, the transformation threshold is crossed repeatedly, and structural learning — not just incremental knowledge adjustment — becomes the norm.

---

## 2.7 When Does the Ordering Emerge?

H1 holds from the first observable window. In the first 30-day measurement window, the NONE > LOCAL > NEIGHBOR > GLOBAL incident ordering is already present and statistically distinguishable. There is no warm-up period in which scenarios cluster together before separating.

Under GLOBAL, Prevention K plateaus near K=0.992 by approximately day 90 of the simulation. After that point, the organization is not accumulating materially new knowledge — it has approached the ceiling of what the model permits. The continued incident reduction from day 90 onward is attributable to the existing high-K state preventing failures, not to new learning.

---

## 2.8 Effect Sizes

Cohen's d measures how far apart two distributions are in terms of standard deviations. A d of 0 means the distributions are identical; a d above 0.8 is conventionally classified as a *large* effect (Cohen, 1988). All pairwise comparisons between scenarios exceed this threshold.

| Comparison | Cohen's d | Interpretation |
|------------|-----------|----------------|
| NONE vs. LOCAL | 4.23 | Large |
| NONE vs. NEIGHBOR | 7.89 | Large |
| NONE vs. GLOBAL | 11.51 | Large |
| LOCAL vs. NEIGHBOR | 3.67 | Large |
| LOCAL vs. GLOBAL | 7.28 | Large |
| NEIGHBOR vs. GLOBAL | 3.44 | Large |

The NONE vs. GLOBAL d of 11.51 is particularly notable. At d=11.51, the two distributions do not overlap at all — there is no seed in the NONE condition that produces an outcome as good as the worst seed in the GLOBAL condition. These are categorically different organizational regimes, not gradations of the same outcome. [ -- Note-- Can you explain in detail in lamen terms what these distribution means.. for someone that may not understand it at all..]

---

## 2.9 Robustness

H1 holds — with the same directional ordering and large effect sizes — across every sensitivity dimension tested:

- **Team count:** 6, 20, and 50 teams
- **Simulation duration:** 180 to 1,095 days
- **Incident rate:** 0.01 to 0.20 daily probability per subsystem
- **Knowledge decay:** half-lives ranging from approximately 2 weeks to 19 years
- **Documentation quality:** from poor (high noise in knowledge transfer) to high fidelity

The ordering is not a function of organizational size, time horizon, failure environment, memory persistence, or information quality. It is a structural property of knowledge flow.

---

## 2.10 Conclusion

Broader knowledge sharing monotonically reduces organizational incident rates, and the effect is large enough to be practically unambiguous across all tested conditions. The practitioner implication follows directly: **the structural boundary of who you share incident knowledge with — not the quality of the post-mortem document or the skill of the team that experienced the failure — is the dominant driver of organizational reliability.** Investing in cross-team knowledge sharing mechanisms (blameless post-mortems distributed organization-wide, shared runbooks, cross-functional incident reviews) is not a process nicety; it is the primary reliability lever available to an engineering organization.
