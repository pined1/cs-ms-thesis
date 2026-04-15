# Organizational Learning from Software Incidents - Simulation

Agent-based simulation for studying how organizational learning strategies affect software incident outcomes.

## Project Structure

```
02-Framework-Code/
├── model.py              # Core simulation
├── run_experiments.py    # Experiment runner (7 experiments)
├── pyproject.toml        # Lint & type check config
├── Makefile              # Build commands
├── requirements.txt      # Dependencies
├── tests/
│   └── test_model.py     # Unit tests (57 tests)
└── thesis_results/       # Experiment outputs
```

## Quick Start

```bash
# Run tests
make test

# Run quick experiment
python3 run_experiments.py --quick --experiment 1

# Run all experiments
python3 run_experiments.py
```

## Core Concepts

### Four Learning Scenarios
- **NONE**: No learning (baseline control)
- **LOCAL**: Teams learn only from their own incidents
- **NEIGHBOR**: Learning propagates to adjacent teams in network
- **GLOBAL**: All teams can learn from any incident

### Four-Stage Absorptive Capacity (Zahra & George 2002)
1. **Acquisition**: Hearing about an incident
2. **Assimilation**: Understanding root cause and adapting to context
3. **Transformation**: Connecting new knowledge to existing mental models
4. **Exploitation**: Implementing preventive or mitigating changes

### Transformation Modes

The transformation stage supports two modes:

**MINIMAL (default)**: Single probability check with cognitive factors
- Transformation probability depends on cognitive distance and relevance
- Teams with different knowledge bases or subsystems find transformation harder
- Formula: `p_transform = (0.8 * cognitive_factor + 0.2 * doc_quality) * base_prob * relevance_scale`

**TIME-BASED (optional)**: Cumulative effort over multiple timesteps
- Enabled via `use_time_based_transformation=True`
- Transformation requires accumulated effort to reach 1.0 progress
- Models the real-world insight: "teams need time to figure out how this applies to them"
- Progress rate depends on cognitive alignment, relevance, and documentation quality

```python
# Enable TIME-BASED mode
params = SimulationParams(
    use_time_based_transformation=True,
    transformation_effort_rate=0.2  # Progress per timestep
)
```

### Three Knowledge Dimensions
- **Prevention**: Reduces probability of similar incidents
- **Detection**: Reduces Mean Time to Detect (MTTD)
- **Mitigation**: Reduces severity and time to recovery

### Incident Types (ARTS Taxonomy)
- Database timeout
- Configuration error
- Dependency failure
- Capacity issue
- Deployment problem

### Subsystem Types
- DATABASE, PAYMENT, AUTH, FRONTEND, API, CACHE
- Each subsystem has different susceptibility to incident types

### Output Metrics
- **Frequency**: Incidents per subsystem over time
- **Duration**: Time to resolve incidents
- **MTTD**: Mean Time to Detect
- **MTTR**: Mean Time to Recovery
- **Severity**: Impact on 1-5 scale
- **Availability**: MTBF / (MTBF + MTTR)
- **Engineering Cost**: Developer-hours spent

## Experiments

1. **Learning Scenario Comparison**: NONE vs LOCAL vs NEIGHBOR vs GLOBAL
2. **Network Topology Effect**: How topology affects knowledge diffusion
3. **Exploitation Effectiveness**: How learning reduces incident impact
4. **Deployment Velocity**: Can learning keep pace with increased risk?
5. **Baseline Comparison**: Documentation quality effects
6. **Transformation Sensitivity**: Impact of transformation probability
7. **Transformation Mode Comparison**: MINIMAL vs TIME-BASED modes

## Development

```bash
# Install dev dependencies
make install-dev

# Run linter
make lint

# Run type checker
make typecheck

# Run all checks
make check
```

## Theoretical Foundations

- **Absorptive Capacity**: Cohen & Levinthal (1990), Zahra & George (2002)
- **Cognitive Distance**: Nooteboom et al. (2007) inverted-U curve
- **Exploration vs Exploitation**: March (1991)
- **Learning from Incidents**: Lunney & Lueder (2016), Drupsteen & Guldenmund (2014)
- **Incident Taxonomy**: Dogga et al. (2023) ARTS classification

## Dependencies

- numpy
- networkx
- matplotlib
- scipy

---

**Last Updated**: February 2026
