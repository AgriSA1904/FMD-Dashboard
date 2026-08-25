As at 2026-08-25 (session 70 -- scheduled daily inbox ingest; FS-DARDLEA weekly stats pack, 14 August):

- Master: **3,095 rows** (was 3,085; 10 added). Dashboard snapshot unchanged at **20 August 2026** (the new data is dated 14 Aug, older than the existing EC-driven snapshot); weekly points now 74. Rebuild via importlib, validation passed (281,563 bytes).
- New source this session: Free State FMD STATS 14 AUGUST 2026.zip (FS-DARDLEA), containing the weekly xlsx template plus a two-page ministerial-style media release. Only new file found in the inbox since the last run; no other provincial folders had material newer than the 24 August build.
- **FS positive cases: 770** per the 14 August media release (up from 764 at 6 Aug; six new cases -- Kroonstad SVA 1, Bloemfontein SVA 3, Welkom SVA 2). 551 resolved, 219 active under quarantine, spread across 19 local municipalities. The accompanying xlsx template states 769 (one less); both held, same rounding-gap pattern seen in prior FS releases.
- **FS animals vaccinated: 1,485,340** (up from 1,458,124 at 6 Aug; +27,216), again reported as a standalone summary cell with the municipality-level vaccination table left blank. FS doses received remains stale at 1,272,180 (10 Jul) except for one district figure: Mangaung received 370,000 Bioaftogen doses and vaccinated 2,231 animals with OBP dose 1 this week -- the only district with non-zero vaccine entries in the template.
- District-level positive case totals held steady versus 6 Aug for Fezile Dabi (366), Thabo Mofutsanyana (193) and Xhariep (42); Lejweleputswa rose from 136 to 138.

**National programme headline (unchanged ICC basis, 4 August):** positive cases 2,725; doses distributed 8,529,687; administered 6,249,525; balance 2,280,162. The ICC update covering the 11 August Ministerial Task Team meeting remains outstanding (now about three weeks overdue).

**Per-province latest figures (programme sources only):**

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 1,786,510 (JOC; PC 1,527,230 held) | 1,378,088 (dose-count basis) | 498 outbreaks, 229 suspected | 20 Aug |
| FS | 1,272,180 (stale, 10 Jul) | 1,485,340 | 770 | 14 Aug |
| GP | 643,300 (approx 800,000 per 24 Jul minutes, unconfirmed) | 527,626 | 307 | 29 Jul |
| KZN | 1,329,112 (stale, 9 Jun) | 1,567,971 (OFFICIAL) | 336 (stale, 5 Jun) | 26 Jul |
| LP | 994,725 | 758,379 | 109 | 31 Jul |
| MP | 897,000 | 729,074 | 259 | 27 to 31 Jul |
| NW | 1,271,140 | 1,220,669 | 476 | 25 Jul |
| NC | 333,560 | 215,546 | 40 outbreaks (basis change) | 5 Aug |
| WC | 547,100 | 428,657 | 35 outbreaks (GIS 29 retained) | 30 to 31 Jul |

**New data quality flags (session 70):**

- FS positive cases: media release states 770, xlsx template states 769; State Vet Area breakdown in the media release itself sums to 769, one short of its own stated total. Consistent with a recurring FS off-by-one pattern.
- FS animals-vaccinated total (1,485,340) is again a manually-entered summary figure disconnected from the (blank) municipality-level table -- cannot be cross-checked against a per-district sum this week.
- FS doses received still has no provincial-level update; only Mangaung reported a district figure (370,000 Bioaftogen).

**Automation health:** local Windows-scheduled Claude CLI run continues to fail with 401 OAuth expiry (confirmed again at 08:00 on 25 Aug in scripts/ingest_task_log.txt; same failure every day since at least 17 Aug). This Cowork scheduled session remains the only ingest path actually landing data. Re-authentication of the local CLI is still outstanding.

**Parked/outstanding:**

- ICC Update PDF covering the 11 August Ministerial Task Team meeting, plus the rollout plan for the Minister. Still not arrived; about three weeks overdue.
- FS doses received figure (stale since 10 Jul and below animals vaccinated).
- KZN doses received and official case count (received stale since 9 Jun; cases since 5 Jun).
- Gauteng exact doses received (approximately 800,000 per 24 Jul minutes; last precise 643,300).
- EC unique-animals versus dose-count basis; EC internal 5,022 gap between used and vaccinated totals (5 Aug).
- Sarah Baartman kudu suspects (20 Aug) -- watch for confirmation; wildlife involvement would matter to the ICC.
- Mpumalanga reconciliation queries (in-hand and loss totals; Bioaftogen 3 quantity).
- Biogenesis Bago 1.5 million provincial split; Section 9 and Section 10 follow-ups; ICC Terms of Reference.
- North West allocation confirmation (1,271,140 versus 1,350,140) and spreadsheet versus FMD Portal gap.
- Consolidated AgriSA weekly xlsx, now more than 136 days outstanding.
- Limpopo incoming batches, the 2 million doses referenced in the 24 July minutes, and the two Section 11 district lines.
- Western Cape case-count basis (three counts held) and AWC/RPO methodology gap.
- NC booster campaign due to start August 2026; no booster figures seen yet.
- Re-authenticate the local Claude CLI and check the Windows scheduled task trigger.
- GitHub: session 70 push done this session; verify remote HEAD next run.
