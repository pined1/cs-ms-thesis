"""
Publication-level tests for thesis validation.

Covers remaining gaps identified for reviewer-level rigor:
  - Simulation duration sensitivity (180 / 365 / 730 / 1095 days)
  - ba_m sweep (Barabási-Albert edge density)
  - ws_k sweep (Watts-Strogatz neighbor count)
  - Knowledge decay rate sweep
  - 500-seed H3 rerun
  - Documentation quality × sharing scenario interaction
  - base_incident_rate sweep

Usage:
    python publication_tests.py --sweep duration
    python publication_tests.py --sweep ba_m
    python publication_tests.py --sweep ws_k
    python publication_tests.py --sweep decay_rate
    python publication_tests.py --sweep h3_500seeds
    python publication_tests.py --sweep doc_quality_interaction
    python publication_tests.py --sweep base_incident_rate
"""

import argparse
import json
import warnings
from datetime import datetime
from pathlib import Path

import numpy as np

warnings.filterwarnings("ignore")

from model import SimulationParams, LearningScenario, run_simulation

RESULTS_DIR = Path("thesis_results")
NUM_SEEDS = 100

BASE_PARAMS = {
    "num_teams": 20,
    "steps": 365,
    "network_topology": "watts_strogatz",
    "base_incident_rate": 0.05,
    "deployment_rate": 0.1,
    "transformation_probability": 0.6,
    "learning_scenario": LearningScenario.NEIGHBOR,
}


def save_results(name: str, results: dict) -> Path:
    RESULTS_DIR.mkdir(exist_ok=True)
    filepath = RESULTS_DIR / f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    def convert(obj):
        if isinstance(obj, np.ndarray): return obj.tolist()
        if isinstance(obj, np.integer): return int(obj)
        if isinstance(obj, np.floating): return float(obj)
        if isinstance(obj, dict): return {k: convert(v) for k, v in obj.items()}
        if isinstance(obj, list): return [convert(v) for v in obj]
        return obj

    with open(filepath, "w") as f:
        json.dump(convert(results), f, indent=2)
    print(f"  Saved: {filepath}")
    return filepath


def run_with_seeds(base_params: dict, seeds: list) -> list:
    results = []
    for seed in seeds:
        params = SimulationParams(**{**base_params, "seed": seed})
        results.append(run_simulation(params))
    return results


def aggregate(results: list) -> dict:
    raw = {
        "total_incidents": [],
        "overall_availability": [],
        "final_prevention_knowledge": [],
        "transformation_rate": [],
    }
    for r in results:
        raw["total_incidents"].append(r["summary"]["total_incidents"])
        raw["overall_availability"].append(r["summary"]["overall_availability"])
        ts = r["time_series"]
        if ts.get("avg_prevention_knowledge"):
            raw["final_prevention_knowledge"].append(ts["avg_prevention_knowledge"][-1])
        if ts.get("transformation_rate"):
            raw["transformation_rate"].append(ts["transformation_rate"][-1])
    stats = {}
    for key, values in raw.items():
        if values:
            n = len(values)
            arr = np.array(values)
            std = float(np.std(arr))
            se = std / np.sqrt(n)
            ci = 1.96 * se
            stats[key] = {
                "mean": float(np.mean(arr)),
                "std": std,
                "ci_lower": float(np.mean(arr)) - ci,
                "ci_upper": float(np.mean(arr)) + ci,
                "raw": values,
                "n": n,
            }
    return stats


def print_row(label: str, r: dict):
    inc = r.get("total_incidents", {}).get("mean", float("nan"))
    avail = r.get("overall_availability", {}).get("mean", float("nan"))
    prevK = r.get("final_prevention_knowledge", {}).get("mean", float("nan"))
    tr = r.get("transformation_rate", {}).get("mean", None)
    tr_str = f"{tr:.1%}" if tr is not None else "N/A"
    print(f"  {label:<32} inc={inc:>7.1f}  avail={avail:.4f}  prevK={prevK:.3f}  transform={tr_str}")


# ==============================================================================
# 1. Simulation Duration Sensitivity
# ==============================================================================

def sweep_duration(seeds):
    print("\n" + "=" * 70)
    print("PUBLICATION TEST: Simulation Duration Sensitivity")
    print("Sweep: [180, 365, 730, 1095 days] | All 4 scenarios")
    print("=" * 70)
    print("  Question: Is 365 days in transient or steady state?")
    print("  Does H1 ordering hold at all durations?")

    durations = [180, 365, 730, 1095]
    results = {}

    for steps in durations:
        results[str(steps)] = {}
        for scenario in LearningScenario:
            label = scenario.name
            print(f"\n  Running steps={steps}, {label}...", end=" ", flush=True)
            params = {**BASE_PARAMS, "steps": steps, "learning_scenario": scenario}
            r = aggregate(run_with_seeds(params, seeds))
            results[str(steps)][label] = r
            print(f"Done. Incidents: {r['total_incidents']['mean']:.1f}")

    print("\n  RESULTS SUMMARY (mean incidents per day to normalize across durations):")
    print("  " + "-" * 70)
    print(f"  {'Steps':<8} {'NONE':>10} {'LOCAL':>10} {'NEIGHBOR':>10} {'GLOBAL':>10} {'H1?':>6}")
    print("  " + "-" * 70)
    for steps in durations:
        r = results[str(steps)]
        none_i = r["NONE"]["total_incidents"]["mean"]
        local_i = r["LOCAL"]["total_incidents"]["mean"]
        neighbor_i = r["NEIGHBOR"]["total_incidents"]["mean"]
        global_i = r["GLOBAL"]["total_incidents"]["mean"]
        h1 = "✓" if none_i > local_i > neighbor_i > global_i else "✗"
        # Normalize by duration for fair comparison
        print(f"  {steps:<8} {none_i/steps:>10.3f} {local_i/steps:>10.3f} {neighbor_i/steps:>10.3f} {global_i/steps:>10.3f} {h1:>6}")

    print("  (values = incidents per day)")
    save_results("publication_simulation_duration", results)
    return results


# ==============================================================================
# 2. ba_m Sweep (Barabási-Albert edge density)
# ==============================================================================

def sweep_ba_m(seeds):
    print("\n" + "=" * 70)
    print("PUBLICATION TEST: Barabási-Albert ba_m Sweep")
    print("Sweep: ba_m = [1, 2, 3, 4, 6] | NEIGHBOR scenario")
    print("=" * 70)
    print("  Question: At what ba_m does scale-free topology stop underperforming?")
    print("  Answers committee question on minimum network size for scale-free.")

    ba_m_values = [1, 2, 3, 4, 6]
    results = {}

    for m in ba_m_values:
        print(f"\n  Running ba_m={m}...", end=" ", flush=True)
        params = {**BASE_PARAMS, "network_topology": "barabasi_albert", "ba_m": m}
        r = aggregate(run_with_seeds(params, seeds))
        results[str(m)] = r
        print("Done.")
        print_row(f"ba_m={m}", r)

    # Compare against Watts-Strogatz baseline
    print(f"\n  Running watts_strogatz baseline...", end=" ", flush=True)
    ws_r = aggregate(run_with_seeds(BASE_PARAMS, seeds))
    results["watts_strogatz_baseline"] = ws_r
    print("Done.")
    print_row("watts_strogatz (baseline)", ws_r)

    print("\n  INTERPRETATION: Does higher ba_m rescue BA performance?")
    ws_inc = ws_r["total_incidents"]["mean"]
    for m in ba_m_values:
        ba_inc = results[str(m)]["total_incidents"]["mean"]
        gap = ba_inc - ws_inc
        better = "BA better" if gap < 0 else f"BA worse by {gap:.1f}"
        print(f"  ba_m={m}: {ba_inc:.1f} vs WS {ws_inc:.1f} → {better}")

    save_results("publication_ba_m_sweep", results)
    return results


# ==============================================================================
# 3. ws_k Sweep (Watts-Strogatz neighbor count)
# ==============================================================================

def sweep_ws_k(seeds):
    print("\n" + "=" * 70)
    print("PUBLICATION TEST: Watts-Strogatz ws_k Sweep")
    print("Sweep: ws_k = [2, 4, 6, 8, 10] | NEIGHBOR scenario")
    print("=" * 70)
    print("  Question: How sensitive is NEIGHBOR learning to network degree?")
    print("  ws_k controls how many direct neighbors each team has.")

    ws_k_values = [2, 4, 6, 8, 10]
    results = {}

    for k in ws_k_values:
        print(f"\n  Running ws_k={k}...", end=" ", flush=True)
        params = {**BASE_PARAMS, "ws_k": k}
        r = aggregate(run_with_seeds(params, seeds))
        results[str(k)] = r
        print("Done.")
        print_row(f"ws_k={k}", r)

    print("\n  INTERPRETATION:")
    for k in ws_k_values:
        inc = results[str(k)]["total_incidents"]["mean"]
        prevK = results[str(k)]["final_prevention_knowledge"]["mean"]
        print(f"  ws_k={k}: {inc:.1f} incidents, prevK={prevK:.3f}")

    save_results("publication_ws_k_sweep", results)
    return results


# ==============================================================================
# 4. Knowledge Decay Rate Sweep
# ==============================================================================

def sweep_decay_rate(seeds):
    print("\n" + "=" * 70)
    print("PUBLICATION TEST: Knowledge Decay Rate Sweep")
    print("Sweep: knowledge_decay = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05]")
    print("=" * 70)
    print("  0.0001 → half-life ~19 years")
    print("  0.001  → half-life ~2 years (default, Darr et al.)")
    print("  0.005  → half-life ~5 months")
    print("  0.01   → half-life ~2.5 months")
    print("  0.05   → half-life ~2 weeks")
    print("  Question: Does H1 survive aggressive knowledge decay?")

    decay_rates = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05]
    results = {}

    for rate in decay_rates:
        results[str(rate)] = {}
        for scenario in [LearningScenario.NONE, LearningScenario.NEIGHBOR, LearningScenario.GLOBAL]:
            label = scenario.name
            print(f"\n  Running decay={rate}, {label}...", end=" ", flush=True)
            params = {**BASE_PARAMS, "knowledge_decay": rate, "learning_scenario": scenario}
            r = aggregate(run_with_seeds(params, seeds))
            results[str(rate)][label] = r
            print(f"Done. Incidents: {r['total_incidents']['mean']:.1f}")

    print("\n  RESULTS SUMMARY:")
    print("  " + "-" * 65)
    print(f"  {'Decay':<10} {'NONE':>10} {'NEIGHBOR':>10} {'GLOBAL':>10} {'H1?':>6}")
    print("  " + "-" * 65)
    for rate in decay_rates:
        r = results[str(rate)]
        none_i = r["NONE"]["total_incidents"]["mean"]
        neighbor_i = r["NEIGHBOR"]["total_incidents"]["mean"]
        global_i = r["GLOBAL"]["total_incidents"]["mean"]
        h1 = "✓" if none_i > neighbor_i > global_i else "✗"
        print(f"  {rate:<10} {none_i:>10.1f} {neighbor_i:>10.1f} {global_i:>10.1f} {h1:>6}")

    save_results("publication_decay_rate_sweep", results)
    return results


# ==============================================================================
# 5. H3 500-Seed Rerun
# ==============================================================================

def sweep_h3_500seeds(seeds_500):
    print("\n" + "=" * 70)
    print("PUBLICATION TEST: H3 Exploitation Effectiveness — 500 Seeds")
    print("Sweep: prevention_effect = [0.0, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5]")
    print("=" * 70)
    print("  Extended range (adds 0.2 and 0.5) to find saturation zone.")
    print("  Question: Is the linear finding real, or did 100 seeds miss sublinear signal?")

    effect_levels = [0.0, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5]
    results = {}

    for effect in effect_levels:
        print(f"\n  Running prevention_effect={effect} ({len(seeds_500)} seeds)...", end=" ", flush=True)
        params = {**BASE_PARAMS, "prevention_effect": effect}
        r = aggregate(run_with_seeds(params, seeds_500))
        results[str(effect)] = r
        print(f"Done. Incidents: {r['total_incidents']['mean']:.1f}")

    print("\n  RESULTS SUMMARY:")
    print("  " + "-" * 55)
    prev_inc = None
    for effect in effect_levels:
        inc = results[str(effect)]["total_incidents"]["mean"]
        delta = f"  Δ={inc - prev_inc:+.1f}" if prev_inc is not None else ""
        print(f"  effect={effect:<5}  incidents={inc:>7.1f}{delta}")
        prev_inc = inc

    # Check if sublinear (diminishing returns)
    deltas = []
    incs = [results[str(e)]["total_incidents"]["mean"] for e in effect_levels]
    for i in range(1, len(incs)):
        step = effect_levels[i] - effect_levels[i-1]
        deltas.append((incs[i] - incs[i-1]) / step if step > 0 else 0)

    print(f"\n  Slope analysis (incidents per unit effect):")
    for i, (effect, delta) in enumerate(zip(effect_levels[1:], deltas)):
        print(f"  At effect={effect}: slope={delta:.1f}")

    if all(deltas[i] >= deltas[i-1] for i in range(1, len(deltas))):
        print("  → Relationship is LINEAR or accelerating (H3 rejected)")
    else:
        print("  → Diminishing returns detected (H3 supported)")

    save_results("publication_h3_500seeds", results)
    return results


# ==============================================================================
# 6. Documentation Quality × Scenario Interaction
# ==============================================================================

def sweep_doc_quality_interaction(seeds):
    print("\n" + "=" * 70)
    print("PUBLICATION TEST: Documentation Quality × Scenario Interaction")
    print("doc_quality = [0.1, 0.5, 0.9] × all 4 scenarios")
    print("=" * 70)
    print("  Question: Does poor postmortem quality cancel out global sharing benefit?")

    doc_levels = [0.1, 0.5, 0.9]
    results = {}

    for doc_q in doc_levels:
        results[str(doc_q)] = {}
        for scenario in LearningScenario:
            label = scenario.name
            print(f"\n  Running doc_quality={doc_q}, {label}...", end=" ", flush=True)
            params = {**BASE_PARAMS, "documentation_quality": doc_q, "learning_scenario": scenario}
            r = aggregate(run_with_seeds(params, seeds))
            results[str(doc_q)][label] = r
            print(f"Done. Incidents: {r['total_incidents']['mean']:.1f}")

    print("\n  RESULTS SUMMARY (mean incidents):")
    print("  " + "-" * 65)
    print(f"  {'Doc Quality':<14} {'NONE':>10} {'LOCAL':>10} {'NEIGHBOR':>10} {'GLOBAL':>10}")
    print("  " + "-" * 65)
    for doc_q in doc_levels:
        r = results[str(doc_q)]
        none_i = r["NONE"]["total_incidents"]["mean"]
        local_i = r["LOCAL"]["total_incidents"]["mean"]
        neighbor_i = r["NEIGHBOR"]["total_incidents"]["mean"]
        global_i = r["GLOBAL"]["total_incidents"]["mean"]
        print(f"  {doc_q:<14} {none_i:>10.1f} {local_i:>10.1f} {neighbor_i:>10.1f} {global_i:>10.1f}")

    print("\n  INTERACTION: GLOBAL benefit at low vs high doc quality:")
    for doc_q in doc_levels:
        r = results[str(doc_q)]
        none_i = r["NONE"]["total_incidents"]["mean"]
        global_i = r["GLOBAL"]["total_incidents"]["mean"]
        benefit_pct = (none_i - global_i) / none_i * 100
        print(f"  doc={doc_q}: GLOBAL saves {none_i - global_i:.1f} incidents ({benefit_pct:.1f}% vs NONE)")

    save_results("publication_doc_quality_interaction", results)
    return results


# ==============================================================================
# 7. Base Incident Rate Sweep
# ==============================================================================

def sweep_base_incident_rate(seeds):
    print("\n" + "=" * 70)
    print("PUBLICATION TEST: Base Incident Rate Sweep")
    print("Sweep: base_incident_rate = [0.01, 0.02, 0.05, 0.1, 0.2]")
    print("=" * 70)
    print("  Question: Does H1 hold when incidents are rare (slow learning)?")
    print("  Does GLOBAL advantage shrink when incidents are frequent (fast learning)?")

    rates = [0.01, 0.02, 0.05, 0.1, 0.2]
    results = {}

    for rate in rates:
        results[str(rate)] = {}
        for scenario in LearningScenario:
            label = scenario.name
            print(f"\n  Running base_incident_rate={rate}, {label}...", end=" ", flush=True)
            params = {**BASE_PARAMS, "base_incident_rate": rate, "learning_scenario": scenario}
            r = aggregate(run_with_seeds(params, seeds))
            results[str(rate)][label] = r
            print(f"Done. Incidents: {r['total_incidents']['mean']:.1f}")

    print("\n  RESULTS SUMMARY:")
    print("  " + "-" * 65)
    print(f"  {'Rate':<8} {'NONE':>10} {'LOCAL':>10} {'NEIGHBOR':>10} {'GLOBAL':>10} {'H1?':>6}")
    print("  " + "-" * 65)
    for rate in rates:
        r = results[str(rate)]
        none_i = r["NONE"]["total_incidents"]["mean"]
        local_i = r["LOCAL"]["total_incidents"]["mean"]
        neighbor_i = r["NEIGHBOR"]["total_incidents"]["mean"]
        global_i = r["GLOBAL"]["total_incidents"]["mean"]
        h1 = "✓" if none_i > local_i > neighbor_i > global_i else "✗"
        print(f"  {rate:<8} {none_i:>10.1f} {local_i:>10.1f} {neighbor_i:>10.1f} {global_i:>10.1f} {h1:>6}")

    save_results("publication_base_incident_rate", results)
    return results


# ==============================================================================
# MAIN
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="Publication-level tests")
    parser.add_argument(
        "--sweep", "-s",
        choices=["duration", "ba_m", "ws_k", "decay_rate", "h3_500seeds",
                 "doc_quality_interaction", "base_incident_rate", "all"],
        default="all",
    )
    parser.add_argument("--quick", action="store_true", help="5 seeds for fast check")
    args = parser.parse_args()

    seeds = list(range(5 if args.quick else NUM_SEEDS))
    seeds_500 = list(range(5 if args.quick else 500))

    print(f"Seeds: {len(seeds)} (H3 rerun: {len(seeds_500)}) | Sweep: {args.sweep}")

    sweep_map = {
        "duration": lambda s: sweep_duration(s),
        "ba_m": lambda s: sweep_ba_m(s),
        "ws_k": lambda s: sweep_ws_k(s),
        "decay_rate": lambda s: sweep_decay_rate(s),
        "h3_500seeds": lambda s: sweep_h3_500seeds(seeds_500),
        "doc_quality_interaction": lambda s: sweep_doc_quality_interaction(s),
        "base_incident_rate": lambda s: sweep_base_incident_rate(s),
    }

    if args.sweep == "all":
        for fn in sweep_map.values():
            fn(seeds)
    else:
        sweep_map[args.sweep](seeds)


if __name__ == "__main__":
    main()
