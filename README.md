# MS Thesis: Organizational Learning from Software Incidents

## Project Structure

```
CS MS/
├── 01-Papers/              # Reference papers
├── 02-Framework-Code/      # Simulation code
├── 04-Meetings-Advisor/    # Advisor meeting notes
├── 05-Meetings-Answers/    # Q&A notes
└── 06-Thesis-Proposal/     # Committee proposal
```

## Thesis Contributions

1. **A reusable simulation platform** that separates configuration from code, enabling systematic study of knowledge-sharing strategies
2. **An operationalization of absorptive capacity** where exploitation means measurable improvements in prevention, detection, and mitigation

## Research Questions

1. How can we model teams learning from incidents in a simulation?
2. How do different knowledge-sharing strategies affect reliability over time?

## Core Framework

### Four-Stage Absorptive Capacity (Zahra & George 2002)

1. **Acquisition** - Team becomes aware of the incident
2. **Assimilation** - Team understands the root cause
3. **Transformation** - Team connects new knowledge to existing understanding
4. **Exploitation** - Team implements changes that improve capabilities

### Three Knowledge Dimensions

- **Prevention** - Reduces probability of similar incidents
- **Detection** - Reduces Mean Time to Detect (MTTD)
- **Mitigation** - Reduces severity and time to recovery

### Four Knowledge-Sharing Scenarios

- **NONE** - Teams do not learn (baseline)
- **LOCAL** - Teams learn only from their own incidents
- **NEIGHBOR** - Teams also learn from adjacent teams
- **GLOBAL** - All teams learn from every incident

## Testable Hypotheses

- **H1:** Broader knowledge sharing improves reliability (GLOBAL > NEIGHBOR > LOCAL > NONE)
- **H2:** Higher deployment rates increase incident frequency
- **H3:** Stronger learning effectiveness improves reliability faster
- **H4:** Denser organizational networks spread knowledge more quickly

---

## Papers

### Core Citations (in proposal)

| Paper | Authors | Role |
|-------|---------|------|
| Cohen & Levinthal (1990) | Cohen & Levinthal | Absorptive capacity foundation |
| Zahra & George (2002) | Zahra & George | 4-stage absorptive capacity |
| March (1991) | March | Exploration vs exploitation |
| Cook (1998) | Cook | How complex systems fail |
| Dekker (2014) | Dekker | Psychology of investigation |
| Drupsteen (2014) | Drupsteen & Guldenmund | Learning from incidents definition |
| Lunney & Lueder (2016) | Google SRE | Postmortem practices |
| Allspaw (2012) | Etsy | Blameless postmortems |
| Reed (2019) | J.P. Reed | Post-incident artifacts |
| Argote et al. (2021) | Argote, Lee, Park | Org learning review |
| Margaryan (2017) | Margaryan et al. | LFI research agenda |
| Dogga et al. (2023) | Microsoft Azure | ARTS incident taxonomy |
| Harrison (2007) | Harrison et al. | Simulation methodology |
| Nooteboom (2007) | Nooteboom et al. | Cognitive distance |
| Conway (1968) | Conway | Conway's Law |

### Methodology Citations (need to download)

| Citation | What It Is | Where to Get |
|----------|------------|--------------|
| Yin (2018) | Case study methodology book | [SAGE Publications](https://us.sagepub.com/en-us/nam/case-study-research-and-applications/book250150) ISBN: 978-1506336169 |
| Edmondson (1999) | Psychological safety in teams | [JSTOR](https://www.jstor.org/stable/2666999) |
| Dingsøyr (2005) | Postmortem reviews in software | [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0950584904001296) |

---

## 4-Month Timeline

| Month | Focus |
|-------|-------|
| **Month 1** | Run full experiments, generate figures, start results chapter |
| **Month 2** | Complete results analysis, validation work |
| **Month 3** | Write full thesis draft, get advisor feedback |
| **Month 4** | Revisions, defense prep, buffer time |

---

## Quick Commands

```bash
# Run simulation tests
cd 02-Framework-Code && make test

# Run experiments
cd 02-Framework-Code && python3 run_experiments.py

# Compile proposal
cd 06-Thesis-Proposal && pdflatex FOUR_PAGER_PROPOSAL.tex && bibtex FOUR_PAGER_PROPOSAL && pdflatex FOUR_PAGER_PROPOSAL.tex && pdflatex FOUR_PAGER_PROPOSAL.tex
```

---

**Last Updated:** February 2026
