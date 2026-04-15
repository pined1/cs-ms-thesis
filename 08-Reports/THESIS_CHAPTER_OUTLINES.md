# Thesis Chapter Outlines
**David Pineda | BYU CS MS Thesis**
**Target: 75–100 pages total | Deadline: Two chapters drafted by Apr 19**

---

## Page Count Guide

| Chapter | Target Pages | Status |
|---|---|---|
| 1. Introduction | 10–12 | ⬜ Not started |
| 2. Related Work | 18–22 | ⬜ Not started |
| 3. Methodology | 15–18 | ⬜ Not started |
| 4. Results | 25–30 | ⬜ Not started |
| 5. Discussion & Limitations | 10–12 | ⬜ Not started |
| 6. Conclusion | 3–5 | ⬜ Not started |
| **Total** | **81–99 pages** | |

> **Apr 19 goal:** Chapter 3 (Methodology) + Chapter 4 (Results) drafted — these are data-heavy and advisor needs to validate them before May.

---

## Chapter 1: Introduction
**Target: 10–12 pages**

### Sections
1.1 The Problem — Software systems fail. What organizations *do* with failures separates high-reliability orgs from struggling ones. Postmortem culture is widespread but the *scope* of sharing is unstudied.

1.2 Why This Question Matters — Industry investment in postmortem culture (Google SRE, Netflix, Amazon). Gap in literature: no formal simulation study on sharing scope vs. reliability outcomes.

1.3 What We Built — Overview of the ABM: 20 teams, 4 sharing scenarios, 365-day simulation, 4-stage absorptive capacity pipeline.

1.4 The Four-Stage Learning Pipeline — Acquisition → Assimilation → Transformation → Exploitation. Why all 4 stages matter (justify to committee).

1.5 Research Contributions — (1) First ABM of incident knowledge sharing, (2) quantified H1–H4, (3) open-source simulator.

1.6 The Four Hypotheses — Table format (already drafted in HTML).

1.7 Thesis Organization — One paragraph describing each chapter.

### Papers to Cite Here
| Paper | Notes to Make |
|---|---|
| Cook (1998) | Complex systems fail in complex ways — single root cause is a myth |
| Lunney & Lueder (2016) | Industry standard for postmortem culture (Google SRE chapter) |
| Allspaw (2012) | Blameless postmortems at Etsy — practitioner anchor |
| Forsgren et al. (2018) | DORA research — high performers deploy frequently AND fail less |
| Levitt & March (1988) | Organizational learning as routine-based, history-dependent |
| Argote (1999) | Knowledge must flow through org to be useful |
| Cohen & Levinthal (1990) | Receiving knowledge is not enough — need capacity to absorb |
| Zahra & George (2002) | 4-stage absorptive capacity pipeline — core theory |
| Bonabeau (2002) | ABMs well-suited to emergent organizational behavior |
| Harrison et al. (2007) | Simulation modeling in org/management research |

---

## Chapter 2: Related Work
**Target: 18–22 pages**

### Sections
2.1 Learning from Software Incidents
- What a postmortem is and why it matters
- Current industry practice vs. what research knows
- Gap: scope of sharing has never been formally modeled

2.2 Organizational Learning Theory
- Levitt & March (1988) — routines as carriers of knowledge
- March (1991) — exploration vs. exploitation tradeoff
- Argote (1999) / Argote et al. (2021) — knowledge retention and transfer
- Crossan, Lane & White (1999) — 4I framework (second pipeline model to compare to yours)
- Huber (1991) if found — org learning processes

2.3 Absorptive Capacity
- Cohen & Levinthal (1990) — original model, prior knowledge enables new knowledge
- Zahra & George (2002) — 4-stage reformulation (your core theory)
- Nooteboom et al. (2007) — cognitive distance and absorptive capacity
- Levinthal (1997) — why knowledge accumulation is nonlinear (rugged landscapes)

2.4 Knowledge Transfer and Its Barriers
- Nonaka (1991) — tacit vs. explicit knowledge, why transformation is hardest
- Szulanski (1996) — internal stickiness, why knowledge transfer fails
- Hansen (1999) — weak ties and cross-unit knowledge sharing
- Darr, Argote & Epple (1995) — knowledge decay in service organizations

2.5 Organizational Network Structure
- Watts & Strogatz (1998) — small-world networks
- Barabási & Albert (1999) — scale-free / hub-spoke networks
- Borgatti & Foster (2003) — network paradigm in org research
- Reagans & McEvily (2003) — network cohesion/range and knowledge transfer
- Conway (1968) — org structure mirrors system structure (mirroring hypothesis)
- MacCormack et al. (2012) — test of the mirroring hypothesis

2.6 Learning from Incidents — Safety & Systems Literature
- Dekker (2014) — human error is systemic, not individual
- Leveson (2004) — STAMP, systems-theoretic accident model
- Drupsteen & Guldenmund (2014) — what does learning from incidents actually mean
- Margaryan et al. (2017) — research agenda for learning from incidents
- Sujan et al. (2017) — Safety-II: learn from what goes right too
- Reed (2019) — the fix-it treadmill problem in software

2.7 DevOps and Software Reliability
- Forsgren et al. (2018) — deployment frequency vs. change failure rate
- Kim et al. (2016) — DevOps Handbook, three ways of DevOps
- Dingsøyr (2005) — postmortem reviews in software engineering
- Dogga et al. (2023) — incident taxonomy at Microsoft Azure scale
- Godfrey & German (2008) — software evolution is inevitable

2.8 Agent-Based Modeling Methodology
- Bonabeau (2002) — ABM methods for simulating human systems
- Epstein (1999) — generative social science, why ABM
- Harrison et al. (2007) — ABM in org/management research
- Müller et al. (2021) — ABM of knowledge diffusion in R&D networks (closest prior work)
- Grimm et al. (2020) — ODD protocol (committee asked about this)
- Sargent (2020) — verification and validation of simulation models

### Papers to Cite Here
*(All papers listed above — this chapter cites nearly everything)*

### Notes to Make While Reading
For each paper, answer:
- What is the main finding?
- How does it connect to H1 / H2 / H3 / H4?
- What does it say I should do differently, or validate that I did right?
- One sentence I could quote or paraphrase in this chapter

---

## Chapter 3: Methodology ⭐ DUE APR 19
**Target: 15–18 pages**

### Sections
3.1 Research Design and Approach
- Why simulation over survey/field study (controlled causality)
- ABM as the right tool for emergent org behavior
- Cite: Bonabeau (2002), Epstein (1999), Harrison et al. (2007), Sargent (2020)

3.2 Theoretical Grounding
- Zahra & George (2002) absorptive capacity → 4-stage pipeline
- Darr et al. (1995) → knowledge decay parameter
- Watts & Strogatz (1998), Barabási & Albert (1999) → network topologies

3.3 Model Architecture
- 20 teams, subsystem ownership, stochastic incident generation
- The 4-stage pipeline: Acquisition, Assimilation, Transformation, Exploitation
- Source asymmetry design decision and why
- Knowledge decay function (exponential, half-life ~2 years)
- Signal decay across network hops

3.4 Concrete Worked Example *(committee asked for this)*
- 3-team network: Team A (DATABASE), Team B (neighbor), Team C (neighbor of B)
- Day 1: DATABASE incident on Team A
- Trace through all 4 stages with real probabilities
- Show what changes in Team B's knowledge vector
- Show what C can and cannot get (cascade point)

3.5 The Four Sharing Scenarios
- NONE, LOCAL, NEIGHBOR, GLOBAL — mechanistic description of each
- How switching scenarios changes stage-transition probabilities
- Why all 4 stages are modeled (not collapsed into one probability)

3.6 Network Topologies
- Complete, Erdős-Rényi, Watts-Strogatz, Barabási-Albert, Star
- ba_m and ws_k parameter choices and justification
- Scale-free caveat at 20 nodes

3.7 Experimental Design
- Parameter table (base values and ranges)
- 100 seeds per condition (500 for H3)
- 365-day simulation duration
- What each experiment tests

3.8 Validation Approach
- Conceptual validity: does the model reflect theory?
- Operational validity: do outputs match expectations?
- Sensitivity analysis as robustness check
- Cite: Sargent (2020)

### Papers to Cite Here
| Paper | Where in Chapter |
|---|---|
| Zahra & George (2002) | 3.2, 3.3 — pipeline stages |
| Cohen & Levinthal (1990) | 3.2 — absorptive capacity foundation |
| Darr et al. (1995) | 3.3 — decay parameter calibration |
| Watts & Strogatz (1998) | 3.3, 3.6 — WS network |
| Barabási & Albert (1999) | 3.3, 3.6 — BA network |
| Bonabeau (2002) | 3.1 — ABM justification |
| Epstein (1999) | 3.1 — generative social science |
| Harrison et al. (2007) | 3.1 — ABM in management research |
| Sargent (2020) | 3.1, 3.8 — simulation validation |
| Grimm et al. (2020) | 3.8 — ODD protocol |
| Edmondson (1999) | 3.3 — psychological safety assumption |
| Nooteboom et al. (2007) | 3.3 — cognitive distance in transformation |

---

## Chapter 4: Results ⭐ DUE APR 19
**Target: 25–30 pages**

### Sections
4.1 Overview of Findings
- Summary table of all hypotheses and outcomes
- Effect sizes (Cohen's d) front and center
- All four hypotheses supported

4.2 H1 — Sharing Scope (Experiments 1–3)
- Core results table (NONE/LOCAL/NEIGHBOR/GLOBAL)
- Time dynamics: when does ordering emerge?
- Transformation rate jump explained (source asymmetry)
- Knowledge K saturation curves
- Effect sizes: GLOBAL vs NONE d = 11.51

4.3 H2 — Deployment Velocity (Experiments 4, 10)
- Deployment rate sweep results table
- The saturation finding: 10× deployment → only 24% more incidents under GLOBAL
- H2 × H3 cross-sweep orthogonality finding
- Connection to DORA/Accelerate findings

4.4 H3 — Exploitation Effectiveness (Experiments 3, 5)
- Why we ran it twice (100-seed narrow range → 500-seed wide range)
- Diminishing returns curve
- Comparison to H1: 4% (realistic H3) vs 45% (H1)
- Stage 4 is not the bottleneck — Stage 3 is

4.5 H4 — Network Topology (Experiment 7)
- Five topologies ranked: Complete → ER → WS → BA → Star
- 40% incident range explained by topology alone
- ba_m crossover at 3
- Signal decay math across hops
- Does every team need every incident? (cosine similarity filter)

4.6 Ablation Tests
- exp11 (no decay): NEIGHBOR benefits most, H1 holds
- exp12 (no source asymmetry): LOCAL degrades 7.7%, fragility exposed
- exp13 (learning cost): cost-benefit of GLOBAL

4.7 Sensitivity Sweeps
- ba_m sweep, ws_k sweep, decay rate sweep, base incident rate sweep
- Simulation duration (180/365/730/1095 days)
- Key message: H1 ordering holds across all parameter variations

4.8 Publication-Level Validation
- 500-seed H3 rerun
- Documentation quality × scenario interaction
- Time dynamics analysis
- Cohen's d for all key comparisons

### Papers to Cite Here
| Paper | Where in Chapter |
|---|---|
| Zahra & George (2002) | 4.2, 4.4 — pipeline stage interpretation |
| Forsgren et al. (2018) | 4.3 — DORA connection to H2 |
| Darr et al. (1995) | 4.6 — decay ablation grounding |
| Nooteboom et al. (2007) | 4.4 — cognitive distance explains transformation |
| Watts & Strogatz (1998) | 4.5 — WS baseline topology |
| Barabási & Albert (1999) | 4.5 — BA crossover finding |
| Borgatti & Foster (2003) | 4.5 — network structure and outcomes |
| Reagans & McEvily (2003) | 4.5 — cohesion/range and knowledge transfer |
| Hansen (1999) | 4.5 — weak ties and cross-unit sharing |
| Levinthal (1997) | 4.4 — nonlinear knowledge accumulation |

---

## Chapter 5: Discussion & Limitations
**Target: 10–12 pages**

### Sections
5.1 Interpretation of Findings
- H1 is the dominant lever: structural sharing beats behavioral intensity every time
- H4 is underappreciated: topology alone = 40% variance in reliability
- H2 + H3 provide guidance on where NOT to invest first

5.2 Practical Recommendations for Engineering Organizations
- Invest in global sharing infrastructure before optimizing postmortem quality
- Minimum viable sharing: what's the cheapest topology change that gets 80% of GLOBAL's benefit?
- Avoid star/hub-spoke org designs for incident knowledge flow

5.3 Theoretical Contributions
- First formal ABM test of absorptive capacity in software incident context
- Confirms Zahra & George (2002) pipeline in a computational model
- Extends Darr et al. (1995) decay model to software org context
- Network topology as reliability determinant (extends Borgatti & Foster 2003)

5.4 Limitations
- All 8 MODEL_LIMITATIONS.md items (already written — copy and expand)
- Synthetic data — no real org validation
- Static topology, homogeneous teams, fixed stage probabilities
- Each limitation: what it affects, why H1 still holds

5.5 Future Work
- Per-stage developer hour tracking (advisor requested)
- Severity-weighted acquisition probability
- Dynamic network topology (reorgs)
- ODD protocol formal write-up (JASSS submission)
- 50+ node scale-free validation
- Fun experiments: brain drain, minimum viable sharing, bad actor

### Papers to Cite Here
| Paper | Where in Chapter |
|---|---|
| Zahra & George (2002) | 5.3 — theoretical contribution |
| Cohen & Levinthal (1990) | 5.3 — absorptive capacity extension |
| Darr et al. (1995) | 5.3 — decay model extension |
| Borgatti & Foster (2003) | 5.3 — network topology contribution |
| Szulanski (1996) | 5.1 — knowledge stickiness explains LOCAL ceiling |
| Nonaka (1991) | 5.1 — tacit knowledge explains transformation bottleneck |
| Grimm et al. (2020) | 5.5 — ODD protocol as future work |
| Sargent (2020) | 5.4 — simulation limitations framing |
| Leveson (2004) | 5.4 — systems-theoretic view of model limitations |

---

## Chapter 6: Conclusion
**Target: 3–5 pages**

### Sections
6.1 Summary of Contributions
6.2 Answer to the Research Question — does sharing scope affect reliability? Yes. Quantifiably. GLOBAL = 45% fewer incidents.
6.3 The Practical Message — one paragraph a VP of Engineering could read and act on
6.4 Closing — the simulator as a reusable tool for future org-learning research

### Papers to Cite Here
- Forsgren et al. (2018) — connect back to DORA as real-world validation
- Zahra & George (2002) — close the loop on the theoretical framework
- Cook (1998) — software systems fail; the question is what you do next

---

## Paper Notes Template
*Use this format as you read each paper:*

```
## [Author(s) Year] — [Title]
**Journal/Source:**
**Read date:**

### Main Finding
(1–2 sentences)

### Connection to My Thesis
- H1:
- H2:
- H3:
- H4:
- Methodology:
- Limitations:

### Which Chapter(s)
- Chapter X, Section Y.Z

### Key Quote or Paraphrase
"..."

### What It Validates or Challenges
```

---

## Revised Schedule (updated Apr 14, 2026)

> **Context shift:** Advisor reviewed index.html on Apr 14 and gave major structural feedback.
> index.html is the north star — chapters are written FROM the HTML, not before it.
> Chapter prose deadline shifted to ~Apr 22 to accommodate HTML restructure first.

| Dates | Task | Status |
|---|---|---|
| Apr 14–17 | Restructure index.html per advisor feedback | ⬜ In progress |
| Apr 17–18 | Send updated HTML to advisor for alignment check | ⬜ Not started |
| Apr 18–19 | Upload full project to GitHub | ⬜ Not started |
| Apr 19–22 | Chapter 3 prose (translate cleaned HTML → thesis format) | ⬜ Not started |
| Apr 20 – May 1 | Chapter 4 draft + Chapter 2 (Related Work) | ⬜ Not started |
| May (advisor away) | Finish remaining 8 downloaded papers | Chapters 1, 5, 6 |
| June (advisor returns) | — | Full draft review + revisions |

### HTML Restructure Checklist (must complete before chapter writing)

- [ ] Separate model description from experiment execution (Section 1 = mechanics only)
- [ ] Replace Figure 1.1 hardcoded values with parameter names (P_acquire etc.)
- [ ] Add master "fixed parameters" table at top of Section 2
- [ ] Add per-hypothesis parameter table in each H1–H4 section
- [ ] Introduce exploitation before H3 (can't appear cold in H3)
- [ ] Introduce signal decay before H1
- [ ] Clarify transformation vs. exploitation in Section 1.4
- [ ] Clarify acquisition definition in Section 1.2
- [ ] Add source asymmetry callout in Section 1.3
- [ ] State "20 teams is the study config, not a model limit" in Section 1.4
- [ ] Rewrite conclusions: two-part (model validity + interesting patterns)
- [ ] Add "Open Questions / Future Directions" section
