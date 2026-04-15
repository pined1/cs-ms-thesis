# Section 3.6: Network Topologies

To examine how organizational communication structure influences incident learning, the simulation tests five distinct network topologies connecting the twenty agent teams. Each topology represents a different model of how real-world engineering organizations coordinate, share information, and propagate knowledge. Topology assignment affects which neighbors a team can observe under the NEIGHBOR learning rule and which teams a team is exposed to under diffusion-based knowledge transfer. The fifth hypothesis (H4) predicts that topology moderates incident rates; varying topology across otherwise identical simulation runs isolates this structural effect.

The **complete graph** connects every team directly to every other team, yielding maximum possible connectivity. No pair of teams is more than one hop apart, and every team has equal access to the full organization's incident history. This configuration represents a theoretically flat, fully transparent organization in which all communication channels are always open. Under the NEIGHBOR learning rule it produces the lowest mean incident count of any topology tested (298.7), confirming that information access alone reduces repeated failures when no structural bottlenecks exist.

The **Erdős-Rényi (ER) random graph** assigns edges between pairs of nodes with a fixed probability (er_p = 0.3), producing a network with no deliberate structural logic. Connectivity emerges from chance rather than organizational design, analogous to an organization whose cross-team communication patterns have developed ad hoc rather than through intentional coordination mechanisms. Mean incidents under NEIGHBOR reach 312.4, modestly worse than the complete graph, reflecting the occasional disconnected subgraphs and uneven degree distribution that random wiring introduces.

The **Watts-Strogatz (WS) small-world** topology serves as the default configuration for all non-topology experiments. Generated with ws_k = 4 nearest-neighbor connections and a rewiring probability of ws_p = 0.1, it combines high local clustering with short average path lengths — the defining signature of small-world networks (Watts & Strogatz, 1998). This pairing maps directly onto the empirical structure of engineering organizations, where tightly-knit squads or pods maintain dense intra-group communication while tech leads, architects, and platform teams provide a small number of cross-cutting ties that dramatically shorten the path between any two teams. Reagans and McEvily (2003) show that the optimal network for knowledge transfer requires both cohesion — dense local connections that build trust and shared context — and range — ties to structurally diverse knowledge pools. The WS topology satisfies both criteria simultaneously: its high clustering coefficient supplies cohesion, while its rewired long-range edges supply range. The complete graph maximizes both properties in principle but is organizationally unrealistic at twenty or more teams. The star topology, discussed below, provides neither. WS is thus the most theoretically defensible default for a simulation intended to reflect real software engineering organizations. Mean incidents under WS NEIGHBOR runs are 336.0.

The **Barabási-Albert (BA) scale-free** topology is generated via preferential attachment with ba_m = 2, producing a small number of highly connected hub nodes and a large number of low-degree peripheral nodes (Barabási & Albert, 1999). This hub-spoke structure models hierarchical organizations in which certain teams — staff engineers, platform groups, or architecture guilds — concentrate the majority of cross-team connections. Mean incidents reach 351.2. A notable crossover finding emerges across parameter sweeps: below ba_m = 3, hubs act as bottlenecks that slow knowledge propagation to peripheral teams; above ba_m = 3, the same hubs become accelerators that broadcast learned solutions broadly. This nonlinear behavior is reported in full in Section 4.5.

The **star** topology places a single hub team at the center connected to all nineteen peripheral teams, with no direct connections among peripheral teams themselves. It is the worst-performing topology in the experiment, with mean incidents of 418.6. Peripheral teams are entirely dependent on the hub for any knowledge received from outside their own experience, and they share no cohesion with one another. The star embodies extreme centralization: range is artificially bottlenecked through a single node, and cohesion among the majority of teams is structurally impossible.

Across all five topologies the range in mean incident counts under the NEIGHBOR learning rule spans 119.9 incidents — from 298.7 (complete) to 418.6 (star) — a difference that represents approximately 40% of the variance in incident rates attributable to topology alone. This finding underscores that structural choices about how teams communicate are not incidental to organizational safety outcomes; they are a primary determinant of them. Full statistical results for H4 are reported in Section 4.5.

A methodological caveat applies to the BA topology. Formal verification of a power-law degree distribution — the mathematical definition of scale-free structure — requires networks of 50 to 100 or more nodes. At twenty nodes, hub-spoke connectivity patterns are observable and organizationally meaningful, but the scale-free property cannot be statistically confirmed. This constraint is acknowledged as Limitation 2 in Section 5.4.

---

**Table 3.3: Network Topologies Tested**

| Topology | Key Property | Parameters | Mean Incidents (NEIGHBOR) |
|---|---|---|---|
| Complete | All-to-all connectivity | — | 298.7 |
| Erdős-Rényi | Random connectivity | er_p = 0.3 | 312.4 |
| Watts-Strogatz (default) | Small-world | ws_k = 4, ws_p = 0.1 | 336.0 |
| Barabási-Albert | Hub-spoke / scale-free | ba_m = 2 | 351.2 |
| Star | Extreme centralization | 1 hub, 19 leaves | 418.6 |

---

## Citation Checklist

- [ ] Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. *Nature*, 393(6684), 440–442. — WS topology definition, clustering coefficient, and path length properties
- [ ] Barabási, A.-L., & Albert, R. (1999). Emergence of scaling in random networks. *Science*, 286(5439), 509–512. — BA preferential attachment and scale-free degree distribution
- [ ] Reagans, R., & McEvily, B. (2003). Network structure and knowledge transfer: The effects of cohesion and range. *Administrative Science Quarterly*, 48(2), 240–267. — Cohesion + range as dual requirements for effective knowledge transfer; primary justification for WS as default

## Committee Watch

- **Scale-free caveat (Limitation 2):** The 20-node constraint on verifying power-law distribution is flagged here and must be addressed consistently in Section 5.4. Committee members familiar with network science may probe this; the response should acknowledge the limitation while defending the hub-spoke behavioral patterns as organizationally valid at this scale.
- **BA crossover finding (ba_m = 3 threshold):** The hub-as-bottleneck vs. hub-as-accelerator crossover is a substantive result; ensure Section 4.5 presents it with the full parameter sweep data to preempt questions about whether ba_m = 2 is cherry-picked.
- **WS default justification:** The Reagans & McEvily (2003) cohesion-range argument is the load-bearing theoretical claim here. If asked why WS was chosen as default rather than the better-performing complete graph, the answer is organizational realism: complete graphs do not exist in organizations of this size.
- **40% variance figure:** This is previewed here and must be substantiated with effect size statistics (eta-squared or similar) in Section 4.5 to satisfy quantitative rigor expectations.
