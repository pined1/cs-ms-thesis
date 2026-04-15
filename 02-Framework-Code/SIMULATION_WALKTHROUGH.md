# Simulation Walkthrough — Two Teams, Complete Detail
**David Pineda | BYU Computer Science MS**

This document traces a complete simulation run through two teams — Team A (DATABASE) and
Team B (PAYMENT) — from initialization through final metric collection. Every parameter,
formula, and calculation is explained with its real-world meaning and theoretical grounding.

---

## Overview — What the Simulation Models

The simulation models one year (365 business days) of a software engineering organization.
Each team owns one software subsystem. Production incidents occur stochastically each day.
Teams can learn from those incidents to reduce future incident frequency and severity.

The simulation answers one central question: **does the breadth of knowledge sharing
determine how much reliability improves over a one-year period?**

Four strategies are compared: no sharing (NONE), sharing only within the team that
experienced the incident (LOCAL), sharing with directly connected teams (NEIGHBOR), and
sharing across the entire organization (GLOBAL).

---

## STEP 0 — Organization Initialization

Two teams are instantiated at the start of the simulation:

```
Team A
  - team_id   = 0
  - subsystem = DATABASE
  - responsible for the database layer — data storage and retrieval

Team B
  - team_id   = 1
  - subsystem = PAYMENT
  - responsible for payment processing — financial transaction handling
```

**Theoretical basis:** Conway's Law (Conway, 1968) states that organizations design systems
that mirror their own communication structure. The six subsystem types in the model reflect
common microservice boundaries found in real software organizations.

---

## STEP 0A — Knowledge Grid Initialization

Each team is assigned an independent knowledge grid at initialization. The grid has 15 cells:
5 incident types × 3 knowledge dimensions.

**The 5 incident types** are drawn from Dogga et al. (2023) ARTS taxonomy — an empirical
classification of software failures derived from industry postmortem analysis:

```
DATABASE_TIMEOUT    = database queries exceed time limits and stop responding
CONFIG_ERROR        = incorrect configuration deployed (wrong credentials, URLs, env vars)
DEPENDENCY_FAILURE  = an upstream or downstream service the team depends on becomes unavailable
CAPACITY_ISSUE      = memory, CPU, disk, or connection pool resources are exhausted
DEPLOYMENT_PROBLEM  = a code release directly causes a production failure
```

**The 3 knowledge dimensions** represent what a team can learn about any given incident type:

```
prevention  = competence that reduces the probability of the incident occurring
detection   = competence that reduces the time between incident start and team awareness
mitigation  = competence that reduces incident severity and total duration once active
```

**Team A's knowledge grid at initialization:**

```
                   prevention   detection   mitigation
DATABASE_TIMEOUT      0.0          0.0          0.0
CONFIG_ERROR          0.0          0.0          0.0
DEPENDENCY_FAILURE    0.0          0.0          0.0
CAPACITY_ISSUE        0.0          0.0          0.0
DEPLOYMENT_PROBLEM    0.0          0.0          0.0
```

**Team B's knowledge grid at initialization (independent and separate):**

```
                   prevention   detection   mitigation
DATABASE_TIMEOUT      0.0          0.0          0.0
CONFIG_ERROR          0.0          0.0          0.0
DEPENDENCY_FAILURE    0.0          0.0          0.0
CAPACITY_ISSUE        0.0          0.0          0.0
DEPLOYMENT_PROBLEM    0.0          0.0          0.0
```

Each team's knowledge grid is stored as a separate dictionary in memory. Updating one
team's grid has no effect on any other team's grid. Knowledge transfer between teams
occurs only when a team successfully completes all four stages of the learning pipeline,
at which point a calculated amount is written to that team's own grid.

Each cell holds a value in the range [0.0, 1.0]:
- `0.0` — no competence on this incident type and dimension
- `1.0` — maximum competence on this incident type and dimension
- Values accumulate through learning events and decay slightly each day

---

## STEP 0B — Subsystem Susceptibility Table

Before any incident is generated, the simulation requires a mapping of how vulnerable each
subsystem type is to each incident type. This is stored as a static lookup table initialized
at the start of the simulation.

Every value in the table was set based on domain reasoning about real software system failure
modes. Theoretical grounding: Dogga et al. (2023) ARTS incident taxonomy.

```
                   DB_TIMEOUT  CONFIG_ERR  DEPEND_FAIL  CAPACITY  DEPLOY_PROB
DATABASE              0.9         0.6          0.3          0.8       0.4
PAYMENT               0.4         0.7          0.8          0.5       0.6
AUTH                  0.3         0.8          0.5          0.4       0.6
FRONTEND              0.2         0.7          0.6          0.5       0.8
API                   0.5         0.7          0.7          0.6       0.7
CACHE                 0.3         0.6          0.4          0.9       0.5
```

Each cell represents the susceptibility of that subsystem to that incident type on a 0–1
scale. A value of 0.9 indicates very high vulnerability. A value of 0.2 indicates low
vulnerability.

**Rationale for each row:**

- **DATABASE** — High susceptibility to DATABASE_TIMEOUT (0.9) because database query
  timeouts are a primary failure mode for database systems. High CAPACITY (0.8) because
  databases accumulate data over time. Low DEPENDENCY_FAILURE (0.3) because databases
  are depended upon by other services rather than depending on them.

- **PAYMENT** — High DEPENDENCY_FAILURE (0.8) because payment processing calls external
  payment processor APIs (e.g., Stripe, Braintree). Failure of those external services
  cascades directly into the payment subsystem.

- **AUTH** — High CONFIG_ERROR (0.8) because authentication systems are highly sensitive
  to configuration. An incorrect JWT secret, OAuth redirect URI, or environment variable
  immediately prevents all users from logging in.

- **FRONTEND** — High DEPLOYMENT_PROBLEM (0.8) because frontend deployments produce
  immediate, visible failures. Low DATABASE_TIMEOUT (0.2) because frontend code does
  not interact directly with the database.

- **API** — Moderate values across all incident types (0.5–0.7) because the API gateway
  is the connective layer that interacts with databases, external dependencies, configuration,
  capacity management, and deployment pipelines simultaneously.

- **CACHE** — High CAPACITY_ISSUE (0.9) because caching systems exist specifically to
  absorb memory load. Cache exhaustion causes cascading failures. Low DATABASE_TIMEOUT
  (0.3) because caches exist to reduce database calls.

**Two uses of this table:**

1. **Incident generation** — when an incident fires for a team, the simulation draws the
   incident type using the team's susceptibility row as a probability distribution.

2. **Relevance calculation** — when a secondary team attempts to learn from another team's
   incident, the target team's susceptibility to that incident type determines how relevant
   the learning material is.

---

## STEP 0C — Network Construction

The communication network is constructed once at simulation startup and remains fixed for
all 365 days. It represents the communication structure of the organization — which teams
regularly share information, review each other's postmortems, and attend shared meetings.

Each team is represented as a node. Each communication relationship between two teams is
represented as an edge. The edge carries a weight representing the strength of that
communication channel.

**Two-team network for this walkthrough:**

```
[Team A] ————— [Team B]
           0.85
```

The edge weight of 0.85 was drawn at network construction time from a uniform distribution:

```python
edge_weight = Uniform(0.5, 1.0)
```

- `0.5` — minimal communication. The teams are connected but interact infrequently.
- `1.0` — maximum communication. Teams collaborate daily, share OKRs, co-review work.
- `0.85` — strong communication channel. Regular interaction and information sharing.

Edge weights are randomized because communication relationship strength varies across
real organizations. Running 100 independent seeds averages the effect of any one
network's particular edge weight distribution.

**Three network topologies used across experiments:**

**Watts-Strogatz (default for all core experiments):**
```python
g = nx.watts_strogatz_graph(n, k=4, p=0.1)
```
Each team begins connected to its 4 nearest neighbors. Then 10% of those edges are
randomly rewired to create long-range connections. This produces a small-world graph:
locally clustered like a real team structure, with occasional cross-org shortcuts.
Grounded in: Watts & Strogatz (1998).

**Erdős-Rényi (used in topology sensitivity experiment):**
```python
g = nx.erdos_renyi_graph(n, p=0.3)
```
Every pair of teams has an independent 30% probability of being connected. No structural
assumption is imposed. Used to verify the core H1 finding is not dependent on topology.

**Barabási-Albert (used in H3 org conditions experiment):**
```python
g = nx.barabasi_albert_graph(n, m=2)
```
New nodes preferentially attach to existing high-degree nodes. Produces hub teams with
many connections and peripheral teams with few. Models organizations with a central
platform or SRE team connected to all product teams.

**How the four learning scenarios use the network:**

```
NONE      — network is not consulted. No teams are eligible to learn.
LOCAL     — network is not consulted. Only the source team is eligible.
NEIGHBOR  — network is active. Source team + direct neighbors are eligible.
GLOBAL    — network is not consulted. All teams are eligible regardless of position.
```

The network is only consequential under the NEIGHBOR scenario. Under GLOBAL, every team
is eligible at full acquisition probability regardless of network distance. This is the
primary structural difference between the two strategies and is why GLOBAL outperforms
NEIGHBOR at larger organizational scales — GLOBAL removes distance penalties entirely.

---

## STEP 0D — Metrics Storage Initialization

Before the simulation loop begins, all metric containers are initialized to empty.

```python
metrics = {
    # Running totals — single numbers that accumulate across all 365 days
    "total_incidents":             0,
    "cumulative_engineering_cost": 0.0,
    "cumulative_learning_cost":    0.0,

    # Time series — one value appended per day, 365 values at end of simulation
    "incident_frequency":          {},    # per subsystem
    "incident_duration":           [],
    "incident_severity":           [],
    "engineering_cost":            [],
    "avg_prevention_knowledge":    [],
    "avg_detection_knowledge":     [],
    "avg_mitigation_knowledge":    [],
    "acquisition_rate":            [],
    "assimilation_rate":           [],
    "transformation_rate":         [],
    "exploitation_rate":           [],
    "mtbf":                        [],
    "mttr":                        [],
    "mttd":                        [],
}
```

The running totals accumulate across the entire year and become the summary statistics
reported in the thesis results tables. The time series arrays each contain one value per
day and become the data behind learning-curve plots and trajectory charts.

---

# THE DAILY SIMULATION LOOP — Day 1

The following sequence executes once per day for each of the 365 simulation days.
Day 1 is traced in complete detail below.

---

## PRE-PHASE A — Deployment Risk Decay

At the start of each day, the deployment risk counter for each subsystem decrements by one,
with a floor of zero:

```python
recent_deployments[DATABASE] = max(0, recent_deployments[DATABASE] - 1)
recent_deployments[PAYMENT]  = max(0, recent_deployments[PAYMENT]  - 1)
```

This counter tracks residual deployment risk from recent code pushes. When a deployment
occurs, the counter is set to 3. It decrements daily until it returns to 0. An active
counter (value > 0) triggers an elevated incident probability multiplier.

Day 1: both counters are 0 at initialization and remain 0.

---

## PRE-PHASE B — Deployment Roll

Each team independently rolls for a deployment event:

```python
if random() < deployment_rate:      # deployment_rate = 0.1
    recent_deployments[team.subsystem] = 3
```

**`deployment_rate = 0.1`** — each team deploys code on approximately 10% of business days,
or roughly once every two weeks. This aligns with the "medium performer" deployment
frequency band in Forsgren et al. (2018) *Accelerate*.

**Why 3 days of elevated risk?** Empirical evidence from site reliability engineering
practice indicates that deployment-caused incidents predominantly surface within 72 hours
of the release. After that window, the change is considered stable in production.

Day 1 results:
- Team A roll: 0.07 < 0.10 → **Team A deployed.** `recent_deployments[DATABASE] = 3`
- Team B roll: 0.54 > 0.10 → Team B did not deploy.

---

## PRE-PHASE C — Knowledge Decay

All knowledge values across all teams decay by a fixed daily rate before any new
knowledge is added:

```python
for team in teams:
    for incident_type in IncidentType:
        team.knowledge[incident_type]["prevention"] *= (1 - knowledge_decay)
        team.knowledge[incident_type]["detection"]  *= (1 - knowledge_decay)
        team.knowledge[incident_type]["mitigation"] *= (1 - knowledge_decay)
```

**`knowledge_decay = 0.001`** — a 0.1% daily decay applied to every cell in every team's
knowledge grid.

**Formal expression:** `K_t = K_{t-1} × (1 - δ) + ΔK_t`

where δ = 0.001 is the daily decay rate and ΔK_t is any new knowledge gained on day t.

**Theoretical basis:** Darr et al. (1995) measured organizational learning decay in
production environments and found an empirical half-life of approximately two years.
At δ = 0.001 per day, a knowledge value of 1.0 decays to 0.5 in 693 days (≈ 1.9 years),
consistent with that finding.

**What this models:** Engineers leave organizations. Runbooks go stale. Documentation
becomes outdated. Systems change and previously learned defenses become less applicable.
Knowledge decay ensures the simulation reaches a dynamic steady state in which teams
must continually refresh knowledge rather than converging to zero incidents.

Day 1: all knowledge values are 0.0. `0.0 × 0.999 = 0.0`. No observable effect on day 1,
but the mechanism becomes consequential once knowledge has accumulated.

---

## PHASE 1 — Incident Generation

For each team, the simulation determines whether a production incident occurs on this day.
Three factors combine to produce the final incident probability.

---

### Step 1.1 — Calculate Team A's Incident Probability

**Factor 1 — Base incident rate:**

```
base_incident_rate = 0.05
```

Every team begins each day with a 5% baseline probability of experiencing an incident.
This represents the irreducible background risk present in any software system regardless
of team competence: hardware failures, cloud provider outages, novel failure modes, and
external dependencies introduce risk that no amount of internal learning can fully eliminate.

**Parameter justification:** At 5% per day, a team expects approximately 18 incidents per
year (0.05 × 365 = 18.25). This equates to 1–2 incidents per month, a rate consistent with
mid-maturity software teams as described in Lunney & Lueder (2016).

---

**Factor 2 — Prevention modifier:**

The simulation reads the team's current prevention knowledge across all five incident types
and computes an average:

```python
avg_prevention = mean([
    team_A.knowledge[DATABASE_TIMEOUT]["prevention"],    # 0.0
    team_A.knowledge[CONFIG_ERROR]["prevention"],         # 0.0
    team_A.knowledge[DEPENDENCY_FAILURE]["prevention"],  # 0.0
    team_A.knowledge[CAPACITY_ISSUE]["prevention"],      # 0.0
    team_A.knowledge[DEPLOYMENT_PROBLEM]["prevention"],  # 0.0
]) = 0.0

prevention_modifier = 1.0 - (avg_prevention × prevention_effect)
                    = 1.0 - (0.0 × 0.5)
                    = 1.0
```

**`prevention_effect = 0.5`** — the maximum achievable incident rate reduction from
prevention knowledge. A team with perfect knowledge across all incident types
(avg_prevention = 1.0) achieves a modifier of `1.0 - 0.5 = 0.50`, reducing incident
probability by 50%. This ceiling reflects that some incident causes remain external and
unpreventable regardless of team competence.

**Why average across all five incident types?** General team preparedness — monitoring
discipline, runbook maintenance, architectural vigilance — is not perfectly partitioned
by incident type. A team experienced in database timeouts also develops general
operational habits that reduce vulnerability across other failure modes.

**Modifier scale across the range of possible knowledge values:**
```
avg_prevention = 0.0 → modifier = 1.00 → incident rate = 5.0%
avg_prevention = 0.2 → modifier = 0.90 → incident rate = 4.5%
avg_prevention = 0.5 → modifier = 0.75 → incident rate = 3.75%
avg_prevention = 1.0 → modifier = 0.50 → incident rate = 2.5%
```

---

**Factor 3 — Deployment modifier:**

```python
if recent_deployments[team.subsystem] > 0:
    deployment_modifier = 1.5
else:
    deployment_modifier = 1.0
```

Team A deployed on this day, so `recent_deployments[DATABASE] = 3 > 0`.

**`deployment_risk_multiplier = 1.5`** — active deployment windows elevate incident
probability by 50%. This operationalizes the empirical finding from Forsgren et al. (2018)
that change failure rate — incidents directly attributable to code releases — is one of
the four key DORA reliability metrics distinguishing high-performing engineering organizations.

---

**Final incident probability computation:**

```
p_incident = base_incident_rate × prevention_modifier × deployment_modifier
           = 0.05               × 1.0                 × 1.5
           = 0.075
```

The three factors multiply because they are independent. Prevention knowledge reflects
internal team readiness. Deployment risk reflects external change pressure. Neither
modulates the other — they scale the base rate independently.

A random draw is taken: `roll = 0.04`. Since 0.04 < 0.075, **an incident fires for Team A.**

---

### Step 1.2 — Incident Type Selection

The incident type is drawn probabilistically using Team A's susceptibility row as weights:

```
DATABASE_TIMEOUT:    0.9 / 3.0 = 30%
CONFIG_ERROR:        0.6 / 3.0 = 20%
DEPENDENCY_FAILURE:  0.3 / 3.0 = 10%
CAPACITY_ISSUE:      0.8 / 3.0 = 27%
DEPLOYMENT_PROBLEM:  0.4 / 3.0 = 13%
```

The five susceptibility values sum to 3.0. Dividing each by the total converts them to
a proper probability distribution. A weighted random draw selects **DATABASE_TIMEOUT**.

This outcome is consistent with real-world patterns: a database team that just pushed a
deployment is at elevated risk of database timeout errors caused by schema changes,
query plan invalidation, or connection pool misconfiguration.

---

### Step 1.3 — Severity Calculation

Incident severity is drawn from a normal distribution and scaled by the team's current
mitigation knowledge:

```python
avg_mitigation = mean([all 5 mitigation values for Team A]) = 0.0

severity_modifier = 1.0 - (avg_mitigation × mitigation_effect)
                  = 1.0 - (0.0 × 0.3)
                  = 1.0

severity = clip(Normal(3.0, 1.0) × severity_modifier, 1.0, 5.0)
         = clip(3.4 × 1.0, 1.0, 5.0)
         = 3.4
```

**`incident_severity_base = 3.0`** — the mean severity of an incident on a 1–5 scale.
A value of 3.0 places the average incident in the moderate range — significant enough
to require on-call response but not catastrophic. This mirrors real severity classification
schemes such as PagerDuty P1–P5 or Google SRE criticality levels (Lunney & Lueder, 2016).

**`incident_severity_std = 1.0`** — incident severity follows a normal distribution with
standard deviation 1.0. Most incidents fall between severity 2 and 4. Severe (5) and
trivial (1) incidents occur at the tails of the distribution.

**`mitigation_effect = 0.3`** — mitigation knowledge can reduce effective severity by up
to 30%. A team with full mitigation knowledge (`avg_mitigation = 1.0`) achieves
`severity_modifier = 0.70`, meaning incidents that do occur are 30% less damaging because
the team responds more effectively — correct escalation, faster diagnosis, avoiding actions
that worsen the situation.

**`clip(value, 1.0, 5.0)`** — constrains the result to the valid severity range. The
normal distribution can occasionally produce values below 1.0 or above 5.0; the clip
operation enforces the scale boundaries.

---

### Step 1.4 — Duration Calculation

Incident duration has two components: detection time and resolution time.

**Detection time** — the interval from incident onset to team awareness:

```python
avg_detection = mean([all 5 detection values for Team A]) = 0.0

detection_modifier = 1.0 - (avg_detection × detection_effect)
                   = 1.0 - (0.0 × 0.3)
                   = 1.0

base_detection_time = incident_duration_base × 0.4 = 2.0 × 0.4 = 0.8 hours
detection_time = max(0.1, Normal(0.8, 0.4) × detection_modifier)
               = max(0.1, 0.72)
               = 0.72 hours
```

**`incident_duration_base = 2.0 hours`** — the baseline mean total incident duration.
A 2-hour total incident duration (combining detection and resolution) reflects a typical
moderate-severity incident at a mid-maturity engineering organization. Google SRE data
(Lunney & Lueder, 2016) supports this range for P3-equivalent incidents.

**Why 40% of duration is detection?** Empirical SRE data indicates that teams commonly
spend 30–50% of total incident time in the detection phase — the period between when
something first fails and when the team confirms an active incident. Alert validation,
false positive ruling-out, and root cause localization contribute to this fraction.
The 40/60 detection-to-resolution split is a calibrated modeling choice.

**`detection_effect = 0.3`** — detection knowledge (improved dashboards, tuned alert
thresholds, runbook-guided diagnosis) can reduce time-to-detect by up to 30%.

**`max(0.1, ...)`** — detection time has a minimum floor of 0.1 hours (6 minutes),
reflecting that even the fastest team requires some minimum time for alert processing,
acknowledgment, and initial investigation.

---

**Resolution time** — the interval from detection to full incident resolution:

```python
base_resolution_time = incident_duration_base × 0.6 = 2.0 × 0.6 = 1.2 hours
resolution_time = max(0.4, Normal(1.2, 0.6) × severity_modifier)
                = max(0.4, 1.35)
                = 1.35 hours
```

Resolution time is scaled by `severity_modifier` rather than `detection_modifier` because
the difficulty of resolving an incident is driven by its severity, not by how quickly it
was detected. The `max(0.4)` floor represents the minimum resolution time even for simple
fixes — deployment, verification, and post-fix monitoring require some minimum duration.

**Total duration:**

```
duration = detection_time + resolution_time = 0.72 + 1.35 = 2.07 hours
```

---

### Step 1.5 — Engineering Cost Calculation

Engineering cost quantifies the human labor consumed by the incident, measured in
engineer-hours.

**Definition:** One engineer-hour equals one engineer working for one hour. This unit is
used because it is technology-agnostic and converts directly to financial cost (engineer
salary × hours) and opportunity cost (features not built, technical debt not addressed,
other work deferred).

**Formula:**

```python
cost = engineering_cost_base × (severity / 3.0) × (duration / 2.0)
     = 4.0               × (3.4 / 3.0)       × (2.07 / 2.0)
     = 4.0               × 1.133              × 1.035
     = 4.69 engineer-hours
```

**`engineering_cost_base = 4.0 hours`** — every incident incurs a minimum floor cost of
4 engineer-hours regardless of severity or duration. This floor accounts for the sum of
all labor associated with an incident response: the interrupt cost of paging the on-call
engineer, context switching from ongoing work, initial triage, coordination overhead,
the fix itself, post-incident review, and the time of all engineers reading the postmortem.
Even a trivial severity-1 incident that resolves in under 30 minutes typically consumes
4 total engineer-hours across all participants.

**`(severity / 3.0)`** — re-centers severity around a neutral multiplier of 1.0. An
average-severity incident (3.0) produces a ratio of 1.0 and leaves cost unchanged. Higher
severity produces a ratio above 1.0, scaling cost upward proportionally.

**`(duration / 2.0)`** — re-centers duration around a neutral multiplier of 1.0. A
baseline-duration incident (2.0 hours) produces a ratio of 1.0. Longer incidents scale
cost upward; shorter incidents scale it downward.

**This is an org-wide metric.** The simulation collects incident costs from every team
throughout the day and sums them:

```python
timestep_costs = []

# Each time any team has an incident during Phase 1:
timestep_costs.append(cost)    # add to today's cost list

# At Phase 3, the day's total is recorded:
metrics["engineering_cost"].append(sum(timestep_costs))
metrics["cumulative_engineering_cost"] += sum(timestep_costs)
```

Day 1 has only one incident (Team A's DATABASE_TIMEOUT):
```python
timestep_costs = [4.69]
metrics["engineering_cost"].append(4.69)
metrics["cumulative_engineering_cost"] += 4.69    # running total = 4.69
```

**Two related metrics:**

`metrics["engineering_cost"]` — a 365-element array, one value per day, representing the
total engineering labor cost of all incidents across all teams on that specific day.

`metrics["cumulative_engineering_cost"]` — a single running total that accumulates all
daily costs. At year end, this is the total organizational engineering labor cost of
all production incidents for the year. This is one of the two primary outcome variables
for economic comparison across learning scenarios.

---

### Step 1.6 — Learnable Knowledge Assignment

Each incident is assigned a fixed quantity of knowledge that can potentially be extracted
from a thorough postmortem:

```python
learnable_knowledge = {
    "prevention": Uniform(0.10, 0.25),    # drawn = 0.18
    "detection":  Uniform(0.10, 0.25),    # drawn = 0.21
    "mitigation": Uniform(0.10, 0.25),    # drawn = 0.14
}
```

**What this represents:** If a team perfectly completes all four stages of the learning
pipeline for this incident, they will gain 0.18 units of prevention knowledge, 0.21 units
of detection knowledge, and 0.14 units of mitigation knowledge for the DATABASE_TIMEOUT
incident type. These values represent the maximum extractable insight from one incident.

**Parameter justification:** The range Uniform(0.10, 0.25) models variation in incident
richness. Some incidents expose novel failure modes and carry substantial learning value.
Others repeat familiar patterns and yield marginal new insight. The floor of 0.10 ensures
every incident contributes at least some learning opportunity. The ceiling of 0.25 ensures
no single incident provides complete expertise — reaching mastery requires accumulation
across multiple incidents over time.

---

### Step 1.7 — MTBF Tracking

Each time an incident fires, the simulation records the elapsed days since the previous
incident for that subsystem as an MTBF sample:

```python
if time_since_incident[DATABASE] > 0:
    mtbf_samples[DATABASE].append(time_since_incident[DATABASE])
time_since_incident[DATABASE] = 0    # reset counter
```

**MTBF (Mean Time Between Failures)** — the average number of days between production
incidents for a given subsystem. Measured in days.

The counter `time_since_incident[subsystem]` increments by 1 each day without an incident
and resets to 0 when an incident occurs. The sequence of recorded gaps constitutes the
MTBF sample set.

Day 1: `time_since_incident[DATABASE]` was 0 at initialization. No gap sample is recorded.
The counter resets to 0. Starting from Day 2, gap accumulation begins.

Concurrently, the incident's duration and detection time are appended to their respective
sample lists for MTTR and MTTD tracking:

```python
mttr_samples.append(duration)          # 2.07 hours
mttd_samples.append(detection_time)    # 0.72 hours
```

---

### Step 1.8 — Source Team Knowledge Update (Source Asymmetry)

The team that directly experienced the incident — Team A — gains knowledge immediately,
bypassing the four-stage learning pipeline:

```python
team_A.acquired_incidents.add(0)
team_A.assimilated_incidents.add(0)
team_A.transformed_incidents.add(0)
team_A.exploited_incidents.add(0)

team_A.learn(DATABASE_TIMEOUT, "prevention", 0.18)
team_A.learn(DATABASE_TIMEOUT, "detection",  0.21)
team_A.learn(DATABASE_TIMEOUT, "mitigation", 0.14)
```

The `learn()` method applies a knowledge update capped at 1.0:

```python
new_value = min(1.0, current_value + amount)
          = min(1.0, 0.0 + 0.18)
          = 0.18
```

**Theoretical basis:** The source team's direct experience constitutes a fundamentally
different learning mode from secondary observation. The experiencing team acquires
first-hand causal knowledge, observes the full failure sequence, and is motivated by
urgency to implement preventive changes. Zahra & George (2002) distinguish this as
realized absorptive capacity emerging from direct operational experience rather than
through the mediated learning pathway.

**Ablation note:** This asymmetry is a model assumption tested in Experiment 12. Setting
`disable_source_asymmetry = True` routes the source team through the same four-stage
pipeline as all other teams, allowing measurement of how much the asymmetry assumption
affects the core results.

**Team A's knowledge grid after Day 1:**

```
                   prevention   detection   mitigation
DATABASE_TIMEOUT      0.18         0.21         0.14    ← updated
CONFIG_ERROR          0.0          0.0          0.0
DEPENDENCY_FAILURE    0.0          0.0          0.0
CAPACITY_ISSUE        0.0          0.0          0.0
DEPLOYMENT_PROBLEM    0.0          0.0          0.0
```

Only the DATABASE_TIMEOUT row was updated because that is the incident type that occurred.
The remaining 12 cells are unchanged.

**Effect on Day 2 incident probability:**

```
avg_prevention = mean([0.18, 0.0, 0.0, 0.0, 0.0]) = 0.036
prevention_modifier = 1.0 - (0.036 × 0.5) = 0.982
p_incident (no deployment) = 0.05 × 0.982 = 0.049
```

The incident probability for Team A decreases from 5.0% to 4.9% on Day 2 — a modest
but real reduction. Across many incidents over 365 days, this compounding effect produces
a substantial year-end reduction in total incidents.

---

## PHASE 2 — Four-Stage Learning Pipeline (Secondary Teams)

Following incident generation, the simulation processes learning opportunities for all
teams eligible to learn from the incident under the active sharing scenario.

**Eligibility determination:**

```python
potential_learners = get_learners_for_scenario(
    scenario = NEIGHBOR,
    source   = team_A.team_id,
    all_ids  = [0, 1],
    graph    = network
)
→ [0, 1]    # Team A + Team A's direct neighbors
```

Team A (the source) is excluded from Phase 2 because it already updated its knowledge in
Phase 1. The pipeline processes Team B only.

The pipeline consists of four sequential stages based on Zahra & George (2002) absorptive
capacity theory. Each stage is a stochastic gate: passing requires a probability draw to
succeed. Failing any stage permanently terminates learning for that team-incident pair.
The simulation does not retry failed stages on subsequent days.

```
ACQUISITION → ASSIMILATION → TRANSFORMATION → EXPLOITATION → Knowledge Written to Grid
```

---

### STAGE 1 — ACQUISITION
**Operational question: Did Team B receive and read the incident postmortem?**

**Real-world process:** Following an incident, the source team publishes a postmortem
document — in a shared wiki, a Slack channel, or an incident management system. Whether
secondary teams receive and read this document depends on organizational communication
reach and the strength of the connection between teams.

**Theoretical basis:** Drupsteen & Guldenmund (2014) documented that organizations
systematically fail to disseminate incident lessons even when documentation exists.
Information reach decreases with organizational distance.

**Formula:**

For a direct neighbor (Team B is adjacent to Team A in the network):
```python
p_acquire = acquisition_probability × edge_weight
           = 0.9               × 0.85
           = 0.765
```

**`acquisition_probability = 0.9`** — the maximum probability that a directly connected
team receives and reads an incident postmortem. Even in the best-connected organizations,
some postmortems are missed: they are posted in channels not monitored by the relevant
team, or they are deprioritized during high-workload periods. The 10% miss rate reflects
this documented organizational reality.

**`edge_weight = 0.85`** — the communication channel strength between Team A and Team B,
assigned at network construction from Uniform(0.5, 1.0). Stronger channels produce
higher information reach.

**Signal decay for non-adjacent teams (path hops):**

When a learning-eligible team is not directly connected to the source team, information
must propagate through intermediate teams. Each hop attenuates the signal:

```python
p_acquire = acquisition_probability × (signal_decay ^ path_length)
```

**`signal_decay = 0.8`** — each intermediate hop reduces effective acquisition probability
by 20%. Each retelling of an incident story drops contextual details, simplifies causal
chains, and introduces distortion. Grounded in Shannon & Weaver (1949) information theory;
supported by organizational communication research on knowledge degradation through
transmission chains.

**Decay by hop distance:**
```
1 hop (direct):  0.9 × 0.80 = 0.720
2 hops:          0.9 × 0.64 = 0.576
3 hops:          0.9 × 0.51 = 0.461
4 hops:          0.9 × 0.41 = 0.369
5 hops:          0.9 × 0.33 = 0.295
```

**Relevance to H1 and H3:** Under GLOBAL, all teams receive `p_acquire = 0.9` regardless
of distance — the broadcast mechanism removes the distance penalty. Under NEIGHBOR, only
direct neighbors are eligible and the edge weight applies. This structural difference
explains why GLOBAL produces superior outcomes at large organizational scales where many
teams are multiple hops from any given incident source.

**Day 1 acquisition for Team B:**
```
p_acquire = 0.9 × 0.85 = 0.765
roll = 0.41 < 0.765 → PASS
```

Team B's `acquired_incidents` set: `{0}`

---

### STAGE 2 — ASSIMILATION
**Operational question: Did Team B understand the root cause of the incident?**

**Real-world process:** Reading a postmortem is not equivalent to understanding it.
A database timeout postmortem may reference connection pool exhaustion, query plan
invalidation, or index fragmentation. Comprehending these mechanisms requires prior
exposure to database systems. Without that prior knowledge, the team may read the
document but fail to extract the causal logic.

**Theoretical basis:** Cohen & Levinthal (1990) absorptive capacity theory: the ability
to recognize, value, and absorb new knowledge is a function of prior related knowledge.
Organizations with no prior knowledge in a domain cannot assimilate new knowledge in
that domain regardless of how clearly it is documented.

**Formula:**

```python
p_assimilate = (0.7 × cognitive_factor + 0.3 × documentation_quality)
               × assimilation_probability
               × (0.5 + 0.5 × relevance)
```

**Component 1 — Cognitive Factor**

The cognitive factor measures how well-positioned Team B is to understand Team A's
knowledge, based on the cognitive distance between the two teams.

Step 1: Flatten each team's 15-cell knowledge grid into a vector.

```
Team A's knowledge vector (15 values):
[0.18, 0.21, 0.14,  ← DATABASE_TIMEOUT: prevention, detection, mitigation
 0.0,  0.0,  0.0,   ← CONFIG_ERROR
 0.0,  0.0,  0.0,   ← DEPENDENCY_FAILURE
 0.0,  0.0,  0.0,   ← CAPACITY_ISSUE
 0.0,  0.0,  0.0]   ← DEPLOYMENT_PROBLEM

Team B's knowledge vector (15 values):
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

Step 2: Compute cosine similarity between the two vectors. Cosine similarity measures
the angle between vectors, capturing directional similarity in knowledge structure.
When Team B's vector contains all zeros (no prior knowledge), the cosine is undefined.
The simulation returns 0.5 in this case.

**Why 0.5 for undefined similarity?** A value of 0.5 maps to the peak of the
inverted-U absorptive capacity function, representing maximum learning capacity.
Cohen & Levinthal (1990) establish that blank-slate learners — those with no prior
knowledge in a domain — have maximum absorptive potential precisely because they carry
no conflicting prior models or entrenched misunderstandings.

Step 3: Apply the inverted-U function from Nooteboom et al. (2007):

```python
cognitive_factor = 4.0 × similarity × (1 - similarity) / (4.0 × 0.5 × 0.5)
                 = 4.0 × 0.5 × 0.5 / 1.0
                 = 1.0
```

**The inverted-U relationship:**
```
similarity = 0.0 → cognitive_factor = 0.0  (identical knowledge: nothing new to learn)
similarity = 0.5 → cognitive_factor = 1.0  (intermediate distance: maximum learning)
similarity = 1.0 → cognitive_factor = 0.0  (fully dissimilar: cannot comprehend)
```

This curve captures two failure modes: learning nothing because the teams already know
the same things, and learning nothing because the knowledge gap is too large to bridge.
Maximum learning occurs at intermediate cognitive distance.

As teams accumulate knowledge over 365 days, their vectors fill in. If two teams both
experience similar incident types, their cosine similarity rises, cognitive_factor
decreases, and the marginal value of sharing between them diminishes. The model
captures diminishing returns on knowledge sharing between highly similar teams.

---

**Component 2 — Documentation Quality**

The two components are weighted and combined:

```
0.7 × cognitive_factor + 0.3 × documentation_quality
= 0.7 × 1.0            + 0.3 × 0.5
= 0.85
```

**`documentation_quality = 0.5`** — represents average postmortem quality. The document
exists, has some structure, and captures the key facts, but is not a comprehensive
root-cause analysis.

**Weight rationale (70% cognitive, 30% documentation):** An engineer's existing knowledge
is the primary determinant of whether they can absorb new information. A senior engineer
with deep domain expertise can extract root cause understanding from a minimal incident
description. A junior engineer with no domain background will not comprehend a technically
detailed postmortem. Documentation quality is a contributing factor but secondary to
the cognitive readiness of the learner. This weighting is consistent with absorptive
capacity theory (Cohen & Levinthal, 1990).

---

**Component 3 — Relevance**

Relevance measures how applicable the incident type is to the learning team's subsystem.

```python
target_susceptibility = DEFAULT_SUSCEPTIBILITY[PAYMENT][DATABASE_TIMEOUT]
                      = 0.4

if target_susceptibility > 0.5:
    relevance = target_susceptibility    # high relevance: directly applicable
else:
    relevance = BASE_RELEVANCE = 0.3     # lower relevance: general lessons only
```

PAYMENT's susceptibility to DATABASE_TIMEOUT is 0.4, which does not exceed the 0.5
threshold. Therefore `relevance = 0.3`.

**Interpretation:** DATABASE_TIMEOUT is not a primary failure mode for payment systems.
The PAYMENT team receives general lessons from this incident — awareness that timeouts
exist, that defensive programming (retry logic, circuit breakers) is warranted, that
monitoring should include timeout metrics — but does not extract database-specific
expertise.

**The relevance modifier applied to the probability:**

```
(0.5 + 0.5 × relevance) = 0.5 + 0.5 × 0.3 = 0.65
```

**Why `0.5 + 0.5 × relevance` rather than `relevance` directly?** Using raw relevance as
a multiplier would reduce learning probability to near zero for low-relevance incidents.
However, general operational lessons (monitoring practices, escalation procedures,
incident taxonomy, runbook structure) transfer across all subsystem boundaries. The
additive floor of 0.5 ensures that every incident, regardless of subsystem mismatch,
carries at least half-weight learning value for cross-functional organizational
competence.

**Relevance modifier scale:**
```
relevance = 0.0 → modifier = 0.50  (no direct applicability; general lessons only)
relevance = 0.3 → modifier = 0.65  (low applicability)  ← present case
relevance = 0.5 → modifier = 0.75  (moderate applicability)
relevance = 0.8 → modifier = 0.90  (high applicability)
relevance = 1.0 → modifier = 1.00  (maximum applicability; same subsystem type)
```

---

**Final assimilation probability:**

```
p_assimilate = 0.85 × assimilation_probability × relevance_modifier
             = 0.85 × 0.7                       × 0.65
             = 0.387
```

**`assimilation_probability = 0.7`** — the maximum assimilation probability under ideal
cognitive and documentation conditions. This ceiling reflects that even in favorable
circumstances, 30% of assimilation attempts fail due to cognitive load, distraction,
or incomplete processing. This ceiling is not exceeded regardless of cognitive_factor
or documentation quality values.

Random draw: `roll = 0.29`. Since 0.29 < 0.387, **Team B passes assimilation.**

Team B's `assimilated_incidents` set: `{0}`

Team B has processed the root cause of Team A's incident and understands the mechanism
that caused the DATABASE_TIMEOUT.

---

### STAGE 3 — TRANSFORMATION
**Operational question: Did Team B connect this incident's lessons to their own system?**

**Real-world process:** Understanding another team's incident is distinct from recognizing
its implications for one's own system. The transformation step requires an engineer to
reason analogically: "Team A's database timed out due to connection pool exhaustion.
Our payment service maintains a connection pool to our payment processor API. The same
exhaustion mechanism could apply. We should audit our connection pool configuration and
add circuit breakers." This analogical mapping from an external incident to an internal
vulnerability is the transformation step.

**Theoretical basis:** Zahra & George (2002) identify transformation as the most
cognitively demanding stage of absorptive capacity. It requires recombining externally
acquired knowledge with existing organizational knowledge to produce novel insights
about one's own system.

**Formula:**

```python
p_transform = (0.8 × cognitive_factor + 0.2 × documentation_quality)
              × transformation_probability
              × (0.5 + 0.5 × relevance)
```

The same cognitive_factor (1.0) and relevance (0.3) apply. The key structural difference
from assimilation is the weighting: **80% cognitive, 20% documentation**.

```
0.8 × 1.0 + 0.2 × 0.5 = 0.90
```

**Weighting rationale:** Transformation is an internal cognitive process. The postmortem
has already been read and understood during assimilation. What determines transformation
success is whether the engineer can reason from the external incident to internal
vulnerability — a task that depends on the engineer's existing knowledge of their own
system, not on the quality of the external document. The documentation weight decreases
from 0.3 to 0.2 to reflect this shift.

```
p_transform = 0.90 × 0.7 × 0.65 = 0.409
```

**`transformation_probability = 0.7`** — the base ceiling for transformation under ideal
conditions. Transformation is the stage most susceptible to failure in organizational
learning. Zahra & George (2002) note that organizations frequently succeed in acquiring
and understanding external knowledge yet fail to integrate it into operational practice.

Random draw: `roll = 0.52`. Since 0.52 > 0.409, **Team B fails transformation.**

Incident #0 remains permanently in Team B's `assimilated_incidents` set and will never
be added to `transformed_incidents`. The learning pathway for this incident is closed.
Team B understood the incident in the abstract but did not connect it to a vulnerability
in their own system.

---

### STAGE 4 — EXPLOITATION
*This stage would execute if Stage 3 had succeeded. Presented for completeness.*

**Operational question: Did Team B implement a concrete change based on the transformed
knowledge?**

**Real-world process:** Recognizing that one's system has a vulnerability analogous to
another team's incident does not automatically result in a fix. Engineers must prioritize
the remediation, allocate sprint capacity, implement the change, and deploy it. Many
recognized vulnerabilities are logged in a backlog and never addressed.

**Theoretical basis:** Pfeffer & Sutton (2000) documented the knowing-doing gap —
the systematic organizational failure to convert knowledge and intention into action.
Exploitation is where the knowing-doing gap manifests in the simulation.

**Formula:**

```python
relevance = team_B.get_susceptibility(DATABASE_TIMEOUT)
           = DEFAULT_SUSCEPTIBILITY[PAYMENT][DATABASE_TIMEOUT]
           = 0.4

p_exploit = exploitation_probability × (0.5 + 0.5 × relevance)
           = 0.6 × (0.5 + 0.5 × 0.4)
           = 0.6 × 0.70
           = 0.42
```

**`exploitation_probability = 0.6`** — the lowest ceiling among the four pipeline stages.
Even when a team has fully transformed knowledge about a vulnerability, 40% of potential
exploitation events do not produce an implemented change. Sprint capacity constraints,
competing priorities, and organizational inertia contribute to this gap.

**Different relevance source at Stage 4:** Stages 2 and 3 used `calculate_relevance()`
which applies a floor of 0.3 for general lessons. Stage 4 uses raw susceptibility directly
(0.4 for PAYMENT+DATABASE_TIMEOUT). The rationale: exploitation is driven by urgency and
perceived risk. Teams prioritize defensive implementations based on how vulnerable their
own system is to the specific incident type. Conceptual general lessons (Stages 2 and 3)
benefit from the relevance floor because understanding is valuable regardless of urgency.
Action prioritization (Stage 4) is determined by actual risk exposure.

**Knowledge written to Team B's grid if exploitation succeeds:**

```python
for dimension in ["prevention", "detection", "mitigation"]:
    amount = learnable_knowledge[dimension]
             × (0.5 + 0.5 × susceptibility)
             × (0.5 + 0.5 × documentation_quality)
```

For prevention:
```
= 0.18 × (0.5 + 0.5 × 0.4) × (0.5 + 0.5 × 0.5)
= 0.18 × 0.70               × 0.75
= 0.095
```

For detection: `= 0.21 × 0.70 × 0.75 = 0.110`

For mitigation: `= 0.14 × 0.70 × 0.75 = 0.074`

Team B would receive approximately 53% of what Team A gained from direct experience.
The discount reflects low subsystem susceptibility (0.70 multiplier) and average
documentation quality (0.75 multiplier): `0.70 × 0.75 = 0.525`.

**Learning cost charged on successful exploitation:**

```python
metrics["cumulative_learning_cost"] += learning_cost    # += 2.0 hours
```

**`learning_cost = 2.0 hours`** — each successful exploitation event costs 2 engineer-hours.
This represents the total labor of careful postmortem reading, team discussion, runbook
update, and implementation of the defensive change. This is the investment side of the
knowledge-sharing equation. The return is a reduced future incident rate.

**Economic interpretation:** At year end, the net organizational cost under each scenario is:

```
net_cost = cumulative_engineering_cost + cumulative_learning_cost
```

Under NONE: high incident costs, zero learning costs.
Under GLOBAL: lower incident costs, non-trivial learning costs.

The thesis finding is that even after paying learning costs, broader sharing strategies
produce lower net costs — the investment has positive ROI.

---

## PHASE 3 — Daily Metric Recording

At the end of each day, the simulation appends one value to every time-series array and
updates all running totals. After 365 days, each time-series array contains exactly
365 values.

**All cost and frequency metrics aggregate across the entire organization.** The
simulation sums contributions from all teams and all incidents that occurred during the
day before recording. A day with incidents at multiple teams contributes the combined
cost of all those incidents.

---

### Metric 1 — Incident Frequency

```python
metrics["incident_frequency"]["DATABASE"].append(1)
metrics["incident_frequency"]["PAYMENT"].append(0)
```

**What is recorded:** The count of incidents per subsystem on this day (0, 1, or
occasionally more if multiple incidents fire for the same subsystem in one day).

**Real-world meaning:** Whether a given subsystem experienced a production failure on
this business day. Over 365 days, this array becomes the incident timeline — the raw
record from which total incident counts and trend analysis are derived.

**Role in the thesis:** Summing each subsystem's array gives total incidents per subsystem
for the year. Plotting the array over time shows whether incidents become less frequent
in the second half of the year as knowledge accumulates, which is the visual evidence
of learning.

---

### Metric 2 — Engineering Cost

**How the daily cost is computed from all teams:**

```python
timestep_costs = []    # initialized empty at the start of each day

# During Phase 1, every time any team experiences an incident:
timestep_costs.append(incident.engineering_cost)

# At end of day (Phase 3):
metrics["engineering_cost"].append(sum(timestep_costs))
metrics["cumulative_engineering_cost"] += sum(timestep_costs)
```

**Example with two incidents on the same day:**

If Team A experienced a DATABASE_TIMEOUT (cost = 4.69 hours) and Team B experienced
a CONFIG_ERROR (cost = 3.20 hours) on the same day:

```python
timestep_costs = [4.69, 3.20]

metrics["engineering_cost"].append(7.89)           # org-wide cost today
metrics["cumulative_engineering_cost"] += 7.89     # running year total
```

**Day 1 (one incident only):**

```python
timestep_costs = [4.69]
metrics["engineering_cost"].append(4.69)
metrics["cumulative_engineering_cost"] += 4.69     # running total = 4.69
```

**`metrics["engineering_cost"]`** — a 365-element array. Each value is the total
engineering labor cost in hours across all teams for that specific day. Days without
incidents record 0.0. This array is used to plot engineering cost over time and
observe whether it trends downward as learning accumulates.

**`metrics["cumulative_engineering_cost"]`** — a single scalar that accumulates all
daily totals across the full year. At year end, this number represents the total
organizational engineering labor cost of all production incidents. It is one of the
two primary outcome variables used in the thesis comparison table.

**Why this matters for H1:** The cumulative engineering cost comparison directly answers
the economic question — not just "did fewer incidents happen?" but "how much human time
did the organization save by adopting a broader sharing strategy?"

```
NONE scenario:   ~9,800 engineer-hours per year
GLOBAL scenario: ~7,400 engineer-hours per year
Reduction:       ~2,400 hours saved = 24% reduction in incident labor cost
```

---

### Metric 3 — Learning Cost

```python
# Recorded inside Phase 2 whenever a team successfully completes exploitation:
metrics["cumulative_learning_cost"] += 2.0    # learning_cost = 2.0 hours
```

**`metrics["cumulative_learning_cost"]`** — a running total of all engineer-hours the
organization invested in knowledge sharing activities across the year. It increments
by 2.0 each time any team successfully exploits an incident.

**Real-world meaning:** Time spent reading postmortems in depth, conducting cross-team
incident reviews, updating runbooks based on other teams' incidents, and implementing
defensive changes motivated by secondhand incident knowledge. This is overhead that
organizations incur when they invest in systematic knowledge sharing.

**Relationship to engineering cost:** The two together define total organizational cost:

```
net_cost = cumulative_engineering_cost + cumulative_learning_cost

NONE:    high incident cost + zero learning investment = high total
GLOBAL:  lower incident cost + non-trivial learning cost = lower total
```

The simulation demonstrates that the learning investment under GLOBAL yields a net
reduction in total organizational cost — the ROI on knowledge sharing is positive.

---

### Metric 4 — Incident Duration and Severity

```python
if timestep_durations:      # at least one incident occurred today
    metrics["incident_duration"].append(mean(timestep_durations))
    metrics["incident_severity"].append(mean(timestep_severities))
else:
    metrics["incident_duration"].append(0.0)
    metrics["incident_severity"].append(0.0)
```

**What is recorded:** On days with incidents, the mean duration (hours) and mean
severity (1–5 scale) across all incidents that day. On quiet days, 0.0 is recorded.

**Real-world meaning:**

- `incident_duration` — how long the organization was actively managing a production
  failure, from onset through full resolution. As mitigation and detection knowledge
  accumulate, incidents that do occur are resolved faster and detected sooner,
  producing a downward trend in this metric over the year.

- `incident_severity` — how disruptive the incidents were on the 1–5 scale. As
  mitigation knowledge accumulates, the severity of incidents trends downward because
  teams respond more effectively, limiting blast radius and duration of impact.

---

### Metric 5 — Average Knowledge Level (Org-Wide)

```python
prevention_values = []
for team in all_teams:
    for incident_type in IncidentType:
        prevention_values.append(team.knowledge[incident_type]["prevention"])

# 2 teams × 5 incident types = 10 values
avg_prevention = mean(prevention_values)
               = mean([0.18, 0.0, 0.0, 0.0, 0.0,    # Team A
                        0.0, 0.0, 0.0, 0.0, 0.0])   # Team B
               = 0.018

metrics["avg_prevention_knowledge"].append(0.018)
```

The same process is applied to detection and mitigation knowledge.

**What is recorded:** The mean knowledge value across every team, every incident type,
and the specified knowledge dimension — a single number summarizing the organization's
collective competence on that day.

**Real-world meaning:** A value of 0.018 on Day 1 indicates that the organization is
nearly at baseline — only one team has learned anything and only in one incident type.
By Day 365 under GLOBAL scenario, this value may reach 0.40–0.50, representing
substantial collective organizational learning. This rising curve is the direct
visualization of the thesis's core mechanism.

**Why aggregate across all teams and incident types:** The thesis question concerns
organizational learning as a whole. Averaging across all teams captures whether the
entire organization is becoming more competent, not just the team that experienced
the most incidents.

---

### Metric 6 — Pipeline Stage Rates

```python
total_possible = len(timestep_incidents) × (num_teams - 1)
# The source team is excluded because it already learned directly.
# total_possible represents all (non-source team, incident) learning opportunities today.

acquired_count    = count of non-source teams that acquired today
assimilated_count = count of non-source teams that assimilated today
transformed_count = count of non-source teams that transformed today
exploited_count   = count of non-source teams that exploited today

metrics["acquisition_rate"].append(acquired_count    / total_possible)
metrics["assimilation_rate"].append(assimilated_count / total_possible)
metrics["transformation_rate"].append(transformed_count / total_possible)
metrics["exploitation_rate"].append(exploited_count   / total_possible)
```

**Day 1 values:**

```
total_possible = 1 incident × (2 teams - 1) = 1

acquired:    1 → rate = 1.00    (Team B acquired)
assimilated: 1 → rate = 1.00    (Team B assimilated)
transformed: 0 → rate = 0.00    (Team B failed transformation)
exploited:   0 → rate = 0.00    (stage not reached)
```

**Real-world meaning:** On any given day, what fraction of possible cross-team learning
opportunities actually completed each stage? A transformation rate of 0.20 means that
20% of all eligible team-incident pairs successfully transformed knowledge on that day.

**Role in the thesis:** These four rates are the quantitative evidence that the Zahra &
George (2002) four-stage pipeline model is functioning as designed. The expected pattern
is a funnel that narrows at each stage:

```
acquisition_rate > assimilation_rate > transformation_rate > exploitation_rate
```

Plotting these rates over 365 days shows how the learning pipeline performs across the
organization throughout the year and reveals which stage is the primary bottleneck.

---

### Metric 7 — MTBF, MTTR, and MTTD

```python
# MTBF — running average of days between incidents, per subsystem
for subsystem in all_subsystems:
    if mtbf_samples[subsystem]:
        current_mtbf[subsystem] = mean(mtbf_samples[subsystem])
    else:
        current_mtbf[subsystem] = 365    # no failures yet: assume full year
metrics["mtbf"].append(current_mtbf)

# MTTR — running average of all incident durations recorded so far
metrics["mttr"].append(mean(mttr_samples))    # Day 1: mean([2.07]) = 2.07

# MTTD — running average of all detection times recorded so far
metrics["mttd"].append(mean(mttd_samples))    # Day 1: mean([0.72]) = 0.72
```

**MTBF (Mean Time Between Failures)** — measured in days.

The average number of days between consecutive incidents for a given subsystem. Calculated
as the mean of all recorded inter-incident gaps. As prevention knowledge accumulates,
incidents occur less frequently, gaps grow longer, and MTBF increases. Higher MTBF
indicates greater system reliability.

**MTTR (Mean Time To Recovery)** — measured in hours.

The average total duration of incidents from onset through full resolution. Calculated
as the running mean of all `incident.duration` values recorded so far. As mitigation
and detection knowledge accumulate, resolution becomes faster and MTTR decreases.
Lower MTTR means the organization recovers from failures more quickly.

**MTTD (Mean Time To Detect)** — measured in hours.

The average time between when an incident begins and when the team first becomes aware
of it. Calculated as the running mean of all `incident.detection_time` values. As
detection knowledge accumulates (better alerts, improved dashboards, diagnostic runbooks),
MTTD decreases. Lower MTTD means problems are noticed sooner, limiting the window of
user impact before response begins.

**Why all three are tracked separately:**

Each metric responds to a different knowledge dimension:

```
prevention knowledge → MTBF increases  (incidents occur less frequently)
detection knowledge  → MTTD decreases  (problems noticed sooner)
mitigation knowledge → MTTR decreases  (incidents resolved faster)
```

An organization that invests exclusively in monitoring improvements will see MTTD improve
but MTBF and MTTR remain stable. An organization that runs thorough postmortems and
implements preventive fixes will see MTBF improve. Tracking all three separately allows
attribution of reliability improvement to specific knowledge dimensions.

**Final availability calculation (computed at end of simulation):**

```
availability = MTBF / (MTBF + MTTR)
```

Converts MTBF and MTTR into a single uptime percentage. With `MTBF = 10 days` and
`MTTR = 2.07 hours = 0.086 days`:

```
availability = 10 / (10 + 0.086) = 0.991 = 99.1% uptime
```

---

### Complete Metric State After Day 1

After all three phases complete on Day 1, every metric container holds its first value:

```
metrics["incident_frequency"]["DATABASE"]  = [1]       ← 1 incident today
metrics["incident_frequency"]["PAYMENT"]   = [0]       ← 0 incidents today

metrics["incident_duration"]               = [2.07]    ← 2 hrs 4 min total duration
metrics["incident_severity"]               = [3.4]     ← moderate severity
metrics["engineering_cost"]                = [4.69]    ← 4.69 hrs org-wide today
metrics["cumulative_engineering_cost"]     = 4.69      ← year running total

metrics["cumulative_learning_cost"]        = 0.0       ← no exploitation occurred

metrics["avg_prevention_knowledge"]        = [0.018]   ← near baseline
metrics["avg_detection_knowledge"]         = [0.021]
metrics["avg_mitigation_knowledge"]        = [0.014]

metrics["acquisition_rate"]               = [1.00]    ← Team B acquired
metrics["assimilation_rate"]              = [1.00]    ← Team B assimilated
metrics["transformation_rate"]            = [0.00]    ← Team B failed
metrics["exploitation_rate"]              = [0.00]    ← not reached

metrics["mtbf"]   = [{DATABASE: 365, PAYMENT: 365}]  ← no gaps recorded yet
metrics["mttr"]   = [2.07]
metrics["mttd"]   = [0.72]
```

---

## DAYS 2–365 — The Remaining Simulation

The identical sequence — Pre-Phase A through Phase 3 — executes for each of the remaining
364 days. Each day, the following dynamics compound:

```
Teams learn → knowledge cells increase → avg_prevention rises
    ↓
Higher avg_prevention → lower prevention_modifier → lower p_incident
    ↓
Fewer incidents per day → longer gaps between incidents → MTBF increases
    ↓
When incidents do occur → higher mitigation and detection knowledge
    → shorter duration → MTTR and MTTD decrease
```

Knowledge decay counteracts accumulation daily, preventing any team from reaching
complete immunity and ensuring the simulation represents a dynamic equilibrium rather
than a one-directional trajectory toward zero incidents.

---

## FINAL OUTPUT — End of Day 365

After the simulation loop completes, a final computation pass generates summary statistics.

### Final Availability

```python
for subsystem in all_subsystems:
    mtbf = mean(mtbf_samples[subsystem])
    mttr = mean([inc.duration for inc in all_incidents if inc.subsystem == subsystem])
    availability[subsystem] = mtbf / (mtbf + mttr)

overall_availability = mean(availability.values())
```

### Final Results Structure

```python
results = {
    "summary": {
        "total_incidents":        490,       ← count of all incidents all year (all teams)
        "total_engineering_cost": 9,800,     ← total engineer-hours on incidents (all teams)
        "total_learning_cost":    184,        ← total engineer-hours on learning (all teams)
        "final_availability": {
            "DATABASE": 0.991,
            "PAYMENT":  0.987,
            # ... all subsystems
        },
        "overall_availability":   0.989,     ← mean across all subsystems
        "final_mttr":             1.94,      ← mean incident duration for the year (hours)
        "final_mttd":             0.69,      ← mean detection time for the year (hours)
    },

    "time_series": {
        # 365-element arrays for plotting
        "avg_prevention_knowledge": [0.018, 0.018, 0.020, ...],
        "incident_frequency": {
            "DATABASE": [1, 0, 0, 1, 0, ...],
            "PAYMENT":  [0, 1, 0, 0, 1, ...],
        },
        "engineering_cost":     [4.69, 0.0, 0.0, 3.8, ...],
        "acquisition_rate":     [1.00, 0.0, 0.40, ...],
        "transformation_rate":  [0.00, 0.0, 0.20, ...],
        # ... all other time series
    },

    "final_knowledge": {
        0: {                           # Team A's complete state at end of year
            "subsystem": "DATABASE",
            "knowledge": {
                "DATABASE_TIMEOUT":   {"prevention": 0.71, "detection": 0.68, "mitigation": 0.54},
                "CONFIG_ERROR":       {"prevention": 0.22, "detection": 0.19, "mitigation": 0.16},
                "DEPENDENCY_FAILURE": {"prevention": 0.08, "detection": 0.06, "mitigation": 0.05},
                "CAPACITY_ISSUE":     {"prevention": 0.41, "detection": 0.38, "mitigation": 0.29},
                "DEPLOYMENT_PROBLEM": {"prevention": 0.14, "detection": 0.12, "mitigation": 0.09},
            },
            "incidents_experienced": 18,    ← Team A was the source of 18 incidents this year
            "incidents_acquired":    43,    ← Team A received postmortems from 43 incidents
            "incidents_assimilated": 31,    ← Team A understood the root cause of 31
            "incidents_transformed": 19,    ← Team A connected 19 to their own system
            "incidents_exploited":   12,    ← Team A implemented changes from 12
        },
        1: {                           # Team B's complete state — independent from Team A
            "subsystem": "PAYMENT",
            "knowledge": { ... },
            ...
        }
    }
}
```

**Reading the final knowledge grid:** DATABASE_TIMEOUT holds the highest values (0.71
prevention) because Team A is a DATABASE subsystem and experiences database timeouts
most frequently. DEPENDENCY_FAILURE holds the lowest values (0.08) because database
teams rarely encounter dependency failures as the primary incident type. The grid
reflects one full year of Team A's actual incident history.

**Reading the pipeline funnel:**

```
43 received  →  31 understood  →  19 applied  →  12 implemented
100%             72%               61%              63%

End-to-end: 12 / 43 = 28% conversion rate from postmortem received to change implemented
```

28% of all incidents Team A received information about resulted in an implemented system
change. The remaining 72% leaked out at one of the four pipeline stages. This funnel
is the quantitative representation of Zahra & George (2002) absorptive capacity —
each stage is a gate, and the cascade of partial failures is the expected pattern in
real organizational learning.

---

## The Primary Thesis Outcome Variable

After 365 days, each simulation run produces one number:

```python
results["summary"]["total_incidents"]
```

This process is repeated 100 times with different random seeds. The 100 values are
aggregated into a mean and 95% confidence interval:

```
95% CI = mean ± 1.96 × (standard_deviation / sqrt(100))
```

This produces four data points, one per learning scenario:

```
NONE scenario:     mean = 490  [95% CI: 478 – 502]
LOCAL scenario:    mean = 419  [95% CI: 409 – 429]
NEIGHBOR scenario: mean = 406  [95% CI: 396 – 416]
GLOBAL scenario:   mean = 372  [95% CI: 363 – 381]
```

The H1 hypothesis is confirmed when the confidence intervals do not overlap and the
ordering GLOBAL < NEIGHBOR < LOCAL < NONE holds consistently across all 100 seeds.

Every element of the simulation described in this document — the susceptibility table,
the network topology, the three incident probability modifiers, the learnable knowledge
assignment, the four-stage pipeline with its cognitive distance and relevance calculations,
the knowledge decay, and the metric collection — contributes to producing this one outcome
number per run, which is then compared across the four scenarios to answer the central
thesis question.

---

## Citation Reference

| Mechanism | Source |
|---|---|
| Team-to-system mapping | Conway (1968) — Conway's Law |
| Incident type taxonomy | Dogga et al. (2023) — ARTS classification |
| Four-stage absorptive capacity model | Zahra & George (2002) |
| Prior knowledge required for absorption | Cohen & Levinthal (1990) |
| Inverted-U cognitive distance function | Nooteboom et al. (2007) |
| Knowledge decay half-life (~2 years) | Darr et al. (1995) |
| Deployment frequency and change failure rate | Forsgren et al. (2018) — *Accelerate* |
| Incident rate and MTTR baselines | Lunney & Lueder (2016) — *Site Reliability Engineering* |
| Signal attenuation over transmission distance | Shannon & Weaver (1949) |
| Lesson dissemination failure in organizations | Drupsteen & Guldenmund (2014) |
| Knowing-doing gap | Pfeffer & Sutton (2000) |
| Small-world network topology | Watts & Strogatz (1998) |
| Simulation validation framework | Sargent (2020) |
