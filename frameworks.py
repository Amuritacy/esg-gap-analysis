"""
ESG Regulatory Frameworks
Defines disclosure requirements for CSRD, EU Taxonomy, and SFDR.
Author: Amra Gadzo | github.com/Amuritacy
"""

CSRD_REQUIREMENTS = {
    "Environment": {
        "E1 - Climate Change": [
            "GHG emissions (Scope 1, 2, 3)",
            "Climate transition plan",
            "Physical climate risks assessment",
            "Energy consumption and mix",
            "Carbon removal and storage",
        ],
        "E2 - Pollution": [
            "Air pollutant emissions",
            "Water pollutant emissions",
            "Hazardous substance management",
            "Microplastics impact",
        ],
        "E3 - Water & Marine": [
            "Water consumption",
            "Water recycling rate",
            "Marine ecosystem impact",
        ],
        "E4 - Biodiversity": [
            "Biodiversity strategy",
            "Land use and degradation",
            "Species impact assessment",
        ],
        "E5 - Resource Use": [
            "Resource inflows (materials, water, energy)",
            "Resource outflows (waste, emissions)",
            "Circular economy strategy",
        ],
    },
    "Social": {
        "S1 - Own Workforce": [
            "Headcount and employment types",
            "Gender pay gap",
            "Health & safety incidents",
            "Training hours per employee",
            "Collective bargaining coverage",
        ],
        "S2 - Value Chain Workers": [
            "Supply chain due diligence",
            "Living wage assessment",
            "Child and forced labour risks",
        ],
        "S3 - Affected Communities": [
            "Community engagement processes",
            "Indigenous peoples' rights",
            "Socioeconomic impact assessment",
        ],
        "S4 - Consumers & End-users": [
            "Product safety incidents",
            "Data privacy breaches",
            "Responsible marketing policy",
        ],
    },
    "Governance": {
        "G1 - Business Conduct": [
            "Anti-corruption policy",
            "Whistleblowing mechanisms",
            "Political engagement and lobbying",
            "Supplier payment practices",
            "Animal welfare policy",
        ],
    },
}

EU_TAXONOMY_CRITERIA = {
    "Climate Change Mitigation": {
        "description": "Activities that contribute to stabilising GHG concentrations",
        "screening_criteria": [
            "Substantial contribution to climate mitigation",
            "Do No Significant Harm (DNSH) to other 5 objectives",
            "Minimum social safeguards compliance",
            "Technical Screening Criteria (TSC) alignment",
        ],
        "key_metrics": [
            "Taxonomy-aligned revenue (%)",
            "Taxonomy-aligned capex (%)",
            "Taxonomy-aligned opex (%)",
            "GHG intensity (tCO2e / €M revenue)",
        ],
    },
    "Climate Change Adaptation": {
        "description": "Activities that reduce adverse impacts of current and future climate",
        "screening_criteria": [
            "Climate risk and vulnerability assessment",
            "Adaptation solutions implementation",
            "No significant harm to other objectives",
        ],
        "key_metrics": [
            "Physical risk exposure score",
            "Adaptation measure investment (€)",
            "Assets at risk ratio (%)",
        ],
    },
    "Sustainable Use of Water": {
        "description": "Conservation and sustainable use of water and marine resources",
        "screening_criteria": [
            "Water stress area identification",
            "Water efficiency improvement",
            "Wastewater treatment standards",
        ],
        "key_metrics": [
            "Water withdrawal (m³)",
            "Water recycled/reused (%)",
            "Water in stressed areas (%)",
        ],
    },
    "Circular Economy": {
        "description": "Transition to circular economy including waste prevention",
        "screening_criteria": [
            "Waste prevention and minimisation",
            "Reuse and recycling rate",
            "Hazardous substance phase-out",
        ],
        "key_metrics": [
            "Waste diverted from landfill (%)",
            "Recycled material input (%)",
            "Product recyclability (%)",
        ],
    },
    "Pollution Prevention": {
        "description": "Prevention and control of pollution",
        "screening_criteria": [
            "Emissions below EU regulatory thresholds",
            "Best Available Techniques compliance",
            "Chemical substances management",
        ],
        "key_metrics": [
            "NOx / SOx emissions (tonnes)",
            "Hazardous waste generated (tonnes)",
            "Sites with pollution incidents",
        ],
    },
    "Biodiversity & Ecosystems": {
        "description": "Protection and restoration of biodiversity and ecosystems",
        "screening_criteria": [
            "No net loss of biodiversity",
            "Protected area impact assessment",
            "Ecosystem services valuation",
        ],
        "key_metrics": [
            "Sites in/near protected areas",
            "Land use change (hectares)",
            "Biodiversity net gain score",
        ],
    },
}

SFDR_REQUIREMENTS = {
    "Entity-Level (Article 3-5)": [
        "Sustainability risk integration policy",
        "Principal Adverse Impacts (PAI) statement",
        "Remuneration policy alignment with sustainability risks",
    ],
    "Product-Level": {
        "Article 6 (No sustainability claim)": [
            "Sustainability risk disclosure",
            "Statement on PAI consideration (or explanation of non-consideration)",
        ],
        "Article 8 (ESG characteristics promoted)": [
            "Description of ESG characteristics",
            "Proportion of sustainable investments",
            "Good governance assessment methodology",
            "Pre-contractual disclosure template (Annex II)",
            "Periodic reporting template (Annex III)",
        ],
        "Article 9 (Sustainable investment objective)": [
            "Sustainable investment objective description",
            "Do No Significant Harm methodology",
            "Principal Adverse Impacts integration",
            "Pre-contractual disclosure template (Annex IV)",
            "Periodic reporting template (Annex V)",
        ],
    },
    "PAI Indicators (Mandatory)": [
        "GHG emissions (Scope 1, 2, 3)",
        "Carbon footprint",
        "GHG intensity of investee companies",
        "Fossil fuel sector exposure",
        "Non-renewable energy consumption",
        "Energy consumption intensity",
        "Biodiversity-sensitive area activities",
        "Water emissions",
        "Hazardous waste ratio",
        "Violations of UN Global Compact / OECD Guidelines",
        "Lack of UNGC/OECD compliance processes",
        "Unadjusted gender pay gap",
        "Board gender diversity",
        "Exposure to controversial weapons",
    ],
}
