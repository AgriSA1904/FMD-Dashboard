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
- 2 million DolVet doses expected approximately 15 June -- not confirmed in RMIS.
- 7 million Biogenesis doses expected end July 2026 -- forward pipeline.
- KZN booster programme -- 240,000 done; resumption expected.
- MPO Week 36 -- not yet in inbox.
- LP DolVet 150,000 receipt -- outstanding.
- KZN animals vaccinated gap (DoA 1.16 million versus master 648,609).
- MPO Week 35 GP/MP dairy active case swap -- confirm with MPO.

---

As at 2026-06-24 (session 44e -- FS DARDLEA 23 Jun media release + MP JOC 23 Jun minutes):
- Master: **1,807 rows** (+17 from 1,790 at session 44d; +27 from 1,780 at session 44c)
- Dashboard snapshot: **23 June 2026** (39 weekly points; 168,451 bytes; validation passed)
- Dashboard rebuilt: Yes -- snapshot advanced from 22 June to 23 June

**New data ingested (session 44e):**
- FS FMD Vaccine Data - 23.06.2026.xlsx + WhatsApp images (FS-DARDLEA): 17 rows. positive_cases 634; animals_vaccinated 1,053,502; 15 district rows.
- JOC 23 June 2026 minutes.pdf (MP-DVS): Minutes only -- no data rows.

**Key figures added:**
- FS positive_cases 634 confirmed as at 23 June 2026 (up from 620 on 12 June; +14 new cases)
- FS animals_vaccinated 1,053,502 cattle (Biogenesis Bago + DolVet) as at 22 June 2026
- FS district breakdown: Moqhaka 117; Ngwathe 93; Mafube 74; Metsimaholo 64; Dihlabeng+Nketoana 67; Phumelela 43; Maluti-A-Phofung 29; Matjhabeng+Nala 43; Mantsopa+Setsoto 46; Smithfield 9; Fauresmith 8; Bloemfontein 9; Thaba Nchu 2; Bultfontein 15; Tokologo 15

**National headlines (dashboard 23 June 2026):**
- Distributed (doses received): 6,635,041 (unchanged; no new national distribution data)
- Animals vaccinated: updated (FS contribution now 1,053,502 vs prior 935,809)
- Positive cases: updated (FS now 634 vs prior 620)

**Per-province latest vaccine figures:**

| Province | Received | Animals vaccinated | Date |
|---|---|---|---|
| EC | 1,000,660 | 926,233 | 11 Jun |
| FS | 838,400 | 1,053,502 | 22 Jun |
| GP | 643,300 | 333,221 | 10 Jun |
| KZN | 1,329,112 | 648,609 | 21 May |
| LP | 775,660 | 495,102 | 21 Jun |
| MP | 732,489 | 344,629 | 8 Jun |
| NW | 617,720 | 527,337 | Jun dates |
| NC | 200,600 | 114,443 | 10 Jun |
| WC | 497,100 | 299,969 | 15 Jun |

**Data quality notes (session 44e):**
- FS animals_vaccinated 1,053,502: from GIS map caption; Biogenesis Bago + DolVet combined. Dose breakdown not provided.
- FS xlsx vaccine allocation columns all zero in PROVINCIAL TOTAL row -- vaccine metrics not filled in this submission; only disease data valid.
- MP JOC 23 June: Section 9 not signed; ARC surveillance delays noted; next JOC 7 July 2026.

**Parked/outstanding (carry forward):**
- 24 June FMD Weekly Engagement outcomes -- meeting today; outcomes expected.
- LP PCM 6 July 2026 -- next meeting confirmed.
- Section 9 gazette: approximately 70 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 73 days outstanding. Urgent.
- 2 million DolVet doses expected ~15 June -- not confirmed in RMIS.
- 7 million Biogenesis doses expected end July 2026 -- forward pipeline.
- KZN booster programme -- 240,000 done; resumption expected.
- MPO Week 36 -- not yet in inbox.
- LP DolVet 150,000 receipt -- outstanding.
- KZN animals vaccinated gap (DoA 1.16 million vs master 648,609).
- MPO Week 35 GP/MP dairy active case swap -- confirm with MPO.

---

As at 2026-06-24 (session 44d -- RMIS Vaccine Orders 22 June):
- Master: **1,790 rows** (+10 from 1,780)
- Dashboard snapshot: **22 June 2026** (38 weekly points; 167,386 bytes; validation passed)
- Dashboard rebuilt: Yes (logistics-only addition; snapshot unchanged)
- RMIS feedlot orders 22 June: 2,141,146 national approved doses (1,763 orders; nearly double the June 9 figure of 1,097,179)

**New data ingested (session 44):**
- GDARD FMD JOC Meeting 12_06_2026.pdf (GP-GDARD): 8 rows. Formal JOC; effective 10 June.
- FMD PCM MEETINGPACK 20260622 REV2.pdf (LP-LDARD): 12 rows. Week 28 + Week 29 + doses_received update.
- MPO Week 35 snapshot 19 June 2026: 23 rows. Dairy vaccinated per province + active dairy FMD.
- AgriSA Weekly FMD Engagement_ 2026.06.24.pdf: Agenda only -- no data rows.

**Key figures added:**
- GP animals_vaccinated 333,221 as at 10 June (formal GDARD; includes Karan 80,000; supersedes verbal 274,757)
- GP positive_cases 300 confirmed outbreaks to 10 June (formal GDARD; supersedes 275 from DoA 9 June)
- GP doses_received 643,300 total allocated (supersedes 518,500; includes 15 May DV 124,800 batch)
- GP controlled_slaughter 225,134 cattle via 5,380 permits (Karan and Beefcor feedlots)
- LP doses_received 775,660 confirmed (additional 163,980 Bioaftogen received ~10 June; supersedes 611,000)
- LP animals_vaccinated 463,132 (Week 28); 495,102 (Week 29 = 21 June)
- LP positive_cases 84 confirmed (Week 28 and 29); LP suspected_cases 87 (Week 28) to 96 (Week 29)
- MPO national dairy cows 1st dose: 921,522; 2nd dose: 247,956 (KZN 240,000 + EC 7,956)
- MPO active dairy FMD farms: 124 of 171 total

**National headlines (dashboard 21 June 2026):**
- Distributed (doses received): 6,635,041
- Animals vaccinated: 4,625,352
- Positive cases: 2,404 (EC 381; FS 620; GP 300; KZN 336; LP 84; MP 251; NW 375; NC 20; WC 37)

**Per-province latest vaccine figures (21 June 2026 snapshot):**

| Province | Received | Animals vaccinated | Date |
|---|---|---|---|
| EC | 1,000,660 | 926,233 | 11 Jun |
| FS | 838,400 | 935,809 | 12 Jun |
| GP | 643,300 | 333,221 | 10 Jun |
| KZN | 1,329,112 | 648,609 | 21 May |
| LP | 775,660 | 495,102 | 21 Jun |
| MP | 732,489 | 344,629 | 8 Jun |
| NW | 617,720 | 527,337 | Jun dates |
| NC | 200,600 | 114,443 | 10 Jun |
| WC | 497,100 | 299,969 | 15 Jun |

**Data quality notes (session 44):**
- GP positive_cases 300 (10 Jun GDARD) conflicts with DoA 275 (9 Jun); both held; GDARD authoritative.
- GP animals_vaccinated 333,221 includes Karan 80,000; per-commodity table = 253,251 + Karan 80,000.
- GP OBP column-mapping issue resolved: 1,700 ARC-OVR allocated; 1,533 administered (under-filled).
- LP DolVet 150,000 parked item remains open: LP DV unchanged at 410,000 across all weeks.
- LP Biogenesis discrepancy resolved: LDARD records now show 100,020 matching AgriSA-NAT.
- EC dairy cows MPO Week 35 (306,879) slightly lower than Week 34 (307,266): possible revision. Both held.
- MPO Week 35 GP/MP dairy active case CONFLICT: Week 34 GP=3 MP=17; Week 35 GP=17 MP=3. Possible swap. Flag for confirmation.
- LP vaccination Week 29 weekly total 19,201 (lower than Week 28 38,964): LDARD attributes to late rural reporting.

**Parked/outstanding (carry forward):**
- 17 June FMD Weekly Engagement summary -- still not in inbox.
- 24 June FMD Weekly Engagement outcomes -- meeting today; outcomes expected.
- LP PCM 6 July 2026 -- next meeting confirmed.
- Section 9 gazette: approximately 69 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 72 days outstanding. Urgent.
- 2 million Dollvet doses expected ~15 June -- not confirmed in RMIS (8 days past expected).
- 7 million Biogenesis doses expected end July 2026 -- forward pipeline.
- KZN booster programme -- 240,000 done; MPO says resumption expected soon.
- RMIS Vaccine Orders Export (08 June; 09 June) xlsx files still unprocessed.
- RMIS GLN Locations export (2026-06-11) xlsx still unprocessed.
- LP DolVet 150,000 receipt -- outstanding.
- KZN animals vaccinated gap (DoA 1.16 million vs master 648,609).
- SAPPO 2026-05-25 unknown province (62 bottles) -- follow up.
- MPO Week 35 GP/MP dairy active case swap -- confirm with MPO.
- MPO Week 36 -- not yet in inbox.

---
name: FMD daily run state
description: Latest master_data.csv row count and dashboard snapshot
type: project
---

As at 2026-06-22 (session 43 -- NC vaccination campaign overview and situation update):
- Master: **1,692 rows** (+6 from 1,686)
- Dashboard snapshot: **16 June 2026** (35 weekly points; 167,032 bytes; validation passed)
