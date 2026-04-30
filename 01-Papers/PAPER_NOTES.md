# Master Thesis — Paper Notes
*Source-of-truth document. Every entry follows the canonical structure: read the paper → write down notes → how to include in the paper.*

> **Core thesis reminder:** "My simulation studies emergent reliability."
> Every paper you read should connect back to this sentence.

---

## Status Tracker

| # | Paper | Status |
|---|---|---|
| 1 | Cook (1998) — How Complex Systems Fail | ✅ Read |
| 2 | Lunney & Lueder (2016) — Postmortem Culture | ✅ Read |
| 3 | Harrison et al. (2007) — Simulation in Org Research | ✅ Read |
| 4 | Dogga et al. (2023) — AutoARTS Incident Taxonomy | ✅ Read |
| 5 | Forsgren et al. (2018) — Accelerate / DORA | ✅ Read |
| 6 | Bonabeau (2002) — ABM Methods | ✅ Read |
| 7 | Conway (1968) — How Do Committees Invent? | ✅ Read |
| 8 | MacCormack et al. (2012) — Mirroring Hypothesis | ✅ Read |
| 9 | Darr, Argote & Epple (1995) — Knowledge Decay | ✅ Read |
| 10 | Watts & Strogatz (1998) — Small-World Networks | ✅ Read |
| 11 | Barabási & Albert (1999) — Scale-Free Networks | ✅ Read |
| 12 | Cohen & Levinthal (1990) — Absorptive Capacity | ✅ Read |
| 13 | Zahra & George (2002) — AC Reconceptualized | ✅ Read |
| 14 | March (1991) — Exploration & Exploitation | ✅ Read |
| 15 | Argote & Miron-Spektor (2011) — Org Learning Framework | ✅ Read |
| 16 | Nooteboom et al. (2007) — Cognitive Distance | ✅ Read |
| 17 | Dekker (2014) — Human Error Field Guide | ✅ Read |
| 18 | Drupsteen & Guldenmund (2014) — LFI Sub-Processes | ✅ Read |
| 19 | Margaryan et al. (2017) — LFI Research Agenda | ✅ Read |
| 20 | Edmondson (1999) — Psychological Safety | ✅ Read |
| 21 | Reed (2019) — Beyond the Fix-It Treadmill | ✅ Read |
| 22 | Dingsøyr (2005) — Postmortem Reviews in SE | ✅ Read |
| 23 | Sargent (2020) — V&V of Simulation Models | ✅ Read |
| 24 | Grimm et al. (2020) — ODD Protocol | ✅ Read |
| 25 | Epstein (1999) — Generative Social Science | ✅ Read |
| 26 | Szulanski (1996) — Internal Stickiness | ✅ Read |
| 27 | Hansen (1999) — Search-Transfer Problem | ✅ Read |
| 28 | Reagans & McEvily (2003) — Cohesion and Range | ✅ Read |
| 29 | Kim et al. (2016) — The DevOps Handbook | ✅ Read |
| 30 | Borgatti & Foster (2003) — Network Paradigm Typology | ✅ Read |
| 31 | Levinthal (1997) — Adaptation on Rugged Landscapes | ✅ Read  |
| 32 | Müller, Kudic & Vermeulen (2021) — ABM of R&D Knowledge | ✅ Read |
| 33 | Carley (1992) — Organizational Learning and Personnel Turnover | ✅ Read |
| 34 | Leveson (2004) — STAMP Accident Model | ✅ Read |
| 35 | Allspaw (2012) — Blameless PostMortems and Just Culture | ✅ Read |
| 36 | Sujan, Huang & Braithwaite (2017) — Safety-II Critique | ✅ Read |

**Total: 36 papers — bibliography is committee-ready (see verdict at end of document).**

---

## Paper Entries

---

### 1. Cook (1998) — How Complex Systems Fail

**Journal/Source:** Cognitive Technologies Laboratory, University of Chicago (technical report)
**Bib key:** `cook1998`

**Raw notes:**
- Complex systems are intrinsically hazardous — danger is part of their nature, not an anomaly
- Engineers build defense mechanisms because the hazard is known and expected
- Both technical and organizational safety nets protect the system
- Failure is always latent — present in the system before the incident occurs
- There is no single root cause — "root cause" is a cultural narrative imposed after the fact
- Hindsight bias: once the story's ending is known, it is impossible to remember not knowing

**Summary:** Foundational essay establishing that complex system failures are multi-causal, latent, and that "root cause" is a retrospective fiction. Used to justify blameless postmortems and the systems view of incidents.

**What I'm taking from it:** The argument that root cause is a fiction creates a tension with the simulation's use of Dogga's incident taxonomy (which implies discrete root cause categories). Need one sentence in limitations acknowledging this is a modeling simplification, not an ontological claim.

**Connection to my simulation:** The simulation assigns incident types from Dogga's taxonomy as a practical modeling choice. 

**Citation sentence:**
> *"Cook observes that complex systems always operate with latent failures present, and that 'root cause' is a retrospective narrative rather than an objective finding \cite{cook1998}. Our incident taxonomy follows Dogga et al.\ \cite{dogga2023} as a practical modeling simplification, not a claim that single root causes exist."*

**What it does NOT claim:**
- Does not address software incidents specifically — drawn from healthcare and safety-critical systems
- Does not say postmortems are useless — says blame-oriented postmortems are counterproductive
- The "18 points" are observations, not empirically tested hypotheses

---

### 2. Lunney & Lueder (2016) — Postmortem Culture: Learning from Failure

**Journal/Source:** Site Reliability Engineering (Google SRE Book), Chapter 15, O'Reilly Media
**Bib key:** `lunney2016`

**Raw notes:**
- Outlines Google's philosophy and practical guidelines for blameless postmortems
- Key question shift: "Why did the system allow the human to make this mistake?" not "Who caused this?"
- Uses the 5 Whys to trace the timeline of a failure
- Cultural shift toward transparency and broad sharing
- Psychological safety is a prerequisite for useful postmortems

**Summary:** Prescriptive practitioner guide describing Google's blameless postmortem culture — what high-performing organizations do in practice to learn from incidents.

**What I'm taking from it:** The cultural framing — that learning requires psychological safety and a blame-free environment. The "5 Whys" as a structured investigation method that maps onto the simulation's assimilation stage.

**Connection to my simulation:** The simulation assumes agents share incident knowledge honestly. This assumption is realistic only in organizations with blameless culture. Lunney & Lueder ground that assumption in real practice at scale.

**Citation sentence:**
> *"Blameless postmortem culture, as practiced at Google, assumes that teams share incident details openly without fear of punishment \cite{lunney2016} — an assumption our simulation encodes by modeling agents as willing participants in knowledge sharing under each strategy."*

**What it does NOT claim:**
- Prescriptive guidance, not empirical research — does not prove postmortems produce measurable learning
- Google-specific — does not claim all organizations operate this way
- Cite as evidence that postmortems are designed to produce learning, not that they are proven to achieve outcomes

---

### 3. Harrison et al. (2007) — Simulation Modeling in Organizational and Management Research

**Journal/Source:** Academy of Management Review, 32(4), 1229–1245
**Bib key:** `harrison2007`

**Raw notes:**
- Simulation is a legitimate primary research method in organizational and management research
- Best practice when studying complex organizational behavior with many interacting variables
- Empirical approaches may lack the variables needed for full induction
- "A computer simulation can be used to generate hypotheses that are integrated and consistent"
- Management scholars historically lacked exposure to simulation as a method

**Summary:** Methodological advocacy paper arguing that simulation is the appropriate primary method for organizational research, particularly when controlled real-world experiments are infeasible.

**What I'm taking from it:** The legitimacy argument — simulation is not a fallback when data is unavailable; it is the right tool when studying complex organizational dynamics where controlled experiments are impossible.

**Connection to my simulation:** Directly justifies why simulation is appropriate for studying knowledge-sharing strategies. Real organizations cannot be randomly assigned to sharing policies and observed for years; simulation is the only way to isolate the variable.

**Citation sentence:**
> *"Simulation enables controlled experiments impossible in real organizations and can generate hypotheses that are integrated and consistent \cite{harrison2007} --- precisely the contribution we aim for in comparing knowledge-sharing strategies."*

**What it does NOT claim:**
- Does not specifically endorse agent-based modeling — covers simulation broadly; cite Bonabeau (2002) and Epstein (1999) for ABM-specific justification
- Does not claim simulation replaces empirical work — argues it complements
- Does not prove simulation findings generalize to real organizations

---

### 4. Dogga et al. (2023) — AutoARTS: Taxonomy, Insights and Tools for Root Cause Labelling of Incidents in Microsoft Azure

**Journal/Source:** USENIX Annual Technical Conference (ATC), 359–372
**Bib key:** `dogga2023`

**Raw notes:**
- Largest and most comprehensive study of production incident postmortem reports (PIRs) at the time
- Empirical study of 2,000+ Microsoft Azure incidents with user evaluation
- Built and evaluated the ARTS taxonomy of root-cause categories
- ~20% of incidents labeled solely as "Other"; another ~58% labeled with categories *containing* "Other" (e.g., "Network – Other") — the prior labeling system did not adequately capture root causes
- Different teams used different ad-hoc taxonomies; no industry standard existed before this

**Summary:** Microsoft Azure analysis of 2,000+ production incidents producing the empirically grounded ARTS taxonomy of root cause categories. The prevalence of "Other" labels (~20% solely "Other"; ~58% with "Other" as a qualifier) shows organizations had no consistent language for incidents before ARTS.

**What I'm taking from it:** The ARTS taxonomy (code bugs, config errors, dependency failures, capacity issues, deployment problems) is used as the type system for synthetic incidents in the simulation. Empirical incident frequency data also provides a partial validation anchor.

**Connection to my simulation:** Synthetic incidents in the simulation follow the ARTS taxonomy. This grounds incident generation in real-world categories observed at scale in production systems. The prevalence of "Other"-class labels in the prior taxonomy motivates why a consistent, precise taxonomy matters in practice — something the simulation assumes is already solved.

**Citation sentence:**
> *"Incident types in our simulation follow the ARTS taxonomy derived from analysis of over 2{,}000 production incidents at Microsoft Azure \cite{dogga2023}, grounding synthetic incident generation in empirically observed failure categories."*

**What it does NOT claim:**
- Azure-specific — taxonomy may not generalize to all software organizations
- Does not prove the categories are universal or exhaustive
- AutoARTS labels existing incidents; it does not predict future ones

---

### 5. Forsgren, Humble & Kim (2018) — Accelerate: The Science of Lean Software and DevOps

**Journal/Source:** IT Revolution Press (book)
**Bib key:** `forsgren2018`

**Raw notes:**
- Cluster analysis across four years of survey data identifies three distinct software-delivery performance tiers
- High performers deploy on demand with MTTR under one hour and change failure rates of 0–15%
- Pattern consistent across 2016 and 2017
- High performers do not trade off speed for stability — they excel at both
- Performance gap between tiers is widening over time, not converging

**Summary:** Empirical analysis (DORA program) of high-performing software delivery organizations. High performers achieve sub-hour MTTR with low change failure rates, and the gap between performance tiers grows over time rather than narrowing.

**What I'm taking from it:** MTTR < 1 hour for high performers provides a calibration anchor. The widening gap directly supports the premise that learning compounds — teams with broader knowledge-sharing should pull progressively further ahead.

**Connection to my simulation:** Two connections. (1) MTTR < 1 hour gives a calibration target for high-performing organizations. (2) The widening gap is exactly what the simulation should reproduce — teams with GLOBAL sharing should pull progressively further ahead of LOCAL/NONE teams over time.

**Citation sentence:**
> *"Simulated MTTR is calibrated against high-performing organizations as defined by Forsgren et al., where service restoration occurs in under one hour, a finding consistent across both 2016 and 2017 cohorts \cite{forsgren2018}. The growing performance gap between high and low performers further motivates studying learning strategies that compound reliability improvement over time."*

**What it does NOT claim:**
- Does not prove knowledge sharing causes better MTTR — correlation only
- The "Elite" tier in later DORA reports (2019+) is not in this book
- Change-failure-rate equality between High and Medium performers in 2017 is a cluster artifact — do not over-interpret

---

### 6. Bonabeau (2002) — Agent-Based Modeling: Methods and Techniques for Simulating Human Systems

**Journal/Source:** Proceedings of the National Academy of Sciences, 99(S3), 7280–7287
**Bib key:** `bonabeau2002`

**Raw notes:**
- ABM is a modeling mindset — describing a system from the perspective of its individual constituent units, not aggregate equations
- Primary advantage: capturing emergent phenomena that cannot be predicted from parts alone
- Most appropriate when individual behavior is nonlinear, stochastic, or too complex for differential equations
- Describing behavior through agent activities is more natural than through aggregate transition rates
- Output should be treated as qualitative insight unless carefully calibrated; soft factors in human agents are hard to quantify

**Summary:** Methodological primer arguing ABM is a distinct modeling paradigm best suited for emergent phenomena arising from heterogeneous, nonlinear agent interactions. Explicitly addresses limitations of the method.

**What I'm taking from it:** Three things — (1) the three-benefit framework (emergent phenomena, natural description, flexibility); (2) the explicit "when to use ABM" list matches the simulation's situation: nonlinear behavior, stochastic events, complex individual rules; (3) the qualitative-to-quantitative output spectrum directly supports framing the simulation as exploratory, not predictive.

**Connection to my simulation:** Organization-wide reliability is an emergent phenomenon — not predictable by examining one team in isolation. It arises from interactions of all teams learning and sharing across the network. Bonabeau provides the methodological grounding for treating ABM as the right tool here.

**Citation sentence:**
> *"We use agent-based modeling because organization-wide reliability is an emergent phenomenon arising from team interactions and cannot be captured by aggregate equations \cite{bonabeau2002}. ABM is most appropriate when individual behavior is nonlinear and stochastic, both of which characterize our learning model."*

**What it does NOT claim:**
- Does not say ABM produces accurate quantitative predictions without calibration data — explicitly warns against this
- Does not claim ABM is always better than other methods — only suited for emergent phenomena
- "Only game in town" framing is rhetorical — use as support, not as sole justification

---

### 7. Conway (1968) — How Do Committees Invent?

**Journal/Source:** Datamation, 14(4), 28–31
**Bib key:** `conway1968`

**Raw notes:**
- Organizations that design systems are constrained to produce designs that mirror their own communication structures
- If two teams do not communicate, the components they build will not communicate either
- The structure of a system reflects the structure of the organization that built it
- Design work requires communication; possible designs are limited by existing communication paths
- Stated as a structural necessity, not a choice

**Summary:** Classic practitioner essay arguing that system architecture inevitably mirrors organizational communication structure. Organizations can only build what their communication topology permits.

**What I'm taking from it:** Direct justification for assigning one subsystem per team in the simulation. If team structure mirrors system structure, the organizational network is also the network through which both knowledge and system dependencies flow — making it a meaningful simulation variable.

**Connection to my simulation:** Two design choices grounded by Conway. (1) One subsystem per team is realistic. (2) The knowledge-sharing network and the system-dependency network are related — adjacent teams' incidents are more relevant to each other because their systems are more tightly coupled. This is the basis for similarity-based learning transfer.

**Citation sentence:**
> *"Each agent owns one subsystem, following Conway's observation that organizations are constrained to produce system designs that mirror their communication structures \cite{conway1968,maccormack2012} --- teams build what they talk about, and they talk about what they own."*

**What it does NOT claim:**
- 1968 practitioner essay with no formal data — reasoned observation, not empirical proof
- Does not address incident learning or knowledge sharing directly
- Does not prove causation — MacCormack et al.\ (2012) provides empirical backing

---

### 8. MacCormack, Rusnak & Baldwin (2012) — Exploring the Duality Between Product and Organizational Architectures

**Journal/Source:** Research Policy, 41(8), 1309–1324
**Bib key:** `maccormack2012`

**Raw notes:**
- Tested the "mirroring hypothesis" across 5 matched software product pairs (financial management, word processing, spreadsheet, OS, database)
- Tightly-coupled organizations (co-located, single firm, frequent face-to-face communication) produced architectures with 3–6× higher propagation costs than loosely-coupled organizations
- Result held across all 5 product categories at p < 0.1%
- Linux example: by 2012, 95% of Linux code was written by people who never met Torvalds, yet architecture still reflected early organizational decisions
- Two rival mechanisms: designs evolve to reflect communication constraints, or designers make purposeful choices — either way organizational structure predicts system structure

**Summary:** Empirical confirmation of Conway's 1968 conjecture across five matched software product pairs. Tightly-coupled organizations produce tightly-coupled architectures with overwhelming statistical significance.

**What I'm taking from it:** Empirical propagation-cost values (loosely-coupled 7–23%, tightly-coupled 22–54%) across all product categories. The Linux case shows architectural decisions persist long after the people who made them depart — organizational heritage accumulates in the system.

**Connection to my simulation:** Validates the design choice that each agent owns one subsystem — teams build what they communicate about. Also grounds similarity-based learning transfer: teams that communicate more build more interdependent systems, so their incidents are more relevant to each other.

**Citation sentence:**
> *"MacCormack et al.\ provide empirical confirmation of Conway's Law across five matched software product pairs, finding that tightly-coupled organizations produce architectures with 3--6$\times$ higher propagation costs than loosely-coupled ones (p < 0.1\% in all cases) \cite{maccormack2012}. This grounds our design decision that each agent owns one subsystem and that subsystem similarity reflects organizational proximity."*

**What it does NOT claim:**
- Studied only commercial vs. open-source extremes — real organizations fall between these poles
- Does not address incident learning or knowledge sharing — only architectural coupling
- Establishes correlation, not causation, between organizational and system structure

---

### 9. Darr, Argote & Epple (1995) — The Acquisition, Transfer and Depreciation of Knowledge in Service Organizations

**Journal/Source:** Management Science, 41(11), 1750–1762
**Bib key:** `darr1995`

**Raw notes:**
- Studied 36 pizza franchise stores across 10 franchisees in southwestern Pennsylvania
- Stores exhibit classic learning curves — unit production cost decreases at decreasing rate as cumulative output increases
- Knowledge transfers within same franchisee (weekly sharing, regular meetings, personal ties) but not across franchisees (no required cross-reporting)
- Organizational knowledge depreciates over time through personnel turnover, forgetting, and lost documentation
- Knowledge loss is empirically observed phenomenon, not arbitrary assumption

**Summary:** Organizations exhibit learning curves, but transfer is bounded by organizational structure. Within-franchisee stores benefit from shared learning through regular communication; cross-franchisee stores do not. Crucially, knowledge depreciates over time without reinforcement.

**What I'm taking from it:** The depreciation finding directly justifies the δ decay parameter. The within- vs. cross-franchisee asymmetry maps onto LOCAL/NEIGHBOR/GLOBAL strategy comparison. The mechanisms (turnover, forgetting, lost documentation) are exactly what δ abstracts.

**Connection to my simulation:** The δ decay parameter is grounded empirically here. Organizational knowledge fades without reinforcement; the simulation encodes this as exponential decay applied to each team's knowledge dimensions (Kp, Kd, Km) at each tick. The bounded-by-structure transfer finding validates LOCAL strategy as a realistic baseline.

**Citation sentence:**
> *"Knowledge decay is modeled following Darr et al.'s empirical finding that organizational knowledge depreciates over time through personnel turnover, forgetting, and loss of documentation \cite{darr1995}. Their study of 36 franchise stores demonstrates that knowledge transfer is bounded by organizational structure --- a finding that motivates comparing LOCAL, NEIGHBOR, and GLOBAL sharing strategies."*

**What it does NOT claim:**
- Pizza franchises ≠ software incidents — the mechanism (decay exists, transfer is structure-dependent) generalizes; specific rates do not
- Does not quantify a universal depreciation rate — context-specific
- Does not address software engineering, incidents, or postmortems

---

### 10. Watts & Strogatz (1998) — Collective Dynamics of `Small-World' Networks

**Journal/Source:** Nature, 393(6684), 440–442
**Bib key:** `watts1998`

**Raw notes:**
- Most real networks occupy middle ground between perfectly regular and perfectly random
- Small-world networks have high clustering coefficient C (neighbors tend to know each other) and short characteristic path length L (any two nodes are only a few hops apart)
- Small fraction of randomly rewired shortcut edges dramatically reduces L while barely affecting C
- Transition to small-world is invisible at local level but has global consequences
- Demonstrated on three real networks: film actor collaborations, western US power grid, C. elegans neural network

**Summary:** Real networks exhibit small-world topology — high local clustering alongside short global path lengths — emerging from a mix of regular local connections and a small number of long-range shortcuts.

**What I'm taking from it:** Real organizational networks are small-world: teams cluster tightly around adjacent teams (high clustering), but cross-functional relationships and informal connections bridge distant parts of the organization (shortcuts). Information spreads much faster than in a regular lattice.

**Connection to my simulation:** Watts–Strogatz is one of three baseline network topologies tested. It is the most realistic for mid-sized software organizations. The W&S result predicts that small-world topology should accelerate knowledge accumulation across teams, even at constant connection count — a theoretical prediction the simulation can check against H4 results.

**Citation sentence:**
> *"Organizational networks are modeled using three topologies: random, small-world, and scale-free. The small-world topology follows Watts \& Strogatz \cite{watts1998}, who demonstrate that real social and organizational networks exhibit high local clustering alongside short global path lengths --- a property that significantly accelerates information propagation relative to regular lattices."*

**What it does NOT claim:**
- Does not address organizations, knowledge sharing, or software incidents — application to organizations is our contribution
- Mathematical formulas for L(p), C(p) do not require thesis citation in detail
- Does not prove small-world is better for learning — faster spread does not necessarily improve learning outcomes
- Disease-spreading results are not an appropriate analogy for knowledge sharing

---

### 11. Barabási & Albert (1999) — Emergence of Scaling in Random Networks

**Journal/Source:** Science, 286(5439), 509–512
**Bib key:** `barabasi1999`

**Raw notes:**
- Real networks are not random; they follow power-law degree distributions (scale-free topology)
- Found across biology, technology, and society: a few nodes with enormous connections (hubs), many with few
- Mechanism is preferential attachment: new nodes connect preferentially to already well-connected nodes
- Rich-get-richer dynamic naturally produces hubs
- Topology is universal regardless of network's age, function, or domain

**Summary:** Real networks across biological, technological, and social domains converge to scale-free topology — a few highly-connected hubs surrounded by many sparsely-connected nodes — emerging through preferential attachment.

**What I'm taking from it:** The scale-free topology and its mechanism. In organizational terms: new engineers disproportionately seek out well-connected senior engineers or platform teams. Over time this produces a few hub teams (architecture, platform, DevOps) surrounded by many teams with fewer cross-connections — a realistic structure for large software companies.

**Connection to my simulation:** Scale-free is one of three network topologies tested. It represents large mature organizations where a few hub teams have connections to many other teams while most teams are sparsely connected. The B&A prediction is that hub-mediated knowledge propagates rapidly, but teams far from hubs receive knowledge slowly — testable in H4.

**Citation sentence:**
> *"The scale-free topology follows Barab\'asi \& Albert \cite{barabasi1999}, who demonstrate that preferential attachment --- new nodes connecting preferentially to already well-connected nodes --- produces a small number of highly connected hubs across real-world networks regardless of domain. This models mature software organizations where platform or infrastructure teams serve as knowledge hubs."*

**What it does NOT claim:**
- Does not address organizations or knowledge sharing — application to software teams is our interpretation
- Does not claim scale-free is better or worse than other topologies — that is what the simulation tests
- Detailed power-law mathematics does not require citation in the thesis

---

### 12. Cohen & Levinthal (1990) — Absorptive Capacity: A New Perspective on Learning and Innovation

**Journal/Source:** Administrative Science Quarterly, 35(1), 128–152
**Bib key:** `cohen1990`

**Raw notes:**
- Organizations differ in ability to learn from external knowledge due to what they already know, not effort or intent
- Absorptive capacity = ability to recognize value of new information, assimilate it, apply to productive ends
- Determined by prior related knowledge — you can only absorb what you partially understand
- Learning is self-reinforcing; more knowledge enables more learning (path dependence)
- Lockout: failing to invest early in fast-moving field risks falling too far behind to recognize value of new information
- Boundary-spanning individuals emerge when team's internal expertise differs from external knowledge
- Over-specialization produces Not-Invented-Here (NIH) syndrome

**Summary:** Organizations possess varying absorptive capacities — the ability to recognize the value of new external information, assimilate it, and apply it productively. This capacity is determined entirely by prior related knowledge, creating path dependence and the risk of "lockout" from fast-moving domains.

**What I'm taking from it:** The foundational three-part definition (recognize → assimilate → apply) maps to the first three stages of the four-stage model the simulation implements. Path dependence and lockout predict the widening performance gap between strategies. Boundary-spanners justify small-world shortcuts as high-leverage transfer nodes. The competency trap explains why LOCAL teams may perform adequately short-term but fall behind long-term.

**Connection to my simulation:** Cohen & Levinthal provide the theoretical foundation for the entire learning model. The three-part definition maps to stages 1–3 of the four-stage model. Path dependence and lockout predict widening performance gaps between strategies. Boundary-spanners justify shortcuts in small-world topology. Within-team absorptive limits explain LOCAL's 0% transformation rate (where Szulanski's inter-unit framework does not apply).

**Citation sentence:**
> *"Our learning model builds on Cohen \& Levinthal's \cite{cohen1990} foundational definition of absorptive capacity: the ability to recognize the value of new external information, assimilate it, and apply it to productive ends --- a capacity determined by prior related knowledge and subject to path dependence. The specific four-stage operationalization (acquisition, assimilation, transformation, exploitation) follows Zahra \& George \cite{zahra2002}."*

**What it does NOT claim:**
- Does not provide the four-stage model — that is Zahra & George (2002)
- Original context is R&D investment in manufacturing firms — domain transfer to software incident learning is our contribution
- Lockout finding is theoretical, not empirically tested
- Does not address postmortems, incidents, or software engineering

---

### 13. Zahra & George (2002) — Absorptive Capacity: A Review, Reconceptualization, and Extension

**Journal/Source:** Academy of Management Review, 27(2), 185–203
**Bib key:** `zahra2002`

**Raw notes:**
- Cohen & Levinthal's 3-part definition did not distinguish between ability to take in knowledge and ability to act on it
- Four organizational routines: acquisition, assimilation, transformation, exploitation
- Acquisition: capability to identify and acquire externally generated knowledge critical to operations
- Assimilation: routines and processes allowing the firm to analyze, process, interpret, understand external information
- Transformation: combining newly acquired and assimilated knowledge with existing knowledge, recognizing new combinations
- Exploitation: incorporating transformed knowledge into operations to produce and refine competencies
- Split into Potential AC (PACAP: acquisition + assimilation) and Realized AC (RACAP: transformation + exploitation)
- Gap between PACAP and RACAP governed by efficiency factor (r); social integration mechanisms are primary lever (Proposition 4)

**Summary:** Absorptive capacity comprises four sequential combinative capabilities. Organizations split into Potential AC (acquire, assimilate) and Realized AC (transform, exploit); social integration mechanisms reduce the gap between these.

**What I'm taking from it:** The four-stage model is the direct theoretical specification for agent learning. Each agent progresses through acquisition → assimilation → transformation → exploitation. PACAP/RACAP split explains failure modes — teams can receive and understand postmortems (high PACAP) but fail to change behavior (low RACAP). Proposition 4 justifies why NEIGHBOR/GLOBAL outperform LOCAL/NONE: more sharing = higher social integration = higher efficiency factor.

**Connection to my simulation:** Zahra & George operationalize Cohen & Levinthal conceptually. The four stages are the agent state machine. PACAP maps to knowledge accumulation (Kp/Kd/Km); RACAP maps to operational outcome (reduced incident rate, lower MTTR). Efficiency factor r is what sharing strategies manipulate — GLOBAL maximizes it.

**Citation sentence:**
> *"Agent learning follows the four-stage absorptive capacity framework of Zahra \& George \cite{zahra2002}: acquisition of incident knowledge from postmortems, assimilation through team analysis, transformation by combining new and existing knowledge, and exploitation through updated operational practices. Zahra \& George further establish that social integration mechanisms reduce the gap between potential and realized absorptive capacity (Proposition 4) --- the theoretical basis for predicting that higher-connectivity sharing strategies will produce greater operational improvement."*

**What it does NOT claim:**
- Does not address software incidents, postmortems, or engineering organizations — domain transfer is our contribution
- Efficiency factor r is a theoretical construct, not an empirically measured value
- PACAP and RACAP are organizational constructs; the simulation models them at team level — a scope simplification
- Proposition 4 is theoretical, not empirically tested

---

### 14. March (1991) — Exploration and Exploitation in Organizational Learning

**Journal/Source:** Organization Science, 2(1), 71–87
**Bib key:** `march1991`

**Raw notes:**
- Organizations face tension between exploitation (refining what they know — certain, proximate, predictable returns) and exploration (searching for new knowledge — uncertain, distant, often negative returns)
- Exploitation produces faster, more visible feedback; adaptive processes systematically favor it
- Self-destructive in long run: organizations become highly competent at known domains while losing capacity to adapt
- Formal simulation of mutual learning: individuals learn from organizational code; code adapts from individuals
- Heterogeneous populations including slower-learning individuals produce superior organizational knowledge in equilibrium because they preserve cognitive diversity — fast-learning homogeneous populations converge prematurely to current code beliefs (including errors)
- Moderate personnel turnover improves organizational code by reintroducing diversity

**Summary:** Adaptive processes systematically favor exploitation (refinement of existing knowledge) over exploration (search for new knowledge) because exploitation produces faster, more certain feedback. Effective short-term, self-destructive long-term. Diversity matters more than individual skill.

**What I'm taking from it:** Exact definitions of exploration and exploitation as distinct organizational behaviors. The insight that adaptive processes favor exploitation structurally, not rationally. The mechanism that organizational diversity matters more than individual skill — heterogeneous populations including slower-learning members preserve the cognitive diversity that prevents premature convergence on flawed organizational beliefs.

**Connection to my simulation:** March's exploration/exploitation tension maps onto the four sharing strategies — NONE (pure exploitation), LOCAL (exploitation-dominant), NEIGHBOR (balanced), GLOBAL (exploration-rich). NONE and LOCAL should show competency-trap behavior. The δ parameter interaction: moderate decay may benefit long-run learning by preventing over-convergence — testable in ablation.

**Citation sentence:**
> *"March \cite{march1991} establishes that adaptive processes systematically favor exploitation over exploration because exploitation produces faster, more proximate, and more certain feedback --- a tendency that is effective short-term but self-destructive long-term. Our four sharing strategies represent points on this spectrum: NONE and LOCAL are exploitation-dominant, while NEIGHBOR and GLOBAL introduce increasing degrees of exploratory knowledge acquisition from outside the team's direct experience."*

**What it does NOT claim:**
- Does not address software incidents, postmortems, or engineering organizations
- Mutual learning model is formal simulation, not empirical data — use as theoretical support, not empirical evidence
- Does not prescribe an optimal balance — explicitly states it depends on context

---

### 15. Argote & Miron-Spektor (2011) — Organizational Learning: From Experience to Knowledge

**Journal/Source:** Organization Science, 22(5), 1123–1137
**Bib key:** `argote2011`

**Raw notes:**
- Organizational learning is a process by which experience interacts with context to create knowledge
- Three subprocesses: knowledge creation (generating new knowledge from direct experience), knowledge retention (embedding knowledge so it persists), knowledge transfer (moving knowledge between units)
- Context split into active component (members, tools, tasks and their networks) and latent component (culture, identity, structure, psychological safety)
- Individual learning is necessary but not sufficient — knowledge must be embedded in supra-individual repositories (routines, transactive memory, shared practice) to survive at the organizational level
- Documents robust evidence of knowledge depreciation across multiple industries

**Summary:** Unified theoretical framework for organizational learning. Three subprocesses (creation, retention, transfer) operate within active and latent contexts. Individual learning is insufficient on its own; knowledge must be embedded in organizational structures to persist.

**What I'm taking from it:** Three things. (1) The create/retain/transfer framework is the theoretical spine of the simulation: incidents create knowledge, δ governs retention, sharing strategies govern transfer. (2) The multi-level argument (individual → group → organizational) maps to the three-level structure of the simulation. (3) Documentation of knowledge depreciation across multiple industries provides a second source supporting the δ decay parameter alongside Darr et al. (1995).

**Connection to my simulation:** This is the broadest theoretical umbrella in the bibliography. Every mechanism in the model corresponds to one of its subprocesses or repository types. Cite in Ch 2 to establish the organizational learning framework before introducing absorptive capacity.

**Citation sentence:**
> *"Argote \& Miron-Spektor \cite{argote2011} provide the organizing theoretical framework for this work: organizational learning occurs through three subprocesses --- knowledge creation, retention, and transfer --- embedded in an active context of members and tools operating within a latent context of culture and structure. Our simulation directly operationalizes each subprocess: incidents produce knowledge increments (creation), a decay parameter $\delta$ governs depreciation (retention), and four sharing strategies vary the scope of knowledge dissemination (transfer)."*

**What it does NOT claim:**
- Theoretical framework paper — not an empirical study of software engineering teams; the mapping is our contribution
- Does not prescribe optimal sharing strategies — identifies transfer as a subprocess, not a recommendation for how to structure it
- Does not specify the form of knowledge decay mathematically — cites Darr et al. (1995) for empirical evidence
- The active/latent context distinction is conceptual, not directly operationalized — used here to justify the fixed-parameter treatment of psychological safety

---

### 16. Nooteboom et al. (2007) — Optimal Cognitive Distance and Absorptive Capacity

**Journal/Source:** Research Policy, 36(7), 1016–1034 (working paper version dated 2006)
**Bib key:** `nooteboom2007`

**Raw notes:**
- Inverted-U relationship between cognitive distance and innovation performance, demonstrated across 116 firms in chemicals, automotive, and pharmaceuticals over 12 years
- Two forces: novelty value (increases with distance) and absorptive capacity (decreases with distance)
- Innovation peaks at optimal middle distance; effect stronger for exploratory alliances
- Boredom hypothesis: firms with more accumulated R&D capital get less novelty value from distant partners over time
- Insufficient absorptive capacity is the bottleneck — moderated by cognitive distance, not caused by distance directly

**Summary:** Empirical confirmation of an inverted-U relationship between cognitive distance and innovation outcomes. Distance creates both opportunity (novelty) and constraint (absorption difficulty); insufficient absorptive capacity is the binding constraint, with distance as a moderator.

**What I'm taking from it:** The theoretical mechanism that knowledge sharing across large cognitive distances has diminishing returns. More distant teams hold more novel knowledge, but agents struggle to absorb it efficiently. This grounds why GLOBAL sharing does not always dominate NEIGHBOR sharing in the simulation.

**Connection to my simulation:** Cognitive distance between firms maps to knowledge gaps between teams. Absorptive capacity declining with distance explains why distant teams struggle to integrate incident knowledge from operationally different teams. Optimal cognitive distance is the implicit mechanism behind any result where NEIGHBOR outperforms GLOBAL.

**Citation sentence:**
> *"Nooteboom et al.\ \cite{nooteboom2007} empirically confirm that knowledge sharing follows an inverted-U relationship with cognitive distance: partners who are too similar offer no novelty, while partners who are too distant exceed absorptive capacity. This motivates our comparison of four sharing strategies --- the optimal scope of sharing is not self-evident but depends on cognitive distance between teams."*

**What it does NOT claim:**
- R&D alliances between large industrial firms — not software engineering teams; domain transfer is extrapolation
- Cognitive distance is measured via patent portfolios — a proxy unavailable in software incident contexts; knowledge vector distance is the analogous construct
- Does not model sharing strategies directly — studies alliance partner selection
- Does not show GLOBAL is always worse — shows diminishing returns at high distance

---

### 17. Dekker (2014) — The Field Guide to Understanding `Human Error'

**Journal/Source:** Ashgate Publishing (book, 3rd edition)
**Bib key:** `dekker2014`

**Raw notes:**
- Old View: human error is a cause — find the person, identify bad judgment, fix or remove them
- New View: human error is a symptom — indicator that the system contained conditions making failure likely
- Complex systems are inherently risky trade-offs between safety, productivity, speed, thoroughness
- People create safety through practice at all levels; when they fail, actions made local sense given their knowledge and constraints
- Root cause is not found — it is constructed after the fact
- Removing bad actors leaves the trap in place for the next person and drives reporting underground
- Work-as-imagined vs. work-as-done — gap is where incidents hide

**Summary:** Distinguishes the Old View (human error as cause) from the New View (human error as symptom of systemic conditions). Complex systems are inherently risky; blaming individuals suppresses the incident reporting needed for organizational learning.

**What I'm taking from it:** New View operationalized — each incident is product of systemic conditions (team knowledge, network topology, sharing strategy), not individual incompetence. No root cause exists; it is constructed in postmortems. Blame-oriented response actively harms organizational learning by driving reporting underground.

**Connection to my simulation:** Dekker grounds the systemic view of incidents the simulation assumes. The model never "blames" an agent; it tracks systemic patterns. Dekker's warning about blame driving reporting underground explains why blame-oriented strategies suppress the data that makes learning possible.

**Citation sentence:**
> *"Consistent with Dekker's New View of human error \cite{dekker2014}, our simulation treats incidents as systemic outcomes rather than individual failures --- the incident generation process reflects team-level knowledge gaps, not agent-level incompetence. This framing also justifies our assumption of honest knowledge sharing: Dekker demonstrates that blame-oriented responses drive incident reporting underground, eliminating the information flow that postmortem-based learning requires."*

**What it does NOT claim:**
- Primary context is safety-critical industries (aviation, healthcare, nuclear) — software incident transfer must be acknowledged
- Does not provide empirical data on postmortem outcomes — prescriptive framework
- Source is the book, not the training-presentation derivative

---

### 18. Drupsteen & Guldenmund (2014) — What Is Learning? A Review of the Safety Literature to Define Learning from Incidents

**Journal/Source:** Journal of Contingencies and Crisis Management, 22(2), 81–96
**Bib key:** `drupsteen2014`

**Raw notes:**
- Systematic review of 47 papers on learning from incidents (LFI) in safety-critical industries
- Three LFI subprocesses: (1) analyzing events to learn lessons, (2) using lessons for improvement, (3) sharing and storing lessons
- Analysis is well-documented; implementation and sharing are consistently neglected
- "Potential level of learning was considerably higher than the actual level of learning" — empirical PACAP/RACAP gap
- Sharing typically one-way (email, IT systems); face-to-face/network discussion is more effective
- Trust and openness are prerequisites — without them, incidents are underreported
- Comparison with Argyris & Schön's organizational learning theory shows LFI lacks attention to sharing/storing

**Summary:** Literature review identifying that the sharing-and-storing sub-process is the most neglected stage of incident learning. Organizations identify lessons but consistently fail to implement them or distribute them organization-wide — exactly the PACAP/RACAP gap the absorptive capacity literature predicts.

**What I'm taking from it:** Direct empirical motivation for the thesis. The finding that sharing is the underexposed sub-process is precisely what the simulation isolates and varies. The PACAP/RACAP gap documentation validates that the gap the simulation studies is real and consequential. Trust prerequisite connects to the blameless-postmortem assumption (independently grounded by Edmondson 1999 and Lunney & Lueder 2016).

**Connection to my simulation:** Drupsteen & Guldenmund provide the safety-science version of the research question. Their three-process framework maps to the simulation's pipeline: analyzing events ≈ acquisition + assimilation; using lessons ≈ transformation + exploitation; sharing/storing ≈ the four sharing strategies. Their identification of sharing as the neglected sub-process is the central motivation for varying sharing strategies systematically.

**Citation sentence:**
> *"Drupsteen \& Guldenmund \cite{drupsteen2014} identify sharing and storing lessons as the most underexposed sub-process in organizational learning from incidents --- organizations consistently fail to move from lesson identification (potential absorptive capacity) to organization-wide implementation (realized absorptive capacity). Our simulation directly addresses this gap by comparing four sharing strategies that vary systematically in the scope of knowledge dissemination."*

**What it does NOT claim:**
- Safety-critical industries (chemical, nuclear, aviation) — not software engineering specifically; domain transfer acknowledged via Reed (2019) and Dingsøyr (2005)
- Literature review, not empirical measurement of learning outcomes — use for framing, not causal claims
- Does not quantify the sharing gap — qualitative synthesis only
- Uses Argyris & Schön as theoretical frame, not Zahra & George — acknowledge framework difference if asked

---

### 19. Margaryan, Littlejohn & Stanton (2017) — Research and Development Agenda for Learning from Incidents

**Journal/Source:** Safety Science, 99, 5–13
**Bib key:** `margaryan2017`

**Raw notes:**
- LFI is an underdeveloped research area with four main R&D challenges
- LFI is not coherently defined — cross-study comparison is difficult
- Measurement is immature and inconsistent
- Multi-level operation (individual, team, organizational) and enabler/blocker factors are not well understood
- Persistent gap between LFI research and practitioner use
- Calls for unified research program across safety science, organizational learning, and human factors
- LFI typically assessed through process proxies (did a postmortem happen?) rather than outcome measures (did incident rates change?)
- Identifies simulation as an underused but appropriate method given the multi-level, emergent nature of LFI

**Summary:** Literature review mapping the current state of LFI across four R&D challenges and calling for a unified research program. Identifies simulation as an underused methodological approach.

**What I'm taking from it:** Two contributions — (1) explicit acknowledgment that LFI operates at multiple levels (individual, team, organization), mapping to the simulation's three-level structure; (2) the measurement-by-process-proxy critique. The simulation measures outcomes directly (incident frequency, MTTR), which is the kind of metric the field needs. Margaryan et al.'s identification of simulation as underused is one of the strongest methodological justifications for the ABM approach.

**Connection to my simulation:** Margaryan et al. identify simulation as appropriate for LFI research, noting that multi-level emergent dynamics make controlled field experiments infeasible. The agent-based model directly responds to this gap. Cite in the methodology section to justify the simulation approach itself.

**Citation sentence:**
> *"Margaryan et al.\ \cite{margaryan2017} identify simulation as an underused but appropriate method for LFI research, noting that the multi-level, emergent nature of organizational learning makes controlled field experiments infeasible. Our agent-based model directly responds to this methodological gap by enabling systematic comparison of sharing strategies under controlled conditions."*

**What it does NOT claim:**
- Not an empirical study — literature review and research agenda; use for framing only
- Does not validate any specific sharing strategy or AC model — maps the problem space
- The "multi-level" argument is descriptive, not a formal model; the mapping to AC stages is our contribution
- Primary context is aviation/nuclear/chemical industries — software engineering transfer is extrapolation

---

### 20. Edmondson (1999) — Psychological Safety and Learning Behavior in Work Teams

**Journal/Source:** Administrative Science Quarterly, 44(2), 350–383
**Bib key:** `edmondson1999`

**Raw notes:**
- Team psychological safety: shared belief that the team is safe for interpersonal risk-taking
- Primary predictor of team learning behavior — accounts for more variance than team efficacy, context support, or leader coaching
- Mechanism: interpersonal threat — people who fear embarrassment, rejection, or punishment will not share errors, ask for help, or discuss problems
- Team-level property, not individual confidence — demonstrated through ICC = .39 (p < .0001)
- Learning behavior mediates between psychological safety and team performance
- Held across all four team types studied (functional, self-managed, product development, project)

**Summary:** Empirical demonstration across 51 work teams that psychological safety — a shared belief that interpersonal risk is safe — is the primary predictor of team learning behaviors including error sharing and feedback seeking.

**What I'm taking from it:** Psychological safety is the empirical mechanism that removes interpersonal threat and enables honest incident sharing. This grounds the simulation's assumption of willing knowledge sharing — it holds in teams with psychological safety, which blameless postmortem culture (Lunney & Lueder, Allspaw) creates.

**Connection to my simulation:** The simulation assumes agents share incident knowledge openly — encoding psychological safety as a given. Edmondson provides empirical grounding for when this assumption holds: blameless culture creates the safety that makes honest sharing possible. Without it, NEIGHBOR/GLOBAL strategies would be undermined by incomplete or distorted sharing the model does not capture.

**Citation sentence:**
> *"Our simulation assumes agents share incident knowledge openly --- an assumption that holds only in teams with psychological safety, defined by Edmondson as a shared belief held by members of a team that the team is safe for interpersonal risk-taking \cite{edmondson1999}. Edmondson demonstrates empirically that this belief is the primary predictor of team learning behavior, including the sharing of errors and seeking of feedback that postmortem culture requires."*

**What it does NOT claim:**
- Single company (office-furniture manufacturer) — not a software organization; domain transfer must be acknowledged
- Cross-sectional design — cannot prove psychological safety causes learning, only that they are associated
- Does not address postmortems, incidents, or software specifically
- Psychological safety is not the same as group cohesiveness or team efficacy

---

### 21. Reed (2019) — Beyond the `Fix-It' Treadmill: The Use of Post-Incident Artifacts in High-Performing Organizations

**Journal/Source:** ACM Queue, 17(6), 27–46
**Bib key:** `reed2019`

**Raw notes:**
- Most organizations treat postmortems as source of static remediation items — "fix-it treadmill": incident → postmortem → fix list → repeat
- High-performing organizations use post-incident artifacts to share rich context and update mental maps of complex socio-technical systems
- 91% of organizations consider remediation-item collection the core purpose of postmortems
- Three phases of organizational learning map onto AC stages
- Post-incident artifacts as "patches" to engineers' mental maps
- Three postmortem archetypes: Record-keeper (most common, documents but doesn't drive learning), Facilitator (adds prompts and cultural reminders), Signpost (lightweight pointer to data sources)
- Blamelessness emerges from process centered on context, not from declarations

**Summary:** High-performing organizations use post-incident artifacts primarily to share context and update mental maps of complex systems — moving from tactical accountability to strategic understanding of systemic failure modes — rather than merely to generate remediation lists.

**What I'm taking from it:** Reed is the most directly relevant practitioner paper in the reading list. Every postmortem event in the simulation is exactly what Reed describes: an artifact that transfers knowledge across teams and patches their mental models. Depending on sharing strategy, it reaches only the source team (LOCAL), adjacent teams (NEIGHBOR), or the entire organization (GLOBAL). Reed identifies the failure mode that NONE/LOCAL strategies model: organizations stuck on the fix-it treadmill accumulate static fixes without building the organizational knowledge that prevents future incidents.

**Connection to my simulation:** Reed provides empirical evidence that postmortems function as knowledge-transfer mechanisms in practice. Each postmortem in the simulation increments the receiving team's knowledge dimensions (Kp, Kd, Km) by patching their model of failure propagation — precisely the mechanism Reed observed in high-performing organizations.

**Citation sentence:**
> *"Reed \cite{reed2019} observes that high-performing organizations use post-incident artifacts primarily to share context and update mental maps of complex socio-technical systems --- not merely to generate remediation lists. This empirically grounds our simulation's model of postmortems as knowledge-transfer events: each postmortem increments the receiving team's knowledge dimensions by patching their model of how failures propagate."*

**What it does NOT claim:**
- Single organization case study — generalizability is limited
- Practitioner article, not peer-reviewed empirical research — use as applied evidence
- Does not quantify learning outcomes — observational study, no before/after metrics
- Does not prove that more sharing leads to better outcomes — that is what the simulation tests

---

### 22. Dingsøyr (2005) — Postmortem Reviews: Purpose and Approaches in Software Engineering

**Journal/Source:** Information and Software Technology, 47(5), 293–303
**Bib key:** `dingsoyr2005`

**Raw notes:**
- Postmortem reviews are simple, practical methods for organizational learning in software projects — yet rarely conducted and rarely satisfying
- Survey of 19 European companies: not a single company expressed satisfaction with their postmortem process; only 1 in 5 projects received a post-project review
- Reviews three lightweight postmortem methods (Whitten; Collison & Parcell; Birk et al.)
- Frames postmortems through two knowledge-management lenses: communities of practice (Wenger) and tacit-to-explicit knowledge conversion (Nonaka & Takeuchi)
- Single-loop learning: tune process to fix specific error; double-loop learning: understand governing values and systemic factors
- Kerth's prime directive: "everyone did the best job they could, given what was known at the time"

**Summary:** Empirical documentation that postmortem reviews are underused despite being low-cost, high-value mechanisms for transferring experience. Frames postmortems as tacit-to-explicit knowledge conversion within communities of practice.

**What I'm taking from it:** The 1-in-5 adoption statistic is direct empirical motivation — the gap the simulation studies is real, widespread, and consequential. The single/double-loop distinction explains what the simulation measures: not incident counts per se, but accumulation of double-loop knowledge that changes incident probability over time. Tacit-to-explicit conversion maps to the AC stages — postmortems are the mechanism by which acquisition and assimilation produce transferable knowledge.

**Connection to my simulation:** Provides the software-engineering foundation the simulation builds on. The 1-in-5 adoption statistic motivates why comparing sharing strategies matters — most organizations do not do this well. The single/double-loop distinction explains what the simulation measures.

**Citation sentence:**
> *"Dings{\o}yr \cite{dingsoyr2005} documents that only one in five software projects receives a post-project review, and no organization in a 19-company European study expressed satisfaction with its postmortem process --- empirically grounding the gap our simulation addresses."*

**What it does NOT claim:**
- 2005 paper — predates modern DevOps/SRE postmortem culture; Reed (2019) and Lunney & Lueder (2016) are more current
- Survey and case study evidence, not controlled experiment — use for motivation and framing
- Does not measure learning outcomes — describes practices, not their effects
- Three postmortem methods are for project retrospectives, not operational incident postmortems — acknowledge scope difference

---

### 23. Sargent (2020) — Verification and Validation of Simulation Models: An Advanced Tutorial

**Journal/Source:** Proceedings of the Winter Simulation Conference (WSC), 16–29
**Bib key:** `sargent2020`

**Raw notes:**
- Validity is purpose-relative — a model is valid for its intended use, not in the abstract
- Parsimonious model is always preferred — as simple as possible while meeting purpose
- Exploratory models require less demanding validity standards than operational decision-making models
- Four V&V activities: (1) conceptual model validity, (2) computerized model verification, (3) operational validity, (4) data validity

**Summary:** Establishes that simulation validity is purpose-relative rather than absolute, provides a four-part V&V taxonomy every study must address, and demonstrates that exploratory models require lower accuracy standards than predictive ones.

**What I'm taking from it:** Purpose-driven validity framework protects the thesis against "how do you know your model is valid?" critique — Sargent establishes there is no universal test. Parsimony justifies every simplification (one subsystem per team, fixed team size, etc.). Operational validity for the simulation means MTTR output checked against Forsgren and incident-type distribution checked against Dogga.

**Connection to my simulation:** Maps directly to the thesis validation section. Conceptual validity through AC framework and literature grounding. Computerized verification through unit tests. Operational validity through range-checking against empirical benchmarks. Data validity through parameter grounding in literature.

**Citation sentence:**
> *"Simulation validity is assessed following Sargent's \cite{sargent2020} framework of conceptual model validity, computerized verification, and operational validity. Consistent with Sargent's principle that validity is determined relative to a model's purpose, we claim exploratory validity --- the model is designed to compare knowledge-sharing strategies under controlled conditions, not to produce calibrated predictions of real organizational MTTR."*

**What it does NOT claim:**
- Does not say exploratory simulations require no validation — they still require all four activities, just at lower accuracy thresholds
- Does not provide a formula for acceptable accuracy — must be stated explicitly per purpose
- Hypothesis testing here is not formal statistical testing against real-system data

---

### 24. Grimm et al. (2020) — The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update

**Journal/Source:** Journal of Artificial Societies and Social Simulation, 23(2), 7
**Bib key:** `grimm2020`

**Raw notes:**
- ODD (Overview, Design Concepts, Details) is the accepted standard protocol for documenting agent-based models
- Addresses five limitations of the original protocol: limited guidance, excessive document length, difficulty handling complex models, insufficient detail for reimplementation, no provisions for model rationale or evaluation
- Seven-element structure: Purpose and Patterns; Entities/State Variables/Scales; Process Overview and Scheduling; Design Concepts; Initialization; Input Data; Submodels
- ODD as "lingua franca" for simulation modeling broadly
- Both a reporting format and a workflow that forces modelers to think through every part of design
- Compact ODD summary for journal articles with full details in supplementary material
- "Patterns" as evaluation criteria — modelers must specify patterns the model should reproduce

**Summary:** ODD is the accepted standard protocol for documenting agent-based models, now in its second update. Provides a seven-element structure and serves as both a reporting format and a design checklist.

**What I'm taking from it:** Three uses. (1) The replication standard (2) ODD as a workflow that forces justification of every model component — the methodology chapter implicitly follows this structure. (3) The "Patterns" framing — the simulation's patterns to reproduce are the GLOBAL < NEIGHBOR < LOCAL < NONE ordering, K saturation by day 90 under GLOBAL, and the ba_m crossover at 3.

**Connection to my simulation:** The model has all seven ODD components implicitly. Chapter 3 can organize the methodology section around ODD's structure to signal methodological rigor. 

**Citation sentence:**
> *"Following the ODD protocol \cite{grimm2020}, which provides a standardized structure for describing agent-based models sufficient for replication, our model is described in terms of its entities, state variables, process scheduling, initialization conditions, and submodels."*

**What it does NOT claim:**
- Does not require every ABM paper to include a full ODD document — a summary is sufficient for journal articles
- ODD is a description standard, not a validation framework — cite Sargent (2020) separately for validation
- Methodological guidance, not a theoretical contribution — do not use it to justify ABM as the right method

---

### 25. Epstein (1999) — Agent-Based Computational Models and Generative Social Science

**Journal/Source:** Complexity, 4(5), 41–60
**Bib key:** `epstein1999`

**Raw notes:**
- Agent-based computational models represent a new mode of scientific explanation — "generative social science"
- Core claim: a social phenomenon is only truly explained when you can grow it from the bottom up using simple agent-level rules
- Sharp distinction between explanation and prediction: a model can explain why something happens without being able to predict when or where
- Plate tectonics explains earthquakes but cannot predict them; evolutionary theory explains species diversity but cannot predict phenotypes
- Unpredictability does not mean unexplainability
- ABM is a mature, general-purpose methodology for studying emergent social phenomena

**Summary:** Argues that agent-based computational models represent a new mode of scientific explanation — "generative social science." A phenomenon is only truly explained when it can be grown from the bottom up. Explanation and prediction are separate goals.

**What I'm taking from it:** Three uses. (1) The "if you didn't grow it, you didn't explain its emergence" framing is the methodological backbone of the thesis. (2) The explanation/prediction distinction is the answer to the synthetic-data critique — the simulation explains a mechanism, not predicts a specific organization's incident count. (3) Epstein's list of phenomena successfully modeled by ABM includes "organizational behaviors" — the work sits in that lineage.

**Connection to my simulation:** Epstein's generative framing is the philosophical backbone of the methodology. The simulation "grows" organizational reliability from 20 agents following local rules. The H1 finding (GLOBAL reduces incidents 45%) is a generated emergent outcome, not a statistical correlation.

**Citation sentence:**
> *"Epstein \cite{epstein1999} argues that emergent social phenomena are only truly explained when they can be computationally generated from simple agent-level rules: `if you didn't grow it, you didn't explain its emergence.' Organizational reliability is precisely such a phenomenon --- it emerges from thousands of learning events accumulated across teams over time, and ABM is the appropriate tool for generating and studying that emergence."*

**What it does NOT claim:**
- Does not claim ABM is superior to all other methods — it is the right tool for emergent phenomena specifically
- The explanation/prediction distinction does not mean the model cannot be validated — cite Sargent (2020) for validation
- Epstein's examples are drawn from economics, ecology, and social science — software incident application is our contribution

---

### 26. Szulanski (1996) — Exploring Internal Stickiness: Impediments to the Transfer of Best Practice within the Firm

**Journal/Source:** Strategic Management Journal, 17(S2), 27–43
**Bib key:** `szulanski1996`

**Raw notes:**
- Empirical study of 122 best-practice transfers in 8 companies
- Three biggest barriers to internal knowledge transfer are knowledge-related, not motivational
- Recipient's lack of absorptive capacity is #1 barrier (canonical weight 0.54)
- Causal ambiguity (recipient cannot determine why source's practice works) is #2 (0.34)
- Arduous relationship between source and recipient is #3 (0.33)
- Motivation barely registers (source 0.05; recipient 0.18)
- Four-stage transfer process: Initiation → Implementation → Ramp-up → Integration
- Stickiness explains inter-unit transfer failure; does NOT apply to within-unit learning

**Summary:** Empirical refutation of the conventional view that knowledge transfer fails for motivational reasons. The dominant barriers are knowledge-related: insufficient absorptive capacity, causal ambiguity, and arduous relationships. Motivation barely registers as a predictor.

**What I'm taking from it:**

1. **Lack of absorptive capacity is the #1 barrier — empirical validation of Stage 2.** Teams fail to absorb transferred knowledge because they lack prior related knowledge, not because they don't want to.

2. **Causal ambiguity is the Stage 3 (Transformation) bottleneck.** Recipients can read the postmortem but cannot determine why the source's fix worked or how it applies to their own systems. This explains NEIGHBOR's only-14% transformation rate. Note: LOCAL's 0% transformation is a separate phenomenon — under LOCAL no cross-unit transfer is attempted, so Szulanski's stickiness framework does not apply; LOCAL's failure mode is within-team absorptive limits per Cohen & Levinthal (1990).

3. **Arduous relationships explain the H4 topology finding.** Star topologies create arduous relationships by design — peripheral teams only connect through the hub. Watts–Strogatz outperforms star because regular neighbor interactions reduce relationship friction.

4. **Motivation barely matters — validates the model assumption.** The blameless-postmortem assumption is not naive optimism; even where motivation varies, knowledge barriers dominate.

5. **Four transfer stages complement Zahra & George's pipeline.** Initiation ≈ Acquisition; Implementation ≈ Assimilation; Ramp-up ≈ Transformation; Integration ≈ Exploitation. Two independent research streams converge on a multi-stage transfer process.

**Connection to my simulation:** Szulanski is the empirical anchor for three model design choices: prior knowledge influences assimilation probability, transformation is the hardest stage, and network proximity reduces transfer friction. When the committee asks "why is transformation hardest?" — Szulanski's causal-ambiguity finding (weight 0.34) is the answer. When they ask "why does topology matter?" — the arduous-relationship finding is the answer.

**Citation sentence:**
> *"Szulanski \cite{szulanski1996} empirically demonstrates that the primary barrier to internal knowledge transfer is not motivational but cognitive: causal ambiguity --- the recipient's inability to determine why the source's practice works --- is the second-strongest predictor of transfer difficulty. This grounds our model's design choice to treat Stage 3 (Transformation) as the hardest pipeline stage, gated by cosine similarity between the incoming incident's feature vector and the team's existing knowledge base."*

**What it does NOT claim:**
- Best-practice transfers broadly, not software incident postmortems specifically — domain transfer must be acknowledged via Reed (2019)
- Correlational design — cannot establish strong causality
- Survival bias: aborted transfers excluded, so difficulty may be understated
- Stickiness explains inter-unit transfer failure; does NOT apply to within-unit learning (LOCAL sharing) — for that, use Cohen & Levinthal (1990) on prior-knowledge absorptive limits

---

### 27. Hansen (1999) — The Search-Transfer Problem: The Role of Weak Ties in Sharing Knowledge across Organization Subunits

**Journal/Source:** Administrative Science Quarterly, 44(1), 82–111
**Bib key:** `hansen1999`

**Raw notes:**
- Study of 41 divisions in a large electronics/computer company
- Weak interunit ties help locate knowledge but hurt transfer of complex knowledge
- Strong ties needed for noncodified, dependent knowledge transfer
- Search and transfer are two separate problems requiring opposite solutions
- Weak ties sufficient for both when knowledge is codified and self-contained
- Postmortems are codified knowledge

**Summary:** Weak interunit ties help project teams search for and locate knowledge held by other divisions, but hurt the actual transfer of that knowledge when it is complex. Strong ties are needed to transfer complex (noncodified) knowledge; weak ties are sufficient for codified knowledge.

**What I'm taking from it:** Hansen separates the problem into two: finding who has the knowledge (search) and getting it into the recipient's head (transfer). In the simulation pipeline, Acquisition solves the search problem (GLOBAL eliminates it entirely); Transformation is the transfer problem where relationship strength matters. Postmortems are codified — they cross weak ties cleanly. The deeper structural lessons are noncodified and require closer ties — explaining why GLOBAL's transformation rate is high (89.5%) but not 100%.

**Connection to my simulation:** Hansen provides the empirical mechanism behind two findings. (1) GLOBAL outperforms LOCAL not just because more teams receive knowledge, but because postmortems are codified artifacts that transfer well across weak ties. (2) The transformation bottleneck persists even under GLOBAL because deeper cognitive work requires shared context that weak ties don't provide. The search-transfer distinction also maps cleanly onto the Acquisition vs. Transformation stage asymmetry.

**Citation sentence:**
> *"Hansen \cite{hansen1999} demonstrates empirically that weak interunit ties are sufficient for transferring codified knowledge --- knowledge that is documented and structured. Since postmortems are written artifacts specifying what failed, why, and what was changed, they constitute codified knowledge that transfers effectively across weak ties. This grounds our model's assumption that GLOBAL sharing reaches all teams productively, even those with no prior direct relationship to the incident source."*

**What it does NOT claim:**
- Studies product-development knowledge transfer, not incident postmortems — codification is the bridge; explicitly note the domain transfer
- Weak ties are not always bad — only specifically bad for noncodified, dependent knowledge
- Correlational study — project completion time as a proxy for transfer success has limitations
- Does not address sharing scope directly — studies tie strength, not broadcasting policy

---

### 28. Reagans & McEvily (2003) — Network Structure and Knowledge Transfer: The Effects of Cohesion and Range

**Journal/Source:** Administrative Science Quarterly, 48(2), 240–267
**Bib key:** `reagans2003`

**Raw notes:**
- Two structural properties independently facilitate knowledge transfer above and beyond tie strength: cohesion and range
- Cohesion (mutual connections surrounding a relationship) creates cooperative norms and reputation effects
- Range (different knowledge pools a person connects to) builds ability to transfer complex knowledge across expertise boundaries
- Optimal network combines both — they are complementary, not competing
- Codified knowledge crosses weak-tie bridges easily; tacit knowledge stays in local clusters
- Star topology fails on both dimensions; WS topology combines both — high local clustering + short average path lengths via cross-cutting bridges

**Summary:** Two structural properties — cohesion and range — independently facilitate knowledge transfer. The optimal network structure combines both. This reconciles Coleman (cohesion) and Burt (structural holes/range) as complementary rather than competing.

**What I'm taking from it:**

1. **Cohesion explains why NEIGHBOR outperforms LOCAL beyond exposure.** Dense mutual connections create cooperative norms — sharing becomes the expected behavior.

2. **Range explains GLOBAL's transformation advantage.** People who connect to diverse knowledge pools learn to frame ideas across expertise boundaries — they can make non-obvious connections.

3. **Tacit knowledge stays local; codified crosses bridges.** Postmortems are codified — they cross weak ties (GLOBAL). Deeper organizational learning that produces structural change is more tacit and requires either strong ties or network range.

4. **The optimal network combines cohesion AND range — exactly Watts–Strogatz.** Local clusters (cohesion) connected by bridging ties (range) is the textbook description of small-world. WS outperforming complete and star networks is now theoretically grounded.

5. **Star topology fails on both dimensions.** Peripheral teams have neither cohesion among themselves nor range beyond the hub. Reagans & McEvily predict poor transfer in this configuration — consistent with H4.

**Connection to my simulation:** Provides the mechanism-level explanation for three H4 findings: NEIGHBOR > LOCAL because cohesion creates cooperative norms beyond simple exposure; GLOBAL's high transformation rate because range builds cross-domain transfer ability; WS outperforms star because it combines cohesion and range — the exact combination Reagans & McEvily identify as optimal. Together with Hansen (1999), this paper completes the theoretical foundation for H4.

**Citation sentence:**
> *"Reagans \& McEvily \cite{reagans2003} demonstrate that both network cohesion --- dense mutual connections that create cooperative norms --- and network range --- ties to diverse knowledge pools --- independently facilitate knowledge transfer. The Watts--Strogatz small-world topology, which combines high local clustering with short cross-cutting path lengths, instantiates both properties simultaneously."*

**What it does NOT claim:**
- Conducted at the individual level in a single R&D firm — team-level and org-level dynamics may differ
- Cohesion and range measured at individual network level, not organizational topology level — H4 connects at the topology level, so the mapping is conceptual
- Does not address sharing policy (NONE/LOCAL/NEIGHBOR/GLOBAL) — that is our contribution
- Does not resolve whether cohesion or range is more important — both matter, weights depend on knowledge type

---

### 29. Kim, Humble, Debois & Willis (2016) — The DevOps Handbook

**Journal/Source:** IT Revolution Press (book)
**Bib key:** `kim2016`

**Raw notes:**
- Three Ways: Flow, Feedback, Continual Learning
- First Way (Flow): accelerates delivery, increases quality and throughput via faster experimentation
- Second Way (Feedback): fast feedback loops amplify failure signals and embed knowledge where needed
- Third Way (Continual Learning): generative high-trust culture transforms local discoveries into global improvements
- Organizational condition: every person works with cumulative collective experience of everyone

**Summary:** The Three Ways describe the organizational conditions under which software teams reliably learn from failures and improve over time. Flow accelerates experimentation; Feedback closes learning loops; the Third Way embeds distributed learning into normalized organizational behavior.

**What I'm taking from it:** "Transforming local discoveries into global improvements" is the practitioner statement of the thesis. Local discoveries = individual team postmortems. Global improvements = the 45% incident reduction under GLOBAL. The Second Way maps directly onto the four-stage pipeline. The First Way + H2 — Kim et al. argue that accelerating flow increases quality when paired with feedback, exactly the H2 finding. The Third Way justifies the blameless-sharing assumption as documented industry practice.

**Connection to my simulation:** Forsgren et al. (2018) gives the empirical correlation (high performers deploy more and fail less). Kim et al. give the framework that explains why — the Three Ways create the organizational conditions the simulation models. The contribution is the mechanism-level explanation for how the Third Way produces the reliability outcomes both books describe.

**Citation sentence:**
> *"Kim et al.\ \cite{kim2016} describe the Third Way of DevOps as designing systems of work that `multiply the effects of new knowledge, transforming local discoveries into global improvements' so that `regardless of where someone performs work, they do so with the cumulative and collective experience of everyone.' Our simulation operationalizes this principle directly: the four sharing scenarios test how the structural reach of the knowledge pipeline determines whether local incident discoveries remain local (NONE/LOCAL) or compound into organizational-level reliability improvements (GLOBAL)."*

**What it does NOT claim:**
- Practitioner book, not peer-reviewed empirical research — pair with Forsgren et al. (2018) for the empirical version
- The Three Ways are prescriptive principles, not a measured causal model — the simulation provides the causal mechanism
- Does not quantify the reliability benefit of global sharing — that is our contribution
- Does not address network topology or absorptive capacity theory

---

### 30. Borgatti & Foster (2003) — The Network Paradigm in Organizational Research: A Review and Typology

**Journal/Source:** Journal of Management, 29(6), 991–1013
**Bib key:** `borgatti2003`

**Raw notes:**
- Review and typology of network research in organizations
- Proposes 2×2 typology: explanatory goals (performance variation vs. homogeneity) × explanatory mechanisms (structuralist/topology vs. connectionist/flows)
- Four canonical types: structural capital, resource access, convergence, contagion
- Distinguishes structuralist (how: topology/girders) from connectionist (who/what: flows/pipes/traffic) perspectives
- Methodological emphasis: network research focuses primarily on consequences, not causes

**Summary:** A literature review and organizing typology for organizational network research. Classifies studies along two theoretical dimensions to reveal four major research traditions. The contribution is taxonomic, not mechanistic.

**What I'm taking from it:** A *positioning* citation for Ch 2, not a theoretical engine for H4. Use it to map the thesis against the four traditions — H4 fits the contagion tradition (diffusion via tie channels). The cohesion+reach claim should be attributed to Hansen (1999) and Reagans & McEvily (2003), not B&F.

**Connection to my simulation:** H4 sits in the contagion tradition. B&F's typology lets the thesis explicitly position itself in this tradition; the actual mechanistic theory comes from Hansen and Reagans & McEvily.

**Citation sentence:**
> *"Borgatti \& Foster \cite{borgatti2003} provide a typology organizing network consequences research into four types distinguished by explanatory goal (performance vs. homogeneity) and mechanism (structural topology vs. resource flow), positioning studies of how network structure shapes outcomes."*

**What it does NOT claim:**
- Does NOT propose that cohesion + reach optimize knowledge diffusion — that is Hansen (1999) and Reagans & McEvily (2003)
- Does NOT theorize how topology affects learning or incident outcomes — only classifies what theory exists
- Does NOT address network antecedents or change; focuses on consequences only

---

### 31. Levinthal (1997) — Adaptation on Rugged Landscapes

**Journal/Source:** Management Science, 43(7), 934–950
**Bib key:** `levinthal1997`

**Raw notes:**
- NK model: organizations adapt on multidimensional fitness landscapes with epistatic interactions; K controls ruggedness
- K = 0 (smooth landscape): single global optimum; organizations quickly converge via local search
- K > 0 (rugged landscape): multiple local peaks; organizations get trapped at suboptimal forms
- Local adaptation: organizations sample neighboring forms, adopt if fitness improves
- Population-level selection operates alongside organizational adaptation
- Tight attribute coupling makes organizations vulnerable to environmental shifts

**Summary:** Models how organizational *form* (strategy, structure, systems) evolves through local adaptive search on multidimensional fitness landscapes. The "rugged landscape" is a metaphor for organizational attribute interdependencies — NOT knowledge accumulation.

**What I'm taking from it:** Diminishing returns to local search on a rugged landscape — defensible parallel for H3's diminishing returns to exploitation effort. CRITICAL: cite Levinthal as an analogy for organizational adaptation under constraint, NOT as a source on knowledge accumulation. Conflating fitness with knowledge invites committee scrutiny.

**Connection to my simulation:** H3's prevention_effect sweep (0.0 → 0.5, 30% reduction with diminishing marginal returns) mirrors landscape dynamics: initial adaptations yield large gains; as local neighbors are exhausted, each additional unit of effort produces smaller returns. Levinthal legitimizes this as adaptation physics.

**Citation sentence:**
> *"Organizations engaged in local adaptation on interdependent fitness landscapes experience diminishing returns as they exhaust local improvements \cite{levinthal1997}, an adaptation analog for the marginal-gains plateau observed under the prevention\_effect sweep."*

**What it does NOT claim:**
- Does NOT model knowledge accumulation, learning curves, or epistemic development
- Fitness landscape is organizational *form* space, not *knowledge* space
- Ruggedness stems from attribute interactions, not information integration
- No claim about how organizations learn or accumulate wisdom

---

### 32. Müller, Kudic & Vermeulen (2021) — The Influence of the Structure of Technological Knowledge on Inter-Firm R&D Collaboration: An ABM Approach

**Journal/Source:** Journal of Business Research, 129, 570–579
**Bib key:** `muller2021`

**Raw notes:**
- ABM with agents = firms; knowledge as a directed network; firms discover knowledge through recombination of ancestor nodes
- Lock-in effects when knowledge network is dense and firms have limited endowments; collaboration overcomes lock-in
- Trade-off: narrow scope reduces lock-in but creates redundancy; broad scope increases redundancy but avoids lock-in
- Optimal cognitive distance between partners depends on knowledge structure
- Network endogeneity: persistent ties strengthen with successful discoveries
- 500-step simulation, logit-based partner selection

**Summary:** ABM study of how technological knowledge structure shapes inter-firm R&D collaboration. Demonstrates that collaboration becomes essential when knowledge is complex and identifies systemic failures when individual and collective interests diverge regarding research scope.

**What I'm taking from it:** Methodological precedent for ABM of knowledge diffusion in networks. The "nearly identical methodology" framing in PAPERS_TO_READ.md was overstated — the domain differs (inter-firm R&D vs. within-firm software incident learning) — but the methodological lineage is real and worth citing in Ch 2.

**Connection to my simulation:** Parallels: agents in network, knowledge sharing, network effects on outcomes. Differences: Müller et al. model inter-firm strategic R&D partnerships with explicit partner selection; this thesis focuses on within-firm postmortem sharing. Cite as positioning + methodological grounding in Ch 2.

**Citation sentence:**
> *"Agent-based simulation has proven effective for studying knowledge dynamics in organizational networks; prior work has modeled inter-firm R\&D collaboration as complex adaptive systems where knowledge structure shapes discovery and network evolution \cite{muller2021}. The present work extends this methodological tradition into the within-firm context of software-incident learning."*

**What it does NOT claim:**
- Not about software incidents — inter-firm R&D
- Does not model organizational learning from failures or postmortem processes
- Assumes rational partner selection based on technological distance, not peer recommendation or incident narrative

---

### 33. Carley (1992) — Organizational Learning and Personnel Turnover

**Journal/Source:** Organization Science, 3(1), 20–46
**Bib key:** `carley1992`

**Raw notes:**
- Treats organizational learning as accumulation of distributed knowledge across individual agents in roles within an organizational structure
- Models task as decomposable into sub-tasks performed by interdependent roles; performance depends on accumulated role-level knowledge plus the structure that integrates it
- Personnel turnover removes accumulated knowledge from the organization; replacements re-learn from scratch
- Key finding: turnover hurts learning more in complex, interdependent tasks than in simple, decomposable ones
- Uses agent-based simulation (Soar-based, the agent simulation framework Carley used in her early organizational learning work) — methodological precedent for ABM of organizational learning
- Distinguishes individual learning (an agent improving at their role) from organizational learning (the structure-mediated aggregate that survives any one individual)

**Summary:** Foundational ABM-of-organizational-learning study. Organizational knowledge is structurally distributed; the rate at which it is lost (turnover, decay) interacts with task complexity to determine net learning. Establishes the ABM tradition for modeling organizational learning as an emergent property of distributed agent-level knowledge under structural constraints — exactly the lineage this thesis builds on.

**What I'm taking from it:** Methodological precedent. Carley demonstrates ABM is the appropriate tool for studying how distributed knowledge survives organizational dynamics. Her turnover mechanism is the closest literature analog to the simulation's `knowledge_decay` parameter, and her finding that decay matters more under interdependence parallels H1 (sharing scope dominates when knowledge must move across structural boundaries).

**Connection to my simulation:** Three direct connections. (1) Carley's turnover-as-knowledge-loss is the methodological precedent for the per-tick decay parameter. (2) Her task-complexity result — distributed-knowledge organizations are more vulnerable to loss — supports the thesis framing of NEIGHBOR/GLOBAL as more resilient than LOCAL: broad sharing creates redundancy across the network. (3) Methodologically, Carley legitimizes ABM as the right tool — pair with Bonabeau (2002), Epstein (1999), and Harrison et al. (2007) when defending the methodological choice in Chapter 3.

**Citation sentence:**
> *"The agent-based modeling approach taken here builds on a tradition of simulating organizational learning as the structurally mediated accumulation of distributed agent-level knowledge \cite{carley1992,harrison2007,epstein1999}. Carley in particular demonstrates that the rate of knowledge loss interacts with task interdependence to determine net organizational performance --- a finding the present model extends from personnel turnover to incident-driven postmortem learning."*

**What it does NOT claim:**
- Not about software incidents — generic organizational task performance
- Turnover ≠ knowledge decay exactly: Carley models discrete loss; this thesis models continuous decay per tick. The mechanisms differ but the high-level result transfers
- Does not model network topology — uses task interdependence
- Carley's later work in agent-based modeling (e.g., the CONSTRUCT model developed in subsequent decades) has evolved substantially beyond the 1992 paper; cite the 1992 paper for the foundational result on knowledge loss and task interdependence, not as a description of her later methodological framework

---

### 34. Leveson (2004) — A New Accident Model for Engineering Safer Systems (STAMP)

**Journal/Source:** Safety Science, 42(4), 237–270
**Bib key:** `leveson2004`

**Raw notes:**
- STAMP = Systems-Theoretic Accident Model and Processes
- Accidents emerge from inadequate control of safety constraints in complex socio-technical systems, not from chains of individual component failures
- Contrast with chain-of-events / domino models: STAMP frames failure as control breakdown, not sequential propagation
- Hierarchical control structures: operators, management, organizational layers all contribute to systemic control failure
- Applies broadly: aerospace, medical, nuclear, software

**Summary:** STAMP reconceptualizes accidents as emergent properties of system interactions rather than chains of individual failures. Control structures enforce safety constraints; when communication, monitoring, or decision-making becomes inadequate, the system state becomes unsafe.

**What I'm taking from it:** Systems-theoretic framing for software incidents; complements Cook (1998) on complex system failure. Supports the framing that incidents are emergent and multi-causal, justifying both stochastic incident generation and the Dogga (2023) taxonomy as a modeling choice rather than an ontological claim.

**Connection to my simulation:** Ch 2 background: STAMP is the theoretical anchor for why a stochastic, taxonomy-based incident model is reasonable. Failures arise from inadequate control across system layers; the simulation captures this by treating incidents as probabilistic outputs of subsystem state and deployment activity.

**Citation sentence:**
> *"Systems-theoretic accident analysis frames complex-system failures as emergent properties of inadequate control rather than chains of component failures \cite{leveson2004,cook1998}, motivating the simulation's treatment of incidents as stochastic outcomes of subsystem state and recent activity rather than as deterministic consequences of single root causes."*

**What it does NOT claim:**
- Not specific to software — applies to aerospace, medical, nuclear
- Does not address postmortem analysis or organizational learning directly
- Requires detailed control-structure modeling per domain in its full application
- The IEEE TDSC paper "A Systems-Theoretic Approach to Safety in Software-Intensive Systems" (also 2004) is a *different* paper — use the Safety Science 42(4) citation as the canonical STAMP source

---

### 35. Allspaw (2012) — Blameless PostMortems and a Just Culture

**Journal/Source:** Etsy Code as Craft (engineering blog), May 22, 2012
**Bib key:** `allspaw2012`

**Raw notes:**
- "Just Culture": balance between accountability and learning; rejects the "Bad Apple Theory"
- "Second Stories": going beyond surface explanations to systemic vulnerabilities and situational context
- Practitioner anchor for blameless postmortem culture at Etsy
- Key mechanism: when engineers feel safe, they willingly contribute expertise to remediation
- Draws on Hollnagel: accidents occur when people believe risk is justified or danger is impossible/irrelevant
- Analogous to Edmondson's psychological safety; addresses hindsight bias and fundamental attribution error

**Summary:** Argues that treating incidents as learning opportunities rather than occasions for blame yields better safety outcomes. Just Culture distinguishes between human error, at-risk behavior, and reckless behavior. Blamelessness is not absolution — it focuses investigation on circumstances and decision-making rather than punitive attribution.

**What I'm taking from it:** Practitioner grounding for the assumption that organizations can and do conduct postmortems honestly. Bridges theory (Edmondson 1999) to real-world implementation at scale (Etsy's engineering operations).

**Connection to my simulation:** The simulation assumes agents share incident knowledge truthfully — only realistic when blameless culture exists. Allspaw provides a real-world existence proof. Cite in Ch 2 alongside Edmondson (1999) and Lunney & Lueder (2016) to support the blameless-sharing assumption.

**Citation sentence:**
> *"Industry practice at mature engineering organizations like Etsy grounds the assumption that incidents can be discussed openly through structured blameless postmortems \cite{allspaw2012}, complementing Edmondson's \cite{edmondson1999} empirical findings on psychological safety in team learning."*

**What it does NOT claim:**
- Blog post — not peer-reviewed (committee may push back; consider also citing Allspaw's Chapter 13 in *Web Operations*, O'Reilly 2010, for a peer-edited venue)
- Does NOT prove blamelessness improves reliability empirically
- Generalization beyond Etsy's context is implicit, not demonstrated
- Optimal postmortem structures or methodologies are not prescribed

---

### 36. Sujan, Huang & Braithwaite (2017) — Learning from Incidents in Health Care: Critique from a Safety-II Perspective

**Journal/Source:** Safety Science, 99, 115–121
**Bib key:** `sujan2017`

**Raw notes:**
- Safety-I: safety as the absence of negative events; learning comes from analyzing what goes wrong
- Safety-II: safety as the ability to make dynamic adjustments and trade-offs; learning comes from what goes right (everyday clinical work, successful adaptive responses)
- Incident-reporting systems (RCA, NRLS) focus narrowly on failures and struggle with effectiveness due to organizational barriers
- Healthcare can extract learning from successful uneventful operations, not just adverse events
- Hollnagel's Safety-II framework applied to healthcare-specific contexts

**Summary:** Critiques healthcare's incident-learning paradigm (Safety-I) as incomplete. Relying exclusively on incidents misses the majority of clinical knowledge generated during routine successful operations. Safety-II — learning from how clinicians adaptively manage everyday demands — would complement incident-focused systems.

**What I'm taking from it:** Frames a clean limitation for Ch 5: this thesis's ABM captures only Safety-I dynamics (learning from failures). Sujan et al. is the citation that scopes this as a deliberate choice rather than an oversight, and names Safety-II (learning from successful adaptive operations) as a natural future-work extension.

**Connection to my simulation:** Ch 5 limitations: the ABM models organizational learning exclusively from incidents. A Safety-II extension would incorporate learning from successful uneventful operations (e.g., near-miss recovery) — expanding learning feedback loops beyond failure-driven improvement.

**Citation sentence:**
> *"This work models Safety-I learning dynamics, in which knowledge accumulation is driven exclusively by incidents. The Safety-II perspective \cite{sujan2017} suggests a natural future-work extension: capturing learning from successful adaptive operations and near-miss recoveries, which the present model does not represent."*

**What it does NOT claim:**
- Not about software incidents — about healthcare
- Does not invalidate incident reporting or root-cause analysis — argues for *complementing* it
- Not a replacement for Safety-I but a complementary framework
- Empirical findings (barriers to incident learning) are healthcare-specific; software-engineering transfer is interpretive

---