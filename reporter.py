"""
ESG Gap Analysis Report Generator
Outputs structured CSV data and a formatted executive summary.
Author: Amra Gadzo | github.com/Amuritacy
"""

import csv
import os
from datetime import date
from typing import Dict
from analyzer import FrameworkResult


def generate_csv(results: Dict[str, FrameworkResult], output_dir: str = "outputs") -> str:
    """Export all gap items to CSV for further analysis in Excel / Power BI."""
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, f"esg_gap_analysis_{date.today()}.csv")

    fieldnames = [
        "Framework", "Category", "Requirement",
        "Disclosed", "Quality Score (0-3)", "Quality Label",
        "Priority", "Score (%)", "Notes",
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for framework, result in results.items():
            for gap in result.gaps:
                writer.writerow({
                    "Framework":            gap.framework,
                    "Category":             gap.category,
                    "Requirement":          gap.requirement,
                    "Disclosed":            "Yes" if gap.disclosed else "No",
                    "Quality Score (0-3)":  gap.quality,
                    "Quality Label":        gap.quality_label,
                    "Priority":             gap.priority,
                    "Score (%)":            gap.score_pct,
                    "Notes":                gap.notes,
                })

    return filepath


def generate_text_report(
    results: Dict[str, FrameworkResult],
    company_name: str,
    output_dir: str = "reports",
) -> str:
    """Generate a formatted executive-level gap analysis report."""
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, f"esg_report_{date.today()}.txt")
    today = date.today().strftime("%d %B %Y")

    with open(filepath, "w", encoding="utf-8") as f:
        _write = lambda s="": f.write(s + "\n")

        _write("=" * 72)
        _write(f"  ESG REGULATORY GAP ANALYSIS REPORT")
        _write(f"  {company_name}")
        _write(f"  Generated: {today}")
        _write("=" * 72)
        _write()

        # Executive summary table
        _write("EXECUTIVE SUMMARY")
        _write("-" * 72)
        _write(f"{'Framework':<20} {'Requirements':>14} {'Disclosed':>10} {'Rate':>8} {'Avg Quality':>12} {'Critical Gaps':>14}")
        _write("-" * 72)
        for name, result in results.items():
            _write(
                f"{name:<20} {result.total_requirements:>14} "
                f"{result.disclosed_count:>10} {result.disclosure_rate:>7.1f}% "
                f"{result.avg_quality_score:>11.1f}% "
                f"{len(result.critical_gaps):>14}"
            )
        _write("-" * 72)
        _write()

        # Per-framework detail
        for name, result in results.items():
            _write()
            _write("=" * 72)
            _write(f"  {name} — DETAILED FINDINGS")
            _write("=" * 72)

            # Category scores
            _write()
            _write("Category Scores:")
            _write("-" * 50)
            for cat, score in result.scores_by_category.items():
                bar = "█" * int(score / 5) + "░" * (20 - int(score / 5))
                _write(f"  {cat[:35]:<35} {bar} {score:>5.1f}%")

            # Critical gaps
            if result.critical_gaps:
                _write()
                _write(f"CRITICAL GAPS ({len(result.critical_gaps)} items — immediate action required):")
                _write("-" * 72)
                for gap in result.critical_gaps:
                    _write(f"  ✗  [{gap.category}]")
                    _write(f"     {gap.requirement}")
                    _write(f"     → {gap.notes}")
                    _write()

            # High priority gaps
            if result.high_priority_gaps:
                _write(f"HIGH PRIORITY GAPS ({len(result.high_priority_gaps)} items — partial disclosures to strengthen):")
                _write("-" * 72)
                for gap in result.high_priority_gaps:
                    _write(f"  ▲  [{gap.category}]")
                    _write(f"     {gap.requirement}")
                    _write(f"     → {gap.notes}")
                    _write()

        # Recommendations
        _write()
        _write("=" * 72)
        _write("  PRIORITISED RECOMMENDATIONS")
        _write("=" * 72)
        _write()

        all_critical = [
            (fw, gap)
            for fw, result in results.items()
            for gap in result.critical_gaps
        ]

        if all_critical:
            _write("IMMEDIATE ACTIONS (Critical — Missing Disclosures):")
            _write("-" * 72)
            for i, (fw, gap) in enumerate(all_critical[:10], 1):
                _write(f"  {i:>2}. [{fw}] {gap.requirement}")
                _write(f"      Category: {gap.category}")
                _write()

        _write()
        _write("─" * 72)
        _write("Report generated by ESG Gap Analysis Tool | github.com/Amuritacy")
        _write("─" * 72)

    return filepath


def print_summary(results: Dict[str, FrameworkResult], company_name: str) -> None:
    """Print a concise summary to the console."""
    print("\n" + "=" * 60)
    print(f"  ESG GAP ANALYSIS — {company_name.upper()}")
    print("=" * 60)

    for name, result in results.items():
        print(f"\n  {name}")
        print(f"  {'─' * 40}")
        print(f"  Disclosure rate:  {result.disclosure_rate:.1f}%")
        print(f"  Avg quality:      {result.avg_quality_score:.1f}%")
        print(f"  Critical gaps:    {len(result.critical_gaps)}")
        print(f"  High priority:    {len(result.high_priority_gaps)}")

        if result.critical_gaps:
            print(f"\n  Top critical gaps:")
            for gap in result.critical_gaps[:3]:
                print(f"    ✗ {gap.requirement}")

    print("\n" + "=" * 60 + "\n")
