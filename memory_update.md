As at 2026-09-15 (session 75 -- Cowork scheduled run, shell healthy, full backlog cleared -- master now **3,597 rows**, 265 rows added; **dashboard rebuilt, snapshot 11 September 2026, 82 weekly points, validation passed**):

**Session 75 (15 Sep, FS 28 Aug / 4 Sep / 11 Sep, EC 27 Aug / 3 Sep / 10 Sep, LP Week 39 and Week 41, RMIS 3 Sep xlsx):**

- Free State: confirmed cases 783 -> 795 -> 796 (11 Sep), 604 resolved, 192 active, 19 municipalities. First vaccinations 1,643,655 (11 Sep). Doses received 1,961,840 (4 Sep; cell blank on 28 Aug and 11 Sep templates). Suspected 266 (4 Sep only).
- Eastern Cape: confirmed outbreaks 500 -> 501 -> 506 (10 Sep), suspected 228. Vaccine received 1,939,510 (27 Aug) -> 2,174,510 (10 Sep). Doses administered (dose-count basis) 1,615,211, usage 74.2 percent, coverage 42.7 percent. Dairy boosters 163,038. Fixed the stalled EC positive_cases series (was 459 since 16 Jul) by mirroring the August reported_outbreaks rows.
- Limpopo: animals vaccinated 956,974 (cattle 880,162, 73.3 percent of 1.2 million) to 11 Sep; register received 1,225,660, issued 1,144,725, used 971,866, usable 167,757. Positive 101 (down from 110 through Section 23 closures; confirmed incl closed 136), suspected 73, pending 124; no new cases sampled since 28 Aug. Booster campaign about to launch; 36 AHTs appointed; 250,000 RFID tags delivered.
- RMIS industry channel to 3 Sep: 2,814,006 doses shipped (Biogenesis 2,068,984, Dollvet 745,022); feedlot 1,785,576, commercial 822,180, stud 199,505, dairy 6,745.
- Dashboard rebuilt via importlib: snapshot 21 Aug -> 11 Sep 2026, 82 weekly points, 315,454 bytes. National: positive 2,834, suspected 896, distributed 10,174,110, administered 8,989,076, balance 1,185,034.
- The 14 Sep "update-status FAILED" note in `AgriSA FMD Updates/` came from a shell-less task and its "last rebuilt session 52" claim is wrong; ignore it.

## Publishing

- **GitHub Pages** (primary public site): https://AgriSA1904.github.io/FMD-Dashboard/. Push per the pattern in CLAUDE.md (clone `AgriSA1904/FMD-Dashboard`, copy `FMD_Dashboard.html` as both itself and `index.html` plus `master_data.csv`, `change_log.md`, `memory_update.md`, `scripts/build_dashboard.py`, commit, push to `main`). Session 75 push: see change_log session 75 GitHub section.
- **Claude Artifact** (added session 73): https://claude.ai/code/artifact/c6f5c0bc-212c-4ac9-8946-8fe3f2c5a9f4. Republish by taking the freshly rebuilt `FMD_Dashboard.html`, stripping the outer `<!DOCTYPE>`/`<html>`/`<head>`/`<body>` wrapper, and republishing to the same URL. Session 75: attempted after the GitHub push; result recorded in change_log.

## National programme headline (dashboard, 11 September)

Positive cases 2,834; suspected 896; doses distributed 10,174,110; administered 8,989,076; balance 1,185,034. Last ICC basis remains 4 August (positive 2,725; distributed 8,529,687; administered 6,249,525); the ICC update covering the 11 August Ministerial Task Team meeting is more than five weeks overdue.

## Per-province latest figures (programme sources only)

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 2,174,510 | 1,615,211 (dose-count basis) | 506 outbreaks, 228 suspected | 10 Sep |
| FS | 1,961,840 (4 Sep) | 1,643,655 | 796 (266 suspected at 4 Sep) | 11 Sep |
| GP | 643,300 (approx 800,000 per 24 Jul minutes, unconfirmed) | 527,626 | 307 | 29 Jul |
| KZN | 1,120,000 / 1,329,112 (stale, Jun) | 1,700,000 (MEC, rounded) | 336 (stale, 5 Jun) | 20 Aug |
| LP | 1,225,660 (register; issued 1,144,725) | 956,974 | 101 (73 suspected; 136 incl closed) | 11 Sep |
| MP | 897,000 | 729,074 | 259 | 27 to 31 Jul |
| NW | 1,271,140 | 1,172,333 (Portal) / 1,220,669 (spreadsheet, 25 Jul) | 478 (115 suspected) | 11 Aug |
| NC | 333,560 | 215,546 | 40 outbreaks (dashboard positive_cases 22) | 5 Aug |
| WC | 547,100 | 428,657 | 35 outbreaks (GIS 29 retained) | 30 to 31 Jul |

## Known data quality issues, carry forward awareness

1. NC 25 March: vaccinated 23,000 exceeds received 18,846 because of a pre-period stock draw. Expected behaviour.
2. EC `animals_vaccinated all/all` figures are dose-count totals and double-count animals receiving more than one dose. Corrected unique-animals figure pending past 7 May (309,935).
3. EC Alfred Nzo district: 450 doses labelled BVI in the xlsx, ARC in the pptx. Unresolved.
4. WC AWC/RPO methodology (449,370 received) versus WC-GIS portal (547,100 latest). Both held; GIS portal figure used.
5. WC dairy cows Week 28 vs Week 29 -- MPO methodology change.
6. KZN suspected case in vaccinated herd (MPO) -- booster programme expected; monitor.
7. FS 8 May DolVet 466,100 originally recorded as Bioaftogen. Flagged in notes, not corrected.
8. GP OBP distributed 1,700 versus administered 127,580 in a prior template upload -- likely column mapping, unresolved.
9. NW doses_received 1,271,140 (summary slide) versus 1,350,140 (allocation table incl RPO) -- unresolved since 16 Jul.
10. NW animals_vaccinated: FMD Portal 1,172,333 (11 Aug) versus internal spreadsheet 1,220,669 (25 Jul). Dashboard shows the Portal figure as the latest row.
11. NW per-municipality case detail not machine-readable from the 11 Aug PDF.
12. **EC internal inconsistencies (session 75):** 10 Sep summary slide still shows 501 outbreaks versus 506 in the outbreak-control table; 3 Sep summary total 1,548,788 versus sector total 1,545,729; 27 Aug "previously reported 497" versus 498 closed on 20 Aug.
13. **LP received basis (session 75):** 11 Sep row uses register total received (1,225,660); earlier rows used doses issued to districts. Capricorn/Vhembe transfer not yet reconciled in the register.
14. **LP positive_cases falls as cases close** (110 -> 101) because closed cases are held separately; use confirmed-incl-closed (136) when comparing with other provinces' cumulative counts.
15. **FS template gaps:** provincial received cell blank on 28 Aug and 11 Sep; suspected n/a on 28 Aug and 11 Sep.

## Automation health

Cowork scheduled runs are the only reliable ingest path. The local Claude CLI was still failing with 401 OAuth at last check (late August). The Windows scheduled task (`ingest.py`) runs daily but only reprocesses the same static Mpumalanga file and pushes empty "Update FMD dashboard" commits to GitHub (4 and 14 Sep); it does not advance data.

## Parked/outstanding

- ICC Update PDF covering the 11 August Ministerial Task Team meeting, plus the rollout plan for the Minister. More than five weeks overdue.
- MPO Week 47 update (due around 11 Sep) not yet in the inbox.
- KZN doses received and official case count (stale since June).
- Gauteng exact doses received (approximately 800,000 per 24 Jul minutes; last precise 643,300).
- FS provincial received and suspected cases for 28 Aug and 11 Sep (blank / n/a in templates).
- LP: confirm received basis, Capricorn/Vhembe reconciliation, booster campaign launch figures (to be a distinct series), Mopani lab backlog (66).
- EC unique-animals versus dose-count basis; EC summary-slide staleness.
- Sarah Baartman: 3 new confirmed outbreaks at 10 Sep (41 total) following the 20 Aug kudu suspects -- watch.
- Mpumalanga reconciliation queries; Biogenesis Bago 1.5 million provincial split; Section 10 follow-ups; ICC Terms of Reference.
- North West allocation confirmation (1,271,140 versus 1,350,140) and district-level case breakdown.
- Consolidated AgriSA weekly xlsx, now more than 145 days outstanding.
- Western Cape case-count basis and AWC/RPO methodology gap.
- NC booster campaign due to start August 2026; no booster figures seen yet.
- Re-authenticate the local Claude CLI; disable or fix the Windows scheduled task's empty commits.
- Republish the Claude Artifact alongside every GitHub Pages push.
