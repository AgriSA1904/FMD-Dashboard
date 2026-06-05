"""Append MPO Week 32 dairy cows vaccinated data (5 June 2026).
WC: 158 127 (up from 150 116 +8 011)
EC: 297 793 (up from 269 211 +28 582)
All other provinces unchanged from Week 31.
"""
import csv, os

ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "master_data.csv")

EFFDT = "2026-06-05"
SRC   = "WhatsApp MPO Week 32 - 5 June 2026"
ORG   = "MPO"
SUB   = "2026-06-05"
TODAY = "2026-06-05"

# KZN, EC, FS, LP, GP, MP, NW, WC, NC — carry forward unchanged from Week 31 except WC and EC
provinces = [
    ("KZN", "360200", "Unchanged from Week 31 (360200). All KZN dairy animals vaccinated."),
    ("EC",  "297793", "MPO Week 32 (5 Jun 2026): EC dairy cows vaccinated. Up from 269211 (+28582). Source: WhatsApp from MPO."),
    ("FS",  "15104",  "Unchanged from Week 31 (15104)."),
    ("LP",  "5475",   "Unchanged from Week 31 (5475)."),
    ("GP",  "14832",  "Unchanged from Week 31 (14832)."),
    ("MP",  "9863",   "Unchanged from Week 31 (9863)."),
    ("NW",  "6342",   "Unchanged from Week 31 (6342)."),
    ("WC",  "158127", "MPO Week 32 (5 Jun 2026): WC dairy cows vaccinated. Up from 150116 (+8011). Source: WhatsApp from MPO."),
    ("NC",  "0",      "Unchanged from Week 31 (0)."),
]

# KZN 360200 + EC 297793 + FS 15104 + LP 5475 + GP 14832 + MP 9863 + NW 6342 + WC 158127 + NC 0
national = 360200 + 297793 + 15104 + 5475 + 14832 + 9863 + 6342 + 158127 + 0
print(f"National total Week 32: {national:,}")

new_rows = []
for code, val, note in provinces:
    new_rows.append([EFFDT, code, "vaccine_admin", "dairy_cows_vaccinated", "all", "total",
                     val, "dairy cows", SRC, ORG, SUB, TODAY, "1", "", note])

new_rows.append([EFFDT, "national", "vaccine_admin", "dairy_cows_vaccinated", "all", "total",
                 str(national), "dairy cows", SRC, ORG, SUB, TODAY, "1", "",
                 f"MPO Week 32 (5 Jun 2026): national total. Sum: KZN 360200 + EC 297793 + FS 15104 + LP 5475 + GP 14832 + MP 9863 + NW 6342 + WC 158127 + NC 0 = {national}."])

with open(MASTER, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    for r in new_rows:
        w.writerow(r)

with open(MASTER, "r", encoding="utf-8") as f:
    count = sum(1 for _ in f)
print(f"Done. master_data.csv now has {count} lines ({count - 1} data rows).")
