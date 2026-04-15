# Proposal Defense — Committee Presentation
**David Pineda | BYU Computer Science MS | March 27, 2026**

---

## SLIDE DECK

---

### Slide 1 — Title

**Title:** A Simulation Tool for Exploring Organizational Learning from Software Incidents
**Subtitle:** MS Thesis Proposal Defense — David Pineda, BYU Computer Science

**SAY:**
"Good morning — thank you for being here. My proposal is about building a simulation tool to study how software teams learn from incidents, and using it to compare knowledge-sharing strategies that organizations currently choose without much empirical guidance."

*~15 seconds*

---

### Slide 2 — The Problem

**Headline:** Software systems fail. The question is whether teams learn from those failures to prevent them from happening again.

**Bullets:**
- Should teams only learn from their own incidents?
- Should they share with neighboring teams?
- Should everyone learn from every incident?

**Bottom line:** We want to understand how knowledge-sharing strategies affect reliability — and these questions are hard to answer with real organizations.

**SAY:**
"Software systems fail. The real question is whether teams learn from those failures to prevent them from happening again. In modern distributed systems this matters even more — one team's outage can cascade to other services, but one team's lessons can also help other teams avoid the same problem. We want to understand how knowledge-sharing strategies affect reliability. Should teams only learn from their own incidents? Should they share with neighboring teams? Should everyone learn from every incident? These are the questions this work is trying to answer."

*~30 seconds*

---

### Slide 3 — Why This is Hard to Study

**Headline:** These questions are hard to answer with real organizations

**Bullets:**
- Researchers cannot randomly assign half a company to share knowledge globally while the other half shares nothing
- Then wait years to compare incident rates
- This work builds a general-purpose simulation platform to explore these questions

**Bottom line:** Unlike prior simulations built for single studies, our platform is designed for reuse — researchers configure organizational structures, incident types, and learning rules without modifying code (Harrison et al. 2007)

**SAY:**
"These questions are hard to answer with real organizations. Researchers cannot randomly assign half a company to share knowledge globally while the other half shares nothing, then wait years to compare incident rates. So this work builds a general-purpose simulation platform to explore these questions. And unlike prior organizational simulations that were built for a single study, our platform is designed for reuse — researchers can configure the organizational structure, the incident types, and the learning rules without modifying any code. That lets the research community study many questions about incident learning, not just the ones we anticipate."

*~30 seconds*

---

### Slide 4 — What This Work Addresses

**Headline:** This work combines concepts from organizational learning and software engineering in a novel way

| Organizational Learning | Software Engineering |
|---|---|
| Absorptive capacity — how organizations acquire, assimilate, and exploit external knowledge (Cohen & Levinthal 1990; Zahra & George 2002) | Incidents and postmortems (Lunney & Lueder 2016; Dogga et al. 2023) |
| Leaves "exploitation" abstract | Lacks theoretical frameworks for how learning improves reliability |

**Bold line (word-for-word from proposal):**
> This combination is what we address. We connect these fields by giving exploitation concrete meaning: a team exploits knowledge when it reduces incident rates, shortens detection time, or improves mitigation effectiveness. This operationalization lets us measure whether learning actually happened — something prior work could not do.

**SAY:**
"This work combines concepts from organizational learning and software engineering in a novel way. Organizational learning research has studied absorptive capacity — how organizations acquire, assimilate, and exploit external knowledge — but leaves 'exploitation' abstract. Software engineering research has studied incidents and postmortems, but lacks theoretical frameworks for how learning improves reliability. This combination is what we address. We connect these fields by giving exploitation concrete meaning: a team exploits knowledge when it reduces incident rates, shortens detection time, or improves mitigation effectiveness. That operationalization is what lets us measure whether learning actually happened — something prior work could not do."

*~45 seconds*

---

### Slide 5 — Goals and Contribution

**Headline:** What this thesis does

**Goals (word-for-word from proposal):**
- **Goal 1:** Build a configurable simulation platform that models teams learning from incidents through the four-stage absorptive capacity framework (acquisition, assimilation, transformation, exploitation).
- **Goal 2:** Use the platform to systematically compare four knowledge-sharing strategies (NONE, LOCAL, NEIGHBOR, GLOBAL) and measure their effects on incident rates, detection time, and mitigation effectiveness across varied organizational configurations.

**Contributions (word-for-word from proposal):**
- **A reusable simulation platform for studying incident learning.** The platform separates configuration from logic. Researchers can study different organizational structures, incident taxonomies, and learning strategies through configuration files. This enables systematic comparison of knowledge-sharing approaches that practitioners often choose based on experience rather than systematic evidence.
- **A concrete operationalization of absorptive capacity for incident learning.** We model exploitation as measurable improvements: teams learn to prevent incidents, detect them faster, and fix them more effectively. This bridges organizational learning theory and software engineering practice, giving researchers a testable model of how postmortem knowledge translates into reliability outcomes.

**SAY:**
"Two goals, two contributions. Goal 1 is building the platform — configurable, so researchers can set up different organizational structures and learning rules without modifying code. Goal 2 is using it: systematically comparing the four sharing strategies and measuring their effects on incident rates, detection time, and mitigation effectiveness. The two contributions follow directly from those goals. The platform itself — reusable, separating configuration from logic. And a concrete operationalization of absorptive capacity: we model exploitation as measurable improvements, teams learn to prevent incidents, detect them faster, and fix them more effectively. That bridge between theory and measurable outcome is the core of what this work adds."

*~45 seconds*

---

### Slide 6 — The Simulation Platform

**Headline:** An agent-based simulator where each agent is a software team that owns a subsystem

**Visual:**
```
[Team A]──[Team B]──[Team C]──[Team D]
  DB        PAY       AUTH      CACHE
```

**Bullets:**
- Teams connect through an organizational network — network governs how knowledge flows after incidents
- The sharing strategy determines which teams can learn from which incidents
- Simulation proceeds in discrete timesteps — one simulated day each
- Each timestep: incident generation, learning propagation, metric collection

**Bottom:** We use ABM because it naturally captures heterogeneous teams with local decision rules and network-mediated interactions — features difficult to represent in aggregate models

**SAY:**
"We propose an agent-based simulator to study how software organizations learn from incidents. Each agent represents a team that owns a subsystem within a larger distributed system. Teams connect through an organizational network that governs how knowledge flows after incidents occur. The sharing strategy determines which teams can learn from which incidents. We use agent-based modeling because it naturally captures heterogeneous teams with local decision rules, emergent system-wide behavior, and network-mediated interactions — features that are difficult to represent in aggregate models."

*~30 seconds*

---

### Slide 7 — The Four Knowledge-Sharing Strategies

**Headline:** We compare four knowledge-sharing strategies

| Strategy | Who learns from an incident? |
|---|---|
| NONE | Teams do not learn — baseline |
| LOCAL | Teams learn only from their own incidents |
| NEIGHBOR | Teams also learn from adjacent teams in the network |
| GLOBAL | All teams learn from every incident |

**Bottom:** These represent real choices practitioners currently make without empirical guidance.

**SAY:**
"We compare four knowledge-sharing strategies. NONE is the baseline — teams do not learn at all. LOCAL means teams learn only from their own incidents. NEIGHBOR means teams also learn from adjacent teams in their network. GLOBAL means all teams learn from every incident. These represent real choices that practitioners currently make without empirical guidance — and that is exactly the gap this work addresses."

*~30 seconds*

---

### Slide 8 — What "Learning" Means in the Model

**Headline:** Each team maintains a knowledge vector over incident types — three dimensions, ranging from 0 to 1

**Visual: 5×3 grid**
```
              PREVENT    DETECT    MITIGATE
DB_TIMEOUT      0.0       0.0        0.0
CONFIG_ERR      0.0       0.0        0.0
DEPENDENCY      0.0       0.0        0.0
CAPACITY        0.0       0.0        0.0
DEPLOYMENT      0.0       0.0        0.0
```
*0 = no knowledge → 1 = full competence*

**How each dimension affects reliability (from proposal):**
- **Prevention** → reduces incident probability
- **Detection** → reduces Mean Time to Detect (MTTD)
- **Mitigation** → reduces severity and recovery time

**Incident types follow Microsoft's ARTS taxonomy** (Dogga et al. 2023)

**SAY:**
"Each team maintains a knowledge vector over incident types, where each dimension — prevention, detection, mitigation — ranges from 0 to 1. The incident types follow Microsoft's ARTS taxonomy from Dogga et al.: database timeouts, configuration errors, dependency failures, capacity issues, deployment problems. Each subsystem has a vulnerability profile determining which incident types it is most susceptible to. When a team learns from an incident, the relevant cells increase, and that feeds directly back: prevention knowledge reduces the probability of that incident firing again, detection knowledge reduces time to detect, mitigation knowledge reduces severity and recovery time."

*~30 seconds*

---

### Slide 9 — The Four-Stage Learning Pipeline

**Headline:** Learning follows the absorptive capacity framework — when an incident occurs, teams progress through four stages

**Four boxes:**
```
[ACQUISITION] → [ASSIMILATION] → [TRANSFORMATION] → [EXPLOITATION]
The team becomes  The team          The team connects   The team implements
aware of the      understands the   new knowledge to    changes that affect
incident          root cause and    existing mental     reliability
                  context           models
```

**We operationalize exploitation — often left abstract — by tying it to three measurable outcomes:**
- Prevention reduces the probability of similar incidents
- Detection reduces Mean Time to Detect
- Mitigation reduces severity and recovery time

**SAY:**
"Learning follows the absorptive capacity framework. When an incident occurs, teams progress through four stages: acquisition — the team becomes aware of the incident; assimilation — the team understands the root cause and context; transformation — the team connects new knowledge to existing mental models; and exploitation — the team implements changes that affect reliability. We operationalize exploitation — which is often left abstract in organizational learning research — by tying it to three measurable reliability outcomes: prevention, faster detection, and more effective mitigation. That is what lets us measure whether learning actually happened. And importantly — these stages impose different burdens depending on whether a team lived through the incident or is learning from others. The source team's acquisition and assimilation are automatic. For everyone else, all four stages require real effort. That asymmetry is why cross-team learning is nontrivial."

*~45 seconds*

---

### Slide 10 — What the Platform Measures

**Headline:** By simulating different strategies and tracking outcomes over time, we can study which configurations improve reliability — and at what cost

**Outputs (from proposal):**
- **Incident count** — total incidents over the simulation period
- **Severity** — impact distribution
- **Duration** — time to resolution
- **Availability** — uptime percentage
- **Learning cost** — developer-hours invested in learning activities

**The ratio that matters:**
> Reliability improvement per developer-hour invested — across all four sharing strategies

**SAY:**
"By simulating different knowledge-sharing strategies and tracking these outcomes over time, we can systematically study which organizational configurations improve reliability — and at what cost in learning overhead. The outputs we track are incident count, severity, duration, availability, and the developer-hours spent on learning. The ratio of reliability improvement to learning cost across strategies is the primary outcome of interest. That is the question this platform is designed to answer."

*~30 seconds*

---

### Slide 11 — The Four Hypotheses

**Headline:** We frame evaluation as four testable hypotheses

| # | Hypothesis (word-for-word from proposal) |
|---|---|
| **H1** | Broader sharing reduces total incidents: GLOBAL < NEIGHBOR < LOCAL < NONE in mean incident count over 365 simulated days. Rejected if ordering does not hold in >80% of parameter configurations. |
| **H2** | Deployment rate increases incidents: doubling the deployment rate will increase incident count by at least 20%, holding learning parameters constant. |
| **H3** | Learning investment shows diminishing returns: the relationship between learning effectiveness parameters and reliability improvement will be sublinear, with marginal gains decreasing as effectiveness increases beyond moderate levels. |
| **H4** | Network density accelerates knowledge spread: complete networks will show faster knowledge accumulation than sparse networks, measured by mean team knowledge at simulation midpoint. |

**SAY:**
"We frame the evaluation as four testable hypotheses, and these are the exact words from the proposal. H1 is the central claim — broader sharing produces fewer incidents in a strict ordering, and we have a clear rejection criterion: if the ordering fails in more than 20 percent of configurations, H1 is rejected. H2 connects to real deployment conditions from Forsgren's Accelerate research. H3 asks whether there is a ceiling on learning investment — does more postmortem effort always pay off, or do returns flatten out? H4 is about network structure — does a more connected organization accumulate knowledge faster? All four are directly testable in the simulator."

*~45 seconds*

---

### Slide 12 — H1: Learning Strategy Comparison

**Headline:** Broader sharing reduces total incidents: GLOBAL < NEIGHBOR < LOCAL < NONE

**What it does:** 4 strategies × 20 teams × small-world network × 365 days × 100 seeds = 400 runs

**Expected output — bar chart:**
```
incidents
  ████  NONE
  ███   LOCAL
  ██    NEIGHBOR
  █     GLOBAL
```
*With 95% confidence intervals*

**SAY:**
"H1 is the central verification. We already expect broader sharing to produce fewer incidents — that is the theoretical prediction. What we are checking is whether the model we built actually reproduces that ordering. If it does not hold in more than 20 percent of configurations, that is a signal something is off in the model, not a surprise finding. This is the anchor — if H1 holds, we have confidence the rest of the platform is working as designed."

*~30 seconds*

---

### Slide 13 — H2: Deployment Rate

**Headline:** Deployment rate increases incidents: doubling the rate will increase incident count by at least 20%

**What it does:** Vary deployment rate across a range × fixed learning parameters × 100 seeds per level

**Expected output — bar/line chart:**
```
incident
count
    ↑                              ●
    |                         ●
    |                    ●
    |               ●
    |          ●
    └──────────────────────────────→ deployment rate
      1×      2×      3×      4×
```
*If incident count does not rise by ≥20% when deployment doubles, H2 is rejected*

**SAY:**
"H2 is another model behavior check. We know from Forsgren's Accelerate research that higher deployment frequency increases failure risk in real organizations. So we expect the model to reproduce that — doubling the deployment rate should increase incident count by at least 20%. If it does not, we investigate the incident generation mechanism. This is not a surprising finding, it is a verification that the model is sensitive to the right inputs."

*~30 seconds*

---

### Slide 14 — H3: Diminishing Returns

**Headline:** Learning investment shows diminishing returns — marginal gains decrease as effectiveness increases beyond moderate levels

**What it does:** Sweep learning effectiveness parameters across a range × 100 seeds per level

**Prediction:** Sublinear relationship — curve flattens at higher effectiveness

**Expected output — curve:**
```
reliability
improvement
    ↑    ●●
    |  ●●
    | ●●
    |●●
    |●
    └──────────────────────→ learning effectiveness
      low              high
```

**SAY:**
"H3 checks that the model produces diminishing returns on learning investment — a relationship we expect based on how absorptive capacity works in theory. If we increase learning effectiveness from weak to strong, the reliability improvement should be sublinear — early gains are large, later gains flatten out. If the model instead produces a linear or accelerating curve, that tells us something in the learning mechanism is not behaving correctly."

*~30 seconds*

---

### Slide 15 — H4: Network Density

**Headline:** Network density accelerates knowledge spread — complete networks will show faster knowledge accumulation than sparse networks

**What it does:** Compare dense vs sparse networks under NEIGHBOR scenario × 100 seeds

**Topologies compared:**
- Dense (complete or scale-free with hubs)
- Small-world (Watts-Strogatz)
- Sparse (random, low connectivity)

**Measure:** Mean team knowledge at simulation midpoint (day 182)

**SAY:**
"H4 checks that network structure affects learning speed the way we expect — denser networks should accumulate knowledge faster because incidents reach more teams through fewer hops. We measure mean team knowledge at the simulation midpoint. If a denser network does not show faster accumulation, we look at how knowledge is propagating through the model. Again — this is a behavior check. We already expect this relationship. If the model does not reproduce it, the propagation mechanism needs investigation."

*~30 seconds*

---

### Slide 16 — Robustness and Partial Validation

**Headline:** Results should hold across configurations — and outputs should fall within published ranges

**Robustness — we plan to vary (from proposal):**
- Team count: 6, 20, 50
- Network type: random, small-world, scale-free
- Deployment rate: low to high
- Learning effectiveness: weak to strong

**100+ simulations per configuration — report confidence intervals — note edge cases**

**Partial validation against published data (from proposal):**
- Simulated incident frequencies (10–50 per team per year) benchmarked against Dogga et al. (2023)
- Mean time to recovery (1–8 hours) benchmarked against Forsgren et al. (2018)

**From proposal:** "We acknowledge this constitutes weak validation and does not substitute for calibration against real organizational data. Stronger validation — such as calibration against proprietary incident logs — is beyond the scope of this thesis but represents a natural direction for future work."

**SAY:**
"Results should hold across different configurations — we plan to vary team count, network type, deployment rate, and learning effectiveness, running 100 or more simulations per configuration and reporting confidence intervals. We also seek partial validation by checking whether simulated outputs fall within published ranges: incident frequencies between 10 and 50 per team per year from Dogga et al., and mean time to recovery between 1 and 8 hours from Forsgren et al. We are explicit in the proposal that this is weak validation — it does not substitute for calibration against real organizational data, which is documented as future work."

*~30 seconds*

---

### Slide 17 — Timeline

**Headline:** Achievable because the platform is already built

| Date | Milestone |
|---|---|
| March 23–27 | Run all experiments |
| April 5 | Analysis complete — all figures and tables |
| April 12 | Implementation chapter draft |
| April 19 | Results chapter draft |
| May 10 | Background + Methodology written |
| May 20 | Full draft assembled |
| June 1 | Complete draft to advisor |
| June 14 | Revisions complete |
| Late June | **Thesis defense** |

**SAY:**
"The timeline is realistic because the platform is already built and pilot runs are working. The week of March 23 is dedicated entirely to running experiments at full scale. May is for independent writing while my advisor is traveling — so when he returns in June, a complete draft is ready for one review cycle before defense."

*~30 seconds*

---

### Slide 18 — Limitations

**Headline:** What this thesis does not claim

**Bullets (word-for-word from proposal):**
- **Synthetic data** — results show what the model predicts, not necessarily what would happen at a real company
- **Simplified model** — individual skill differences, office politics, and budget pressures are excluded for tractability
- **Exploratory, not predictive** — the platform helps explore "what if" questions; it does not predict exactly what will happen at your organization
- **Uncalibrated parameters** — stage transition probabilities and learning rates are expert estimates, not empirically calibrated values; sensitivity analysis identifies which assumptions most affect conclusions
- **Static network topology** — real organizations restructure over time; the model does not capture this
- **Untested learning model** — we adopt Cohen and Levinthal's absorptive capacity framework, developed for R&D contexts; whether software teams actually learn through these stages is an empirical question this work does not address; future work could validate through practitioner interviews or longitudinal case studies

**SAY:**
"I want to be direct about what this work does not do. The findings are directional — we cannot tell a specific company their incident rate will drop by X percent. The model is simplified for tractability, excluding individual skill differences, politics, and budget constraints. Parameters are expert estimates, not calibrated against real data. And importantly — whether software teams actually learn through absorptive capacity stages the way R&D teams do is an empirical question this work does not resolve. We adopt the framework as a theoretically grounded starting point. Practitioner interviews or longitudinal case studies would be the natural next step for validating that assumption."

*~30 seconds*

---

### Slide 19 — One Question for the Committee

**Headline (large, centered):**
> Do you see the core value proposition of this platform — and are there gaps in the scope that should be addressed before running at full scale this week?

**SAY:**
"I want to close by opening the floor. The platform is built and ready to run. My question for the committee is: does this scope — the platform, the four strategies, the four hypotheses, and the robustness testing — represent the right contribution for a master's thesis? If there are gaps or concerns about the framing, now is the time to address them before the full experiment run this week. That is why we are here."

*~30 seconds — stop and let the committee respond*

---

### Slide 20 — Thank You / Questions

**Title:** Questions

**SAY:**
"Thank you. I'm happy to go into more detail on any part of this — the theoretical grounding, the simulation design, the hypotheses, or the evaluation plan."

*Leave this slide up for Q&A*

---

## SPEAKING NOTES — Key Talking Points for Q&A

### If asked: "Why agent-based modeling specifically?"
"Agent-based modeling captures what matters here — heterogeneous teams with local decision rules, emergent organization-wide behavior from individual learning, and network-mediated interactions. Aggregate models like system dynamics flatten those distinctions. ABM keeps each team's knowledge state separate, which is what lets us measure whether learning actually transferred."

### If asked about specific formulas or stage probabilities
"The specific parameter values are expert-estimated defaults, not empirically calibrated numbers. The sensitivity analysis will identify which parameters most drive the results — if the conclusions change dramatically when we vary a parameter, that is a finding in itself. The exact coefficients are tunable, and I document them as such in the proposal."

### If asked: "How is this different from prior simulations?"
"Prior simulations in this space — like Nooteboom et al.'s R&D alliance model — were built for single studies and are not reusable. Our platform separates configuration from logic so researchers can vary organizational structure and learning rules without modifying code. That generality is one of the two stated contributions."

### If asked about knowledge decay
"In the current model, knowledge values are capped at 1.0 and do not decay. Decay is a natural extension — Darr et al. document measurable knowledge depreciation over time in service organizations — but it is scoped as future work to keep the current model tractable and the results interpretable."

### If asked about the proposal language vs. slides
"The goals and contributions on slide 5 and the hypotheses on slide 12 are word-for-word from the submitted proposal. I deliberately kept that language intact."

---
