"""
ESG Regulatory Gap Analysis Tool
Maps corporate disclosures against CSRD, EU Taxonomy, and SFDR requirements.

Usage:
    python main.py                  # Run with sample data
    python main.py --company "Your Company AG"

Author: Amra Gadzo | github.com/Amuritacy
"""

import argparse
from analyzer import run_full_analysis
from reporter import generate_csv, generate_text_report, print_summary
from sample_data import (
    SAMPLE_COMPANY,
    CSRD_DISCLOSURES,
    EU_TAXONOMY_DISCLOSURES,
    SFDR_DISCLOSURES,
)


def main(company_name: str = None):
    name = company_name or SAMPLE_COMPANY["name"]

    print(f"\nRunning ESG gap analysis for: {name}")
    print("Frameworks: CSRD · EU Taxonomy · SFDR\n")

    # Run analysis
    results = run_full_analysis(
        csrd_data=CSRD_DISCLOSURES,
        taxonomy_data=EU_TAXONOMY_DISCLOSURES,
        sfdr_data=SFDR_DISCLOSURES,
    )

    # Console summary
    print_summary(results, name)

    # Export CSV
    csv_path = generate_csv(results)
    print(f"  CSV exported:    {csv_path}")

    # Export text report
    report_path = generate_text_report(results, name)
    print(f"  Report exported: {report_path}")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ESG Regulatory Gap Analysis Tool")
    parser.add_argument(
        "--company",
        type=str,
        default=None,
        help="Company name to use in the report",
    )
    args = parser.parse_args()
    main(args.company)
