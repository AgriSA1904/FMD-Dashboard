---
name: FMD daily run state
description: Latest master_data.csv row count and dashboard snapshot
type: project
---

As at 2026-06-08 (session 30 -- automated daily ingest, no new sources; data quality correction):
- Master: **1,455 rows** (+5 rows from 1,450; 3 rows superseded with versioned corrections)
- Dashboard snapshot: **3 June 2026** (unchanged; corrections did not affect dashboard-facing calculations)
- Dashboard rebuilt: Yes -- FMD_Dashboard.html (93,631 bytes), validation passed

**Key highlights:**

- No new source data in inbox today. The file AgriSA Weekly FMD Engagement 2026.06.10.pdf is the agenda for the 10 June meeting (meeting date 10 June; today is 8 June). No data to extract.
- Data quality correction: FS-JOC 29 May xlsx had a 3-column offset error in its prior ingest. Three rows superseded and five corrected/new rows added. Corrections affect component-level breakdown only; dashboard headline figures unaffected (build script uses vaccine_type=all).

Correction detail:
- Row superseded: doses_received obp_arc val=199899 (was Bioaftogen Dose 1 Total from col[22]); corrected to val=2300.
- Row superseded: animals_vaccinated_dose1 bioaftogen val=193164 (was DolVet Dose 1 col[30]); corrected to val=199899.
- Row superseded: animals_vaccinated_dose1 dolvet val=2231 (was OBP Dose 1 col[38]); corrected to val=193164.
- New row: animals_vaccinated_dose1 obp_arc val=2231 (missed in prior ingest).
- New row: animals_vaccinated_dose2 bioaftogen val=116900 (Bioaftogen second doses; missed in prior ingest).

**National dashboard (3 June 2026 snapshot -- unchanged):**
- Doses distributed: 5,875,790
- Doses administered: 3,556,621
- Animals vaccinated: 3,416,885
- Positive cases: 2,201 (EC 566; FS 604; GP 296; KZN 69; LP 74; MP 231; NW 332; NC 7; WC 22)
- Suspected cases: 920

**Per-province (3 June 2026):**

| Province | Distributed | Administered | Animals vaccinated | Positive |
|---|---|---|---|---|
| EC | 652,349 | 489,979 | 738,614 | 566 |
| FS | 1,100,000 | 482,848 | 609,900 | 604 |
| GP | 518,500 | 370,837 | 266,121 | 296 |
| KZN | 1,329,112 | 800,177 | 648,609 | 69 |
| LP | 611,680 | 379,471 | 377,484 | 74 |
| MP | 565,489 | 419,066 | 344,629 | 231 |
| NW | 617,720 | 331,103 | 171,561 | 332 |
| NC | 150,600 | 51,227 | 28,054 | 7 |
| WC | 330,340 | 231,913 | 231,913 | 22 |

**Data quality notes:**
1. EC positive_cases 566: stated without confirmed/suspected qualifier; cross-check with EC-DRDAR required.
2. FS doses_received 1,100,000 and animals_vaccinated 609,900: approximate verbal-report figures.
3. MP 344,629 (commercial+communal): lower than ministerial floor >430,000 -- excludes private vet channel.
4. SAPPO rep corrections: 2026-05-05 NW 37 ML->TC; 2026-05-12 FS 8 TC->ML (no dashboard impact).
5. SAPPO 2026-05-25 unknown province -- follow up with Dr Chiappero.
6. FS-JOC 29 May: corrected component-level dose breakdown. Bioaftogen Dose 2 = 116,900 confirmed (second-dose programme under way). OBP Dose 1 = 2,231. No dashboard impact.

**Parked/outstanding:**
- Consolidated AgriSA weekly xlsx: 17 days outstanding (last 22 May). Urgent.
- MPO Weeks 32+33 -- not received.
- Section 9 gazette: ~14 days overdue. Urgent.
- LP DolVet 150,000 receipt -- outstanding.
- LP Biogenesis allocation -- depot at 0; urgent.
- NW: DDG Serage engagement + Biogenesis reinfection investigation.
- EC: confirm 566 cases qualifier with EC-DRDAR.
- SAPPO: bottles-to-doses conversion + unknown province follow-up.
- Dollvet 4M first consignment -- expected June 2026; monitor RMIS.
- FMD Weekly Engagement summary: 10 June meeting (agenda received; summary expected after meeting).
- KZN booster -- ongoing.
- EC Artio-Preva duplication -- pending.
- GP OBP column-mapping -- ongoing.

---

*Session 29 (07 June 2026): 1,450 rows; dashboard 3 June 2026 (26 weekly points). Sources: 3 June weekly engagement summary + SAPPO 5 June email.*
