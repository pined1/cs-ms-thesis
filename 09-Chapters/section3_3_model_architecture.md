# Section 3.3: Model Architecture

This section describes every component of the simulation in sufficient detail that a reader could reproduce the model from scratch. Parameters named below correspond to identically named variables in the simulation source code. Table 3.1 at the end of this section consolidates all default values.

## 3.3.1 Agents and Environment

The simulation populates a virtual organization with 20 software engineering teams, each implemented as an autonomous agent. Each team owns a disjoint subset of six software subsystem types — `DATABASE`, `PAYMENT`, `AUTH`, `FRONTEND`, `API`, and `CACHE` — distributed across the agent population at initialization. Ownership is relevant because incidents arise from the subsystems a team is responsible for, and a team's knowledge state directly modulates the rate at which those incidents occur.

Teams are embedded in a social network that governs which agents can exchange knowledge. The network topology is an experimental parameter: the default configuration is a Watts-Strogatz (WS) small-world graph, parameterized by `ws_k = 4` (the number of nearest neighbors before rewiring) and `ws_p = 0.1` (the per-edge rewiring probability). Additional topologies tested across experiments include Barabási-Albert scale-free networks (`ba_m = 2`, edges added per new node) and Erdős-Rényi random graphs. Topology assignment is independent of subsystem ownership. The network structure does not change during a simulation run; it is fixed at initialization and held constant for all 365 simulated days.

## 3.3.2 Incident Generation

Incidents are generated stochastically via a Poisson process. Each subsystem owned by a team independently draws an incident event each day with base probability `base_incident_rate = 0.05`. This base rate is modified by the team's accumulated prevention knowledge: the effective incident rate for a given subsystem is computed as

> effective_rate = base_rate × (1 − prevention_k)

where `prevention_k` is the prevention dimension of the relevant cell in the team's knowledge vector (described in Section 3.3.3). A team with no relevant knowledge operates at the full base rate; a team with prevention knowledge approaching 1.0 asymptotically suppresses the corresponding incident type. When an incident fires, it enters the four-stage learning pipeline (Section 3.3.4), and its type — one of the five incident categories described below — is recorded along with the originating team and the simulation day.

## 3.3.3 The Knowledge Vector

Every team carries a knowledge representation structured as a 5 × 3 matrix — five incident types by three knowledge dimensions — yielding 15 scalar cells per team, each bounded to the interval [0, 1]. The five incident types are `DATABASE_TIMEOUT`, `CONFIG_ERROR`, `DEPENDENCY_FAILURE`, `CAPACITY_ISSUE`, and `DEPLOYMENT_PROBLEM`. The three knowledge dimensions are *prevention*, *detection*, and *mitigation*. Table 3.X presents the matrix layout; dashes indicate cells that are populated at runtime with team-specific values.

**Table 3.X: Team Knowledge Matrix Structure**

| Incident Type | Prevention | Detection | Mitigation |
|---|---|---|---|
| Database Timeout | — | — | — |
| Config Error | — | — | — |
| Dependency Failure | — | — | — |
| Capacity Issue | — | — | — |
| Deployment Problem | — | — | — |

Each dimension corresponds to a distinct operational outcome. The *prevention* dimension reduces the effective incident rate for the corresponding type, as described in Section 3.3.2. The *detection* dimension reduces the time-to-identify an incident once it occurs — teams with higher detection knowledge recognize and classify a failure more rapidly. The *mitigation* dimension reduces incident severity and recovery time once an incident has been identified. Only prevention directly suppresses incident occurrence; detection and mitigation affect incident handling costs after the event fires.

The primary outcome metric of this study is Prevention K: the mean value of all prevention-dimension cells, averaged across all 15 cells per team and across all 20 teams, measured at simulation day 365. This single scalar summarizes the extent to which the simulated organization has collectively built the capability to suppress recurring failure — the operational definition of organizational reliability improvement in this model.

## 3.3.4 The Four-Stage Learning Pipeline

When an incident fires, it initiates a knowledge-sharing and absorption sequence operationalized as four sequential probabilistic stages, grounded in the Zahra & George (2002) absorptive capacity framework. Each stage is a gated transition; failure at any stage halts the pipeline for that event–team pair for that day. The pipeline is instantiated once per receiving team per incident event; the source team is excluded from stages 2 through 4 by design (see Section 3.3.6).

**Stage 1 — Acquisition.** The receiving team must first obtain the incident knowledge signal. The acquisition probability decays with network distance from the source:

> p_acquire = acquisition_prob × signal_decay ^ path_length

The default `acquisition_prob = 0.9` represents the base probability that a directly adjacent team receives the signal. The `signal_decay = 0.8` parameter is applied once per hop: each additional step in the network path between source and receiver multiplies the probability by 0.8. Under the `GLOBAL` sharing scenario, all teams receive the signal as if they were one hop away (`path_length = 1` for all non-source teams), approximating a centralized broadcast. Under the `NEIGHBOR` sharing scenario, `path_length` is set to the actual shortest-path distance in the network graph, so distant teams receive attenuated signals and may fail acquisition altogether. This distance-dependent attenuation is the primary mechanism by which network topology interacts with sharing scope.

**Stage 2 — Assimilation.** Teams that acquire the signal must then process and interpret it. The base probability of successful assimilation is `assimilation_prob = 0.7`, modified by the team's existing knowledge state in the relevant incident dimensions. Teams with richer prior knowledge in adjacent cells are modeled as better equipped to make sense of incoming information, consistent with Cohen and Levinthal's (1990) original argument that assimilation capacity is a function of prior related knowledge. A daily retry mechanism governs failed assimilation events: if a team fails assimilation on day *d*, the attempt is repeated on each subsequent day until it succeeds or the incident's knowledge signal is superseded. This retry design reflects the organizational reality that exposure to an incident report does not always produce immediate comprehension — meaning may crystallize over days as related incidents accumulate.

**Stage 3 — Transformation.** Transformation is the bottleneck stage of the pipeline. Unlike acquisition and assimilation, transformation is not governed by a fixed probability parameter. Instead, it is gated by the cosine similarity between the incoming incident's feature vector and the receiving team's current knowledge vector. Transformation succeeds when this similarity exceeds a threshold; it fails when the cognitive distance between source knowledge and receiver knowledge is too large for the receiver to integrate the new information into existing mental models. This operationalization is grounded in Nooteboom et al.'s (2007) cognitive distance framework, which predicts that knowledge transfer fails not because of motivational barriers but because the recipient lacks the structural overlap necessary to connect incoming knowledge to existing competencies. Szulanski's (1996) empirical study of intra-firm knowledge transfer corroborates this: the transformation-equivalent stage was the most difficult to complete across the 122 knowledge transfers he studied, and lack of absorptive capacity — not lack of motivation — was the primary barrier. The simulation implements this finding directly: transformation difficulty is a function of the knowledge gap, not of willingness to share.

**Stage 4 — Exploitation.** Teams that successfully complete transformation then apply the knowledge operationally. The exploitation probability is `exploitation_prob = 0.6`. On a successful exploitation event, the knowledge vector cells corresponding to the incident type are incremented: prevention, detection, and mitigation values all increase by a fixed learning increment, bounded at 1.0. Exploitation is the only stage in the pipeline that produces a measurable change in agent state and, consequently, the only stage that contributes to the Prevention K outcome metric. An incident event that completes stages 1 through 3 but fails stage 4 leaves the team's knowledge vector unchanged.

## 3.3.5 Knowledge Decay

After each simulated day, all knowledge vector values decay according to an exponential function:

> K_t = K_0 × e^(−decay_rate × t)

The default `knowledge_decay_rate = 0.001` corresponds to a half-life of approximately 693 days, or roughly two years. This calibration is grounded in Darr et al.'s (1995) empirical study of knowledge depreciation in franchise organizations, which documented substantial loss of operationally relevant knowledge over periods of months to years in the absence of reinforcing experience. Decay is applied uniformly to all 15 cells of every team's knowledge matrix at each time step, independent of whether the team experienced or shared any incidents on that day. The decay function ensures that knowledge capital must be continuously replenished through ongoing learning activity — teams cannot accumulate knowledge permanently from a single incident exposure. This design also ensures that the simulation does not produce monotonically increasing Prevention K curves that would trivially confirm any hypothesis; the equilibrium value of Prevention K under a given sharing scenario reflects the steady-state balance between acquisition-through-learning and attrition-through-decay.

## 3.3.6 Source Asymmetry

The incident source team is excluded from stages 2 through 4 of the learning pipeline. This is a deliberate design decision, not an implementation artifact. The rationale is that direct experience of a failure constitutes a qualitatively different learning modality than receiving a documented account of that failure from another team. A team that experiences a database timeout at 2 a.m. and spends four hours restoring service has acquired knowledge through embodied, high-stakes engagement with the system — a mode of learning that does not require passing through assimilation, transformation, and exploitation gates. The simulation reflects this by treating the source team as having learned implicitly and immediately, and by restricting the formal pipeline to non-source teams only.

This design decision has a consequential structural implication. Under the `LOCAL` sharing scenario — in which only the source team is within sharing scope — no non-source team ever enters the pipeline, and the transformation rate is therefore 0% by construction. This is not a pathological outcome; it is the model's representation of the real-world situation in which a team treats its incident response as a local matter and does not communicate findings to adjacent teams. The finding that `LOCAL` produces the weakest reliability outcomes across all experiments follows directly from this structural constraint.

The source asymmetry assumption further reflects the psychological safety premise described in Section 3.3.7: teams are modeled as willing and honest knowledge sharers. The assumption is that when sharing does occur, it is substantive. What varies across experiments is not the quality of sharing but its scope.

## 3.3.7 Psychological Safety Assumption

The model assumes that all teams share knowledge honestly and that all teams are open to receiving it. No motivational barriers to knowledge transfer are modeled. This is the blameless postmortem assumption: when an incident occurs, the affected team documents what happened and communicates findings without distortion, and receiving teams engage with those findings in good faith. This simplification is grounded in two bodies of literature. Edmondson (1999) demonstrates that psychological safety — the shared belief that the team is safe for interpersonal risk-taking — is the primary organizational precondition for honest incident reporting and post-failure learning. The model treats psychological safety as uniformly present across all teams, representing an idealized blameless culture. Szulanski (1996) provides the complementary empirical finding: across observed knowledge transfers, motivational factors (such as reluctance to share or reluctance to learn) were substantially weaker predictors of transfer difficulty than knowledge-structural factors (such as causal ambiguity and absorptive capacity gaps). The decision to model knowledge-structural barriers — via the transformation cosine-similarity gate — while abstracting away motivational barriers is therefore empirically defensible: it models the harder problem.

---

**Table 3.1: Model Parameters and Default Values**

| Parameter | Default Value | Description |
|---|---|---|
| `num_teams` | 20 | Number of agent teams |
| `simulation_days` | 365 | Duration of each run |
| `seeds` | 100 (500 for H3) | Independent replications |
| `base_incident_rate` | 0.05 | Daily incident probability per subsystem |
| `acquisition_prob` | 0.9 | Stage 1 base probability |
| `assimilation_prob` | 0.7 | Stage 2 base probability |
| `exploitation_prob` | 0.6 | Stage 4 base probability |
| `knowledge_decay_rate` | 0.001 | Exponential decay constant (~2yr half-life) |
| `signal_decay` | 0.8 | Per-hop acquisition multiplier |
| `ws_k` | 4 | WS network: neighbors per node |
| `ws_p` | 0.1 | WS network: rewiring probability |
| `ba_m` | 2 | BA network: edges per new node |

---

## Citation Checklist

- [ ] Zahra & George (2002) — Section 3.3.4, pipeline stage definitions: "four sequential probabilistic stages, grounded in the Zahra & George (2002) absorptive capacity framework"
- [ ] Darr et al. (1995) — Section 3.3.5, decay calibration: "grounded in Darr et al.'s (1995) empirical study of knowledge depreciation in franchise organizations"
- [ ] Nooteboom et al. (2007) — Section 3.3.4 Stage 3, transformation gate: "grounded in Nooteboom et al.'s (2007) cognitive distance framework"
- [ ] Szulanski (1996) — Section 3.3.4 Stage 3 and Section 3.3.7: "Szulanski's (1996) empirical study...transformation-equivalent stage was the most difficult to complete"; motivation not primary barrier
- [ ] Edmondson (1999) — Section 3.3.7, psychological safety assumption: "Edmondson (1999) demonstrates that psychological safety...is the primary organizational precondition for honest incident reporting"
- [ ] Cohen & Levinthal (1990) — Section 3.3.4 Stage 2, assimilation: "consistent with Cohen and Levinthal's (1990) original argument that assimilation capacity is a function of prior related knowledge"

resentation of a team that does not share knowledge beyond its own boundary. The 0% transformation rate under LOCAL is the model's prediction of what happens when organizations treat incidents as local events. This is a finding, not a flaw.
