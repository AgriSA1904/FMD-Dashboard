As at 2026-06-22 (session 43 -- NC vaccination campaign overview and situation update):
- Master: **1,692 rows** (+6 new rows from 1,686)
- Dashboard snapshot: **16 June 2026** (35 weekly points)
- Dashboard rebuilt: Yes (167,032 bytes; validation passed)

**New data ingested (session 43):**
- NC Image Jun 10, 2026 (NC vaccination campaign overview image): 5 rows.
- NC Image Jun 16, 2026 (NC Vet Surveillance System situation overview): 1 row.

**Key figures added:**
- NC doses_received 200,600 as at 10 June 2026 (NC-DALRRD; confirms Ministry allocation)
- NC doses_administered 114,443 as at 10 June 2026 (derived: 200,600 - 86,157 balance)
- NC animals_vaccinated 114,443 as at 10 June 2026 (breakdown: commercial 76,835; communal 34,521; smallholder 2,879; dairy 208; private vets 3,567 doses; farms/facilities 641; tags used 65,364)
- NC vaccine_balance 86,157 as at 10 June 2026
- NC vaccination_sites 641 farms/facilities visited as at 10 June 2026
- NC positive_cases 20 confirmed outbreaks as at 16 June 2026 (up from 17 at 9 June; 5 SVA areas; 9 municipalities; cumulative cases 79; Karnarvon 4 Upington 5 De Aar 1 Gordonia 4 Namakwa 6)

**National headlines (dashboard 16 June 2026):**
- Distributed (doses received, sum of latest per province): 6,345,581
- Administered (doses administered, sum of latest per province): 4,094,702
- Animals vaccinated (sum of latest per province): 4,499,745
- Positive cases: 2,376 (EC 381, FS 620, GP 275, KZN 336, LP 81, MP 251, NW 375, NC 20, WC 37)

**Per-province latest vaccine figures (updated NC):**

| Province | Received | Administered | Animals vaccinated | Date |
|---|---|---|---|---|
| EC | 1,000,660 | 489,979 | 926,233 | 11 Jun |
| FS | 838,400 | 482,848 | 935,809 | 12 Jun |
| GP | 518,500 | 370,837 | 274,757 | 10 Jun |
| KZN | 1,329,112 | 800,177 | 648,609 | 21 May |
| LP | 611,000 | 379,471 | 427,959 | 5 Jun |
| MP | 732,489 | 486,818 | 344,629 | 8 Jun |
| NW | 617,720 | 642,745 | 527,337 | Jun dates |
| NC | 200,600 | 114,443 | **114,443** | **10 Jun** |
| WC | 497,100 | 327,384 | 299,969 | 15 Jun |

**Data quality notes (session 43):**
- NC campaign overview sourced from NC-DALRRD (new provincial source added to PROGRAMME_SOURCES). Source org inferred from content style; no explicit department name on image.
- NC situation overview (Jun 16) reports 79 cumulative FMD cases total and 20 confirmed outbreak premises. Dashboard uses 20 confirmed outbreaks as positive_cases (consistent with other provinces counting outbreak premises). Cumulative 79 noted in row notes.
- NC balance (86,157) implies doses administered = 114,443, which matches animals_vaccinated exactly -- consistent with single-dose campaign.
- NC FMD map (15 June, Directorate Animal Health) confirms outbreak cluster near Kimberley and along Orange River -- qualitative only; no additional numeric rows added.

**Parked/outstanding (carry forward):**
- 17 June FMD Weekly Engagement summary -- meeting held 17 June; outcomes not in inbox.
- LP PCM 18 June 2026 minutes -- meeting held; not yet in inbox.
- Section 9 gazette: approximately 55 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 58 days outstanding. Urgent.
- 2 million Dollvet doses expected ~15 June -- not confirmed in RMIS (now 7 days past expected date).
- KZN booster programme confirmation -- 260,000 of 360,200 dairy cows receiving booster; Harry Gwala still awaiting.
- RMIS Vaccine Orders Export (08 June, 09 June) xlsx files unprocessed.
- RMIS GLN Locations export (2026-06-11) xlsx unprocessed.
- MPO Week 35 -- not in inbox.
- LP DolVet 150,000 receipt -- outstanding.
- LP Biogenesis discrepancy: LDARD 99,020 vs AgriSA-NAT 100,020. Minor.
- GP OBP column-mapping issue -- ongoing.
- EC Artio-Preva duplication -- ongoing.
- KZN animals vaccinated gap (DoA 1.16 million vs master 648,609).
- SAPPO 2026-05-25 unknown province (62 bottles) -- follow up with Dr Chiappero.

---

---
name: FMD daily run state
description: Latest master_data.csv row count and dashboard snapshot
type: project
---

As at 2026-06-18 (session 42 -- 10 June FMD Weekly Engagement summary):
- Master: **1,686 rows** (+13 new rows from 1,673)
- Dashboard snapshot: **15 June 2026** (34 weekly points)
- Dashboard rebuilt: Yes (167,165 bytes; validation passed)

**New data ingested (session 42):**
- Summary and Outcomes_FMD Weekly Engagement_2026.06.10.pdf (long-awaited post-meeting outcomes): 13 rows.

**Key figures added:**
- GP animals_vaccinated 274,757 as at 10 June 2026 (up from 266,121 at 22 May 2026; GDARD verbal report)
- GP feedlot animals vaccinated: 112,669
- GP private vets approved: 57; farmer applications approved: 474; doses via private vets: >140,000
- National GLN registrations exceeded 10,500 as at 10 June 2026 (RMIS)
- Incoming vaccine pipeline: 2 million Dollvet expected ~15 June; 7 million Biogenesis expected end July 2026
- Section 9 nearing ministerial approval as at 10 June (Dewald/RMIS verbal)
- Jordan reopened beef export; Sparta regained export registration
- MPO dairy allocation: 300,000 doses total; 260,000 to KZN (booster); 40,000 to WC
- SAPPO: 150,000 pig doses confirmed fully utilised; one small outbreak in northern KZN

**National headlines (dashboard 15 June 2026 -- unchanged):**
- Distributed (doses received, sum of latest per province): ~6,128,581
- Administered (doses administered, sum of latest per province): ~3,963,734
- Animals vaccinated (sum of latest per province): ~4,412,977 (GP advanced to 274,757)
- Positive cases: 2,373

**Per-province latest vaccine figures (updated GP):**

| Province | Received | Administered | Animals vaccinated | Date |
|---|---|---|---|---|
| EC | 1,000,660 | 489,979 | 926,233 | 11 Jun |
| FS | 838,400 | 482,848 | 935,809 | 12 Jun |
| GP | 518,500 | 370,837 | **274,757** | **10 Jun** |
| KZN | 1,329,112 | 800,177 | 648,609 | 21 May |
| LP | 611,000 | 379,471 | 427,959 | 5 Jun |
| MP | 732,489 | 486,818 | 344,629 | 9 Jun |
| NW | 617,720 | 642,745 | 527,337 | Jun dates |
| NC | 150,600 | 51,227 | 28,054 | 21 May |
| WC | 497,100 | 327,384 | 299,969 | 15 Jun |

**Data quality notes (session 42):**
- GP 274,757 is a verbal report from the 10 June engagement (Dalene); not a formal GDARD JOC submission. Used source_org AgriSA-NAT with note. Advance the figure cautiously pending next formal GP JOC.
- Incoming 2M Dollvet doses expected ~15 June: already past expected arrival date (today is 18 June); monitor RMIS for confirmation of receipt.
- Incoming 7M Biogenesis end July: forward-looking forecast.
- Section 9 stated as "nearing approval" at 10 June -- still not published as at 18 June (41+ days overdue from original estimate).

**Parked/outstanding (carry forward):**
- 17 June FMD Weekly Engagement summary -- meeting held 17 June; outcomes not yet in inbox.
- LP PCM 18 June 2026 minutes -- meeting held yesterday (17 June); outcomes not yet in inbox.
- Section 9 gazette: approximately 41 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 44 days outstanding. Urgent.
- 2 million Dollvet doses expected ~15 June -- confirm receipt in RMIS.
- RMIS inbox: Vaccine Orders Export 2026-06-08 and 2026-06-09 xlsx files unprocessed (require Python/openpyxl approval to read).
- RMIS GLN Locations export 2026-06-11 unprocessed.
- MPO Week 35 -- not yet in inbox.
- KZN booster programme confirmation: 260,000 of 360,200 dairy cows receiving booster (~100,000 Harry Gwala still awaiting).
- LP DolVet 150,000 receipt -- stated "to be issued soon" at 7 May PCM; not confirmed.
- LP Biogenesis discrepancy: LDARD 99,020 vs AgriSA-NAT 100,020. Minor.
- GP OBP column-mapping issue (distributed 1,700 vs administered 127,580) -- investigate before next ingest.
- EC "Other/Artio-Preva" duplication of BVI 1,250 -- confirm with EC.
- KZN: animals vaccinated gap (DoA 1.16 million vs master 648,609).
- SAPPO 2026-05-25 unknown province (62 bottles) -- follow up with Dr Chiappero.
- Dollvet 4 million first consignment -- expected June 2026; now overdue per 15 June expected date. Monitor RMIS.


As at 2026-06-17 (session 41 -- FS JOC, LP PCM, MPO Week 34, WC GIS portal):
- Master: **1,673 rows** (+35 new rows from 1,638)
- Dashboard snapshot: **15 June 2026** (33 weekly points)
- Dashboard rebuilt: Yes (166,927 bytes; validation passed)

**New data ingested (session 41):**
- FS JOC 12 June 2026 (from FMD STATS - 15 June.zip): 10 rows. Key: animals_vaccinated 935,809; doses_received 838,400; positive_cases 620.
- LP-LDARD 5 June 2026 (from FMD PCM MEETINGPACK 20260622 REV0.pdf, 11 June minutes): 9 rows. Key: animals_vaccinated 427,959; doses_received 611,000; positive_cases 81.
- MPO Week 34 12 June 2026: 11 rows. National dairy cows 1st dose 912,250; KZN booster 240,000.
- WC-GIS 15 June 2026 (portal): 5 rows. Positive cases 37; vaccinations 327,384; received 497,100; sites 1,443; private vets 29.

**National headlines (dashboard 15 June 2026):**
- Distributed (doses received, sum of latest per province): ~6,128,581
- Administered (doses administered, sum of latest per province): ~3,963,734
- Animals vaccinated (sum of latest per province): ~4,404,720
- Positive cases: 2,373 (EC 381, FS 620, GP 275, KZN 336, LP 81, MP 251, NW 375, NC 17, WC 37)

**Per-province latest vaccine figures:**

| Province | Received | Administered | Animals vaccinated | Date |
|---|---|---|---|---|
| EC | 1,000,660 | 489,979 | 926,233 | 11 Jun |
| FS | 838,400 | 482,848 | 935,809 | 12 Jun |
| GP | 518,500 | 370,837 | 266,121 | 22 May |
| KZN | 1,329,112 | 800,177 | 648,609 | 21 May |
| LP | 611,000 | 379,471 | 427,959 | 5 Jun |
| MP | 565,489 | 419,066 | 344,629 | 3 Jun |
| NW | 617,720 | 642,745 | 527,337 | Jun dates |
| NC | 150,600 | 51,227 | 28,054 | 21 May |
| WC | 497,100 | 327,384 | 299,969 | 15 Jun |

**Data quality notes (session 41):**
- LP Biogenesis conflict carried forward: LP-LDARD 99,020 vs Ministry 164,000 (same consignment). Both rows held.
- FS doses_received formula-cache issue on provincial total cell (shows 0); Mangaung Bioaftogen 370,000 matches existing master -- no new row added for doses_received.
- WC doses_received 497,100 unchanged from 9 June (no new consignment).

**Parked/outstanding (carry forward):**
- LP PCM 18 June 2026 outcomes -- meeting was yesterday (17 June); minutes not yet in inbox.
- 17 June FMD Weekly Engagement summary -- meeting was today; outcomes expected.
- 10 June FMD Weekly Engagement post-meeting summary -- still not received.
- Section 9 gazette: approximately 34 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 37 days outstanding. Urgent.
- MPO Week 32 -- not received; gap between Week 31 (22 May) and Week 33 (5 June).
- LP DolVet 150,000 receipt -- stated "to be issued soon" at 7 May PCM; not confirmed.
- LP Biogenesis ~164,000 doses -- expected; not yet confirmed.
- GP OBP column-mapping issue (distributed 1,700 vs administered 127,580) -- investigate before next ingest.
- EC "Other/Artio-Preva" duplication of BVI 1,250 -- confirm with EC.
- KZN: animals vaccinated gap (DoA 1.16 million vs master 648,609).
- KZN Harry Gwala: ~100,000 dairy cows still awaiting booster.
- Dollvet 4 million first consignment -- expected June 2026; monitor RMIS.
- SAPPO 2026-05-25 unknown province (62 bottles) -- follow up with Dr Chiappero.
- WC animals_vaccinated: GIS portal "Vaccinations" 327,384 differs from WC-GIS 9 June row of 299,969 used in dashboard -- updated for 15 June.

---

As at 2026-06-17 (session 40b -- MPO Week 34 ingest):
- Master: **1,661 rows** (+23 new rows from 1,638)
- Dashboard snapshot: **11 June 2026** (31 weekly points; unchanged -- MPO is not a programme source)
- Dashboard rebuilt: Yes (164,948 bytes; validation passed)

**New data ingested (session 40b):**
- MPO Week 34 (snapshot 12 June 2026): 23 rows. Dairy cows vaccinated per province (1st dose) + KZN 2nd dose booster + farm stats + per-province active dairy FMD cases from map.

**Key MPO Week 34 figures (12 June 2026):**
- National dairy cows vaccinated 1st dose: 912,250 (up from 904,950 at Week 33)
- KZN booster (2nd dose): 240,000 dairy cows vaccinated; ~100,000 in Harry Gwala still awaiting booster
- EC: 311,038 1st dose (up from 307,266); all first-round dairy vaccinations confirmed complete
- WC: 189,396 1st dose (up from 185,868); first round nearing completion
- Active dairy farms with FMD: 124 (of 171 total; unchanged from Week 33)
- Per-province active dairy FMD cases: LP 1 | NW 6 | GP 3 | FS 10 | MP 17 | KZN 62 | EC 18** | WC 7 | NC 0

**EC note (Week 34):** 18 active dairy cases in EC total; 10 actual EC cases; 8 farms on KZN border placed under EC surveillance for management purposes.

**National headlines (dashboard 11 June 2026 -- unchanged):**
- Distributed: 6,573,661
- Animals vaccinated: 4,126,422
- Positive cases: 2,346

**Parked/outstanding (carry forward):**
- LP PCM 18 June 2026 outcomes -- meeting was yesterday; pack expected imminently.
- 17 June FMD Weekly Engagement summary -- meeting was today; outcomes expected.
- 10 June FMD Weekly Engagement post-meeting summary -- still not in inbox.
- Section 9 gazette: approximately 33 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 36 days outstanding. Urgent.
- MPO Week 32 -- not received; gap in dairy time series between Week 31 (22 May) and Week 33 (5 June).
- LP DolVet 150,000 receipt -- expected; not yet confirmed.
- LP Biogenesis Bago approximately 164,000 dose receipt -- expected; not yet confirmed.
- MP animals_vaccinated not updated (pending MP-DVS confirmation).
- KZN: animals vaccinated gap (DoA 1.16 million vs master 648,609).
- FS doses_received conflict: VL BKS 1,110,500 vs FS-JOC formal 838,400.
- Dollvet 4 million first consignment -- expected June 2026; monitor RMIS.
- SAPPO 2026-05-25 unknown province (62 bottles) -- follow up with Dr Chiappero.
- KZN Harry Gwala district: ~100,000 dairy cows still awaiting booster vaccine.

---

As at 2026-06-17 (session 40 -- null run, no new inbox files):
- Master: **1,638 rows** (unchanged)
- Dashboard snapshot: **11 June 2026** (31 weekly points; unchanged -- no new programme-source data)
- Dashboard rebuilt: No -- no new data

**Inbox scan result (session 40):**
All inbox subfolders last modified Jun 10 or earlier (filesystem confirmed). No new provincial JOC submissions, no consolidated AgriSA xlsx, no MPO, no LP PCM 18 June meeting pack, no FMD Weekly Engagement summary from the 17 June meeting, and no new dated root folder. SharePoint search confirmed no new files after 2026-06-15. Null run.

**National headlines (dashboard 11 June 2026 -- unchanged):**
- Distributed: 6,573,661
- Animals vaccinated: 4,126,422
- Positive cases: 2,346

**Parked/outstanding (carry forward):**
- LP PCM 18 June 2026 -- meeting was yesterday; outcomes and pack expected imminently.
- 10 June FMD Weekly Engagement post-meeting summary -- still not in inbox (agenda only was received).
- 17 June FMD Weekly Engagement -- meeting today; outcomes expected.
- Section 9 gazette: approximately 33 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 36 days outstanding. Urgent.
- MPO Week 32 and Week 34+ -- not received; gap in dairy time series.
- LP DolVet 150,000 receipt -- expected; not yet confirmed.
- LP Biogenesis Bago approximately 164,000 dose receipt -- expected; not yet confirmed.
- MP animals_vaccinated not updated (pending MP-DVS confirmation).
- KZN: animals vaccinated gap (DoA 1.16 million vs master 648,609).
- FS doses_received conflict: VL BKS 1,110,500 vs FS-JOC formal 838,400.
- Dollvet 4 million first consignment -- expected June 2026; monitor RMIS.
- SAPPO 2026-05-25 unknown province (62 bottles) -- follow up with Dr Chiappero.

---

As at 2026-06-15 (session 39 -- SAPPO 10 June dispatch update):
- Master: **1,638 rows** (+3 new rows from 1,635)
- Dashboard snapshot: **11 June 2026** (31 weekly points; unchanged -- no new programme-source data)
- Dashboard rebuilt: Yes (164,453 bytes; validation passed)

**New data ingested (session 39):**
- Email - SAPPO - 10 June.pdf (SAPPO, Dr Thandi Chiappero): 3 new dispatch rows not in 5 June email -- KZN 14 bottles (5 June), MP 34 bottles (9 June), MP 20 bottles (9 June). Commodity-body source; no dashboard headline change.

**Data quality flags (session 39):**
1. SAPPO 2026-05-25 ML 62 bottles: province still unknown; carry forward for follow-up.
2. LP PCM MEETINGPACK 20260611.pdf confirmed as pre-meeting pack (11 June agenda + 4 June minutes). 4 June minutes data already in master. No duplicate rows added.
3. MP Screenshot 2026-06-10: Confirms session 34b figures exactly. Confirmed duplicate.

**National headlines (dashboard 11 June 2026 -- unchanged):**
- Distributed: 6,573,661
- Animals vaccinated: 4,126,422
- Positive cases: 2,346

**Parked/outstanding (carry forward):**
- LP PCM 18 June 2026 -- meeting today; outcomes expected.
- 10 June FMD Weekly Engagement post-meeting summary -- still not in inbox.
- Section 9 gazette: approximately 26 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 29 days outstanding. Urgent.
- MPO Week 32 and Week 34+ -- not received; gap in dairy time series.
- LP DolVet 150,000 receipt -- expected; not yet confirmed.
- LP Biogenesis Bago approximately 164,000 dose receipt -- expected; not yet confirmed.
- MP animals_vaccinated not updated (pending MP-DVS confirmation).
- KZN: animals vaccinated gap (DoA 1.16 million vs master 648,609).
- FS doses_received conflict: VL BKS 1,110,500 vs FS-JOC formal 838,400.
- Dollvet 4 million first consignment -- expected June 2026; monitor RMIS.
- SAPPO 2026-05-25 unknown province (62 bottles) -- follow up with Dr Chiappero.

---

As at 2026-06-12 (session 38 -- EC FMD Update 11 June 2026):
- Master: **1,635 rows** (+14 new rows from 1,621)
- Dashboard snapshot: **11 June 2026** (31 weekly points; advanced from 9 June)
- Dashboard rebuilt: Yes (164,418 bytes; validation passed)

**New data ingested (session 38):**
- EC FMD Update - 11.06.2026 Final.pptx (EC-DRDAR, effective 2026-06-11): 14 rows. Full EC provincial JOC update.
- archive/2026-06-12/Reporting of cases & vaccines - 11.06.2026.xlsx: EC-only consolidated template confirming same figures. No additional rows.

**National headlines (dashboard 11 June 2026):**
- Distributed: 6,573,661 (unchanged -- EC received confirmed at 1,000,660)
- Animals vaccinated: 4,126,422 (+93,120 from EC update; EC 833,113 to 926,233)
- Positive cases: 2,346 (NOTE: apparent decrease from 2,361 due to methodology change -- EC-DRDAR outbreak premises 381 vs Ministry individual cases 396 at 9 June; both valid metrics held in master)

**EC figures as at 11 June 2026 (EC-DRDAR):**
- Confirmed outbreaks (premises): 381 (+20 from 361 at 3 June)
- Suspected outbreaks: 237
- Animals vaccinated (all incl. MPO 299,282): 926,233
- Animals vaccinated (state channel only): 626,951
- Doses received (state/dept): 1,000,660 (unchanged)
- Vaccine usage: 92.5%
- Breakdown: BVI 1,250 | ARC 2,177 | Biogenesis state 246,824 + MPO 131,499 | DolVet state 376,700 + MPO 167,783
- Balance: 74,427

**Data quality flags (session 38):**
1. EC positive_cases methodology conflict: EC-DRDAR 11 Jun = 381 confirmed outbreak premises; Ministry 9 Jun = 396 individual cases. Dashboard uses EC-DRDAR (more recent programme source). Both rows in master.
2. EC state Biogenesis on 11 Jun (246,824) lower than previous combined all (367,694 on 3 Jun) because 11 Jun template splits state/private. State+MPO total = 378,323 (+10,629 from 367,694). Consistent.

**Per-province (11 June 2026 snapshot):**

| Province | Received | Animals vaccinated | Positive cases | As at |
|---|---|---|---|---|
| EC | 1,000,660 | 926,233 | 381 (EC-DRDAR) | 2026-06-11 |
| FS | 838,400 | 707,986 | 595 | 2026-06-09 |
| GP | 518,500 | 266,121 | 275 | 2026-06-09 |
| KZN | 1,329,112 | 648,609 | 336 | 2026-06-09 |
| LP | 611,680 | 377,484 | 81 | 2026-06-09 |
| MP | 732,489 | 344,629 | 251 | 2026-06-09 |
| NW | 895,120 | 527,337 | 375 | 2026-06-09 |
| NC | 150,600 | 28,054 | 17 | 2026-06-09 |
| WC | 497,100 | 299,969 | 35 | 2026-06-09 |

**Parked/outstanding (carry forward):**
- 10 June FMD Weekly Engagement post-meeting summary -- still not in inbox.
- Section 9 gazette: approximately 19 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 22 days outstanding. Urgent.
- MPO Week 32 -- not received; gap in dairy time series.
- LP DolVet 150,000 receipt -- expected; not yet confirmed.
- LP Biogenesis Bago ~147,000 dose receipt -- expected; not yet confirmed.
- MP animals_vaccinated not updated (pending MP-DVS confirmation).
- EC methodology reconciliation: EC-DRDAR 381 outbreak premises vs Ministry 396 individual cases at 9 June.
- KZN: animals vaccinated gap (DoA 1.16M vs master 648k).
- FS doses_received conflict: VL BKS 1,110,500 vs FS-JOC formal 838,400.
- Dollvet 4M first consignment -- expected June 2026; monitor RMIS.
- Next LP PCM meeting: 18 June 2026.

---

As at 2026-06-11 (session 37 -- AHGEN WOAH report 29 May + VL BKS FS-Landbou 5 June + template fix):
- Master: **1,621 rows** (+21 new rows from clean 1,600)
- Dashboard snapshot: **9 June 2026** (30 weekly points; unchanged -- new data backdated or non-programme source)
- Dashboard rebuilt: Yes (164,064 bytes; template duplicate-tail bug fixed)

**New data ingested (session 37):**
- AHGEN112 FMD Outbreak Report, 29 May 2026 (DoA Directorate Animal Health, Ministry): WOAH-notified outbreak counts per province as at 29 May 2026. 10 rows woah_outbreaks_open + 7 rows woah_outbreaks_closed (non-zero only). National open: 2,130; closed: 32; total: 2,162.
- VL BKS JOC verslag 260605.pdf (Vrystaat Landbou, FS-Landbou): FS vaccine component breakdown (Biogenesis 318,649 + DolVet 389,337 = 707,986 animals vaccinated); FS total doses received per VL BKS 1,110,500 (CONFLICT: FS-JOC formal 838,400 authoritative). 4 rows.
- inbox/Free State/WhatsApp Image 2026-06-10 at 10.59.11.jpeg: Confirmed duplicate of FS-DARDEA 5 June 2026 media release (positive_cases 608, SVA breakdown). Data already in master from session 32. No rows added.

**Template fix (session 37):**
- scripts/dashboard_template.html had duplicated tail (lines 1720-1723: extra `}());
</script>
</body>
</html>`). Removed. Script tag count corrected to 4 open/4 close.

**National headlines (dashboard 9 June 2026 -- unchanged):**
- Distributed: 6,573,661
- Administered: 4,033,302
- Positive cases: 2,361

**WOAH outbreak counts (29 May 2026, Ministry source):**

| Province | Open | Closed | Total |
|---|---|---|---|
| EC | 256 | 0 | 256 |
| FS | 581 | 4 | 585 |
| GP | 272 | 3 | 275 |
| KZN | 316 | 20 | 336 |
| LP | 76 | 3 | 79 |
| MP | 242 | 1 | 243 |
| NW | 350 | 1 | 351 |
| NC | 15 | 0 | 15 |
| WC | 22 | 0 | 22 |
| National | 2,130 | 32 | 2,162 |

**Parked/outstanding (carry forward):**
- WC primary/booster split -- Vaccinations tab not accessible. Retry next session.
- 10 June FMD Weekly Engagement post-meeting summary -- not yet in inbox.
- Section 9 gazette: approximately 18 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 21 days outstanding. Urgent.
- MPO Week 32 -- not received; gap in dairy time series.
- LP Biogenesis Bago ~147,000 dose receipt -- expected; not yet confirmed.
- MP animals_vaccinated not updated (unique animals pending MP-DVS confirmation).
- EC: 396 cases (+71 since 5 June) -- confirm not a backlog.
- KZN: animals vaccinated gap (DoA 1.16M vs master 648k) -- next submission.
- Dollvet 4M first consignment -- expected June 2026; monitor RMIS.
- FS doses_received conflict: VL BKS 1,110,500 vs FS-JOC formal 838,400 -- confirm additional 266,100 DolVet batch with FS-JOC.
- Next LP PCM meeting: 18 June 2026.

---

As at 2026-06-10 (session 36 -- WC GIS portal 9 June 2026 ingested):
- Master: **1,601 rows** (+7 WC GIS rows from session 34b total of 1,593 + 1 blank line artefact)
- Dashboard snapshot: **9 June 2026** (30 weekly points)
- Dashboard rebuilt: Yes

**New data ingested (WC-GIS, effective 2026-06-09):**
- WC positive_cases: 35 (up from 22 on 21 May 2026)
- WC doses_received: 497,100 (up from 330,140 on 19 May 2026)
- WC animals_vaccinated: 299,969 (up from 231,913 on 19 May 2026)
- WC doses_administered: 299,969
- WC vaccine_balance: 197,131
- WC vaccination_sites: 1,307
- Source: WC Government GIS portal live dashboard (Last Updated: 9 June 2026). Primary/booster split not available from main dashboard view.

**National headlines (dashboard 9 June 2026):**
- Distributed: 6,573,661
- Administered: 4,033,302
- Positive cases: 2,361

**Parked/outstanding (carry forward):**
- WC primary/booster split -- Vaccinations tab not accessible from main dashboard view. Retry next session.
- 10 June FMD Weekly Engagement post-meeting summary -- not yet in inbox.
- Section 9 gazette: approximately 17 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 20 days outstanding. Urgent.
- MPO Week 32 -- not received; gap in dairy time series.
- LP Biogenesis Bago ~147,000 dose receipt -- expected; not yet confirmed.
- MP animals_vaccinated not updated (AgriMP reported doses_administered only; unique animals pending MP-DVS confirmation).
- EC: 396 cases (+71 since 5 June) -- confirm not a backlog.
- KZN: animals vaccinated gap (DoA 1.16M vs master 648k) -- next submission.
- Dollvet 4M first consignment -- expected June 2026; monitor RMIS.
- Next LP PCM meeting: 18 June 2026.

---

As at 2026-06-10 (session 34b -- AgriMP Mpumalanga WhatsApp update; ministerial comparison fix):
- Master: **1,593 rows** (+4 from session 34 total of 1,589)
- Dashboard snapshot: **9 June 2026** (30 weekly points)
- Dashboard rebuilt: Yes

**New data ingested:**
- MP doses_received: 732,489 cumulative as at 8 June 2026 (167,000 new batch received 8 Jun; prior 565,489)
- MP doses_administered: 486,818 as at 9 June 2026
- MP doses_allocated_doa: 680,000 total (580,000 prior + 100,000 additional)
- MP doses_allocated_doa private channel: 61,000 (RPO Mpumalanga)
- Source: Robert Davel, Agri Mpumalanga (AgriMP)

**Build fixes this session:**
- Ministerial comparison JOC column was pulling stale AgriSA-NAT carry-forwards instead of current provincial submissions. Fixed by widening prefer_org to full PROGRAMME_SOURCES. EC now 833,113, NW 527,337, LP 377,484, FS 707,986 in JOC column.
- Ministerial date placeholder (__MINISTERIAL_DATE_LONG__) was not being replaced due to truncated build_dashboard.py (Edit tool truncation bug). File repaired; now shows "4 June 2026" dynamically.
- AgriMP added to PROGRAMME_SOURCES.
- FS-DARDEA added to PROGRAMME_SOURCES.

**Parked/outstanding (carry forward):**
- 10 June FMD Weekly Engagement post-meeting summary -- not yet in inbox.
- Section 9 gazette: approximately 17 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 20 days outstanding. Urgent.
- MPO Week 32 -- not received; gap in dairy time series.
- LP Biogenesis Bago ~147,000 dose receipt -- expected; not yet confirmed.
- MP animals_vaccinated not updated (AgriMP reported doses_administered only; unique animals pending MP-DVS confirmation).
- EC: 396 cases (+71 since 5 June) -- confirm not a backlog.
- WC: George case confirmed in narrative but not in new_cases table -- confirm.
- KZN: animals vaccinated gap (DoA 1.16M vs master 648k) -- next submission.
- Dollvet 4M first consignment -- expected June 2026; monitor RMIS.
- Next LP PCM meeting: 18 June 2026.

---

As at 2026-06-10 (session 35 -- null run, no new inbox files):
- Master: **1,579 rows** (unchanged)
- Dashboard snapshot: **9 June 2026** (unchanged; 28 weekly points)
- Dashboard rebuilt: No -- no new data

**Inbox scan result (session 35):**
All inbox subfolders last modified May 2026 or earlier. No new provincial JOC submissions, no consolidated AgriSA xlsx, no MPO, no dated root folder, no FMD Weekly Engagement summary from the 10 June meeting. Null run.

**Parked/outstanding (carry forward):**
- 10 June FMD Weekly Engagement post-meeting summary -- not yet in inbox.
- Section 9 gazette: approximately 17 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 20 days outstanding. Urgent.
- MPO Week 32 -- not received; gap in dairy time series.
- LP Biogenesis Bago ~147,000 dose receipt -- expected; not yet confirmed.
- EC: 396 cases (+71 since 5 June) -- confirm not a backlog.
- WC: George case confirmed in narrative but not in new_cases table -- confirm.
- KZN: animals vaccinated gap (DoA 1.16M vs master 648k) -- next submission.
- GP OBP column-mapping -- ongoing.
- Dollvet 4M first consignment -- expected June 2026; monitor RMIS.
- Next LP PCM meeting: 18 June 2026.

---

As at 2026-06-10 (session 34 -- NW RPO JIC 1+9 June + Portfolio Committee 9 June ingest):
- Master: **1,579 rows** (+78 new rows from 1,501)
- Dashboard snapshot: **9 June 2026** (advanced from 5 June; 28 weekly points, validation passed)
- Dashboard rebuilt: Yes -- FMD_Dashboard.html (163,496 bytes)

**Key highlights (session 34):**
- NW RPO JIC 1 June: 361 confirmed cases, 527,337 animals vaccinated, 524,839 total doses used. First NW data since 21 May 2026.
- NW RPO JIC 9 June: 375 confirmed cases (+14), 642,745 total doses used. New Bioaftogen 117,000 received 8 June (Biogenesis Bago 3).
- Portfolio Committee 9 June: DoA case table (5 June status + new cases since). National cumulative at 9 June = 2,338 (up from 2,205 at 5 June). EC +71 new cases is notable.
- DoA per-province allocation and animals vaccinated figures stored as doses_allocated_doa and animals_vaccinated_doa (to avoid overriding provincial JOC data; DoA allocation methodology differs from provincial received figures).
- Biogenesis Bago 3 per-province allocations confirmed: total 1.35M to provinces (EC 217k, FS 170k, KZN 217k, MP 267k, LP 164k, NW 117k confirmed, NC 67k, GP 64k, WC 67k).
- Sakeliga court ruling confirmed: private farmers may procure and use FMD vaccine subject to State Vet reporting.

**National dashboard (9 June 2026 snapshot):**
- Doses distributed: 5,962,501
- Doses administered: 3,868,263
- Animals vaccinated: 3,965,246
- Positive cases: 2,348 (EC 396; FS 595; GP 275; KZN 336; LP 81; MP 251; NW 375; NC 17; WC 22)

**Per-province (9 June 2026):**

| Province | Distributed | Administered | Animals vaccinated | Positive |
|---|---|---|---|---|
| EC | 1,000,660 | 833,113 | 833,113 | 396 |
| FS | 838,400 | 482,848 | 707,986 | 595 |
| GP | 518,500 | 370,837 | 266,121 | 275 |
| KZN | 1,329,112 | 800,177 | 648,609 | 336 |
| LP | 611,680 | 379,471 | 377,484 | 81 |
| MP | 565,489 | 419,066 | 344,629 | 251 |
| NW | 617,720 | 642,745 | 527,337 | 375 |
| NC | 150,600 | 51,227 | 28,054 | 17 |
| WC | 330,340 | 231,913 | 231,913 | 22 |

**Parked/outstanding:**
- 10 June FMD Weekly Engagement post-meeting summary -- not yet in inbox.
- Section 9 gazette: approximately 16 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 19 days outstanding. Urgent.
- MPO Week 32 -- not received; gap in dairy time series.
- LP Biogenesis Bago ~147,000 dose receipt -- expected; not yet confirmed.
- EC: 396 cases (+71 since 5 June) -- confirm not a backlog.
- WC: George case confirmed in narrative but not in new_cases table -- confirm.
- KZN: animals vaccinated gap (DoA 1.16M vs master 648k) -- next submission.
- GP OBP column-mapping -- ongoing.
- Dollvet 4M first consignment -- expected June 2026; monitor RMIS.
- Next LP PCM meeting: 18 June 2026.

---

*Session 33 (10 June 2026): 1,501 rows; dashboard 5 June 2026 (27 weekly points). LP RPO Blouberg allocation from 4 June LP PCM minutes.*

---

As at 2026-06-10 (session 33 -- LP RPO Blouberg allocation + 11 June LP PCM pack review):
- Master: **1,501 rows** (+1 new row from 1,500)
- Dashboard snapshot: **5 June 2026** (unchanged; 27 weekly points, validation passed)
- Dashboard rebuilt: Yes -- FMD_Dashboard.html (163,030 bytes)

**Key highlights (session 33):**
- Two new inbox files identified: AgriSA Weekly FMD Engagement 10 June agenda (agenda only, no data) and LP PCM Meeting Pack 20260611 (4 June 2026 LP PCM full minutes + 11 June agenda).
- 10 June FMD Weekly Engagement post-meeting summary not yet in inbox.
- LP PCM 4 June 2026 minutes confirm RPO LP Blouberg allocation of approximately 23,000 doses; to be administered via private vets in Blouberg, facilitated by Buffalo Analytics. Added as 1 row (source_org: RPO; NOT a programme-source figure).
- LP PCM minutes confirm Biogenesis 3.5M shipment was the final approved import; no new Section 21 permits submitted (Dr Danie Odendaal).
- LP expected approximately 147,000 doses from Biogenesis Bago national consignment (not yet received as at 4 June; not added pending confirmation).
- Next LP PCM meeting: 18 June 2026.

**National dashboard (5 June 2026 snapshot -- unchanged):**
- Doses distributed: 5,875,790
- Doses administered: 3,556,621
- Animals vaccinated: 3,416,885
- Positive cases: 2,205 (EC 361; FS 608; GP 296; KZN 69; LP 74; MP 231; NW 332; NC 7; WC 22)
- Suspected cases: 920

**Per-province (5 June 2026):**

| Province | Distributed | Administered | Animals vaccinated | Positive |
|---|---|---|---|---|
| EC | 1,000,660 | 833,113 | 833,113 | 361 / 566 conflict |
| FS | 838,400 | 482,848 | 707,986 | 608 |
| GP | 518,500 | 370,837 | 266,121 | 296 |
| KZN | 1,329,112 | 800,177 | 648,609 | 69 |
| LP | 611,680 | 379,471 | 377,484 | 74 |
| MP | 565,489 | 419,066 | 344,629 | 231 |
| NW | 617,720 | 331,103 | 171,561 | 332 |
| NC | 150,600 | 51,227 | 28,054 | 7 |
| WC | 330,340 | 231,913 | 231,913 | 22 |

**Parked/outstanding:**
- 10 June FMD Weekly Engagement post-meeting summary -- not yet in inbox.
- Section 9 gazette: approximately 16 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 19 days outstanding. Urgent.
- MPO Week 32 -- not received; gap in dairy time series.
- LP Biogenesis Bago ~147,000 dose receipt -- expected; not yet confirmed.
- LP Biogenesis depot at 0 -- urgent.
- NW: DDG Serage outcome + reinfection investigation.
- EC: confirm 361 vs 566; confirm 18,730 doses gap.
- KZN booster programme -- monitor.
- GP OBP column-mapping -- ongoing.
- SAPPO: bottles-to-doses conversion + unknown province follow-up.
- Dollvet 4M first consignment -- expected June 2026; monitor RMIS.
- Next LP PCM meeting: 18 June 2026.

---

*Session 32 (09 June 2026): 1,500 rows; dashboard 5 June 2026 (27 weekly points). FS 5 June JOC + MPO Week 33 ingest.*

---

As at 2026-06-09 (session 32 -- FS 5 June JOC + MPO Week 33 ingest):
- Master: **1,500 rows** (+32 new rows from 1,468)
- Dashboard snapshot: **5 June 2026** (advanced from 3 June; 27 weekly points, validation passed)
- Dashboard rebuilt: Yes -- FMD_Dashboard.html (162,794 bytes)

**Key highlights (session 32):**
- FS-JOC 5 June submission ingested (from FMD STATS 08 june.zip): positive_cases 608 (+4 from 604); suspected 412; doses received formally confirmed at 838,400 (bioaftogen 370,000 + dolvet 466,100 + obp 2,300). CONFLICT: formal 838,400 vs AgriSA-NAT verbal 1,100,000 at 3 June ICC meeting -- formal FS-JOC is authoritative.
- FS-DARDEA media release (5 June 2026, map dated 4 June): 707,986 cattle vaccinated with Biogenesis Bago and DolVet. Higher than prior verbal estimate of 609,900.
- MPO Week 33 ingested (snapshot 5 June 2026): national dairy cows vaccinated 904,950 (up from 831,143 at 22 May). WC increased 150,116 → 185,868; EC increased 269,211 → 307,266.
- MPO Week 31 confirmed already ingested (snapshot 22 May, data matches 2026-05-22 entries in master).
- MPO Week 32 still not received (not in inbox).
- KZN FMD booster vaccinations started 8 June 2026 (per MPO Week 33).
- EC: 4 dairy reinfection cases after vaccination (MPO Week 33).

**National dashboard (5 June 2026 snapshot):**
- Doses distributed: 5,875,790 (unchanged; next update pending consolidated weekly xlsx)
- Doses administered: 3,556,621
- Animals vaccinated: 3,416,885
- FS animals vaccinated updated to 707,986 (FS-DARDEA 4 June) — dashboard may use 513,167 (last formal FS-JOC dose-level total); check build script logic
- Positive cases: 2,205 (EC 361; FS 608; GP 296; KZN 69; LP 74; MP 231; NW 332; NC 7; WC 22) — FS up 4 from 604
- Suspected cases: 920

**Per-province (5 June 2026 where updated; others unchanged from 3 June):**

| Province | Distributed | Administered | Animals vaccinated | Positive |
|---|---|---|---|---|
| EC | 1,000,660 | 833,113 (dose-count) | 833,113 | 361 (EC-DRDAR) / 566 (AgriSA-NAT) |
| FS | 838,400 (formal) | 482,848 | 707,986 (FS-DARDEA 4 Jun) | 608 |
| GP | 518,500 | 370,837 | 266,121 | 296 |
| KZN | 1,329,112 | 800,177 | 648,609 | 69 |
| LP | 611,680 | 379,471 | 377,484 | 74 |
| MP | 565,489 | 419,066 | 344,629 | 231 |
| NW | 617,720 | 331,103 | 171,561 | 332 |
| NC | 150,600 | 51,227 | 28,054 | 7 |
| WC | 330,340 | 231,913 | 231,913 | 22 |

**Data quality notes:**
1. FS doses_received conflict: formal JOC 838,400 vs AgriSA-NAT verbal 1,100,000 (3 June). FS-JOC authoritative.
2. FS animals_vaccinated 707,986 (FS-DARDEA media release, map 4 June) covers all cattle vaccinated with Biogenesis Bago + DolVet. Component breakdown from Mangaung district (xlsx) sums to 512,194 -- remainder from other districts not captured in xlsx detail rows.
3. EC positive_cases conflict: EC-DRDAR 361 (confirmed only) vs AgriSA-NAT 566 (qualifier ambiguous). Both rows held.
4. MPO Week 32 still missing from inbox -- gap in dairy data between 22 May and 5 June.
5. FS-DARDEA media release references Government Gazette No. 51512 of 13 June 2025 for quarantine regulations -- distinct from Section 9 gazette still outstanding.

**Parked/outstanding:**
- Consolidated AgriSA weekly xlsx: ~18 days outstanding. Urgent.
- Section 9 gazette: ~15 days overdue. Urgent.
- MPO Week 32 -- not received; gap in dairy time series.
- LP DolVet 150,000 receipt -- outstanding.
- LP Biogenesis depot at 0 -- urgent replenishment required.
- NW: DDG Serage engagement outcome + Biogenesis reinfection investigation.
- EC: confirm 361 vs 566 cases; confirm 18,730 doses gap.
- SAPPO: bottles-to-doses conversion + unknown province (2026-05-25) follow-up.
- Dollvet 4M first consignment -- expected June 2026; monitor RMIS.
- Next FMD Weekly Engagement: 10 June 2026 (tomorrow).
- KZN booster programme -- started 8 June; monitor progress.
- GP OBP column-mapping -- ongoing.
- FMD_Membership_Report_08June2026.pdf in root folder -- generated AgriSA report; no new data to ingest.

---

*Session 31 (08 June 2026): 1,468 rows; dashboard 3 June 2026 (26 weekly points). EC 3 June JOC ingest + dashboard restore.*

---

As at 2026-06-08 (session 31 -- EC 3 June JOC ingest + dashboard restore):
- Master: **1,468 rows** (+13 new rows from 1,455)
- Dashboard snapshot: **3 June 2026** (unchanged; 26 weekly points, validation passed)
- Dashboard rebuilt: Yes -- FMD_Dashboard.html (161,323 bytes); full visual restoration (tabs, MPO, SAPPO, RMIS, drill-down)

**Key highlights (session 31):**
- EC 3 June EC-DRDAR JOC ingested (13 rows): positive_cases 361 (conflicts with AgriSA-NAT 566 -- both held); suspected 237; doses_received total 1,000,660 (breakdown gap 18,730 flagged); doses_administered total 833,113.
- EC Artio-PREVA 1,250 duplication (21 May) superseded.
- Dashboard visual regression from sessions 29--30 fixed: build_dashboard.py and dashboard_template.html restored from commit fe5dc99.

**National dashboard (3 June 2026 snapshot):**
- Doses distributed: 5,875,790
- Doses administered: 3,556,621
- Animals vaccinated: 3,416,885
- Positive cases: 2,201 (EC 361 per EC-DRDAR confirmed / 566 per AgriSA-NAT; FS 604; GP 296; KZN 69; LP 74; MP 231; NW 332; NC 7; WC 22)
- Suspected cases: 920

**Per-province (3 June 2026):**

| Province | Distributed | Administered | Animals vaccinated | Positive |
|---|---|---|---|---|
| EC | 1,000,660 | 833,113 (dose-count) | 833,113 | 361 (EC-DRDAR) / 566 (AgriSA-NAT) |
| FS | 1,100,000 | 482,848 | 609,900 | 604 |
| GP | 518,500 | 370,837 | 266,121 | 296 |
| KZN | 1,329,112 | 800,177 | 648,609 | 69 |
| LP | 611,680 | 379,471 | 377,484 | 74 |
| MP | 565,489 | 419,066 | 344,629 | 231 |
| NW | 617,720 | 331,103 | 171,561 | 332 |
| NC | 150,600 | 51,227 | 28,054 | 7 |
| WC | 330,340 | 231,913 | 231,913 | 22 |

**Parked/outstanding:**
- Consolidated AgriSA weekly xlsx: 17 days outstanding. Urgent.
- Section 9 gazette: ~14 days overdue. Urgent.
- MPO Weeks 32+33 -- not received.
- LP DolVet 150,000 receipt -- outstanding.
- LP Biogenesis allocation -- depot at 0; urgent.
- NW: DDG Serage engagement + Biogenesis reinfection investigation.
- EC: confirm 361 vs 566 cases; confirm 18,730 doses gap.
- SAPPO: bottles-to-doses conversion + unknown province (2026-05-25) follow-up.
- Dollvet 4M first consignment -- expected June 2026; monitor RMIS.
- Next FMD Weekly Engagement: 10 June 2026.
- KZN booster -- ongoing.
- GP OBP column-mapping -- ongoing.