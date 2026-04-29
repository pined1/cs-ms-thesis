# MS Thesis: Organizational Learning from Software Incidents

**David Pineda | BYU Computer Science MS**
**Advisor: Jonathan Lunt**

> Does sharing incident knowledge more broadly reduce software system failures? This thesis uses an agent-based simulation to study how sharing scope, network topology, deployment velocity, and learning effectiveness interact to determine organizational reliability.

---

## Project Structure

```
CS MS/
├── 01-Papers/              # Paper notes and reading list (29 papers)
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

## Bibliography (29 papers)

### Absorptive Capacity & Organizational Learning

| # | Paper | Key Contribution |
|---|---|---|
| 1 | Cohen & Levinthal (1990) | Absorptive capacity foundation — prior knowledge enables new knowledge |
| 2 | Zahra & George (2002) | 4-stage ACAP pipeline — core theory of this thesis |
| 3 | March (1991) | Exploration vs. exploitation tradeoff |
| 4 | Argote et al. (2021) | Org learning processes and outcomes review |
| 5 | Nooteboom et al. (2007) | Cognitive distance and absorptive capacity |
| 6 | Szulanski (1996) | Internal stickiness — why knowledge transfer fails within firms |

### Learning from Incidents

| # | Paper | Key Contribution |
|---|---|---|
| 7 | Cook (1998) | How complex systems fail — no single root cause |
| 8 | Lunney & Lueder (2016) | Postmortem culture — Google SRE chapter |
| 9 | Allspaw (2012) | Blameless postmortems at Etsy |
| 10 | Dogga et al. (2023) | AutoARTS incident taxonomy at Microsoft Azure scale |
| 11 | Drupsteen & Guldenmund (2014) | What learning from incidents actually means |
| 12 | Margaryan et al. (2017) | Research agenda for learning from incidents |
| 13 | Reed (2019) | The fix-it treadmill problem in software |
| 14 | Dingsøyr (2005) | Postmortem reviews in software engineering |
| 15 | Dekker (2014) | Human error is systemic, not individual |

### Network Structure

| # | Paper | Key Contribution |
|---|---|---|
| 16 | Watts & Strogatz (1998) | Small-world networks — WS topology used as default |
| 17 | Barabási & Albert (1999) | Scale-free networks — BA topology, ba_m crossover finding |
| 18 | Conway (1968) | Org structure mirrors system structure |
| 19 | MacCormack et al. (2012) | Empirical test of the mirroring hypothesis |
| 20 | Hansen (1999) | Weak ties and cross-unit knowledge sharing |
| 21 | Reagans & McEvily (2003) | Network cohesion and range both facilitate knowledge transfer |

### Knowledge Transfer & Decay

| # | Paper | Key Contribution |
|---|---|---|
| 22 | Darr, Argote & Epple (1995) | Knowledge decay in service organizations — grounds decay_rate parameter |
| 23 | Edmondson (1999) | Psychological safety — justifies blameless sharing assumption |

### DevOps & Software Reliability

| # | Paper | Key Contribution |
|---|---|---|
| 24 | Forsgren et al. (2018) | DORA research — deployment frequency vs. change failure rate |
| 25 | Kim et al. (2016) | The DevOps Handbook — Three Ways, local-to-global learning |

### Agent-Based Modeling Methodology

| # | Paper | Key Contribution |
|---|---|---|
| 26 | Bonabeau (2002) | ABM methods for simulating human systems |
| 27 | Epstein (1999) | Generative social science — "if you didn't grow it, you didn't explain it" |
| 28 | Harrison et al. (2007) | ABM in org/management research |
| 29 | Sargent (2020) | Verification and validation of simulation models |
| 30 | Grimm et al. (2020) | ODD protocol — standard for documenting ABMs |

---

| Chapters 1, 2, 5, 6 | ⬜ Not started |

**Last Updated:** April 14, 2026
