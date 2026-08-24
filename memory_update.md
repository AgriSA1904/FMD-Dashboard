As at 2026-08-24 (session 69 -- scheduled daily inbox ingest; EC JOC decks and RMIS export):

- Master: **3,085 rows** (was 2,948; 137 added). Dashboard snapshot advanced to **20 August 2026**; weekly points 73. Rebuild via importlib, validation passed (278,464 bytes).
- New sources this session: three Eastern Cape provincial JOC decks (EC FMD Update 6, 13 and 20 August, Teams screenshot slides read visually) and the RMIS industry vaccine distribution export of 17 August (orders shipped through 11 August).
- **EC received jumps to 1,786,510.** The JOC allocation table gives state 1,423,510 plus MPO 302,000 plus RPO 61,000, including a Biogenesis consignment of 259,980 received 4 August. This conflicts with the Portfolio Committee figure of 1,527,230 (5 Aug); both held by source and date. The JOC series is now the EC received channel.
- **EC vaccination weekly series restored:** 1,299,271 (6 Aug), 1,346,933 (13 Aug), 1,378,088 (20 Aug), all dose-count basis, usage 77.1 percent at 20 August, coverage 36.5 percent of an estimated 3,775,342 cattle.
- **EC outbreaks:** 491 (6 Aug), 496 (13 Aug), 498 confirmed and 229 suspected (20 Aug). The two new suspects at 20 August are kudu in Sarah Baartman -- second wildlife signal after the earlier KZN vaccinated-herd suspect.
- **RMIS industry channel** as at 16 August: 2,580,315 doses distributed nationally (Biogenesis 2,060,239, Dollvet 520,076). A new Dairy sector channel appears in the export for the first time (vet_channel "dairy").

**National programme headline (unchanged ICC basis, 4 August):** positive cases 2,725; doses distributed 8,529,687; administered 6,249,525; balance 2,280,162. The ICC update covering the 11 August Ministerial Task Team meeting remains outstanding (about two weeks overdue); bottom-up provincial sums continue to run ahead of the ICC administered figure and reconciliation is the key check when it lands.

**Per-province latest figures (programme sources only):**

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 1,786,510 (JOC; PC 1,527,230 held) | 1,378,088 (dose-count basis) | 498 outbreaks, 229 suspected | 20 Aug |
| FS | 1,272,180 (stale, 10 Jul) | 1,458,124 | 764 | 6 Aug |
| GP | 643,300 (approx 800,000 per 24 Jul minutes, unconfirmed) | 527,626 | 307 | 29 Jul |
| KZN | 1,329,112 (stale, 9 Jun) | 1,567,971 (OFFICIAL) | 336 (stale, 5 Jun) | 26 Jul |
| LP | 994,725 | 758,379 | 109 | 31 Jul |
| MP | 897,000 | 729,074 | 259 | 27 to 31 Jul |
| NW | 1,271,140 | 1,220,669 | 476 | 25 Jul |
| NC | 333,560 | 215,546 | 40 outbreaks (basis change) | 5 Aug |
| WC | 547,100 | 428,657 | 35 outbreaks (GIS 29 retained) | 30 to 31 Jul |

**New data quality flags (session 69):**

- EC received conflict: JOC 1,786,510 versus Portfolio Committee 1,527,230 (5 Aug). Both held; JOC includes industry consignments and the 4 August batch.
- EC JOC slide vaccine-type totals (Biogenesis 467,831, Dollvet 646,650, ARC OVI 2,177, BVI 1,250) are identical across the 6, 13 and 20 August decks and do not sum to the weekly totals; treated as stale and not ingested as type splits.
- EC dose-count caveat still applies to animals vaccinated (boosters double-counted).
- RMIS introduces a Dairy sector channel; recorded as vet_channel "dairy" alongside commercial, feedlot and stud.

**Automation health:** local Claude CLI still failing with 401 OAuth (latest failures 20 and 21 August in scripts/ingest_task_log.txt; a 19 August run appears to have completed its wrapper but the 20 August run hit the 401). No local run entries for 22 to 24 August. This Cowork session remains the reliable ingest path.

**Parked/outstanding:**

- ICC Update PDF covering the 11 August Ministerial Task Team meeting, plus the rollout plan for the Minister. Still not arrived; about two weeks overdue.
- FS doses received figure (stale since 10 Jul and below animals vaccinated).
- KZN doses received and official case count (received stale since 9 Jun; cases since 5 Jun).
- Gauteng exact doses received (approximately 800,000 per 24 Jul minutes; last precise 643,300).
- EC unique-animals versus dose-count basis; EC internal 5,022 gap between used and vaccinated totals (5 Aug).
- Sarah Baartman kudu suspects (20 Aug) -- watch for confirmation; wildlife involvement would matter to the ICC.
- Mpumalanga reconciliation queries (in-hand and loss totals; Bioaftogen 3 quantity).
- Biogenesis Bago 1.5 million provincial split; Section 9 and Section 10 follow-ups; ICC Terms of Reference.
- North West allocation confirmation (1,271,140 versus 1,350,140) and spreadsheet versus FMD Portal gap.
- Consolidated AgriSA weekly xlsx, now more than 135 days outstanding.
- Limpopo incoming batches, the 2 million doses referenced in the 24 July minutes, and the two Section 11 district lines.
- Western Cape case-count basis (three counts held) and AWC/RPO methodology gap.
- NC booster campaign due to start August 2026; no booster figures seen yet.
- Re-authenticate the local Claude CLI and check the Windows scheduled task trigger.
- GitHub: session 69 push done this session; verify remote HEAD next run.
