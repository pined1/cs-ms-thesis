# Chapter 3: Methodology — Writing Guide
## "Organizational Learning from Software Incidents: An Agent-Based Simulation Study"
### BYU CS MS Thesis — David Pineda

---

> **How to use this guide:** Each section below tells you exactly what to write, which citations to use and how to deploy them, which tables/figures belong there, the target page count, and a "Committee Watch" block flagging what the committee will push back on. Write the sections in order — each one sets up the next.

---

## 3.1 Research Design and Approach
**Target: 1–2 pages**

### What to Write

**Opening paragraph — frame the core question as a design choice.**
State that the central empirical question — whether and how knowledge-sharing scope affects organizational learning from software incidents — is not answerable with field data alone, because the causal mechanisms are confounded by organizational history, culture, team size, and incident frequency in real organizations. This motivates a computational approach.

**Justify ABM specifically (not just simulation generally).**
- Explain what ABMs are: systems of autonomous agents following local rules, from which macro-level patterns emerge without being explicitly programmed in.
- Argue that ABM is the right method when (a) agents are heterogeneous, (b) interactions are local and network-structured, (c) the phenomenon of interest is emergent rather than aggregate, and (d) controlled counterfactual experiments are impossible in the field.
- All four conditions hold here: teams differ in knowledge state, interactions are topology-constrained, organizational learning is emergent from team-level decisions, and you cannot randomly assign real organizations to sharing-scope conditions.
- [CITE: Bonabeau 2002] — use this for the core methodological justification: "Agent-based models are particularly well-suited for studying emergent phenomena in social and organizational systems."
- [CITE: Harrison et al. 2007] — cite here to anchor the method in the management/org-science tradition, not just computer science.

**The explanation vs. prediction distinction — this is philosophically important.**
- Make clear that this study's goal is mechanistic explanation, not predictive forecasting. The simulation does not claim to predict what will happen in any specific organization.
- [CITE: Epstein 1999] — deploy the famous quote directly: "If you didn't grow it, you didn't explain it." Use this to argue that generating the phenomenon from first principles (local rules → observed learning curves) constitutes a genuine explanation of the mechanism, which field regression studies cannot provide.
- Epstein (1999) also provides the justification for synthetic data: mechanism demonstration does not require empirical calibration to a specific organization. Write one sentence explicitly addressing why synthetic data are acceptable here — the committee will ask.

**Scope and limitations paragraph.**
- State clearly: this is a simulation study. Results are claims about the modeled mechanism, not direct prescriptions for practice. The simulation is calibrated to plausible empirical ranges (cite Darr et al. 1995 here as a forward reference) but is not fit to a specific dataset.
- [CITE: Sargent 2020] — mention that model validity is addressed in Section 3.8 per the V&V framework.

**Closing sentence** — state what the rest of Chapter 3 covers: the theoretical grounding (3.2), the model architecture (3.3), a worked example (3.4), the four sharing scenarios (3.5), network topologies (3.6), experimental design (3.7), and validation (3.8).

### Tables / Figures
- No new tables or figures in this section.
- You may include a one-sentence forward reference to Figure 1.1 (the 4-stage pipeline diagram) and Figure 1.2 (the 3-team network diagram) from Chapter 1, noting they will be described in detail in 3.2 and 3.3.

### Citations Summary for This Section
| Citation | How to Use |
|---|---|
| Bonabeau (2002) | Core ABM method justification; cite on first mention of ABM |
| Epstein (1999) | "Grow it" quote + explanation vs. prediction; cite when defending synthetic data |
| Harrison et al. (2007) | Anchor ABM in org/management research tradition |
| Sargent (2020) | Forward reference to V&V in 3.8 |

---

> **Committee Watch — 3.1**
> - **"Why not use real incident data?"** The committee will ask this directly. Your answer: real data confound mechanism with organizational context; ABM allows controlled variation of a single mechanism. Epstein (1999) is your philosophical cover.
> - **"Why not a survey or interview study?"** Same answer — you are not studying perceptions of learning; you are studying the mechanism by which learning propagates. That question requires a model.
> - **"Is this science if there's no empirical grounding?"** Pre-empt this by citing Darr et al. (1995) as the calibration source for decay rates (even though you don't fit to their data, you use their empirically-established half-life range). This is addressed more fully in 3.2 and 3.8.

---

## 3.2 Theoretical Grounding
**Target: 2–3 pages**

### What to Write

**Subsection 3.2.1 — Absorptive Capacity**

Open with the original absorptive capacity (ACAP) construct. [CITE: Cohen & Levinthal 1990] — their foundational insight is that a firm's ability to recognize, assimilate, and apply external knowledge is a function of its prior related knowledge. Explain this in one paragraph. Note that their model was dyadic and non-sequential; it described ACAP as a single capacity but did not specify the internal stages.

Then introduce the Zahra & George (2002) reformulation as your core theoretical framework. [CITE: Zahra & George 2002] — this is the single most important citation in the thesis. Explain their four-stage model in detail:
- **Acquisition:** the firm's ability to identify and obtain externally generated knowledge.
- **Assimilation:** routines and processes that allow the firm to analyze, process, interpret, and understand information from external sources.
- **Transformation:** the ability to develop and refine routines that facilitate combining existing knowledge with newly acquired and assimilated knowledge.
- **Exploitation:** the routines that allow firms to refine, extend, and leverage existing competencies or to create new ones by incorporating acquired and transformed knowledge into operations.

Explain that Zahra & George (2002) distinguish "potential ACAP" (acquisition + assimilation) from "realized ACAP" (transformation + exploitation), and that this distinction directly maps onto the simulation pipeline: potential ACAP governs whether knowledge reaches a team, realized ACAP governs whether the team actually updates its operational competency.

Write a transition sentence: "This study operationalizes each of the four stages as a probabilistic gate in the simulation pipeline, with parameters calibrated to empirically grounded ranges from the literature."

[CITE: Szulanski 1996] — cite here when introducing Transformation. Szulanski's empirical study found that lack of absorptive capacity is the single largest barrier to knowledge transfer (more important than motivation or relationship quality). Use this to justify why the transformation stage has a cosine-similarity threshold rather than a simple probability: knowledge is harder to transform when the receiving team's existing knowledge is distant from the incoming knowledge.

[CITE: Nooteboom et al. 2007] — cite here for "cognitive distance." Their concept directly motivates the cosine-similarity operationalization of transformation difficulty. The greater the cognitive distance between source and receiver, the lower the probability of successful transformation. Write a sentence explaining how this is implemented in the simulation (forward reference to Section 3.3.3).

**Subsection 3.2.2 — Knowledge Decay**

Devote one paragraph to knowledge decay. Without refreshment (new incidents of the same type), teams' knowledge of how to handle that incident type degrades over time. [CITE: Darr, Argote & Epple 1995] — their pizza franchise study is the empirical anchor for this assumption. They found that organizational learning decays at a measurable rate when not reinforced. The exponential decay model with a half-life of approximately 2 years is calibrated to their findings. Write the decay equation explicitly:

```
K(t) = K(t-1) × e^(-λ)   where λ = knowledge_decay_rate = 0.001
```

Show that this implies a half-life of ln(2)/0.001 ≈ 693 days ≈ approximately 2 years, matching Darr et al. (1995).

**Subsection 3.2.3 — Network Structure and Knowledge Flow**

Open with the observation that knowledge does not flow uniformly across an organization; it flows through network ties. Two observations from the literature are particularly relevant:

1. [CITE: Hansen 1999] — weak ties are sufficient for codified knowledge transfer. Hansen found that inter-unit weak ties are effective for transferring codified (explicit, documentable) knowledge, while strong ties are needed for complex tacit knowledge. Software incident knowledge — especially postmortem documents — is largely codified. This justifies the GLOBAL scenario's assumption that a postmortem can reach all teams via weak ties, not just direct neighbors.

2. [CITE: Watts & Strogatz 1998] and [CITE: Barabási & Albert 1999] — provide the structural background for the network topologies studied. One paragraph each, summarizing the small-world and scale-free properties respectively. Forward reference to Section 3.6 for the full topology comparison.

[CITE: Reagans & McEvily 2003] — end this subsection with their finding that both cohesion and range facilitate knowledge transfer, and that the optimal network combines both. This is the theoretical justification for using Watts-Strogatz as the default topology (WS combines local cohesion with global reach via a small number of long-range rewired edges).

### Tables / Figures
- **[FIGURE: Reference Figure 1.1]** — The 4-stage absorptive capacity pipeline diagram (already in Chapter 1). Write: "Figure 1.1 illustrates the four-stage pipeline as implemented in this simulation." Do not reproduce it; reference it.
- You may create a small in-text equation block for the knowledge decay formula (not a numbered figure, just a displayed equation).

### Citations Summary for This Section
| Citation | How to Use |
|---|---|
| Cohen & Levinthal (1990) | Original ACAP; one paragraph |
| Zahra & George (2002) | 4-stage reformulation; your core theory; extended treatment |
| Szulanski (1996) | Transformation difficulty; lack of ACAP as #1 empirical barrier |
| Nooteboom et al. (2007) | Cognitive distance → cosine-similarity operationalization |
| Darr, Argote & Epple (1995) | Knowledge decay half-life calibration |
| Hansen (1999) | Weak ties sufficient for codified knowledge; justifies GLOBAL scenario |
| Watts & Strogatz (1998) | Small-world networks; forward reference to 3.6 |
| Barabási & Albert (1999) | Scale-free networks; forward reference to 3.6 |
| Reagans & McEvily (2003) | Cohesion + range; justifies WS as default topology |

---

> **Committee Watch — 3.2**
> - **"Is Zahra & George (2002) the right framework, or is it just convenient?"** Pre-empt this by explaining what the alternatives are (e.g., organizational learning theory, communities of practice, transactive memory) and why ACAP is the best fit: it is stage-sequential, it distinguishes potential from realized capacity, and it has been explicitly applied to inter-unit knowledge transfer in technology firms.
> - **"Is a 2-year half-life right for software knowledge?"** Defend with Darr et al. (1995) and note the sensitivity sweep in exp11 (ablation — no decay) as a boundary condition. Also note that the 365-day simulation window means most knowledge decays only 20–25% from its peak, so the results are not highly sensitive to the exact decay rate within a reasonable range.
> - **"How do you handle tacit vs. codified knowledge?"** Your answer: the model focuses on incident response knowledge that is codifiable as postmortems. Hansen (1999) justifies this scope restriction.

---

## 3.3 Model Architecture
**Target: 3–4 pages**

### What to Write

This is the most technically detailed section and the one that establishes scientific credibility with a CS committee. Write it with enough specificity that a reader could reimplement the model. Use subsections.

**Subsection 3.3.1 — Agent Design**

Describe the two agent types:

1. **Team agents (20 total):** Each team agent has:
   - A knowledge vector: 15 cells (5 incident types × 3 dimensions). Write out the dimensions explicitly: prevention, detection, mitigation. Explain what each dimension represents operationally (prevention = ability to avoid the incident class; detection = ability to identify it quickly when it occurs; mitigation = ability to reduce impact once detected).
   - A position in the network graph (node).
   - An incident history (tracks which incident types the team has experienced directly).

2. **Incident events:** Not agents in the strict sense, but autonomous events generated stochastically. Each simulation day, each team draws from a Poisson process with base_incident_rate = 0.05 (approximately one incident per team per 20 days). When an incident fires, the type is drawn uniformly from the 5 incident types.

Include the knowledge vector as a table:

**[TABLE: Knowledge Vector Structure]**
| Incident Type | Prevention | Detection | Mitigation |
|---|---|---|---|
| DATABASE_TIMEOUT | cell [0][0] | cell [0][1] | cell [0][2] |
| CONFIG_ERROR | cell [1][0] | cell [1][1] | cell [1][2] |
| DEPENDENCY_FAILURE | cell [2][0] | cell [2][1] | cell [2][2] |
| CAPACITY_ISSUE | cell [3][0] | cell [3][1] | cell [3][2] |
| DEPLOYMENT_PROBLEM | cell [4][0] | cell [4][1] | cell [4][2] |

Explain that each cell holds a real value in [0, 1] representing the team's proficiency on that (type, dimension) combination. Initial values are drawn from a uniform distribution (state what range, e.g., [0.0, 0.2]) to represent low baseline proficiency at simulation start.

**Subsection 3.3.2 — The Four-Stage Learning Pipeline**

This subsection operationalizes Zahra & George (2002) computationally. For each stage, write:
- What it represents theoretically
- How it is implemented in the simulation (what random draw, what threshold)
- What happens if the stage fails (knowledge does not proceed to the next stage)

**Stage 1 — Acquisition (acquisition_prob = 0.9):**
A receiving team encounters a knowledge artifact (postmortem or incident signal) from a source team. With probability 0.9, the team successfully acquires (receives) the artifact. If the team does not acquire it, the pipeline terminates for that event. The high probability (0.9) reflects the assumption that, under the sharing scenario's structural conditions, knowledge artifacts are broadly accessible; the stage models information-retrieval friction, not social barriers. [CITE: Edmondson 1999] — note that the high acquisition probability assumes psychological safety (teams share honestly and do not withhold); cite Edmondson (1999) as the theoretical assumption behind this parameter.

Note the signal decay modifier: for knowledge traveling across the network, acquisition probability is attenuated by path length:

```
p_acquire = acquisition_prob × signal_decay^path_length
           = 0.9 × 0.8^path_length
```

This means knowledge two hops away has p_acquire = 0.9 × 0.64 = 0.576, and three hops away has p_acquire = 0.9 × 0.512 = 0.461. Explain that this reflects information fidelity loss across transmission hops — a well-established phenomenon in organizational communication.

**Stage 2 — Assimilation (assimilation_prob = 0.7):**
Conditional on acquisition, the team attempts to parse and contextualize the knowledge. With probability 0.7, assimilation succeeds. If it fails, the pipeline terminates. Assimilation failure represents the team reading a postmortem but failing to connect it to their operational context — common in cross-functional or geographically distributed teams.

**Source asymmetry:** The source team (the team that directly experienced the incident) is assumed to learn implicitly (by experiencing the incident) and therefore skips stages 2–4. The pipeline stages 2–4 apply only to receiving teams, not the source. This is a deliberate design choice: direct experience is a different learning mode from vicarious learning. Note the ablation study (exp12) that tests what happens when source asymmetry is removed.

**Stage 3 — Transformation (cosine similarity threshold):**
Transformation is qualitatively different from the preceding stages: instead of a fixed probability, it succeeds only when the receiving team's existing knowledge vector (for the relevant incident type) is sufficiently similar to the incoming knowledge. The similarity is measured by cosine similarity between the receiving team's knowledge subvector (3 cells for the incident type) and the incoming knowledge subvector. [CITE: Nooteboom et al. 2007] — cognitive distance; [CITE: Szulanski 1996] — causal ambiguity; the cosine-similarity threshold operationalizes both. If transformation fails, knowledge is not integrated into the team's vector, though the team may retry on future incidents.

**Stage 4 — Exploitation (exploitation_prob = 0.6):**
Conditional on transformation, the team updates its knowledge vector by averaging its existing value with the incoming value (or by taking a weighted update — specify exactly which). Exploitation probability = 0.6 models the organizational friction between knowing what to do and actually changing operational practice. This is the "potential → realized ACAP" gap that Zahra & George (2002) describe. The ablation study exp13 (learning cost) tests a variant where exploitation carries an additional computational cost.

**Subsection 3.3.3 — Knowledge Decay**

After each simulation day, all knowledge cells in all team vectors are multiplied by the decay factor:

```
K(t) = K(t-1) × e^(-0.001)
```

Explain the choice of daily decay (applied each of 365 simulation days). Note that this decay is universal — all cells decay regardless of sharing scenario — so the decay mechanism does not confound the sharing comparisons. It does make the no-sharing (NONE) scenario more disadvantageous over time, which is the theoretically expected direction. [CITE: Darr, Argote & Epple 1995] — recite here briefly; full calibration discussion is in 3.2.

**Subsection 3.3.4 — Simulation Time Step**

Describe the tick structure clearly:
1. For each team, draw incidents from Poisson process.
2. For each incident, source team learns directly (implicit learning; stages 2–4 skipped).
3. Under the active sharing scenario, propagate the incident signal to reachable teams via the pipeline.
4. Apply knowledge decay to all cells in all teams.
5. Record state for analysis.

Explain that the simulation runs for 365 ticks (days). Write a sentence justifying 365 days: results are stable across 180/365/730/1095-day runs with the same ordering of conditions; 365 days represents approximately one annual cycle, which is a natural unit for organizational planning.

### Tables / Figures
- **[TABLE: Knowledge Vector Structure]** — as drafted in 3.3.1 above.
- **[FIGURE: Reference Figure 1.2]** — The 3-team network diagram from Chapter 1. Write: "Figure 1.2 illustrates the signal propagation mechanism through a three-team network, showing how signal decay attenuates acquisition probability across hops."
- Consider including a short pseudocode block (not a numbered figure) showing the per-tick simulation loop. This helps CS readers and demonstrates rigor.

---

> **Committee Watch — 3.3**
> - **ODD Protocol:** CS and simulation-methodology committee members may ask why the model is not described using the ODD (Overview, Design concepts, Details) protocol. Your answer: [CITE: Grimm et al. 2020] — acknowledge ODD as the standard and note that a full ODD-format description is available as supplementary material (or "is provided in Appendix X" / "is left for future work"). Do not dismiss the question; acknowledge the standard and explain your deviation. Grimm et al. (2020) write that "incomplete descriptions violate the central requirement of science that materials and methods must be specified in sufficient detail to allow replication" — use this quote to show you know the standard, then point to Sections 3.3–3.7 as providing the equivalent information outside the ODD template.
> - **"Why 20 teams?"** The committee will push on this. Your answer: 20 teams is the practical sweet spot for ABM at this scale — large enough for network topology to matter (you need at least 10–15 nodes for WS and BA topologies to show their characteristic properties), small enough for full experimental replication at 100 seeds to be computationally tractable. Note the limitation explicitly: at N=20, scale-free (BA) topology is constrained because hub formation is less pronounced than at larger scales. Flag this as a limitation in Chapter 5.
> - **"Is the pipeline Markovian?"** Yes — each stage depends only on the current state of the receiving team, not on history. Be prepared to state this clearly.
> - **"What are initial conditions?"** Write the initialization procedure explicitly in 3.3.1 (uniform distribution for initial knowledge values). The committee will ask.

---

## 3.4 Concrete Worked Example
**Target: 1–2 pages**

### What to Write

This section is pedagogical — it shows the pipeline in action with specific numbers. A well-written worked example is one of the best things you can do for your thesis: it proves the mechanism is computationally well-defined, it helps readers who are not simulation experts, and it catches implementation errors before the committee does.

**Set up the example:**
- Three teams: Team A (source), Team B (1 hop away), Team C (2 hops away).
- Incident type: DATABASE_TIMEOUT.
- Team A experiences a DATABASE_TIMEOUT incident on Day 47.

**Walk through each stage with specific numbers:**

Step 1 — Team A (source) experiences the incident:
- Team A's knowledge subvector for DATABASE_TIMEOUT: [prevention=0.45, detection=0.30, mitigation=0.55].
- Direct experience updates this vector (implicit learning); assume a fixed direct-learning increment, e.g., each cell increases by 0.1 (capped at 1.0). State the update rule explicitly.
- Post-incident: [prevention=0.55, detection=0.40, mitigation=0.65].

Step 2 — Signal propagates to Team B (1 hop):
- p_acquire = 0.9 × 0.8^1 = 0.72. Draw: success (assume).
- p_assimilate = 0.7. Draw: success (assume).
- Team B knowledge subvector: [0.20, 0.15, 0.25]. Cosine similarity with Team A's post-incident vector [0.55, 0.40, 0.65]: compute the value. (You should compute this in your write-up; it will be approximately 0.99 given both vectors are positive and not too far apart, but use the actual formula.)
- Transformation threshold: assume 0.6 (choose a defensible threshold and state it explicitly). Cosine similarity exceeds threshold: transformation succeeds.
- p_exploit = 0.6. Draw: success (assume).
- Update rule: Team B's new vector = average of [0.20, 0.15, 0.25] and [0.55, 0.40, 0.65] = [0.375, 0.275, 0.45].

Step 3 — Signal propagates to Team C (2 hops):
- p_acquire = 0.9 × 0.8^2 = 0.576. Draw: failure (assume, to illustrate attenuation).
- Pipeline terminates. Team C does not update.

Step 4 — Decay applied at end of day:
- All cells multiplied by e^(-0.001) ≈ 0.999. Team A's prevention cell: 0.55 × 0.999 = 0.54945. Note this is negligible over one day but compounds over hundreds of days.

**Closing interpretation:**
Write a paragraph interpreting what this example demonstrates:
- Signal attenuation limits learning for distant teams (Team C fails at 2 hops with 57.6% acquisition probability).
- The pipeline stages act as successive filters; even under GLOBAL sharing, not all knowledge reaches all teams.
- The decay mechanism is slow per-day but creates meaningful knowledge obsolescence by Day 365.
- This example corresponds to the NEIGHBOR scenario for a WS network (Team B is a direct neighbor; Team C is 2 hops). In the GLOBAL scenario, path length would be fixed at 1 for all teams.

### Tables / Figures
- Consider a small inline table showing the pipeline stages and their outcomes for this example (Stage | Probability | Draw | Outcome).
- No separate figure needed; the example is self-contained prose + numbers.

---

> **Committee Watch — 3.4**
> - **Numerical precision:** Make sure the numbers are correct. Compute the cosine similarity by hand and show the formula. The committee will check.
> - **"What is the direct learning update rule?"** You must define it explicitly here (or in 3.3). Do not leave this implicit — it is a core model parameter.
> - **"What is the transformation threshold value?"** Commit to a specific value and cite or argue for it. If it was calibrated empirically or chosen by sweep, say so.

---

## 3.5 The Four Sharing Scenarios
**Target: 1–2 pages**

### What to Write

Open with a framing sentence: the four scenarios represent a progression from zero organizational learning from external incidents to full organizational learning, and they are designed to correspond to recognizable real-world practices.

**Describe each scenario in sequence:**

**NONE — No sharing:**
The baseline / null condition. When a team experiences an incident, no signal is propagated to other teams. Each team learns only from incidents it directly experiences. This scenario models an organization that does not systematically share incident knowledge — the default state for many software organizations without formal postmortem processes. Use this as the reference condition for all hypothesis tests.

**LOCAL — Sharing within the team only:**
Incidents are shared only within the team that experienced them. In the simulation, this means all members of the source team update their knowledge (the team is the atomic unit, so LOCAL is functionally equivalent to NONE at the team level unless you have sub-team agents). Clarify in the text how LOCAL is distinct from NONE in your model — if teams are the atomic agents, LOCAL may be the same as NONE. If LOCAL is distinct, explain how.

Note: Re-read the thesis context and clarify whether LOCAL means "within the team" or "within the local network neighborhood." Based on the four-scenario description, it appears LOCAL means sharing only with direct neighbors (1-hop), and NEIGHBOR means sharing with neighbors-of-neighbors (2-hop). Clarify this and write the definitions clearly and unambiguously.

**NEIGHBOR — Sharing with neighboring teams:**
Incident signals propagate to teams within 1–2 hops in the network graph. This models informal cross-team learning (e.g., ad-hoc Slack conversations, informal postmortem sharing between adjacent squads). The NEIGHBOR scenario is topology-sensitive: the number of reachable teams depends on network structure. This creates an interesting interaction with H4 (topology effects).

**GLOBAL — Organization-wide sharing:**
Incident signals are broadcast to all 20 teams (path length = 1 for all receivers). This models a formal, organization-wide incident review process — a postmortem database that all teams can access. [CITE: Lunney & Lueder 2016] — cite Google's SRE blameless postmortem practice as the real-world archetype for this scenario. [CITE: Kim et al. 2016] — cite the "Third Way" principle: "transforming local discoveries into global improvements" as the design philosophy underlying GLOBAL. For GLOBAL, p_acquire = 0.9 × 0.8^1 = 0.72 (path length is 1 for all non-source teams, since even in GLOBAL the signal travels at least one organizational hop).

Write a table summarizing the four scenarios:

**[TABLE: Four Sharing Scenarios]**
| Scenario | Signal Propagation Rule | Real-World Analogue | Path Length |
|---|---|---|---|
| NONE | No propagation | Siloed teams, no postmortems | N/A |
| LOCAL | Source team only | Team-internal debrief | 0 |
| NEIGHBOR | 1–2 hop neighbors | Informal cross-team sharing | 1–2 |
| GLOBAL | All teams, path_length=1 | Org-wide postmortem database | 1 |

Close with a sentence noting that GLOBAL is topology-independent (all teams receive the signal regardless of graph structure), while NONE and NEIGHBOR are topology-dependent. This motivates H4: topology matters most in the intermediate sharing scenarios.

### Citations Summary for This Section
| Citation | How to Use |
|---|---|
| Lunney & Lueder (2016) | Practitioner anchor for GLOBAL (Google SRE blameless postmortems) |
| Kim et al. (2016) | "Third Way" — theoretical rationale for GLOBAL design |
| Hansen (1999) | Back-reference: weak ties sufficient for codified knowledge (GLOBAL justification) |

---

> **Committee Watch — 3.5**
> - **"How is LOCAL distinct from NONE in your model if teams are atomic?"** You must answer this precisely. If there is no functional difference, either collapse the two conditions or explain what LOCAL adds (e.g., sub-team learning, or LOCAL = sharing with the team's direct network neighbors).
> - **"Why is path_length=1 for GLOBAL and not 0?"** Because even in a global broadcast, knowledge still travels from the source team to the platform (one hop), and then from the platform to the receiver (one hop). Path length = 1 reflects that organizational hops exist even in global scenarios. Make this explicit.
> - **"Are these scenarios realistic?"** Cite Lunney & Lueder (2016) and Kim et al. (2016) to ground GLOBAL. For NONE, note that many software organizations operate this way by default — an argument you can support with any industry survey of incident management maturity.

---

## 3.6 Network Topologies
**Target: 1–2 pages**

### What to Write

Open with a framing sentence: network structure determines the reachability and path length of knowledge signals in the NEIGHBOR scenario, and moderates the efficiency of GLOBAL sharing. H4 tests whether topology meaningfully affects organizational learning outcomes.

**Describe each of the 5 topologies:**

**Complete graph:**
Every team is connected to every other team. Maximum connectivity; minimum average path length (= 1 for all pairs). Represents a hypothetical frictionless organization. Useful as an upper-bound reference condition.

**Erdős-Rényi (ER) random graph:**
Edges are included with a fixed probability p, independently. ER graphs have relatively short average path lengths but low clustering compared to real organizational networks. Represent the baseline "random connectivity" condition.

**Watts-Strogatz (WS) small-world graph — DEFAULT:**
Start with a regular ring lattice (each node connected to ws_k=4 nearest neighbors), then rewire each edge with probability ws_p=0.1. Parameters: ws_k=4, ws_p=0.1. WS graphs exhibit high local clustering (like real organizational teams) AND short average path lengths (like real communication networks). [CITE: Watts & Strogatz 1998] — this is the foundational citation for small-world networks.

Justify WS as the default topology: [CITE: Reagans & McEvily 2003] — their study of knowledge transfer in 182 teams found that both network cohesion (clustering) and range (bridging weak ties to distant nodes) independently facilitate knowledge transfer. WS combines both properties. Write explicitly: "The WS topology was selected as the default because it best approximates empirical organizational network structure (Reagans & McEvily, 2003; Watts & Strogatz, 1998) and because it combines the local cohesion and global reach that Reagans and McEvily (2003) identify as independently predictive of knowledge transfer effectiveness."

**Barabási-Albert (BA) scale-free graph:**
Grows by preferential attachment: new nodes attach to existing nodes proportional to their degree. Parameters: ba_m=2. Produces a power-law degree distribution with a small number of high-degree "hub" teams. [CITE: Barabási & Albert 1999] — foundational citation for scale-free networks. Note the limitation at N=20: scale-free properties (including the heavy tail of the degree distribution) are most pronounced at larger N. At N=20, the BA graph has hub-and-spoke characteristics but the degree distribution tail is not well-developed. Flag this as a limitation and note it is addressed in Chapter 5.

**Star graph:**
One central hub team connected to all other teams; no direct connections between peripheral teams. Represents the most extreme hub-and-spoke topology. All inter-team knowledge transfer in NEIGHBOR scenario must flow through the central hub. Tests the effect of extreme centralization.

**[TABLE or FIGURE: Network Topology Comparison]**
Propose a new figure here:

**[FIGURE: Topology Comparison (NEW — to be created)]** — Suggest a 5-panel figure showing a 20-node graph for each topology side by side. Include: Complete, ER, WS (default), BA, Star. For each panel, annotate approximate average path length and average clustering coefficient. This figure should appear in Section 3.6.

You may also include a summary table:
| Topology | Parameters | Avg. Clustering | Avg. Path Length | Key Property |
|---|---|---|---|---|
| Complete | — | High | 1 | Maximum connectivity |
| Erdős-Rényi | p=0.3 (example) | Moderate | Short | Random baseline |
| Watts-Strogatz | k=4, p=0.1 | High | Short | Small-world (DEFAULT) |
| Barabási-Albert | m=2 | Moderate | Short | Scale-free (limited at N=20) |
| Star | 1 hub | Low | 2 | Maximum centralization |

Close with a sentence about what H4 predicts: if topology matters, then WS and Complete should show higher organizational learning than Star under NEIGHBOR sharing, because Star creates a single-point bottleneck.

### Citations Summary for This Section
| Citation | How to Use |
|---|---|
| Watts & Strogatz (1998) | WS small-world topology; foundational |
| Barabási & Albert (1999) | BA scale-free topology; foundational |
| Reagans & McEvily (2003) | Cohesion + range; justifies WS as default |

---

> **Committee Watch — 3.6**
> - **"Why WS as default, not Complete or ER?"** This is the most likely topology question. Answer: WS best approximates empirically observed organizational networks (Reagans & McEvily, 2003) and is the theoretically motivated choice (combines cohesion and range). Complete is an idealization; ER has unrealistically low clustering for human organizations.
> - **"Isn't N=20 too small for BA to show scale-free properties?"** Yes — acknowledge this explicitly in the text and again in Chapter 5 limitations. A follow-up study with N=200 would be a future-work item.
> - **"How do you generate the ER graph — what is p?"** You need to specify the ER parameter or note that it was set to produce the same expected number of edges as WS (degree-matched comparison). If you degree-match, say so explicitly.

---

## 3.7 Experimental Design
**Target: 2–3 pages**

### What to Write

Open with an overview: the experimental design consists of a primary set of hypothesis-testing experiments and a secondary set of ablation studies. Each experiment varies one or two parameters while holding all others at their base values (Table X). All experiments run 100 seeds (500 for H3) to ensure statistical reliability; each seed corresponds to a different random number sequence, so outcomes reflect the distribution of possible simulation trajectories rather than any single run.

**Subsection 3.7.1 — Base Parameter Table**

**[TABLE: Base Parameters]** — include this table with the following rows:

| Parameter | Symbol | Base Value | Range Tested | Notes |
|---|---|---|---|---|
| Number of teams | num_teams | 20 | — | Fixed |
| Simulation days | simulation_days | 365 | 180, 365, 730, 1095 (sensitivity) | 1 year baseline |
| Random seeds | seeds | 100 | 500 (H3 only) | Per condition |
| Base incident rate | base_incident_rate | 0.05 | 0.01–0.20 (H2 sweep) | Daily per-team Poisson rate |
| Acquisition probability | acquisition_prob | 0.9 | — | Fixed; Edmondson (1999) |
| Assimilation probability | assimilation_prob | 0.7 | — | Fixed |
| Transformation threshold | transformation_threshold | cosine similarity | — | Szulanski (1996) |
| Exploitation probability | exploitation_prob | 0.6 | 0.1–1.0 (H3 sweep) | Stage 4 gate |
| Knowledge decay rate | knowledge_decay_rate (λ) | 0.001 | 0 (exp11 ablation) | ~2 yr half-life; Darr et al. (1995) |
| Signal decay | signal_decay | 0.8 | — | Per-hop attenuation |
| WS neighbors | ws_k | 4 | — | Watts-Strogatz param |
| WS rewiring prob | ws_p | 0.1 | — | Watts-Strogatz param |
| BA attachment edges | ba_m | 2 | — | Barabási-Albert param |

**Subsection 3.7.2 — Hypothesis-Testing Experiments**

Describe each hypothesis and its operationalization as one short paragraph each, then present the experiment summary table.

**H1 — Sharing scope predicts organizational learning:**
Prediction: GLOBAL > NEIGHBOR > LOCAL > NONE on cumulative knowledge (or incident resolution quality). Operationalized by exp01–03 (100 seeds each, all 4 sharing scenarios, WS default topology). Three replications confirm result stability.

**H2 — Deployment velocity (incident rate) moderates learning:**
Prediction: higher incident rates (more learning events) accelerate knowledge accumulation, but only under sharing conditions; under NONE, higher incident rates do not benefit non-experiencing teams. Operationalized by exp04: 5 incident rates × 2 scenarios (NONE vs GLOBAL) × 100 seeds = 1,000 simulation runs. Also exp10: H2×H3 cross-sweep for interaction effects.

**H3 — Exploitation probability shows diminishing returns:**
Prediction: increasing exploitation probability from low values yields large gains in organizational learning, but the marginal benefit diminishes at high exploitation probabilities (diminishing returns). Operationalized by exp05: exploitation probability swept from 0.1 to 1.0 × 100 seeds (500 seeds for the primary H3 result). Note: H3 uses 500 seeds because exploitation is a within-pipeline parameter whose effect is noisier than scenario-level effects.

**H4 — Network topology moderates organizational learning:**
Prediction: under NEIGHBOR sharing, topology significantly affects organizational learning; Complete > WS ≈ ER > BA > Star (roughly). Under GLOBAL sharing, topology effect is attenuated (GLOBAL broadcasts to all teams regardless of topology). Operationalized by exp07: 5 topologies × 100 seeds.

**[TABLE: Experiment Summary]**

| Exp ID | Hypothesis | Variables | Conditions | Seeds | Total Runs |
|---|---|---|---|---|---|
| exp01 | H1 (baseline) | Sharing scenario | 4 scenarios | 100 | 400 |
| exp02 | H1 (replication 1) | Sharing scenario | 4 scenarios | 100 | 400 |
| exp03 | H1 (replication 2) | Sharing scenario | 4 scenarios | 100 | 400 |
| exp04 | H2 | Incident rate × scenario | 5 rates × 2 scenarios | 100 | 1,000 |
| exp05 | H3 | Exploitation probability | 10 levels | 100 | 1,000 |
| exp07 | H4 | Network topology | 5 topologies | 100 | 500 |
| exp10 | H2×H3 | Incident rate × exploitation | Cross-sweep | 100 | varies |
| exp11 | Ablation — no decay | knowledge_decay_rate=0 | 4 scenarios | 100 | 400 |
| exp12 | Ablation — no source asymmetry | Source included in pipeline | 4 scenarios | 100 | 400 |
| exp13 | Ablation — learning cost | Exploitation cost penalty | 4 scenarios | 100 | 400 |
| H3 rerun | H3 (high-power) | Exploitation probability | 10 levels | 500 | 5,000 |

**Subsection 3.7.3 — Statistical Analysis Approach**

Write a short paragraph on the analysis approach. The primary outcome variable is cumulative organizational knowledge at Day 365 (sum of all knowledge cells across all teams). Secondary outcomes: average knowledge per team, variance across teams (knowledge inequality), and fraction of teams above a threshold proficiency level.

State the inferential approach: given 100 seeds per condition, condition means are compared using one-way ANOVA with post-hoc pairwise tests (Tukey HSD or Bonferroni correction for multiple comparisons). Effect sizes are reported as Cohen's d or η². Because this is a simulation study with complete control over the data-generating process, statistical significance at α=0.05 is a lower bar than in empirical studies; effect size interpretation is more informative.

Note: with 100 seeds, the study has high statistical power for detecting medium-to-large effects. The 500-seed H3 rerun was conducted to confirm the diminishing-returns curve shape at higher precision.

### Tables / Figures
- **[TABLE: Base Parameters]** — as described in 3.7.1.
- **[TABLE: Experiment Summary]** — as described in 3.7.2.
- No new figures required in this section; results figures belong in Chapter 4.

---

> **Committee Watch — 3.7**
> - **"Why 100 seeds and not more?"** Answer: 100 seeds per condition provides sufficient statistical power (>0.90) to detect medium effects at α=0.05. The 500-seed H3 rerun demonstrates that 100 seeds is adequate for the hypothesis-level comparisons. Mention total computation time if relevant — this contextualizes the choice.
> - **"Why 365 days?"** See 3.3.4. Results stable across 180/730/1095-day sensitivity runs. Write this sentence explicitly here as well.
> - **"What is the outcome variable, exactly?"** You must define this precisely and operationally. "Cumulative organizational knowledge" must be mathematically defined (sum of all 15×20 = 300 knowledge cells at Day 365, for example). Write the formula.
> - **"How do you handle the interaction between incident rate and knowledge accumulation?"** The H2 design (exp04) addresses this. Be prepared to explain the parametric sweep structure.
> - **"Is exp11/12/13 a full factorial or one-at-a-time ablation?"** Answer: one-at-a-time. Acknowledge the limitation (you cannot observe interaction effects between ablation conditions) and note this is standard practice for simulation sensitivity analysis.

---

## 3.8 Validation Approach
**Target: 1–2 pages**

### What to Write

Open with a sentence about why validation matters for a simulation study: unlike empirical studies where data quality is assessed via reliability and validity of measurement instruments, simulation studies require demonstrating that the model (a) correctly implements the intended design and (b) produces behavior that is plausible given real-world evidence.

**Frame the V&V framework:**
[CITE: Sargent 2020] — use Sargent's verification and validation framework. Distinguish:
- **Verification:** Does the simulation correctly implement the conceptual model? (Is the code bug-free relative to the design spec?)
- **Validation:** Does the conceptual model adequately represent the real-world phenomenon?

**Subsection 3.8.1 — Verification**

Describe the verification procedures used:
1. **Unit tests:** Each pipeline stage (acquisition, assimilation, transformation, exploitation) was tested in isolation with known inputs and expected outputs. Write the specific check for each stage (e.g., "acquisition with probability = 1.0 always passes; probability = 0.0 always fails").
2. **Boundary condition checks:** Knowledge values remain in [0, 1] under all conditions. Decay never produces negative values. The NONE scenario produces no knowledge updates in non-source teams.
3. **Replication of known results:** Under GLOBAL with no decay and exploitation_prob = 1.0, all teams should converge to uniform knowledge by Day 365. Verify this analytically and computationally.
4. **Seed independence:** Results are not driven by a single seed. The 100-seed design demonstrates this; variance across seeds is reported in Chapter 4.

**Subsection 3.8.2 — Validation**

Describe the validation approaches at two levels:

**Face validity:**
- The qualitative ordering of scenarios (GLOBAL > NEIGHBOR > LOCAL > NONE) is consistent with theoretical expectations from Zahra & George (2002) and empirical findings on knowledge-sharing benefits (cite any relevant empirical org-learning study).
- The knowledge decay calibration is grounded in Darr et al. (1995)'s empirical half-life estimates. Write explicitly: "The knowledge decay rate (λ=0.001) was calibrated to match the approximately 2-year half-life reported by Darr et al. (1995) for organizational learning in service contexts."

**Sensitivity analysis as validation:**
- Ablation studies (exp11–13) test whether the key design choices (decay, source asymmetry, learning cost) meaningfully affect results. If the ordering of scenarios is robust across ablation conditions, this strengthens confidence in the mechanism.
- Parameter sensitivity sweeps (H2 and H3) show that the model responds to parameter variation in theoretically expected directions.

**ODD Protocol acknowledgment:**
[CITE: Grimm et al. 2020] — acknowledge the ODD protocol here. Write: "Following Grimm et al. (2020), complete reproducibility requires a full specification of the model's Overview, Design concepts, and Details. The model description provided in Sections 3.3–3.7 covers these elements; a formal ODD-format appendix is provided as supplementary material." If you do not have this appendix yet, note it as future work.

**Limitations of validation:**
Be honest. Write a paragraph noting:
- There is no empirical dataset to validate against (the model is not calibrated to a specific organization's incident history).
- External validity — how well the simulation generalizes to real organizations — depends on the plausibility of the modeled mechanisms, which are grounded in published theory (Zahra & George, 2002; Darr et al., 1995; Szulanski, 1996) but not tested against field data.
- This is appropriate for a theory-building / mechanism-demonstration study (Epstein, 1999), but real-world applicability should be tested in future empirical work.

### Citations Summary for This Section
| Citation | How to Use |
|---|---|
| Sargent (2020) | V&V framework; distinguish verification from validation |
| Grimm et al. (2020) | ODD protocol; acknowledge standard; provide supplementary ODD or flag as future work |
| Darr, Argote & Epple (1995) | Calibration anchor for decay rate |
| Epstein (1999) | Theory-building / mechanism-demonstration; synthetic data acceptable |

---

> **Committee Watch — 3.8**
> - **"Where is the ODD protocol?"** This is the most likely validation question. Have the answer ready: [CITE: Grimm et al. 2020]. Acknowledge the standard, point to Appendix (or note as future work), and explain that Sections 3.3–3.7 cover equivalent content.
> - **"How do you know the simulation is correct?"** Point to unit tests in 3.8.1. If you have a test suite, reference it. If not, describe the manual verification steps.
> - **"Without real data, how can you validate?"** This is the deepest question. Your answer has three parts: (1) calibration to published empirical estimates (Darr et al., 1995); (2) face validity of qualitative predictions; (3) the study's goal is mechanism demonstration (Epstein, 1999), not predictive accuracy. Prepare this answer as a 3-sentence response.
> - **"What would falsify your model?"** If GLOBAL performed worse than NONE, that would falsify H1 and indicate a model error. This is a good question to preempt in the text — write one sentence about what constitutes a disconfirmatory result.

---

## Chapter 3 — Cross-Cutting Notes

### Recommended Writing Order
Write the sections in this order for efficiency:
1. **3.3 first** — it is the most detailed and sets all the terminology.
2. **3.2 second** — once you know exactly how you implemented ACAP, you can write the theory to match.
3. **3.4 third** — the worked example flows naturally after writing 3.3.
4. **3.5 and 3.6** — relatively self-contained; write in order.
5. **3.7** — write after all the above so you can reference the parameter table correctly.
6. **3.8** — write last; references everything above.
7. **3.1** — write last of all; the introduction to the methodology is easiest to write once you know what the methodology is.

### Total Page Target: 12–17 pages

### Master Citation Checklist for Chapter 3
| Citation | Section(s) | Role |
|---|---|---|
| Bonabeau (2002) | 3.1 | ABM justification |
| Epstein (1999) | 3.1, 3.8 | Explanation vs. prediction; synthetic data |
| Harrison et al. (2007) | 3.1 | ABM in org research |
| Sargent (2020) | 3.1, 3.8 | V&V framework |
| Zahra & George (2002) | 3.2, 3.3 | Core theory; 4-stage pipeline |
| Cohen & Levinthal (1990) | 3.2 | Original ACAP |
| Darr, Argote & Epple (1995) | 3.2, 3.3, 3.8 | Knowledge decay calibration |
| Szulanski (1996) | 3.2, 3.3 | Transformation difficulty; causal ambiguity |
| Nooteboom et al. (2007) | 3.2, 3.3 | Cognitive distance; cosine similarity |
| Watts & Strogatz (1998) | 3.2, 3.6 | Small-world topology |
| Barabási & Albert (1999) | 3.2, 3.6 | Scale-free topology |
| Hansen (1999) | 3.2, 3.5 | Weak ties for codified knowledge |
| Reagans & McEvily (2003) | 3.2, 3.6 | Cohesion + range; WS as default |
| Edmondson (1999) | 3.3 | Psychological safety; acquisition_prob assumption |
| Lunney & Lueder (2016) | 3.5 | GLOBAL scenario practitioner anchor |
| Kim et al. (2016) | 3.5 | Third Way; GLOBAL theoretical rationale |
| Grimm et al. (2020) | 3.8 | ODD protocol; reproducibility standard |

### Global Committee Concerns Addressed in Chapter 3
| Concern | Where Addressed | How |
|---|---|---|
| ODD protocol | 3.8 | Grimm et al. (2020); supplementary appendix or future work |
| Why synthetic data? | 3.1, 3.8 | Epstein (1999) explanation vs. prediction |
| Why WS as default? | 3.6 | Reagans & McEvily (2003) cohesion + range |
| Why 20 teams? | 3.3 | Practical scale for ABM; BA limitation noted |
| Why 365 days? | 3.3, 3.7 | Sensitivity sweep stable across 180/730/1095 days |
| Is ACAP the right theory? | 3.2 | Explicit discussion of alternatives |
| Is 2-year decay rate right? | 3.2, 3.7 | Darr et al. (1995); exp11 ablation as boundary |
