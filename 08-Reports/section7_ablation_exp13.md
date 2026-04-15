# Section 7: Ablation — exp13 Learning Cost

## 7.1 The Central Question

Fewer incidents are good. But incidents are not the only cost an engineering organization bears. Every postmortem review, every retrospective, every knowledge integration session consumes engineering time — time that could have been spent building features, paying down technical debt, or responding to customer needs. If global sharing dramatically increases the number of learning events, and each learning event has a real time cost, could the overhead of learning *outweigh* the benefit of fewer failures?

exp13 asks the question directly: **does global knowledge sharing reduce total engineering cost, or does the learning overhead it generates cancel out the firefighting hours it saves?**

---

## 7.2 A Real-World Analogy: The Postmortem Burden

Consider a mid-sized software company after a major production incident. The on-call engineer who was paged at 3 a.m. spent four hours restoring service. That cost is obvious and unavoidable — it happened, it was paid.

What is less obvious is the cost of what comes next. If the company runs a thorough postmortem, ten engineers may spend an hour each reading the write-up. A retrospective may consume another hour for six team leads. An on-call rotation update may take two hours of a senior engineer's time. Across a twenty-team organization where every team reviews every incident, a single outage could generate more learning overhead than the outage itself consumed in firefighting.

Now multiply that across a year with hundreds of incidents. A skeptical VP of Engineering, looking at the learning investment required to sustain a global sharing culture, might reasonably ask: "Are we spending more time *reading about* incidents than *fixing* them? Is this worth it?"

exp13 is the simulation's answer to that question.

---

## 7.3 Two Buckets of Cost

The simulation tracks engineering time in two distinct categories. It is important to understand both before interpreting the results.

**Cost Type 1 — Incident Response Cost (firefighting)**

When a production system fails, engineers drop what they are doing and restore it. This cost is incurred regardless of what learning scenario the organization operates under. Even NONE — which never learns anything — still pays this cost every time an incident occurs. The formula is:

> `engineering_cost_base (4 hrs) × severity_scale × duration_scale`

More incidents means more firefighting hours. An organization that experiences 484 incidents in a year spends substantially more time firefighting than one that experiences 265. The severity and duration multipliers mean that major, long-running incidents cost disproportionately more than minor ones.

**Cost Type 2 — Learning Cost (investment)**

When teams move through the four-stage knowledge pipeline — reading postmortems, attending retrospectives, updating runbooks, implementing preventive fixes — they spend time that is tracked separately as a learning investment. The model assigns:

> `learning_cost = 2.0 hours per successful learning event`

More teams learning from more incidents generates more learning events and, therefore, more learning hours. GLOBAL, where all 20 teams process every incident, accumulates the highest learning cost. NONE accumulates zero.

**Why they pull in opposite directions**

More sharing produces more learning events, which *increases* learning cost — but also produces more knowledge capital, which *decreases* future incidents and, therefore, future firefighting cost. These two effects work against each other throughout the 365-day simulation. The question is which effect dominates by year end.

---

## 7.4 How the Cost Dynamics Evolve Over Time

The opposition between the two cost types is not static. It shifts across the simulation year in a way that makes GLOBAL's economics increasingly favorable over time.

In the early months, GLOBAL is genuinely expensive. Consider a hypothetical Month 1: the organization experiences 40 incidents, generating 160 hours of firefighting cost (40 × 4 hrs), while all 20 teams process each incident, generating a large learning overhead. Total early-month cost under GLOBAL is high — the knowledge investment has been made, but the benefit in avoided incidents has not yet materialized.

By Month 6, the picture has changed substantially. Under GLOBAL, Prevention K reaches near-saturation (K=0.992) by approximately day 90. With knowledge capital at its ceiling, incident rates have dropped sharply — perhaps only 15 incidents that month, generating 60 hours of firefighting. Critically, *fewer incidents also means fewer learning events*, so learning overhead shrinks as well. Both cost buckets are smaller simultaneously.

By year end, the arithmetic is decisive: the learning investment was concentrated in the first 90 days, while the avoided firefighting benefit accumulates across the remaining 275 days of the simulation year. Prevention knowledge does not expire once K saturates — it continues suppressing incidents without generating new learning overhead.

This is the core insight the time-series structure of exp13 makes visible: the learning cost is front-loaded; the prevention benefit is persistent.

---

## 7.5 Experimental Setup

exp13 uses the same foundational configuration as H1: **20 teams**, a **Watts-Strogatz small-world network** topology, **365 simulated days**, and **100 independent random seeds**. All four learning scenarios (NONE, LOCAL, NEIGHBOR, GLOBAL) were run in parallel with complete cost tracking enabled.

Two cost tracking outputs were recorded at each time step: cumulative firefighting hours (driven by incident count and severity) and cumulative learning hours (driven by learning event count). These were summed at simulation end to produce the total engineering cost per scenario.

To confirm that the cost accounting layer does not interfere with the learning mechanics, the experiments were also run with `learning_cost=0.0` — a configuration in which learning hours are not charged. This serves as a model integrity check: if incident counts differ between the standard and zero-cost runs, it would indicate that cost tracking has inadvertently created a feedback loop into the learning process, contaminating the measurement. If incident counts are identical, cost tracking is confirmed as a pure accounting layer.

---

## 7.6 Results

| Scenario | Incidents | Firefighting Hrs | Learning Hrs | Total Hrs |
|----------|-----------|-----------------|--------------|-----------|
| **NONE** | 484 | 1,970 | 0 | 1,970 |
| **LOCAL** | 406 | 1,377 | ~400 | ~1,777 |
| **NEIGHBOR** | 336 | 959 | ~500 | ~1,459 |
| **GLOBAL** | 265 | 609 | ~580 | ~1,189 |

The ordering is unambiguous: total engineering cost decreases monotonically as knowledge sharing broadens, despite learning cost increasing monotonically in the same direction.

**NONE** never learns and never pays learning overhead. It pays 1,970 hours in pure firefighting — the heaviest total cost of any scenario. Without any knowledge accumulation, incident rates remain elevated for the full 365 days. The absence of learning investment does not save money; it merely converts learning cost into an even larger firefighting bill.

**LOCAL** reduces incidents by 78 (relative to NONE), saving approximately 593 firefighting hours. It spends roughly 400 hours in learning overhead. The net savings relative to NONE are approximately **193 hours** — positive, but modest, because local-only learning limits knowledge dissemination to single teams and does not cross organizational boundaries.

**NEIGHBOR** extends knowledge to adjacent teams and makes a substantially larger dent. It saves approximately 1,011 firefighting hours relative to NONE while spending roughly 500 learning hours. Net savings relative to NONE are approximately **511 hours**. The wider knowledge reach pays for the higher learning overhead with room to spare.

**GLOBAL** presents the most striking accounting. It spends the most on learning — approximately 580 hours across 100 seeds — but saves 1,361 firefighting hours relative to NONE (1,970 − 609). Net savings relative to NONE are approximately **781 hours**, the largest of any scenario despite the highest learning investment.

---

## 7.7 The Return on Investment Calculation

The economics of GLOBAL can be stated as a straightforward return on investment:

- **Learning investment:** ~580 engineering hours
- **Firefighting savings (vs. NONE):** ~1,361 engineering hours
- **Net gain:** ~781 engineering hours per year, per 20-team organization
- **ROI:** **2.3× return on every hour invested in learning**

For organizations tracking engineering labor costs, the business case is direct. At a fully-loaded engineering rate of $150 per hour — conservative for most software organizations — 781 hours of recovered capacity represents approximately **$117,150 in engineering value recovered annually** per 20-team organization. This gain does not require hiring, does not require tooling changes, and does not require architectural redesign. It requires only that incident knowledge be shared organization-wide rather than siloed within the team that experienced the failure.

---

## 7.8 Why GLOBAL Has the Highest Learning Cost but the Lowest Total Cost

The intuition that "more learning = more cost" is correct in isolation but misleading in context. GLOBAL does generate the most learning events and the highest learning overhead. What changes the arithmetic is the *persistence* of prevention knowledge relative to the *duration* of the simulation.

Once Prevention K reaches 0.992 (approximately day 90 under GLOBAL), the organization is operating near its knowledge ceiling. New incidents become rare. Rare incidents generate few new learning events. Learning overhead drops sharply in the second half of the year — but the accumulated knowledge capital continues suppressing failures for the remaining 275 days. The prevention benefit is durable; the learning cost is not.

NONE, by contrast, pays its firefighting cost uniformly across all 365 days. There is no acceleration, no saturation, and no improvement. The cost curve is flat and high throughout the year.

GLOBAL's total cost trajectory crosses below NONE's early in the simulation and continues declining. NONE's trajectory never improves.

---

## 7.9 Model Integrity: Learning Cost as Pure Accounting

Running the simulation with `learning_cost=0.0` produced **identical incident counts** to the standard configuration. This confirms that the cost tracking layer is correctly isolated from the simulation's learning mechanics. Learning cost is a measurement instrument, not a feedback mechanism — it observes without distorting.

This is a necessary result for the experiment's validity. If incident counts had changed when cost tracking was disabled, it would indicate that the cost model was inadvertently influencing agent behavior, and the cost comparisons would be confounded with changes in the underlying incident dynamics. The clean replication under zero-cost conditions validates that the numbers in Section 7.6 reflect cost accounting applied to a stable simulation, not a simulation altered by cost accounting.

---

## 7.10 Conclusion

exp13 provides the clearest practitioner argument in the thesis. The objection it addresses — that global knowledge sharing might be prohibitively expensive in engineering overhead — is well-founded in intuition and wrong in the data.

Organizations that invest heavily in postmortem culture, cross-team retrospectives, and organization-wide knowledge sharing do spend more on learning. But they spend far less in total. The learning investment yields a 2.3× return in avoided firefighting, and the longer an organization operates under a global sharing regime, the more durable that return becomes as knowledge capital approaches saturation.

The converse is equally important: organizations that avoid learning investment to protect engineering bandwidth do not avoid the cost — they displace it into firefighting, where it accumulates across every incident for the full duration of the year without improvement. Choosing not to invest in postmortem culture is not a cost-saving strategy; it is a cost-shifting strategy that shifts cost to a more expensive bucket.

**The pay-now-or-pay-more-later structure is not an abstraction.** It is a measurable difference of 781 engineering hours per year in a 20-team organization, at a 2.3× penalty for organizations that choose to pay later.
