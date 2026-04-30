# Section 5: H4 — Network Topology and the Spread of Incident Knowledge

## 5.1 The Question

Does the shape of how teams are connected affect how well incident knowledge spreads? When a team experiences a failure and learns something from it, who else learns? The answer, it turns out, depends almost entirely on the topology of the organizational network — the pattern of connections between teams. H4 investigates whether network structure affects incident knowledge spread—and thus whether it is a meaningful lever for organizational reliability.

The hypothesis: **evenly distributed connectivity will outperform centralized hub-spoke arrangements in total incidents prevented.**

---

## 5.2 Why Topology Matters: Signal Decay

Knowledge in this model does not travel losslessly. Every time incident information passes through an intermediary team — every hop in the network — the probability of the receiving team successfully acquiring that knowledge degrades. The acquisition probability formula is:

```
p_acquire = acquisition_prob × signal_decay ^ path_length
```

With `signal_decay = 0.8` and `acquisition_prob = 0.9`, the math is unforgiving:

| Path Length | Calculation | Acquisition Probability |
|-------------|-------------|------------------------|
| 1 hop (direct neighbor) | 0.9 × 0.8¹ | 0.720 |
| 2 hops | 0.9 × 0.8² | 0.576 |
| 3 hops | 0.9 × 0.8³ | 0.461 |

The practical implication: **denser networks produce shorter average path lengths, which produce less decay, which produce more learning.** A team that is three hops from the source of an incident is 36% less likely to learn from it than a team that is one hop away. Structure shapes outcomes before a single agent makes a decision.

---

## 5.3 Why the NEIGHBOR Scenario

Three knowledge-sharing scenarios were evaluated across experiments: LOCAL (only the directly affected team learns), GLOBAL (all teams learn regardless of distance), and NEIGHBOR (teams learn from their immediate network neighbors).

Topology only becomes the primary variable under NEIGHBOR conditions:

- **LOCAL**: The source team learns from its own incident. Network structure is irrelevant — no information travels at all.
- **GLOBAL**: All teams learn from every incident. Network structure is again irrelevant — information reaches everyone regardless of connections.
- **NEIGHBOR**: A team's neighborhood IS defined by its network connections. Who you're connected to determines who you learn from and who learns from you. Topology is the mechanism.

NEIGHBOR is also the most realistic condition for a 20-team software organization. Knowledge rarely stays entirely local; it rarely broadcasts organization-wide. Engineers share post-mortems in Slack channels their adjacent teams follow. Senior engineers carry lessons when they rotate between squads. The neighbor relationship is the plausible unit of knowledge diffusion.

---

## 5.4 The Five Network Topologies

### 5.4.1 Complete Graph — 273 Incidents

```
    [A]---[B]---[C]
     | \ / | \ / |
     |  X  |  X  |
     | / \ | / \ |
    [D]---[E]---[F]
      (every node connects to every other node)
```

**What it is:** Every team is directly connected to every other team. With 20 teams, this means 190 unique connections.

**Real-world analog:** A tiny startup where everyone attends every meeting, there are no silos, and any engineer can walk to any other engineer's desk. Zero organizational distance.

**Why test it:** The theoretical ceiling. This is the best connectivity that any organization can achieve, and it establishes the upper bound for knowledge diffusion.

**Why it produces 273 incidents:** Every team is exactly one hop from the source of every incident. Signal decay applies at its minimum (0.8¹ = 0.80). Knowledge reaches the maximum number of teams at the highest possible fidelity.

---

### 5.4.2 Erdős-Rényi Random Graph — 323 Incidents

```
    [A]---[B]   [C]
     |         / |
    [D]---[E]-[F] |
               \  |
               [G]-[H]
      (connections formed with 30% probability)
```

**What it is:** Each of the 190 possible team pairs is connected with probability `p = 0.3`. The resulting graph is random — no structural principle governs who knows whom. Like the Complete graph, this uses the same 20 teams; only the connection pattern varies with p = 0.3 across the 100 seeds.

**Real-world analog:** Relationships that formed by chance. The engineers who happened to sit together at the company offsite. The two teams that were accidentally merged for a quarter and stayed in touch. No deliberate org design — just accumulated coincidence.

**Why test it:** The null model. If network structure does not matter, a random graph should produce results statistically indistinguishable from deliberate designs. It does not.

**Why it produces 323 incidents:** At `p = 0.3`, the expected number of connections per team is approximately 5.7 (versus Watts-Strogatz's fixed 4). The random graph is simply denser at these parameters. This finding is important: ER outperforms WS not because randomness is superior to structure, but because *density wins*. The lesson is not that random organizations are effective; it is that connection count matters independently of topology pattern.

---

### 5.4.3 Watts-Strogatz Small-World — 336 Incidents (Baseline)

```
    [1]-[2]-[3]-[4]-[5]
     |               |
    [20]  ring with  [6]
     |   shortcuts   |
    [19]            [7]
         ...
      (ring + 10% rewired shortcuts)
```

**What it is:** Teams are arranged in a conceptual ring, each connected to its 4 nearest neighbors. Then, 10% of connections are randomly rewired to create long-range shortcuts — the "small world" property.

**Real-world analog:** A 20-team software company with a squad structure. The backend squad knows the teams closest to them in the product stack. A few informal cross-team relationships exist — the engineer who used to be on another team, the tech lead who has mentored people in three different squads. These shortcuts dramatically reduce average path length without requiring full connectivity.

**Why test it:** This is the most realistic topology for a mid-sized software organization, which is why it serves as the baseline for H1, H2, and H3. Results from this section are most directly comparable to real organizational design choices.

**Why it produces 336 incidents:** With 4 connections per team and moderate path lengths, diffusion is reliable but not maximal. The shortcuts prevent total isolation of any team, but the lower average degree (versus ER) limits how many teams are reached per incident. K = 0.890 indicates strong but incomplete organizational learning.

---

### 5.4.4 Barabási-Albert Hub-Spoke — 346 Incidents

```
           [Hub-1]
          / | | \ \
        [A][B][C][D][E]
         |
       [Hub-2]
       /  |  \
     [F] [G] [H]
      (new nodes attach preferentially to well-connected nodes)
```

**What it is:** Teams join the network one at a time, each connecting to `ba_m = 2` existing teams with probability proportional to those teams' existing degree (the "rich get richer" mechanism). The result is 2-3 hub teams with 10-12 connections each, and 12-14 peripheral teams with only 2-3 connections.

**Real-world analog:** The platform team or SRE function that every product team depends on. All product teams have a relationship with platform; product teams have few relationships with each other.

**Why peripheral teams hurt performance:** In a 20-team organization, the majority of incidents occur at peripheral teams (by definition, since they are the majority). Each incident at a peripheral team reaches only that team's 2 neighbors — a fraction of WS's 4. Knowledge accumulates at hubs, which are incident-prone themselves and learn well, but it cannot efficiently diffuse outward to the spoke majority. The hub is a knowledge repository; the spokes remain underinformed.

**The ba_m crossover:** A parameter sweep reveals a crossover at `ba_m = 3`. Below this value, BA performs worse than WS — hubs are insufficiently dense to compensate for peripheral isolation. Above `ba_m = 3`, BA begins to outperform WS as hubs accumulate enough connections to function as genuine accelerators. At `ba_m = 2`, the default tested here, BA is net-negative relative to equitable distribution.

**Scale-free caveat:** Statistical verification of a true power-law degree distribution requires substantially more than 20 nodes. The hub-spoke behavior is empirically observable and the measured performance differences are real, but any claim that this is a canonical "scale-free" network should be treated as informal at this scale. Future work with 50+ team organizations would permit formal verification.

---

### 5.4.5 Star — 382 Incidents (Worst)

```
         [Hub]
        / | | \
      [A][B][C][D]...[S]
      (all 19 spokes connect only to hub)
```

**What it is:** One team serves as the central hub. All 19 other teams connect exclusively to the hub. No spoke connects to any other spoke.

**Real-world analog:** Extreme centralization. Every incident debrief goes through the SRE lead. Every post-mortem is written by the CTO. No peer-to-peer incident sharing exists — knowledge must travel up and back down through a single person or team.

**Why it produces 382 incidents:** Approximately 95% of incidents occur at spoke teams. When a spoke team experiences a failure, its neighborhood consists of the hub and zero other spokes. The hub learns. No other spoke learns. Then the hub team — now slightly more knowledgeable — continues to watch 19 relatively uninformed teams make the same errors. Knowledge concentrates at the center and never diffuses to where incidents predominantly occur. K = 0.670, the lowest of any topology tested, reflects an organization where the lessons of failures are systematically trapped rather than distributed.

---

## 5.5 Results Summary

| Topology | Total Incidents | Prevention K | Real-World Analog |
|---|---|---|---|
| Complete Graph | 273 | 0.990 | Tiny startup, no silos |
| Erdős-Rényi Random | 323 | 0.916 | Organic, chance-based relationships |
| Watts-Strogatz Small-World | 336 | 0.890 | Squad structure with informal ties |
| Barabási-Albert Hub-Spoke | 347 | 0.835 | Platform team as central node |
| Star | 382 | 0.670 | Everything through one person |

The range spans approximately 109 incidents — from 273 (Complete) to 382 (Star). Topology alone accounts for a 40% difference in organizational reliability when comparing the best and worst configurations.

---

## 5.6 Does Every Team Need to Know About Every Incident?

A reasonable objection: should a frontend team really learn from a database partition failure? Should a mobile team update its knowledge based on a Kubernetes scheduling incident? The concern is that broad diffusion wastes cognitive bandwidth on irrelevant information.

The model handles this through cosine similarity filtering. Each incident has a feature vector; each team has a competency profile. The transformation probability — the likelihood that a team actually internalizes and applies what it encounters — is scaled by the cosine similarity between team and incident. A frontend team encountering a deep storage incident will have low similarity and correspondingly low transformation probability. The model effectively says "no" to irrelevant signals on the team's behalf.

More substantively: most failure patterns in software systems are not subsystem-specific at the mechanism level. Deployment sequencing errors, configuration drift, cascading dependency failures, and insufficient timeout handling recur across subsystem types. A frontend team that witnesses a database team's incident report learns that services can fail in ways that downstream consumers inherit. This builds dependency awareness and cross-subsystem pattern recognition — forms of knowledge that are directly relevant the next time the frontend team must reason about an outage it did not cause but must respond to.

Broader exposure does not require that every team become an expert in every domain. It requires that teams develop appropriate mental models of the broader system they operate within.

---

## 5.7 Conclusion

Network topology is not an implementation detail — it is a primary determinant of organizational reliability. Across the five topologies tested, the difference between the best and worst performers spans 40% of total incident volume. The key findings:

1. **Evenly distributed connectivity outperforms hub-spoke at org scale.** Complete and ER graphs, which distribute connections equitably, produce the fewest incidents. Every percentage point of average path length increase costs preventable failures.

2. **The commonly assumed advantage of scale-free networks only emerges at sufficient connection density.** Barabási-Albert hub-spoke structures underperform Watts-Strogatz at `ba_m = 2`. The crossover occurs at `ba_m = 3`. Hubs are accelerators only when they are dense enough to actually bridge the peripheral majority.

3. **Extreme centralization is the worst possible structure.** Star topology produces 40% more incidents than complete connectivity. Organizations that route all knowledge through a single team or person are not just inefficient — they are systematically preventing the diffusion that would reduce future failures.

4. **Watts-Strogatz small-world structure — the most realistic model for a 20-team software company — sits in the middle of the distribution.** It is significantly better than star, meaningfully worse than complete. This suggests that deliberate investment in cross-team connections, particularly bridging connections that reduce path lengths between distant teams, would produce measurable reliability gains.

The practical recommendation is not to make every team connect to every other team, which is operationally infeasible at scale. It is to identify which connections are currently missing that would most reduce average path length — and to treat those connections as infrastructure investments, not social niceties.
