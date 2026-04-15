# Code Walkthrough: Organizational Learning from Software Incidents
## Agent-Based Simulation — `model.py`

> **How to use this document.** Read Section 1 first and draw the big-picture diagram on paper. Then read each subsequent section and draw the supplementary diagrams as you go. Every section answers three questions: *what* does this code do, *how* does it do it, and *why* was it designed this way.

---

# Section 1: The Big Picture (One Timestep — Draw This First)

---
### 🔑 Analogy First — Before You Read the Technical Details

**The analogy:** Imagine a hospital network running for one full year. Each day, the chief medical officer runs the same routine: check whether any departments had a medical error, see who can learn from it, then log the outcomes. Every single day follows this exact three-phase rhythm — housekeeping, errors and learning, then recording — and the lessons from Monday's error in the ER make Tuesday's ER a little safer.

**What maps to what:**
- One day in the hospital system → one simulation timestep `t`
- Housekeeping (staff rotations, new patients arriving) → pre-step decay and deployment rolls
- A medical error occurring in a department → an incident being generated for a team
- Departments reviewing the error and updating their procedures → the four-stage learning pipeline
- The chief medical officer logging MTBF, MTTR, harm rates → Phase 3 metrics collection
- The safety improvement feeding back into tomorrow's error rate → the feedback loop from Phase 2 knowledge into Phase 1 probabilities

**Now read the technical detail below with this picture in your head.**

---

Before reading anything else, draw this diagram on paper. It shows exactly what happens during a single call of the main `for t in range(params.steps)` loop in `run_simulation()`. Every box corresponds to real lines of code. The arrows show control flow. This is the skeleton onto which every other section hangs.

```
┌─────────────────────────────────────────────────────────────┐
│                  START OF TIMESTEP  t                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  PRE-STEP HOUSEKEEPING                                      │
│  1. Decay deployment counters   (recent_deployments[st]-=1) │
│  2. Roll random deployments     (p = deployment_rate = 0.1) │
│  3. Apply knowledge decay       K *= (1 - δ)   [δ = 0.001] │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 1 — INCIDENT GENERATION   (for each team)            │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Compute p_incident =                               │    │
│  │    base_rate * (1 - Kp*0.5) * deployment_modifier  │    │
│  │  Roll rng.random() < p_incident?                    │    │
│  │       NO ──► skip                                   │    │
│  │       YES ──► pick incident_type (susceptibility    │    │
│  │               weighted), compute severity,          │    │
│  │               detection_time, resolution_time,      │    │
│  │               cost, learnable_knowledge             │    │
│  │               append Incident to list               │    │
│  │               source team bypasses pipeline→learns  │    │
│  └─────────────────────────────────────────────────────┘    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 2 — FOUR-STAGE LEARNING PIPELINE                     │
│  (for each incident generated this timestep,                │
│   for each eligible team)                                   │
│                                                             │
│  get_learners_for_scenario() → [team ids]                   │
│       │                                                     │
│       ▼                                                     │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ STAGE 1: ACQUISITION                                 │   │
│  │   Did this team hear about the incident?             │   │
│  │   p_acquire = acq_prob * edge_weight                 │   │
│  │               (or signal_decay^path_length)          │   │
│  │   Roll → acquired_incidents.add(id) on success       │   │
│  └──────────────────┬───────────────────────────────────┘   │
│                     │ only if acquired                      │
│                     ▼                                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ STAGE 2: ASSIMILATION                                │   │
│  │   Did the team understand it?                        │   │
│  │   p_assim = (0.7*cog_factor + 0.3*doc_qual)         │   │
│  │             * assim_prob * (0.5 + 0.5*relevance)    │   │
│  │   where cog_factor = inverted-U(cosine_similarity)  │   │
│  │   Roll → assimilated_incidents.add(id) on success   │   │
│  └──────────────────┬───────────────────────────────────┘   │
│                     │ only if assimilated                   │
│                     ▼                                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ STAGE 3: TRANSFORMATION                              │   │
│  │   Did the team recombine it with existing knowledge? │   │
│  │   MINIMAL mode: p_transform =                        │   │
│  │     (0.8*cog_factor + 0.2*doc_qual)                  │   │
│  │     * transform_prob * (0.5 + 0.5*relevance)        │   │
│  │   Roll → transformed_incidents.add(id) on success   │   │
│  └──────────────────┬───────────────────────────────────┘   │
│                     │ only if transformed                   │
│                     ▼                                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ STAGE 4: EXPLOITATION                                │   │
│  │   Did the team act on it?                            │   │
│  │   relevance = team.get_susceptibility(incident_type) │   │
│  │   p_exploit = exploit_prob * (0.5 + 0.5*relevance)  │   │
│  │   Roll → team.learn(type, dim, amount) for each dim │   │
│  │         cumulative_learning_cost += learning_cost    │   │
│  └──────────────────────────────────────────────────────┘   │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  PHASE 3 — METRICS COLLECTION                               │
│  Record incident counts, durations, severities, costs       │
│  Record stage rates (acquired/assimilated/etc. per team)    │
│  Record avg_prevention/detection/mitigation knowledge       │
│  Record MTBF, MTTR, MTTD running means                      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  END OF TIMESTEP  t                         │
│              loop back to t+1                               │
└─────────────────────────────────────────────────────────────┘
```

**Key insight to write on your diagram:** The simulation has a *feedback loop*. Knowledge accumulated in Phase 2 feeds back into Phase 1 of the *next* timestep, making incidents less frequent (Kp), less severe (Km), and faster to detect (Kd). This is the core causal mechanism of the model.

---

# Section 2: The Data Structures (What Exists Before Anything Runs)

---
### 🔑 Analogy First — Before You Read the Technical Details

**The analogy:** Before the hospital network opens its doors on Day 1, the administrator fills out a master configuration binder: how many departments exist, what the baseline error rate is, how rigorously postmortems are written, and how quickly institutional knowledge fades when staff turn over. Each department also gets its own personnel file — its skill scores across three competency areas — and the building blueprint shows which departments share hallways and can easily talk to each other.

**What maps to what:**
- The master configuration binder → `SimulationParams` dataclass (every tunable parameter)
- Each department's personnel file with skill scores → `Team` object with its `knowledge` dictionary
- A filed incident report → `Incident` object with all its measured attributes
- The building blueprint showing which departments share hallways → the NetworkX `graph`
- The table showing which departments are prone to which error types → `DEFAULT_SUSCEPTIBILITY` matrix

**Now read the technical detail below with this picture in your head.**

---

Before `run_simulation()` enters its main loop, it constructs the following objects. Understand these first; everything else is operations on them.

---

## 2.1 `SimulationParams` — the control panel

`SimulationParams` is a Python `dataclass` (lines 231–305). A dataclass is just a class whose only job is to hold data fields with default values; it auto-generates `__init__`, `__repr__`, etc. Every parameter that governs the simulation lives here. Running `SimulationParams()` with no arguments gives you a sensible default experiment.

**Structural parameters**

| Field | Default | What it controls |
|---|---|---|
| `seed` | 42 | NumPy random seed — makes the run reproducible |
| `num_teams` | 6 | Number of team-agents in the simulation |
| `steps` | 365 | Number of timesteps (each = one business day) |
| `learning_scenario` | NEIGHBOR | Which teams are eligible to learn from each incident |
| `network_topology` | "watts_strogatz" | Graph structure of the communication network |

**Network parameters**

| Field | Default | What it controls |
|---|---|---|
| `er_p` | 0.3 | Erdős-Rényi: probability each pair of nodes is connected |
| `ws_k` | 4 | Watts-Strogatz: each node connects to k nearest neighbors before rewiring |
| `ws_p` | 0.1 | Watts-Strogatz: rewiring probability (controls small-worldness) |
| `ba_m` | 2 | Barabási-Albert: edges each new node brings when joining the graph |

**Incident generation parameters**

| Field | Default | What it controls | Citation |
|---|---|---|---|
| `base_incident_rate` | 0.05 | Per-team, per-day probability of an incident before modifiers | — |
| `deployment_rate` | 0.1 | Per-team, per-day probability of a deployment occurring | — |
| `deployment_risk_multiplier` | 1.5 | Incident rate multiplier active for 3 days after a deployment | [PAPER] Forsgren et al. (2018): deployment frequency and stability are core DORA metrics; high deployment frequency without quality gates increases change-failure rate |

**Incident characteristic parameters**

| Field | Default | What it controls |
|---|---|---|
| `incident_severity_base` | 3.0 | Mean severity (1–5 scale) drawn from normal distribution |
| `incident_severity_std` | 1.0 | Spread in severity |
| `incident_duration_base` | 2.0 | Mean total incident duration in hours |
| `incident_duration_std` | 1.0 | Spread in duration |

**Learning pipeline probabilities** — these are the per-stage *base* probabilities, before cognitive-distance and relevance modifiers are applied:

| Field | Default | Stage it controls | Citation |
|---|---|---|---|
| `acquisition_probability` | 0.9 | Stage 1: hearing about the incident | [PAPER] Zahra & George (2002): acquisition is the most reliable stage; organizations generally hear about significant incidents |
| `assimilation_probability` | 0.7 | Stage 2: understanding root cause | [PAPER] Cohen & Levinthal (1990): prior knowledge is the gate for understanding; not all heard incidents are understood |
| `transformation_probability` | 0.7 | Stage 3: recombining with existing knowledge | [PAPER] Zahra & George (2002): transformation requires integrating new knowledge into existing schemas — harder than assimilation |
| `exploitation_probability` | 0.6 | Stage 4: implementing changes | [PAPER] March (1991): exploitation is costly (developer time, process change); organizations often fail to act on knowledge they possess |

**Cognitive factors**

| Field | Default | What it controls | Citation |
|---|---|---|---|
| `documentation_quality` | 0.5 | Quality of postmortems, [0,1]; boosts assimilation and transformation | [PAPER] Lunney & Lueder (2016): well-structured postmortems (with timelines, root-cause analysis, and action items) are the primary knowledge transfer mechanism in SRE |
| `use_inverted_u` | True | Whether to apply the Nooteboom inverted-U curve | [PAPER] Nooteboom et al. (2007): cognitive proximity (similarity) has a non-linear effect — see Section 5 |
| `signal_decay` | 0.8 | Per-hop decay in acquisition probability in NEIGHBOR scenario | Encodes the folk theorem that information fidelity decreases with each retelling |

**Exploitation effectiveness** — how strongly knowledge actually reduces operational outcomes:

| Field | Default | Effect | Citation |
|---|---|---|---|
| `prevention_effect` | 0.5 | Max fractional reduction in `p_incident` when Kp = 1.0 | [PAPER] Reed et al. (2019): prevention knowledge reduces incident probability through improved system understanding and defensive coding practices |
| `detection_effect` | 0.3 | Max fractional reduction in detection time when Kd = 1.0 | [PAPER] Dogga et al. (2023): detection improvements come from better alerting and runbooks — more bounded gains than prevention |
| `mitigation_effect` | 0.3 | Max fractional reduction in severity/duration when Km = 1.0 | [PAPER] Dogga et al. (2023): mitigation knowledge enables faster resolution through practiced runbooks |

**Time-based transformation (optional)**

| Field | Default | What it controls |
|---|---|---|
| `use_time_based_transformation` | False | Switches from single-roll to cumulative-effort transformation model |
| `transformation_min_effort` | 3 | Minimum timesteps before transformation can succeed (not enforced in code as a gate, but the progress rate makes it de-facto) |
| `transformation_effort_rate` | 0.2 | Base progress added per timestep; team accumulates toward 1.0 |

**Engineering costs**

| Field | Default | What it controls |
|---|---|---|
| `engineering_cost_base` | 4.0 | Base developer-hours per incident; scales with severity and duration |
| `learning_cost` | 2.0 | Developer-hours per successful exploitation event (postmortem + fix time) |

**Ablation flags**

| Field | Default | Scientific purpose |
|---|---|---|
| `knowledge_decay` | 0.001 | Daily decay rate δ; see Section 6 for half-life calculation |
| `disable_knowledge_decay` | False | Set True to run without decay — tests whether decay is load-bearing |
| `disable_source_asymmetry` | False | Set True so source team goes through pipeline like everyone else |

---

## 2.2 `Team` — the agent

Each team (lines 166–212) is a software development team that owns a subsystem. This is a `dataclass` with five categories of fields:

**Identity**
- `team_id: int` — index 0 through num_teams-1
- `subsystem: SubsystemType` — which system this team owns (DATABASE, PAYMENT, AUTH, FRONTEND, API, CACHE), assigned round-robin

**Knowledge state** — the core state variable
- `knowledge: Dict[IncidentType, Dict[str, float]]` — a nested dictionary. The outer key is one of the five `IncidentType` values. The inner key is one of the three knowledge dimensions: "prevention", "detection", "mitigation". Every value starts at 0.0 and is capped at 1.0. You can think of it as a 5×3 matrix of competence scores.

**Learning progress sets** — each is a `Set[int]` of incident IDs
- `acquired_incidents` — IDs where Stage 1 succeeded
- `assimilated_incidents` — IDs where Stage 2 succeeded
- `transformed_incidents` — IDs where Stage 3 succeeded
- `exploited_incidents` — IDs where Stage 4 succeeded

These sets serve two purposes: (1) prevent re-processing an incident a team already learned from, and (2) allow metric collection to count pipeline throughput.

**Time-based transformation state**
- `transformation_progress: Dict[int, float]` — maps incident_id to accumulated progress toward 1.0. Only relevant when `use_time_based_transformation = True`.

**Experience log**
- `incidents_experienced: List[Dict]` — records of incidents this team suffered directly. Used for per-team logging.

**Methods:**
- `get_susceptibility(incident_type)` — looks up `DEFAULT_SUSCEPTIBILITY[self.subsystem][incident_type]`. Returns 0.0–1.0.
- `get_knowledge_vector()` — flattens the 5×3 knowledge dictionary into a 15-element numpy array for cosine similarity calculation. The ordering is fixed (IncidentType outer, dimension inner), which is critical — the vectors must always be constructed identically so the similarity calculation is meaningful.
- `learn(incident_type, dimension, amount)` — adds `amount` to the specified knowledge cell, clamping at 1.0. This is the only place knowledge is increased.

---

## 2.3 `Incident` — the event record

An `Incident` (lines 215–228) is created each time a team generates an incident and persists in `all_incidents` for the entire run. It carries:

| Field | Type | What it represents |
|---|---|---|
| `incident_id` | int | Unique sequential counter |
| `timestep` | int | When it occurred |
| `source_team_id` | int | Which team suffered it |
| `subsystem` | SubsystemType | Which system was affected |
| `incident_type` | IncidentType | Drawn from susceptibility-weighted distribution |
| `severity` | float (1–5) | How bad — drives engineering cost and availability |
| `duration` | float (hours) | Total time from start to resolution (detection + resolution) |
| `detection_time` | float (hours) | Portion of duration spent before the team knew about it |
| `engineering_cost` | float (hours) | Computed as `base_cost * (severity/3.0) * (duration/2.0)` |
| `learnable_knowledge` | Dict[str, float] | How much each knowledge dimension *could* be learned from this incident — drawn uniform [0.1, 0.25] per dimension |

The `learnable_knowledge` field is important: it represents how much theoretical insight this incident contains. A team that exploits this incident gains `learnable_knowledge[dim] * relevance_factor * doc_quality_factor` knowledge in each dimension — never the full amount.

---

## 2.4 The network graph

The variable `graph` (created by `init_graph()`) is a NetworkX `Graph` object — an undirected graph where nodes are team IDs (0 through num_teams-1) and edges represent communication channels between teams.

**Why NetworkX?** NetworkX is the standard Python library for graph algorithms. It provides breadth-first search (for path length computation), degree centrality, clustering coefficients, and average path length — all metrics the simulation computes for the final results dictionary.

**What edge weights represent:** Each edge `(u, v)` has a `weight` attribute drawn from `Uniform(0.5, 1.0)`. This represents communication *strength* — how reliably information flows across that channel. Teams with stronger direct connections (weight closer to 1.0) have higher acquisition probability for each other's incidents.

**Why network structure is load-bearing:** In the NEIGHBOR scenario, the set of teams that can learn from an incident is determined entirely by graph adjacency. A team with high degree (many neighbors) both spreads its own incidents widely and receives knowledge from many sources. A team with low degree is structurally isolated. This is exactly the mechanism Nooteboom (2007) describes: network position shapes organizational learning opportunities. The choice of network topology is therefore not cosmetic — it determines the fundamental learning dynamics being studied.

---

## 2.5 The susceptibility matrix

`DEFAULT_SUSCEPTIBILITY` (lines 92–135) is a dictionary mapping `SubsystemType → IncidentType → float`. It encodes domain knowledge about which systems tend to suffer which failure modes:

- DATABASE has 0.9 susceptibility to DATABASE_TIMEOUT and 0.8 to CAPACITY_ISSUE (makes intuitive sense — databases suffer from query storms and connection pool exhaustion)
- CACHE has 0.9 susceptibility to CAPACITY_ISSUE (caches hit capacity limits)
- FRONTEND has 0.8 susceptibility to DEPLOYMENT_PROBLEM (frontend deployments often have UI regressions)
- AUTH has 0.8 susceptibility to CONFIG_ERROR (auth systems are highly configuration-sensitive)

This matrix serves two distinct roles:
1. **Incident generation** (Phase 1): the row for `team.subsystem` is normalized into a probability distribution to pick which incident type occurs.
2. **Relevance calculation** (Pipeline Stages 2–4): a target team's susceptibility to the incident type determines how much they can benefit from learning about it.

[PAPER] Dogga et al. (2023): the ARTS taxonomy (Availability, Reliability, Traffic, Software) classifies production incidents by failure mode, enabling systematic analysis of which system types are vulnerable to which categories. The susceptibility matrix operationalizes this taxonomy.

---

# Section 3: Network Construction (How Teams Are Connected)

---
### 🔑 Analogy First — Before You Read the Technical Details

**The analogy:** The hospital architect is deciding how to arrange departments in the building. In one design (Watts-Strogatz), departments are laid out in a ring with mostly adjacent neighbours sharing a corridor, but a few random cross-building passages create shortcuts — realistic and efficient. In a second design (Erdős-Rényi), corridors are punched through walls randomly, with no deliberate plan. In a third design (Barabási-Albert), a central hub department like the ICU gets connected to everyone who joins the building later, creating a few overwhelmed relay stations and many peripheral departments that talk only through the hub.

**What maps to what:**
- Departments sharing a physical corridor → an edge between two team nodes in the graph
- How reliably the intercom works between two departments → the edge weight (0.5–1.0)
- The ring-with-shortcuts layout → Watts-Strogatz small-world topology
- Randomly punched corridors → Erdős-Rényi null model topology
- The ICU-as-central-hub layout → Barabási-Albert scale-free topology
- A peripheral department that only hears news through the hub → a low-degree node structurally isolated from most incident reports

**Now read the technical detail below with this picture in your head.**

---

`init_graph(params, rng)` (lines 372–414) creates the communication graph. After construction, edge weights are assigned: `rng.uniform(0.5, 1.0)` for each edge.

The choice of topology is a **treatment variable** in the thesis experiment. Different topologies produce different learning dynamics even holding all other parameters constant.

---

## 3.1 Watts-Strogatz (default)

`nx.watts_strogatz_graph(n, k, p)` — controlled by `ws_k=4` and `ws_p=0.1`.

**Construction algorithm:** Start with n nodes arranged in a ring. Connect each node to its k/2 nearest neighbors on each side. Then, for each edge, with probability p, rewire one endpoint to a random node (avoiding self-loops and duplicates).

**For 6 teams with k=4, p=0.1:**
```
        0
       / \
      5   1
      |   |
      4   2
       \ /
        3

Each node connects to its 2 nearest neighbors on each side.
p=0.1 rewiring occasionally creates a "shortcut" edge
across the ring, e.g. 0—3 might appear.
```

**Key properties:**
- High *clustering coefficient*: neighbors of a node tend to know each other (like real org charts — team members overlap in their communication patterns)
- Low *average path length*: the occasional rewired shortcut edges keep the diameter small
- This combination — high clustering + short paths — is the definition of a *small-world network*

[PAPER] Watts & Strogatz (1998): small-world networks arise naturally in social systems (actors, power grids, neural networks). They enable rapid information diffusion (short paths) while maintaining local cohesion (high clustering). This is why ws is the *default* topology — it is empirically the most realistic model of how engineering teams communicate.

---

## 3.2 Erdős-Rényi

`nx.erdos_renyi_graph(n, p)` — controlled by `er_p=0.3`.

**Construction:** For each of the n*(n-1)/2 possible edges, include it independently with probability p.

**For 6 teams with p=0.3 (expected ~4.5 edges):**
```
  0 --- 2
  |     |
  1     3 --- 5
        |
        4

Edges are random. Any pair can be connected or not.
Structure varies each run (hence controlled by seed).
```

**Key properties:**
- No structural bias: no hubs, no guaranteed clustering
- At p=0.3 with n=6, the graph is usually connected but sparse
- Expected degree: (n-1)*p = 5*0.3 = 1.5 neighbors per node on average

**Role in the thesis:** Erdős-Rényi is the *null model*. It represents an organization with no particular communication structure — teams connected randomly. Comparing NEIGHBOR+ER results to NEIGHBOR+WS or NEIGHBOR+BA isolates the effect of network topology.

[PAPER] Erdős & Rényi (1959): random graphs exhibit sharp threshold phenomena; below a critical p, the graph is fragmented; above it, a giant connected component emerges. At p=0.3, n=6, the graph is almost certainly connected.

---

## 3.3 Barabási-Albert

`nx.barabasi_albert_graph(n, m)` — controlled by `ba_m=2`.

**Construction:** Start with m+1 nodes (fully connected). Add each subsequent node with m new edges. New edges are added preferentially — the probability that a new node connects to existing node v is proportional to v's current degree (rich-get-richer).

**For 6 teams with m=2:**
```
     0
    /|\
   1 2 3       <- node 0 tends to be a hub (added first,
    \|/           accumulated connections early)
     4
     |
     5

One or two nodes accumulate many connections.
Peripheral nodes have degree ~2.
```

**Key properties:**
- Power-law degree distribution: a few hubs, many peripheral nodes
- Short average path length (hubs act as relay stations)
- Low clustering (hubs connect distant nodes, not each other)

[PAPER] Barabási & Albert (1999): preferential attachment explains the scale-free structure observed in the internet, citation networks, and corporate communication networks. In an organization, this corresponds to certain teams (platform teams, DevOps, SRE) becoming central communication hubs due to accumulated cross-team interactions.

**Why network structure matters for knowledge sharing:** The topology determines which teams are in the "learner list" for each incident under NEIGHBOR. A peripheral node in a BA graph might only hear about incidents from the one hub it is connected to. A hub hears about incidents from every direction. This creates structural inequality in learning opportunities.

[PAPER] Nooteboom (2007): network position mediates absorptive capacity; teams with more diverse connections encounter more cognitively distant knowledge, which can be both beneficial (variety of lessons) and detrimental (harder to assimilate) depending on the inverted-U relationship.

---

# Section 4: Incident Generation (Phase 1 of Each Timestep)

---
### 🔑 Analogy First — Before You Read the Technical Details

**The analogy:** Each morning the risk officer rolls through every department and asks: did a medical error occur overnight? A department with highly trained, experienced staff (high prevention knowledge) has a lower baseline chance of an error. But on days when a department just introduced a new drug protocol or switched EHR software (a "deployment"), the error rate spikes for the next three days. When an error does happen, its type — wrong dosage, missed diagnosis, equipment failure — is drawn from a profile of what that department is historically prone to.

**What maps to what:**
- A department's experienced staff reducing daily error risk → prevention knowledge (`Kp`) lowering `p_incident`
- Introducing a new drug protocol or EHR system → a software deployment triggering the `deployment_risk_multiplier`
- The three-day elevated-risk window post-deployment → `recent_deployments` counter decrementing from 3 to 0
- The type of error (wrong dosage vs. equipment failure vs. missed diagnosis) → the `IncidentType` drawn from the susceptibility-weighted distribution
- Some departments being historically prone to certain error types → the `DEFAULT_SUSCEPTIBILITY` matrix

**Now read the technical detail below with this picture in your head.**

---

This is the first half of the main loop body (lines 540–674). For each of the `num_teams` teams, the simulation rolls a Bernoulli trial to decide whether an incident occurs.

---

## 4.1 What is `base_incident_rate`?

`base_incident_rate = 0.05` means that in the absence of any modifiers, each team has a 5% chance of suffering an incident on any given day. Across 6 teams and 365 days, this yields approximately 6 × 0.05 × 365 ≈ 109 incidents per year in the baseline (no learning, no deployments). This is the anchor point; all modifiers scale relative to it.

---

## 4.2 How prevention knowledge reduces incident rate

The actual incident probability is computed as (lines 546–558):

```python
avg_prevention = mean(team.knowledge[it]["prevention"] for it in IncidentType)
prevention_modifier = 1.0 - (avg_prevention * params.prevention_effect)
p_incident = base_incident_rate * prevention_modifier * deployment_modifier
```

With default `prevention_effect = 0.5`:

```
avg_prevention = 0.0  →  modifier = 1.0 - 0*0.5 = 1.00  →  p = 0.05 * 1.00 = 0.050
avg_prevention = 0.2  →  modifier = 1.0 - 0.2*0.5 = 0.90  →  p = 0.05 * 0.90 = 0.045
avg_prevention = 0.5  →  modifier = 1.0 - 0.5*0.5 = 0.75  →  p = 0.05 * 0.75 = 0.038
avg_prevention = 1.0  →  modifier = 1.0 - 1.0*0.5 = 0.50  →  p = 0.05 * 0.50 = 0.025
```

A team with maximum prevention knowledge has its incident rate halved. This is the feedback loop. Note that `avg_prevention` averages across *all* incident types — a team that learned about CONFIG_ERROR incidents also gets partial protection against other types. This reflects the real-world observation that general operational maturity (monitoring, testing, code review) reduces incidents across the board.

---

## 4.3 How deployments elevate incident rate

If `recent_deployments[team.subsystem] > 0`:

```python
deployment_modifier = params.deployment_risk_multiplier  # = 1.5
```

This counter is set to 3 when a deployment occurs (`recent_deployments[team.subsystem] = 3`) and decremented by 1 each timestep. So deployment risk is elevated for 3 days after a deployment. With both effects combined:

```
p_incident = 0.05 * 0.90 * 1.5 = 0.068   (some prevention knowledge + recent deployment)
```

This mirrors the empirical finding in Forsgren et al. (2018) that deployments are the single largest source of production incidents, and that change-failure rate is a key DevOps stability metric.

---

## 4.4 What is the ARTS taxonomy and why does it matter?

The five `IncidentType` values (DATABASE_TIMEOUT, CONFIG_ERROR, DEPENDENCY_FAILURE, CAPACITY_ISSUE, DEPLOYMENT_PROBLEM) are drawn from the ARTS classification scheme.

[PAPER] Dogga et al. (2023): analyzed production incidents at a major cloud provider and found that incidents cluster into four failure-mode categories — Availability, Reliability, Traffic, and Software — each with distinct detection patterns, resolution patterns, and learning opportunities. The ARTS taxonomy provides a principled basis for distinguishing incident types rather than treating all incidents as interchangeable.

Why does type matter in the model? Because the knowledge structure is *typed*. Knowledge about CONFIG_ERROR incidents is stored separately from knowledge about CAPACITY_ISSUE incidents. A team that has only encountered CONFIG_ERROR incidents has no knowledge that helps with DATABASE_TIMEOUT incidents. This creates realistic heterogeneity: teams are experts in the failure modes their subsystem is susceptible to, and novices in others.

---

## 4.5 Probability tree for incident occurrence

Draw this on paper as a decision tree:

```
Each timestep, for each team:

                            ┌─────────────────────┐
                            │   Roll vs p_incident │
                            │   p = base * mods    │
                            └──────────┬──────────┘
                                       │
               ┌───────────────────────┴────────────────────────┐
            p_incident                                    1 - p_incident
               │                                               │
               ▼                                               ▼
     ┌──────────────────┐                           ┌──────────────────┐
     │  INCIDENT OCCURS │                           │   No incident    │
     │                  │                           │   this step      │
     │  Pick type via   │                           └──────────────────┘
     │  susceptibility  │
     │  weights         │
     │                  │
     │  Compute:        │
     │  - severity      │
     │  - detection_t   │
     │  - resolution_t  │
     │  - cost          │
     │  - learnable_K   │
     └──────────────────┘
```

**Incident type selection:** The susceptibility weights for the team's subsystem are normalized to sum to 1, then used as a probability distribution over the five `IncidentType` values. For a DATABASE team: DATABASE_TIMEOUT gets 0.9/(0.9+0.6+0.3+0.8+0.4) = 0.9/3.0 = 30% of incidents.

---

# Section 5: The Learning Pipeline (The Heart of the Model)

---
### 🔑 Analogy First — Before You Read the Technical Details

**The analogy:** After a medication error in the cardiology ward, the hospital wants other departments to learn from it. First, the radiology department has to actually hear about it — someone sends them the incident report (acquisition). Second, they have to read it carefully enough to understand how the error happened (assimilation). Third, they have to connect it to their own workflows: "we handle contrast agents the same way, so this applies to us" (transformation). Fourth and finally, they actually update their protocol checklist (exploitation). A cardiologist reading the report learns the most — close enough to understand it deeply, but different enough that it contains genuinely new information. A dermatologist reading the same report learns almost nothing — too far from their daily work to map it onto anything.

**What maps to what:**
- Hearing that an error occurred → Stage 1 Acquisition (receiving the incident report)
- Understanding the root cause → Stage 2 Assimilation (grasping why it happened)
- Connecting it to your own department's workflow → Stage 3 Transformation (seeing how it applies to you)
- Actually changing your protocol checklist → Stage 4 Exploitation (updating knowledge and procedures)
- A cardiologist learning most from an ER error, not a dermatology error → the inverted-U cognitive distance curve
- The department that suffered the error learning it immediately and completely → the source-team asymmetry (first-person experience bypasses the pipeline)

**Now read the technical detail below with this picture in your head.**

---

The four-stage learning pipeline (lines 676–817) is the theoretical core of the simulation. It is the operationalization of absorptive capacity theory. Read this section carefully and draw each diagram.

---

## 5.1 The pipeline overview

```
         INCIDENT
            │
            ▼
   ┌─────────────────┐
   │  ACQUISITION    │  "Did we hear about this?"
   │  p ~ 0.7–0.9   │
   └────────┬────────┘
            │ fail → incident forgotten
            ▼
   ┌─────────────────┐
   │  ASSIMILATION   │  "Do we understand what happened?"
   │  p ~ 0.2–0.6   │  (most lossy stage)
   └────────┬────────┘
            │ fail → knowledge gap persists
            ▼
   ┌─────────────────┐
   │ TRANSFORMATION  │  "Can we connect it to our own work?"
   │  p ~ 0.2–0.6   │
   └────────┬────────┘
            │ fail → understanding doesn't generalize
            ▼
   ┌─────────────────┐
   │  EXPLOITATION   │  "Did we change anything?"
   │  p ~ 0.3–0.6   │
   └────────┬────────┘
            │
            ▼
   Knowledge update:
   team.knowledge[type][dim] += amount
```

[PAPER] Zahra & George (2002): distinguished *potential* absorptive capacity (acquisition + assimilation) from *realized* absorptive capacity (transformation + exploitation). Potential ACAP is the ability to internalize external knowledge; realized ACAP is the ability to apply it commercially. The pipeline models this two-phase structure.

[PAPER] Cohen & Levinthal (1990): the original absorptive capacity paper argued that prior related knowledge determines the ability to recognize, assimilate, and apply new knowledge. In the model, this is operationalized through the `cosine_similarity` between team knowledge vectors.

---

## 5.2 Stage 1: Acquisition

**Real-life analogy:** A team receives the postmortem document or attends a cross-team incident review meeting. They now know the incident happened. They may not understand it yet.

**What probability controls it:** `acquisition_probability = 0.9` is the base, modified by network distance:

```python
# For a direct neighbor (edge exists):
p_acquire = acquisition_probability * edge_weight
           = 0.9 * weight   (weight ∈ [0.5, 1.0])
           → p ∈ [0.45, 0.90]

# For teams further away (no direct edge):
path_length = nx.shortest_path_length(graph, team, source)
p_acquire = acquisition_probability * (signal_decay ^ path_length)
           = 0.9 * (0.8 ^ path_length)
```

For path length 2: 0.9 × 0.64 = 0.576
For path length 3: 0.9 × 0.512 = 0.461

**What makes probability higher:** A strong communication channel (high edge weight), direct network connection (short path), or the GLOBAL scenario (no distance penalty, full 0.9 applies).

**Why this stage has a separate probability at all:** Information does not diffuse perfectly. A postmortem might be published to a Confluence space that a team never reads. An incident review might be scheduled during a sprint deadline. The 0.9 base reflects that significant incidents usually do get communicated, but it is not guaranteed.

---

## 5.3 Stage 2: Assimilation

**Real-life analogy:** The team reads the postmortem carefully, asks follow-up questions, discusses it in their own standup, and concludes "yes, this could happen to us — it happened because of X and we also do X."

**Formula (lines 741–744):**

```
p_assimilate = (COGNITIVE_WEIGHT * cognitive_factor + DOC_WEIGHT * doc_quality)
               * assimilation_probability
               * (0.5 + 0.5 * relevance)

             = (0.7 * cognitive_factor + 0.3 * doc_quality)
               * 0.7
               * (0.5 + 0.5 * relevance)
```

**What each term does:**
- `cognitive_factor`: computed from `inverted_u_absorptive_capacity(cosine_similarity(...))` — see Section 5.5
- `doc_quality` (0.0–1.0): quality of the postmortem. A team cannot assimilate what was poorly documented. At `doc_quality=0.5` (default), this contributes 0.3 × 0.5 = 0.15 to the weighted average.
- `assimilation_probability = 0.7`: the base ceiling on this stage
- `relevance` (0.3–0.9): whether the incident type can affect the learner's own subsystem (from `calculate_relevance()`)

**Worked example:** Team AUTH (assimilating) reads about a DATABASE_TIMEOUT incident from Team DATABASE.
- AUTH's susceptibility to DATABASE_TIMEOUT = 0.3 → relevance = 0.3 (base relevance, since 0.3 < 0.5)
- Say cognitive_factor = 0.8 (intermediate similarity, near inverted-U peak)
- doc_quality = 0.5 (default)
- p_assimilate = (0.7×0.8 + 0.3×0.5) × 0.7 × (0.5 + 0.5×0.3) = (0.56+0.15) × 0.7 × 0.65 = 0.71 × 0.7 × 0.65 ≈ 0.323

AUTH has about a 32% chance of assimilating a DATABASE_TIMEOUT incident — reflecting that it's not highly relevant to their work.

---

## 5.4 Stage 3: Transformation

**Real-life analogy:** The team connects the incident to their own specific codebase. "They had connection pool exhaustion — we also use connection pooling, so we should add connection pool metrics to our dashboard and add a check to our deployment runbook." The insight is recombined with what they already know about their own system.

**Formula (MINIMAL mode, lines 789–793):**

```
p_transform = (0.8 * cognitive_factor + 0.2 * doc_quality)
              * transformation_probability
              * (0.5 + 0.5 * relevance)
```

Note the weight change from Assimilation: cognitive_factor now gets 0.8 weight (vs 0.7) and doc_quality gets 0.2 (vs 0.3). Transformation is more about internal cognitive work than documentation quality — you need to be able to mentally map the lesson onto your own system, which depends more on cognitive alignment than on how well the postmortem was written.

**Time-based transformation (optional, controlled by `use_time_based_transformation`):**

When this flag is True, transformation no longer succeeds in a single timestep. Instead, each timestep adds progress:

```
progress_rate = effort_rate × (0.5 + 0.5×cognitive_factor) × (0.5 + 0.5×relevance) × (0.5 + 0.5×doc_quality)
```

Progress accumulates until it reaches 1.0, at which point transformation is complete. This models the real-world observation that deep integration of new knowledge into existing practices takes weeks of sustained effort — sprint planning, architecture discussions, gradual refactoring.

**Why have Transformation as a separate stage from Assimilation?** Zahra & George (2002) argue that understanding an external lesson (assimilation) and being able to apply it in your own context (transformation) are cognitively distinct processes. A team might fully understand a postmortem about a Kubernetes networking failure but have no mental model of how their own stack relates to it, leaving them unable to act.

---

## 5.5 The source-team asymmetry: why p = 1.0 for acquisition by the source

When an incident occurs on Team X, Team X skips the entire pipeline (lines 660–669):

```python
if (params.learning_scenario != LearningScenario.NONE
        and not params.disable_source_asymmetry):
    team.acquired_incidents.add(incident.incident_id)
    team.assimilated_incidents.add(incident.incident_id)
    team.transformed_incidents.add(incident.incident_id)
    team.exploited_incidents.add(incident.incident_id)
    for dim in KNOWLEDGE_DIMENSIONS:
        team.learn(incident_type, dim, learnable_knowledge[dim])
```

The team that *experienced* the incident automatically passes all four stages with probability 1.0 and gains the full `learnable_knowledge` amount (no relevance or doc quality discount).

**Why is this theoretically justified?**

[PAPER] Darr et al. (1995): organizations learn faster from direct experience than from observation of others' experience. First-person experience creates episodic memory — the team was present, they felt the pain, they ran the recovery. This produces far richer encoding of the lesson than reading a postmortem.

[PAPER] Cohen & Levinthal (1990): the absorptive capacity pipeline exists precisely *because* indirect learning is difficult. The source team has no absorption barrier — the knowledge is self-generated.

[PAPER] Lunney & Lueder (2016): SRE practice confirms that the team on-call during an incident produces the most accurate and actionable postmortem, because they have context the document cannot fully capture.

The `disable_source_asymmetry` ablation flag removes this special treatment, forcing the source team through the same pipeline as everyone else. This is useful for measuring how much of the model's learning dynamics are driven by the asymmetry alone — see Section 10.

---

## 5.6 Cognitive distance and the inverted-U curve

**The core function** (lines 330–347):

```python
def inverted_u_absorptive_capacity(similarity, peak_location=0.5, steepness=4.0):
    normalization = steepness * peak_location * (1 - peak_location)
    return steepness * similarity * (1 - similarity) / normalization
```

This is a scaled version of the function f(s) = 4s(1-s), which is a parabola opening downward with peak at s=0.5. Plugging in values:

```
similarity = 0.0  →  f = 4×0.0×1.0 / 1.0 = 0.00
similarity = 0.2  →  f = 4×0.2×0.8 / 1.0 = 0.64
similarity = 0.5  →  f = 4×0.5×0.5 / 1.0 = 1.00  ← peak
similarity = 0.8  →  f = 4×0.8×0.2 / 1.0 = 0.64
similarity = 1.0  →  f = 4×1.0×0.0 / 1.0 = 0.00
```

Draw this curve on paper:

```
cognitive_factor
    1.0 |         *
        |       *   *
    0.8 |     *       *
        |   *           *
    0.6 | *               *
        |*                 *
    0.4 |                   *
        |                     *
    0.2 |                      *
        |*                      *
    0.0 +─────────────────────────→ similarity
        0.0  0.2  0.5  0.8  1.0
```

**What this means in plain English:**

- **Too similar (similarity → 1.0):** Both teams already know essentially the same things. There is no new information to transfer. A DATABASE team learning from another DATABASE team with identical incident history gains nothing.
- **Too different (similarity → 0.0):** Teams have no common conceptual framework. The learner cannot map the lesson onto their own context. A new graduate reading a postmortem about Kubernetes control-plane leader election failures has not yet built the mental scaffolding to extract lessons.
- **Intermediate similarity (similarity ≈ 0.5):** Teams share enough background to communicate but differ enough that the incident represents genuinely new information. Maximum learning occurs here.

[PAPER] Nooteboom et al. (2007): using empirical data from R&D alliances, they showed that inter-firm learning is maximized at intermediate levels of cognitive proximity. Very similar partners have little to teach each other; very different partners cannot communicate effectively. The inverted-U operationalizes this relationship.

**The zero-vector edge case:** When a team has no knowledge at all (vector of zeros), cosine similarity is undefined. The code returns 0.5 in this case, placing the team at the peak of the inverted-U. This is theoretically correct:

[PAPER] Cohen & Levinthal (1990): organizations starting from a blank slate have maximal absorptive capacity for any knowledge because they have no prior commitments or cognitive lock-in that would interfere with assimilation.

---

# Section 6: Knowledge Decay (Why Knowledge Fades)

---
### 🔑 Analogy First — Before You Read the Technical Details

**The analogy:** A hospital department updated its medication-error checklist two years ago after a serious adverse event. But since then, three experienced nurses have left, the new ones were never formally trained on the checklist, and the laminated card on the wall has faded and been half-ignored. When the next error occurs, the department is almost as vulnerable as before — the institutional knowledge walked out the door with the staff who originally learned the lesson. The skill does not vanish overnight; it erodes gradually, day by day, unless the department actively reinforces it.

**What maps to what:**
- Experienced nurses leaving and taking tacit knowledge with them → staff turnover driving knowledge decay
- The daily `K *= (1 - δ)` multiplication → the slow, compounding erosion of each knowledge score
- δ = 0.001 per day → a half-life of roughly two years, consistent with real organisational forgetting
- A department in a high-sharing scenario staying sharp because it receives reinforcing lessons constantly → learning gains from Phase 2 outpacing decay at dynamic equilibrium
- The NONE scenario team slowly forgetting even baseline competence → unchecked decay with no learning input

**Now read the technical detail below with this picture in your head.**

---

## 6.1 The decay formula

Applied at the start of each timestep (lines 530–535):

```
K_t = K_{t-1} * (1 - δ) + ΔK_t
```

where δ = `knowledge_decay = 0.001` per day. The `ΔK_t` term is the learning gains from Phase 2, added *after* decay is applied.

**What δ = 0.001 per day means in real terms:**

After t days without reinforcement: K_t = K_0 × (1-0.001)^t = K_0 × 0.999^t

Half-life: solve 0.999^t = 0.5
→ t = ln(0.5) / ln(0.999) = -0.693 / -0.001 ≈ 693 days ≈ 1.9 years

So a knowledge level of 0.5 that receives no reinforcement decays to 0.25 after roughly 2 years. This is consistent with organizational forgetting timescales observed in empirical literature.

[PAPER] Darr et al. (1995): studying pizza franchises, found that learning curve benefits depreciated with time since the learning event, with the largest losses occurring when operational practices were not regularly reinforced. They estimated knowledge half-lives on the order of months to a few years depending on practice frequency.

---

## 6.2 Why knowledge decays at all

Knowledge decay is not just a modeling convenience — it represents several real mechanisms:

1. **Personnel turnover:** Engineers leave, taking tacit knowledge with them.
2. **System change:** The system itself evolves, making old incident knowledge obsolete.
3. **Attention decay:** Runbooks that are not consulted are forgotten. Monitoring rules that were set up after an incident are later removed as "noisy."
4. **Organizational restructuring:** Team mergers, reorgs, and role changes disrupt established practices.

Without decay, the model would show knowledge monotonically increasing and eventually reaching a ceiling at 1.0, at which point incidents become very rare. This is unrealistic: organizations genuinely do "re-learn" the same lessons repeatedly, which is exactly what motivates learning scenario research.

---

## 6.3 Knowledge trajectory over time (ASCII graph)

```
Knowledge
  level
  1.0 |                     _ _ _ _ _
      |                  --/          (GLOBAL scenario: rapid learning)
  0.8 |               --/
      |           ---/
  0.6 |        --/            _ _ _ _
      |      -/          ----/        (NEIGHBOR scenario)
  0.4 |    -/        ---/
      |  -/     ----/
  0.2 | /  ----/               _ _ _
      |/---/               ---/       (LOCAL scenario)
  0.0 |_ _ _ _ _ _ _ _ _ _/_ _ _ _ _→ time (days)
      0        100        200        365

Note: decay creates a slight downward pressure that is overcome
by learning events. On days with no incidents, knowledge slowly
decreases. Without decay (ablation), curves monotonically increase
to ceiling; with decay, they reach a dynamic equilibrium.
```

**The dynamic equilibrium:** The simulation reaches a steady state where knowledge gain from new incidents approximately equals decay. Teams in high-sharing scenarios reach higher equilibria because they receive learning impulses from more sources.

---

# Section 7: The Four Sharing Scenarios (What Makes Them Different)

---
### 🔑 Analogy First — Before You Read the Technical Details

**The analogy:** After a serious medication error, hospital leadership must decide who gets to read the incident report. In the NONE policy, the report is shredded — no one learns, not even the department that made the error. In the LOCAL policy, the department files it in their own binder and learns internally, but it never leaves the room. In the NEIGHBOR policy, the department shares it at the weekly hallway debrief with adjacent departments — the ER tells the ICU and radiology, but the dermatology ward never hears. In the GLOBAL policy, the hospital broadcasts the report to every single department at the all-hands safety meeting.

**What maps to what:**
- Shredding the incident report → NONE scenario (empty learner list, no learning at all)
- Filing it only in the department's own binder → LOCAL scenario (only source team learns)
- Sharing at the hallway debrief with adjacent departments → NEIGHBOR scenario (source plus graph-adjacent teams)
- Broadcasting at the all-hands safety meeting → GLOBAL scenario (every team in the organisation)
- The adjacent department's intercom reliability → edge weight modifying acquisition probability in NEIGHBOR

**Now read the technical detail below with this picture in your head.**

---

`get_learners_for_scenario()` (lines 417–440) is a simple dispatcher that returns a list of team IDs eligible to learn from a given incident. This function is the central mechanism that distinguishes the four scenarios.

---

## 7.1 NONE — No learning (baseline control)

```python
if scenario == LearningScenario.NONE:
    return []
```

**Which teams learn:** Nobody. The source team does not even go through the pipeline (because the asymmetry check at line 660 is also gated on `scenario != NONE`).

**Network diagram:**

```
Team 0  ○ ─── ○ Team 1
        │         │
Team 5  ○         ○ Team 2
        │         │
Team 4  ○ ─── ○ Team 3

Incident at Team 2 →  (no arrows, nobody learns)
```

**Real-world analogy:** An organization that experiences incidents, resolves them, and moves on with no postmortem process, no incident database, no retrospectives. Each team is siloed.

**Why study this:** It is the control condition. Every other scenario is compared against NONE to measure the *effect* of learning. If NEIGHBOR produces the same total incidents as NONE, the learning mechanism has no effect.

---

## 7.2 LOCAL — Source team only

```python
elif scenario == LearningScenario.LOCAL:
    return [source_team_id]
```

**Which teams learn:** Only the team that experienced the incident. They go through the pipeline (or bypass it via asymmetry), but no other team is eligible.

**Network diagram:**

```
Team 0  ○ ─── ○ Team 1
        │         │
Team 5  ○         ○ Team 2  ←── Incident
        │         │
Team 4  ○ ─── ○ Team 3

→ Team 2 learns (via asymmetry bypass, p=1.0)
→ All other teams: not in learner list, no pipeline attempted
```

**Real-world analogy:** Teams write postmortems for their own reference, but the documents live in a team-specific wiki that nobody else reads. The learning exists but is not shared.

**Why study this:** LOCAL isolates within-team learning from cross-team learning. Comparing LOCAL vs NEIGHBOR vs GLOBAL tells you how much *additional* value is created by sharing.

[PAPER] Drupsteen & Guldenmund (2014): organizations typically perform better at recording lessons than at distributing them. The LOCAL scenario models this well-documented failure mode where documentation exists but diffusion does not occur.

---

## 7.3 NEIGHBOR — Network-adjacent teams

```python
elif scenario == LearningScenario.NEIGHBOR:
    neighbors = list(graph.neighbors(source_team_id))
    return [source_team_id] + neighbors
```

**Which teams learn:** Source team plus all teams directly connected to it in the communication graph.

**Network diagram (for a 6-node WS graph where Team 2 has neighbors 1 and 3):**

```
Team 0  ○ ─── ○ Team 1 ←── learns (neighbor of 2)
        │         │
Team 5  ○         ○ Team 2 ←── incident (learns via asymmetry)
        │         │
Team 4  ○ ─── ○ Team 3 ←── learns (neighbor of 2)

Teams 0, 4, 5: not in learner list
```

**Acquisition probability for neighbors** depends on edge weight (0.5–1.0), so even eligible teams may not acquire at this step.

**Real-world analogy:** The team that had the incident presents at the next department standup, or sends a Slack message to their immediate channel. Adjacent teams hear it. Teams two hops away do not.

**Why study this:** NEIGHBOR is the most realistic scenario for most mid-sized engineering organizations. Information sharing is limited by communication bandwidth and organizational proximity. This scenario is also where network topology matters most — a hub node in a BA graph shares its incidents with many more teams than a peripheral node.

[PAPER] Drupsteen & Guldenmund (2014): organizational incident learning requires both documentation and active dissemination. The NEIGHBOR scenario captures the common pattern where dissemination occurs within a team's immediate communication network but does not propagate further.

---

## 7.4 GLOBAL — All teams

```python
elif scenario == LearningScenario.GLOBAL:
    return all_team_ids
```

**Which teams learn:** Every team in the organization is added to the learner list. No network distance penalty applies — acquisition probability is the full `acquisition_probability = 0.9` for all teams.

**Network diagram:**

```
Team 0  ○ ─── ○ Team 1 ←── learns
        │         │
Team 5  ○         ○ Team 2 ←── incident
        │         │
Team 4  ○ ─── ○ Team 3 ←── learns

All teams, including 0, 4, 5: in learner list
(arrows from Team 2 to all other nodes)
```

**Real-world analogy:** A company-wide incident review broadcast, a mandatory "Learning from Incidents" weekly meeting, or an automated incident notification bot that posts to every team's channel. SRE organizations at Google, Netflix, and Etsy have described practices of this type.

**Why study this:** GLOBAL is the theoretical upper bound on knowledge sharing. It represents maximum possible diffusion. Comparing GLOBAL to NEIGHBOR quantifies the marginal value of expanding sharing beyond immediate neighbors — which has a cost (engineering time at learning_cost per event) that may or may not be justified.

---

# Section 8: Knowledge Update and Effects

---
### 🔑 Analogy First — Before You Read the Technical Details

**The analogy:** When a department finally updates its protocol after studying an incident report, the improvement shows up in three measurable ways: errors become less likely to happen in the first place (better pre-procedure checklists), errors that do happen get caught sooner (better monitoring and warning signs), and when errors occur they cause less harm and are resolved faster (better emergency response runbooks). Each of these three competencies improves independently — a department can be excellent at catching errors early but still weak at preventing them from starting.

**What maps to what:**
- Better pre-procedure checklists reducing the chance an error starts → prevention knowledge `Kp` lowering `p_incident`
- Better vital-sign monitoring catching a deteriorating patient sooner → detection knowledge `Kd` shrinking mean time to detect (MTTD)
- Practiced emergency runbooks limiting harm once an error occurs → mitigation knowledge `Km` reducing severity and resolution time
- A department being expert in medication errors but a novice on equipment failures → the typed knowledge structure (5 incident types × 3 dimensions, stored separately)
- How much usable insight an incident actually contains → `learnable_knowledge` drawn per incident, scaled by relevance and documentation quality

**Now read the technical detail below with this picture in your head.**

---

When Stage 4 (Exploitation) succeeds, `team.learn()` is called (lines 808–815):

```python
for dim in KNOWLEDGE_DIMENSIONS:
    learning_amount = (
        incident.learnable_knowledge[dim]
        * (0.5 + 0.5 * relevance)
        * (0.5 + 0.5 * params.documentation_quality)
    )
    team.learn(incident.incident_type, dim, learning_amount)
```

This multiplies three factors:
1. `learnable_knowledge[dim]` — how much the incident contains (drawn Uniform[0.1, 0.25])
2. `(0.5 + 0.5 * relevance)` — how applicable it is (ranges from 0.65 at relevance=0.3 to 1.0 at relevance=1.0)
3. `(0.5 + 0.5 * doc_quality)` — how well it was documented (ranges from 0.5 at doc=0.0 to 1.0 at doc=1.0)

At default doc_quality=0.5 and full relevance=1.0: learning_amount = 0.175 × 1.0 × 0.75 ≈ 0.13 per event.

---

## 8.1 How Kp (prevention knowledge) reduces incidents

Formula (applied in Phase 1 each timestep, lines 546–551):

```
p_incident = base_incident_rate
             × (1 - avg_prevention × prevention_effect)
             × deployment_modifier
```

- `avg_prevention` = mean of `team.knowledge[it]["prevention"]` across all IncidentType
- `prevention_effect = 0.5`
- Maximum reduction: 50% when avg_prevention = 1.0

**Mechanism:** Prevention knowledge represents things like: code review checklists that catch error-prone patterns, deployment runbooks that prevent misconfigurations, load testing that prevents capacity incidents. It reduces the probability that the team's actions cause an incident.

[PAPER] Reed et al. (2019): organizational resilience interventions (which include incident learning) primarily operate through prevention — improving the reliability of routine operations rather than the response to failures.

---

## 8.2 How Kd (detection knowledge) reduces MTTD

Formula (applied when generating incident characteristics, lines 582–592):

```
detection_modifier = 1.0 - (avg_detection × detection_effect)
detection_time = base_detection_time × detection_modifier × noise
```

- `avg_detection` = mean of `team.knowledge[it]["detection"]` across all IncidentType
- `detection_effect = 0.3`
- Maximum reduction: 30% in detection time when avg_detection = 1.0
- `base_detection_time = incident_duration_base × 0.4 = 0.8 hours` by default

Detection knowledge represents things like: alert thresholds set at correct sensitivity, symptom-cause mappings in runbooks, dashboard panels that make anomalies visible. It reduces the time between when an incident starts and when the team knows about it.

[PAPER] Dogga et al. (2023): detection speed is empirically the most variable component of incident response time across organizations, and improvements in monitoring and alerting practices produce measurable MTTD reductions.

---

## 8.3 How Km (mitigation knowledge) reduces severity and duration

Formula (applied to severity and resolution time, lines 570–596):

```
severity_modifier = 1.0 - (avg_mitigation × mitigation_effect)
severity = clip(Normal(severity_base, severity_std) × severity_modifier, 1.0, 5.0)

resolution_time = base_resolution_time × severity_modifier × noise
```

- `mitigation_effect = 0.3`
- Maximum reduction: 30% in severity and resolution time when avg_mitigation = 1.0

Mitigation knowledge represents things like: rollback procedures, circuit breakers, graceful degradation patterns, practiced incident response runbooks. It does not prevent incidents from occurring but reduces their impact when they do.

Note that `duration = detection_time + resolution_time`, so both Kd and Km together determine total incident duration, which drives MTTR and availability.

---

## 8.4 The three knowledge dimensions and why three

The choice of exactly three dimensions — prevention, detection, mitigation — is grounded in two theoretical frameworks:

[PAPER] Reed et al. (2019): organizational resilience requires three distinct capabilities: anticipation (preventing adverse events), detection (recognizing when things go wrong), and response (recovering effectively). These map directly to prevention, detection, and mitigation.

[PAPER] Dogga et al. (2023): ARTS incident analysis identifies distinct phases of incident lifecycles: the conditions that allow incidents to occur (prevention-relevant), the time to acknowledgment (detection-relevant), and the time to resolution (mitigation-relevant). Each phase is improved by different types of knowledge.

**Why not collapse to one dimension?** Because the three dimensions are independently learnable and have distinct effects. A team might have excellent monitoring (high Kd) but poor defensive coding practices (low Kp). Collapsing to one dimension would prevent the model from capturing this realistic heterogeneity in operational maturity.

**Why not more dimensions?** Five dimensions might include "capacity planning" and "dependency management," but this adds parameters without clear additional theoretical motivation. Three is sufficient to demonstrate differential knowledge effects while keeping the model interpretable.

---

# Section 9: Metrics Collection

---
### 🔑 Analogy First — Before You Read the Technical Details

**The analogy:** At the end of every single day, the hospital's quality-assurance office fills in its dashboard: how many adverse events occurred across each department, how long it took to notice each one, how long it took to resolve it, how many staff-hours were consumed, and what the current skill levels look like across the network. At the end of the year, that daily log is what the hospital board uses to answer the big question: did the incident-sharing policy actually reduce harm — and what did it cost in staff time to run those safety reviews?

**What maps to what:**
- The QA dashboard updated every day → `metrics` dictionary populated each timestep in Phase 3
- Number of adverse events per department per day → `incident_frequency` time series
- Average time from error to detection → `mttd` (mean time to detect)
- Average time from detection to full resolution → `mttr` (mean time to resolve)
- Staff-hours consumed by safety reviews and protocol updates → `cumulative_learning_cost`
- The year-end board report comparing policies → `total_incidents` and `overall_availability` as primary experimental outcomes

**Now read the technical detail below with this picture in your head.**

---

## 9.1 What is collected each timestep (Phase 3, lines 876–962)

The `metrics` dictionary is populated inside the main loop and finalized after it ends. Here is every field:

**Incident counts and characteristics:**
- `incident_frequency[subsystem_name]` — list of per-timestep incident counts per subsystem. Used to plot how incident rate evolves over time.
- `incident_duration` — mean duration across incidents occurring this timestep (0.0 if none)
- `incident_severity` — mean severity across incidents this timestep
- `engineering_cost` — total engineering cost of incidents this timestep
- `total_incidents` — scalar, total across all timesteps
- `total_incidents_by_type` — breakdown by IncidentType
- `total_incidents_by_subsystem` — breakdown by SubsystemType

**Learning pipeline stage rates:**
- `acquisition_rate`, `assimilation_rate`, `transformation_rate`, `exploitation_rate` — for each timestep, the fraction of (non-source team, incident) pairs that passed that stage. Used to diagnose which stage is the bottleneck.

**Knowledge over time:**
- `avg_prevention_knowledge`, `avg_detection_knowledge`, `avg_mitigation_knowledge` — each is a list of length `steps`. At each timestep, compute the mean knowledge value across all teams × all incident types. This time series shows the learning curve.

**Reliability metrics:**
- `mtbf` — per-timestep dictionary of running mean MTBF per subsystem
- `mttr` — per-timestep running mean MTTR
- `mttd` — per-timestep running mean MTTD

---

## 9.2 Why each metric matters

**`total_incidents`** is the primary experimental outcome. The thesis question is whether and how much knowledge sharing reduces incident frequency over time. Scenarios with more sharing should produce fewer total incidents.

**`overall_availability`** (computed post-loop, lines 968–987):

```
Availability = MTBF / (MTBF + MTTR)
```

This is the standard reliability formula. `overall_availability` is the mean across all subsystems. At MTBF=20 days and MTTR=2 hours ≈ 0.083 days: A = 20/(20.083) ≈ 99.6%.

[PAPER] Forsgren et al. (2018): availability is a primary DevOps outcome metric. The DORA research program found that high-performing engineering organizations achieve 99.95%+ availability. Availability is more informative than raw incident count because it accounts for both incident frequency and incident duration.

**`avg_mttd`** (final_mttd in summary) measures how quickly teams detect incidents on average. This should decrease over time as detection knowledge accumulates — and should decrease faster in higher-sharing scenarios.

**`cumulative_learning_cost`** tracks the total developer-hours spent on learning activities. Each successful exploitation event costs `learning_cost = 2.0` hours (attending incident reviews, writing action items, implementing changes). This is the *investment* side of the learning equation. Together with `total_engineering_cost` (cost of incidents), it allows computation of the return on investment from different sharing policies.

**Knowledge time series** (avg_prevention_knowledge etc.) are tracked over all 365 timesteps rather than just the final value because the *trajectory* matters: How quickly does knowledge accumulate? Does it plateau? Does it decay faster than it accumulates in low-incident periods? These time series are necessary for the thesis to distinguish between scenarios that might have similar final knowledge levels but different trajectories.

---

# Section 10: The Ablation Flags (Why They Exist)

---
### 🔑 Analogy First — Before You Read the Technical Details

**The analogy:** The hospital's research team wants to verify that their safety model is actually explaining the right things. So they run two controlled experiments: in the first, they imagine a hospital where staff never leave — institutional knowledge never fades — and check whether the improvement curves look unrealistically perfect. In the second, they remove the advantage that the department involved in an error normally has (being present, feeling the pain, owning the recovery) and instead force that department through the same slow review process as everyone else. If removing either assumption collapses the model's predictions or makes them implausible, that assumption is confirmed to be genuinely load-bearing.

**What maps to what:**
- Imagining a hospital with zero staff turnover → `disable_knowledge_decay = True` (knowledge only ever rises)
- Removing the first-person experience advantage of the department that made the error → `disable_source_asymmetry = True` (source team goes through the pipeline like everyone else)
- Checking whether the model still produces sensible rankings with each assumption removed → the Sargent (2020) validation methodology
- Finding that LOCAL scenario collapses to near-NONE when the first-person advantage is gone → confirming that source asymmetry is load-bearing
- Finding that all scenarios converge to the same high ceiling without decay → confirming that decay is what separates long-run scenario performance

**Now read the technical detail below with this picture in your head.**

---

`SimulationParams` has two flags specifically for model validation and sensitivity analysis: `disable_knowledge_decay` and `disable_source_asymmetry`.

---

## 10.1 `disable_knowledge_decay`

**What it does when True:** The decay block (lines 530–535) is skipped:

```python
if not params.disable_knowledge_decay:
    for team in teams:
        for it in IncidentType:
            team.knowledge[it]["prevention"] *= (1 - params.knowledge_decay)
            ...
```

When `disable_knowledge_decay = True`, this block is never executed. Knowledge only ever increases; it never decays.

**What scientific question it answers:** Is the decay mechanism necessary for the model's behavior? Specifically:
- Does decay explain why NONE scenario produces more incidents over time? (Without decay, NONE would still be flat — no learning occurs, so no decay occurs either; the flat baseline is not affected.)
- Does the *difference* between scenarios change when decay is absent? If GLOBAL accumulates knowledge faster than it decays (equilibrium well above 0), removing decay might not change the ranking. If decay substantially suppresses knowledge in lower-sharing scenarios, removing it would compress the performance gap between scenarios.
- Does removing decay produce implausibly optimistic results? (Yes, it should — organizations that never forget maintain knowledge levels that are unrealistically high.)

**What result to expect when True:** Knowledge in all non-NONE scenarios rises monotonically until it plateaus near ceiling (1.0). Total incidents keep declining throughout the 365-day run, with no equilibrium. The gap between GLOBAL and LOCAL disappears at long run-times because both approach the same ceiling.

---

## 10.2 `disable_source_asymmetry`

**What it does when True:** The source team bypass block (lines 660–669) is skipped. Instead, the source team goes through the pipeline like any other team in the learner list:

```python
if (params.learning_scenario != LearningScenario.NONE
        and not params.disable_source_asymmetry):
    # bypass: direct full learning
    ...
```

When `disable_source_asymmetry = True`, the source team is in `potential_learners` (because LOCAL/NEIGHBOR/GLOBAL return `source_team_id` in the list) and goes through the four-stage pipeline with the same probabilities as everyone else.

**What scientific question it answers:** How much of the observed learning dynamics are driven by the first-person experience advantage? Specifically:
- Does the asymmetry create a significant within-team learning advantage over shared learning?
- If the source team goes through the pipeline, do LOCAL and NEIGHBOR converge? (In LOCAL, only the source team can learn, and they now go through the pipeline. Under asymmetry, they bypass it. Disabling asymmetry makes LOCAL much less effective.)
- Does the model produce different ranking of scenarios when this assumption is removed?

**What result to expect when True:** LOCAL scenario performance degrades substantially — the source team now has only ~0.9 × 0.7 × 0.7 × 0.6 ≈ 26% chance of passing all four stages (versus 100% with asymmetry). NEIGHBOR and GLOBAL scenarios are less affected because they include many teams, so the source team's contribution to knowledge growth is a small fraction of total learning. Total incidents in the LOCAL scenario should be much closer to NONE when asymmetry is disabled.

---

## 10.3 Why Sargent (2020) requires these checks

[PAPER] Sargent (2020) — "Verification and Validation of Simulation Models" — establishes that agent-based simulation models require systematic validation at three levels:

1. **Conceptual model validation:** Does the model's theoretical structure correctly represent the real-world system? (The source asymmetry represents a real phenomenon — direct experience confers superior learning. The ablation test can confirm this by showing that removing it produces results inconsistent with empirical literature.)

2. **Computerized model verification:** Does the code correctly implement the conceptual model? (The ablation tests serve as unit tests — with decay disabled, knowledge should never decrease; with asymmetry disabled, source teams should have similar pipeline pass rates to neighbors.)

3. **Operational validation:** Does the model's output behavior match observed real-world behavior? (If disabling decay produces implausibly high knowledge levels, this validates that decay is set at a reasonable magnitude.)

**The ablation methodology:** Run the simulation four times with the same seed: (1) full model, (2) no decay, (3) no asymmetry, (4) neither. Compare total_incidents, overall_availability, and knowledge trajectories across all four. If the results are qualitatively similar regardless of which flags are set, the model is not sensitive to these assumptions and they may not be necessary. If removing decay or asymmetry dramatically changes results, these mechanisms are load-bearing and require careful parameter calibration.

Concretely: you should expect that `disable_knowledge_decay=True` produces lower `total_incidents` (knowledge keeps accumulating, so incidents keep declining), and `disable_source_asymmetry=True` produces more `total_incidents` in LOCAL/NEIGHBOR (teams learn more slowly from their own incidents). If these effects do *not* appear, there is a bug.

---

# Appendix: Complete Function Reference

| Function | Lines | What it does |
|---|---|---|
| `cosine_similarity(a, b)` | 311–327 | Similarity between two knowledge vectors; returns 0.5 when either is zero |
| `inverted_u_absorptive_capacity(similarity)` | 330–347 | Maps similarity to learning multiplier via 4s(1-s)/normalization |
| `calculate_relevance(source_sub, target_sub, type)` | 350–369 | Returns target's susceptibility if >0.5, else 0.3 |
| `init_graph(params, rng)` | 372–414 | Builds NetworkX graph from topology parameter; assigns random edge weights |
| `get_learners_for_scenario(scenario, source, all_ids, graph)` | 417–440 | Returns list of team IDs eligible to learn (the scenario dispatcher) |
| `run_simulation(params)` | 447–1096 | The main simulation loop; returns nested results dict |
| `compare_learning_scenarios(base_params, scenarios, seeds)` | 1103–1151 | Convenience wrapper: runs all four scenarios and returns results dict |
| `Team.__post_init__` | 189–195 | Initializes knowledge dict to all zeros at construction |
| `Team.get_susceptibility` | 197–199 | Lookup into DEFAULT_SUSCEPTIBILITY |
| `Team.get_knowledge_vector` | 201–207 | Flattens 5×3 knowledge dict to 15-element numpy array |
| `Team.learn` | 209–212 | Adds amount to knowledge[type][dim], capping at 1.0 |

---

*Document generated from `/Users/csuser/Downloads/CS MS/02-Framework-Code/model.py` (1184 lines). All line numbers are accurate to the version read.*
