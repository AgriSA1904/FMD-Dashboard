As at 2026-06-23 (session 44b -- EC 28 May pptx backfill + RMIS 9 June feedlot orders):
- Master: **1,750 rows** (+18 new rows from 1,732)
- Dashboard snapshot: **21 June 2026** (37 weekly points; no advance -- new data is historical backfill)
- Dashboard rebuilt: Yes (168,021 bytes; validation passed)

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
