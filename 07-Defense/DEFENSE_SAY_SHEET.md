# Defense — Say Sheet
**David Pineda | March 27, 2026**

---

**Slide 1 — Title**
"Good morning — thank you for being here. My proposal is about building a simulation tool to study how software teams learn from incidents, and using it to compare knowledge-sharing strategies that organizations currently choose without much empirical guidance."

---

**Slide 2 — The Problem**
"Software systems fail. The real question is whether teams learn from those failures to prevent them from happening again. In modern distributed systems this matters even more — one team's outage can cascade to other services, but one team's lessons can also help other teams avoid the same problem. We want to understand how knowledge-sharing strategies affect reliability. Should teams only learn from their own incidents? Should they share with neighboring teams? Should everyone learn from every incident? These are the questions this work is trying to answer."

---

**Slide 3 — Why Simulation**
"These questions are hard to answer with real organizations. Researchers cannot randomly assign half a company to share knowledge globally while the other half shares nothing, then wait years to compare incident rates. So this work builds a general-purpose simulation platform to explore these questions. And unlike prior organizational simulations that were built for a single study, our platform is designed for reuse — researchers can configure the organizational structure, the incident types, and the learning rules without modifying any code. That lets the research community study many questions about incident learning, not just the ones we anticipate."

---

**Slide 4 — The Gap**
"This work combines concepts from organizational learning and software engineering in a novel way. Organizational learning research has studied absorptive capacity — how organizations acquire, assimilate, and exploit external knowledge — but leaves 'exploitation' abstract. Software engineering research has studied incidents and postmortems, but lacks theoretical frameworks for how learning improves reliability. This combination is what we address. We connect these fields by giving exploitation concrete meaning: a team exploits knowledge when it reduces incident rates, shortens detection time, or improves mitigation effectiveness. That operationalization is what lets us measure whether learning actually happened — something prior work could not do."

---

**Slide 5 — Goals & Contribution**
"Two goals, two contributions. Goal 1 is building the platform — configurable, so researchers can set up different organizational structures and learning rules without modifying code. Goal 2 is using it: systematically comparing the four sharing strategies and measuring their effects on incident rates, detection time, and mitigation effectiveness. The two contributions follow directly from those goals. The platform itself — reusable, separating configuration from logic. And a concrete operationalization of absorptive capacity: we model exploitation as measurable improvements, teams learn to prevent incidents, detect them faster, and fix them more effectively. That bridge between theory and measurable outcome is the core of what this work adds."

---

**Slide 6 — The Platform**
"We propose an agent-based simulator to study how software organizations learn from incidents. Each agent represents a team that owns a subsystem within a larger distributed system. Teams connect through an organizational network that governs how knowledge flows after incidents occur. The sharing strategy determines which teams can learn from which incidents. We use agent-based modeling because it naturally captures heterogeneous teams with local decision rules, emergent system-wide behavior, and network-mediated interactions — features that are difficult to represent in aggregate models."

---

**Slide 7 — Four Strategies**
"We compare four knowledge-sharing strategies. NONE is the baseline — teams do not learn at all. LOCAL means teams learn only from their own incidents. NEIGHBOR means teams also learn from adjacent teams in their network. GLOBAL means all teams learn from every incident. These represent real choices that practitioners currently make without empirical guidance — and that is exactly the gap this work addresses."

---

**Slide 8 — Knowledge Vector**
"Each team maintains a knowledge vector over incident types, where each dimension — prevention, detection, mitigation — ranges from 0 to 1. The incident types follow Microsoft's ARTS taxonomy from Dogga et al.: database timeouts, configuration errors, dependency failures, capacity issues, deployment problems. Each subsystem has a vulnerability profile determining which incident types it is most susceptible to. When a team learns from an incident, the relevant cells increase, and that feeds directly back: prevention knowledge reduces the probability of that incident firing again, detection knowledge reduces time to detect, mitigation knowledge reduces severity and recovery time."

---

**Slide 9 — Four-Stage Pipeline**
"Learning follows the absorptive capacity framework. When an incident occurs, teams progress through four stages: acquisition — the team becomes aware of the incident; assimilation — the team understands the root cause and context; transformation — the team connects new knowledge to existing mental models; and exploitation — the team implements changes that affect reliability. We operationalize exploitation — which is often left abstract in organizational learning research — by tying it to three measurable reliability outcomes: prevention, faster detection, and more effective mitigation. That is what lets us measure whether learning actually happened. And importantly — these stages impose different burdens depending on whether a team lived through the incident or is learning from others. The source team's acquisition and assimilation are automatic. For everyone else, all four stages require real effort. That asymmetry is why cross-team learning is nontrivial."

---

**Slide 10 — What the Platform Measures**
"By simulating different knowledge-sharing strategies and tracking these outcomes over time, we can systematically study which organizational configurations improve reliability — and at what cost in learning overhead. The outputs we track are incident count, severity, duration, availability, and the developer-hours spent on learning. The ratio of reliability improvement to learning cost across strategies is the primary outcome of interest. That is the question this platform is designed to answer."

---

**Slide 11 — The Four Hypotheses**
"We frame the evaluation as four testable hypotheses, and these are the exact words from the proposal. H1 is the central claim — broader sharing produces fewer incidents in a strict ordering, and we have a clear rejection criterion: if the ordering fails in more than 20 percent of configurations, H1 is rejected. H2 connects to real deployment conditions from Forsgren's Accelerate research. H3 asks whether there is a ceiling on learning investment — does more postmortem effort always pay off, or do returns flatten out? H4 is about network structure — does a more connected organization accumulate knowledge faster? All four are directly testable in the simulator."

---

**Slide 12 — H1**
"H1 is the central verification. We already expect broader sharing to produce fewer incidents — that is the theoretical prediction. What we are checking is whether the model we built actually reproduces that ordering. If it does not hold in more than 20 percent of configurations, that is a signal something is off in the model, not a surprise finding. This is the anchor — if H1 holds, we have confidence the rest of the platform is working as designed."

---

**Slide 13 — H2**
"H2 is another model behavior check. We know from Forsgren's Accelerate research that higher deployment frequency increases failure risk in real organizations. So we expect the model to reproduce that — doubling the deployment rate should increase incident count by at least 20%. If it does not, we investigate the incident generation mechanism. This is not a surprising finding, it is a verification that the model is sensitive to the right inputs."

---

**Slide 14 — H3**
"H3 checks that the model produces diminishing returns on learning investment — a relationship we expect based on how absorptive capacity works in theory. If we increase learning effectiveness from weak to strong, the reliability improvement should be sublinear — early gains are large, later gains flatten out. If the model instead produces a linear or accelerating curve, that tells us something in the learning mechanism is not behaving correctly."

---

**Slide 15 — H4**
"H4 checks that network structure affects learning speed the way we expect — denser networks should accumulate knowledge faster because incidents reach more teams through fewer hops. We measure mean team knowledge at the simulation midpoint. If a denser network does not show faster accumulation, we look at how knowledge is propagating through the model. Again — this is a behavior check. We already expect this relationship. If the model does not reproduce it, the propagation mechanism needs investigation."

---

**Slide 16 — Robustness & Validation**
"Results should hold across different configurations — we plan to vary team count, network type, deployment rate, and learning effectiveness, running 100 or more simulations per configuration and reporting confidence intervals. We also seek partial validation by checking whether simulated outputs fall within published ranges: incident frequencies between 10 and 50 per team per year from Dogga et al., and mean time to recovery between 1 and 8 hours from Forsgren et al. We are explicit in the proposal that this is weak validation — it does not substitute for calibration against real organizational data, which is documented as future work."

---

**Slide 17 — Timeline**
"The timeline is realistic because the platform is already built and pilot runs are working. The week of March 23 is dedicated entirely to running experiments at full scale. May is for independent writing while my advisor is traveling — so when he returns in June, a complete draft is ready for one review cycle before defense."

---

**Slide 18 — Limitations**
"I want to be direct about what this work does not do. The findings are directional — we cannot tell a specific company their incident rate will drop by X percent. The model is simplified for tractability, excluding individual skill differences, politics, and budget constraints. Parameters are expert estimates, not calibrated against real data. And importantly — whether software teams actually learn through absorptive capacity stages the way R&D teams do is an empirical question this work does not resolve. We adopt the framework as a theoretically grounded starting point. Practitioner interviews or longitudinal case studies would be the natural next step for validating that assumption."

---

**Slide 19 — Committee Question**
"I want to close by opening the floor. The platform is built and ready to run. My question for the committee is: does this scope — the platform, the four strategies, the four hypotheses, and the robustness testing — represent the right contribution for a master's thesis? If there are gaps or concerns about the framing, now is the time to address them before the full experiment run this week. That is why we are here."

---

**Slide 20 — Thank You**
"Thank you. I'm happy to go into more detail on any part of this — the theoretical grounding, the simulation design, the hypotheses, or the evaluation plan."

---
