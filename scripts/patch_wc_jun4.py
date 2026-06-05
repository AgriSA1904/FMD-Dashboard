"""Patch Western Cape figures from WC GIS portal as at 4 June 2026."""
import csv, os

ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "master_data.csv")

TODAY  = "2026-06-05"
EFFDT  = "2026-06-04"
SRC    = "WC GIS Portal (gis.westerncape.gov.za) — Claude in Chrome live read, 5 Jun 2026"
ORG    = "WC-GIS"
SUB    = "2026-06-05"

new_rows = [
    [EFFDT, "WC", "disease",           "positive_cases",      "all", "all", "33",     "count", SRC, ORG, SUB, TODAY, "1", "", "WC GIS Portal live read 5 Jun 2026. Up from 22. Last updated 4 June 2026 per portal."],
    [EFFDT, "WC", "vaccine_receipt",   "doses_received",      "all", "all", "430140", "doses", SRC, ORG, SUB, TODAY, "1", "", "WC GIS Portal: Vaccines Received as at 4 June 2026. Up from 330 340."],
    [EFFDT, "WC", "animals_vaccinated","animals_vaccinated",   "all", "all", "279301", "count", SRC, ORG, SUB, TODAY, "1", "", "WC GIS Portal: Vaccinations (animals) as at 4 June 2026. Up from 231 913."],
    [EFFDT, "WC", "operations",        "vaccination_sites",   "all", "all", "1204",   "count", SRC, ORG, SUB, TODAY, "1", "", "WC GIS Portal: active vaccination sites as at 4 June 2026."],
    [EFFDT, "WC", "operations",        "private_vets_active",  "all", "all", "29",     "count", SRC, ORG, SUB, TODAY, "1", "", "WC GIS Portal: private vets vaccinating as at 4 June 2026."],
]

with open(MASTER, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    for r in new_rows:
        w.writerow(r)

with open(MASTER, "r", encoding="utf-8") as f:
    count = sum(1 for _ in f)
print(f"Done. master_data.csv now has {count} lines ({count - 1} data rows).")
