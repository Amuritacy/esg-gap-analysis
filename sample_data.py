"""
Sample Corporate ESG Disclosure Data
Simulates a financial institution's current ESG disclosure state.
Author: Amra Gadzo | github.com/Amuritacy
"""

# Each entry: requirement -> (disclosed: bool, quality: 0-3, notes)
# Quality: 0=missing, 1=partial, 2=adequate, 3=best practice

SAMPLE_COMPANY = {
    "name": "Example Financial AG",
    "sector": "Financial Services",
    "reporting_year": 2024,
    "size": "Large (>500 employees)",
    "listed": True,
}

CSRD_DISCLOSURES = {
    # E1
    "GHG emissions (Scope 1, 2, 3)":           (True,  2, "Scope 1&2 reported; Scope 3 partially covered"),
    "Climate transition plan":                   (True,  1, "High-level plan exists, no interim targets"),
    "Physical climate risks assessment":         (False, 0, "Not yet conducted"),
    "Energy consumption and mix":                (True,  2, "Reported in annual report"),
    "Carbon removal and storage":                (False, 0, "No disclosure"),
    # E2
    "Air pollutant emissions":                   (True,  1, "Limited to direct operations only"),
    "Water pollutant emissions":                 (False, 0, "Not disclosed"),
    "Hazardous substance management":            (True,  1, "Policy exists, no quantitative data"),
    "Microplastics impact":                      (False, 0, "Not applicable — not assessed"),
    # E3
    "Water consumption":                         (True,  2, "Office water use reported"),
    "Water recycling rate":                      (False, 0, "Not tracked"),
    "Marine ecosystem impact":                   (False, 0, "Not assessed"),
    # E4
    "Biodiversity strategy":                     (False, 0, "No strategy in place"),
    "Land use and degradation":                  (False, 0, "Not disclosed"),
    "Species impact assessment":                 (False, 0, "Not conducted"),
    # E5
    "Resource inflows (materials, water, energy)":(True,  1, "Energy only; materials not tracked"),
    "Resource outflows (waste, emissions)":       (True,  2, "Waste data reported"),
    "Circular economy strategy":                  (False, 0, "No formal strategy"),
    # S1
    "Headcount and employment types":            (True,  3, "Full breakdown available"),
    "Gender pay gap":                            (True,  2, "Reported at entity level"),
    "Health & safety incidents":                 (True,  3, "LTIFR and TRIFR disclosed"),
    "Training hours per employee":               (True,  2, "Average hours reported"),
    "Collective bargaining coverage":            (True,  1, "Percentage not disclosed"),
    # S2
    "Supply chain due diligence":                (True,  1, "Policy only, no monitoring data"),
    "Living wage assessment":                    (False, 0, "Not conducted"),
    "Child and forced labour risks":             (True,  1, "Policy exists, no audit results"),
    # S3
    "Community engagement processes":            (True,  1, "Ad-hoc, not systematic"),
    "Indigenous peoples' rights":                (False, 0, "Not relevant — not assessed"),
    "Socioeconomic impact assessment":           (False, 0, "Not conducted"),
    # S4
    "Product safety incidents":                  (True,  2, "Complaints data available"),
    "Data privacy breaches":                     (True,  3, "GDPR incident reporting in place"),
    "Responsible marketing policy":              (True,  2, "Policy published"),
    # G1
    "Anti-corruption policy":                    (True,  3, "Comprehensive policy and training"),
    "Whistleblowing mechanisms":                 (True,  3, "Anonymous hotline operational"),
    "Political engagement and lobbying":         (False, 0, "Not disclosed"),
    "Supplier payment practices":                (True,  1, "Average payment terms only"),
    "Animal welfare policy":                     (False, 0, "Not applicable — not assessed"),
}

EU_TAXONOMY_DISCLOSURES = {
    "Climate Change Mitigation": {
        "Taxonomy-aligned revenue (%)":          (True,  2, "32% reported"),
        "Taxonomy-aligned capex (%)":            (True,  2, "41% reported"),
        "Taxonomy-aligned opex (%)":             (True,  1, "Partial methodology disclosure"),
        "GHG intensity (tCO2e / €M revenue)":   (False, 0, "Not calculated"),
    },
    "Climate Change Adaptation": {
        "Physical risk exposure score":          (False, 0, "Assessment not completed"),
        "Adaptation measure investment (€)":     (False, 0, "Not tracked separately"),
        "Assets at risk ratio (%)":              (False, 0, "Not calculated"),
    },
    "Sustainable Use of Water": {
        "Water withdrawal (m³)":                 (True,  2, "Office-level data available"),
        "Water recycled/reused (%)":             (False, 0, "Not tracked"),
        "Water in stressed areas (%)":           (False, 0, "Not assessed"),
    },
    "Circular Economy": {
        "Waste diverted from landfill (%)":      (True,  2, "74% reported"),
        "Recycled material input (%)":           (False, 0, "Not tracked"),
        "Product recyclability (%)":             (False, 0, "Not assessed"),
    },
    "Pollution Prevention": {
        "NOx / SOx emissions (tonnes)":         (False, 0, "Not measured"),
        "Hazardous waste generated (tonnes)":    (True,  1, "Approximate figure only"),
        "Sites with pollution incidents":        (True,  3, "Zero incidents — verified"),
    },
    "Biodiversity & Ecosystems": {
        "Sites in/near protected areas":         (False, 0, "Not mapped"),
        "Land use change (hectares)":            (False, 0, "Not tracked"),
        "Biodiversity net gain score":           (False, 0, "No methodology adopted"),
    },
}

SFDR_DISCLOSURES = {
    "Sustainability risk integration policy":                    (True,  3, "Published on website"),
    "Principal Adverse Impacts (PAI) statement":                (True,  2, "Published, mandatory indicators only"),
    "Remuneration policy alignment with sustainability risks":  (True,  1, "Brief reference only"),
    "GHG emissions (Scope 1, 2, 3)":                           (True,  2, "Scope 3 incomplete"),
    "Carbon footprint":                                          (True,  2, "Entity-level reported"),
    "GHG intensity of investee companies":                      (True,  1, "Partial coverage of portfolio"),
    "Fossil fuel sector exposure":                               (True,  3, "Full portfolio screen done"),
    "Non-renewable energy consumption":                          (True,  2, "Reported"),
    "Energy consumption intensity":                              (False, 0, "Not calculated at portfolio level"),
    "Biodiversity-sensitive area activities":                   (False, 0, "Not assessed"),
    "Water emissions":                                           (False, 0, "Not tracked at portfolio level"),
    "Hazardous waste ratio":                                     (False, 0, "Not reported"),
    "Violations of UN Global Compact / OECD Guidelines":        (True,  2, "Screening tool in use"),
    "Lack of UNGC/OECD compliance processes":                   (True,  1, "Policy only"),
    "Unadjusted gender pay gap":                                (True,  2, "Entity-level data"),
    "Board gender diversity":                                    (True,  3, "40% women on board"),
    "Exposure to controversial weapons":                        (True,  3, "Zero exposure — screened"),
}
