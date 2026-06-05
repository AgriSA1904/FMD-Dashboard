"""Supersede stale doses_incoming rows from 5 May briefing.
Both have now arrived; they are replaced by the hardcoded pipeline in build_dashboard.py."""
import csv, os

ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "master_data.csv")

with open(MASTER, "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

header = list(rows[0].keys())
updated = 0
for r in rows:
    if (r["metric"] == "doses_incoming"
            and r["source_org"] == "Ministry"
            and r["superseded_by"] == ""):
        r["superseded_by"] = "pipeline-hardcoded-in-build-1jun2026"
        updated += 1

with open(MASTER, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=header)
    w.writeheader()
    w.writerows(rows)

print(f"Superseded {updated} old doses_incoming rows.")
