# Thesis Proposal: Organizational Learning from Software Incidents

## Current Status

**Proposal:** Ready for committee review (`FOUR_PAGER_PROPOSAL.tex`)

**Simulation Code:** Complete in `../02-Framework-Code/`

## Contributions

1. **A reusable simulation platform** that separates configuration from code, enabling systematic study of knowledge-sharing strategies
2. **An operationalization of absorptive capacity** where exploitation means measurable improvements in prevention, detection, and mitigation

## What This Thesis Does

We built a simulation platform to study how software teams learn from incidents. The simulation models:

- **Teams** that own subsystems within a distributed system
- **Incidents** that hit those subsystems (based on ARTS taxonomy)
- **Learning** through four stages: acquisition, assimilation, transformation, exploitation
- **Knowledge sharing** between teams (NONE, LOCAL, NEIGHBOR, GLOBAL)

We track how different knowledge-sharing strategies affect reliability over time.

## Research Questions

1. How can we model teams learning from incidents in a simulation?
2. How do different knowledge-sharing strategies affect reliability over time?

## Testable Hypotheses

- **H1:** Broader knowledge sharing improves reliability (GLOBAL > NEIGHBOR > LOCAL > NONE)
- **H2:** Higher deployment rates increase incident frequency
- **H3:** Stronger learning effectiveness improves reliability faster
- **H4:** Denser organizational networks spread knowledge more quickly

## Key Experiments

1. **Learning Scenarios:** Compare NONE vs LOCAL vs NEIGHBOR vs GLOBAL
2. **Network Topology:** How does team structure affect knowledge spread?
3. **Exploitation Effectiveness:** How much does learning reduce incidents?
4. **Deployment Velocity:** Can learning keep pace with faster deployments?
5. **Documentation Quality:** Does better documentation improve learning transfer?

## Remaining Work

- [ ] Run all experiments with 30+ seeds
- [ ] Generate publication-quality figures
- [ ] Write results chapter
- [ ] Compare simulated patterns to real incident data (Azure, Google SRE)
- [ ] Platform usability test with external collaborator
- [ ] Write full thesis (expand 4-pager to ~50 pages)
- [ ] Prepare defense slides

## Files

```
06-Thesis-Proposal/
└── FOUR_PAGER_PROPOSAL.tex    # Committee proposal (4 pages + bibliography)

02-Framework-Code/
├── model.py                   # Core simulation
├── run_experiments.py         # 5 experiments
├── tests/test_model.py        # Unit tests
└── thesis_results/            # Experiment outputs
```

## Compile Proposal

```bash
cd 06-Thesis-Proposal
pdflatex FOUR_PAGER_PROPOSAL.tex
bibtex FOUR_PAGER_PROPOSAL
pdflatex FOUR_PAGER_PROPOSAL.tex
pdflatex FOUR_PAGER_PROPOSAL.tex
```

---

**Last Updated:** February 2026
