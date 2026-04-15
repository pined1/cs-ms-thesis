# Section 3.8: Validation Approach

Because this study relies on a synthetic simulation rather than empirical field data, establishing confidence in the model's outputs requires deliberate attention. This section describes the validation strategy employed, organized according to Sargent's (2020) widely cited framework for simulation verification and validation. Sargent distinguishes three complementary validity types: conceptual validity, which concerns whether the model accurately represents the real system; operational validity, which concerns whether the model behaves as theory predicts; and data validity, which concerns whether input parameters are grounded in empirical evidence. Each type is addressed in turn.

## Conceptual Validity

Conceptual validity is established by tracing each core model component to a peer-reviewed theoretical or empirical source. The four-stage knowledge pipeline — acquisition, assimilation, transformation, and exploitation — is a direct computational implementation of Zahra and George's (2002) absorptive capacity framework, one of the most-cited constructs in organizational learning research. The knowledge decay function follows the empirically-grounded exponential decay model documented by Darr et al. (1995), who observed this decay pattern in franchised pizza stores sharing operational knowledge across sites. The three network topologies representing how teams are connected structurally derive from foundational network science: random graphs follow Watts and Strogatz (1998), and preferential-attachment graphs follow Barabási and Albert (1999). The assumption that teams share incident knowledge without attributing blame is grounded in Edmondson's (1999) psychological safety construct and the practitioner framework articulated by Lunney and Lueder (2016). Because every major model component maps to an established citation, the conceptual structure of the simulation reflects theoretical consensus rather than arbitrary design choices.

## Operational Validity

Operational validity was assessed using pattern-oriented validation, following Grimm et al. (2020). Under this approach, observable patterns are specified in advance as validation criteria, and the model is evaluated on whether it reproduces those patterns. Three patterns were designated prior to running experiments.

Pattern 1 predicted that the GLOBAL sharing scenario would produce fewer incidents than the NONE scenario across all random seeds. This pattern was confirmed: the difference was large (Cohen's d = 11.51) and statistically significant (p < 0.001) with no overlap between seed distributions.

Pattern 2 predicted that prevention knowledge under GLOBAL sharing would saturate by approximately day 90, consistent with absorptive capacity theory's prediction that organizations approach knowledge ceilings as the available incident space becomes covered. This pattern was confirmed: mean prevention knowledge reached 0.992 by day 90.

Pattern 3 predicted that denser networks would produce lower incident rates. This pattern was confirmed, with the full ordering Complete < Erdős–Rényi < Watts–Strogatz < Barabási–Albert < Star matching theoretical expectations about information diffusion in networks of varying connectivity.

Confirmation of all three pre-specified patterns provides systematic operational validity evidence.

## Data Validity and Sensitivity Analysis

Data validity is addressed through the grounding of input parameters in published empirical estimates, most centrally the knowledge decay half-life parameter derived from Darr et al. (1995). Beyond point-estimate grounding, the model was subjected to sensitivity analysis across eight parameter dimensions, including team count (6 to 50), simulation duration (180 to 1,095 days), incident rate (0.01 to 0.20 per day), knowledge decay (two weeks to nineteen years), documentation quality, acquisition probability, assimilation probability, and exploitation probability. The primary finding — that sharing scope produces the ordering GLOBAL > NEIGHBOR > LOCAL > NONE on reliability outcomes — held across all tested parameter combinations. The result is therefore not an artifact of any specific default parameter choice.

## Model Documentation and the Explanation–Prediction Distinction

The model structure follows the Overview, Design Concepts, and Details (ODD) protocol (Grimm et al. 2020), which provides a standardized documentation structure sufficient for independent replication. A full formal ODD document is planned for the journal submission stage (see Section 10, Future Work).

Finally, this study does not claim predictive validity in the sense of forecasting how many incidents a specific organization will experience. The simulation's goal is explanatory: to demonstrate the mechanism by which sharing scope produces differential reliability outcomes under controlled conditions. Epstein (1999) draws this distinction precisely — plate tectonics explains earthquakes without predicting them. The explanatory goal is fully achievable without predictive accuracy, and the validation evidence described above is sufficient to support explanatory conclusions.

---

## Citation Checklist

- [x] Sargent (2020)
- [x] Grimm et al. (2020)
- [x] Zahra & George (2002)
- [x] Darr et al. (1995)
- [x] Epstein (1999)

## Committee Watch

**Q: "How do you know your results aren't just an artifact of your parameter choices?"**
A: Sensitivity analysis across eight parameter dimensions confirmed that the H1 ordering (GLOBAL > NEIGHBOR > LOCAL > NONE) held in every tested variation. The result is robust, not parameter-dependent.

**Q: "Your data is synthetic — how can we trust it?"**
A: Sargent's (2020) framework does not require empirical field data; it requires that the model be theoretically grounded (conceptual validity), behaviorally consistent with theory (operational validity), and parameterized from empirical estimates (data validity). All three are satisfied here.

**Q: "Did you pre-register or specify validation criteria in advance?"**
A: Yes. Pattern-oriented validation per Grimm et al. (2020) requires specifying observable patterns before running experiments. The three validation patterns were designated prior to the experimental runs described in Chapter 4.

**Q: "Why not predict real incident counts rather than just explain trends?"**
A: Following Epstein (1999), explanation and prediction are distinct scientific goals. Predicting incident counts for a specific organization would require calibration to that organization's actual incident history, which is outside the scope of this study. The explanatory goal — demonstrating a causal mechanism — is supported by the validation evidence presented here.
