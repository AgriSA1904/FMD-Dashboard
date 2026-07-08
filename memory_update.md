As at 2026-07-08 (session 54 -- NW-RPO 7 Jul JIC update):
- Master: **2,353 rows** (+35: all NW-RPO, week 26 Jun-3 Jul 2026)
- Dashboard snapshot: **3 July 2026** (54 weekly points; 220,966 bytes; validation passed)
- Dashboard rebuilt: Yes -- North West now current to 3 Jul 2026.

**New data ingested (session 54):**
- `07 JULY 2026- RPO JIC FMD UPDATE_.pdf` (NW-RPO, effective 3 Jul 2026): 35 rows. 18-page slide pack; text extracted with pypdf (charts/maps are images and were not needed for the figures).
  - positive_cases 445 confirmed outbreaks (up from 421 at 25 Jun, +24). 421 reported to WOAH; 24 still to report. Regions: DKK 88, Bojanala 79, DRSM 188, NMM 90. Full 20-office breakdown captured.
  - new_cases_week 24 (26 Jun-3 Jul): Kagisano Molopo 15, Naledi 2, Greater Taung 2, Mamusa 1, Ratlou 2, Maquassi Hills 1, Madibeng 1. All PCR tissue/swab except Madibeng (serology NSP).
  - Vaccine received (cumulative) now 1,271,140 -- up from 1,021,140, driven by a new Aftodoll 09AFT26 batch of 250,000 (0 used so far). Supersedes the 18 Jun cumulative of 1,021,140.
  - Doses administered per batch: OVR 1,291; Bioaftogen 1185 99,678; Aftodoll 15AFT25 Gov 47,712; Aftodoll 15AFT25 Emergency 24,171; Bioaftogen 1186 first 59,935; Aftodoll 03AFT25 Gov 219,928; Aftodoll 03AFT25 Feedlot 81,346; Aftodoll 05AFT26 299,116; Bioaftogen 1186 11 Jun 86,241. Page-10 usage total 919,318; per-batch sum 919,418 (source rounding, 100 diff, noted).
  - Animals vaccinated: internal spreadsheet 892,119 (92pct with spillages) -- unchanged from 30 Jun, flagged as possibly stale; FMD Portal 942,566 (74pct of 1,271,140). Vaccine coverage 42pct against census of 2,196,694.
  - Update note: the Section 9 Contingency Plan for FMD has been approved by the Minister and awaits gazetting before it can be used.

**National (programme sources only) as at this run:**
- Doses received 7,800,322; animals vaccinated 5,358,243; positive cases 2,575; suspected cases 965.

**Per-province latest figures (8 July 2026):**

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 1,064,230 | 1,026,694 | 423 | 2 Jul |
| FS | 1,272,180 | 1,106,191 | 648 | 26 Jun |
| GP | 643,300 | 405,404 | 306 | 24 Jun |
| KZN | 1,329,112 | 648,609 (UNOFFICIAL) | 336 | 9 Jun |
| LP | 775,660 | 520,185 | 95 | 26 Jun |
| MP | 747,000 | 344,629 | 261 | 22 Jun |
| NW | 1,271,140 | 892,119 (internal) | 445 | 3 Jul |
| NC | 200,600 | 114,443 | 22 | 26 Jun |
| WC | 497,100 | 299,969 | 39 | 29 Jun |

**Parked/outstanding (carry forward):**
- NW internal spreadsheet animals-vaccinated figure (892,119) unchanged from 30 Jun -- confirm whether stale; page-10 usage total is 919,318 and FMD Portal is 942,566.
- NW new Aftodoll 09AFT26 batch (250,000) received but 0 administered as at 3 Jul -- track uptake next update.
- 8 July FMD Weekly Engagement outcomes (agenda already received; outcomes pending).
- Section 9 / Section 10 gazette: Section 9 Contingency Plan approved by Minister, awaiting gazetting.
- Consolidated AgriSA weekly xlsx: ~100+ days outstanding. Longstanding gap in national reconciliation.
- KZN official JOC documents outstanding; current figures UNOFFICIAL and now stale (9 Jun).
- KZN vaccine shortage: 1,500,000 more doses requested urgently.
- LP DolVet 150,000 receipt -- still unconfirmed as at 26 Jun.
- LP Biogenesis 99,020 vs 100,020 discrepancy -- unresolved.
- GP OBP distributed vs administered column-mapping concern (carried).
- Automated daily-run auth failure (401) on 2026-07-06 -- check CLI credentials before relying on the unattended run.
