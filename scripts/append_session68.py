#!/usr/bin/env python3
"""Session 68 ingest — 17 Aug 2026.

Sources:
  1. RMIS Industry Allocated FMD Vaccine Distribution Dashboard (Shiny portal,
     live read 17 Aug 2026; portal release date 11 Aug 2026).
  2. Western Cape GIS portal (ArcGIS FeatureServer REST, live query 17 Aug 2026).
  3. Ministerial updates, Minister Willie Aucamp era (Jun-Aug 2026), from
     public statements and press coverage.
"""
import csv, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "master_data.csv")

RMIS_SRC = "rmis.shinyapps.io industry dashboard (live read 17 Aug 2026; release 11 Aug 2026)"
WCGIS_SRC = "WC GIS portal ArcGIS REST live query 17 Aug 2026"
ING = "2026-08-17"

rows = []

def add(effective, province, cat, metric, vtype, channel, value, unit,
        source_file, source_org, submitted, notes):
    rows.append({
        "effective_date": effective, "province": province, "metric_category": cat,
        "metric": metric, "vaccine_type": vtype, "vet_channel": channel,
        "value": value, "unit": unit, "source_file": source_file,
        "source_org": source_org, "submitted_date": submitted,
        "ingested_date": ING, "version": "1", "superseded_by": "", "notes": notes,
    })

# ─────────────────────────────────────────────────────────────────────────────
# 1. RMIS — headline KPIs (release 11 Aug 2026)
# ─────────────────────────────────────────────────────────────────────────────
E = "2026-08-11"
add(E, "national", "vaccine_receipt", "doses_allocated_industry", "all", "private",
    "2900000", "doses", RMIS_SRC, "RMIS", E,
    "RMIS portal release 11 Aug 2026. Vaccine doses allocated to industry, all manufacturers "
    "(ministerial figure). Up from 2 500 000 at 22 Jun. Industry/private channel only.")
add(E, "national", "vaccine_admin", "doses_distributed_industry", "all", "private",
    "2578470", "doses", RMIS_SRC, "RMIS", E,
    "RMIS portal release 11 Aug 2026. National doses distributed by industry (portal headline; "
    "sum of stud+commercial+feedlot sectors). Provincial table sums to 2 580 315 incl 1 845 dairy "
    "doses (FS) omitted from the headline sector card. Non-programme logistics source.")

# national manufacturer totals (sum of provincial x manufacturer, incl dairy)
add(E, "national", "vaccine_admin", "doses_distributed_industry", "bioaftogen", "private",
    "2060239", "doses", RMIS_SRC, "RMIS", E,
    "RMIS portal release 11 Aug 2026. National manufacturer total, Biogenesis (Argentina). "
    "Sum of provincial split from portal chart. Non-programme logistics source.")
add(E, "national", "vaccine_admin", "doses_distributed_industry", "dolvet", "private",
    "520076", "doses", RMIS_SRC, "RMIS", E,
    "RMIS portal release 11 Aug 2026. National manufacturer total, Dollvet (Turkey). "
    "Sum of provincial split from portal chart. Non-programme logistics source.")

# operations
add(E, "national", "operations", "vet_practices_ordering", "all", "private",
    "121", "count", RMIS_SRC, "RMIS", E,
    "RMIS portal release 11 Aug 2026. Veterinary practices ordering vaccines. Up from 64 at 22 Jun.")
add(E, "national", "operations", "vaccination_sites", "all", "private",
    "1622", "count", RMIS_SRC, "RMIS", E,
    "RMIS portal release 11 Aug 2026. Vaccination sites (GLN locations). Up from 650 at 22 Jun. "
    "Industry/private channel only.")

# national sector split
SECTORS = {"stud": "166710", "commercial": "626462", "feedlot": "1785298", "dairy": "1845"}
for sec, val in SECTORS.items():
    add(E, "national", "vaccine_admin", "doses_distributed_industry", "all", sec,
        val, "doses", RMIS_SRC, "RMIS", E,
        f"RMIS portal release 11 Aug 2026. National sector total: {sec}. "
        + ("Dairy inferred from provincial detail (FS only); omitted from portal headline card. "
           if sec == "dairy" else "") + "Industry/private channel only.")

# province totals and manufacturer split
PROV = {  # code: (total, dolvet, bioaftogen)
    "EC":  (165671,  52923, 112748),
    "FS":  (706422, 164876, 541546),
    "GP":  (558255, 100800, 457455),
    "KZN": (151728,  36944, 114784),
    "LP":  (112857,  21112,  91745),
    "MP":  (282780,  61468, 221312),
    "NW":  (503721,  65418, 438303),
    "NC":  ( 98201,  16335,  81866),
    "WC":  (   680,    200,    480),
}
for p, (tot, dol, bio) in PROV.items():
    add(E, p, "vaccine_admin", "doses_distributed_industry", "all", "private",
        str(tot), "doses", RMIS_SRC, "RMIS", E,
        "RMIS portal release 11 Aug 2026. Province total, all manufacturers. "
        "Industry/private channel only.")
    add(E, p, "vaccine_admin", "doses_distributed_industry", "dolvet", "private",
        str(dol), "doses", RMIS_SRC, "RMIS", E,
        "RMIS portal release 11 Aug 2026. Province x manufacturer: Dollvet (Turkey).")
    add(E, p, "vaccine_admin", "doses_distributed_industry", "bioaftogen", "private",
        str(bio), "doses", RMIS_SRC, "RMIS", E,
        "RMIS portal release 11 Aug 2026. Province x manufacturer: Biogenesis (Argentina).")

# municipality x sector detail
MUNIC = {
 "FS": [("Fezile Dabi","commercial",2691),("Fezile Dabi","feedlot",135021),("Fezile Dabi","stud",5095),
        ("Lejweleputswa","commercial",37223),("Lejweleputswa","feedlot",21890),("Lejweleputswa","stud",21242),
        ("Mangaung","commercial",40794),("Mangaung","dairy",1345),("Mangaung","feedlot",200),("Mangaung","stud",5219),
        ("Thabo Mofutsanyane","commercial",52740),("Thabo Mofutsanyane","dairy",500),
        ("Thabo Mofutsanyane","feedlot",279277),("Thabo Mofutsanyane","stud",17554),
        ("Xhariep","commercial",69676),("Xhariep","feedlot",3920),("Xhariep","stud",12035)],
 "GP": [("City of Tshwane","commercial",120),("City of Tshwane","feedlot",87000),("City of Tshwane","stud",455),
        ("Ekurhuleni","feedlot",71650),("Sedibeng","feedlot",394090),("Sedibeng","stud",190),
        ("West Rand","commercial",1100),("West Rand","feedlot",2900),("West Rand","stud",150),
        ("Unspecified","feedlot",600)],
 "NW": [("Bojanala","commercial",1395),("Bojanala","feedlot",52840),("Bojanala","stud",1806),
        ("Doctor Kenneth Kaunda","commercial",4854),("Doctor Kenneth Kaunda","feedlot",132730),("Doctor Kenneth Kaunda","stud",4109),
        ("Doctor Ruth Segomotsi Mompati","commercial",88739),("Doctor Ruth Segomotsi Mompati","feedlot",131170),("Doctor Ruth Segomotsi Mompati","stud",13644),
        ("Ngaka Modiri Molema","commercial",14994),("Ngaka Modiri Molema","feedlot",55350),("Ngaka Modiri Molema","stud",1910),
        ("ZF Mgcawu","commercial",180)],
 "MP": [("Gert Sibande","commercial",49521),("Gert Sibande","feedlot",82220),("Gert Sibande","stud",10079),
        ("Nkangala","commercial",860),("Nkangala","feedlot",138650),("Nkangala","stud",1450)],
 "EC": [("Alfred Nzo","commercial",10863),("Alfred Nzo","stud",900),
        ("Amathole","commercial",26287),("Amathole","stud",6529),
        ("Buffalo City Metropolitan Municipality","commercial",743),("Buffalo City Metropolitan Municipality","stud",465),
        ("Chris Hani","commercial",19978),("Chris Hani","feedlot",1320),("Chris Hani","stud",4077),
        ("Joe Gqabi","commercial",17549),("Joe Gqabi","stud",17444),
        ("Sarah Baartman","commercial",36357),("Sarah Baartman","feedlot",9630),("Sarah Baartman","stud",12689),
        ("Unspecified","commercial",540),("Unspecified","feedlot",300)],
 "KZN":[("Amajuba","commercial",31193),("Amajuba","feedlot",7160),("Amajuba","stud",2900),
        ("Umgungundlovu","feedlot",14020),("Umzinyathi","commercial",20728),("Umzinyathi","feedlot",8620),
        ("Uthukela","commercial",26832),("Uthukela","feedlot",35870),
        ("Zululand","commercial",2285),("Zululand","stud",2120)],
 "LP": [("Capricorn","commercial",8538),("Capricorn","feedlot",29320),("Capricorn","stud",404),
        ("Mopani","feedlot",2180),("Sekhukhune","commercial",950),
        ("Vhembe","commercial",1296),("Vhembe","feedlot",15430),("Vhembe","stud",372),
        ("Waterberg","commercial",2140),("Waterberg","feedlot",46820),("Waterberg","stud",5407)],
 "NC": [("Frances Baard","commercial",2900),("Frances Baard","feedlot",1980),("Frances Baard","stud",2625),
        ("John Taolo Gaetsewe","commercial",5565),("John Taolo Gaetsewe","feedlot",1380),("John Taolo Gaetsewe","stud",1590),
        ("Namakwa","commercial",1458),
        ("Pixley ka Seme","commercial",12294),("Pixley ka Seme","feedlot",7190),("Pixley ka Seme","stud",8485),
        ("ZF Mgcawu","commercial",33079),("ZF Mgcawu","feedlot",13890),("ZF Mgcawu","stud",5765)],
 "WC": [("Garden Route","feedlot",680)],
}
SEC_LABEL = {"commercial": "Commercial farms", "feedlot": "Feedlot", "stud": "Stud", "dairy": "Dairy"}
for p, entries in MUNIC.items():
    for munic, sec, val in entries:
        add(E, p, "vaccine_admin", "doses_distributed_industry", "all", sec,
            str(val), "doses", RMIS_SRC, "RMIS", E,
            f"RMIS portal release 11 Aug 2026. Municipality: {munic}. Sector: {SEC_LABEL[sec]}. "
            "Industry/private channel only.")

# industry allocation log (arrival month x manufacturer x sector) — new portal table
ALLOC_LOG = [
    ("2026-04-01", "dolvet",     "stud",        50000),
    ("2026-04-01", "dolvet",     "feedlot",    150000),
    ("2026-05-01", "dolvet",     "stud",        50000),
    ("2026-05-01", "dolvet",     "feedlot",    150000),
    ("2026-06-01", "bioaftogen", "commercial", 500000),
    ("2026-06-01", "bioaftogen", "stud",       100000),
    ("2026-06-01", "bioaftogen", "feedlot",   1500000),
    ("2026-07-01", "dolvet",     "commercial", 350000),
    ("2026-07-01", "dolvet",     "stud",        50000),
    ("2026-07-01", "dolvet",     "feedlot",         0),
]
for d, mfr, sec, val in ALLOC_LOG:
    add(d, "national", "vaccine_receipt", "industry_allocation_batch", mfr, sec,
        str(val), "doses", RMIS_SRC, "RMIS", E,
        f"RMIS Industry Allocation Log (portal release 11 Aug 2026): arrival month "
        f"{d[:7]}, manufacturer {'Biogenesis (Argentina)' if mfr=='bioaftogen' else 'Dollvet (Turkey)'}, "
        f"sector {SEC_LABEL[sec]}. Log total 2 900 000 doses.")

# ─────────────────────────────────────────────────────────────────────────────
# 2. WC-GIS — live REST query 17 Aug 2026
# ─────────────────────────────────────────────────────────────────────────────
W = "2026-08-17"
add(W, "WC", "disease", "positive_cases", "", "", "36", "count", WCGIS_SRC, "WC-GIS", W,
    "Live WC GIS portal Disease Reporting layer, confirmed FMD establishments, queried 17 Aug 2026. "
    "Up from 29 at 14 Jul. Establishment/case basis, not outbreaks basis (deck reported 35 outbreaks "
    "at end Jul); case-count basis discrepancy flag remains open.")
add(W, "WC", "disease", "suspected_cases", "", "", "19", "count", WCGIS_SRC, "WC-GIS", W,
    "Live WC GIS portal Disease Reporting layer, suspected FMD establishments, queried 17 Aug 2026. "
    "Up from 12 at 14 Jul.")
add(W, "WC", "vaccine_admin", "doses_administered", "all", "all", "469770", "doses",
    WCGIS_SRC, "WC-GIS", W,
    "Live WC GIS portal FMD Vaccinations layer: sum of NumberVaccinated across 2 497 records, "
    "queried 17 Aug 2026. Up from 403 243 at 14 Jul. Monthly sums: Nov-25 679; Feb 27 609; "
    "Mar 125 952; Apr 28 148; May 105 298; Jun 105 406; Jul 43 118; Aug-to-date 33 560. "
    "Record dates run to 20 Aug 2026 (some forward-dated).")
add(W, "WC", "vaccine_admin", "animals_vaccinated", "all", "all", "469770", "count",
    WCGIS_SRC, "WC-GIS", W,
    "Live WC GIS portal FMD Vaccinations layer: sum of NumberVaccinated across 2 497 records, "
    "queried 17 Aug 2026. Same basis as doses_administered row.")
add("2026-08-13", "WC", "vaccine_receipt", "doses_received", "all", "all", "597080", "doses",
    WCGIS_SRC, "WC-GIS", W,
    "WC GIS portal FMD_Vaccines stat table 'Vaccines Received', last edited 13 Aug 2026. "
    "Up from 497 100 (29 Jun) and 547 100 (30-31 Jul deck).")
add(W, "WC", "operations", "vaccination_sites", "all", "all", "2497", "count",
    WCGIS_SRC, "WC-GIS", W,
    "Live WC GIS portal FMD Vaccinations layer record count (vaccination site visits), "
    "queried 17 Aug 2026. Up from 1 777 at 29 Jun.")
add(W, "WC", "operations", "private_vets_vaccinating", "all", "private", "29", "count",
    WCGIS_SRC, "WC-GIS", W,
    "WC GIS portal FMD_Vaccines stat table 'Private Vets', last edited 13 Aug 2026. Unchanged since May.")

# ─────────────────────────────────────────────────────────────────────────────
# 3. Ministry — Aucamp era (public statements)
# ─────────────────────────────────────────────────────────────────────────────
add("2026-07-01", "national", "policy", "minister_appointed", "", "", "1", "event",
    "Public announcements (africanfarming.com 1 Jul 2026; engineeringnews.co.za 17 Jun 2026)",
    "Ministry", "2026-07-01",
    "Willie Aucamp officially replaced John Steenhuisen as Minister of Agriculture on 1 Jul 2026 "
    "(DA GNU reshuffle announced 17 Jun 2026). FMD response continuity confirmed; new emphasis on "
    "public-private partnership and market liberalisation of vaccine supply.")
add("2026-07-10", "national", "policy", "fmd_settlement_private_imports", "", "", "1", "event",
    "Settlement announcement (polity.org.za 10 Jul 2026; sanews.gov.za)",
    "Ministry", "2026-07-10",
    "Historic FMD settlement between Department of Agriculture, SAAI, Sakeliga and Free State "
    "Agriculture ends litigation. State and OBP expressly relinquish sole rights to import and "
    "distribute FMD vaccines — private imports and sales opened. Livestock owners may vaccinate "
    "voluntarily subject to biosecurity, traceability and reporting rules.")
add("2026-07-25", "national", "policy", "self_vaccination_portal_launched", "", "", "1", "event",
    "Media coverage (news24.com 25 Jul 2026; proagrimedia.com; algoafm.co.za)",
    "Ministry", "2026-07-25",
    "Minister Aucamp launched the online FMD self-vaccination authorisation system: authorised "
    "farmers can apply online to vaccinate their own livestock under traceability and reporting "
    "conditions. Delivers on the July settlement commitment.")
add("2026-07-17", "national", "vaccine_admin", "animals_vaccinated_ministerial", "all", "all",
    "8000000", "count",
    "Minister Aucamp statement (africanfarming.com 31 Jul 2026)", "Ministry", "2026-07-31",
    "Over 8 million animals vaccinated as at 17 Jul 2026 per Minister Aucamp: commercial sector "
    "4.9M; communal and emerging farmers 3.1M; entire dairy herd vaccinated. KZN, NW, EC and FS "
    "each above 1 million. Floor estimate ('over 8 million'). Supersedes 4 709 529 (4 Jun) as "
    "latest ministerial national figure.")
add("2026-07-17", "national", "vaccine_admin", "commercial_vaccinated", "all", "all",
    "4900000", "count",
    "Minister Aucamp statement (africanfarming.com 31 Jul 2026)", "Ministry", "2026-07-31",
    "Commercial sector animals vaccinated as at 17 Jul 2026, ministerial figure.")
add("2026-07-17", "national", "vaccine_admin", "communal_vaccinated", "all", "all",
    "3100000", "count",
    "Minister Aucamp statement (africanfarming.com 31 Jul 2026)", "Ministry", "2026-07-31",
    "Communal and emerging farmer animals vaccinated as at 17 Jul 2026, ministerial figure.")
add("2026-07-17", "national", "policy", "vaccination_target_pct", "", "", "80", "percent",
    "Minister Aucamp statement (africanfarming.com 31 Jul 2026)", "Ministry", "2026-07-31",
    "National target: 80% of the national cattle herd vaccinated by December 2026. "
    "Strain matching and limited consignments noted as constraints on pace.")
add("2026-08-03", "national", "vaccine_receipt", "doses_incoming", "dolvet", "all",
    "4000000", "doses",
    "Minister Aucamp statement (africanfarming.com 31 Jul 2026)", "Ministry", "2026-07-31",
    "4 million doses landing week of 3 Aug 2026 per Minister Aucamp (31 Jul). Consistent with the "
    "'further four million expected' in the 5 Aug Portfolio Committee statement and the 14M SAHPRA "
    "Section 21 Dollvet approval pipeline.")

# ─────────────────────────────────────────────────────────────────────────────
with open(MASTER, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    existing = list(reader)
    fieldnames = reader.fieldnames

# duplicate guard
existing_keys = {(r["effective_date"], r["province"], r["metric"], r["vaccine_type"],
                  r["vet_channel"], r["source_org"], r["value"]) for r in existing}
new = [r for r in rows if (r["effective_date"], r["province"], r["metric"], r["vaccine_type"],
                            r["vet_channel"], r["source_org"], r["value"]) not in existing_keys]

with open(MASTER, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    for r in new:
        w.writerow(r)

print(f"Appended {len(new)} rows (of {len(rows)} candidates); master now {len(existing)+len(new)} rows.")
