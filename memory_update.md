As at 2026-07-01 (session 50 -- WC GIS portal live pull, 29 Jun snapshot; RMIS Vaccine Orders 24 & 30 Jun; NC outbreak dashboard 26 Jun; KZN-DARD PDMAF screenshots 11 Jun; Gauteng advocacy email reviewed, not ingested):
- Master: **2,069 rows** (+5 WC-GIS, +20 RMIS, +1 NC, +21 KZN-DARD = +47 total today)
- Dashboard snapshot: **29 June 2026** (44 weekly points; 206,938 bytes; validation passed)
- Dashboard rebuilt: Yes -- WC-GIS live portal read via browser at user's request; snapshot advanced from 26 June to 29 June. RMIS logistics tab, NC positive cases, and KZN vaccination/district figures updated (none move the snapshot date -- all are dated earlier than 29 June or RMIS is not a programme source).

**New data ingested (session 50, continued -- KZN):**
- `inbox/KZN/DARDKZN 11 06 2026.docx` (19 Teams-screenshot slides of a KZN-DARD PDMAF presentation, 11 June meeting; user confirmed official JOC documents not yet circulated -- all rows marked UNOFFICIAL): 21 rows.
  - **Resolves the long-parked KZN animals-vaccinated gap.** KZN-DARD's own figure: 1,085,495 animals vaccinated as at 30 May 2026 (45.2% coverage) -- sits neatly between the stale AgriSA-NAT 648,609 (21 May) and the DoA's 1,163,193 (4 June). The 648,609 row is now marked superseded by this figure.
  - Doses issued to province: 1,120,000 (state 560,000 / private 560,000).
  - Full 13-district vaccination breakdown added (Amajuba, eThekwini, Harry Gwala, ilembe, King Cetshwayo, uGu, uMgungundlovu, uMkhanyakude x2 state vet areas, uMzinyathi, uThukela, Zululand x2 state vet areas).
  - Dairy cows vaccinated: 267,000 (DARD figure -- differs from MPO's 360,200 series; both held, not reconciled).
  - Vaccine balance: 500,000 doses on hand, stated as insufficient; DARD requests a further 1,500,000 doses urgently.
  - Two new metrics introduced (flagged as non-standard): budget_required R725 million; designated_abattoirs = 6 named facilities.
  - Data quality flags: district table's own total (1,089,316) vs cattle+pig sum (1,085,495) differ by exactly eThekwini's value (3,821); a couple of individual district rows' species sub-splits don't sum cleanly either. Not reconciled -- read as presented.

**New data ingested (session 50, continued -- NC):**
- `inbox/Northern Cape/WhatsApp Image 2026-06-26 at 12.10.46.jpeg` (NC-DALRRD FMD outbreak dashboard, 26 June): 1 row.
  - positive_cases (total reported outbreaks) 22, up from 20 at 16 June.
  - Data quality flag: KPI card states 8 municipalities affected, but the municipality chart lists 9 named municipalities summing to the 22 outbreaks. Not reconciled -- held as-is with both figures in notes.
  - 4 State Veterinary Areas affected (Kuruman, Kimberley, De Aar, Upington); Upington alone accounts for 50% (11 outbreaks) per the chart's own footnote.
  - Diagnostic split: 10 lab confirmed / 12 clinical. By production type: commercial 12, communal 4, feedlot 3, other 2, emerging farm 1.
  - Two accompanying WhatsApp images were an identical duplicate outbreak-location map; no extra numeric data.

**New data ingested (session 50):**
- WC GIS portal (gis.westerncape.gov.za), read live in-browser, "Last Updated: 29 June 2026": 5 rows.
  - positive_cases 39 (up from 38 at 22 June)
  - doses_administered ("Vaccinations") 376,020 (up from 339,410 at 22 June)
  - doses_received ("Vaccines Received") 497,100 (unchanged since 9 June)
  - vaccination_sites 1,777 (up from 1,595 at 22 June)
  - private_vets_vaccinating 29 (unchanged)
- `inbox/RMIS/Vaccine Orders Export (2026-06-24).xlsx` and `(2026-06-30) (1).xlsx` (RMIS): 20 rows (9 provinces + national, x2 dates).
  - National cumulative approved feedlot doses: 2,209,794 (24 Jun) -> 3,179,243 (30 Jun), up from 2,141,146 at 22 Jun.
  - Order count: 1,858 (24 Jun) -> 2,306 (30 Jun), up from 1,763 at 22 Jun.
  - Both files had a corrupted autoFilter XML reference; repaired before parsing. See change_log.md for detail and a flag to RMIS.

**Inbox scan (session 50, prior to WC update):**
- Only one file newer than master_data.csv: `inbox/Gauteng/Email - Ryan - 30 June.pdf`.
- File is a forwarded advocacy email (AgricultureGauteng CEO to Jason Kumm, originally dated 22 June) lobbying for SAHPRA approval of a private Gauteng vaccine manufacturer (Disease Control Africa, Koedoespoort). Not a formal GDARD/JOC submission.
- Email cites a Gauteng "351,945 livestock vaccinated year-to-date" figure with no stated effective date or methodology. This conflicts with the master's GP animals_vaccinated figure of 333,221 (GDARD, 10 June, JOC-formal). Given the source is a commodity/lobby body (not GP-GDARD) and the date is unclear, no row was added -- flagged for confirmation with GDARD rather than silently adopted.
- All other national figures in the email (4.4 million nationwide vaccinated, 2 million DolVet doses at OR Tambo 21 June, ARC 40,000 doses/month local production, 25 May court ruling on private vaccination) are already captured in master from prior ministerial statement ingests.
- No AgriSA Weekly Engagement outcomes PDF for the 1 July 2026 meeting has landed yet (agenda-only PDF already logged in session 48).
- No new dated weekly folder (`DD MMM YYYY/`) at root.

**Inbox scan (session 50):**
- Only one file newer than master_data.csv: `inbox/Gauteng/Email - Ryan - 30 June.pdf`.
- File is a forwarded advocacy email (AgricultureGauteng CEO to Jason Kumm, originally dated 22 June) lobbying for SAHPRA approval of a private Gauteng vaccine manufacturer (Disease Control Africa, Koedoespoort). Not a formal GDARD/JOC submission.
- Email cites a Gauteng "351,945 livestock vaccinated year-to-date" figure with no stated effective date or methodology. This conflicts with the master's GP animals_vaccinated figure of 333,221 (GDARD, 10 June, JOC-formal). Given the source is a commodity/lobby body (not GP-GDARD) and the date is unclear, no row was added -- flagged for confirmation with GDARD rather than silently adopted.
- All other national figures in the email (4.4 million nationwide vaccinated, 2 million DolVet doses at OR Tambo 21 June, ARC 40,000 doses/month local production, 25 May court ruling on private vaccination) are already captured in master from prior ministerial statement ingests.
- No AgriSA Weekly Engagement outcomes PDF for the 1 July 2026 meeting has landed yet (agenda-only PDF already logged in session 48).
- No new dated weekly folder (`DD MMM YYYY/`) at root.

**GitHub push:** Yes -- master_data.csv and FMD_Dashboard.html updated (see change_log.md for commit).

**Parked/outstanding (carry forward):**
- 1 July FMD Weekly Engagement outcomes PDF -- meeting held today; not yet in inbox.
- NC outbreak dashboard (26 June): confirm with NC-DALRRD whether 8 or 9 municipalities are affected -- KPI card and chart disagree by one.
- KZN: obtain official JOC documents once circulated and confirm the KZN-DARD screenshot figures (1,085,495 animals vaccinated, district table, 267,000 dairy vs MPO's 360,200) are accurate before treating as final.
- KZN vaccine shortage: DARD says current 500,000-dose balance is insufficient; a further 1,500,000 requested urgently -- watch for confirmation of the next allocation.
- Gauteng DCA/private-manufacturer advocacy email -- confirm GP 351,945 vaccinated figure with GDARD; consider as a policy/advocacy item for AgriSA leadership rather than a data point.
- Section 9 gazette: announced 25 June 2026; publication still pending.
- LP PCM 6 July 2026 -- next meeting confirmed; await pack and update.
- Consolidated AgriSA weekly xlsx: ~85 days outstanding. Urgent.
- 2 million DolVet doses expected mid-June -- not yet confirmed in RMIS data.
- 7 million Biogenesis doses expected end July 2026 -- forward pipeline.
- KZN booster programme -- 240,000 done per MPO Week 36; resumption expected.
- LP DolVet 150,000 receipt -- outstanding.
- KZN animals vaccinated gap (DoA 1.16 million versus master 648,609).
- MPO Week 37 -- not yet in inbox.

---

As at 2026-06-30 (session 49b -- FS 26 Jun xlsx + media release + Vrystaat Landbou timeline):
- Master: **2,022 rows** (+25 from session 49b, +1 from session 49 = +26 total today)
- Dashboard snapshot: **26 June 2026** (43 weekly points; 194,415 bytes; validation passed)
- Dashboard rebuilt: Yes — FS vaccine receipt updated (Bio 539,980; DolVet 732,200; total 1,272,180); animals vaccinated 1,106,191; positive cases 648 confirmed from DARDLEA media release

**New files ingested (session 49b):**
- `inbox/Free State/FMD STATS - 30 June/FS FMD Vaccine Data - 26.06.2026.xlsx` (FS-DARDLEA): 8 rows. Bio received 539,980; DolVet received 732,200; total received 1,272,180; animals vaccinated 1,106,191; positive 648; suspected 414.
- `inbox/Free State/FMD STATS - 30 June/WhatsApp Image 2026-06-29 at 15.23.14.jpeg` (FS-DARDLEA media release 26 Jun): 16 rows. 14 new cases; 15 State Vet area district breakdowns; 19 municipalities affected.
- `inbox/Free State/WhatsApp Image 2026-06-29 at 12.50.17.jpeg` (FS-Landbou timeline chart Jul 2025 – 26 Jun 2026): 2 rows confirming cumulative 648 positive cases and intermediate 620 (~18 Jun).

**National headlines (dashboard 26 June 2026):**
- Total positive cases (latest per province): 2,526 (EC 411, FS 648, GP 300, KZN 336, LP 84, MP 261, NW 414, NC 20, WC 38) — FS unchanged at 648 but now confirmed from DARDLEA
- Total animals vaccinated (programme sources, JOC-tracked): reflects FS update to 1,106,191

**Data quality notes:**
- FS doses received: 1,272,180 vs prior master 838,400 (5 Jun JOC). New Bioaftogen tranche (+169,980 to 539,980) and DolVet tranche (+266,100 to 732,200) now captured.
- FS animals_vaccinated 1,106,191 from xlsx footer row (col 45); prior DARDLEA 22 Jun was 1,053,502. Treat as cumulative total; no breakdown by dose or vaccine type submitted.
- FS DARDLEA media release notes increasing number of farmers not reporting suspected cases — compliance concern flagged.

**Per-province latest figures (as at 30 June 2026):**

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 1,117,680 | 696,408 (JOC) / 1,001,292 (all) | 411 | 25 Jun |
| FS | 1,272,180 | 1,106,191 | 648 | 26 Jun |
| GP | 643,300 | 333,221 | 300 | 12 Jun |
| KZN | 1,329,112 | 648,609 | 336 | 21 May / 5 Jun |
| LP | 775,660 | 495,102 (LDARD 21 Jun) | 84 | 21-24 Jun |
| MP | 747,000 | 344,629 | 261 | 22 Jun |
| NW | 1,021,140 | 876,483 | 414 | 18 Jun |
| NC | 200,600 | 114,443 | 20 | 16 Jun |
| WC | 497,100 | 299,969 | 38 | 22 Jun |

**Parked/outstanding (carry forward):**
- 1 July FMD Weekly Engagement: meeting held 1 July 2026; outcomes PDF expected in inbox.
- Section 9 gazette: Announced 25 June 2026 by Minister Steenhuisen; gazette publication still pending.
- LP PCM 6 July 2026 — next meeting confirmed; await pack and update.
- Consolidated AgriSA weekly xlsx: ~84 days outstanding. Urgent.
- 2 million DolVet doses expected mid-June — not yet confirmed in RMIS data.
- 7 million Biogenesis doses expected end July 2026 — forward pipeline.
- KZN booster programme — 240,000 done per MPO Week 36; resumption expected.
- LP DolVet 150,000 receipt — outstanding.
- KZN animals vaccinated gap (DoA 1.16 million versus master 648,609).
- MPO Week 37 — not yet in inbox.

---

As at 2026-06-29 (session 48 -- EC 25 Jun; MPO Week 36; 24 Jun outcomes; Ministerial Section 9 announcement):
- Master: **1,996 rows** (+40 from session 48)
- Dashboard snapshot: **25 June 2026** (42 weekly points; 190,849 bytes; validation passed)
- Dashboard rebuilt: Yes — snapshot advanced from 23 Jun to 25 Jun; EC and MPO data updated

**New files ingested (session 48):**
- `inbox/Eastern Cape/EC FMD Update - 25.06.2026.pptx` (EC-DRDAR; 17 image slides): 17 rows. Positive cases 411, suspected 235. Total vaccinations 1,001,292 (incl MPO dairy 304,884); JOC state+private 696,408. Doses received 1,117,680. Balance 116,388. Vaccine utilisation 89.5%.
- `inbox/MPO/Week 36 - Update on the state of FMD and vaccine rollouts in the dairy industry.pdf` (MPO; snapshot 26 Jun): 16 rows. National dairy first vaccinations 935,918; boosters 250,328. 171 dairy farms with FMD cases; 124 still active.
- `inbox/AgriSA Summary and Outcomes/24-june-2026-outcomes.pdf` (AgriSA-NAT; 24 Jun): 6 rows. GLN registrations ~12,500; ~650 vaccination sites; ~260,000 dairy boosters nationally; industry expecting to dispatch ~1.9M doses by end of week following meeting; LP 84 positive cases and ~500,000 vaccinated confirmed.
- `inbox/Ministerial Updates/MEDIA STATEMENT NEW FMD CONTROL MEASURES...pdf` (Ministry; 25 Jun): 1 row (classification event). New FMD control measures approved by Minister Steenhuisen — replaces Section 9 directives incl 2019 FMD Contingency Plan. Gazette publication pending.
- `inbox/AgriSA Summary and Outcomes/AgriSA Weekly FMD Engagement_ 2026.07.01.pdf`: Agenda only; no data rows.

**National headlines (dashboard 25 June 2026):**
- Total positive cases (latest per province): 2,498 (EC 411, FS 634, GP 300, KZN 336, LP 84, MP 261, NW 414, NC 20, WC 38)
- Total animals vaccinated (programme sources, JOC-tracked): 4,780,875

**Data quality notes:**
- EC animals_vaccinated total on slide 16 is 1,001,292 including MPO dairy (304,884). JOC-tracked state+private excl MPO: 696,408. Dashboard uses 696,408 for EC to avoid double-counting with MPO rows.
- LP vaccine_balance row in master shows 0 from 2026-06-01 (stale). LP received 775,660, administered 497,363 = implied balance ~278,297. No JOC balance row for LP.
- EC positive cases 411 is "confirmed outbreaks Dec 2025 to date" per slide; includes Buffalo City Amathole subdistrict flagged with asterisk.
- MPO Week 36 LP figure of 5,475 dairy cows vaccinated — low relative to LP general herd (495,102). Consistent with prior MPO data.

**Per-province latest figures (as at 29 June 2026):**

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 1,117,680 | 696,408 (JOC) / 1,001,292 (all) | 411 | 25 Jun |
| FS | 838,400 | 1,053,502 | 634 | 22-23 Jun |
| GP | 643,300 | 333,221 | 300 | 12 Jun |
| KZN | 1,329,112 | 648,609 | 336 | 21 May / 5 Jun |
| LP | 775,660 | 495,102 (LDARD 21 Jun) | 84 | 21-24 Jun |
| MP | 747,000 | 344,629 | 261 | 22 Jun |
| NW | 1,021,140 | 876,483 | 414 | 18 Jun |
| NC | 200,600 | 114,443 | 20 | 16 Jun |
| WC | 497,100 | 299,969 | 38 | 22 Jun |

**Parked/outstanding (carry forward):**
- 1 July FMD Weekly Engagement: meeting held 1 July 2026; outcomes PDF expected in inbox.
- Section 9 gazette: Announced 25 June 2026 by Minister Steenhuisen; gazette publication still pending — watch inbox.
- LP PCM 6 July 2026 — next meeting confirmed; await pack and update.
- Consolidated AgriSA weekly xlsx: ~83 days outstanding. Urgent.
- 2 million DolVet doses expected mid-June — not yet confirmed in RMIS data.
- 7 million Biogenesis doses expected end July 2026 — forward pipeline.
- KZN booster programme — 240,000 done per MPO Week 36; resumption expected.
- LP DolVet 150,000 receipt — outstanding.
- KZN animals vaccinated gap (DoA 1.16 million versus master 648,609).
- MPO Week 37 — not yet in inbox.

---

As at 2026-06-29 (session 47b -- null ingest; inbox clear; MP received corrected):
- Master: **1,956 rows** (unchanged)
- Dashboard snapshot: **23 June 2026** (40 weekly points; 187,415 bytes; validation passed)
- Dashboard rebuilt: No -- no new data

**Inbox scan (session 47b):**
- All files in inbox confirmed processed in prior sessions.
- MP VWG PPTX 22 June: confirmed in master (session 42; 747,000 received / 577,751 administered / 261 positive cases).
- FS FMD STATS zip (15 June folder): contains FS 12 June xlsx already in master.
- RMIS GLN Locations 22 June: location registry (auction facilities); no dose/case data.
- FMD_Data_Stakeholder_Report_25May2026.xlsx: output report derived from master (1,308 rows, 22 May snapshot); not a source file.
- OneDrive_1_23-06-2026 bundle: June 8 and 18 vaccine orders superseded by June 22 already in master.

**Correction noted:** MP received figure is 747,000 (22 Jun, MP-DVS VWG) not 732,489 shown in session 47 table. Animals vaccinated unchanged at ~344,629. Per-province table below updated.

**No GitHub push this session (no data change).**

**Per-province latest figures (corrected as at 29 June 2026):**

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 1,000,660 | 926,233 | 381 | 11 Jun |
| FS | 838,400 | 1,053,502 | 634 | 22-23 Jun |
| GP | 643,300 | 333,221 | 300 | 12 Jun |
| KZN | 1,329,112 | 648,609 | 336 | 21 May / 5 Jun |
| LP | 775,660 | 495,102 | 84 | 21 Jun |
| MP | 747,000 | 344,629 | 261 | 22 Jun |
| NW | 1,021,140 | 876,483 | 414 | 18 Jun |
| NC | 200,600 | 114,443 | 20 | 10-16 Jun |
| WC | 497,100 | 299,969 | 38 | 22 Jun |

**Parked/outstanding (carry forward):**
- 1 July FMD Weekly Engagement: meeting 1 July 2026; outcomes PDF expected in inbox on or after 1 July.
- Section 9 gazette: Announced 25 June 2026; publication still pending.
- LP PCM 6 July 2026 -- next meeting confirmed; await pack and update.
- Consolidated AgriSA weekly xlsx: approximately 83 days outstanding. Urgent.
- 2 million DolVet doses expected approximately 15 June -- not in RMIS (14+ days overdue).
- 7 million Biogenesis doses expected end July 2026 -- forward pipeline.
- KZN booster programme -- 240,000 done; resumption expected.
- MPO Week 36 -- not yet in inbox.
- LP DolVet 150,000 receipt -- outstanding.
- KZN animals vaccinated gap (DoA 1.16 million versus master 648,609).
- MPO Week 35 GP/MP dairy active case swap -- confirm with MPO.
- NW 793,564 vs 793,964 administered discrepancy (summary slide vs table) -- minor; table value used.

---

As at 2026-06-29 (session 47 -- NW RPO JIC 23 June; AgriSA Weekly Engagement 1 Jul agenda):
- Master: **1,956 rows** (+43 from session 46: NW-RPO 23 June 2026 JIC)
- Dashboard snapshot: **23 June 2026** (40 weekly points; 187,415 bytes; validation passed)
- Dashboard rebuilt: Yes -- NW animals vaccinated updated to 876,483

**New files ingested (session 47):**
- `inbox/North West/23 JUNE 2026- RPO JIC FMD UPDATE.pdf` (NW-RPO): 43 rows. Positive cases 414; animals vaccinated 876,483 (platform); doses allocated 1,021,140; doses used 793,964; balance 156,573.
- `inbox/AgriSA Summary and Outcomes - FMD Weekly Engagement/AgriSA Weekly FMD Engagement_ 2026.07.01.pdf`: Agenda only (meeting 1 July 2026). No data rows.

**National headlines (dashboard 23 June 2026):**
- Distributed (doses received): 6,635,041 (unchanged — NW update is provincial-only, not yet reflected in national headline pending full ICC reconciliation)
- Animals vaccinated: updated (NW contribution now 876,483 vs prior 527,337)
- Positive cases: updated (NW now 414 vs prior 375)

**Per-province latest vaccine figures:**

| Province | Received | Animals vaccinated | Date |
|---|---|---|---|
| EC | 1,000,660 | 926,233 | 11 Jun |
| FS | 838,400 | 1,053,502 | 22 Jun |
| GP | 643,300 | 333,221 | 10 Jun |
| KZN | 1,329,112 | 648,609 | 21 May |
| LP | 775,660 | 495,102 | 21 Jun |
| MP | 732,489 | 344,629 | 8 Jun |
| NW | 1,021,140 | 876,483 | 18 Jun |
| NC | 200,600 | 114,443 | 10 Jun |
| WC | 497,100 | 299,969 | 15 Jun |

**Key NW data added (session 47):**
- positive_cases: 414 cumulative as at 18 Jun (DKK 87, Bojanala 78, DRSM 161, NMM 88); +39 from prior 375
- new_cases_week: 10 (week 13-18 Jun; Ramotshere Moiloa 4, Kagisano 4, Naledi 1, Ratlou 1)
- doses_allocated total: 1,021,140 (includes Bioaftogen 1186 11th June batch 117,000)
- doses_administered total: 793,964 (78%; internal spreadsheet figure; summary slide shows 793,564 -- minor discrepancy noted)
- animals_vaccinated: 876,483 (86% per platform)
- vaccine_balance: 156,573 (of which 34,235 with feedlot industry)
- Per-vaccine administered: Aftodoll 03 Gov 215,942 / Feedlot 65,765 / Aftodoll 05: 279,070 / Bioaftogen 1186 11Jun: 30,215
- NW booster vaccination scheduled to start September, from farms/villages vaccinated in March
- FS RMIS AHTs may be redeployed to NW (FS unable to utilise)

**GitHub commit:** 48c161d (session 47)

**Parked/outstanding (carry forward):**
- Section 9 gazette: Announced 25 June 2026; gazette publication still pending. Monitor for gazette date and number.
- 1 July FMD Weekly Engagement outcomes -- meeting was today (1 July); outcomes PDF not yet in inbox.
- LP PCM 6 July 2026 -- next meeting confirmed; await update.
- Consolidated AgriSA weekly xlsx: approximately 82 days outstanding. Urgent.
- 2 million DolVet doses expected approximately 15 June -- not confirmed in RMIS (14+ days overdue).
- 7 million Biogenesis doses expected end July 2026 -- forward pipeline.
- KZN booster programme -- 240,000 done; resumption expected.
- MPO Week 36 -- not yet in inbox.
- LP DolVet 150,000 receipt -- outstanding.
- KZN animals vaccinated gap (DoA 1.16 million versus master 648,609).
- MPO Week 35 GP/MP dairy active case swap -- confirm with MPO.
- NW 793,564 vs 793,964 administered discrepancy (summary slide vs table) -- minor; table value used.

---

As at 2026-06-26 (session 46 -- ministerial policy statement; null data ingest):
- Master: **1,913 rows** (unchanged)
- Dashboard snapshot: **23 June 2026** (39 weekly points; 182,734 bytes; validation passed)
- Dashboard rebuilt: No -- no new quantitative data

**New files found (session 46):**
- `inbox/Ministerial Updates/MEDIA STATEMENT NEW FMD CONTROL MEASURES GIVE FARMERS A CLEARER PATH TO RECOVERY WHILE PROTECTING TRADE.pdf` (25 June 2026). Policy/regulatory announcement. No data rows added. Section 9 replacement measures approved; gazette pending.

**National headlines (dashboard 23 June 2026):**
- Distributed (doses received): 6,635,041 (unchanged)
- Animals vaccinated: 4,742,044 (unchanged)
- Positive cases: 2,418 (unchanged)

**Per-province latest vaccine figures:**

| Province | Received | Animals vaccinated | Date |
|---|---|---|---|
| EC | 1,000,660 | 926,233 | 11 Jun |
| FS | 838,400 | 1,053,502 | 22 Jun |
| GP | 643,300 | 333,221 | 10 Jun |
| KZN | 1,329,112 | 648,609 | 21 May |
| LP | 775,660 | 495,102 | 21 Jun |
| MP | 732,489 | 344,629 | 8 Jun |
| NW | 895,120 | 527,337 | 1 Jun |
| NC | 200,600 | 114,443 | 10 Jun |
| WC | 497,100 | 299,969 | 15 Jun |

**Parked/outstanding (carry forward):**
- Section 9 gazette: **MEASURES ANNOUNCED 25 JUNE 2026**. Gazette publication still pending. Monitor for gazette date and gazette number.
- 24 June FMD Weekly Engagement outcomes -- meeting was 24 June; outcomes PDF not yet in inbox.
- LP PCM 6 July 2026 -- next meeting confirmed.
- Consolidated AgriSA weekly xlsx: approximately 76 days outstanding. Urgent.
- 2 million DolVet doses expected approximately 15 June -- not confirmed in RMIS (11 days overdue).
- 7 million Biogenesis doses expected end July 2026 -- forward pipeline.
- KZN booster programme -- 240,000 done; resumption expected.
- MPO Week 36 -- not yet in inbox.
- LP DolVet 150,000 receipt -- outstanding.
- KZN animals vaccinated gap (DoA 1.16 million versus master 648,609).
- MPO Week 35 GP/MP dairy active case swap -- confirm with MPO.

---

As at 2026-06-24 (session 44g -- RMIS industry distribution tab update):
- Master: **1,913 rows** (+90 from session 44f: RMIS industry Excel province x manufacturer and municipality x sector rows)
- Dashboard snapshot: **23 June 2026** (39 weekly points; 182,734 bytes; validation passed)
- Dashboard rebuilt: Yes -- RMIS tab redesigned; build_dashboard.py and dashboard_template.html updated

**New data ingested (session 44g):**
- rmis_industry_allocated_fmd_vaccine_distribution_data_2026-06-24.xlsx: 90 rows.
  - Sheet 2 (provincial_distribution): 18 rows: province x manufacturer (Biogenesis/DolVet) breakdowns + 2 national manufacturer totals.
  - Sheet 3 (sector_distribution): 70 rows: province x municipality x sector (feedlot/commercial/stud) breakdown.
- Total industry doses distributed confirmed: 986,012 (39.4% of 2,500,000 allocated to industry).
- Sector split: feedlot 674,060 (68.4%) / commercial 263,373 (26.7%) / stud 48,579 (4.9%).
- Top districts: GP Sedibeng feedlot 151,990; FS Thabo Mofutsanyane feedlot 113,020; MP Nkangala feedlot 60,230.

**RMIS tab changes (dashboard):**
- Kicker updated to "Industry distribution view" (was "Feedlot sector view").
- Title updated to "RMIS: Industry vaccine distribution." (was "RMIS: Feedlot vaccine orders.").
- KPI cards: doses distributed 986,012; utilisation 39.4% of 2.5M; vet practices 64; GLN sites 650.
- New province x manufacturer stacked bar (Biogenesis vs DolVet per province).
- New sector donut: feedlot / commercial / stud with legend.
- New top-15 districts table with sector colour-coding and mini bar.
- Manufacturer split panel (Biogenesis vs DolVet with progress bars).
- Feedlot orders cumulative timeline retained.

**GitHub commit:** 514624b (session 44g)

---

As at 2026-06-24 (session 44f -- verification pass; null ingest):
- Master: **1,807 rows** (unchanged from session 44e)
- Dashboard snapshot: **23 June 2026** (39 weekly points; 168,451 bytes; validation passed)
- Dashboard rebuilt: No -- no new data

**New data ingested (session 44f):**
- None. Inbox fully clear as at 24 June 2026 (second daily pass).
- NW June 1 RPO confirmed already in master (all rows at 2026-06-01).
- RMIS June 18 file skipped (superseded by June 22 already in master).

**National headlines (dashboard 23 June 2026):**
- Distributed (doses received): 6,635,041 (unchanged)
- Animals vaccinated: 4,742,044 (unchanged)
- Positive cases: 2,418 (unchanged)

**Per-province latest vaccine figures:**

| Province | Received | Animals vaccinated | Date |
|---|---|---|---|
| EC | 1,000,660 | 926,233 | 11 Jun |
| FS | 838,400 | 1,053,502 | 22 Jun |
| GP | 643,300 | 333,221 | 10 Jun |
| KZN | 1,329,112 | 648,609 | 21 May |
| LP | 775,660 | 495,102 | 21 Jun |
| MP | 732,489 | 344,629 | 8 Jun |
| NW | 895,120 | 527,337 | 1 Jun |
| NC | 200,600 | 114,443 | 10 Jun |
| WC | 497,100 | 299,969 | 15 Jun |

**Parked/outstanding (carry forward):**
- 24 June FMD Weekly Engagement outcomes -- meeting was today; outcomes PDF not yet in inbox.
- LP PCM 6 July 2026 -- next meeting confirmed.
- Section 9 gazette: approximately 71 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 74 days outstanding. Urgent.
- 2 million DolVet d