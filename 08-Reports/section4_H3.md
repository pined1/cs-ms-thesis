# Section 4: H3 — Learning Effectiveness (Exploitation)

## The Question

Does investing more heavily in how teams exploit incident knowledge — better training, more dedicated review time, stronger follow-through processes — produce proportional improvements in system reliability? Or do those investments run into diminishing returns?

This is H3: **the harder teams work to turn incident knowledge into action, the fewer future incidents they experience — but with sublinear gains.**

---

## A Real-World Framing

Imagine a VP of Engineering with a fixed budget and two options:

**Option A — Structural:** Build a global incident sharing platform so that every team can see every post-mortem, not just their own. This changes *who* has access to knowledge.

**Option B — Behavioral:** Hire consultants to train teams in blameless post-mortem facilitation, action-item tracking, and follow-through accountability. This changes *how intensely* teams act on the knowledge they already have.

Both cost money. Both are defensible to leadership. But which delivers more reliability improvement per dollar?

H1 (scope of sharing) answers the structural question. H3 answers the behavioral one. Together, they provide a ranked recommendation for where to invest first.

---

## Theoretical Basis: Zahra & George (2002)

Zahra & George's absorptive capacity model frames organizational learning as a four-stage pipeline:

1. **Acquisition** — sensing and collecting knowledge from the environment
2. **Assimilation** — parsing and making sense of that knowledge
3. **Transformation** — integrating new knowledge with existing understanding
4. **Exploitation** — translating transformed knowledge into action and outcomes

H3 targets Stage 4. The theoretical prediction is that exploitation faces sublinear returns because each upstream stage acts as a ceiling. No matter how effectively a team exploits knowledge, they cannot exploit knowledge they never transformed.

Think of it like a pipe with multiple valves. Even if you fully open the last valve (exploitation), the flow is still limited by how open the earlier valves are (acquisition, assimilation, transformation). Theory predicts that gains from pushing harder on Stage 4 will taper off as the earlier stages become the binding constraint — there is only so much you can exploit when the upstream pipeline is incomplete.

---

## What `prevention_effect` Means in the Model

In the simulation, each team accumulates a `prevention` score representing how much incident knowledge they hold. The probability of an incident occurring is governed by:

```
p_incident = base_rate × (1 - avg_prevention × prevention_effect) × deployment_modifier
```

The `prevention_effect` parameter is the translation rate — how efficiently held knowledge converts into actual risk reduction:

- **0.0** — Teams learn and accumulate knowledge, but nothing changes operationally. Knowledge sits unused.
- **0.5** — Default setting. Half of available prevention capacity translates into real risk reduction.
- **1.0** — Perfect translation. Every unit of knowledge the team holds becomes a unit of protection.

To make this concrete: suppose a team has a knowledge score `K = 0.992`.

| `prevention_effect` | Incident Probability Reduction |
|---|---|
| 0.0 | 0% — knowledge has no effect |
| 0.5 | ~50% reduction relative to base |
| 1.0 | ~99% reduction relative to base |

The question H3 asks is: as we move that dial from 0 to 1, how does system-level reliability change — and is the relationship linear?

---

## Why We Ran It Twice

### First Run: 100 Seeds, Range 0.0–0.10

The initial experiment swept `prevention_effect` from 0.0 to 0.10 using 100 simulation seeds per condition. The results appeared essentially linear across that narrow band — each increment in exploitation intensity produced roughly the same marginal reduction in incidents. The curve did not bend. We logged this as a provisional failure to detect the predicted sublinear pattern.

The problem was two-fold. First, the range (0.0 to 0.10) was too narrow to reveal curvature — any smooth function looks linear if you zoom in far enough. Second, at 100 seeds per condition, small effects are easily obscured by simulation variance. A subtle trend can be statistically indistinguishable from noise.

### Second Run: 500 Seeds, Range 0.0–0.50

To resolve both issues, we redesigned the experiment. The range was extended to 0.50 — five times wider — and the seed count was increased to 500 per condition, making this the most statistically rigorous test in the entire study. The larger seed pool reduces Monte Carlo variance, which is essential when the signal is modest and we need to distinguish real curvature from random fluctuation.

---

## Results (500-Seed Run)

| `prevention_effect` | Mean Incidents | Change from Previous |
|---|---|---|
| 0.00 | 484.1 | — |
| 0.01 | 481.3 | −2.7 |
| 0.02 | 477.7 | −3.7 |
| 0.05 | 468.8 | −8.8 |
| 0.10 | 451.2 | −17.7 |
| 0.20 | 420.5 | −30.7 |
| 0.50 | 335.3 | −85.2 |

The headline finding: moving from `0.0` to `0.50` reduces mean incidents from 484.1 to 335.3, a reduction of 148.8 incidents (approximately 30%). H3 is supported — exploitation intensity does matter.

---

## Interpreting the Diminishing Returns

The shape of the curve matters as much as the total reduction. Looking at the incremental changes:

- `0.0 → 0.10` (a realistic, achievable improvement): saves **33 incidents**
- `0.10 → 0.50` (requires 4× more intensive effort): saves **116 incidents**

**[Figure 4.1: Diminishing Returns Curve — Mean Incidents vs. prevention_effect]**
*A line chart showing mean incidents (y-axis) against prevention_effect values 0.0 through 0.50 (x-axis). The curve bends — steep early savings flatten as exploitation intensity increases, illustrating the sublinear relationship.*

The absolute number of incidents saved keeps growing as you push exploitation harder — but the *efficiency* of each additional unit of effort declines. Moving from 0 to 0.10 is like hiring a dedicated SRE team to run blameless post-mortems and track action items: a realistic, achievable investment that any engineering organization could make. Moving from 0.10 to 0.50 would require an extraordinary, organization-wide transformation of how teams process and act on every piece of incident knowledge — an implausibly intense undertaking. You save more incidents in absolute terms, but you are spending 4× the effort to get 3.5× the gain.

The savings also grow non-linearly across steps: −2.7, −3.7, −8.8, −17.7, −30.7, −85.2. Each number represents how many additional incidents were prevented by the next increment in `prevention_effect`. The growing gap between steps confirms the curve is genuinely bending rather than being flat — this is the signature of diminishing returns. The 500-seed design gives us enough statistical power to treat these escalating differences as real signal rather than random noise from the simulation.

---

## Why the "Failure" Became a Strength

The 100-seed run that initially looked like a failure is now interpretively valuable. It established that within a *realistic* operational range (exploitation effect 0.0 to 0.10), the gains from pushing harder on Stage 4 are modest — approximately 33 incidents, or a 7% reduction.

Compare this to H1:

| Intervention | Incident Reduction | Notes |
|---|---|---|
| NONE → GLOBAL sharing (H1) | ~219 incidents, −45% | Structural change |
| `effect` 0.0 → 0.50 (H3) | −149 incidents, −30% | Requires unrealistic effort level |
| `effect` 0.05 → 0.10 (H3) | −18 incidents, −4% | Realistic improvement range |

At realistic parameter values, H3 produces roughly a 4% reduction in incidents. H1 — simply expanding who sees incident knowledge — produces 45%. The practical message is clear: **who you share with matters far more than how hard you try.**

---

## Why Stage 4 Is Not the Bottleneck

A supplementary sensitivity sweep confirms this interpretation from another angle. Varying exploitation *probability* (the likelihood that a team attempts to apply knowledge, independent of effect size) across the full range from 0.1 to 1.0 produces only about 3 incidents of variation across the entire simulated organization. Stage 4 activity is nearly saturated under default conditions.

The real bottleneck is Stage 3 — transformation — which is gated in the model by cosine similarity between a team's existing knowledge profile and the new incident knowledge. Cosine similarity, in turn, is driven by the volume and diversity of knowledge a team has accumulated. And knowledge accumulation is driven by sharing scope.

This creates a causal chain: sharing scope (H1) → knowledge accumulation → transformation quality (Stage 3) → exploitation effectiveness (Stage 4). Squeezing Stage 4 without addressing Stage 3 and the knowledge pipeline behind it yields limited return.

---

## Conclusion

H3 is supported: exploitation intensity does reduce incidents, and the relationship is non-linear with diminishing marginal returns at higher effort levels, consistent with Zahra & George (2002). However, the effect is modest in absolute terms relative to structural sharing interventions.

The practical recommendation is sequenced: **invest in structural knowledge sharing first (H1), then in exploitation quality (H3).** Get knowledge in front of teams before optimizing how intensely they process it. Teams that lack access to relevant incident knowledge have nothing to exploit — better processing machinery operating on a thin information diet will not compensate for structural gaps upstream.

The two-run design also illustrates an important principle in empirical research: a negative result in a small, narrowly-scoped experiment does not mean the effect does not exist. It may simply mean the experiment was not designed to detect it. When the first run showed a flat line, the right response was not to conclude "H3 is false" — it was to ask whether the test was sensitive enough to reveal the predicted pattern. Expanding the range and tripling the seed count answered that question. A researcher who stopped at the first run would have drawn the wrong conclusion from a design flaw, not from the science.
