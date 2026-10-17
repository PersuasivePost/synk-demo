#!/usr/bin/env python3
"""Compare Snyk scan results before vs after remediation.

Reads results/{before,after}-{deps,image}.json (created by scripts/scan.sh),
prints a Markdown table, and saves results/comparison.png and results/summary.md.

Usage:  python3 scripts/compare.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
SEVERITIES = ["critical", "high", "medium", "low"]


def count_unique(path: Path) -> dict:
    """Count unique vulnerability IDs per severity in a Snyk JSON report."""
    data = json.loads(path.read_text())
    reports = data if isinstance(data, list) else [data]  # multi-project scans return a list
    seen = {s: set() for s in SEVERITIES}
    for rep in reports:
        for v in rep.get("vulnerabilities", []):
            sev = v.get("severity", "low")
            if sev in seen:
                seen[sev].add(v.get("id"))
    counts = {s: len(ids) for s, ids in seen.items()}
    counts["total"] = sum(counts.values())
    return counts


def main() -> int:
    files = {
        ("Dependencies (npm)", "before"): RESULTS / "before-deps.json",
        ("Dependencies (npm)", "after"): RESULTS / "after-deps.json",
        ("Docker image", "before"): RESULTS / "before-image.json",
        ("Docker image", "after"): RESULTS / "after-image.json",
    }
    missing = [str(p.name) for p in files.values() if not p.exists()]
    if missing:
        print("Missing report(s):", ", ".join(missing))
        print("Run: bash scripts/scan.sh before   and   bash scripts/scan.sh after")
        return 1

    counts = {k: count_unique(p) for k, p in files.items()}

    lines = ["| Target | Version | Critical | High | Medium | Low | Total |",
             "|---|---|---:|---:|---:|---:|---:|"]
    for target in ("Dependencies (npm)", "Docker image"):
        for ver in ("before", "after"):
            c = counts[(target, ver)]
            lines.append(f"| {target} | {ver} | {c['critical']} | {c['high']} | "
                         f"{c['medium']} | {c['low']} | **{c['total']}** |")
        b, a = counts[(target, "before")]["total"], counts[(target, "after")]["total"]
        reduction = 100 * (b - a) / b if b else 0
        lines.append(f"| {target} | _reduction_ | | | | | _{reduction:.0f}%_ |")
    table = "\n".join(lines)
    print(table)
    (RESULTS / "summary.md").write_text(table + "\n")

    # ---- chart ----
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("\n(matplotlib not installed - skipping chart. pip install matplotlib)")
        return 0

    colors = {"critical": "#7f1d1d", "high": "#dc2626", "medium": "#f59e0b", "low": "#60a5fa"}
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for ax, target in zip(axes, ("Dependencies (npm)", "Docker image")):
        labels = ["Before", "After"]
        bottoms = [0, 0]
        for sev in SEVERITIES:
            vals = [counts[(target, "before")][sev], counts[(target, "after")][sev]]
            ax.bar(labels, vals, bottom=bottoms, label=sev.capitalize(), color=colors[sev], width=0.55)
            bottoms = [b + v for b, v in zip(bottoms, vals)]
        for i, tot in enumerate(bottoms):
            ax.text(i, tot, str(tot), ha="center", va="bottom", fontweight="bold")
        ax.set_title(target)
        ax.set_ylabel("Unique vulnerabilities")
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].legend(frameon=False)
    fig.suptitle("Snyk scan: vulnerabilities before vs after remediation", fontweight="bold")
    fig.tight_layout()
    fig.savefig(RESULTS / "comparison.png", dpi=160)
    print(f"\nSaved {RESULTS / 'comparison.png'} and {RESULTS / 'summary.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
