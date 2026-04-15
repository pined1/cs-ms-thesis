# Thesis Work Agenda — 17 Weeks
*8 hours/day | Start: 2026-03-09 | Target: Late June 2026*

---

## Big Picture Calendar

| Phase | Dates | Focus | Why |
|---|---|---|---|
| **Phase 1** | Weeks 1–4 (Mar 9 – Apr 5) | Read + Build + Run | Get experiments done before advisor leaves |
| **Phase 2** | Week 5–6 (Apr 6 – Apr 19) | Analyze + Advisor check-in | Get feedback while you still can |
| **Walk** | ~Apr 25 | Commencement | Celebrate — thesis still in progress |
| **Phase 3** | Weeks 8–11 (May) | Write full thesis | Advisor gone — perfect time to write independently |
| **Phase 4** | Weeks 12–15 (Jun) | Revisions + defense | Advisor back — polish and defend |
| **Buffer** | Weeks 16–17 (late Jun) | Final submission | Submission + any last fixes |

---

## Critical Insight: Use May Wisely

Your advisor is gone all of May. This sounds bad but it's actually fine because:
- Writing does not require your advisor
- You need the first 7 weeks to finish code + get results anyway
- By the time May hits you should have a complete data set and just need to write
- When your advisor returns in June you hand them a complete draft — they review once and you're done

**The worst outcome:** Being in May with no data and no draft. Avoid this by treating April 19 as your hard deadline to have all experiments run.

---

## Phase 1 — Build & Run (Weeks 1–4)
*Mar 9 – Apr 5 | Goal: All experiments run, raw data in hand*

---

### Week 1 — Read Papers + Audit Code
*Mar 9–13*

**Monday** ✅ Done (completed Tuesday)
- [x] Read Forsgren et al. (2018) *Accelerate* — focus on MTTR/deployment data
- [x] Read Bonabeau (2002) — ABM methods
- [x] Read Conway (1968) — Conway's Law original paper
- [x] Notes saved to `01-Papers/PAPER_NOTES.md`

**Tuesday** ← You are here
- [ ] Read MacCormack et al. (2012) — Conway's Law empirical (2 hrs)
- [ ] Read Darr, Argote & Epple (1995) — knowledge decay (2 hrs)
- [ ] Read Watts & Strogatz (1998) — small-world networks, 3 pages (30 min)
- [ ] Read Barabási & Albert (1999) — scale-free networks, 3 pages (30 min)
- [ ] Write notes for each in `01-Papers/PAPER_NOTES.md` (1 hr)
- [ ] Re-read your proposal top to bottom as a committee member would (2 hrs)

**Wednesday**
- [ ] Audit `02-Framework-Code/model.py` against proposal requirements (2 hrs)
- [ ] Document every gap in writing (1 hr)
- [ ] Meet with advisor — show updated proposal, confirm format + expectations (1 hr)
- [ ] Start fixing Gap 1: knowledge decay (4 hrs)

**Thursday**
- [ ] Fix Gap 2: stage-transition probabilities with source/other asymmetry (4 hrs)
- [ ] Fix Gap 3: developer-hour cost tracking per stage (4 hrs)

**Friday**
- [ ] Fix Gap 4: all 4 network types working (3 hrs)
- [ ] Fix Gap 5: all 4 sharing scenarios end-to-end (3 hrs)
- [ ] Quick sanity check — run one config, confirm output makes sense (2 hrs)

---

### Week 2 — Complete Implementation
*Mar 16–20*

**Monday**
- [ ] Implement ablation toggles (no decay, no asymmetry, no cost model)
- [ ] Test each ablation runs without errors

**Tuesday**
- [ ] Write unit tests: decay formula, stage transitions, cost accumulation, network connectivity
- [ ] This is Sargent's "computerized verification" — the code does what you designed

**Wednesday**
- [ ] Run small test (6 teams, 50 sims, all 4 strategies) — verify H1 directionally holds
- [ ] Fix any bugs
- [ ] Document all parameter defaults in code comments

**Thursday**
- [ ] Set up full experiment configurations for robustness sweep:
  - Team counts: 6, 20, 50
  - Network types: random, small-world, scale-free
  - Deployment rates: low, medium, high
  - Learning effectiveness: weak, moderate, strong
- [ ] Estimate total compute time

**Friday**
- [ ] Final implementation review — every function matches the proposal
- [ ] Update `02-Framework-Code/README.md`
- [ ] **Code freeze after today — no new features**

---

### Week 3 — Run All Experiments
*Mar 23–27*

**Monday**
- [ ] Run H1: all 4 strategies, 100+ sims, 365-day horizon
- [ ] Set up results folder structure

**Tuesday**
- [ ] Run H2: doubling deployment rate experiment
- [ ] Run H3: knowledge threshold sweep

**Wednesday**
- [ ] Run H4: network density vs. knowledge accumulation
- [ ] Run robustness Part 1: vary team count

**Thursday**
- [ ] Run robustness Part 2: vary network type
- [ ] Run robustness Part 3: vary deployment rate + learning effectiveness

**Friday**
- [ ] Run 3 ablations (no decay, no asymmetry, no cost)
- [ ] Verify all results files are complete
- [ ] **Back up all results to a second location today**

---

### Week 4 — Analyze + Visualize
*Mar 30 – Apr 5*

**Monday**
- [ ] Load all H1–H4 results, compute means + 95% confidence intervals
- [ ] Does H1 hold in >80% of configs?
- [ ] Write down your most surprising finding

**Tuesday**
- [ ] Analyze H2, H3, H4 results
- [ ] Analyze robustness — does H1 hold across team sizes and network types?

**Wednesday**
- [ ] Analyze ablation results — does removing each component matter?
- [ ] Compare MTTR + incident frequency to Forsgren + Dogga ranges

**Thursday**
- [ ] Create all figures:
  - Incident count by strategy (main result)
  - Learning cost vs. reliability (cost-benefit)
  - Knowledge accumulation over time
  - Robustness across team sizes + network types
  - Ablation comparison

**Friday**
- [ ] Create all tables (H1–H4 summary, parameter table, ablation table)
- [ ] Write one-page results outline — what order to tell the story
- [ ] **Send preliminary results + figures to advisor today**

---

## Phase 2 — Advisor Check-In (Weeks 5–6)
*Apr 6–19 | Goal: Get feedback before advisor leaves for May*

---

### Week 5 — Incorporate Early Feedback + Start Writing
*Apr 6–10*

**Monday–Tuesday**
- [ ] Meet with advisor — walk through preliminary results, get direction on framing
- [ ] Note any concerns about the results or methodology

**Wednesday–Friday**
- [ ] Write Implementation Chapter (~2–3 pages)
  - Tech stack + platform architecture
  - Key implementation decisions
  - How to reproduce experiments

---

### Week 6 — Write Results + Final Advisor Meeting
*Apr 13–19*

**Monday–Wednesday**
- [ ] Write Results Chapter (~4–6 pages)
  - H1–H4 findings with figures
  - Robustness analysis
  - Ablation findings
  - Partial validation section

**Thursday**
- [ ] **Final meeting with advisor before May** — show Implementation + Results draft
- [ ] Get explicit feedback on what needs work
- [ ] Ask: what will you want to see when you return in June?

**Friday**
- [ ] Document all advisor feedback in writing
- [ ] Update your plan for May based on feedback

---

## Walk in April ~Apr 25
*Celebrate. Thesis is in progress but you have data, two chapters drafted, and a clear plan.*

---

## Phase 3 — Write the Thesis (May)
*Weeks 8–11 | Advisor gone — this is your writing month*

This is actually the best possible use of May. No meetings, no interruptions. Just write.

---

### Week 8 — Background + Methodology
*Apr 27 – May 3*

**Monday–Wednesday**
- [ ] Write Background & Related Work (~4–5 pages)
  - One solid paragraph per major paper
  - Each subsection ends with the gap your work addresses

**Thursday–Friday**
- [ ] Write Methodology Chapter (~4–5 pages)
  - Expand from proposal
  - Add parameter table (all defaults in one place)
  - Add simulation pipeline figure

---

### Week 9 — Introduction + Discussion
*May 4–10*

**Monday–Tuesday**
- [ ] Write Introduction (~2–3 pages)
  - Now you know your results — foreshadow them
  - End with explicit contributions list

**Wednesday–Thursday**
- [ ] Write Discussion & Limitations (~2–3 pages)
  - What do results mean for practitioners?
  - Which limitations matter most?

**Friday**
- [ ] Write Conclusion & Future Work (~1–2 pages)

---

### Week 10 — First Complete Draft
*May 11–17*

**Monday**
- [ ] Assemble all chapters into one document
- [ ] Read full draft start to finish as a committee member

**Tuesday–Wednesday**
- [ ] Fix every weak section you flagged
- [ ] Ensure every figure is referenced in text with a caption
- [ ] Check every citation appears in the bibliography

**Thursday–Friday**
- [ ] BYU formatting check (margins, title page, abstract, page numbers)
- [ ] Second full read-through

---

### Week 11 — Polish + Buffer
*May 18–24*

- [ ] Fix any remaining issues from second read
- [ ] Proofread for clarity and grammar
- [ ] Have a friend or peer read it — just for clarity, not content
- [ ] **Complete draft ready and waiting for advisor to return**

---

## Phase 4 — Revisions + Defense (June)
*Weeks 12–15 | Advisor back — finish line*

---

### Week 12 — Advisor Returns
*Jun 1 week*
- [ ] Send complete draft to advisor immediately
- [ ] Schedule defense date
- [ ] Build defense slides while waiting for feedback (see slide outline below)

### Week 13 — Incorporate Feedback
- [ ] First round of revisions from advisor
- [ ] Address all committee concerns

### Week 14 — Defense Prep
- [ ] Final thesis formatting + submission
- [ ] Practice defense presentation out loud (twice minimum)
- [ ] Prepare answers to likely committee questions

### Week 15 — Defend
- [ ] **Thesis defense**
- [ ] Final signatures
- [ ] Submit to BYU graduate studies

---

## Weeks 16–17 — Buffer
*Late June*
Any last fixes, formatting issues, or submission delays. You don't want to need this buffer — but you'll be glad it's there.

---

## Defense Slides Outline

| Slide | Content |
|---|---|
| 1 | Title, your name, committee, date |
| 2 | The problem — why incident learning matters |
| 3 | The gap — why simulation, why absorptive capacity |
| 4 | Your contributions (2 bullet points) |
| 5 | Background — AC framework in 4 stages |
| 6 | Methodology — simulation overview figure |
| 7 | Methodology — 4 sharing strategies explained |
| 8 | Results — H1 main finding (best figure) |
| 9 | Results — H3 threshold finding (most interesting) |
| 10 | Results — Ablation findings |
| 11 | Robustness + partial validation |
| 12 | Limitations (honest, 4 bullet points) |
| 13 | Conclusion + future work |
| 14 | Thank you — questions |

---

## Likely Committee Questions — Prepare Answers Now

1. *Why agent-based modeling instead of a simpler model?*
   → Bonabeau (2002): ABM captures heterogeneous agents, emergent behavior, network interactions — none of which aggregate models handle well.

2. *How do you justify the stage-transition probabilities?*
   → Configurable defaults based on source/other asymmetry. Sensitivity analysis shows which parameters most affect conclusions — the ordering of strategies is robust across plausible ranges.

3. *Why does absorptive capacity from R&D apply to software incidents?*
   → Three reasons: Reed (postmortems = assimilation/transformation), Drupsteen (exploitation gap is identical), and stage-to-practice mapping.

4. *Your validation is weak — how do you know it reflects reality?*
   → We claim exploratory validity, not predictive. Sargent's framework: conceptual validity (theory-grounded), computerized verification (unit tests), operational validity (range-checking against Forsgren + Dogga + ablations). Stronger validation is explicitly scoped as future work.

5. *What would change with real incident data?*
   → Calibration of base rates and learning effectiveness parameters. The structural ordering findings are expected to be robust; magnitude findings would change.

---

## Weekly Check-In (Every Friday)

- [ ] Did I hit this week's deliverable?
- [ ] What is blocking me?
- [ ] Do I need advisor input before next Friday?
- [ ] Am I on track to have all data before advisor leaves Apr 19?
