# The Four-Stage Learning Pipeline
**David Pineda | BYU Computer Science MS | Proposal Defense**

*Slide section: How Knowledge Moves Through the Model*

---

## Grounding: Zahra & George (2002) — Absorptive Capacity

Knowledge transfer between teams is not a single event.
It is a four-stage process, each with its own probability of succeeding.
A team must clear every gate — in order — before knowledge changes their behavior.

> **If any stage fails, the knowledge stops there. The next incident starts fresh.**

---

## The Four Stages at a Glance

Each stage answers one question about whether knowledge actually traveled.

| Stage | Question |
|---|---|
| **Acquisition** | Did you hear about the incident? |
| **Assimilation** | Did you understand it deeply enough to internalize it? |
| **Transformation** | Did you recombine it with what you already know? |
| **Exploitation** | Did you actually change your practices? |

---

## Stage 1 — Acquisition

> *Did you hear about the incident?*

```
p = [channel quality] × [org friction]
  = edge_weight × acquisition_probability
  = 0.75 × 0.9 = 0.675
```

**What each factor means:**

- **Channel quality** — edge weight between teams, sampled Uniform(0.5, 1.0) at simulation start.
  Represents how strong the communication channel is: shared Slack, regular syncs, org proximity.
  A weight of 0.5 is a weak channel; 1.0 is a perfect channel.

- **Org friction** — fixed at 0.9. Even with a perfect channel, some incidents just don't get communicated.
  Announcements get missed. Postmortems go unread. 90% is already optimistic.

- **No relevance factor.** You either hear about an incident or you don't — content doesn't determine broadcast.

---

## Stage 2 — Assimilation

> *Did you understand it deeply enough to internalize it?*

```
p = [how capable] × [org friction] × [how relevant]
  = (0.7 × cognitive_factor + 0.3 × doc_quality) × 0.7 × (0.5 + 0.5 × relevance)
```

**What each factor means:**

- **How capable** — weighted mix of two inputs:
  - `cognitive_factor` (70% weight): inverted-U on cosine similarity between teams' knowledge vectors.
    Peaks at similarity = 0.5 — teams need enough shared context to understand, but enough difference to learn something new.
    Collapses toward zero if teams are too similar (nothing new) or too different (incomprehensible).
  - `doc_quality` (30% weight): how clear and complete the postmortem is. Fixed at 0.5 by default.
    Grounded in Cohen & Levinthal (1990): cognitive proximity dominates over documentation quality.

- **Org friction** — fixed ceiling of 0.7. Even a perfectly capable team in a perfect org only assimilates 70% of the time.
  Organizations are messy. Understanding is hard.

- **How relevant** — slider from 0.5 to 0.95:
  - Floor of 0.5: every incident teaches general lessons (postmortem process, incident response, alerting).
  - Ceiling of 0.95: incident type maps directly to your subsystem's susceptibility.
  - Formula: `0.5 + 0.5 × relevance`. Never drops below 50% transfer.

---

## Stage 3 — Transformation

> *Did you recombine it with what you already know?*

```
p = [how capable, cognition-heavy] × [org friction] × [how relevant]
  = (0.8 × cognitive_factor + 0.2 × doc_quality) × 0.7 × (0.5 + 0.5 × relevance)
```

**What each factor means:**

- **How capable** — same inputs as Stage 2, but the weights shift:
  - `cognitive_factor` rises to 80% weight.
  - `doc_quality` drops to 20% weight.
  - Reason: transformation is a mental act, not a reading act. You are synthesizing the new knowledge
    with your existing mental model — connecting it to past incidents, existing runbooks, known failure modes.
    At this stage, what you already know matters far more than what the doc says.

- **Org friction** — same fixed 0.7 ceiling as assimilation.
  Synthesis is as hard as understanding. Neither step gets easier just because the prior step succeeded.

- **How relevant** — identical relevance slider as Stage 2.

---

## Stage 4 — Exploitation

> *Did you actually change your practices?*

```
p = [org friction] × [how relevant]
  = exploitation_probability × (0.5 + 0.5 × susceptibility)
  = 0.6 × (0.5 + 0.5 × susceptibility)
```

**What each factor means:**

- **No cognitive factor.** By Stage 4, the team already understands and has synthesized the knowledge.
  The remaining question is purely operational: is this incident type worth acting on for your subsystem?

- **Org friction** — lowest cap of all four stages: 0.6.
  This is the hardest organizational step. Understanding something is not the same as changing behavior.
  Updating runbooks, deploying new monitoring, changing deployment gates — these take time and priority.
  Even when teams are ready, only 60% follow through.

- **How relevant** — uses raw subsystem susceptibility directly (not the `calculate_relevance` function).
  A DATABASE team exploiting a DATABASE_TIMEOUT incident has high susceptibility → high exploitation probability.
  A FRONTEND team exploiting the same incident has low susceptibility → exploitation probability approaches the floor.

**When exploitation succeeds, knowledge enters the vector:**
```
knowledge_gained = learnable[dim] × (0.5 + 0.5 × susceptibility) × (0.5 + 0.5 × doc_quality)
```
The amount of knowledge gained is also scaled — high-relevance, well-documented incidents teach more.

---

## Summary — Friction Caps Across Stages

The declining caps encode a core assumption: **behavioral change is harder than cognitive change.**

| Stage | Friction Cap | Interpretation |
|---|---|---|
| Acquisition | 0.9 | Teams usually hear about incidents |
| Assimilation | 0.7 | Deep understanding is hard |
| Transformation | 0.7 | Synthesis is equally hard |
| Exploitation | 0.6 | Actually changing behavior is hardest |

Multiply all four stages together under ideal conditions:
```
0.9 × 0.7 × 0.7 × 0.6 = 0.265
```
Even in a best-case scenario — strong channel, perfectly similar teams, perfectly relevant incident —
**only ~26% of knowledge transfer events result in a behavioral change.**

This is the absorptive capacity bottleneck the thesis is studying.

---

## What the Learning Scenario Controls

The scenario (NONE / LOCAL / NEIGHBOR / GLOBAL) determines **who is eligible to enter Stage 1**.
Once eligible, all four stages apply equally to every team.

| Scenario | Who enters the pipeline? |
|---|---|
| NONE | Nobody (no learning at all) |
| LOCAL | Source team only (direct experience, bypasses pipeline via asymmetry) |
| NEIGHBOR | Source team + direct network neighbors |
| GLOBAL | All teams in the organization |

The source team (the one that experienced the incident) always **bypasses the pipeline** — direct experience
skips acquisition, assimilation, and transformation and goes straight to exploitation. This is the
source-team asymmetry assumption: a team that lived through an incident learns more directly than one
that read about it secondhand (Zahra & George 2002; Argote et al. 2021).

---

*Speaker note: This slide sequence runs approximately 3–4 minutes of the 15-minute proposal presentation.
Follow with Experiment 1 results to show what happens when you vary who enters Stage 1.*
