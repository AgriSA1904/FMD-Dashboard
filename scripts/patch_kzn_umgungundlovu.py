"""
Ingest KZN DARD media statement 4 June 2026 — uMgungundlovu District completion.
District-level data only; no new KZN provincial total provided.
Source: KZN DARD Facebook media statement, 4 June 2026.
"""
import csv, os

ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "master_data.csv")

EFFDT = "2026-06-04"
SRC   = "KZN DARD Facebook media statement 4 June 2026 - uMgungundlovu district completion"
ORG   = "KZN-DARD"
SUB   = "2026-06-04"
TODAY = "2026-06-05"

# Municipality breakdown — uMgungundlovu District
municipalities = [
    ("Impendle LM",     19660, 9307),
    ("uMgeni LM",        7234, 1762),
    ("Richmond LM",      7951, 3527),
    ("Mkhambathini LM",  7142, 3616),
    ("uMshwathi LM",    10217, 2557),
    ("uMsunduzi LM",    15802, 4719),
    ("Mpofana LM",      16169, 3876),
]

total_vacc   = sum(m[1] for m in municipalities)   # 84 175
total_tagged = sum(m[2] for m in municipalities)   # 29 364
assert total_vacc   == 84175, f"Unexpected total: {total_vacc}"
assert total_tagged == 29364, f"Unexpected tagged: {total_tagged}"

context = (
    "KZN DARD media statement 4 Jun 2026. uMgungundlovu is the 5th KZN district completed "
    "(after Ugu, Harry Gwala, uMkhanyakude, Zululand). 197 dip tanks. 77 commercial farms. "
    "Next: eThekwini Metropolitan — 70 dip tanks, 9-16 June 2026."
)

new_rows = []

# District total
new_rows.append([
    EFFDT, "KZN", "animals_vaccinated", "animals_vaccinated_district", "all", "all",
    str(total_vacc), "count", SRC, ORG, SUB, TODAY, "1", "",
    f"uMgungundlovu District total. {context}"
])

# Eartagged (district)
new_rows.append([
    EFFDT, "KZN", "operations", "animals_eartagged_district", "all", "all",
    str(total_tagged), "count", SRC, ORG, SUB, TODAY, "1", "",
    f"uMgungundlovu District: animals eartagged during vaccination. {context}"
])

# Municipality rows
for name, vacc, tagged in municipalities:
    new_rows.append([
        EFFDT, "KZN", "animals_vaccinated", "animals_vaccinated_district", "all", "all",
        str(vacc), "count", SRC, ORG, SUB, TODAY, "1", "",
        f"uMgungundlovu District — {name}: {vacc} animals vaccinated, {tagged} eartagged. 4 Jun 2026."
    ])

# Operational note — eThekwini upcoming
new_rows.append([
    "2026-06-09", "KZN", "operations", "vaccination_planned", "all", "all",
    "70", "dip tanks", SRC, ORG, SUB, TODAY, "1", "",
    "eThekwini Metropolitan vaccination planned: 70 dip tanks, 9-16 June 2026. "
    "Follows completion of uMgungundlovu (5th district). KZN DARD media statement 4 Jun 2026."
])

with open(MASTER, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    for r in new_rows:
        w.writerow(r)

with open(MASTER, "r", encoding="utf-8") as f:
    count = sum(1 for _ in f)

print(f"Done. {len(new_rows)} rows added. master_data.csv now has {count} lines.")
print(f"uMgungundlovu total: {total_vacc:,} vaccinated | {total_tagged:,} eartagged")
print("NOTE: KZN provincial KPI unchanged — no new provincial total in this statement.")
