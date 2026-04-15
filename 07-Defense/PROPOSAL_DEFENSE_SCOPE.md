# Thesis Scope & Timeline — Proposal Defense Document
**David Pineda | BYU Computer Science MS**
*Submitted to Committee: March 14, 2026*

---

## Contribution in Two Sentences

This thesis builds a simulation platform for studying how software teams learn from incidents,
and uses it to answer a question practitioners face daily: should your organization share incident
knowledge only with nearby teams, or broadcast it company-wide? The platform produces the first
controlled comparison of these strategies grounded in absorptive capacity theory, giving
engineering managers a structured framework for evaluating knowledge-sharing trade-offs rather
than relying on intuition alone.

---

## Scope: 7 Experiments

Preliminary implementation is complete and pilot runs confirm the simulation produces
directionally correct behavior. All experiments will be run during the week of March 23.

### Core Experiments

| # | Experiment | What It Asks | Why It Is Necessary |
|---|---|---|---|
| 1 | **Learning Strategy Comparison** | Does broader sharing reduce incidents? Do outcomes rank: GLOBAL < NEIGHBOR < LOCAL < NONE? | This is the central thesis finding. All other experiments build on it. |
| 2 | **Deployment Rate Sensitivity** | Does deploying software more frequently cause more incidents, and does learning mitigate this effect? | Connects the simulation to real DevOps practice; grounded in Forsgren et al. (2018). |
| 3 | **Organizational Conditions for Neighbor ≈ Global** | At what organization size and network connectivity does neighbor-based sharing stop being "good enough" (capturing ≥80% of company-wide sharing's benefit)? | This is the novel, actionable finding. It tells a manager: if your org is under X teams with Y connectivity, you do not need costly company-wide broadcasts. |
| 4 | **Robustness Sweep** | Does the H1 ordering hold across 6, 20, and 50 teams, and across random, small-world, and scale-free networks? | Prevents the finding from being dismissed as specific to one org size or structure. |

### Validation Experiments (Model Verification)

These are not additional findings. They are required verification steps under Sargent's (2020)
simulation validation framework — confirming each model component contributes meaningfully before
trusting the core results.

| # | Ablation | What It Asks |
|---|---|---|
| 5 | **No Knowledge Decay** | If teams never forget what they learned, does reliability improve uniformly? Confirms decay is a meaningful model component. |
| 6 | **No Source-Team Advantage** | If the team that experienced an incident has no learning advantage over others, do outcomes change? Confirms the asymmetry assumption matters. |
| 7 | **No Learning Cost** | If knowledge sharing were free, does the optimal strategy change? Confirms cost structure affects strategy choice. |

---

## What This Thesis Does Not Do

To keep scope achievable for a master's thesis, the following are explicitly out of scope:

- Calibration against proprietary incident logs (requires data access beyond thesis scope)
- Modeling individual skill differences, office politics, or budget constraints
- Dynamic network topology (real org restructuring over time)
- Predictive claims about specific organizations — findings are directional, not prescriptive

These are documented in the proposal's Limitations section and scoped as future work.

---

## Milestones & Timeline

| Date | Milestone | Deliverable |
|---|---|---|
| **March 14** | Send proposal + this document to committee | Committee reads before defense meeting |
| **March 17** | Code freeze | No new features; simulation ready to run |
| **March 18–21** | **Proposal defense meeting** | Committee approves scope and timeline |
| **March 23–27** | Run all 7 experiments | 100 simulations per configuration, 95% confidence intervals |
| **April 5** | Analysis complete | All figures and tables; one-page results summary to advisor |
| **April 12** | Implementation chapter draft | ~2–3 pages: platform architecture, key decisions, reproducibility |
| **April 19** | Results chapter draft | ~4–6 pages: H1–H3 findings, robustness, ablations |
| **April 25** | **Commencement — walk the stage** | Thesis in progress; two chapters drafted, full data in hand |
| **May 10** | Background + Methodology written | ~8–10 pages written independently while advisor is away |
| **May 20** | Introduction + Discussion + Conclusion | Full draft assembled |
| **June 1** | Complete draft to advisor | Advisor returns; reviews once |
| **June 14** | Revisions complete | All committee feedback addressed |
| **Late June** | **Thesis defense** | |
| **Late June** | Final submission | Buffer for formatting and any last fixes |

---

## Why This Timeline Is Achievable

- The simulation platform is already built and producing correct results
- All 7 experiments are implemented and verified with pilot runs
- The week of March 23 is dedicated entirely to running experiments at full scale
- May is reserved for independent writing — no advisor meetings needed during this period
- The advisor returns in June with a complete draft waiting — one review cycle before defense

---

## One Thing I Am Asking the Committee to Confirm

> **Is the scope above — four core experiments plus three ablation checks — the right level of
> depth for a master's thesis in this area?**

If the committee has concerns about any specific experiment being unnecessary or any gap that
should be filled, I want to hear that at the proposal defense so I can adjust before running
full-scale experiments the week of March 23.
