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
> *"Cook observes that complex systems always operate with latent failures present, and that post-accident attributions of 'root cause' reflect a social and cultural need to assign blame rather than a technical understanding of failure \cite{cook1998}. Our incident taxonomy follows Dogga et al.\ \cite{dogga2023} as a practical modeling simplification, not a claim that single root causes exist."*

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
> *"Simulation enables controlled experiments impossible in real organizations and, as Harrison et al.\ document in their methodological review of organizational simulation, can generate hypotheses that are integrated and consistent \cite{harrison2007} --- precisely the contribution we aim for in comparing knowledge-sharing strategies."*

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
> *"We use agent-based modeling because organization-wide reliability is an emergent phenomenon arising from team interactions and cannot be captured by aggregate equations \cite{bonabeau2002}. ABM is most appropriate when individual behavior is heterogeneous, nonlinear, and stochastic — all three of which characterize our learning model: each team has a distinct knowledge state and network position, stage transitions are gated probabilistically, and incident generation is stochastic."*

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
> *"Organizational networks are modeled using three topologies: random, small-world, and scale-free. The small-world topology follows Watts \& Strogatz \cite{watts1998}, who demonstrate across diverse real-world networks --- film actor collaborations, the western US power grid, and the C.\ elegans neural network --- that high local clustering combined with short global path lengths significantly accelerates information propagation relative to regular lattices. We adopt this topology to model organizational communication networks, extending the structural property from Watts \& Strogatz's original domains."*

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

**Connection to my simulation:** Scale-free is one of five canonical topologies tested in H4 (alongside complete, random/Erdős-Rényi, small-world, and star). It models mature large organizations where a few platform/infrastructure teams accumulate connections that feature teams don't, via the preferential-attachment dynamic ("rich get richer"). The H4 BA crossover finding (`ba_m = 3` is where BA begins to beat the small-world baseline) is a result about model behavior under different connectivity levels, not a claim about empirical organizational structure.

**Citation sentence:**
> *"Scale-free topology is included as one of five canonical network shapes tested in H4. We model it following Barab\'asi \& Albert \cite{barabasi1999}, who show that preferential attachment --- new nodes connecting preferentially to already well-connected nodes --- produces a small number of highly connected hubs across real-world networks. This captures a structural pattern observed in mature large software organizations: platform and infrastructure teams accumulate cross-team connections that feature teams do not, as new teams preferentially route through established hubs for shared services. We do not claim real organizations are perfectly scale-free; we use the BA topology as one canonical hub-and-spoke shape for systematic comparison."*

**What it does NOT claim:**
- Does not address organizations or knowledge sharing directly — application to software teams is our interpretation
- Does not claim scale-free is better or worse than other topologies — that is what H4 tests
- Detailed power-law mathematics does not require citation in the thesis
- Does NOT establish that real organizations are exactly scale-free — Broido & Clauset (2019, *Nature Communications*) show many real-world networks claimed to be scale-free are only partially so or fit other distributions equally well. We use BA as one of five tested shapes, not as a claim about empirical network structure.

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

**What I'm taking from it:** Three distinct claims that each apply to a specific part of the simulation:

1. **The three-part definition (recognize → assimilate → apply)** maps to stages 1–3 of the four-stage model. This is the foundation that Zahra & George (2002) later extended into four stages.

2. **Path dependence and lockout** predict that the H1 performance gap should *widen* over time, not converge. Organizations that absorb knowledge early build more capacity, which lets them absorb more — a self-reinforcing process. Organizations that fall behind eventually lose the ability to recognize relevant patterns. This matches both the simulation's H1 finding (GLOBAL pulls further ahead each year) and Forsgren's empirical DORA finding (high/low performer gap widens).

3. **Boundary-spanning individuals** — people who connect their team to outside knowledge — provide the theoretical justification for small-world shortcuts. In Watts–Strogatz topology, the long-range bridges that connect distant clusters are conceptually identical to senior engineers, principal architects, or platform-team leads who bridge product areas. Cohen & Levinthal explain *why* small-world structure works in real organizations: there are real human roles that act as long-range bridges.

**Connection to my simulation:** Cohen & Levinthal provide the theoretical foundation for the upstream half of the learning pipeline (recognition, assimilation). They also explain why **LOCAL produces 0% transformation rate** — a within-team absorptive-limits story, not an inter-unit transfer story:

- A team that only sees its own incidents develops a narrow knowledge vector biased toward its own subsystem.
- Transformation requires high cosine similarity between the team's knowledge vector and an incident's feature vector — but a narrow vector cannot recognize cross-domain patterns.
- The result: LOCAL teams have prior knowledge too narrow to support broader transformation. This is Cohen & Levinthal's mechanism (prior knowledge gates absorption).

This is distinct from Szulanski's (1996) framework, which explains why *inter-unit* transfer fails when transfer is attempted (causal ambiguity, arduous relationships). Szulanski applies to NEIGHBOR's 14% transformation rate — transfer happens, but is impeded by causal ambiguity. Szulanski does NOT apply to LOCAL because no inter-unit transfer is attempted at all. The two papers explain different failure modes:

| Mechanism | Framework | Where it applies |
|---|---|---|
| Within-team narrow knowledge → can't transform | Cohen & Levinthal (1990) | LOCAL — 0% transformation |
| Inter-unit transfer attempted, fails due to causal ambiguity | Szulanski (1996) | NEIGHBOR — 14% transformation |

**Citation sentence:**
> *"Our learning model builds on Cohen \& Levinthal's \cite{cohen1990} foundational definition of absorptive capacity: the ability to recognize the value of new external information, assimilate it, and apply it to productive ends --- a capacity determined by prior related knowledge and subject to path dependence. Cohen \& Levinthal also explain why narrow exposure produces narrow absorption: a unit that sees only its own experience develops prior knowledge too limited to recognize cross-domain patterns. This is the within-team mechanism behind LOCAL sharing's $0\%$ transformation rate in our simulation, and is distinct from the inter-unit transfer-failure mechanism described by Szulanski \cite{szulanski1996}, which applies to NEIGHBOR sharing. The specific four-stage operationalization (acquisition, assimilation, transformation, exploitation) follows Zahra \& George \cite{zahra2002}."*

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

**What I'm taking from it:** Three interlocking ideas that anchor the simulation:

1. **The four-stage model** (acquisition → assimilation → transformation → exploitation) is the direct theoretical specification for agent learning. Each agent progresses through these stages when processing a postmortem.

2. **The PACAP/RACAP split** explains organizational failure modes that pure-acquisition models miss. PACAP (acquisition + assimilation) captures whether knowledge is *received*; RACAP (transformation + exploitation) captures whether it *changes behavior*. A team can have high PACAP and low RACAP — receiving postmortems but never acting on them. The efficiency factor (RACAP/PACAP ratio) measures what fraction of acquired knowledge becomes operational improvement.

3. **Proposition 4** is the theoretical bridge that justifies H1. Z&G propose that *social integration mechanisms* — cross-team interactions, communication norms, shared practices — reduce the gap between PACAP and RACAP. **Postmortem sharing is itself a social integration mechanism**: when Team A's postmortem reaches Team B, the act of reading and discussing it creates cross-team interaction. Therefore, broader sharing scope produces more social integration, which (per Proposition 4) increases the efficiency factor, which produces more behavior change and better outcomes. This is the theoretical prediction; H1 confirms it empirically (45% reduction, d = 11.51).

**Connection to my simulation:** Zahra & George operationalize Cohen & Levinthal's earlier framework. The four stages become the agent state machine. The PACAP/RACAP distinction is what the simulation makes visible: a team can have high Prevention K (high PACAP, knowledge accumulated) but low transformation rate (low RACAP, knowledge not converted to behavior change). The four sharing strategies systematically vary social integration intensity:

| Strategy | Cross-team interaction | Predicted efficiency factor |
|---|---|---|
| NONE | Zero | Undefined (PACAP also zero) |
| LOCAL | Within-team only | Low — narrow conversion |
| NEIGHBOR | Adjacent teams interact | Medium |
| GLOBAL | All teams interact across organization | High |

The H1 ordering (NONE > LOCAL > NEIGHBOR > GLOBAL in incident counts) follows the social-integration ordering, which is exactly what Proposition 4 predicts.

**Citation sentence:**
> *"Agent learning follows the four-stage absorptive capacity framework of Zahra \& George \cite{zahra2002}: acquisition of incident knowledge from postmortems, assimilation through team analysis, transformation by combining new and existing knowledge, and exploitation through updated operational practices. Zahra \& George further distinguish potential absorptive capacity (PACAP --- acquisition and assimilation) from realized absorptive capacity (RACAP --- transformation and exploitation), with the gap between them governed by an efficiency factor that social integration mechanisms increase (their Proposition 4). Postmortem sharing is itself a social integration mechanism: each cross-team postmortem creates an interaction supporting knowledge flow. Broader sharing scope therefore produces higher social integration, which raises the efficiency factor and increases conversion of acquired knowledge into operational improvement --- the theoretical prediction that H1 confirms with a 45\% incident reduction (Cohen's $d = 11.51$)."*

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

**What I'm taking from it:** Two specific concepts from March that DO apply to this thesis (and one common misuse to avoid):

1. **The competency trap.** Organizations focused narrowly on existing knowledge develop deep expertise in their current domain but lose the ability to recognize new patterns or alternatives. This is March's most-cited concept after the exploration/exploitation framing itself.

2. **The value of heterogeneity.** March's mutual-learning model shows that heterogeneous populations — including slower-learning individuals — produce better long-run organizational knowledge than homogeneous fast-learning populations. The mechanism: diversity prevents premature convergence on existing beliefs, including errors.

**Important: do NOT map sharing strategies onto exploration/exploitation directly.** All four scenarios (NONE/LOCAL/NEIGHBOR/GLOBAL) involve the same kind of learning — reactive, incident-driven refinement of existing knowledge. They differ in *scope* of exposure, not in whether they are exploration vs. exploitation. None of the four scenarios involves March's strict notion of exploration (search, experimentation, risk-taking, discovery). All four are variants of exploitation-with-different-scope.

**Connection to my simulation:** March's framework illuminates two specific aspects of the H1 result:

1. **LOCAL exhibits the competency trap.** A team that only sees its own incidents develops deep expertise on its own subsystem but cannot recognize cross-domain patterns. This produces the 0% transformation rate observed under LOCAL — not because transfer fails (Szulanski's mechanism), but because the team's narrow exposure prevents it from developing the diverse prior knowledge needed for cross-domain pattern recognition. GLOBAL sharing breaks this trap by exposing teams to incidents from other subsystems.

2. **The δ decay parameter preserves heterogeneity.** Under GLOBAL with no decay, all teams converge to the same knowledge state (Prevention K → 0.992 across all teams). Under GLOBAL with decay, teams retain slight differences because forgetting operates independently per team. This is exactly what March's mutual-learning model predicts: moderate noise in the learning system (slow learners in his model; knowledge decay in mine) preserves the cognitive diversity that prevents premature convergence and improves long-run organizational outcomes.

**Citation sentence:**
> *"March \cite{march1991} identifies the competency trap: organizations focused narrowly on existing knowledge develop deep expertise in their current domain but lose the ability to recognize new patterns or alternatives. This applies directly to LOCAL sharing in our simulation, where teams that see only their own incidents develop narrow knowledge vectors and produce 0\% transformation rate, unable to recognize patterns from other teams' systems. March's mutual-learning analysis also predicts that moderate heterogeneity in the learning system --- what he calls the value of slower learners --- produces better long-run outcomes than rapid homogenization. The knowledge decay parameter $\delta$ in our model acts as a heterogeneity-preserving mechanism: even under GLOBAL sharing, teams retain slight knowledge-state differences because decay operates independently per team."*

**What it does NOT claim:**
- Does NOT support mapping sharing strategies onto exploration vs. exploitation directly. All four scenarios are variants of exploitation; March's exploration concept (search, experimentation, risk-taking) does not apply to any of them.
- Does not address software incidents, postmortems, or engineering organizations directly
- Mutual-learning model is formal simulation, not empirical data — use as theoretical support, not empirical evidence
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

**Connection to my simulation:** This is the **theoretical umbrella** that organizes every other organizational-learning citation in the bibliography. The three subprocesses subsume the more specific frameworks:

| Subprocess | Specific framework used in this thesis |
|---|---|
| **Creation** | Held constant — every incident produces a postmortem |
| **Retention** | Modeled via knowledge decay parameter δ; empirical grounding from Darr, Argote & Epple (1995) |
| **Transfer** | Operationalized via the four-stage absorptive capacity pipeline (Cohen & Levinthal 1990; Zahra & George 2002); failure modes explained by Szulanski (1996) for inter-unit transfer and by Cohen & Levinthal for within-unit narrow knowledge |

The active/latent context distinction also frames what the simulation does and does NOT capture:
- **Active context** (members, tools, tasks, networks) is explicitly modeled — teams, incidents, knowledge state, communication network
- **Latent context** (culture, identity, structure, psychological safety) is held constant — blameless culture and fixed organizational structure are assumed

This is a deliberate scope choice (not a limitation), because varying both at once would confound the variable being tested (transfer scope). The limitations chapter cites Argote & Miron-Spektor explicitly to acknowledge what is held constant.

**Citation sentence:**
> *"This work follows Argote and Miron-Spektor's \cite{argote2011} synthesis of organizational learning research, which identifies three subprocesses: creation, retention, and transfer. We focus on the transfer subprocess: incident knowledge is created when an incident occurs, retention is modeled through a decay parameter $\delta$ (grounded empirically in \cite{darr1995}), and transfer is what we systematically vary through the four sharing scopes operationalized via the absorptive capacity pipeline (\cite{cohen1990,zahra2002}). Argote and Miron-Spektor's distinction between active context (members, tools, tasks, networks) and latent context (culture, identity, structure, psychological safety) further frames our scope: we explicitly model active context while holding latent context constant, in order to isolate the effect of transfer mechanism on organizational reliability."*

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

**What I'm taking from it:** The theoretical justification for the **Stage 3 (Transformation) cosine-similarity gate**. Nooteboom et al. document that absorptive capacity declines as cognitive distance between source and recipient increases. The simulation operationalizes this by gating Stage 3 on cosine similarity between two knowledge vectors — the source's incident-feature vector and the recipient's accumulated knowledge vector. High similarity → transformation likely; low similarity → transformation fails. Distance reduces successful transfer.

**IMPORTANT — what the simulation does NOT capture:** Nooteboom's full inverted-U has *two* opposing forces:
1. **Absorptive capacity decreases with cognitive distance** — distant partners are harder to understand. (✅ Modeled via Stage 3 cosine-similarity gate.)
2. **Novelty value increases with cognitive distance** — distant partners bring genuinely new ideas you couldn't have generated yourself. (❌ NOT modeled. Distant incidents receive no informational "novelty bonus" in our model.)

Because we only model the first force, distance is purely a cost in our simulation, not a benefit. We do **not** test Nooteboom's full inverted-U; we test only the downward half. This is a deliberate scope choice: we focus on the dominant transfer-failure mechanism (causal ambiguity, narrow absorption) rather than the diversity-benefit mechanism. The implication is that our model may overstate GLOBAL's marginal benefit in regimes where novelty value would matter — flagged in the limitations chapter and identified as future work.

**Connection to my simulation:** Cognitive distance between firms in Nooteboom's data maps conceptually to knowledge-vector distance between teams in our model. The Stage 3 cosine-similarity gate is the operational implementation of "absorptive capacity declines with distance." We do *not* claim our simulation reproduces Nooteboom's empirical inverted-U — only the downward leg of it. GLOBAL dominating NEIGHBOR in our H1 results is consistent with this partial modeling: with no novelty bonus for distance, broader sharing is purely beneficial.

**Citation sentence:**
> *"The Stage 3 (Transformation) cosine-similarity gate in our simulation operationalizes one half of Nooteboom et al.'s \cite{nooteboom2007} empirical finding: absorptive capacity declines as cognitive distance between source and recipient increases, so a recipient team with a knowledge vector dissimilar to an incident's feature vector cannot integrate that incident as effectively as a more similar team. Nooteboom et al.\ document a full inverted-U in which distance also increases novelty value; we do not model this second force, focusing instead on the dominant transfer-failure mechanism. This scope choice is acknowledged in the limitations chapter, and a fully bidirectional cognitive-distance model is identified as future work."*

**What it does NOT claim:**
- The simulation does NOT test Nooteboom's full inverted-U — only the downward (absorption-decreases-with-distance) half. Any prediction that NEIGHBOR should outperform GLOBAL on Nooteboom-like grounds is NOT supported by the simulation.
- R&D alliances between large industrial firms — not software engineering teams; domain transfer is extrapolation
- Cognitive distance is measured via patent portfolios in Nooteboom — a proxy unavailable in software incident contexts; knowledge-vector cosine similarity is the analogous construct
- Does not model sharing strategies directly — studies alliance partner selection
- Boredom hypothesis (firms with more R&D capital get less novelty from distant partners) is not modeled in the simulation

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

**Connection to my simulation:** Dekker grounds the systemic view of incidents the simulation assumes. The model never "blames" an agent; it tracks systemic patterns. Dekker's warning about blame driving reporting underground explains the *mechanism* behind why blame-oriented organizations suppress the data that makes learning possible — but Dekker is one corner of a citation triangle, not the sole support for the honest-sharing assumption:

| Citation | What it provides |
|---|---|
| Dekker (2014) | Theoretical lens (New View) + mechanism (blame → reporting underground) |
| Edmondson (1999) | Empirical anchor (51 work teams; psychological safety predicts learning behavior) |
| Allspaw (2012) + Lunney & Lueder (2016) | Practitioner anchor (real organizations operationalize blameless culture at scale) |

**Citation sentence:**
> *"Consistent with Dekker's New View of human error \cite{dekker2014}, our simulation treats incidents as systemic outcomes rather than individual failures --- the incident generation process reflects team-level knowledge gaps, not agent-level incompetence. Dekker's synthesis of the safety-science literature also argues that blame-oriented responses drive incident reporting underground, eliminating the information flow that postmortem-based learning requires; this argument is empirically supported by Edmondson's \cite{edmondson1999} work on psychological safety in teams and operationally demonstrated by industry practice (\cite{allspaw2012,lunney2016}). Together these literatures ground our assumption of honest knowledge sharing as a property of organizations that have moved past Old View blame culture."*

**What it does NOT claim:**
- Primary context is safety-critical industries (aviation, healthcare, nuclear) — software incident transfer must be acknowledged
- Does not provide *new* empirical data — Dekker's book is a prescriptive synthesis of existing safety research; the empirical claim that "blame drives reporting underground" comes from research Dekker integrates (Reason's just-culture work, hospital safety studies, aviation incident reporting research), not from Dekker's own measurement
- Source is the book (3rd edition, 2014), not the derivative training presentations widely circulated online
- Dekker alone does not justify the honest-sharing assumption — Edmondson (1999) provides the empirical anchor and Allspaw / Lunney & Lueder provide the practitioner anchor

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

**Summary:** Systematic literature review of 47 safety-science papers on Learning from Incidents (LFI). Identifies the sharing-and-storing sub-process as the most consistently neglected stage of incident learning across chemical, nuclear, aviation, and healthcare contexts. Uses Argyris & Schön (1978) as its theoretical lens — single-loop vs. double-loop learning — *not* Cohen & Levinthal or Zahra & George. The gap they document can be re-framed in PACAP/RACAP terms, but that re-framing is the present author's interpretive bridge, not Drupsteen & Guldenmund's own language.

**What I'm taking from it:** Two distinct uses, kept separate so each is honestly grounded:

1. **Empirical motivation that the gap is real.** Their headline finding — *"the potential level of learning was considerably higher than the actual level of learning"* — documents across 47 studies that organizations identify lessons but fail to share them broadly enough to produce real improvement. This is the gap the thesis isolates and varies systematically.

2. **Trust and openness as a prerequisite.** Drupsteen & Guldenmund identify trust and openness as preconditions for LFI — without them, incidents go underreported and the analysis sub-process never starts. This adds a fourth corner to the citation triangle supporting the honest-sharing assumption: Dekker (theoretical lens) + Edmondson 1999 (empirical anchor) + Allspaw 2012 / Lunney & Lueder 2016 (practitioner anchor) + Drupsteen & Guldenmund 2014 (safety-science synthesis).

**Connection to my simulation:** Drupsteen & Guldenmund provide the safety-science version of the empirical motivation. Their three-process framework (analyzing → using → sharing/storing) **approximately maps** onto the simulation's pipeline but is not isomorphic:
- Their *analyzing* corresponds to incident generation + postmortem creation in the simulation (work done at the source team before sharing)
- Their *sharing and storing* corresponds to the four sharing strategies (which determine the *scope* of dissemination)
- Their *using* corresponds to assimilation + transformation + exploitation in the four-stage pipeline (work done at the recipient team after acquisition)

Note that Drupsteen & Guldenmund's temporal ordering (analyze → use → share) is incomplete: in real organizations and in this simulation, sharing must happen *between* analyzing and using when the using team is different from the analyzing team. The mapping is conceptual, not exact.

The central use is motivation: their identification of sharing as the consistently neglected sub-process is what justifies systematically varying sharing scope in the experimental design.

**Citation sentence:**
> *"Drupsteen and Guldenmund's \cite{drupsteen2014} systematic review of 47 safety-science papers identifies sharing and storing lessons as the most consistently neglected sub-process of organizational learning from incidents, documenting that 'the potential level of learning was considerably higher than the actual level of learning' across chemical, nuclear, aviation, and healthcare industries. We re-frame this finding using Zahra and George's potential-versus-realized absorptive capacity terminology, since the structural gap they document maps onto the PACAP/RACAP distinction --- although Drupsteen and Guldenmund themselves work within the Argyris and Schön (1978) single-loop / double-loop framework. Their empirical observation motivates the central design of the thesis: by varying sharing scope systematically through four conditions, we isolate the very sub-process that prior empirical work identifies as the binding constraint."*

**What it does NOT claim:**
- Safety-critical industries (chemical, nuclear, aviation, healthcare) — not software engineering specifically. Domain transfer is acknowledged via Reed (2019) and Dingsøyr (2005), which document analogous gaps in software-engineering contexts.
- Literature review, not new empirical measurement — use for framing and motivation, not for causal claims about postmortem-effectiveness.
- Does not quantify the sharing gap — qualitative synthesis across 47 studies; no effect size or statistical claim.
- **The PACAP/RACAP re-framing is the present author's interpretive bridge, not Drupsteen and Guldenmund's terminology.** They use Argyris & Schön (1978). The structural gap they document is conceptually equivalent to PACAP/RACAP, but the linguistic translation is acknowledged as interpretation.
- The three-process framework (analyzing → using → sharing/storing) is *approximately* aligned with the four-stage absorptive capacity pipeline, not isomorphic. Drupsteen & Guldenmund's temporal ordering is also incomplete for cross-team learning, since sharing must occur between analyzing and using when those happen in different teams.

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

**Summary:** **Research-agenda paper** (not a systematic literature review) published in *Safety Science*'s 2017 special issue on Learning from Incidents. Synthesizes prior work to identify gaps and propose research directions across four R&D challenges. Calls for a unified research program crossing safety science, organizational learning, and human factors. Specifically identifies simulation as an underused but appropriate method given the multi-level emergent nature of LFI, and critiques the field's over-reliance on process proxies rather than outcome measures.

**What I'm taking from it:** Two distinct uses, each precisely scoped:

1. **Domain-specific endorsement of simulation for LFI research.** This is the strongest single contribution. M&L&S — safety-science researchers writing in *Safety Science* — explicitly call simulation an appropriate method for studying LFI. This complements the general-methodology citations (Bonabeau, Harrison et al., Epstein, Carley) by providing *domain-specific* legitimacy: the LFI field itself is asking for the kind of research this thesis conducts.

2. **The outcome-vs-process measurement critique.** M&L&S argue that LFI research has over-relied on process proxies (did a postmortem happen?) rather than outcome measures (did incident rates change?). The simulation measures outcomes directly — incident frequency, MTTR, transformation rate — addressing a field-identified gap.

**Connection to my simulation:** M&L&S provide the domain-specific layer of the methodology defense. Where Bonabeau and Epstein justify ABM as a general method, M&L&S justify it specifically for LFI. The agent-based model directly responds to two of their identified gaps: (a) the methodological gap (simulation underused), and (b) the measurement gap (outcomes not measured directly).

**Note on the multi-level claim:** M&L&S identify LFI as operating at multiple levels — individual, team, organizational, and inter-organizational. This simulation does NOT capture the full range. It operates at the team level (each agent is a team, not an individual) and the network level (teams interact via the communication graph), with organizational outcomes as aggregate metrics. Individual-level dynamics (how single engineers learn) and inter-organizational learning (cross-company knowledge flows) are out of scope. This is a deliberate boundary, not a fix M&L&S would endorse — the model addresses the team-and-network slice of the multi-level challenge, not the entire range.

**Citation sentence:**
> *"Margaryan, Littlejohn, and Stanton's \cite{margaryan2017} research-agenda paper in \emph{Safety Science} identifies simulation as an underused but appropriate method for Learning from Incidents research, citing the multi-level, emergent nature of organizational learning that makes controlled field experiments infeasible. They also critique the field's over-reliance on process proxies (did a postmortem happen?) rather than outcome measures (did incident rates change?). The agent-based model presented here directly responds to both gaps: simulation enables controlled comparison of sharing strategies, and the model measures outcomes (incident frequency, MTTR, transformation rates) rather than process proxies. M\&L\&S provide domain-specific methodological legitimacy that complements the general ABM justifications in Bonabeau \cite{bonabeau2002}, Epstein \cite{epstein1999}, Harrison et al. \cite{harrison2007}, and Carley \cite{carley1992}."*

**What it does NOT claim:**
- **Research-agenda paper, not a systematic review.** Authority is "the field calls for X" not "across N studies, the literature shows X." Use for framing methodology, not for empirical claims about LFI prevalence.
- Does not validate any specific sharing strategy or AC model — maps the problem space, doesn't fill it.
- The simulation does NOT capture all four levels M&L&S identify. It operates at the team and network levels; individual-level and inter-organizational-level dynamics are out of scope. Acknowledge as a deliberate boundary.
- Primary context is aviation/nuclear/chemical/healthcare safety industries — software engineering transfer is extrapolation, supported by Reed (2019) and Dingsøyr (2005).
- M&L&S call for *simulation* generally, not ABM specifically. ABM-specific justification still comes from Bonabeau, Epstein, Harrison et al., and Carley.

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

**Summary:** Foundational multi-method empirical study (51 work teams in one office-furniture manufacturer) using surveys, qualitative interviews, hierarchical linear modeling, and mediation analysis. Demonstrates that psychological safety — a shared team-level belief that interpersonal risk-taking is safe — is the strongest predictor of team learning behavior, with the relationship to team performance fully mediated through learning behavior.

**What I'm taking from it:** Edmondson is the **empirical anchor** of the honest-sharing citation triangle. Three specific contributions, each grounded in the paper's empirical evidence:

1. **The team-level-property argument.** Edmondson demonstrates statistically (intraclass correlation of 0.39, p < 0.0001) that psychological safety is a real team-level construct, not just averaged individual feelings. 39% of variance is explained by team membership. This directly justifies the simulation's modeling choice: each agent is a team, not an individual. Working at the team level isn't an arbitrary simplification — it is the empirically appropriate level of analysis for psychological-safety dynamics.

2. **The interpersonal-threat mechanism.** Edmondson identifies why psychological safety matters: people who fear being seen as ignorant, incompetent, negative, or disruptive will not ask questions, admit errors, seek feedback, or discuss problems. When psychological safety is high, this fear dissolves and learning behavior becomes possible. This is the mechanism behind why blameless culture matters in postmortem practice.

3. **The mediation argument.** Psychological safety → learning behavior → team performance. Mediation analysis showed learning behavior fully mediates the relationship. This matters methodologically: psychological safety doesn't directly cause performance — it causes learning behavior, which causes performance. The simulation's pipeline structure (knowledge acquisition → assimilation → transformation → exploitation → outcome) is consistent with this mediation logic.

**Connection to my simulation:** The simulation assumes teams share incident knowledge openly — encoding the conditions for psychological safety as given. Edmondson provides the **empirical layer** of a four-citation triangle: Dekker (theoretical lens), Allspaw and Lunney & Lueder (practitioner anchors), Drupsteen & Guldenmund (safety-science synthesis), and Edmondson (peer-reviewed empirical evidence). Without Edmondson, the rest is theory and practitioner anecdote. With Edmondson, the assumption is grounded in measured, replicated empirical research.

The simulation models what happens *after* psychological safety conditions hold — that is, in organizations capable of conducting structured postmortems honestly. The research question is what happens *after teams share*, not whether they share at all. Edmondson resolves the latter empirically; the simulation explores the former.

**Citation sentence:**
> *"Our simulation assumes teams share incident knowledge openly. This assumption is grounded empirically in Edmondson's \cite{edmondson1999} foundational study in \emph{Administrative Science Quarterly}, which uses multi-method analysis (surveys, interviews, and hierarchical linear modeling across 51 work teams) to demonstrate that psychological safety --- a shared team-level belief that interpersonal risk-taking is safe --- is the strongest predictor of team learning behavior, including error reporting, feedback seeking, and problem discussion. Edmondson statistically establishes psychological safety as a team-level property (intraclass correlation 0.39, p < 0.0001), which directly justifies the team-level modeling choice in this simulation. The mediation analysis further shows that psychological safety affects performance \emph{through} learning behavior, consistent with the four-stage pipeline structure used here."*

**What it does NOT claim:**
- Single industry (office-furniture manufacturer) — not software engineering. Domain transfer is supported by the broader replication record (see below) rather than by Edmondson's data alone.
- Cross-sectional design — establishes statistical association between psychological safety and learning behavior, not causation. Edmondson's theoretical reasoning supports the proposed direction; the data alone could in principle be reversed.
- Self-report survey data — measures perceptions of psychological safety and learning behavior, not directly observed behavior. This is standard in organizational research but worth acknowledging.
- Psychological safety is *not* the same as group cohesiveness, team efficacy, or trust in leadership — Edmondson explicitly distinguishes these constructs and shows psychological safety has independent predictive power above each of them.
- The 1999 paper is the foundational empirical study, not the only one. The finding has been extensively replicated and extended: Newman, Donohue & Eva (2017) meta-analyze the psychological-safety literature; Edmondson's 2019 book *The Fearless Organization* extends to a popular audience; Google's Project Aristotle (2015) operationalized psychological safety as the strongest predictor of team effectiveness across thousands of Google teams. The 1999 finding is robust, not isolated.

---

### 21. Reed (2019) — Beyond the `Fix-It' Treadmill: The Use of Post-Incident Artifacts in High-Performing Organizations

**Journal/Source:** ACM Queue, 17(6), 27–46
**Bib key:** `reed2019`

**Provenance worth knowing:** Reed's MSc is from Lund University under **Sidney Dekker** (Entry 17 author). This positions Reed as the **software-industry extension of Dekker's resilience-engineering / Safety-II framework**, not just an unrelated practitioner. The intellectual chain is Dekker → Reed → modern software industry practice (Allspaw, Lunney & Lueder).

**Raw notes:**
- Most organizations treat postmortems as source of static remediation items — "fix-it treadmill": incident → postmortem → fix list → repeat
- High-performing organizations use post-incident artifacts to share rich context and update mental maps of complex socio-technical systems
- Reed reports that **91% of organizations in his interview sample** consider remediation-item collection the core purpose of postmortems (this is from his own qualitative research, not a broader industry survey)
- Three phases of organizational learning: (1) what happened (analysis), (2) why did it happen (sense-making), (3) what does it mean (meaning-making / mental-map updates) — most organizations stop at phase 1
- Post-incident artifacts as "patches" to engineers' mental maps
- Three postmortem archetypes: Record-keeper (most common, documents but doesn't drive learning), Facilitator (adds prompts and cultural reminders), Signpost (lightweight pointer to data sources)
- Blamelessness emerges from process structure, not from declarations

**Summary:** Multi-case qualitative research at high-performing software organizations (Salesforce, Etsy, Netflix, Slack, and others appear across Reed's work) published as a practitioner article in ACM Queue. Observes that high-performing organizations use post-incident artifacts to share context and update mental maps of complex systems — moving from tactical accountability to strategic understanding — rather than merely to generate remediation lists. Reed brings Dekker's resilience-engineering framework into the software domain.

**What I'm taking from it:** Reed is the **software-industry bridge** in the citation chain. Where Dekker provides the theoretical lens (Safety-II / New View) and Allspaw + Lunney & Lueder provide pure practitioner descriptions of specific organizations, Reed sits between them: practitioner-researcher with academic training, applying Dekker's framework specifically to software-engineering postmortem practice. Three contributions to the thesis:

1. **Postmortems as knowledge-transfer artifacts.** Reed's central observation is that high-performing organizations use post-incident artifacts primarily to share context and update engineers' mental maps of complex socio-technical systems — not just to produce fix lists. This is the qualitative phenomenon the simulation operationalizes as knowledge-transfer events with stage-by-stage probability gates.

2. **The fix-it treadmill failure mode.** Organizations stuck producing remediation lists without deeper sense-making are exactly what NONE and LOCAL strategies model in the simulation: knowledge stays narrow and tactical, no broader pattern recognition develops, transformation rates stay near zero.

3. **The three postmortem archetypes** (Record-keeper, Facilitator, Signpost) describe real variation in postmortem process and document that most organizations operate at the lowest learning level. This frames the practitioner relevance of varying sharing strategies.

**Connection to my simulation:** Reed's "mental-map patching" is a *conceptual analog* of the simulation's Stage 3 (Transformation) mechanism, not an isomorphic mapping. Reed describes the qualitative phenomenon — engineers reading postmortems and updating their understanding of system failure modes. The simulation operationalizes that phenomenon as cosine-similarity-gated transformation between knowledge vectors. Reed provides observational evidence that this kind of knowledge transfer happens in practice; the simulation tests how its scope (NONE / LOCAL / NEIGHBOR / GLOBAL) determines organizational reliability outcomes.

**Citation sentence:**
> *"Reed's \cite{reed2019} multi-case qualitative research at high-performing software organizations --- conducted within the resilience-engineering tradition (his MSc was supervised by Dekker, Entry 17) --- describes postmortems primarily as knowledge-transfer events that share rich context and update engineers' mental maps of complex socio-technical systems, rather than as remediation-list generators. This observational evidence motivates the simulation's treatment of each postmortem as a knowledge-transfer event whose effect on the receiving team depends on cosine similarity between the team's existing knowledge vector and the incident's feature vector --- a quantitative operationalization of the mental-map-patching phenomenon Reed describes. Reed also documents the \emph{fix-it treadmill} failure mode in which organizations generate remediation items without deeper sense-making; this is the failure mode the NONE and LOCAL sharing strategies model in our simulation."*

**What it does NOT claim:**
- *ACM Queue* is editorially curated, not peer-reviewed empirical research. Use Reed for *observational* claims about software industry practice, not for statistical effect-size claims. Empirical claims about learning behavior come from Edmondson 1999 (peer-reviewed); empirical claims about postmortem adoption come from Dingsøyr 2005 (peer-reviewed).
- The 91% statistic is from Reed's own interview sample, not a broader industry survey. When citing it, qualify as "from Reed's interview sample" or "in the organizations Reed studied" — not as a general industry statistic.
- Multi-case qualitative research, not a single-organization study and not statistical generalization.
- Does not quantify learning outcomes — no before/after metrics; the mental-map-patching mechanism is described qualitatively.
- Does not prove that more sharing leads to better outcomes — that is what the simulation tests.
- Reed's "mental-map patching" maps to the simulation's Stage 3 transformation as a *conceptual analog*, not an isomorphic mapping. The simulation makes operationalization choices (cosine-similarity threshold, Bernoulli probability) that Reed's qualitative description does not specify.

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

**Summary:** Peer-reviewed multi-method study (literature review + 19-company survey + single case study) published in *Information and Software Technology*. Documents that postmortem reviews are underused in software engineering and that even where conducted, organizations are unsatisfied with the learning they produce. Note: Dingsøyr's focus is on *project* postmortems (end-of-project retrospectives), not *incident* postmortems (post-failure analysis of operational events). He frames postmortems through Wenger's (1998) communities of practice and Nonaka & Takeuchi's (1995) tacit-to-explicit knowledge conversion, with single-loop / double-loop learning from Argyris & Schön (1978) — these are *different* from this thesis's absorptive-capacity framework, so the conceptual mapping is interpretive bridging, not Dingsøyr's own claim.

**What I'm taking from it:** Three contributions, each precisely scoped:

1. **Peer-reviewed empirical anchor for the postmortem adoption gap in software engineering.** The 1-in-5 statistic and zero-satisfaction finding from the 19-company survey provide peer-reviewed empirical motivation for the broader question this thesis addresses. (Reed 2019, Allspaw 2012, Lunney & Lueder 2016 are practitioner sources; Dingsøyr is the peer-reviewed end of the chain.)

2. **The persistent satisfaction gap.** Even where postmortems happen, organizations aren't satisfied. This finding has aged better than the 1-in-5 adoption statistic — modern DevOps/SRE practice has higher *incident* postmortem adoption (Reed 2019), but the deeper question of whether postmortems actually produce organizational learning persists. The thesis tests one specific lever (sharing scope) for closing this learning gap.

3. **The single/double-loop distinction (Argyris & Schön via Dingsøyr)** as a *conceptual analog* for what the simulation measures. The Prevention K accumulation across many incidents is conceptually analogous to double-loop learning — broader knowledge that prevents future incidents in different forms, not just patches for specific incidents. The simulation does not explicitly model the single/double-loop distinction; the mapping is interpretive.

**Connection to my simulation:** Dingsøyr provides the **peer-reviewed empirical anchor** in the software-engineering domain, complementing the practitioner observations from Reed (observational, *ACM Queue*) and Allspaw / Lunney & Lueder (industry practitioner). The four-citation chain for software-domain empirical grounding:

| Source-type | Citation | Specific role |
|---|---|---|
| **Peer-reviewed empirical (SE)** | **Dingsøyr (2005)** | **Survey + case study; the 1-in-5 adoption gap and zero-satisfaction finding** |
| Observational practitioner | Reed (2019) | High-performing orgs' postmortem practice |
| Practitioner | Allspaw (2012), Lunney & Lueder (2016) | Etsy and Google operationalization |

The simulation's central design choice — varying sharing scope systematically — is motivated by Dingsøyr's documentation that organizations remain dissatisfied with their postmortem learning even where the practice is conducted. The modern DevOps/SRE evolution has improved adoption; the deeper question is whether broader sharing is the lever that closes the satisfaction gap.

**Citation sentence:**
> *"Dings{\o}yr's \cite{dingsoyr2005} peer-reviewed multi-method study --- combining literature review, a 19-company European survey, and a case study at a Norwegian satellite-software development company --- documents two findings that motivate this thesis: only about one in five software projects received a post-project review, and not a single company in the survey expressed satisfaction with its postmortem process. Dings{\o}yr's focus is on \emph{project} postmortems specifically, and modern DevOps and SRE practice has substantially improved \emph{incident} postmortem adoption (\cite{reed2019,lunney2016,allspaw2012}). However, the deeper finding --- that organizations remain dissatisfied with the learning postmortems actually produce --- has persisted across both practices, and motivates the central question of this thesis: whether the scope of postmortem sharing is the lever that closes this learning gap."*

**What it does NOT claim:**
- **Project postmortems, not incident postmortems.** This is the most important scope qualifier. Dingsøyr studies end-of-project retrospectives, not post-failure operational analysis. The 1-in-5 adoption statistic is about the project-postmortem practice; modern incident postmortem adoption (Lunney & Lueder, Allspaw) is much higher. The deeper *satisfaction* gap is the part that transfers across both practices.
- 2005 paper — predates modern DevOps/SRE incident postmortem culture. Pair with Reed (2019), Lunney & Lueder (2016), and Allspaw (2012) for current incident-postmortem practice.
- 19-company Norwegian/European sample — peer-reviewed but geographically and temporally specific. Use for the structural finding (adoption + satisfaction gaps exist), not for global statistical generalization.
- Does not measure learning outcomes — describes practices and self-reported satisfaction, not their causal effects on incident rates or other outcomes.
- **Framework translation is interpretive.** Dingsøyr uses Wenger (communities of practice), Nonaka & Takeuchi (tacit-to-explicit), and Argyris & Schön (single/double-loop). These are different from the thesis's Cohen & Levinthal / Zahra & George / Argote & Miron-Spektor framework. The conceptual mapping (e.g., "tacit-to-explicit corresponds to acquisition + assimilation") is the present author's bridging, not Dingsøyr's own claim.

---

### 23. Sargent (2020) — Verification and Validation of Simulation Models: An Advanced Tutorial

**Journal/Source:** Proceedings of the Winter Simulation Conference (WSC), 16–29
**Bib key:** `sargent2020`

**Author authority worth knowing:** Sargent (Syracuse University, Emeritus) has been publishing iterations of this V&V tutorial in WSC proceedings since the 1970s. His name on a V&V framework carries the same kind of canonical weight in simulation methodology that Cohen & Levinthal carries in absorptive capacity — he is *the* reference cited in essentially every simulation methodology paper.

**Raw notes:**
- Validity is purpose-relative — a model is valid for its intended use, not in the abstract
- Parsimonious model is always preferred — as simple as possible while meeting purpose
- Exploratory models require less demanding validity standards than operational decision-making models
- **Four V&V activities** every simulation study must address:

| Activity | Question | Evidence in this thesis |
|---|---|---|
| **Conceptual model validity** | Are theories and assumptions identified, stated, and correct? | Bibliography — every design choice has a cited source |
| **Computerized model verification** | Does the code do what the design specified? | Unit tests in `02-Framework-Code/tests/`; pilot reproducibility |
| **Operational validity** | Does the model produce outputs in the right ballpark? | MTTR range-checked against Forsgren DORA bands; incident type distribution against Dogga Azure data; H1 ordering invariant across realistic parameter ranges |
| **Data validity** | Are input parameters correct? | Every parameter grounded in cited literature (decay from Darr et al., acquisition probability from AC literature, topology defaults from Watts & Strogatz / Barabási & Albert) |

**Summary:** Tutorial paper in *Winter Simulation Conference Proceedings* (THE canonical venue for simulation methodology) synthesizing Sargent's V&V framework. Establishes that simulation validity is purpose-relative rather than absolute, provides a four-part V&V taxonomy every study must address, and argues that exploratory models require lower accuracy standards than predictive models. Not new empirical research — methodological prescription synthesized from decades of work.

**What I'm taking from it:** Three contributions, with the first being the most defensively important:

1. **The exploratory-validity shield against the "synthetic data" critique.** This is the single most important defensive use of Sargent. The committee's strongest critique of an ABM thesis is "your data is synthetic — how do you know your model reflects reality?" Sargent's purpose-relative validity framework defuses this directly: validity depends on the model's purpose. An exploratory model — one designed to *explain a mechanism* — requires lower accuracy thresholds than a predictive model — one designed to *forecast specific outcomes*. This thesis claims exploratory validity, not predictive validity, and Sargent provides the methodological grammar to defend that claim.

2. **The four V&V activities as the structure of the validation chapter.** Section 9 of the report (and the validation chapter of the thesis) is organized around Sargent's four activities. Citing Sargent at the start of that section signals adherence to the field's accepted V&V framework, not freelancing.

3. **Parsimony justification for every model simplification.** Sargent's parsimony principle — prefer the simplest model that achieves the purpose — defends each of these scope choices: 20 teams (not 200), homogeneous team capacity, fixed network topology, 365-day horizon, one subsystem per team. Each simplification is methodologically grounded, not an oversight.

**Connection to my simulation:** Sargent is the **V&V framework citation** in the methodology defense, complementary to but distinct from the why-ABM citations:

| Citation | Specific role in methodology defense |
|---|---|
| Bonabeau (2002) | When to use ABM (heterogeneous, nonlinear, stochastic) |
| Epstein (1999) | Generative social science philosophy ("if you didn't grow it, you didn't explain it") |
| Harrison et al. (2007) | Simulation as legitimate organizational research |
| Carley (1992) | ABM precedent specifically for organizational learning |
| Margaryan et al. (2017) | Domain-specific call for simulation in LFI |
| **Sargent (2020)** | **V&V framework — *how* to defend the model's validity** |

The first five citations justify *why* simulation. Sargent justifies *how* you defend its validity once you've chosen it. Different work; non-overlapping role.

**Citation sentence:**
> *"Simulation validity is assessed following Sargent's \cite{sargent2020} four-activity V\&V framework --- conceptual model validity, computerized model verification, operational validity, and data validity --- as iterated over decades in his \emph{Winter Simulation Conference} tutorials, the canonical reference for simulation methodology. Consistent with Sargent's principle that validity is purpose-relative, we claim \emph{exploratory validity}: this model is designed to compare knowledge-sharing strategies under controlled conditions and explain the mechanism by which sharing scope affects organizational reliability, not to predict specific outcomes for any real organization. Sargent's parsimony principle further justifies the model's deliberate simplifications --- 20 teams, homogeneous team capacity, fixed network topology, single subsystem per team, 365-day horizon --- as methodologically grounded scope choices rather than oversights."*

**What it does NOT claim:**
- WSC tutorial — methodological prescription, not new empirical research. The authority claim rests on Sargent's longstanding role in the simulation methodology community, not on data from this specific paper.
- Does not say exploratory simulations require no validation — they still require all four V&V activities, just at lower accuracy thresholds than predictive simulations would.
- Does not provide a formula for acceptable accuracy — the threshold must be stated explicitly per purpose. The thesis states "ordering of sharing strategies is the load-bearing finding; absolute incident counts are not predictions."
- Hypothesis testing in this thesis is not formal statistical testing against real-system data — it is statistical comparison across simulated conditions. Sargent's framework explicitly accommodates this for exploratory work.
- Validity claims do not extend beyond the model's stated purpose. Anyone interpreting the thesis as predictive of specific organizations' incident rates is operating outside the scope Sargent's framework supports.

---

### 24. Grimm et al. (2020) — The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update

**Journal/Source:** Journal of Artificial Societies and Social Simulation, 23(2), 7
**Bib key:** `grimm2020`

**Author authority worth knowing:** Volker Grimm (Helmholtz Centre for Environmental Research – UFZ; University of Potsdam) is the original architect of ODD — he pioneered it for ecological ABM in 2006 and has led each subsequent update. The 2020 paper is a **19-author international consensus collaboration** (Grimm + Railsback + 17 others), not a single-author preference. The co-author list signals that ODD is the *field's* negotiated standard, not one researcher's opinion. *JASSS* is the canonical ABM-specific journal — distinct from Sargent's *WSC* (general simulation methodology) or Bonabeau's *PNAS* (cross-disciplinary primer).

**Raw notes:**
- ODD (Overview, Design Concepts, Details) is the accepted standard protocol for documenting agent-based models
- History: 2006 original (Ecological Modelling) → 2010 first update → 2020 second update (this paper)
- The 2020 update addresses five limitations of earlier versions: limited guidance, excessive document length, difficulty handling complex models, insufficient detail for reimplementation, no provisions for model rationale or evaluation
- ODD as "lingua franca" for simulation modeling broadly
- Both a reporting format and a workflow that forces modelers to think through every part of design
- Compact ODD summary for journal articles with full details in supplementary material
- **The seven ODD elements** mapped to this thesis:

| Element | What it documents | Maps to in this thesis |
|---|---|---|
| **1. Purpose and Patterns** | What is the model for? What patterns should it reproduce? | Comparing four sharing strategies; patterns = H1 ordering + K saturation + BA crossover (see below) |
| **2. Entities, State Variables, and Scales** | Who are the agents, what state do they hold, what scale? | 20 teams; Kp/Kd/Km knowledge vector; subsystem ownership; daily timestep; 365-day horizon |
| **3. Process Overview and Scheduling** | What processes occur each timestep, in what order? | Daily: incident generation → postmortem creation → sharing/acquisition → assimilation → transformation → exploitation → state update |
| **4. Design Concepts** | Emergence, adaptation, learning, sensing, stochasticity, etc. | Emergence (organization-wide reliability); learning (four-stage AC pipeline); stochasticity (incident generation, stage transitions) |
| **5. Initialization** | What is the starting state? | Cold start: zero accumulated knowledge; networks generated per topology rules |
| **6. Input Data** | What external data feeds the model? | None — fully parameterized; no real-world incident data fed in |
| **7. Submodels** | Detailed description of each process | Incident generation; four pipeline stages; decay; sharing-scope routing |

- **"Patterns" as evaluation criteria** (key 2020 addition) — modelers must specify, in advance, what patterns the model should reproduce. The four pre-specified patterns for this thesis: (1) H1 sharing-strategy ordering NONE > LOCAL > NEIGHBOR > GLOBAL in incident count; (2) Knowledge K saturation by day 90 under GLOBAL (Prevention K → 0.992); (3) BA crossover at `ba_m = 3`; (4) H1 ordering invariant across all five tested topologies.

**Summary:** Multi-author consensus paper (19 authors) in *JASSS* updating ODD — the accepted documentation standard for ABM in the field. The 2020 second update introduces patterns as explicit evaluation criteria and a compact summary format suitable for journal articles. Not new empirical research; this is the field's protocol document.

**What I'm taking from it:** Three contributions, each anchoring a specific defensive use:

1. **Documentation standard for replication.** ODD provides the field-accepted structure for documenting an ABM well enough that another researcher could reimplement it. Chapter 3 of the thesis maps directly onto ODD's seven elements (see table above). Citing Grimm signals adherence to the field standard, not freelancing.

2. **The "Patterns" framing as pre-registered evaluation criteria.** This is the load-bearing defensive use. Grimm's 2020 update explicitly requires modelers to specify in advance what patterns the model should reproduce — these become the evaluation criteria. The thesis pre-specifies four patterns (H1 ordering, K saturation by day 90, BA crossover at 3, topology-effect persistence), all of which the simulation reproduces. This gives a methodologically grounded answer to "how do we know your model worked?" — the answer is "Grimm requires pre-specified patterns; I pre-specified four; the simulation reproduces all four."

3. **ODD as a workflow forcing justification of every component.** Beyond reporting format, ODD acts as a design checklist that surfaces underspecified mechanisms. Working through ODD's seven elements forced clarification of, for example, the cold-start initialization choice and the no-input-data scope decision.

**Connection to my simulation:** Grimm is the **documentation standard citation** in the methodology defense, **complementary to but distinct from Sargent's V&V framework**:

| Citation | Question it answers |
|---|---|
| **Sargent (2020)** | **Is the model valid?** (V&V framework: conceptual, computerized, operational, data validity) |
| **Grimm et al. (2020)** | **Is the model documented well enough that someone could reimplement it?** (ODD seven-element protocol) |

The two are non-overlapping. Citing both signals adherence to the field's two canonical methodology standards: validation and documentation.

**Citation sentence:**
> *"The model is documented following the ODD protocol \cite{grimm2020} --- the multi-author consensus standard for agent-based model documentation, in its 2020 second update by Grimm and eighteen co-authors in the \emph{Journal of Artificial Societies and Social Simulation}, the canonical ABM venue. Chapter 3 maps directly onto ODD's seven elements: Purpose and Patterns, Entities and State Variables and Scales, Process Overview and Scheduling, Design Concepts, Initialization, Input Data, and Submodels. The Purpose and Patterns element is load-bearing: ODD requires pre-specifying what patterns the model should reproduce as evaluation criteria. We pre-specify four patterns --- the H1 sharing-strategy ordering, Prevention K saturation by day 90 under GLOBAL, the BA crossover at $\\mathit{ba\\_m} = 3$, and the persistence of the H1 ordering across all five tested topologies --- all of which the simulation reproduces. ODD complements Sargent's \\cite{sargent2020} V\\&V framework: ODD is documentation; Sargent is validation."*

**What it does NOT claim:**
- Does not require every ABM paper to include a full ODD document — the 2020 update specifically supports a compact summary format suitable for journal articles, with full details in supplementary material.
- ODD is a description standard, not a validation framework — cite Sargent (2020) separately for validation. The two are complementary, not overlapping.
- Methodological guidance, not a theoretical contribution — do NOT use Grimm to justify ABM as the right method (use Bonabeau, Epstein, Harrison, Carley for that).
- ODD is the field's negotiated consensus standard, not Grimm's personal preference. The 19-author co-author list signals this; cite as field standard, not as a single researcher's recommendation.
- Pre-specified patterns evaluate whether the model reproduces the *intended phenomena*; they do NOT establish predictive validity for any specific real organization. That is Sargent's exploratory-validity scope claim.

---

### 25. Epstein (1999) — Agent-Based Computational Models and Generative Social Science

**Journal/Source:** Complexity, 4(5), 41–60
**Bib key:** `epstein1999`

**Author authority worth knowing:** Joshua Epstein is a pioneer of social simulation and co-author with Robert Axtell of *Growing Artificial Societies: Social Science from the Bottom Up* (1996) — the "Sugarscape" book that effectively launched the field of social simulation. He was at the Brookings Institution at the time of this paper and is now at NYU School of Global Public Health, where he continues canonical work in epidemic modeling, evacuation modeling, and computational social science. *Complexity* is mid-tier as a venue, but the authority claim rests on Epstein's status as a canonical figure in the field, not on the journal's prestige.

**Raw notes:**
- Agent-based computational models represent a new mode of scientific explanation — "generative social science"
- Core claim: a social phenomenon is only truly explained when you can grow it from the bottom up using simple agent-level rules
- Sharp distinction between explanation and prediction: a model can explain *why* something happens without being able to predict *when* or *where*
- Two natural-science analogies Epstein cites:
  - **Plate tectonics** fully explains why earthquakes occur (stress accumulation along fault lines, sudden release) — but cannot predict when the next earthquake will hit any specific location
  - **Evolutionary theory** fully explains species diversity (variation, selection, inheritance) — but cannot predict specific phenotypes
- These are valid scientific explanations even though they fail at prediction. **Unpredictability does not mean unexplainability.**
- ABM is a mature, general-purpose methodology for studying emergent social phenomena (segregation, cooperation, market dynamics, organizational behavior, epidemic spread, cultural transmission)

**Summary:** Philosophical/methodological essay articulating ABM as a mode of scientific explanation. Argues that emergent social phenomena are truly *explained* when they can be generatively grown from agent-level rules — captured by the famous motto: "if you didn't grow it, you didn't explain its emergence." Critically, draws a sharp distinction between explanation and prediction: a model can fully explain a phenomenon without predicting specific instances, just as plate tectonics explains earthquakes without predicting them.

**What I'm taking from it:** Three contributions, with the explanation/prediction distinction being the most defensively important:

1. **The explanation/prediction distinction as defense against the "synthetic data" critique.** This is the single most important defensive use of Epstein. A committee member can say "your simulation produces synthetic data — how can it produce real scientific knowledge?" Epstein's response: prediction was never the goal. The goal is *explanation* — showing the mechanism by which sharing scope affects organizational reliability. Plate tectonics explains earthquakes without predicting when they hit; evolutionary theory explains species diversity without predicting specific phenotypes. These are valid scientific explanations even though they fail at prediction. The simulation produces explanatory knowledge of the same kind.

2. **The generative motto as methodological backbone.** *"If you didn't grow it, you didn't explain its emergence."* Showing that variable X correlates with outcome Y is description, not explanation. Showing that Y emerges from agent-level interactions involving X is explanation. The simulation grows organizational reliability from twenty teams following local rules — that is the type of explanation Epstein argues is the strongest form available for emergent phenomena.

3. **Lineage placement.** Epstein lists phenomena successfully studied with ABM — segregation (Schelling), cooperation evolution (Axelrod), market dynamics, organizational behavior, epidemic spread. The work sits in the "organizational behavior" lineage Epstein identifies, alongside Carley's organizational learning ABMs and Müller et al.'s knowledge-diffusion ABMs.

**Connection to my simulation:** Epstein is the **philosophy-of-science layer** of the methodology defense. He works together with Bonabeau (when to use ABM) and Sargent (how to validate it):

| Citation | Question it answers |
|---|---|
| Bonabeau (2002) | **When** is ABM the right tool? (heterogeneous, nonlinear, stochastic agents) |
| **Epstein (1999)** | **What kind of scientific explanation does ABM provide?** (generative; explanation ≠ prediction) |
| Sargent (2020) | **How do you validate a simulation given its purpose?** (purpose-relative validity; exploratory validity for explanatory work) |

Epstein and Sargent together defuse the "synthetic data" critique completely: Epstein provides the *philosophical* basis for explanation-without-prediction; Sargent provides the *methodological* framework (exploratory validity) for validating explanatory models at appropriate accuracy thresholds. Bonabeau and Epstein together justify the *choice* of ABM: Bonabeau on conditions, Epstein on epistemological status.

**Citation sentence:**
> *"The simulation is grounded philosophically in Epstein's \cite{epstein1999} framework of generative social science, which argues that emergent social phenomena are truly explained when they can be computationally generated from simple agent-level rules: 'if you didn't grow it, you didn't explain its emergence.' Critically, Epstein draws a sharp distinction between explanation and prediction --- citing natural-science precedents in which plate tectonics explains earthquakes without predicting when they will occur, and evolutionary theory explains species diversity without predicting specific phenotypes. Organizational reliability is similarly an emergent phenomenon, and the simulation generates it from twenty teams following local rules. The thesis claims explanatory validity for the mechanism by which sharing scope affects organizational reliability, not predictive validity for any specific organization --- a scope choice operationalized through Sargent's \cite{sargent2020} purpose-relative V\\&V framework."*

**What it does NOT claim:**
- *Complexity* is a mid-tier journal — the authority claim rests on Epstein's canonical status (Sugarscape co-author; pioneer of social simulation), not the venue's prestige
- Does not claim ABM is superior to all other methods — it is the right tool for emergent phenomena specifically. Statistical methods remain appropriate for description and association; experiments remain appropriate for causal inference; ABM is appropriate for generative explanation
- The explanation/prediction distinction does NOT mean the model cannot be validated — Sargent (2020) provides the V&V framework that operationalizes "exploratory validity" for explanatory models. Epstein and Sargent are complementary, not competing
- Epstein's examples are drawn from economics, ecology, and general social science — software incident application is the present author's domain transfer
- The generative motto is the most-quoted line in the paper but reflects a stronger claim than many ABM practitioners endorse. Quote it for emphasis but be ready to defend it as Epstein's claim, not a universally agreed-on standard

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

**Author authority worth knowing:** Morten T. Hansen — Norwegian-American researcher; was at Harvard Business School at time of publication, then INSEAD, now UC Berkeley Haas School of Business. Major figure in organizational network research and knowledge transfer; one of the most-cited researchers on the topic. *ASQ* is Tier 1 (same venue as Edmondson 1999 and Cohen & Levinthal 1990).

**Raw notes:**
- Empirical study of **120 product-development projects across 41 divisions** in a single large US electronics/computer company
- Methodology: **hazard-rate event history analysis** — sophisticated statistical technique tracking how the probability of project completion changes over time as a function of tie strength and knowledge characteristics
- Two distinct problems require different solutions:
  - **Search** (finding who has the knowledge) — weak ties extend reach across the organization
  - **Transfer** (moving knowledge into the recipient) — strong ties enable back-and-forth required for tacit content
- For **codified knowledge** (written, structured, self-contained), the trade-off disappears: weak ties suffice for both search AND transfer
- Postmortems are codified artifacts (specifying what failed, why, and what was changed in writing)

**The 2x2 matrix that captures Hansen's central finding:**

| | Codified knowledge | Noncodified / complex knowledge |
|---|---|---|
| **Weak ties** | Search ✅ Transfer ✅ | Search ✅ Transfer ❌ |
| **Strong ties** | Search ❌ (limited reach) Transfer ✅ | Search ❌ (limited reach) Transfer ✅ |

The codification "escape hatch" — when knowledge is sufficiently codified, weak ties no longer face a trade-off. The artifact carries the knowledge.

**Summary:** Empirical study of knowledge transfer across organizational subunits. Establishes that weak ties help search but hurt transfer of complex (noncodified) knowledge — UNLESS the knowledge is codified, in which case weak ties suffice for both. Postmortems are codified artifacts, so Hansen's framework predicts they should transfer effectively across weak ties even between teams with no prior relationship.

**What I'm taking from it:** Three contributions, each load-bearing for a specific simulation result:

1. **The codification claim explains why GLOBAL works.** Postmortems are codified — written, structured, self-contained artifacts specifying what failed, why, and what changed. Per Hansen, codified knowledge transfers across weak ties. So GLOBAL sharing doesn't require every team to have a strong relationship with every other team for postmortems to be useful; the codified artifact carries enough of the knowledge to enable transformation. This is the empirical justification for why GLOBAL produces 89.5% transformation rate in the simulation.

2. **The tacit residue explains why GLOBAL doesn't reach 100%.** Postmortems aren't *purely* codified. Reed (2019) emphasizes that the deeper value of postmortems lies in mental-map updates, "second stories," and systemic context — partially tacit content that is harder to fully capture in writing. Per Hansen, this tacit content does NOT transfer effectively across weak ties; it requires stronger relationships. So GLOBAL transformation rate is high but bounded below 100% because the tacit residue doesn't cross weak ties cleanly.

3. **The search-transfer distinction maps to the Acquisition-Transformation asymmetry.** In the simulation pipeline, Acquisition (Stage 1) solves the search problem — GLOBAL eliminates it entirely by broadcasting to all teams. Transformation (Stage 3) is the transfer problem where the codified-vs-tacit distinction matters. Hansen's framework explains why these two stages behave so differently in sensitivity sweeps: acquisition probability is the most sensitive parameter (search matters), but transformation rate stays bounded because tacit content doesn't transfer regardless of how broadly the artifact is shared.

**Connection to my simulation:** Hansen is the **why-GLOBAL-works empirical citation** in the knowledge-transfer mechanism chain:

| Citation | Specific role |
|---|---|
| Cohen & Levinthal (1990) | Within-team absorption — explains LOCAL's 0% transformation |
| Szulanski (1996) | Inter-unit transfer barriers — explains NEIGHBOR's 14% transformation |
| **Hansen (1999)** | **Codified vs noncodified across ties — explains GLOBAL's 89.5% (high but not 100%)** |
| Reagans & McEvily (2003) | Cohesion + range as network mechanisms — explains H4 topology effects |
| Nooteboom et al. (2007) | Cognitive distance — Stage 3 cosine-similarity gate |

The simulation result (89.5% transformation under GLOBAL) is exactly what Hansen's framework predicts: the codified content of postmortems transfers cleanly across weak ties (high rate), but the tacit residue doesn't (rate bounded below 100%). Pair with Reed (2019) for the empirical evidence that postmortems contain partially tacit content.

**Citation sentence:**
> *"Hansen's \cite{hansen1999} empirical study of 120 product-development projects across 41 divisions of a large US electronics company --- using hazard-rate event history analysis --- separates knowledge transfer into two distinct problems: search (finding who has the knowledge) and transfer (moving it into the recipient). For complex tacit knowledge, weak ties enable search but fail at transfer. For codified knowledge --- written, structured, self-contained --- weak ties are sufficient for both. Postmortems are codified artifacts that specify what failed, why, and what was changed in written form, so Hansen's framework predicts they should transfer effectively across weak ties even between teams with no prior relationship. This is the empirical justification for why GLOBAL sharing produces high transformation rates in our simulation. The framework also predicts the rate should not reach 100\%, because postmortems contain partially tacit content (mental-map updates and systemic context, per Reed \cite{reed2019}) that requires stronger ties to transfer fully --- consistent with our observed 89.5\% transformation rate under GLOBAL."*

**What it does NOT claim:**
- Studies product-development knowledge transfer in a single US electronics company, not incident postmortems specifically — codification is the conceptual bridge; explicitly note the domain transfer
- Weak ties are NOT always bad — only specifically bad for noncodified, dependent knowledge transfer
- Project completion time is the outcome measure — an *indirect* proxy for transfer success; not a direct measure of knowledge integration
- Codification is operationalized binary in the analysis, but continuous in reality — postmortems contain both codified and tacit elements
- Does not address sharing scope directly — Hansen studies tie strength and knowledge characteristics, not broadcasting policy. Mapping the search-vs-transfer distinction to Acquisition-vs-Transformation is the present author's interpretation
- Single-company sample limits statistical generalization beyond product-development contexts

---

### 28. Reagans & McEvily (2003) — Network Structure and Knowledge Transfer: The Effects of Cohesion and Range

**Journal/Source:** Administrative Science Quarterly, 48(2), 240–267
**Bib key:** `reagans2003`

**Author authority:** Ray Reagans (now MIT Sloan, then CMU Tepper) and Bill McEvily (now Toronto Rotman, then CMU) — both established network scholars. ASQ is a Tier 1 management journal (~7% acceptance rate); this paper is one of the most-cited empirical resolutions of the Coleman–Burt theoretical debate over whether dense ties or structural holes drive knowledge transfer.

**Raw notes:**
- Empirical setting: 104 employees in a single contract R&D firm in the chemicals industry; full-network survey on advice-seeking and knowledge transfer ease
- Multivariate regression predicts ease of knowledge transfer from cohesion, range, and tie strength controls
- **Cohesion** = the density of mutual third-party connections surrounding a relationship → creates cooperative norms via reputation effects (you can't free-ride if your shared contacts will hear about it)
- **Range** = the diversity of knowledge pools an actor connects to → builds the cross-boundary translation skill needed to transfer complex knowledge to people in different domains
- Both cohesion and range have independent positive effects on transfer ease, controlling for tie strength
- Resolves the Coleman–Burt debate empirically: Coleman's cohesion (dense closed networks) and Burt's range (open networks bridging structural holes) are *complementary* mechanisms, not competing ones — the highest-performing transfer happens when actors have both

**Summary:** Empirical resolution of the Coleman–Burt debate. Using a full-network survey of 104 R&D employees, Reagans & McEvily show that two distinct structural properties — cohesion (mutual connections that create cooperative norms) and range (diverse knowledge pools that build cross-boundary transfer skill) — independently facilitate knowledge transfer above and beyond tie strength. The optimal network combines both.

**What I'm taking from it:**

1. **Coleman and Burt are both right — and the optimal topology combines both.** This is the theoretical justification for why a topology with local clustering *and* bridging ties (Watts–Strogatz) outperforms topologies that have only one or the other.

2. **Cohesion explains why NEIGHBOR outperforms LOCAL beyond simple exposure.** Dense mutual connections create cooperative norms via reputation effects — sharing becomes expected behavior, not optional.

3. **Range explains GLOBAL's cross-domain transfer.** Actors connected to diverse knowledge pools develop the translation skill needed to make incidents from one team useful to teams in different problem spaces.

4. **Topology mapping for H4:**
   - **Complete:** high cohesion (everyone shares neighbors), low range (everyone in the same pool) → mid performance
   - **Star:** low cohesion (peripheral teams share only the hub), low range (hub is the only bridge) → worst performance, predicted by both dimensions failing
   - **Watts–Strogatz:** high cohesion within clusters + range via cross-cutting bridges → best performance, exactly the cohesion+range combination Reagans & McEvily identify as optimal

**Connection to my simulation:** Provides the mechanism-level explanation for the H4 topology ranking. The three findings — Star underperforms, WS outperforms Complete, NEIGHBOR > LOCAL — are precisely what Reagans & McEvily's two-mechanism model predicts. Star fails on both dimensions; Complete has cohesion without range; WS has both. The mapping is conceptual (their measures are individual-level network position; ours are organizational topology), but the mechanisms — cooperative norms from cohesion, cross-boundary translation from range — translate directly. Together with Hansen (1999) on tie-strength × knowledge-type, this paper completes the theoretical foundation for H4.

**Citation sentence:**
> *"Reagans \& McEvily \cite{reagans2003}, in a full-network study of 104 R\&D employees, empirically reconcile the Coleman--Burt debate by showing that network cohesion --- dense mutual connections that create cooperative norms via reputation effects --- and network range --- ties spanning diverse knowledge pools that build cross-boundary translation skill --- have independent positive effects on knowledge transfer. The Watts--Strogatz small-world topology, which combines high local clustering with short cross-cutting path lengths, instantiates both properties simultaneously and is therefore predicted to outperform topologies that achieve only one (Complete: cohesion without range) or neither (Star: peripheral isolation on both dimensions)."*

**What it does NOT claim:**
- Single-firm R&D study — generalization to software-engineering organizations is conceptual, not empirical
- Cohesion and range measured at the individual ego-network level; H4 maps these to organizational topology — the translation is theoretical
- Does not address sharing policy (NONE/LOCAL/NEIGHBOR/GLOBAL) — that is our contribution
- Does not resolve which of cohesion or range matters more in absolute terms — both have independent effects; relative weights are context-dependent
- Does not address tacit vs. codified knowledge directly — that distinction belongs to Hansen (1999)

---

### 29. Kim, Humble, Debois & Willis (2016) — The DevOps Handbook

**Journal/Source:** IT Revolution Press (book)
**Bib key:** `kim2016`

**Author authority:** The four authors are the founding figures of the DevOps movement. **Patrick Debois** coined the term "DevOps" at DevOpsDays 2009. **Gene Kim** authored *The Phoenix Project* (2013, the novel that brought DevOps mainstream) and founded IT Revolution. **Jez Humble** authored *Continuous Delivery* (2010, the book that defined CD) and is co-author of *Accelerate*. **John Willis** is a foundational DevOps evangelist (DevOps Cafe podcast, Docker veteran). This is industry doctrine codified by the people who built the field — practitioner book, not peer-reviewed research, but the canonical synthesis on the prescriptive side of the empirical/prescriptive/observational citation triangle (Forsgren empirical / Kim prescriptive / Allspaw observational).

**Raw notes:**
- Three Ways framework, derived from Kim's earlier *Phoenix Project*
- **First Way (Flow):** optimize flow of work from Dev to Ops; reduce batch sizes; eliminate handoff waste; small frequent changes over large infrequent ones
- **Second Way (Feedback):** create fast, amplified feedback loops at every stage; "stop the line" culture from Toyota; find and fix at source
- **Third Way (Continual Learning):** generative high-trust culture; allocate time for improvement; blameless postmortems; "transforming local discoveries into global improvements"
- Organizational ideal: "regardless of where someone performs work, they do so with the cumulative and collective experience of everyone"
- The Three Ways are *interdependent* — Flow without Feedback produces fast failure; Feedback without Continual Learning produces local-only fixes

**Summary:** The canonical practitioner synthesis of DevOps. The Three Ways framework — Flow, Feedback, Continual Learning — describes the interdependent organizational conditions under which software teams reliably learn from failures and improve over time. The Third Way's central prescription, "transforming local discoveries into global improvements," is the practitioner statement of this thesis's central question.

**What I'm taking from it:**

1. **The Third Way is the thesis hypothesis in practitioner language.** "Transforming local discoveries into global improvements" is exactly what GLOBAL sharing operationalizes. Local discoveries = individual team postmortems. Global improvements = the 45% incident reduction under GLOBAL.

2. **Three Ways → simulation mapping (cleanly):**
   - First Way (Flow) ≈ deployment cadence (the H2 lever — faster deploys, smaller batches)
   - Second Way (Feedback) ≈ within-team learning loop (Stages 1–2 of the pipeline, where incident signals get amplified into team-level knowledge)
   - Third Way (Continual Learning) ≈ cross-team sharing scope (the H1 lever — the headline contribution)

3. **H2 conditional matters.** Kim et al. argue Flow produces quality *only when paired with Feedback and Continual Learning* — not on its own. The H2 finding (faster cadence reduces incidents) holds in our simulation *because* the four-stage learning machinery is also present. Without it, faster deploys would just produce more incidents.

4. **Third Way justifies the blameless-sharing assumption.** The book documents blameless postmortems as normalized industry practice — anchoring the simulation's assumption that teams will share rather than hide incidents.

**Connection to my simulation:** This is the prescriptive vertex of the DevOps citation triangle. **Forsgren et al. (2018)** provides the empirical correlation (high performers deploy 200× more, fail 3× less, recover 24× faster). **Kim et al. (2016)** provides the prescriptive framework (the Three Ways describe what high performers actually do). **Allspaw (2012)** provides the observational evidence (blameless postmortems as field practice at Etsy). The simulation provides the causal mechanism — *why* the Third Way produces the reliability outcomes both Forsgren and Kim describe.

**Citation sentence:**
> *"Kim et al.\ \cite{kim2016} describe the Third Way of DevOps as designing systems of work that `multiply the effects of new knowledge, transforming local discoveries into global improvements' so that `regardless of where someone performs work, they do so with the cumulative and collective experience of everyone.' Our simulation operationalizes this principle directly: the four sharing scenarios test how the structural reach of the knowledge pipeline determines whether local incident discoveries remain local (NONE/LOCAL) or compound into organizational-level reliability improvements (GLOBAL)."*

**What it does NOT claim:**
- Practitioner book, not peer-reviewed empirical research — pair with Forsgren et al. (2018) for the empirical version
- The Three Ways are prescriptive principles, not a measured causal model — the simulation provides the causal mechanism
- Does not quantify the reliability benefit of global sharing — that is our contribution
- Does not address network topology or absorptive capacity theory directly — those framings come from Reagans \& McEvily, Hansen, and Cohen \& Levinthal
- Does not establish that Flow alone produces quality — the Three Ways are interdependent; H2 holds because the simulation includes Feedback and Continual Learning machinery

---

### 30. Borgatti & Foster (2003) — The Network Paradigm in Organizational Research: A Review and Typology

**Journal/Source:** Journal of Management, 29(6), 991–1013
**Bib key:** `borgatti2003`

**Author authority:** **Stephen P. Borgatti** (University of Kentucky LINKS Center) is the co-creator of UCINET — the dominant social-network-analysis software for two decades — and arguably the most-cited network methodologist in the field. **Pacey C. Foster** (UMass Boston) studies organizational and creative-industry networks. *Journal of Management* is a Tier 1 management journal; this review has 4,000+ citations and is the canonical orientation paper for organizational network research, routinely used by junior researchers to position their work within the field.

**Raw notes:**
- Literature review and organizing typology — not an empirical study, not a theoretical model; the contribution is taxonomic
- Goal: organize a fragmented field where studies were citing each other across totally different research questions
- Proposes a **2×2 typology** along two axes:
  - *Explanatory goal:* performance variation (why some actors outperform) vs. homogeneity (why connected actors become similar)
  - *Explanatory mechanism:* structuralist/topology ("girders" — the shape of the network) vs. connectionist/flows ("pipes" — what travels through ties)
- Four resulting traditions:

|  | Structuralist (topology) | Connectionist (flows) |
|---|---|---|
| **Performance variation** | **Structural capital** — Burt's structural holes; brokerage positions yield advantages | **Resource access** — strong/weak ties channel job leads, capital, information |
| **Homogeneity** | **Convergence** — structurally equivalent actors develop similar attitudes | **Contagion** — ideas, behaviors, infections diffuse through tie channels |

- Methodological emphasis: most network research studies *consequences* of network structure, not *antecedents* (how networks form)

**Summary:** A literature review and 2×2 typology that organizes organizational network research into four traditions distinguished by explanatory goal (performance variation vs. homogeneity) and mechanism (structural topology vs. resource flows). Borgatti & Foster do not propose theory; they label the shelves so researchers can identify which tradition their work belongs to. The canonical orientation paper for the field.

**What I'm taking from it:** A *positioning* citation for Chapter 2 — a one-sentence statement of which corner of network research the thesis works in. **H4 sits in the contagion quadrant**: the goal is homogeneity (do teams across the network converge in reliability/learning capability over time?) and the mechanism is connectionist (incident knowledge and capability flow through sharing-tie channels). Naming the quadrant explicitly tells the committee where to map the thesis and pre-empts the question "why aren't you citing Burt on structural holes?" (answer: Burt is in the *performance variation* quadrant — different question).

**Connection to my simulation:** Used as the table-of-contents citation. H4 is positioned in the contagion tradition; the actual mechanistic theory for *how* contagion works in this setting comes from Hansen (1999) on tie strength × knowledge type and Reagans & McEvily (2003) on cohesion and range. Borgatti & Foster does the orientation work in one sentence so the heavy theoretical lifting can be attributed to the right sources.

**Citation sentence:**
> *"Following Borgatti \& Foster's \cite{borgatti2003} 2$\times$2 typology of organizational network research --- distinguishing studies by explanatory goal (performance variation vs.\ homogeneity) and mechanism (structuralist topology vs.\ connectionist flows) --- this thesis sits in the \emph{contagion} tradition, studying how knowledge diffuses through tie channels to produce cross-team capability convergence."*

**What it does NOT claim:**
- Does NOT propose that cohesion + reach optimize knowledge diffusion — that is Hansen (1999) and Reagans & McEvily (2003)
- Does NOT theorize how contagion works mechanically — only labels it as a tradition
- Does NOT predict which topology will outperform — that is Watts & Strogatz (1998) and Reagans & McEvily (2003)
- Does NOT address network antecedents or change; focuses on consequences only
- Does NOT provide empirical results on knowledge transfer — Hansen (1999) does that

---

### 31. Levinthal (1997) — Adaptation on Rugged Landscapes

**Journal/Source:** Management Science, 43(7), 934–950
**Bib key:** `levinthal1997`

**Author authority:** **Daniel A. Levinthal** (Wharton, University of Pennsylvania) is one of the most influential organizational theorists alive. Critically, he is the *same Levinthal* who co-authored **Cohen & Levinthal (1990)** — the foundational absorptive capacity paper used in Entry 12 of this bibliography. The thesis therefore draws on two Levinthal papers applied to two different parts of the simulation: Cohen & Levinthal (1990) for the four-stage learning pipeline; Levinthal (1997) for the shape of the H3 diminishing-returns curve. *Management Science* is INFORMS' flagship Tier 1 theory journal; this paper has 6,000+ citations and is foundational to the computational organization theory tradition.

**Raw notes:**
- **NK model in plain English:** organizations are described by N binary attributes (e.g., centralize/decentralize, standardize/customize, promote-from-within/hire-externally), giving 2^N possible organizational forms. Each form has a fitness. The K parameter controls how much each attribute's contribution to fitness depends on the others.
  - K = 0 → smooth landscape, single global peak, local search finds it easily
  - K > 0 → rugged landscape, many local peaks, local search gets trapped on suboptimal peaks with no way to know a higher peak exists across the valley
- **Headline result:** path dependence and lock-in. Where an organization starts determines where it ends up; two organizations facing the same environment can plateau at very different fitness levels purely from starting-configuration and trajectory differences.
- **Local adaptation:** organizations sample neighboring forms (one-attribute changes), adopt if fitness improves — this is the search dynamic that produces the characteristic diminishing-returns curve as nearby improvements get exhausted.
- The fitness landscape is **organizational form space, not knowledge space** — a critical distinction for using this citation safely.

**Summary:** A foundational theory paper showing that when organizations adapt by local search on landscapes where attributes are interdependent (high K), they produce a characteristic diminishing-returns curve — early changes yield large gains, later changes plateau as nearby improvements are exhausted — and they exhibit path dependence (starting configuration determines outcome). The "rugged landscape" is a metaphor for organizational *attribute interdependencies*, not knowledge accumulation.

**What I'm taking from it:** **One thing only — the canonical curve shape.** When systems improve through local adaptive search, the resulting performance curve is concave with diminishing returns. Levinthal is the canonical citation for that shape in the organizational literature. We are not borrowing the NK math, the fitness concept, or the form-space framing — only the shape. This lets H3's prevention_effect plateau be defended as the recognized signature of local adaptive search rather than a simulation artifact.

**Connection to my simulation:** Used as a one-sentence shape-defense citation for H3's prevention_effect sweep (0.0 → 0.5, ~30% reduction with diminishing marginal returns). When a committee member asks "why does the curve flatten — is this a quirk of your simulation?", Levinthal authorizes the answer: "the concave diminishing-returns shape is the canonical signature of local adaptive search, established in Levinthal (1997); our H3 plateau is consistent with that pattern." **Future-work hook:** Levinthal's headline result is *path dependence* — where you start determines where you end up. Our simulation does not currently vary initial conditions for H3, so we do not test this. Varying starting team configurations to see whether some lock teams into persistently low-learning trajectories is a natural extension that would engage Levinthal's full payload, not just the curve-shape bit.

**Citation sentence:**
> *"The concave diminishing-returns shape observed in the prevention\_effect sweep is the canonical signature of local adaptive search on interdependent landscapes \cite{levinthal1997} --- a shape Levinthal established as foundational in adaptation dynamics, here recovered in the H3 marginal-gains plateau."*

**What it does NOT claim:**
- Does NOT model knowledge accumulation, learning curves, or epistemic development — fitness landscape is organizational *form* space, not *knowledge* space
- Ruggedness stems from attribute interactions, not information integration
- Does NOT support claims about the *magnitude* of H3's plateau — only about the *shape* (concave, diminishing returns) being a recognized adaptation phenomenon
- Does NOT supply the absorptive capacity framework — that is Cohen & Levinthal (1990), a *different* Levinthal paper used elsewhere in this bibliography
- Does NOT test path dependence in our simulation — that is flagged as future work

---

### 32. Müller, Kudic & Vermeulen (2021) — The Influence of the Structure of Technological Knowledge on Inter-Firm R&D Collaboration: An ABM Approach

**Journal/Source:** Journal of Business Research, 129, 570–579
**Bib key:** `muller2021`

**Author authority:** Matthias Müller, Muhamed Kudic, and Ben Vermeulen are a German innovation-economics group working at the intersection of evolutionary economics, network science, and agent-based modeling — Müller's group has produced multiple ABM papers on R&D networks; Kudic (Bremen) specializes in inter-firm network dynamics; Vermeulen (Hohenheim) is a computational economist focused on industrial dynamics. *Journal of Business Research* is an ABDC-A ranked peer-reviewed venue with broad reach in applied business and management research; not the absolute top tier (ASQ/Org Science) but a legitimate methodological reference for ABM of knowledge networks.

<!-- Personal note: this was the first paper I read when starting the thesis. It established for me that ABM of knowledge dynamics in organizational networks was a viable, published methodology — the proof-of-concept that made me confident the postmortem-sharing ABM idea wasn't crazy. Methodological forefather of this thesis even though the domain (inter-firm R&D) differs from mine (within-firm incident learning). -->

**Raw notes:**
- **Agents = firms;** each firm starts with an "endowment" of technological knowledge nodes
- **Knowledge = a directed graph:** ideas are nodes; "X builds on Y" is a directed edge; some regions are dense (mature tech with lots of prior art), others sparse (frontier)
- **Discovery via recombination:** firms can invent a new node only by combining "ancestor" nodes they already own — lock-in occurs when a firm has run out of accessible recombinations (missing crucial ancestors)
- **Collaboration mechanism:** R&D partnerships pool knowledge so partners can recombine each other's nodes; partner selection uses a logit model based on cognitive distance
- **Cognitive-distance trade-off (inverted-U):** too-similar partners produce redundancy without new ancestors; too-distant partners share no recombination base; sweet spot in the middle — the *same inverted-U* Nooteboom (2007, Entry 16) formalizes at the individual cognitive level
- **Scope trade-off:** narrow scope reduces lock-in (focus where you have ancestors) but creates redundancy; broad scope avoids redundancy but increases lock-in risk
- **Network endogeneity:** successful joint discoveries strengthen ties; the collaboration network at step 500 is *path-dependent* on which firms succeeded together — the network *evolves* over the run
- 500-step simulation with parameter sweeps

**Summary:** ABM study of how technological knowledge structure shapes inter-firm R&D collaboration. Demonstrates that collaboration becomes essential when knowledge is complex (firms get locked-in without it), identifies cognitive-distance and scope trade-offs in partner selection, and shows that collaboration networks evolve endogenously based on success history.

**What I'm taking from it:** A methodological precedent — ABM of knowledge networks in organizations is a published, peer-reviewed research program. The earlier "nearly identical methodology" framing in PAPERS_TO_READ.md was overstated and is corrected here: this is a methodological *cousin* in a different domain, not a near-replica. The cognitive-distance inverted-U is the same shape Nooteboom (2007) formalizes individually, suggesting the inverted-U is a general property of knowledge-recombination systems that future work could test in the postmortem-sharing setting.

**Connection to my simulation:** Used in Chapter 2 (Literature Review) to do **two specific jobs**:

1. **Methodological legitimacy.** "ABM of knowledge networks in organizations is an established research program with peer-reviewed precedent (Müller et al. 2021)." This puts the method in a published lineage rather than presenting it as novel.

2. **Domain bridging.** Müller et al. study the *creation of new knowledge through inter-firm recombination*; this thesis studies the *propagation of incident knowledge through within-firm sharing*. The citation lets the thesis say "ABM of knowledge networks is established; we extend it to a different organizational locus (within-firm) and a different knowledge type (incident-driven capability)."

Parallels: agents in a network, knowledge sharing, network effects on outcomes, parameter sweeps. Differences: inter-firm strategic partnerships vs. within-firm policy-set sharing; knowledge as a graph of recombinable nodes vs. scalar capability per team; endogenous network formation vs. fixed topology as treatment variable; innovation (new knowledge creation) vs. learning (capability acquired from failures).

**Citation sentence:**
> *"Agent-based simulation has proven effective for studying knowledge dynamics in organizational networks; Müller et al.\ \cite{muller2021} model inter-firm R\&D collaboration as a complex adaptive system in which knowledge structure shapes recombination, lock-in, and the endogenous evolution of partnership ties. The present work extends this methodological tradition from inter-firm innovation to the within-firm context of software-incident learning."*

**What it does NOT claim:**
- Not about software incidents — inter-firm R&D
- Does not model organizational learning from failures or postmortem processes
- Assumes rational partner selection based on technological distance, not peer recommendation or incident narrative
- Does NOT support claims about endogenous network formation — our topology is treated as exogenous (a treatment variable); Müller's network endogeneity is a future-work hook
- Does NOT theorize the magnitude of any cross-team learning effect — only establishes the methodological precedent for studying knowledge dynamics with ABM

---

### 33. Carley (1992) — Organizational Learning and Personnel Turnover

**Journal/Source:** Organization Science, 3(1), 20–46
**Bib key:** `carley1992`

**Author authority:** **Kathleen M. Carley** (Carnegie Mellon University) is the founder of computational organization theory and director of CASOS (Center for Computational Analysis of Social and Organizational Systems) at CMU. Joint appointments in computer science, engineering & public policy, and the Tepper School of Business. When a methodology committee asks "is ABM a legitimate way to study organizations?", Carley is the canonical answer — she has been doing exactly this since the early 1990s in top venues. *Organization Science* is INFORMS' Tier 1 organization-theory journal (~7% acceptance); this paper has 1,500+ citations and is on every PhD reading list for organizational learning. Her later work (CONSTRUCT, ORA) elaborated this lineage substantially — *that* methodology is not what is invoked here; this entry cites the 1992 foundational result only.

**Raw notes:**
- **Model in plain English:** workers (agents) each handle a piece of a larger organizational task; org performance depends on individual learning *plus* the organizational structure that coordinates the pieces.
- **Knowledge is role-specific.** Each agent accumulates knowledge of their sub-task with experience; performance on that sub-task improves over time.
- **Org performance = (accumulated role-level knowledge) × (structure that integrates the sub-tasks).** Knowledge alone is not enough; coordination matters.
- **Turnover mechanism.** When an agent leaves, their role-knowledge is lost; the replacement starts from zero and must re-learn.
- **Task interdependence is the key parameter.** Low interdependence = sub-tasks are independent (decomposable); high interdependence = sub-tasks tightly coupled, requiring coordination.
- **Headline finding:** turnover hurts organizational learning *much more* under high interdependence than under low. Losing one worker disrupts the coordination the org has built up — the loss cascades through dependencies.
- **Methodological note:** uses Soar-based agents (her early-1990s framework). Carley's later work (CONSTRUCT, ORA) is a different and more elaborate research program — *not* what is invoked when citing the 1992 paper.

**Summary:** Foundational ABM-of-organizational-learning study. Organizational knowledge is distributed across roles; the rate at which it is lost (turnover) interacts with task interdependence to determine net learning. Distributed-knowledge organizations performing interdependent tasks are *more vulnerable* to knowledge loss because coordination cascades amplify the disruption. Establishes the ABM tradition for modeling organizational learning as an emergent property of distributed agent-level knowledge under structural constraints — the methodological lineage this thesis builds on.

**What I'm taking from it:** A foundational methodological precedent and a structural-resilience parallel. Carley shows that (a) ABM is the right tool for studying distributed-knowledge dynamics, and (b) knowledge-loss effects depend on how the org integrates work — both points carry forward to the postmortem-sharing setting.

**Connection to my simulation:** Carley does **three specific jobs**:

1. **Methodological legitimacy (Chapter 3).** Carley is the organizational-learning-specific anchor of the methodology-defense citation quartet. Pair with: Epstein 1999 (Entry 25, generative-science philosophy), Harrison et al. 2007 (Academy of Management Review, ABM in management), Bonabeau 2002 (PNAS, ABM in social systems). The other three defend ABM in general; **Carley shows ABM has been used productively for exactly the kind of question this thesis asks** — how distributed knowledge survives organizational dynamics — in the field's top journal.

2. **Knowledge-decay precedent (Chapter 3 mechanism + Chapter 4 H3 framing).** The simulation's per-tick `knowledge_decay` parameter is a modeling choice that needs justification. Carley provides it: knowledge-loss rate is established as a key driver of net organizational learning. Carley models loss as discrete (a worker leaves); this thesis models it as continuous (per-tick decay). The mechanism differs but the higher-level concept — *knowledge is fragile and that fragility matters* — is established literature.

3. **Interdependence-resilience parallel to H1 (Chapter 4 H1 discussion).** Carley's *task interdependence* maps conceptually to this thesis's *sharing scope*. Her result — distributed-knowledge orgs lose more under interdependence — has a structural parallel: NONE/LOCAL keep knowledge confined; NEIGHBOR/GLOBAL distribute it redundantly across the network. Under NEIGHBOR/GLOBAL, multiple teams hold the same incident knowledge, so the org is *more resilient* to any one team forgetting (decay) or turning over. This is a high-level conceptual parallel — not a direct mechanism transfer — but it grounds the H1 resilience framing in established literature.

**Citation sentence:**
> *"The agent-based modeling approach taken here builds on a tradition of simulating organizational learning as the structurally mediated accumulation of distributed agent-level knowledge \cite{carley1992,harrison2007,epstein1999}. Carley in particular demonstrates that the rate of knowledge loss interacts with task interdependence to determine net organizational performance --- a finding the present model extends from personnel turnover to incident-driven postmortem learning."*

**What it does NOT claim:**
- Not about software incidents — generic organizational task performance
- Turnover ≠ knowledge decay exactly: Carley models discrete loss; this thesis models continuous decay per tick. The mechanisms differ but the high-level result transfers
- Does not model network topology — uses task interdependence as the structural lever
- The H1 parallel is conceptual (distributed-knowledge orgs are more resilient under coordination demands), not a direct mechanism transfer
- Citing Carley (1992) for the **foundational result** of distributed-knowledge fragility under interdependence; her later CONSTRUCT/ORA frameworks are different and more elaborate research programs and are NOT invoked here — the temporal precision matters because conflating 1992 Soar-based modeling with later CONSTRUCT-style dynamic-network agents would be an anachronism

---

### 34. Leveson (2004) — A New Accident Model for Engineering Safer Systems (STAMP)

**Journal/Source:** Safety Science, 42(4), 237–270
**Bib key:** `leveson2004`

**Author authority:** **Nancy G. Leveson** (MIT, Professor of Aeronautics and Astronautics, joint with Engineering Systems) is the most influential safety engineering theorist of the last 40 years. Author of *Safeware: System Safety and Computers* (1995) — the book that defined software safety engineering as a discipline — and *Engineering a Safer World* (2011, MIT Press, open access) — the canonical STAMP textbook. Authored the foundational Therac-25 case study now required reading in every software safety course. STAMP is used by NASA, FAA, FDA, and major defense contractors for hazard analysis. *Safety Science* (Elsevier) is the leading interdisciplinary safety research journal; this paper has 4,000+ citations and is *the* canonical STAMP reference.

**Raw notes:**
- **STAMP** = Systems-Theoretic Accident Model and Processes
- **The chain-of-events critique:** traditional accident models (Heinrich's domino theory, fault trees, root-cause analysis) treat accidents as linear sequences A → B → C → accident, then "fix the root cause." This worked for mechanical systems where failures *were* discrete component breakdowns. **It fails for software-intensive systems** because (a) software doesn't fail by breaking — it does *exactly what it was told to do* in a context the designers didn't anticipate; (b) most modern accidents involve no individual component failure at all — only unsafe *interactions* between components that were each working correctly; (c) "root cause" framing is misleading when the cause is distributed across design, operation, regulation, and management.
- **Accidents as emergent properties of inadequate control.** Every safety-critical system has a hierarchical control structure: operators → supervisors → management → regulators → government. Each layer enforces safety constraints on the layer below via rules, monitoring, feedback loops, and decision authority. An accident occurs when control loops become inadequate: missing feedback (controllers don't know what the system is doing), broken communication, conflicting goals (production vs. safety), mental-model mismatches (controllers think system is in state X when it's actually in state Y).
- **Investigation reframing:** instead of "what failed?", STAMP asks "which safety constraints were violated, and which control loops failed to enforce them?"
- Applies broadly: aerospace, medical, nuclear, software

**Summary:** STAMP reconceptualizes accidents as emergent properties of inadequate control across hierarchical socio-technical systems, replacing the chain-of-events / domino model that was inherited from mechanical systems engineering. Control structures enforce safety constraints; when communication, monitoring, or decision-making becomes inadequate at any layer, the system state becomes unsafe. The framework is now the dominant theoretical lens for accident causation in software-intensive domains.

**What I'm taking from it:** The philosophical grounding for the simulation's stochastic incident generator. Without Leveson, the stochastic generator is a modeling convenience; with Leveson, it is a methodologically defensible reflection of how complex systems actually fail — emergent, multi-causal, not a deterministic chain. Pair with Cook (1998) for the practitioner/clinical version of the same argument.

**Connection to my simulation:** Used in Chapter 2 (accident-causation background) and Chapter 3 (justifying the stochastic incident generator) to do **one specific job**: pre-empt the objection "shouldn't you model the actual causal chain of each incident?" The Leveson-grounded answer: modern incidents *aren't* causal chains; they are emergent stochastic outcomes of inadequate control across a complex socio-technical system. Modeling them stochastically is *more* faithful than modeling them as deterministic chains would be.

**Leveson + Cook pairing.** This is a two-citation pair with explicit role split: **Leveson 2004 = formal academic framework** (the systems-theoretic theory); **Cook 1998 = practitioner/clinical observational version** (the aphoristic distillation, "Catastrophe is always just around the corner"; "Defenses against failure are layered and partial"). Together they provide theoretical and observational anchors for the "incidents are emergent, not chains" framing — same structure as the DevOps triangle (Forsgren empirical / Kim prescriptive / Allspaw observational) used elsewhere in this bibliography.

**Citation sentence:**
> *"Systems-theoretic accident analysis frames complex-system failures as emergent properties of inadequate control rather than chains of component failures \cite{leveson2004,cook1998}, motivating the simulation's treatment of incidents as stochastic outcomes of subsystem state and recent activity rather than as deterministic consequences of single root causes."*

**What it does NOT claim:**
- Not specific to software — applies to aerospace, medical, nuclear (general framework, applied here to software)
- Does not address postmortem analysis or organizational learning directly
- Requires detailed control-structure modeling per domain in its full application
- The IEEE TDSC paper "A Systems-Theoretic Approach to Safety in Software-Intensive Systems" (also 2004) is a *different* paper — use the Safety Science 42(4) citation as the canonical STAMP source
- **Crucially: STAMP is a theory of accident *causation*, not a theory of *learning from* accidents.** Learning is the work of Cohen & Levinthal (absorptive capacity), Argote & Miron-Spektor (learning from experience), and Allspaw/Edmondson (postmortem culture). Leveson grounds the *stochastic incident generator*, not the *learning pipeline* — keep these citations in their respective lanes

---

### 35. Allspaw (2012) — Blameless PostMortems and a Just Culture

**Journal/Source:** Etsy Code as Craft (engineering blog), May 22, 2012
**Bib key:** `allspaw2012`

**Author authority:** **John Allspaw** was VP of Technical Operations at **Etsy** at the time of writing. Co-author of *Web Operations* (O'Reilly, 2010) and *The Art of Capacity Planning* (O'Reilly, 2008). Earned an MSc in **Human Factors and Systems Safety** from **Lund University under Sidney Dekker** (the author of Entry 17 in this bibliography). After Etsy, he co-founded **Adaptive Capacity Labs** with **Richard Cook** (Entry on complex systems failure) and David Woods. He is one of the most influential figures bridging academic safety science (Hollnagel, Dekker, Cook, Woods) and software engineering practice; this blog post is the practitioner output of someone with serious formal safety-science training, not "an engineer with a blog." The post is the document that, more than any other, established the blameless postmortem as standard practice — Google, Stripe, Netflix, and the broader SRE community all reference it as foundational.

**Raw notes:**
- **Reject the Bad Apple Theory.** Traditional incident response assumes a single bad actor (incompetent, careless, negligent) caused the failure → identify, blame, punish. Allspaw, following Dekker, argues this is both *causally wrong* (incidents are emergent systemic properties — same Leveson/Cook argument from Entry 34) and *strategically destructive* (punishment destroys the org's ability to learn — engineers hide problems, avoid risky-but-necessary work, stop sharing).
- **Just Culture (three categories).** Drawing on Dekker and James Reason:
  - **Human error** — honest mistakes by competent people in good faith → learn from them; do not blame
  - **At-risk behavior** — shortcuts/workarounds drifting from procedure → coach, address systemic incentives
  - **Reckless behavior** — knowing violation with conscious disregard → appropriate consequences
  Blamelessness ≠ absolution; reckless behavior still has consequences. But the *vast majority* of incidents involve honest mistakes, and treating those as blameworthy destroys learning capacity.
- **First Story vs. Second Story.**
  - *First Story* = surface narrative blaming an individual ("the engineer pushed a bad config and the site went down")
  - *Second Story* = the cognitive context — *why* did the engineer believe the config was safe? what feedback would have surfaced the mistake? what other engineers would have made the same choice in the same circumstances? — the actionable systemic insight.
  The blameless postmortem is a *technique* for surfacing Second Stories: removing the threat of blame is what allows the engineer to honestly explain what they were thinking.
- **Hollnagel pillars:** accidents occur when people believe **risk is justified** OR **danger is impossible/irrelevant** — these are *cognitive* states, only knowable by asking the engineer, who will only answer honestly absent threat of punishment.
- **Key mechanism:** when engineers feel safe, they willingly contribute expertise to remediation — this is the bridge between theory (Edmondson's psychological safety) and practice (org-level reliability outcomes).

**Summary:** Argues that treating incidents as learning opportunities rather than occasions for blame yields better safety outcomes. Just Culture distinguishes between human error, at-risk behavior, and reckless behavior. Blameless postmortems are a structured technique for surfacing "Second Stories" — the cognitive context that produces actionable systemic insight, only obtainable when engineers can speak honestly without fear of punishment. The founding articulation of blameless postmortems as software-engineering practice.

**What I'm taking from it:** Practitioner grounding (existence proof) for the simulation's assumption that agents share incident knowledge truthfully. Without honest sharing, H1's sharing-scope hypotheses are meaningless — if teams hide incidents, the policy lever doesn't move knowledge. Allspaw documents that mature engineering orgs *do* implement blameless culture, making this assumption defensible rather than naive.

**Connection to my simulation:** Used in Chapter 2 (DevOps and incident-learning practice section) and Chapter 3 (justifying the truthful-sharing assumption). Plays in **two citation triangles**:

1. **Blameless-sharing assumption triangle** (defends the truthful-sharing modeling assumption):
   - Edmondson 1999 (Entry 20) = **theoretical** — psychological safety as a measurable team-level property, peer-reviewed in *ASQ*
   - Allspaw 2012 (this entry) = **practitioner observational** — founding articulation of blameless postmortem technique
   - Lunney & Lueder 2016 (Entry 2, Google SRE Book Ch. 15) = **scale demonstration** — practice institutionalized at Google scale

2. **DevOps practice triangle** (defends the DevOps performance claims; see Entry 29):
   - Forsgren 2018 (Entry 5) = **empirical** — high performers deploy 200× more, fail 3× less
   - Kim 2016 (Entry 29) = **prescriptive** — the Three Ways framework
   - Allspaw 2012 (this entry) = **practitioner observational** — what blameless culture actually looks like in operation

Allspaw doing double duty across triangles is intentional — he is the canonical observational vertex for both incident-learning culture and DevOps reliability practice.

**Citation sentence:**
> *"Industry practice at mature engineering organizations like Etsy grounds the assumption that incidents can be discussed openly through structured blameless postmortems \cite{allspaw2012}, complementing Edmondson's \cite{edmondson1999} empirical findings on psychological safety in team learning."*

**What it does NOT claim:**
- Blog post — not peer-reviewed in the academic sense. Counter-balanced by author's formal academic safety-science training (Lund MSc under Dekker) and current academic-practitioner consultancy (Adaptive Capacity Labs with Cook and Woods). The peer-edited *Web Operations* (O'Reilly, 2010) Chapter 13 by Allspaw is the defensive backup citation if a committee member pushes back on the blog-post venue.
- Does NOT prove blamelessness improves reliability empirically — that empirical work is Edmondson 1999 (psychological safety) and Forsgren et al. 2018 (DevOps performance correlations)
- Generalization beyond Etsy's context is implicit; the *scale* generalization is supplied by Lunney & Lueder (Google SRE Book) as the third triangle vertex
- Does NOT prescribe optimal postmortem structures or methodologies — focuses on the cultural prerequisites
- Allspaw's *role* here is observational/practitioner — not used as evidence for any quantitative claim or methodological choice; keep it in this lane

---

### 36. Sujan, Huang & Braithwaite (2017) — Learning from Incidents in Health Care: Critique from a Safety-II Perspective

**Journal/Source:** Safety Science, 99, 115–121
**Bib key:** `sujan2017`

**Author authority:** **Mark Sujan** (then Warwick Medical School; now Director of Human Factors Everywhere Ltd.) is a leading UK patient-safety researcher bridging human factors engineering and healthcare practice. **Huayi Huang** (Warwick Medical School) studies patient safety. **Jeffrey Braithwaite** (Macquarie University, Sydney) is **one of the world's leading healthcare systems researchers** — Founding Director of the Australian Institute of Health Innovation, President-elect (at the time) of the International Society for Quality in Health Care, and co-author with Erik Hollnagel and Robert Wears of the *Resilient Health Care* book series that brought Safety-II to healthcare. *Safety Science* (Elsevier) is the leading interdisciplinary safety research journal — the same venue as Leveson's STAMP paper (Entry 34); their co-publication there is not coincidence (it is the canonical venue for cross-domain safety theory). This is a serious paper by serious researchers, not a marginal critique.

**Raw notes:**
- **Safety-I (the dominant paradigm):** safety = the absence of negative events; learn by analyzing what goes wrong (RCA, fault trees, incident reporting, NRLS-style central databases). Implicit assumption: things go right because the system was designed correctly; things go wrong because of failures.
- **Safety-II (Hollnagel's reframing):** safety = the system's ability to make dynamic adjustments and trade-offs that keep it functioning under varying conditions. Learn by analyzing how everyday work succeeds — adaptive practices, near-miss recoveries, work-as-imagined vs. work-as-done. Implicit assumption: things go right because of *active adaptation*, not because the design was perfect.
- **Hollnagel anchor:** Safety-II is **Erik Hollnagel's** framework — the same theorist Allspaw (Entry 35) draws on for the "risk justified / danger impossible/irrelevant" framing. Sujan et al. apply Hollnagel's framework specifically to healthcare incident learning.
- **Healthcare argument (the paper's specific contribution):**
  1. Healthcare incident reporting (NRLS, similar systems) has documented organizational barriers to effective learning — even within Safety-I, the paradigm struggles.
  2. Clinicians generate enormous safety-relevant knowledge during *successful* everyday work — adapting to staff shortages, working around equipment quirks, catching colleagues' near-mistakes, escalating ambiguous symptoms.
  3. None of this is captured by incident reporting because no incident *occurred* — yet the adaptive practices that prevented incidents are exactly what the org should institutionalize.
  4. A Safety-II framework would *augment* (not replace) incident reporting with structured study of routine successful operations.
- **Critical positioning:** Safety-II *complements* Safety-I — the paper does not argue Safety-I learning is wrong or unnecessary, only that it is *incomplete*.

**Summary:** Peer-reviewed critique applying Hollnagel's Safety-II framework to healthcare incident learning. Argues that exclusive reliance on incident reporting (Safety-I) misses the majority of safety-relevant knowledge, which is generated during successful everyday adaptive work. Safety-II — studying how clinicians keep things going right under varying conditions — would *complement* (not replace) incident-focused systems.

**What I'm taking from it:** A scope-honesty citation. The simulation captures only Safety-I learning dynamics (knowledge acquired from incidents). Sujan et al. is the citation that *names this scope*, *names what is excluded* (Safety-II adaptive learning), and *credits the excluded paradigm with future-work status* — making the modeling choice a defensible scoping decision rather than an unexamined assumption.

**Connection to my simulation:** Used in **Chapter 5 (Limitations and Discussion)** to do **one specific job**: pre-empt the committee objection — "Why does your model assume learning only happens from failures? Doesn't that ignore most of the safety-relevant knowledge in software organizations?" The Sujan-grounded answer: the model captures Safety-I dynamics by deliberate scope; Safety-II is named explicitly as a future-work extension, not silently omitted.

**Concrete Safety-II extensions for the simulation (future work).** A Safety-II-aware version of this model could:
- Fire Stage-1 acquisition on **near-miss events** (deployments that almost caused incidents but were caught by review, monitoring, or adaptive response)
- Add a separate `successful_adaptation_rate` parameter modeling knowledge gained from routine successful releases
- Distinguish *reactive learning* (incident-driven, current model) from *proactive learning* (adaptation-driven, Safety-II extension)
- Model "work-as-imagined vs. work-as-done" gaps as a distinct knowledge source

**Systems-safety theoretical backdrop.** Sujan is the fourth member of the systems-safety citation cluster that frames the thesis:
- **Dekker 2014** (Entry 17) — Just Culture and the human-error reframing
- **Leveson 2004** (Entry 34) — STAMP, accidents as inadequate control (formal academic)
- **Cook 1998** — *How Complex Systems Fail* (practitioner observational, paired with Leveson)
- **Sujan 2017** (this entry) — Safety-II, learning from successful everyday work (scope-honesty)

Together these establish: incidents are emergent (Leveson + Cook); blame destroys learning (Dekker → Allspaw); incident-only learning is incomplete and the thesis scopes within Safety-I deliberately (Sujan).

**Citation sentence:**
> *"This work models Safety-I learning dynamics, in which knowledge accumulation is driven exclusively by incidents. The Safety-II perspective \cite{sujan2017} --- learning from how systems succeed under varying conditions, including near-miss recoveries and routine adaptive work --- represents a natural future-work extension that the present model does not represent. Distinguishing these paradigms in advance, rather than conflating them, allows the Safety-I dynamics to be studied cleanly."*

**What it does NOT claim:**
- Not about software incidents — about healthcare; software-engineering transfer is interpretive
- Does not invalidate incident reporting or root-cause analysis — argues for *complementing* it
- Sujan et al. argue Safety-II *complements* Safety-I — they do NOT argue Safety-I learning is wrong or unnecessary. The thesis's Safety-I focus is therefore *consistent with* their position; the limitation acknowledged here is one of *scope*, not of *paradigm error*
- Empirical findings (barriers to incident learning) are healthcare-specific; software-engineering transfer is interpretive
- Sujan's *role* here is scope-honesty (naming what the model doesn't capture); not used as evidence for any quantitative claim, methodological choice, or results interpretation — keep it in this lane

---