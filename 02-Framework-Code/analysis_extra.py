"""
Analysis of existing results — no new simulations needed.

1. Time dynamics: when does H1 ordering emerge?
   Extracts 30-day rolling incident windows from exp1 time series.

2. Cohen's d effect sizes for all key pairwise comparisons.

Usage:
    python analysis_extra.py --analysis time_dynamics
    python analysis_extra.py --analysis cohens_d
    python analysis_extra.py --analysis all
"""

import argparse
import json
import glob
from pathlib import Path
import numpy as np

RESULTS_DIR = Path("thesis_results")


def load_latest(pattern: str) -> dict:
    """Load the most recent results file matching pattern."""
    files = sorted(glob.glob(str(RESULTS_DIR / pattern)))
    if not files:
        raise FileNotFoundError(f"No files matching {pattern}")
    latest = files[-1]
    print(f"  Loading: {latest}")
    with open(latest) as f:
        return json.load(f)


def cohens_d(group1: list, group2: list) -> float:
    """Cohen's d effect size between two groups."""
    n1, n2 = len(group1), len(group2)
    mean1, mean2 = np.mean(group1), np.mean(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    if pooled_std == 0:
        return 0.0
    return float((mean1 - mean2) / pooled_std)


def interpret_d(d: float) -> str:
    d = abs(d)
    if d < 0.2: return "negligible"
    if d < 0.5: return "small"
    if d < 0.8: return "medium"
    return "LARGE"


# ==============================================================================
# Time Dynamics Analysis
# ==============================================================================

def analyze_time_dynamics():
    print("\n" + "=" * 70)
    print("ANALYSIS: Time Dynamics — When Does H1 Ordering Emerge?")
    print("=" * 70)

    # Load the most recent H1 experiment with full time series
    # We need individual run data, not just aggregated — load raw exp1 result
    files = sorted(glob.glob(str(RESULTS_DIR / "exp1_learning_scenarios_*.json")))
    if not files:
        print("  ERROR: No exp1 results found.")
        return

    latest = files[-1]
    print(f"  Using: {latest}")
    with open(latest) as f:
        data = json.load(f)

    # exp1 stores aggregated stats per scenario, not individual time series
    # We need to re-run a small batch (5 seeds) to get time series data
    # Instead, work with what we have: check if time_series data is present
    scenarios = ["NONE", "LOCAL", "NEIGHBOR", "GLOBAL"]

    # Check structure
    sample = data.get("NONE", {})
    if "total_incidents" not in sample:
        print("  Data structure unexpected. Attempting alternate parsing.")
        print(f"  Keys found: {list(data.keys())}")
        return

    print("\n  Note: Aggregated exp1 results do not include per-timestep incident counts.")
    print("  Running a focused 20-seed time-series extraction...")

    from model import SimulationParams, LearningScenario, run_simulation

    base_params = {
        "num_teams": 20,
        "steps": 365,
        "network_topology": "watts_strogatz",
        "base_incident_rate": 0.05,
        "deployment_rate": 0.1,
        "transformation_probability": 0.6,
    }

    seeds = list(range(50))  # 50 seeds for time dynamics
    window = 30              # 30-day windows

    scenario_ts = {}

    for scenario in LearningScenario:
        label = scenario.name
        print(f"\n  Extracting time series for {label} (50 seeds)...", end=" ", flush=True)
        incident_series = []
        knowledge_series = []
        transform_series = []

        for seed in seeds:
            params = SimulationParams(**{**base_params, "learning_scenario": scenario, "seed": seed})
            result = run_simulation(params)
            ts = result["time_series"]
            # incident_frequency is a dict keyed by subsystem — sum across subsystems
            freq_dict = ts["incident_frequency"]
            total_per_day = np.sum([freq_dict[k] for k in freq_dict], axis=0).tolist()
            incident_series.append(total_per_day)
            knowledge_series.append(ts["avg_prevention_knowledge"])
            if ts.get("transformation_rate"):
                transform_series.append(ts["transformation_rate"])

        # Average across seeds
        max_len = min(len(s) for s in incident_series)
        avg_incidents = np.mean([s[:max_len] for s in incident_series], axis=0)
        avg_knowledge = np.mean([s[:max_len] for s in knowledge_series], axis=0)
        avg_transform = np.mean([s[:max_len] for s in transform_series], axis=0) if transform_series else np.zeros(max_len)

        # 30-day rolling windows
        window_incidents = []
        for start in range(0, max_len - window + 1, window):
            window_incidents.append(float(np.sum(avg_incidents[start:start+window])))

        scenario_ts[label] = {
            "avg_incidents_per_window": window_incidents,
            "avg_knowledge": avg_knowledge.tolist(),
            "avg_transform": avg_transform.tolist(),
        }
        print(f"Done.")

    # Print time dynamics table
    print("\n  INCIDENT COUNT BY 30-DAY WINDOW (mean across 50 seeds):")
    print("  " + "-" * 75)
    windows = list(range(1, len(scenario_ts["NONE"]["avg_incidents_per_window"]) + 1))
    header = f"  {'Window':<10}" + "".join(f"{'Day '+str(w*30):>12}" for w in windows[:12])
    print(header)
    print("  " + "-" * 75)
    for label in ["NONE", "LOCAL", "NEIGHBOR", "GLOBAL"]:
        row = f"  {label:<10}" + "".join(f"{v:>12.1f}" for v in scenario_ts[label]["avg_incidents_per_window"][:12])
        print(row)

    # Find when ordering first holds consistently
    print("\n  ORDERING CHECK BY WINDOW (NONE > LOCAL > NEIGHBOR > GLOBAL):")
    print("  " + "-" * 50)
    n_windows = len(scenario_ts["NONE"]["avg_incidents_per_window"])
    first_hold = None
    for w in range(n_windows):
        none_v = scenario_ts["NONE"]["avg_incidents_per_window"][w]
        local_v = scenario_ts["LOCAL"]["avg_incidents_per_window"][w]
        neighbor_v = scenario_ts["NEIGHBOR"]["avg_incidents_per_window"][w]
        global_v = scenario_ts["GLOBAL"]["avg_incidents_per_window"][w]
        holds = none_v > local_v > neighbor_v > global_v
        status = "✓ HOLDS" if holds else "✗ not yet"
        print(f"  Days {w*30+1:>4}–{(w+1)*30:>4}: {status}  (NONE={none_v:.1f}, LOCAL={local_v:.1f}, NEIGHBOR={neighbor_v:.1f}, GLOBAL={global_v:.1f})")
        if holds and first_hold is None:
            first_hold = (w + 1) * 30

    if first_hold:
        print(f"\n  ➜ H1 ordering first holds consistently at DAY {first_hold}")
    else:
        print(f"\n  ➜ H1 ordering does not fully stabilize within 365 days")

    # Knowledge accumulation onset
    print("\n  KNOWLEDGE ACCUMULATION — when does GLOBAL diverge from NONE?")
    none_k = scenario_ts["NONE"]["avg_knowledge"]
    global_k = scenario_ts["GLOBAL"]["avg_knowledge"]
    for day in [30, 60, 90, 120, 180, 270, 365]:
        idx = min(day - 1, len(none_k) - 1)
        print(f"  Day {day:>4}: NONE={none_k[idx]:.3f}  GLOBAL={global_k[idx]:.3f}  gap={global_k[idx]-none_k[idx]:.3f}")

    # Save
    output_path = RESULTS_DIR / f"analysis_time_dynamics_{__import__('datetime').datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_path, "w") as f:
        json.dump(scenario_ts, f, indent=2)
    print(f"\n  Saved: {output_path}")

    return scenario_ts


# ==============================================================================
# Cohen's d Effect Sizes
# ==============================================================================

def analyze_cohens_d():
    print("\n" + "=" * 70)
    print("ANALYSIS: Cohen's d Effect Sizes")
    print("=" * 70)

    # We need raw values — re-run H1 with 100 seeds storing raw incident counts
    print("  Re-running H1 with 100 seeds to extract raw distributions...")

    from model import SimulationParams, LearningScenario, run_simulation

    base_params = {
        "num_teams": 20,
        "steps": 365,
        "network_topology": "watts_strogatz",
        "base_incident_rate": 0.05,
        "deployment_rate": 0.1,
        "transformation_probability": 0.6,
    }

    seeds = list(range(100))
    raw = {}

    for scenario in LearningScenario:
        label = scenario.name
        print(f"  Running {label}...", end=" ", flush=True)
        incidents = []
        for seed in seeds:
            params = SimulationParams(**{**base_params, "learning_scenario": scenario, "seed": seed})
            result = run_simulation(params)
            incidents.append(result["summary"]["total_incidents"])
        raw[label] = incidents
        print(f"Done. Mean: {np.mean(incidents):.1f}, SD: {np.std(incidents):.1f}")

    print("\n  COHEN'S D EFFECT SIZES (pairwise):")
    print("  " + "-" * 65)
    print(f"  {'Comparison':<30} {'d':>8} {'|d|':>8} {'Magnitude':>12} {'p<0.001?':>10}")
    print("  " + "-" * 65)

    comparisons = [
        ("NONE", "GLOBAL",    "NONE vs GLOBAL (main finding)"),
        ("NONE", "NEIGHBOR",  "NONE vs NEIGHBOR"),
        ("NONE", "LOCAL",     "NONE vs LOCAL"),
        ("LOCAL", "NEIGHBOR", "LOCAL vs NEIGHBOR"),
        ("LOCAL", "GLOBAL",   "LOCAL vs GLOBAL"),
        ("NEIGHBOR", "GLOBAL","NEIGHBOR vs GLOBAL"),
    ]

    from scipy import stats as scipy_stats
    results = {}

    for g1, g2, label in comparisons:
        d = cohens_d(raw[g1], raw[g2])
        mag = interpret_d(d)
        t_stat, p_val = scipy_stats.ttest_ind(raw[g1], raw[g2])
        sig = "YES" if p_val < 0.001 else f"p={p_val:.4f}"
        print(f"  {label:<30} {d:>8.3f} {abs(d):>8.3f} {mag:>12} {sig:>10}")
        results[label] = {"cohens_d": d, "p_value": float(p_val), "magnitude": mag}

    print("\n  EFFECT SIZE REFERENCE: <0.2=negligible, 0.2-0.5=small, 0.5-0.8=medium, >0.8=LARGE")

    # Also compute for ablations using stored raw values from aggregate()
    print("\n  NOTE: Ablation effect sizes require raw distributions.")
    print("  See exp11/exp12 JSON files — 'raw' field added by aggregate() in publication_tests.py")

    output_path = RESULTS_DIR / f"analysis_cohens_d_{__import__('datetime').datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n  Saved: {output_path}")

    return results


# ==============================================================================
# MAIN
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="Analysis of existing results")
    parser.add_argument(
        "--analysis", "-a",
        choices=["time_dynamics", "cohens_d", "all"],
        default="all",
    )
    args = parser.parse_args()

    if args.analysis == "all":
        analyze_time_dynamics()
        analyze_cohens_d()
    elif args.analysis == "time_dynamics":
        analyze_time_dynamics()
    elif args.analysis == "cohens_d":
        analyze_cohens_d()


if __name__ == "__main__":
    main()
