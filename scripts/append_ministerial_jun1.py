"""Append 1 June 2026 ministerial provincial rows to master_data.csv."""
import csv, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "master_data.csv")

TODAY = "2026-06-05"
SRC   = "Minister_Steenhuisen_1Jun2026_press_statement.pdf"
ORG   = "Ministry"
SUB   = "2026-06-01"

new_rows = [
    ["2026-05-28","national","animals_vaccinated","animals_vaccinated_ministerial","all","all","4400000","count",SRC,ORG,SUB,TODAY,"1","","All animals vaccinated as at 28 May 2026; floor estimate from ministerial briefing 1 June 2026 (Parliament)"],
    ["2026-06-01","national","vaccine_receipt","doses_procured","all","all","13500000","doses",SRC,ORG,SUB,TODAY,"1","","Total doses procured from manufacturers into South Africa; ministerial briefing 1 June 2026 (Parliament)"],
    ["2026-05-28","KZN","animals_vaccinated","cattle_vaccinated_ministerial","all","all","1100000","count",SRC,ORG,SUB,TODAY,"1","","KZN floor estimate: more than 1.1 million animals vaccinated as at 28 May 2026; ministerial briefing 1 June 2026"],
    ["2026-05-28","EC","animals_vaccinated","cattle_vaccinated_ministerial","all","all","720000","count",SRC,ORG,SUB,TODAY,"1","","EC floor estimate: more than 720 000 animals vaccinated as at 28 May 2026; ministerial briefing 1 June 2026"],
    ["2026-05-28","FS","animals_vaccinated","cattle_vaccinated_ministerial","all","all","600000","count",SRC,ORG,SUB,TODAY,"1","","FS floor estimate: more than 600 000 animals vaccinated as at 28 May 2026; ministerial briefing 1 June 2026"],
    ["2026-05-28","MP","animals_vaccinated","cattle_vaccinated_ministerial","all","all","430000","count",SRC,ORG,SUB,TODAY,"1","","MP floor estimate: more than 430 000 animals vaccinated as at 28 May 2026; ministerial briefing 1 June 2026"],
    ["2026-05-28","NW","animals_vaccinated","cattle_vaccinated_ministerial","all","all","430000","count",SRC,ORG,SUB,TODAY,"1","","NW floor estimate: more than 430 000 as at 28 May 2026; press release shows 430 00 interpreted as 430 000"],
    ["2026-05-28","LP","animals_vaccinated","cattle_vaccinated_ministerial","all","all","350000","count",SRC,ORG,SUB,TODAY,"1","","LP floor estimate: more than 350 000 animals vaccinated as at 28 May 2026; ministerial briefing 1 June 2026"],
    ["2026-05-28","GP","animals_vaccinated","cattle_vaccinated_ministerial","all","all","270000","count",SRC,ORG,SUB,TODAY,"1","","GP floor estimate: more than 270 000 animals vaccinated as at 28 May 2026; ministerial briefing 1 June 2026"],
    ["2026-05-28","WC","animals_vaccinated","cattle_vaccinated_ministerial","all","all","260000","count",SRC,ORG,SUB,TODAY,"1","","WC floor estimate: more than 260 000 animals vaccinated as at 28 May 2026; ministerial briefing 1 June 2026"],
    ["2026-05-28","NC","animals_vaccinated","cattle_vaccinated_ministerial","all","all","87000","count",SRC,ORG,SUB,TODAY,"1","","NC floor estimate: more than 87 000 animals vaccinated as at 28 May 2026; ministerial briefing 1 June 2026"],
]

with open(MASTER, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    for r in new_rows:
        w.writerow(r)

with open(MASTER, "r", encoding="utf-8") as f:
    count = sum(1 for _ in f)
print(f"Done. master_data.csv now has {count} lines ({count-1} data rows).")
