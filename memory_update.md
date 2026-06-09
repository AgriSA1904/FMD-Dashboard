---
name: FMD daily run state
description: Latest master_data.csv row count and dashboard snapshot
type: project
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
