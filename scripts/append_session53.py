#!/usr/bin/env python3
import csv

MASTER = "/sessions/laughing-busy-meitner/mnt/FMD Vaccine Data/master_data.csv"
INGESTED = "2026-07-07"

rows = []

def r(effective_date, province, metric_category, metric, vaccine_type, vet_channel,
      value, unit, source_file, source_org, submitted_date, notes, version="1", superseded_by=""):
    rows.append([effective_date, province, metric_category, metric, vaccine_type, vet_channel,
                 value, unit, source_file, source_org, submitted_date, INGESTED, version, superseded_by, notes])

EC_FILE = "inbox/Eastern Cape/EC FMD Update - 02.07.2026.pptx"
EC_ORG = "EC-DRDAR"
EC_DATE = "2026-07-02"

# Province totals
r(EC_DATE,"EC","disease","positive_cases","all","all",423,"cases",EC_FILE,EC_ORG,EC_DATE,
  "Confirmed outbreaks Dec 2025 to date. Provincial JOC 2 Jul 2026. Up from 411 (25 Jun); +12 new.")
r(EC_DATE,"EC","disease","suspected_cases","all","all",234,"cases",EC_FILE,EC_ORG,EC_DATE,
  "Dec 2025 to date. Down from 235 (25 Jun) despite +5 new reported; net reclassification to confirmed/negative.")
r(EC_DATE,"EC","vaccine_receipt","doses_received","all","all",1064230,"doses",EC_FILE,EC_ORG,EC_DATE,
  "Total vaccine received to date per cumulative allocation table (11 batches, Jan-Jun 2026). Vaccine usage 96.4%.")
r(EC_DATE,"EC","animals_vaccinated","animals_vaccinated","all","all",1026694,"animals",EC_FILE,EC_ORG,EC_DATE,
  "All channels incl MPO dairy (311449). JOC state+private excl MPO: 715245. Up from 1001292 (25 Jun). Sector split: Communal 477923 (46.5%), Commercial 548771 (53.5%). Estimated cattle population 4,595,393; vaccine coverage 22.3%.")
r(EC_DATE,"EC","animals_vaccinated","animals_vaccinated","all","state",715245,"animals",EC_FILE,EC_ORG,EC_DATE,
  "JOC-tracked state+private excl MPO dairy. Sum of 6 district totals (Alfred Nzo 111908 + Amathole 294794 + Chris Hani 116291 + Joe Gqabi 82699 + OR Tambo 103210 + Sarah Baartman 6343).")
r(EC_DATE,"EC","vaccine_admin","doses_administered","bioaftogen","all",427820,"doses",EC_FILE,EC_ORG,EC_DATE,
  "Biogenesis all channels incl MPO (132185). Alfred Nzo 80873, Amathole 102064, Chris Hani 58695, Joe Gqabi 17829, OR Tambo 33359, Sarah Baartman 2815, MPO 132185.")
r(EC_DATE,"EC","vaccine_admin","doses_administered","dolvet","all",595447,"doses",EC_FILE,EC_ORG,EC_DATE,
  "DolVet all channels incl MPO (179264). Alfred Nzo 30585, Amathole 190965, Chris Hani 57596, Joe Gqabi 64870, OR Tambo 69851, Sarah Baartman 2316, MPO 179264.")
r(EC_DATE,"EC","vaccine_admin","doses_administered","obp_arc","all",2177,"doses",EC_FILE,EC_ORG,EC_DATE,
  "ARC-OVI: Amathole 965, Sarah Baartman 1212.")
r(EC_DATE,"EC","vaccine_admin","doses_administered","bvi","all",1250,"doses",EC_FILE,EC_ORG,EC_DATE,
  "BVI: Alfred Nzo 450, Amathole 800.")
r(EC_DATE,"EC","logistics","vaccine_balance","all","all",37536,"doses",EC_FILE,EC_ORG,EC_DATE,
  "Derived: 1064230 received - 1026694 administered = 37536.")
r(EC_DATE,"EC","logistics","vaccine_utilisation","all","all",96.4,"percent",EC_FILE,EC_ORG,EC_DATE,
  "As stated on summary slide (vaccine usage 96.4%).")

# District animals_vaccinated_district (state channel)
r(EC_DATE,"EC","animals_vaccinated","animals_vaccinated_district","all","all",111908,"animals",EC_FILE,EC_ORG,EC_DATE,
  "Alfred Nzo district total. Communal 91229, Commercial 20679. Vaccination: Biogenesis 80873, Dolvet 30585, BVI 450.")
r(EC_DATE,"EC","animals_vaccinated","animals_vaccinated_district","all","all",294794,"animals",EC_FILE,EC_ORG,EC_DATE,
  "Amathole district total. Communal 200365, Commercial 94429. Vaccination: Biogenesis 102064, Dolvet 190965, ARC 965, BVI 800.")
r(EC_DATE,"EC","animals_vaccinated","animals_vaccinated_district","all","all",116291,"animals",EC_FILE,EC_ORG,EC_DATE,
  "Chris Hani district total. Communal 47873, Commercial 68418. Vaccination: Biogenesis 58695, Dolvet 57596.")
r(EC_DATE,"EC","animals_vaccinated","animals_vaccinated_district","all","all",82699,"animals",EC_FILE,EC_ORG,EC_DATE,
  "Joe Gqabi district total. Communal 32879, Commercial 49820. Vaccination: Biogenesis 17829, Dolvet 64870.")
r(EC_DATE,"EC","animals_vaccinated","animals_vaccinated_district","all","all",103210,"animals",EC_FILE,EC_ORG,EC_DATE,
  "OR Tambo district total. Communal 103210, Commercial 0 (100% communal). Vaccination: Biogenesis 33359, Dolvet 69851.")
r(EC_DATE,"EC","animals_vaccinated","animals_vaccinated_district","all","all",6343,"animals",EC_FILE,EC_ORG,EC_DATE,
  "Sarah Baartman district total. Communal 2367, Commercial 3976. Vaccination: Biogenesis 2815, Dolvet 2316, ARC 1212.")
r(EC_DATE,"EC","animals_vaccinated","animals_vaccinated_district","all","private",311449,"animals",EC_FILE,EC_ORG,EC_DATE,
  "MPO dairy sector vaccinations within EC (embedded in provincial total). Alfred Nzo 11757, Amathole 3273, Buffalo City 13223, Chris Hani 59583, Joe Gqabi 0, OR Tambo 0, Nelson Mandela 6188, Sarah Baartman 217425.")

# District positive/suspected outbreaks
district_cases = [
    ("Alfred Nzo", 47, "47 previously, 0 new", 33, "31 previously, 2 new"),
    ("Amathole", 213, "204 previously, 9 new", 97, "102 previously, 1 new - net reclassification"),
    ("Chris Hani", 68, "67 previously, 1 new", 20, "20 previously, 0 new"),
    ("Joe Gqabi", 73, "71 previously, 2 new", 5, "5 previously, 0 new"),
    ("OR Tambo", 16, "16 previously, 0 new", 76, "76 previously, 0 new"),
    ("Sarah Baartman", 6, "6 previously, 0 new", 3, "1 previously, 2 new"),
]
for dist, conf, confnote, susp, suspnote in district_cases:
    r(EC_DATE,"EC","disease","positive_cases_district","all","all",conf,"cases",EC_FILE,EC_ORG,EC_DATE,
      f"District: {dist} | Confirmed outbreaks: {confnote}.")
    r(EC_DATE,"EC","disease","suspected_cases_district","all","all",susp,"cases",EC_FILE,EC_ORG,EC_DATE,
      f"District: {dist} | Suspected outbreaks: {suspnote}.")

# Vaccine allocation received per batch (cumulative allocation table shown at 2 Jul JOC)
batches = [
    ("2026-01-23","bvi","all",800,"BVI batch received 23 Jan 2026 (per cumulative allocation table shown 2 Jul JOC)."),
    ("2026-02-10","obp_arc","all",2600,"ARC batch received 10 Feb 2026."),
    ("2026-02-26","bioaftogen_triv2","all",150000,"Biogenesis 1 batch received 26 Feb 2026."),
    ("2026-03-12","dolvet","all",102000,"DolVet 1 batch received 12 Mar 2026."),
    ("2026-04-02","dolvet","all",10000,"DolVet 2 batch received 2 Apr 2026."),
    ("2026-04-11","bioaftogen_triv2","all",132780,"Biogenesis 2 batch received 11 Apr 2026."),
    ("2026-04-17","dolvet","private",100000,"DolVet batch received 17 Apr 2026 via MPO/industry channel."),
    ("2026-05-01","bioaftogen_triv2","private",100000,"Biogenesis batch received 1 May 2026 via MPO/industry channel."),
    ("2026-05-05","dolvet","all",174350,"DolVet 3 batch received 5 May 2026."),
    ("2026-05-20","dolvet","all",174000,"DolVet 4 batch received 20 May 2026."),
    ("2026-06-09","bioaftogen_triv2","all",117000,"Biogenesis 3 batch received 9 Jun 2026."),
]
for eff, vtype, vchan, val, note in batches:
    r(eff,"EC","vaccine_receipt","doses_received",vtype,vchan,val,"doses",EC_FILE,EC_ORG,EC_DATE,
      note + " Reported retrospectively in 2 Jul 2026 JOC cumulative allocation table.")

# ---------------- Limpopo (LP-LDARD PCM pack, 6 Jul 2026 meeting; Week 29 as at 19/21 Jun, Week 30 as at 26 Jun) ----------------
LP_FILE = "inbox/Limpopo/FMD PCM MEETING PACK 20260706 REV0.pdf"
LP_ORG = "LP-LDARD"
LP_SUBMIT = "2026-07-06"

# Week 29 disease (as at 19 Jun 2026)
r("2026-06-19","LP","disease","positive_cases","all","all",84,"cases",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 29 dashboard. Total investigated 509: confirmed 84, suspect 96, negative 69, closed 9, pending 251.")
r("2026-06-19","LP","disease","suspected_cases","all","all",96,"cases",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 29 dashboard, as at 19 Jun 2026.")
r("2026-06-19","LP","disease","negative_cases","all","all",69,"cases",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 29 dashboard, as at 19 Jun 2026.")
r("2026-06-19","LP","disease","pending_cases","all","all",251,"cases",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 29 dashboard, as at 19 Jun 2026.")

lp_w29_cases = [("Capricorn",25,16),("Mopani",3,3),("Sekhukhune",9,20),("Vhembe",16,31),("Waterberg",31,26)]
for dist, pos, susp in lp_w29_cases:
    r("2026-06-19","LP","disease","positive_cases_district","all","all",pos,"cases",LP_FILE,LP_ORG,LP_SUBMIT,
      f"District: {dist} | Week 29 (as at 19 Jun 2026), per PCM minutes narrative (raw table extraction garbled for this week).")
    r("2026-06-19","LP","disease","suspected_cases_district","all","all",susp,"cases",LP_FILE,LP_ORG,LP_SUBMIT,
      f"District: {dist} | Week 29 (as at 19 Jun 2026), per PCM minutes narrative.")

# Week 29 vaccine (as at 21 Jun 2026)
r("2026-06-21","LP","vaccine_receipt","doses_received","all","all",775660,"doses",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 29 vaccine status, as at 21 Jun 2026. 100% issued to districts, 0 balance at province level.")
r("2026-06-21","LP","vaccine_receipt","doses_received","dolvet","all",410000,"doses",LP_FILE,LP_ORG,LP_SUBMIT,
  "Dollvet-oil FMD SAT 1,2&3, Week 29 as at 21 Jun 2026.")
r("2026-06-21","LP","vaccine_receipt","doses_received","bioaftogen_triv2","all",263940,"doses",LP_FILE,LP_ORG,LP_SUBMIT,
  "Bioaftogen FMD SAT 1,2&3 (trivalent), Week 29 as at 21 Jun 2026.")
r("2026-06-21","LP","vaccine_receipt","doses_received","bioaftogen_biv1","all",100020,"doses",LP_FILE,LP_ORG,LP_SUBMIT,
  "Bioaftogen FMD SAT 1&2 (bivalent), Week 29 as at 21 Jun 2026. Known LDARD-vs-AgriSA-NAT discrepancy (99,020 vs 100,020) not resolved in this pack; only 100,020 appears here.")
r("2026-06-21","LP","vaccine_receipt","doses_received","obp_arc","all",1700,"doses",LP_FILE,LP_ORG,LP_SUBMIT,
  "Onderstepoort FMD (OBP/ARC), Week 29 as at 21 Jun 2026.")
r("2026-06-21","LP","animals_vaccinated","animals_vaccinated","all","all",495102,"animals",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 29, as at 21 Jun 2026. Sector split: Commercial 260628 (53%), Communal 194996 (39%), Emerging 39478 (8%). Doses used 497363. Private vets estimated to account for 150000+ of this total.")
r("2026-06-21","LP","vaccine_admin","doses_administered","all","all",497363,"doses",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 29 total doses used, as at 21 Jun 2026.")
r("2026-06-21","LP","logistics","vaccine_wastage","all","all",2261,"doses",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 29 spillage, 0.45% spillage rate, 27 active weeks, as at 21 Jun 2026.")

# Week 30 disease (as at 26 Jun 2026)
r("2026-06-26","LP","disease","positive_cases","all","all",95,"cases",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 30 dashboard, as at 26 Jun 2026. Total investigations (excl 6 farm revisits) 524: positive 95, suspect 96, negative 105, closed 9, pending 219. Note: weekly status-change table on same slide deck shows closed=8 (internal inconsistency); 9 taken as authoritative headline figure.")
r("2026-06-26","LP","disease","suspected_cases","all","all",96,"cases",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 30 dashboard, as at 26 Jun 2026.")
r("2026-06-26","LP","disease","negative_cases","all","all",105,"cases",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 30 dashboard, as at 26 Jun 2026. Record single-week negative clearance (+38) reflecting Waterberg lab backlog resolution.")
r("2026-06-26","LP","disease","pending_cases","all","all",219,"cases",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 30 dashboard, as at 26 Jun 2026.")

lp_w30_cases = [("Capricorn",26,19,12,1,30),("Mopani",3,3,0,0,72),("Sekhukhune",15,18,8,0,12),
                ("Vhembe",17,29,12,2,17),("Waterberg",34,27,73,6,88)]
for dist, pos, susp, neg, closed, pending in lp_w30_cases:
    r("2026-06-26","LP","disease","positive_cases_district","all","all",pos,"cases",LP_FILE,LP_ORG,LP_SUBMIT,
      f"District: {dist} | Week 30 (as at 26 Jun 2026). Suspect {susp}, Negative {neg}, Closed {closed}, Pending {pending}.")
    r("2026-06-26","LP","disease","suspected_cases_district","all","all",susp,"cases",LP_FILE,LP_ORG,LP_SUBMIT,
      f"District: {dist} | Week 30 (as at 26 Jun 2026).")

# Week 30 vaccine/vaccination (as at 26 Jun 2026)
r("2026-06-26","LP","vaccine_receipt","doses_received","all","all",775660,"doses",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 30 vaccine status, as at 26 Jun 2026. Unchanged from Week 29 - no new consignment reflected yet. RMIS/ICC verbally flagged an additional 150,000 doses inbound (22 Jun 2026 meeting) plus a 'previous batch of 164,000' - neither appears in this total. DolVet 150,000 receipt remains UNCONFIRMED.")
r("2026-06-26","LP","animals_vaccinated","animals_vaccinated","all","all",520185,"animals",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 30, as at 26 Jun 2026. Sector split: Commercial 264914 (52%), Communal 212396 (40%), Emerging 42875 (8%). Doses used 522315. Up from 495102 (Week 29).")
r("2026-06-26","LP","vaccine_admin","doses_administered","all","all",522315,"doses",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 30 total doses used, as at 26 Jun 2026.")
r("2026-06-26","LP","logistics","vaccine_wastage","all","all",2130,"doses",LP_FILE,LP_ORG,LP_SUBMIT,
  "Week 30 spillage, 0.41% spillage rate, 28 active weeks, as at 26 Jun 2026.")

lp_w30_vacc = [("Capricorn",47093,40676,8383,96152),("Mopani",14975,44087,6453,65515),
               ("Sekhukhune",2514,58254,3780,64548),("Vhembe",24948,48012,6682,79642),
               ("Waterberg",175384,21367,17577,214328)]
for dist, comm, commu, emerg, tot in lp_w30_vacc:
    r("2026-06-26","LP","animals_vaccinated","animals_vaccinated_district","all","all",tot,"animals",LP_FILE,LP_ORG,LP_SUBMIT,
      f"District: {dist} | Week 30 (as at 26 Jun 2026). Commercial {comm}, Communal {commu}, Emerging {emerg}.")

# ---------------- MPO Week 37 dairy update (snapshot 3 Jul 2026) ----------------
MPO_FILE = "Week 37 - Update on the state of FMD and vaccine rollouts in the dairy industry.pdf"
MPO_ORG = "MPO"
MPO_DATE = "2026-07-03"
MPO_SUBMIT = "2026-07-03"

mpo_data = [
    ("KZN",360200,240000,"No new dairy FMD cases or reinfections. Booster for remaining 100,000 dairy animals should resume soon."),
    ("EC",307275,10328,"One new suspected dairy case, Nelson Mandela District. Awaiting additional vaccine allocation before booster resumes. EC has 10 positive FMD dairy cases; 8 farms on KZN border placed under EC surveillance."),
    ("FS",15104,0,"No new dairy FMD cases. North region booster rollout has started."),
    ("LP",5475,0,"No new dairy FMD cases. North region booster rollout has started."),
    ("GP",14832,0,"No new dairy FMD cases. North region booster rollout has started."),
    ("MP",9863,0,"No new dairy FMD cases. North region booster rollout has started."),
    ("NW",6342,0,"No new dairy FMD cases. North region booster rollout has started."),
    ("WC",239000,0,"No new dairy FMD cases. First round of FMD vaccination for all dairy animals now complete. Up from 216827 (Week 36)."),
    ("NC",0,0,"No dairy cows vaccinated to date."),
]
for prov, dose1, dose2, note in mpo_data:
    r(MPO_DATE,prov,"animals_vaccinated","dairy_cows_vaccinated","all","private",dose1,"animals",MPO_FILE,MPO_ORG,MPO_SUBMIT,
      f"MPO Week 37 snapshot 3 Jul 2026. First vaccination. {note}")
    if dose2:
        r(MPO_DATE,prov,"animals_vaccinated","booster_vaccinations","all","private",dose2,"animals",MPO_FILE,MPO_ORG,MPO_SUBMIT,
          "MPO Week 37 snapshot 3 Jul 2026. Second/booster vaccination.")

r(MPO_DATE,"national","animals_vaccinated","dairy_cows_vaccinated","all","private",958091,"animals",MPO_FILE,MPO_ORG,MPO_SUBMIT,
  "MPO Week 37 national total first vaccinations. Up from 935918 (Week 36); +22173, mostly WC (+22173).")
r(MPO_DATE,"national","animals_vaccinated","booster_vaccinations","all","private",250328,"animals",MPO_FILE,MPO_ORG,MPO_SUBMIT,
  "MPO Week 37 national total booster/second vaccinations. Unchanged from Week 36 (KZN 240000 + EC 10328).")
r(MPO_DATE,"national","classification","dairy_farms_active_fmd_prov","all","all",124,"farms",MPO_FILE,MPO_ORG,MPO_SUBMIT,
  "171 dairy farms have reported FMD cases nationally, of which 124 remain active (per MPO Week 37 map/summary, 3 Jul 2026).")

with open(MASTER, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    for row in rows:
        w.writerow(row)

print(f"Appended {len(rows)} rows.")
