---
name: FMD daily run state
description: Latest master_data.csv row count and dashboard snapshot
type: project
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

**Data quality notes:**
1. EC positive_cases conflict: EC-DRDAR 361 (confirmed only) vs AgriSA-NAT 566 (qualifier ambiguous). Both rows held. Confirm with EC-DRDAR.
2. EC doses_received stated total 1,000,660; breakdown sums to 981,930 -- gap of 18,730 unaccounted.
3. EC Bioaftogen administered (367,694) marginally exceeds received (367,000) -- pre-period stock draw.
4. EC animals_vaccinated 833,113 is dose-count; unique-animals figure not provided.
5. FS doses_received 1,100,000 and animals_vaccinated 609,900 remain approximate verbal-report figures.
6. MP 344,629 (commercial+communal): excludes private vet channel.

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

---

*Session 30 (08 June 2026): 1,455 rows; dashboard 3 June 2026 (26 weekly points). FS-JOC column-mapping correction only; no new source data.*

---

As at 2026-06-08 (session 30 -- automated daily ingest, no new sources; data quality correction):
- Master: **1,455 rows** (+5 rows from 1,450; 3 rows superseded with versioned corrections)
- Dashboard snapshot: **3 June 2026** (unchanged; corrections did not affect dashboard-facing calculations)
- Dashboard rebuilt: Yes -- FMD_Dashboard.html (93,631 bytes), validation passed

**Key highlights:**

- No new source data in inbox today. The file AgriSA Weekly FMD Engagement 2026.06.10.pdf is the agenda for the 10 June meeting (meeting date 10 June; today is 8 June). No data to extract.
- Data quality correction: FS-JOC 29 May xlsx had a 3-column offset error in its prior ingest. Three rows supers