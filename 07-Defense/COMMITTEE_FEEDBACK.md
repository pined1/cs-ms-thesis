# Committee Feedback — Proposal Defense
**Date received: 2026-03-30**

---

## Raw Feedback (from advisor)

> Hi David,
>
> Nice job on fielding questions. Here is feedback/questions from the proposal defense:
>
> - How large does the network need to be for "scale-free"?
> - How does learning strategy affect probabilities?
> - Why are we modeling all 4 stages of the absorptive capacity?
> - Could we track developer hours across each stage?
> - Where could we publish this? (A paper to go with the open source tool?)
> - What else can you do with it? Let's explore the limits, etc.
>
> The committee would appreciate some progress reporting. Say after the validation work is done.
>
> Paper suggestions: (1) walk through an example, and (2) give more detailed and clear explanation of concepts and how they work concretely in the simulator.

---

## Questions to Address in Thesis

### 1. How large does the network need to be for "scale-free"?
- Barabási-Albert networks need a minimum node count before scale-free (power-law degree distribution) properties emerge
- Address in methodology chapter: state minimum team count used and justify it

### 2. How does learning strategy affect probabilities?
- Need a clear mechanical explanation of how switching from LOCAL → NEIGHBOR → GLOBAL changes stage-transition probabilities
- Methodology chapter needs a concrete walkthrough of the 4-stage pipeline for each scenario

### 3. Why are we modeling all 4 stages of absorptive capacity?
- Justify why 4 stages vs. a simpler 2-stage model
- Key argument: assimilation and transformation represent distinct failure modes — collapsing them loses explanatory power

---

## Potential Model Enhancement

### 4. Track developer hours per stage
- Currently: total engineering cost tracked
- Committee wants: per-stage cost breakdown (hours in acquisition, assimilation, transformation, exploitation)
- Would strengthen the cost model and make it more publishable

---

## Future Work / Publication

### 5. Where to publish?
- Committee sees a paper opportunity alongside the open-source simulator
- Possible venues: ICSE, MSR, or software engineering simulation conferences
- Format: simulator paper + worked example

### 6. Explore the limits
- Stress-test the model: extreme team sizes, degenerate networks, edge-case parameters
- Ablations (exp11–13) cover some of this — room to extend further

---

## Process Items

- [ ] Send committee a **progress report after validation work is done** (target: end of Week 4, Apr 5)
- [ ] Paper writing: (1) walk through a concrete example end-to-end, (2) explain each concept with its simulator mapping

---

## Follow-Up Meeting Notes — 2026-03-31
*(Notes from advisor conversation — open design questions)*

### A. Why 4 stages instead of a single joint probability?

Advisor questioned: why not collapse acquisition × assimilation × transformation × exploitation
into one probability P(learning)? David's answer: we want to capture knowledge **at each stage**
separately — this lets us observe where in the pipeline knowledge fails, track per-stage effort,
and see that e.g. transformation is the bottleneck in LOCAL (0% transform) vs GLOBAL (89.5%).

**Keeping 4 stages. Justification in methodology chapter:**
- Each stage is a distinct failure mode
- Stage-specific failure explains the transformation jump (LOCAL 0% → NEIGHBOR 14% → GLOBAL 89%)
- Per-stage hours tracking makes the cost model richer

---

### B. Is the same coin being tossed every day? (coin re-flip question)

Advisor asked: if on day 1 Team B fails to acquire an incident, do we try again on day 2? day 50?
**Answer: Yes** — the same acquisition probability is applied each day the incident is in the system.
This is intentional: teams have repeated opportunities to process an incident until they succeed
or the signal decays.

**To address in paper:** Be explicit that each stage is re-attempted each timestep, not one-shot.

---

### C. Knowledge propagation cascade: A → B → C

Advisor raised: in NEIGHBOR strategy, can C acquire knowledge from A if B never acquired it?
Key question: does B need to acquire/process knowledge before C can get it from B?

**Current model behavior:** Knowledge is stored on each team as a vector. If B acquires from A,
B now holds that knowledge and C can later learn from B. If B never acquires, C cannot get it
through B — C can only learn from A directly if A is in C's neighborhood.

**This IS a cascade:** knowledge must propagate hop by hop through the network. B is the
intermediary; if B doesn't acquire, the chain from A to C via B is broken.

**Implication for writing:** Make this explicit in the methodology. The hop-by-hop cascade
is why signal decay at each hop matters, and why denser networks (lower average path length)
perform better.

---

### D. Relevance filtering — teams can "say no" to transformation

Advisor raised: a frontend team might deliberately not transform backend incident knowledge.
Domain irrelevance = intentional non-adoption (not failure to acquire, but a deliberate skip
of transformation).

**Current model:** Transformation is gated by cosine similarity between incident and team's
knowledge vector. Low similarity → low transformation probability. This implicitly models
relevance filtering — dissimilar knowledge is less likely to be transformed.

**To address in paper:** Frame cosine similarity as the relevance filter. When similarity is low,
the team "says no" — not because they failed, but because the knowledge doesn't apply to them.

---

### E. Per-stage developer hours tracking (model enhancement)

Advisor wants to record: Aq. Time / Ass. Time / Trans. Time / Exploit Time per team per incident.
Goal: show where effort was invested and whether it yielded returns.

**Current model:** Only total learning cost tracked (exp13).
**Needed enhancement:** Instrument each stage to accumulate hours, record stage where pipeline
stopped for each incident-team pair.

**Why it matters:** Can show that teams spending time acquiring but not exploiting are
"wasting" effort — the no-gain/effort problem. Can find optimal balance between acquisition
and exploitation investment.

**Action: Add per-stage hour tracking to model.py**

---

### F. Severity affects acquisition probability

Advisor raised: should the probability of acquiring knowledge decay based on incident severity?
High-severity incidents are more salient — teams pay more attention, more likely to acquire.

**Current model:** Acquisition probability is fixed per scenario. Severity affects incident
impact (duration, MTTD) but not the learning pipeline entry probability.

**Potential enhancement:** acquisition_prob = base_prob × severity_weight
- High severity → guaranteed acquisition (severity=1.0 → p=1.0)
- Low severity → lower attention → lower acquisition probability

**Action: Discuss with advisor whether to implement or treat as future work.**

---

### G. Paper: walk through a concrete example

Advisor explicitly requested: a worked example showing a simple team network, a specific incident,
and tracing it through all 4 stages with real numbers.

**Example structure:**
- 3-team network: Team A (owns DATABASE), Team B (neighbor), Team C (neighbor of B)
- Day 1: DATABASE incident occurs on Team A
- Trace: acquisition attempt (p=0.9), assimilation (p=0.7), transformation (p=0.6, cosine sim), exploitation (p=0.6)
- Show what changes in Team B's knowledge vector
- Show what C can and cannot acquire (cascade point)

**Action: Write this example for methodology section.**
