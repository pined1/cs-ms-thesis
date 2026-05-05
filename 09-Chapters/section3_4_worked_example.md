# Section 3.4: Concrete Worked Example

To make the four-stage pipeline concrete, consider a single incident traced from occurrence to exploitation in a minimal three-team network on simulation day 47. Team A owns the DATABASE subsystem, Team B owns the PAYMENT subsystem and is a direct neighbor of Team A, and Team C owns the AUTH subsystem and is a neighbor of Team B but not of Team A. The sharing condition is NEIGHBOR, meaning that postmortem documents propagate only to teams within one hop of the originating team. On day 47, a DATABASE_TIMEOUT incident occurs on Team A's subsystem.

**Stage 1 — Acquisition.** Team A is the source team. Because the incident occurs within its own subsystem, Team A learns implicitly through the failure itself and is exempt from the acquisition probability calculation; it enters the pipeline at Stage 2 automatically. Team B, a direct neighbor at path length 1, faces an acquisition probability of p\_acquire = 0.9 × 0.8^1 = 0.72. The roll succeeds, and Team B receives the postmortem. Team C sits two hops from Team A (path length 2), which would yield p\_acquire = 0.9 × 0.8^2 = 0.576 under a global sharing regime. Under NEIGHBOR, however, Team C is outside the sharing scope entirely and receives nothing, regardless of that probability. As illustrated in Figure 1.2, under NEIGHBOR sharing, Team B enters the pipeline while Team C does not.

**Stage 2 — Assimilation.** Team B now holds the postmortem and must internalize the failure mode. The base assimilation probability is p\_assimilate = 0.7. Because Team B's PAYMENT system has previously experienced connection-related failures — intermittent timeouts on database queries that its engineers traced to pool exhaustion — Team B carries relevant prior knowledge that slightly elevates this probability. Assimilation succeeds. Team B now "understands" the DATABASE_TIMEOUT failure mode: it can recognize the pattern, name its mechanism, and relate it to the architecture of its own system.

**Stage 3 — Transformation.** Understanding an incident pattern is necessary but not sufficient for organizational learning; the team must connect that pattern to a latent risk in its own context. The simulation computes the cosine similarity between Team B's current knowledge vector and the DATABASE_TIMEOUT incident feature vector. Because Team B's PAYMENT system shares architectural characteristics with Team A's DATABASE system — both use connection pooling with similar timeout configurations — the cosine similarity exceeds the transformation threshold. Transformation succeeds. Team B maps the connection pool exhaustion mechanism observed in Team A's subsystem to an equivalent vulnerability in its own query timeout configuration. The abstract incident has become an actionable local insight.

**Stage 4 — Exploitation.** With the insight transformed into a local action item, Team B faces a final execution probability: p\_exploit = 0.6. The roll succeeds. Team B updates its connection pool limits, adds a monitoring alert targeting early saturation, and logs the change in its operational runbook. Its DATABASE_TIMEOUT prevention knowledge cell increments from 0.31 to 0.44. As a direct consequence, Team B's effective incident rate for DATABASE_TIMEOUT-related failures decreases in subsequent simulation steps.

**What happens to Team C.** Under NEIGHBOR, Team C receives no postmortem on day 47. Its knowledge vector is unchanged, and it remains fully exposed to the same class of failure that just affected Team A. Under a GLOBAL sharing condition, Team C would have received the postmortem at Stage 1 with p\_acquire = 0.9 × 0.8^1 = 0.72, since GLOBAL treats all teams as effectively one hop from the source. Team C's pipeline would then proceed independently, with its own assimilation, transformation, and exploitation rolls determining whether the knowledge translated into a local fix.

**The structural implication.** This single DATABASE_TIMEOUT incident on day 47 produced one knowledge transfer event — Team B — under NEIGHBOR. Under GLOBAL, it would have produced up to 19 transfer events across the full 20-team network. Multiplied across 484 incidents over the 365-day simulation run, this structural difference in reach compounds into the 45% incident reduction observed in H1. The worked example makes the mechanism explicit: the pipeline is the same in both conditions; what changes is how many teams are allowed to enter it.

---
## Citation Checklist

(This section is illustrative rather than theoretical; citations are minimal by design.)

- No new citations required in this section.
- Figure 1.2 reference: already exists in the thesis HTML. Forward reference in Stage 1 paragraph — no citation entry needed, only a figure cross-reference.
- If a reviewer asks for a methodological citation on the cosine similarity computation, forward-reference Section 3.3 (Model Architecture), where that measure is formally defined.

---
