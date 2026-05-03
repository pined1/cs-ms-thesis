# MS Thesis: Organizational Learning from Software Incidents

**David Pineda | BYU Computer Science MS**
**Advisor: Jonathan Lunt**

> Does sharing incident knowledge more broadly reduce software system failures? This thesis uses an agent-based simulation to study how sharing scope, network topology, deployment velocity, and learning effectiveness interact to determine organizational reliability.

---

## Project Structure

```
CS MS/
├── 01-Papers/              # Paper notes (36 papers, all read)
├── 02-Framework-Code/      # Python ABM simulator + experiments
├── 03-Experiments/         # Experiment documentation and results summaries
├── 06-Thesis-Proposal/     # Four-pager committee proposal (LaTeX + PDF)
├── 07-Defense/             # Defense presentation and committee feedback
├── 08-Reports/             # index.html north star report + chapter outlines
└── 09-Chapters/            # Chapter drafts (Chapter 3 sections complete)
```

---

## The Model

20 software engineering teams arranged in a social network. Each team owns a subsystem that generates incidents stochastically. When an incident occurs, a postmortem is written. The simulation tests four strategies for who reads it.

### Four Sharing Scenarios

| Scenario | Who learns from each incident |
|---|---|
| **NONE** | Nobody — baseline floor |
| **LOCAL** | Only the team that experienced it |
| **NEIGHBOR** | Source team + all direct network neighbors |
| **GLOBAL** | Every team in the organization |

### Four-Stage Absorptive Capacity Pipeline (Zahra & George 2002)

| Stage | Question | Gate |
|---|---|---|
| 1. Acquisition | Does the team see the postmortem? | `P_acquire × signal_decay^hops` |
| 2. Assimilation | Does the team understand it? | `P_assimilate = 0.70` |
| 3. Transformation | Does the team connect it to their own systems? | Cosine similarity threshold |
| 4. Exploitation | Does the team change behavior? | `P_exploit = 0.60` |

### Four Hypotheses

| | Hypothesis | Result |
|---|---|---|
| **H1** | Broader sharing → fewer incidents (GLOBAL > NEIGHBOR > LOCAL > NONE) | ✅ Confirmed — 45% reduction, Cohen's d = 11.51 |
| **H2** | Higher deployment rate → more incidents | ✅ Confirmed — but sublinear under GLOBAL (10× deploy = only 24% more incidents) |
| **H3** | Higher exploitation effectiveness → fewer incidents, diminishing returns | ✅ Confirmed — ~4% at realistic values vs. 45% for H1 |
| **H4** | Denser network topology → fewer incidents | ✅ Confirmed — topology alone accounts for 40% variance |

---

## Key Results

- **GLOBAL vs. NONE:** 45% fewer incidents, Cohen's d = 11.51 (p < 0.001)
- **Topology range:** Complete (273) → Star (382) — 40% difference, identical agents
- **H1 ordering holds** across all 13 experiments, 6 sensitivity sweeps, 2 ablation tests
- **Stage 3 (Transformation) is the bottleneck**, not Stage 4 (Exploitation)

---

## Quick Start

```bash
# Run tests
cd 02-Framework-Code && make test

# Run H1 experiment
cd 02-Framework-Code && python3 run_experiments.py

# Run sensitivity sweeps
cd 02-Framework-Code && python3 sensitivity_sweep.py

# Run publication-level validation tests
cd 02-Framework-Code && python3 publication_tests.py
```

---

## Bibliography (36 papers, all read)

### Absorptive Capacity & Organizational Learning (7)

| # | Paper | One-Line Takeaway |
|---|---|---|
| 1 | Cohen & Levinthal (1990) | You can only absorb what you already partly know — prior knowledge gates everything |
| 2 | Zahra & George (2002) | The four-stage ACAP pipeline: acquisition → assimilation → transformation → exploitation |
| 3 | March (1991) | Competency trap + value of heterogeneity; borrowed selectively — sharing scopes are NOT mapped onto exploration vs. exploitation |
| 4 | Argote & Miron-Spektor (2011) | Create / retain / transfer — the broadest organizing framework for org learning |
| 5 | Nooteboom et al. (2007) | Absorptive capacity declines with cognitive distance — Stage 3 cosine-similarity gate; only the downward half of the inverted-U is modeled |
| 6 | Szulanski (1996) | Inter-unit transfer fails on cognitive barriers (causal ambiguity, absorptive capacity), not motivation — explains NEIGHBOR's 14% transformation, not LOCAL |
| 7 | Levinthal (1997) | Concave diminishing-returns curve from local adaptive search — borrowed only as the canonical shape for H3, not as a knowledge-accumulation model |

### Learning from Incidents (11)

| # | Paper | One-Line Takeaway |
|---|---|---|
| 8 | Cook (1998) | "Root cause" is a story we construct after the fact, not an objective property of failure |
| 9 | Leveson (2004) | STAMP — accidents emerge from inadequate control, not chains of component failures |
| 10 | Lunney & Lueder (2016) | Google's blameless postmortem culture: shift the question from "who?" to "why did the system allow this?" |
| 11 | Allspaw (2012) | Etsy's Just Culture — blamelessness as the operating condition for honest sharing |
| 12 | Dogga et al. (2023) | ARTS taxonomy from 2,000+ Azure incidents — used as the type system for synthetic incidents |
| 13 | Drupsteen & Guldenmund (2014) | Sharing-and-storing is the most underexposed sub-process in incident learning |
| 14 | Margaryan et al. (2017) | Research agenda for LFI; identifies simulation as underused but appropriate methodology |
| 15 | Reed (2019) | High performers use postmortems to patch mental models, not to generate fix lists (91% of Reed's interview sample miss this) |
| 16 | Dingsøyr (2005) | Only 1-in-5 software projects do postmortems; zero of 19 companies are satisfied with their process |
| 17 | Dekker (2014) | New View — human error is a symptom of systemic conditions; blame drives reporting underground |
| 18 | Sujan, Huang & Braithwaite (2017) | Safety-II *complements* Safety-I by also studying successful operations — scope-honesty citation for Ch 5, not a refutation of incident-based learning |

### Network Structure (7)

| # | Paper | One-Line Takeaway |
|---|---|---|
| 19 | Watts & Strogatz (1998) | Small-world topology: high local clustering + short global paths via a few shortcuts |
| 20 | Barabási & Albert (1999) | Scale-free topology emerges from preferential attachment — hubs form naturally |
| 21 | Conway (1968) | System architectures mirror the communication structures of the organizations that build them |
| 22 | MacCormack et al. (2012) | Conway's Law empirically confirmed: tightly-coupled orgs produce 3–6× higher propagation costs |
| 23 | Hansen (1999) | Weak ties help search, hurt complex transfer — postmortems are codified, so they cross weak ties cleanly |
| 24 | Reagans & McEvily (2003) | Optimal networks combine cohesion and range — exactly Watts–Strogatz topology |
| 25 | Borgatti & Foster (2003) | Network research typology — Ch 2 positioning citation, not the cohesion+reach engine |

### Knowledge Transfer & Decay (2)

| # | Paper | One-Line Takeaway |
|---|---|---|
| 26 | Darr, Argote & Epple (1995) | Organizational knowledge depreciates without reinforcement — empirical grounding for the δ parameter |
| 27 | Edmondson (1999) | Psychological safety is the strongest predictor of team learning behavior |

### DevOps & Software Reliability (2)

| # | Paper | One-Line Takeaway |
|---|---|---|
| 28 | Forsgren et al. (2018) | DORA: high performers achieve sub-1-hour MTTR; the gap between tiers is widening |
| 29 | Kim et al. (2016) | Three Ways: Flow, Feedback, Continual Learning — local discoveries become global improvements |

### Agent-Based Modeling Methodology (7)

| # | Paper | One-Line Takeaway |
|---|---|---|
| 30 | Bonabeau (2002) | ABM is the right tool for emergent phenomena from heterogeneous, nonlinear interactions |
| 31 | Epstein (1999) | "If you didn't grow it, you didn't explain its emergence" — generative social science |
| 32 | Harrison et al. (2007) | Simulation is a legitimate primary research method when controlled experiments are infeasible |
| 33 | Carley (1992) | Foundational ABM of org learning — knowledge loss × task interdependence drives net learning |
| 34 | Müller, Kudic & Vermeulen (2021) | Methodological cousin — ABM of inter-firm R&D knowledge networks; precedent for the lineage, not a near-replica of this thesis |
| 35 | Sargent (2020) | Validity is purpose-relative — exploratory models require lower accuracy thresholds than predictive ones |
| 36 | Grimm et al. (2020) | ODD protocol — the seven-element standard for documenting agent-based models |

---

## Bibliography Verdict

The intellectual story across four branches:
- **Absorptive capacity spine:** Cohen & Levinthal → Zahra & George → Argote & Miron-Spektor → Nooteboom → Szulanski → March → Levinthal
- **Network science:** Watts & Strogatz, Barabási & Albert, Hansen, Reagans & McEvily, Borgatti & Foster, Conway, MacCormack
- **Software-engineering practice:** Cook, Leveson, Forsgren, Kim, Dogga, Reed, Lunney & Lueder, Allspaw, Edmondson, Dingsøyr, Drupsteen & Guldenmund, Margaryan, Dekker
- **ABM methodology:** Bonabeau, Epstein, Harrison, Sargent, Grimm, Carley, Müller

---
