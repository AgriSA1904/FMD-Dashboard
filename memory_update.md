---
name: FMD daily run state
description: Latest master_data.csv row count and dashboard snapshot
type: project
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
- FS animals vaccinated updated to 707,9