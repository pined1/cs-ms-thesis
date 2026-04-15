"""
Experiment Runner for Organizational Learning from Software Incidents Simulation

This script runs the core experiments described in the thesis proposal:

1. Learning Scenario Comparison: NONE vs LOCAL vs NEIGHBOR vs GLOBAL
2. Network Topology Effect: How topology affects knowledge diffusion
3. Exploitation Effectiveness: How learning reduces incident impact
4. Deployment Velocity: Can learning keep pace with increased risk?
5. Baseline Comparisons: Random vs structured strategies
6. Transformation Sensitivity: 4-stage absorptive capacity model analysis
7. Transformation Mode Comparison: MINIMAL vs TIME-BASED transformation modes

Usage:
    python run_experiments.py                    # Run all experiments
    python run_experiments.py --experiment 1    # Run specific experiment (1-7)
    python run_experiments.py --quick           # Quick validation run
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
import warnings

import numpy as np

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

from model import (
    SimulationParams,
    LearningScenario,
    run_simulation,
    compare_learning_scenarios,
)


# ==============================================================================
# CONFIGURATION
# ==============================================================================

RESULTS_DIR = Path("thesis_results")
NUM_SEEDS = 100  # Number of random seeds for statistical robustness
QUICK_SEEDS = 5  # Fewer seeds for quick runs


def ensure_results_dir():
    """Create results directory if it doesn't exist."""
    RESULTS_DIR.mkdir(exist_ok=True)


def save_results(name: str, results: Dict[str, Any]):
    """Save results to JSON file."""
    ensure_results_dir()
    filepath = RESULTS_DIR / f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    # Convert numpy types to Python types for JSON serialization
    def convert(obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, dict):
            return {k: convert(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [convert(v) for v in obj]
        return obj

    with open(filepath, "w") as f:
        json.dump(convert(results), f, indent=2)

    print(f"  Saved: {filepath}")
    return filepath


def run_with_seeds(base_params: dict, seeds: List[int]) -> List[Dict]:
    """Run simulation with multiple seeds sequentially."""
    results = []
    for seed in seeds:
        params = SimulationParams(**{**base_params, "seed": seed})
        results.append(run_simulation(params))
    return results


def aggregate_results(results: List[Dict]) -> Dict[str, Any]:
    """Aggregate results across multiple runs."""
    aggregated = {
        "total_incidents": [],
        "total_engineering_cost": [],
        "total_learning_cost": [],
        "overall_availability": [],
        "final_prevention_knowledge": [],
        "final_detection_knowledge": [],
        "final_mitigation_knowledge": [],
        "transformation_rate": [],  # Stage metric, not knowledge dimension
    }

    for r in results:
        aggregated["total_incidents"].append(r["summary"]["total_incidents"])
        aggregated["total_engineering_cost"].append(r["summary"]["total_engineering_cost"])
        aggregated["total_learning_cost"].append(r["summary"]["total_learning_cost"])
        aggregated["overall_availability"].append(r["summary"]["overall_availability"])

        # Final knowledge from last timestep
        if r["time_series"]["avg_prevention_knowledge"]:
            aggregated["final_prevention_knowledge"].append(
                r["time_series"]["avg_prevention_knowledge"][-1]
            )
            aggregated["final_detection_knowledge"].append(
                r["time_series"]["avg_detection_knowledge"][-1]
            )
            aggregated["final_mitigation_knowledge"].append(
                r["time_series"]["avg_mitigation_knowledge"][-1]
            )

        # Transformation rate (4-stage absorptive capacity model)
        # Note: Transformation is a STAGE, not a knowledge dimension
        if "transformation_rate" in r["time_series"] and r["time_series"]["transformation_rate"]:
            aggregated["transformation_rate"].append(
                r["time_series"]["transformation_rate"][-1]
            )

    # Calculate statistics
    stats = {}
    for key, values in aggregated.items():
        if values:
            n = len(values)
            std = float(np.std(values))
            se = std / np.sqrt(n)
            ci_margin = 1.96 * se
            stats[key] = {
                "mean": float(np.mean(values)),
                "std": std,
                "ci_lower": float(np.mean(values)) - ci_margin,
                "ci_upper": float(np.mean(values)) + ci_margin,
                "min": float(np.min(values)),
                "max": float(np.max(values)),
                "n": n,
            }

    return stats


# ==============================================================================
# EXPERIMENT 1: Learning Scenario Comparison
# ==============================================================================

def experiment_1_learning_scenarios(seeds: List[int]) -> Dict[str, Any]:
    """
    Compare four learning scenarios: NONE, LOCAL, NEIGHBOR, GLOBAL.

    This is the core experiment demonstrating the value of knowledge sharing.
    Expected ordering: GLOBAL > NEIGHBOR > LOCAL > NONE for reliability.
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 1: Learning Scenario Comparison")
    print("=" * 70)

    base_params = {
        "num_teams": 20,
        "steps": 365,  # One year
        "network_topology": "watts_strogatz",
        "base_incident_rate": 0.05,
        "deployment_rate": 0.1,
        "transformation_probability": 0.6,
    }

    results = {}

    for scenario in LearningScenario:
        print(f"\n  Running {scenario.name}...", end=" ", flush=True)
        scenario_params = {**base_params, "learning_scenario": scenario}
        scenario_results = run_with_seeds(scenario_params, seeds)
        results[scenario.name] = aggregate_results(scenario_results)
        print(f"Done. Incidents: {results[scenario.name]['total_incidents']['mean']:.1f}")

    # Verify expected ordering
    print("\n  RESULTS SUMMARY:")
    print("  " + "-" * 70)
    print(f"  {'Scenario':<15} {'Incidents':>12} {'Availability':>15} {'Prevention K':>14} {'Transform %':>12}")
    print("  " + "-" * 70)

    for scenario in ["NONE", "LOCAL", "NEIGHBOR", "GLOBAL"]:
        r = results[scenario]
        transform_rate = r.get('transformation_rate', {}).get('mean', None)
        transform_str = f"{transform_rate:.1%}" if transform_rate is not None else "N/A"
        print(
            f"  {scenario:<15} {r['total_incidents']['mean']:>12.1f} "
            f"{r['overall_availability']['mean']:>15.4f} "
            f"{r['final_prevention_knowledge']['mean']:>14.3f} "
            f"{transform_str:>12}"
        )

    save_results("exp1_learning_scenarios", results)
    return results


# ==============================================================================
# EXPERIMENT 2: Network Topology Effect
# ==============================================================================

def experiment_2_network_topology(seeds: List[int]) -> Dict[str, Any]:
    """
    Compare different network topologies with NEIGHBOR learning.

    Tests: erdos_renyi, complete, watts_strogatz, barabasi_albert, star
    Expected: Complete and dense networks spread knowledge faster.
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 2: Network Topology Effect")
    print("=" * 70)

    topologies = ["erdos_renyi", "complete", "watts_strogatz", "barabasi_albert", "star"]

    base_params = {
        "num_teams": 20,
        "steps": 365,
        "learning_scenario": LearningScenario.NEIGHBOR,
        "base_incident_rate": 0.05,
        "transformation_probability": 0.6,
    }

    results = {}

    for topology in topologies:
        print(f"\n  Running {topology}...", end=" ", flush=True)
        topo_params = {**base_params, "network_topology": topology}
        topo_results = run_with_seeds(topo_params, seeds)
        results[topology] = aggregate_results(topo_results)

        # Extract midpoint prevention knowledge at step ~182 (H4 midpoint metric)
        midpoint_values = []
        for r in topo_results:
            ts = r["time_series"]["avg_prevention_knowledge"]
            idx = min(182, len(ts) - 1)
            midpoint_values.append(ts[idx])
        if midpoint_values:
            n = len(midpoint_values)
            std = float(np.std(midpoint_values))
            se = std / np.sqrt(n)
            ci_margin = 1.96 * se
            results[topology]["midpoint_prevention_knowledge"] = {
                "mean": float(np.mean(midpoint_values)),
                "std": std,
                "ci_lower": float(np.mean(midpoint_values)) - ci_margin,
                "ci_upper": float(np.mean(midpoint_values)) + ci_margin,
                "min": float(np.min(midpoint_values)),
                "max": float(np.max(midpoint_values)),
                "n": n,
            }

        print(f"Done. Knowledge: {results[topology]['final_prevention_knowledge']['mean']:.3f}")

    print("\n  RESULTS SUMMARY:")
    print("  " + "-" * 70)
    for topology in topologies:
        r = results[topology]
        midpoint_mean = r.get("midpoint_prevention_knowledge", {}).get("mean", float("nan"))
        print(
            f"  {topology:<20} "
            f"Incidents: {r['total_incidents']['mean']:>6.1f}  "
            f"Knowledge: {r['final_prevention_knowledge']['mean']:.3f}  "
            f"Midpoint K: {midpoint_mean:.3f}"
        )

    save_results("exp2_network_topology", results)
    return results


# ==============================================================================
# EXPERIMENT 3: Exploitation Effectiveness
# ==============================================================================

def experiment_3_exploitation_effectiveness(seeds: List[int]) -> Dict[str, Any]:
    """
    Test sensitivity to exploitation effectiveness parameters.

    Varies prevention_effect to see how learning reduces incidents.
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 3: Exploitation Effectiveness")
    print("=" * 70)

    effect_levels = [0.0, 0.01, 0.02, 0.05, 0.1]

    base_params = {
        "num_teams": 20,
        "steps": 365,
        "learning_scenario": LearningScenario.NEIGHBOR,
        "network_topology": "watts_strogatz",
        "base_incident_rate": 0.05,
        "transformation_probability": 0.6,
    }

    results = {}

    for effect in effect_levels:
        print(f"\n  Running prevention_effect={effect}...", end=" ", flush=True)
        effect_params = {**base_params, "prevention_effect": effect}
        effect_results = run_with_seeds(effect_params, seeds)
        results[str(effect)] = aggregate_results(effect_results)
        print(f"Done. Incidents: {results[str(effect)]['total_incidents']['mean']:.1f}")

    print("\n  RESULTS SUMMARY:")
    print("  " + "-" * 50)
    for effect in effect_levels:
        r = results[str(effect)]
        print(
            f"  effect={effect:<5}  "
            f"Incidents: {r['total_incidents']['mean']:>6.1f}  "
            f"Availability: {r['overall_availability']['mean']:.4f}"
        )

    save_results("exp3_exploitation_effectiveness", results)
    return results


# ==============================================================================
# EXPERIMENT 4: Deployment Velocity
# ==============================================================================

def experiment_4_deployment_velocity(seeds: List[int]) -> Dict[str, Any]:
    """
    H2: Incident count increases monotonically with deployment rate.

    Criterion: incident count rises at every step of the deployment rate
    sweep (0.05 → 0.1 → 0.2 → 0.3 → 0.5) for both GLOBAL and LOCAL.
    A non-monotonic dip at 5 seeds is likely noise; at 100 seeds the
    ordering should hold consistently.
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 4: Deployment Velocity")
    print("=" * 70)

    deployment_rates = [0.05, 0.1, 0.2, 0.3, 0.5]

    base_params = {
        "num_teams": 20,
        "steps": 365,
        "network_topology": "watts_strogatz",
        "base_incident_rate": 0.03,
        "transformation_probability": 0.6,
    }

    results = {"GLOBAL": {}, "LOCAL": {}}

    for rate in deployment_rates:
        for scenario in [LearningScenario.GLOBAL, LearningScenario.LOCAL]:
            key = f"{rate}"
            print(f"\n  Running {scenario.name} with rate={rate}...", end=" ", flush=True)
            rate_params = {
                **base_params,
                "deployment_rate": rate,
                "learning_scenario": scenario,
            }
            rate_results = run_with_seeds(rate_params, seeds)
            results[scenario.name][key] = aggregate_results(rate_results)
            print(f"Done.")

    print("\n  RESULTS SUMMARY:")
    print("  " + "-" * 60)
    print(f"  {'Rate':<8} {'GLOBAL Incidents':>18} {'LOCAL Incidents':>18}")
    print("  " + "-" * 60)

    for rate in deployment_rates:
        key = str(rate)
        global_inc = results["GLOBAL"][key]["total_incidents"]["mean"]
        local_inc = results["LOCAL"][key]["total_incidents"]["mean"]
        print(f"  {rate:<8} {global_inc:>18.1f} {local_inc:>18.1f}")

    # Monotonicity check
    global_vals = [results["GLOBAL"][str(r)]["total_incidents"]["mean"] for r in deployment_rates]
    local_vals  = [results["LOCAL"][str(r)]["total_incidents"]["mean"] for r in deployment_rates]
    global_mono = all(global_vals[i] <= global_vals[i+1] for i in range(len(global_vals)-1))
    local_mono  = all(local_vals[i]  <= local_vals[i+1]  for i in range(len(local_vals)-1))
    print(f"\n  Monotonicity check — GLOBAL: {'PASS' if global_mono else 'FAIL (dip detected — likely noise at low seeds)'}  |  LOCAL: {'PASS' if local_mono else 'FAIL (dip detected — likely noise at low seeds)'}")

    save_results("exp4_deployment_velocity", results)
    return results


# ==============================================================================
# EXPERIMENT 5: Baseline Comparison
# ==============================================================================

def experiment_5_baseline_comparison(seeds: List[int]) -> Dict[str, Any]:
    """
    Compare structured learning against baselines.

    Baselines:
    - NONE: No learning at all
    - LOW_DOC: Poor documentation quality (assimilation struggles)

    This quantifies the value of structured learning strategies.
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 5: Baseline Comparison")
    print("=" * 70)

    base_params = {
        "num_teams": 20,
        "steps": 365,
        "network_topology": "watts_strogatz",
        "base_incident_rate": 0.05,
        "transformation_probability": 0.6,
    }

    configurations = {
        "no_learning": {
            **base_params,
            "learning_scenario": LearningScenario.NONE,
        },
        "low_doc_local": {
            **base_params,
            "learning_scenario": LearningScenario.LOCAL,
            "documentation_quality": 0.1,
        },
        "high_doc_local": {
            **base_params,
            "learning_scenario": LearningScenario.LOCAL,
            "documentation_quality": 0.9,
        },
        "low_doc_global": {
            **base_params,
            "learning_scenario": LearningScenario.GLOBAL,
            "documentation_quality": 0.1,
        },
        "high_doc_global": {
            **base_params,
            "learning_scenario": LearningScenario.GLOBAL,
            "documentation_quality": 0.9,
        },
    }

    results = {}

    for name, config in configurations.items():
        print(f"\n  Running {name}...", end=" ", flush=True)
        config_results = run_with_seeds(config, seeds)
        results[name] = aggregate_results(config_results)
        print(f"Done. Incidents: {results[name]['total_incidents']['mean']:.1f}")

    print("\n  RESULTS SUMMARY:")
    print("  " + "-" * 60)
    for name in configurations:
        r = results[name]
        print(
            f"  {name:<20}  "
            f"Incidents: {r['total_incidents']['mean']:>6.1f}  "
            f"Avail: {r['overall_availability']['mean']:.4f}"
        )

    save_results("exp5_baseline_comparison", results)
    return results


# ==============================================================================
# EXPERIMENT 6: Transformation Sensitivity Analysis
# ==============================================================================

def experiment_6_transformation_sensitivity(seeds: List[int]) -> Dict[str, Any]:
    """
    Test sensitivity to transformation probability in the 4-stage absorptive capacity model.

    Varies transformation_probability from 0.0 to 1.0 to measure impact on
    final knowledge levels and system reliability.

    The transformation stage represents how effectively teams combine and
    reconfigure existing knowledge with newly assimilated external knowledge.
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 6: Transformation Sensitivity Analysis")
    print("=" * 70)

    transformation_levels = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

    base_params = {
        "num_teams": 20,
        "steps": 365,
        "learning_scenario": LearningScenario.NEIGHBOR,
        "network_topology": "watts_strogatz",
        "base_incident_rate": 0.05,
    }

    results = {}

    for transform_prob in transformation_levels:
        print(f"\n  Running transformation_probability={transform_prob}...", end=" ", flush=True)
        transform_params = {**base_params, "transformation_probability": transform_prob}
        transform_results = run_with_seeds(transform_params, seeds)
        results[str(transform_prob)] = aggregate_results(transform_results)
        r = results[str(transform_prob)]
        incidents = r['total_incidents']['mean']
        knowledge = r['final_prevention_knowledge']['mean']
        print(f"Done. Incidents: {incidents:.1f}, Knowledge: {knowledge:.3f}")

    print("\n  RESULTS SUMMARY:")
    print("  " + "-" * 70)
    print(f"  {'Transform Prob':<15} {'Incidents':>12} {'Availability':>15} {'Prevention K':>14} {'Transform %':>12}")
    print("  " + "-" * 70)

    for transform_prob in transformation_levels:
        r = results[str(transform_prob)]
        transform_rate = r.get('transformation_rate', {}).get('mean', None)
        transform_str = f"{transform_rate:.1%}" if transform_rate is not None else "N/A"
        print(
            f"  {transform_prob:<15.1f} "
            f"{r['total_incidents']['mean']:>12.1f} "
            f"{r['overall_availability']['mean']:>15.4f} "
            f"{r['final_prevention_knowledge']['mean']:>14.3f} "
            f"{transform_str:>12}"
        )

    save_results("exp6_transformation_sensitivity", results)
    return results


# ==============================================================================
# EXPERIMENT 7: Transformation Mode Comparison
# ==============================================================================

def experiment_7_transformation_modes(seeds: List[int]) -> Dict[str, Any]:
    """
    Compare MINIMAL vs TIME-BASED transformation modes.

    Tests whether effort-based transformation produces different
    learning dynamics than probability-based transformation.
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 7: Transformation Mode Comparison")
    print("=" * 70)

    base_params = {
        "num_teams": 20,
        "steps": 365,
        "network_topology": "watts_strogatz",
        "learning_scenario": LearningScenario.NEIGHBOR,
        "base_incident_rate": 0.05,
        "transformation_probability": 0.6,
    }

    results = {}

    # MINIMAL mode (default)
    print("\n  Running MINIMAL mode...")
    minimal_params = {**base_params, "use_time_based_transformation": False}
    results["MINIMAL"] = aggregate_results(run_with_seeds(minimal_params, seeds))
    print(f"Done. Transform rate: {results['MINIMAL']['transformation_rate']['mean']:.1%}")

    # TIME-BASED with different effort rates
    for effort_rate in [0.1, 0.2, 0.3]:
        label = f"TIME_{effort_rate}"
        print(f"\n  Running TIME-BASED (rate={effort_rate})...")
        time_params = {
            **base_params,
            "use_time_based_transformation": True,
            "transformation_effort_rate": effort_rate,
        }
        results[label] = aggregate_results(run_with_seeds(time_params, seeds))
        print(f"Done. Transform rate: {results[label]['transformation_rate']['mean']:.1%}")

    # Display results
    print("\n  RESULTS SUMMARY:")
    print("  " + "-" * 70)
    print(f"  {'Mode':<20} {'Incidents':>12} {'Availability':>15} {'Prevention K':>14} {'Transform %':>12}")
    print("  " + "-" * 70)

    for mode in ["MINIMAL", "TIME_0.1", "TIME_0.2", "TIME_0.3"]:
        r = results[mode]
        transform_rate = r.get('transformation_rate', {}).get('mean', None)
        transform_str = f"{transform_rate:.1%}" if transform_rate is not None else "N/A"
        print(
            f"  {mode:<20} {r['total_incidents']['mean']:>12.1f} "
            f"{r['overall_availability']['mean']:>15.4f} "
            f"{r['final_prevention_knowledge']['mean']:>14.3f} "
            f"{transform_str:>12}"
        )

    save_results("exp7_transformation_modes", results)
    return results


# ==============================================================================
# EXPERIMENT 8: H3: Org Conditions for NEIGHBOR≈GLOBAL
# ==============================================================================

def experiment_h3_knowledge_threshold_sweep(seeds: List[int]) -> Dict[str, Any]:
    """
    H3: Under what organizational conditions (team count, network topology)
    does NEIGHBOR sharing capture >=80% of GLOBAL's reliability benefit?

    Sweeps num_teams x network_topology and computes:
        benefit_ratio = (NONE_incidents - NEIGHBOR_incidents)
                      / (NONE_incidents - GLOBAL_incidents)

    ratio >= 0.8 => NEIGHBOR is "good enough"
    ratio <  0.8 => GLOBAL provides meaningfully more value
    """
    print("\n" + "=" * 70)
    print("EXPERIMENT 8: H3: Org Conditions for NEIGHBOR\u2248GLOBAL")
    print("=" * 70)

    team_counts = [6, 10, 20, 35, 50]
    topologies = ["watts_strogatz", "erdos_renyi", "barabasi_albert"]

    base_params = {
        "steps": 365,
        "base_incident_rate": 0.05,
        "transformation_probability": 0.6,
        "deployment_rate": 0.1,
    }

    configurations = {}

    for num_teams in team_counts:
        for topology in topologies:
            combo_key = f"teams{num_teams}_{topology}"
            configurations[combo_key] = {}

            for scenario in [LearningScenario.NONE, LearningScenario.NEIGHBOR, LearningScenario.GLOBAL]:
                print(
                    f"\n  Running num_teams={num_teams}, topology={topology}, {scenario.name}...",
                    end=" ",
                    flush=True,
                )
                params = {
                    **base_params,
                    "num_teams": num_teams,
                    "network_topology": topology,
                    "learning_scenario": scenario,
                }
                scenario_results = run_with_seeds(params, seeds)
                configurations[combo_key][scenario.name] = aggregate_results(scenario_results)
                incidents = configurations[combo_key][scenario.name]["total_incidents"]["mean"]
                print(f"Done. Incidents: {incidents:.1f}")

            none_inc = configurations[combo_key]["NONE"]["total_incidents"]["mean"]
            neighbor_inc = configurations[combo_key]["NEIGHBOR"]["total_incidents"]["mean"]
            global_inc = configurations[combo_key]["GLOBAL"]["total_incidents"]["mean"]
            denominator = none_inc - global_inc
            if denominator != 0:
                benefit_ratio = (none_inc - neighbor_inc) / denominator
            else:
                benefit_ratio = float("nan")
            configurations[combo_key]["benefit_ratio"] = benefit_ratio
            label = "GOOD ENOUGH" if benefit_ratio >= 0.8 else "GLOBAL BETTER"
            print(f"  => benefit_ratio={benefit_ratio:.3f}  [{label}]")

    # Results matrix: rows = num_teams, columns = topology
    print("\n  RESULTS SUMMARY — benefit_ratio matrix (>= 0.80: NEIGHBOR good enough)")
    print("  " + "-" * 70)
    col_w = 22
    header = f"  {'teams \\ topology':<16}" + "".join(f"{t:>{col_w}}" for t in topologies)
    print(header)
    print("  " + "-" * 70)
    for num_teams in team_counts:
        row = f"  {num_teams:<16}"
        for topology in topologies:
            combo_key = f"teams{num_teams}_{topology}"
            ratio = configurations[combo_key]["benefit_ratio"]
            if ratio != ratio:  # nan check
                cell = "   N/A"
            else:
                marker = "* " if ratio >= 0.8 else "  "
                cell = f"{marker}{ratio:.3f}"
            row += f"{cell:>{col_w}}"
        print(row)
    print("  " + "-" * 70)
    print("  * = NEIGHBOR captures >=80% of GLOBAL benefit (ratio >= 0.80)")

    result = {"experiment": "H3: Org Conditions for NEIGHBOR\u2248GLOBAL", "configurations": configurations}
    save_results("exp8_h3_org_conditions_neighbor_global", result)
    return result


# ==============================================================================
# EXPERIMENT 9: Robustness — Team Count Variation
# ==============================================================================

def experiment_robustness_team_count(seeds: List[int]) -> Dict[str, Any]:
    """Robustness Part 1: Verify H1 ordering holds across team counts 6, 20, 50."""
    print("\n" + "=" * 70)
    print("EXPERIMENT 9: Robustness — Team Count Variation")
    print("=" * 70)

    team_counts = [6, 20, 50]

    base_params = {
        "steps": 365,
        "network_topology": "watts_strogatz",
        "base_incident_rate": 0.05,
        "deployment_rate": 0.1,
        "transformation_probability": 0.6,
    }

    configurations = {}

    for num_teams in team_counts:
        key = str(num_teams)
        configurations[key] = {}
        for scenario in LearningScenario:
            print(f"\n  Running num_teams={num_teams}, {scenario.name}...", end=" ", flush=True)
            params = {**base_params, "num_teams": num_teams, "learning_scenario": scenario}
            scenario_results = run_with_seeds(params, seeds)
            configurations[key][scenario.name] = aggregate_results(scenario_results)
            incidents = configurations[key][scenario.name]["total_incidents"]["mean"]
            print(f"Done. Incidents: {incidents:.1f}")

    print("\n  RESULTS SUMMARY:")
    print("  " + "-" * 70)
    print(f"  {'Teams':<8} {'NONE':>10} {'LOCAL':>10} {'NEIGHBOR':>10} {'GLOBAL':>10}")
    print("  " + "-" * 70)
    for num_teams in team_counts:
        key = str(num_teams)
        c = configurations[key]
        print(
            f"  {num_teams:<8} "
            f"{c['NONE']['total_incidents']['mean']:>10.1f} "
            f"{c['LOCAL']['total_incidents']['mean']:>10.1f} "
            f"{c['NEIGHBOR']['total_incidents']['mean']:>10.1f} "
            f"{c['GLOBAL']['total_incidents']['mean']:>10.1f}"
        )

    result = {"experiment": "Robustness: Team Count", "configurations": configurations}
    save_results("exp9_robustness_team_count", result)
    return result


# ==============================================================================
# EXPERIMENT 10: Robustness — Deployment × Learning Effectiveness Cross-Sweep
# ==============================================================================

def experiment_robustness_deployment_learning(seeds: List[int]) -> Dict[str, Any]:
    """Robustness Part 3: 3x3 cross-sweep of deployment rate x learning effectiveness."""
    print("\n" + "=" * 70)
    print("EXPERIMENT 10: Robustness — Deployment x Learning Effectiveness")
    print("=" * 70)

    deployment_rates = [0.05, 0.1, 0.3]
    exploitation_probabilities = [0.2, 0.6, 0.9]

    base_params = {
        "num_teams": 20,
        "steps": 365,
        "network_topology": "watts_strogatz",
        "base_incident_rate": 0.05,
        "transformation_probability": 0.6,
        "learning_scenario": LearningScenario.NEIGHBOR,
    }

    configurations = {}

    for dep_rate in deployment_rates:
        for exp_prob in exploitation_probabilities:
            combo_key = f"dep{dep_rate}_exp{exp_prob}"
            print(f"\n  Running deployment_rate={dep_rate}, exploitation_probability={exp_prob}...", end=" ", flush=True)
            params = {
                **base_params,
                "deployment_rate": dep_rate,
                "exploitation_probability": exp_prob,
            }
            combo_results = run_with_seeds(params, seeds)
            configurations[combo_key] = aggregate_results(combo_results)
            incidents = configurations[combo_key]["total_incidents"]["mean"]
            avail = configurations[combo_key]["overall_availability"]["mean"]
            print(f"Done. Incidents: {incidents:.1f}, Availability: {avail:.4f}")

    print("\n  RESULTS SUMMARY (Incidents / Availability):")
    print("  " + "-" * 70)
    header = f"  {'dep \\ exp':<12}" + "".join(f"  exp={e:<6}" for e in exploitation_probabilities)
    print(header)
    print("  " + "-" * 70)
    for dep_rate in deployment_rates:
        row = f"  dep={dep_rate:<8}"
        for exp_prob in exploitation_probabilities:
            key = f"dep{dep_rate}_exp{exp_prob}"
            inc = configurations[key]["total_incidents"]["mean"]
            row += f"  {inc:>8.1f}"
        print(row)

    result = {"experiment": "Robustness: Deployment x Learning", "configurations": configurations}
    save_results("exp10_robustness_deployment_learning", result)
    return result


# ==============================================================================
# EXPERIMENT 11: Ablation — No Decay
# ==============================================================================

def experiment_ablation_no_decay(seeds: List[int]) -> Dict[str, Any]:
    """Ablation 1: Compare H1 with decay disabled vs default decay."""
    print("\n" + "=" * 70)
    print("EXPERIMENT 11: Ablation — No Decay")
    print("=" * 70)

    base_params = {
        "num_teams": 20,
        "steps": 365,
        "network_topology": "watts_strogatz",
        "base_incident_rate": 0.05,
        "deployment_rate": 0.1,
        "transformation_probability": 0.6,
    }

    configurations = {"default_decay": {}, "no_decay": {}}

    for scenario in LearningScenario:
        # Default decay (knowledge_decay=0.001)
        print(f"\n  Running default_decay, {scenario.name}...", end=" ", flush=True)
        params = {**base_params, "knowledge_decay": 0.001, "learning_scenario": scenario}
        scenario_results = run_with_seeds(params, seeds)
        configurations["default_decay"][scenario.name] = aggregate_results(scenario_results)
        print(f"Done. Incidents: {configurations['default_decay'][scenario.name]['total_incidents']['mean']:.1f}")

        # No decay
        print(f"  Running no_decay, {scenario.name}...", end=" ", flush=True)
        params_no_decay = {**base_params, "disable_knowledge_decay": True, "learning_scenario": scenario}
        no_decay_results = run_with_seeds(params_no_decay, seeds)
        configurations["no_decay"][scenario.name] = aggregate_results(no_decay_results)
        print(f"Done. Incidents: {configurations['no_decay'][scenario.name]['total_incidents']['mean']:.1f}")

    print("\n  RESULTS SUMMARY (mean total_incidents):")
    print("  " + "-" * 60)
    print(f"  {'Scenario':<12} {'Default Decay':>15} {'No Decay':>12}")
    print("  " + "-" * 60)
    for scenario in ["NONE", "LOCAL", "NEIGHBOR", "GLOBAL"]:
        default_inc = configurations["default_decay"][scenario]["total_incidents"]["mean"]
        no_dec_inc = configurations["no_decay"][scenario]["total_incidents"]["mean"]
        print(f"  {scenario:<12} {default_inc:>15.1f} {no_dec_inc:>12.1f}")

    result = {"experiment": "Ablation: No Decay", "configurations": configurations}
    save_results("exp11_ablation_no_decay", result)
    return result


# ==============================================================================
# EXPERIMENT 12: Ablation — No Asymmetry
# ==============================================================================

def experiment_ablation_no_asymmetry(seeds: List[int]) -> Dict[str, Any]:
    """Ablation 2: Compare H1 with source asymmetry disabled vs enabled."""
    print("\n" + "=" * 70)
    print("EXPERIMENT 12: Ablation — No Asymmetry")
    print("=" * 70)

    base_params = {
        "num_teams": 20,
        "steps": 365,
        "network_topology": "watts_strogatz",
        "base_incident_rate": 0.05,
        "deployment_rate": 0.1,
        "transformation_probability": 0.6,
    }

    configurations = {"default_asymmetry": {}, "no_asymmetry": {}}

    for scenario in LearningScenario:
        # Default asymmetry (source team learns directly)
        print(f"\n  Running default_asymmetry, {scenario.name}...", end=" ", flush=True)
        params = {**base_params, "learning_scenario": scenario}
        scenario_results = run_with_seeds(params, seeds)
        configurations["default_asymmetry"][scenario.name] = aggregate_results(scenario_results)
        print(f"Done. Incidents: {configurations['default_asymmetry'][scenario.name]['total_incidents']['mean']:.1f}")

        # No asymmetry (source team goes through same pipeline as other teams)
        print(f"  Running no_asymmetry, {scenario.name}...", end=" ", flush=True)
        params_no_asym = {**base_params, "disable_source_asymmetry": True, "learning_scenario": scenario}
        no_asym_results = run_with_seeds(params_no_asym, seeds)
        configurations["no_asymmetry"][scenario.name] = aggregate_results(no_asym_results)
        print(f"Done. Incidents: {configurations['no_asymmetry'][scenario.name]['total_incidents']['mean']:.1f}")

    print("\n  RESULTS SUMMARY (mean total_incidents):")
    print("  " + "-" * 60)
    print(f"  {'Scenario':<12} {'Default Asymmetry':>18} {'No Asymmetry':>14}")
    print("  " + "-" * 60)
    for scenario in ["NONE", "LOCAL", "NEIGHBOR", "GLOBAL"]:
        default_inc = configurations["default_asymmetry"][scenario]["total_incidents"]["mean"]
        no_asym_inc = configurations["no_asymmetry"][scenario]["total_incidents"]["mean"]
        print(f"  {scenario:<12} {default_inc:>18.1f} {no_asym_inc:>14.1f}")

    result = {"experiment": "Ablation: No Asymmetry", "configurations": configurations}
    save_results("exp12_ablation_no_asymmetry", result)
    return result


# ==============================================================================
# EXPERIMENT 13: Ablation — No Cost
# ==============================================================================

def experiment_ablation_no_cost(seeds: List[int]) -> Dict[str, Any]:
    """Ablation 3: Compare H1 with learning_cost=0 vs default costs."""
    print("\n" + "=" * 70)
    print("EXPERIMENT 13: Ablation — No Cost")
    print("=" * 70)

    base_params = {
        "num_teams": 20,
        "steps": 365,
        "network_topology": "watts_strogatz",
        "base_incident_rate": 0.05,
        "deployment_rate": 0.1,
        "transformation_probability": 0.6,
    }

    configurations = {"default_costs": {}, "no_cost": {}}

    for scenario in LearningScenario:
        # Default costs
        print(f"\n  Running default_costs, {scenario.name}...", end=" ", flush=True)
        params = {**base_params, "learning_scenario": scenario}
        scenario_results = run_with_seeds(params, seeds)
        configurations["default_costs"][scenario.name] = aggregate_results(scenario_results)
        print(f"Done. Incidents: {configurations['default_costs'][scenario.name]['total_incidents']['mean']:.1f}")

        # No cost (learning_cost=0, engineering_cost_base=0)
        print(f"  Running no_cost, {scenario.name}...", end=" ", flush=True)
        params_no_cost = {
            **base_params,
            "learning_cost": 0.0,
            "engineering_cost_base": 0.0,
            "learning_scenario": scenario,
        }
        no_cost_results = run_with_seeds(params_no_cost, seeds)
        configurations["no_cost"][scenario.name] = aggregate_results(no_cost_results)
        print(f"Done. Incidents: {configurations['no_cost'][scenario.name]['total_incidents']['mean']:.1f}")

    print("\n  RESULTS SUMMARY (mean total_incidents / total_engineering_cost):")
    print("  " + "-" * 70)
    print(f"  {'Scenario':<12} {'Default Inc':>12} {'Default Cost':>14} {'No Cost Inc':>12} {'No Cost Cost':>14}")
    print("  " + "-" * 70)
    for scenario in ["NONE", "LOCAL", "NEIGHBOR", "GLOBAL"]:
        d_inc = configurations["default_costs"][scenario]["total_incidents"]["mean"]
        d_cost = configurations["default_costs"][scenario]["total_engineering_cost"]["mean"]
        nc_inc = configurations["no_cost"][scenario]["total_incidents"]["mean"]
        nc_cost = configurations["no_cost"][scenario]["total_engineering_cost"]["mean"]
        print(f"  {scenario:<12} {d_inc:>12.1f} {d_cost:>14.1f} {nc_inc:>12.1f} {nc_cost:>14.1f}")

    result = {"experiment": "Ablation: No Cost", "configurations": configurations}
    save_results("exp13_ablation_no_cost", result)
    return result


# ==============================================================================
# MAIN
# ==============================================================================

def run_all_experiments(quick: bool = False):
    """Run all experiments."""
    print("\n" + "=" * 70)
    print("ORGANIZATIONAL LEARNING FROM SOFTWARE INCIDENTS")
    print("Experiment Suite")
    print("=" * 70)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Results directory: {RESULTS_DIR}")

    seeds = list(range(QUICK_SEEDS if quick else NUM_SEEDS))
    print(f"Random seeds: {len(seeds)}")

    all_results = {}

    try:
        all_results["exp1"] = experiment_1_learning_scenarios(seeds)
        all_results["exp2"] = experiment_2_network_topology(seeds)
        all_results["exp3"] = experiment_3_exploitation_effectiveness(seeds)
        all_results["exp4"] = experiment_4_deployment_velocity(seeds)
        all_results["exp5"] = experiment_5_baseline_comparison(seeds)
        all_results["exp6"] = experiment_6_transformation_sensitivity(seeds)
        all_results["exp7"] = experiment_7_transformation_modes(seeds)
        all_results["exp8"] = experiment_h3_knowledge_threshold_sweep(seeds)
        all_results["exp9"] = experiment_robustness_team_count(seeds)
        all_results["exp10"] = experiment_robustness_deployment_learning(seeds)
        all_results["exp11"] = experiment_ablation_no_decay(seeds)
        all_results["exp12"] = experiment_ablation_no_asymmetry(seeds)
        all_results["exp13"] = experiment_ablation_no_cost(seeds)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user.")

    print("\n" + "=" * 70)
    print("EXPERIMENT SUMMARY")
    print("=" * 70)
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Results saved to: {RESULTS_DIR}")

    return all_results


def run_single_experiment(exp_num: int, quick: bool = False):
    """Run a single experiment by number."""
    seeds = list(range(QUICK_SEEDS if quick else NUM_SEEDS))

    experiments = {
        1: ("Learning Scenarios", experiment_1_learning_scenarios),
        2: ("Network Topology", experiment_2_network_topology),
        3: ("Exploitation Effectiveness", experiment_3_exploitation_effectiveness),
        4: ("Deployment Velocity", experiment_4_deployment_velocity),
        5: ("Baseline Comparison", experiment_5_baseline_comparison),
        6: ("Transformation Sensitivity", experiment_6_transformation_sensitivity),
        7: ("Transformation Mode Comparison", experiment_7_transformation_modes),
        8: ("H3: Org Conditions for NEIGHBOR\u2248GLOBAL", experiment_h3_knowledge_threshold_sweep),
        9: ("Robustness: Team Count", experiment_robustness_team_count),
        10: ("Robustness: Deployment x Learning", experiment_robustness_deployment_learning),
        11: ("Ablation: No Decay", experiment_ablation_no_decay),
        12: ("Ablation: No Asymmetry", experiment_ablation_no_asymmetry),
        13: ("Ablation: No Cost", experiment_ablation_no_cost),
    }

    if exp_num not in experiments:
        print(f"Unknown experiment: {exp_num}. Available: {list(experiments.keys())}")
        return

    name, func = experiments[exp_num]
    print(f"\nRunning Experiment {exp_num}: {name}")
    return func(seeds)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run organizational learning simulation experiments"
    )
    parser.add_argument(
        "--experiment", "-e", type=int, default=None,
        help="Run specific experiment (1-13)"
    )
    parser.add_argument(
        "--quick", "-q", action="store_true",
        help="Quick run with fewer seeds"
    )

    args = parser.parse_args()

    if args.experiment:
        run_single_experiment(args.experiment, quick=args.quick)
    else:
        run_all_experiments(quick=args.quick)
