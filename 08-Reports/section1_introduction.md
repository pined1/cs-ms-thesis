# Section 1: Introduction & Study Overview

---

## 1.1 The Central Problem

Software systems fail. Servers go down, databases become unavailable, deployments break production — these events are a routine reality for any organization running software at scale. What separates high-reliability organizations from struggling ones is not whether they have incidents, but what they *do with them afterward*.

Most engineering organizations hold postmortems: structured retrospectives where teams document what went wrong, why it went wrong, and what they will change to prevent recurrence. This practice is well-established. What is far less understood is a more subtle organizational question: **does it matter how widely that postmortem knowledge gets shared?**

If Team A experiences a database failure and writes a detailed postmortem, should only Team A read it? Should Team A's direct neighbors in the organization also receive it? Should the entire company? Intuitively, broader sharing seems better — but organizations pay real costs for broad sharing: meeting time, cognitive load, alert fatigue, and the risk of overwhelming teams with incidents that feel irrelevant to them. The tradeoff is real, and no rigorous simulation study has examined how different sharing policies actually affect organizational reliability outcomes. This thesis addresses that gap directly.

---

## 1.2 Why This Question Matters

Every major technology company invests heavily in postmortem culture. Google's Site Reliability Engineering handbook dedicates entire chapters to blameless postmortems. Netflix's chaos engineering discipline is built on the idea that learning from failures — whether real or simulated — is the path to resilience. Amazon's operational reviews treat incident retrospectives as first-class engineering artifacts.

Despite this industry-wide investment, the literature on *how sharing scope affects reliability outcomes* remains thin. Organizational learning theory (Levitt & March 1988; Argote 1999) tells us that knowledge must flow through an organization to be useful. Absorptive capacity theory (Cohen & Levinthal 1990; Zahra & George 2002) tells us that receiving knowledge is not enough — teams must have the capacity to absorb and apply it. But neither body of theory has been tested in the specific context of software incident knowledge sharing with a formal computational model.

This simulation study provides that test.

---

## 1.3 What We Built: The Agent-Based Model

Think of the model as a digital organization running inside a computer. Twenty software engineering teams are arranged in a social network — some teams are adjacent (they work on related systems or share a product area), some are distant. Each team owns a portfolio of software subsystems, and those subsystems generate incidents over time according to a stochastic process.

**A concrete analogy:** Imagine a technology company with 20 engineering teams. Each team owns a set of software services, and those services experience outages. After each outage, the team writes a postmortem. The question is: should the postmortem findings stay within that team, be shared with the adjacent teams who depend on the same platform, or be broadcast across the entire engineering organization? Our model simulates exactly this decision, run 100 times over a simulated year, under four different sharing policies.

The simulation was implemented as an agent-based model (ABM) — a computational approach where individual agents (teams) follow local rules and their aggregate behavior produces emergent organizational outcomes. ABMs are well-suited to this problem because organizational reliability is inherently an emergent property: no single policy decision produces reliability; it arises from thousands of small learning events accumulated across many teams over time.

**Model parameters at a glance:**

| Parameter | Value |
|---|---|
| Number of teams | 20 |
| Simulation duration | 365 days |
| Independent runs per condition | 100 (seeds 0–99) |
| Learning conditions | 4 (NONE, LOCAL, NEIGHBOR, GLOBAL) |
| Total simulation runs | 400 |
| Incident generation | Stochastic (Poisson process per subsystem) |

---

## 1.4 The 4-Stage Absorptive Capacity Pipeline

The theoretical backbone of the learning model is Zahra & George's (2002) reformulation of absorptive capacity, which describes how organizations acquire, process, and use external knowledge. Rather than treating "learning" as a single binary event, the model implements a four-stage pipeline through which incident knowledge must pass before it changes a team's behavior.

### The Four Stages

**Stage 1 — Acquisition:** Does the team receive the incident knowledge? A team that is not in the sharing scope for an incident never even sees the postmortem. Teams within scope receive the knowledge with a probability that reflects their current attention capacity.

**Stage 2 — Assimilation:** Does the team understand the knowledge? Even when a team receives a postmortem, they may not fully grasp its implications for their own systems. Assimilation probability is influenced by the team's existing knowledge base — teams that have seen similar incidents before assimilate new ones more readily.

**Stage 3 — Transformation:** Does the team connect the new knowledge to what they already know? Transformation is the cognitive work of integration: recognizing that a failure mode in a neighboring team's database layer is relevant to a similar pattern in one's own caching layer. This stage has the highest failure rate in the model, reflecting real-world evidence that cross-domain knowledge transfer is difficult.

**Stage 4 — Exploitation:** Does the team change its behavior to reduce future incident probability? This is the only stage that produces a measurable reliability outcome. A team that fully exploits an incident's lessons lowers the base incident rate for the relevant subsystems.

### A Worked Example

*Team A experiences a database connection pool exhaustion failure on simulation day 47. The incident is logged and a postmortem is generated.*

- **Stage 1 (Acquisition):** Under the NEIGHBOR condition, Team B — an adjacent team in the network — receives the postmortem. Team C, which is not adjacent, never sees it.
- **Stage 2 (Assimilation):** Team B reads the postmortem. Because Team B operates a similar database layer, they have relevant prior knowledge and assimilate the findings with high probability.
- **Stage 3 (Transformation):** Team B's engineers connect the connection pool failure to a latent risk in their own query timeout configuration — a non-obvious but important link. This transformation step succeeds.
- **Stage 4 (Exploitation):** Team B updates their connection pool limits and adds a monitoring alert. Their base incident rate for database-related failures decreases by a model-specified exploitation factor.

If the simulation is running under the LOCAL condition, only Team A traverses this pipeline. Under GLOBAL, all 19 other teams traverse it — each with their own assimilation and transformation probabilities.

---

## 1.5 The Four Sharing Conditions

The experiment manipulates a single organizational policy variable: the **scope of incident knowledge sharing**.

| Condition | Who Learns From Each Incident |
|---|---|
| **NONE** | No team learns; incidents are logged but postmortems are ignored |
| **LOCAL** | Only the team that experienced the incident learns from it |
| **NEIGHBOR** | The owning team plus all direct network neighbors learn |
| **GLOBAL** | Every team in the organization learns from every incident |

These four conditions represent a spectrum from zero organizational learning (NONE) to maximum diffusion (GLOBAL), with two intermediate cases that reflect common real-world policies.

---

## 1.6 The Four Hypotheses

The study tests four pre-registered hypotheses derived from organizational learning theory:

- **H1 (Sharing Scope):** Broader sharing scope produces fewer cumulative incidents. The expected ordering is NONE > LOCAL > NEIGHBOR > GLOBAL in total incident count.
- **H2 (Deployment Velocity):** Higher deployment frequency increases incident rates, as faster change introduces more opportunities for failure.
- **H3 (Diminishing Returns):** The marginal benefit of exploitation effectiveness decreases as effectiveness increases; early gains are large, later gains are small.
- **H4 (Network Density):** Denser organizational networks — where more teams are adjacent to one another — produce faster knowledge accumulation and lower incident rates.

---

## 1.7 Preview of Key Findings

The simulation results are unambiguous. **Global knowledge sharing reduces cumulative incidents by approximately 45% compared to no sharing**, a difference that is both statistically significant and practically enormous. The effect size for the sharing condition comparison is Cohen's *d* = 11.5 — far exceeding conventional thresholds for "large" effects (d > 0.8). This finding replicates across all 100 random seeds and survives every robustness check applied, including parameter sensitivity analysis and network topology variation.

All four hypotheses received support from the data. The sections that follow present the full experimental results, statistical analyses, and robustness evaluations in detail.

---

*Sections 2 through 5 present the quantitative results for each hypothesis in turn. Section 6 addresses robustness and sensitivity. Section 7 discusses implications for organizational practice.*
