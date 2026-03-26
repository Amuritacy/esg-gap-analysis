"""
ESG Gap Analysis Engine
Scores disclosures against CSRD, EU Taxonomy, and SFDR requirements.
Author: Amra Gadzo | github.com/Amuritacy
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple
from frameworks import CSRD_REQUIREMENTS, EU_TAXONOMY_CRITERIA, SFDR_REQUIREMENTS


QUALITY_LABELS = {
    0: "Missing",
    1: "Partial",
    2: "Adequate",
    3: "Best Practice",
}

PRIORITY_THRESHOLDS = {
    "Critical":  0,   # quality == 0 (missing)
    "High":      1,   # quality == 1 (partial)
    "Medium":    2,   # quality == 2 (adequate but improvable)
}


@dataclass
class GapItem:
    requirement: str
    framework: str
    category: str
    disclosed: bool
    quality: int
    quality_label: str
    notes: str
    priority: str

    @property
    def score_pct(self) -> float:
        return round((self.quality / 3) * 100, 1)


@dataclass
class FrameworkResult:
    framework: str
    total_requirements: int
    disclosed_count: int
    gaps: List[GapItem] = field(default_factory=list)
    scores_by_category: Dict[str, float] = field(default_factory=dict)

    @property
    def disclosure_rate(self) -> float:
        return round((self.disclosed_count / self.total_requirements) * 100, 1)

    @property
    def avg_quality_score(self) -> float:
        if not self.gaps:
            return 0.0
        return round(sum(g.quality for g in self.gaps) / (len(self.gaps) * 3) * 100, 1)

    @property
    def critical_gaps(self) -> List[GapItem]:
        return [g for g in self.gaps if g.priority == "Critical"]

    @property
    def high_priority_gaps(self) -> List[GapItem]:
        return [g for g in self.gaps if g.priority == "High"]


def _priority(quality: int) -> str:
    if quality == 0:
        return "Critical"
    if quality == 1:
        return "High"
    return "Medium"


def analyze_csrd(disclosures: dict) -> FrameworkResult:
    """Score disclosures against CSRD ESRS requirements."""
    gaps = []
    scores_by_category = {}

    for topic, categories in CSRD_REQUIREMENTS.items():
        for category, requirements in categories.items():
            cat_scores = []
            for req in requirements:
                if req in disclosures:
                    disclosed, quality, notes = disclosures[req]
                else:
                    disclosed, quality, notes = False, 0, "Not found in disclosures"

                gap = GapItem(
                    requirement=req,
                    framework="CSRD",
                    category=f"{topic} / {category}",
                    disclosed=disclosed,
                    quality=quality,
                    quality_label=QUALITY_LABELS[quality],
                    notes=notes,
                    priority=_priority(quality),
                )
                gaps.append(gap)
                cat_scores.append(quality)

            avg = round(sum(cat_scores) / (len(cat_scores) * 3) * 100, 1) if cat_scores else 0
            scores_by_category[category] = avg

    disclosed_count = sum(1 for g in gaps if g.disclosed)
    return FrameworkResult(
        framework="CSRD",
        total_requirements=len(gaps),
        disclosed_count=disclosed_count,
        gaps=gaps,
        scores_by_category=scores_by_category,
    )


def analyze_eu_taxonomy(disclosures: dict) -> FrameworkResult:
    """Score disclosures against EU Taxonomy KPI requirements."""
    gaps = []
    scores_by_category = {}

    for objective, data in EU_TAXONOMY_CRITERIA.items():
        if objective not in disclosures:
            continue
        obj_disclosures = disclosures[objective]
        cat_scores = []

        for metric in data["key_metrics"]:
            if metric in obj_disclosures:
                disclosed, quality, notes = obj_disclosures[metric]
            else:
                disclosed, quality, notes = False, 0, "Not reported"

            gap = GapItem(
                requirement=metric,
                framework="EU Taxonomy",
                category=objective,
                disclosed=disclosed,
                quality=quality,
                quality_label=QUALITY_LABELS[quality],
                notes=notes,
                priority=_priority(quality),
            )
            gaps.append(gap)
            cat_scores.append(quality)

        avg = round(sum(cat_scores) / (len(cat_scores) * 3) * 100, 1) if cat_scores else 0
        scores_by_category[objective] = avg

    disclosed_count = sum(1 for g in gaps if g.disclosed)
    return FrameworkResult(
        framework="EU Taxonomy",
        total_requirements=len(gaps),
        disclosed_count=disclosed_count,
        gaps=gaps,
        scores_by_category=scores_by_category,
    )


def analyze_sfdr(disclosures: dict) -> FrameworkResult:
    """Score disclosures against SFDR PAI and entity-level requirements."""
    gaps = []

    all_requirements = (
        SFDR_REQUIREMENTS["Entity-Level (Article 3-5)"]
        + SFDR_REQUIREMENTS["PAI Indicators (Mandatory)"]
    )

    for req in all_requirements:
        if req in disclosures:
            disclosed, quality, notes = disclosures[req]
        else:
            disclosed, quality, notes = False, 0, "Not found in disclosures"

        category = (
            "Entity-Level Disclosures"
            if req in SFDR_REQUIREMENTS["Entity-Level (Article 3-5)"]
            else "PAI Indicators"
        )

        gap = GapItem(
            requirement=req,
            framework="SFDR",
            category=category,
            disclosed=disclosed,
            quality=quality,
            quality_label=QUALITY_LABELS[quality],
            notes=notes,
            priority=_priority(quality),
        )
        gaps.append(gap)

    # Category scores
    scores_by_category: Dict[str, List[int]] = {}
    for g in gaps:
        scores_by_category.setdefault(g.category, []).append(g.quality)

    category_avgs = {
        cat: round(sum(scores) / (len(scores) * 3) * 100, 1)
        for cat, scores in scores_by_category.items()
    }

    disclosed_count = sum(1 for g in gaps if g.disclosed)
    return FrameworkResult(
        framework="SFDR",
        total_requirements=len(gaps),
        disclosed_count=disclosed_count,
        gaps=gaps,
        scores_by_category=category_avgs,
    )


def run_full_analysis(
    csrd_data: dict,
    taxonomy_data: dict,
    sfdr_data: dict,
) -> Dict[str, FrameworkResult]:
    """Run gap analysis across all three frameworks."""
    return {
        "CSRD":        analyze_csrd(csrd_data),
        "EU Taxonomy": analyze_eu_taxonomy(taxonomy_data),
        "SFDR":        analyze_sfdr(sfdr_data),
    }
