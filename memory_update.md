As at 2026-08-28 (session 73 -- Cowork run at Jay's request: ingested the North West RPO JIC update of 11 August 2026, rebuilt the dashboard, and published it as a Claude Artifact alongside the existing GitHub Pages site -- master now **3,278 rows**, four rows added):

**Session 73 (28 Aug, NW RPO JIC 11 Aug ingest):**

- Full inbox scan found one new file since the session 71c/71d/71e runs of 26 August: `inbox/North West/11 AUGUST 2026- RPO JIC FMD UPDATE_.pdf`. Extracted: cumulative confirmed cases 478 (up from 476 at 25 Jul), suspected cases 115 (first dedicated NW suspected-cases figure in months), closed cases 142 and active cases 336 per the source (recorded in notes, not as separate rows -- no established metric name for "closed" in this schema). Doses received 1,271,140 (unchanged from 25 Jul -- stale carried-forward slide, consistent with this document family's pattern). Animals vaccinated (FMD Portal) 1,172,333 -- **lower** than the 1,220,669 internal-spreadsheet figure already held for 25 Jul, flagged as a counting-method gap rather than an actual decrease; not used to replace the higher trend figure.
- NW per-municipality case table (20 state vet offices) did not parse reliably from the PDF text extraction; only province-level confirmed/suspected totals were captured. District-level detail (DKK/Bojanala/DRSM/NMM) needs a manual re-check if required.
- Dashboard rebuilt via importlib: snapshot unchanged at 21 August 2026, weekly points 75 -> 76, validation passed (298,900 bytes).
- Pushed to GitHub Pages as usual, and also published as a Claude Artifact for the first time: https://claude.ai/code/artifact/c6f5c0bc-212c-4ac9-8946-8fe3f2c5a9f4. This Artifact should be republished (same URL) whenever the dashboard is rebuilt going forward, in addition to the GitHub Pages push -- see "Publishing" below.

## Publishing

- **GitHub Pages** (primary public site): https://AgriSA1904.github.io/FMD-Dashboard/. Push per the pattern in CLAUDE.md (clone `AgriSA1904/fmd-dashboard`, copy `FMD_Dashboard.html` as both itself and `index.html` plus `master_data.csv`, `change_log.md`, `memory_update.md`, `scripts/build_dashboard.py`, commit, push to `main`).
- **Claude Artifact** (added session 73): https://claude.ai/code/artifact/c6f5c0bc-212c-4ac9-8946-8fe3f2c5a9f4. A hosted claude.ai copy of the same dashboard, useful for sharing a direct link without the GitHub Pages hop. Republish by reading this URL, taking the freshly rebuilt `FMD_Dashboard.html`, stripping the outer `<!DOCTYPE>`/`<html>`/`<head>`/`<body>` wrapper (the Artifact tool supplies its own), and republishing to the same URL so it stays live rather than creating a new page each time.

## National programme headline (unchanged ICC basis, 4 August)

Positive cases 2,725; doses distributed 8,529,687; administered 6,249,525; balance 2,280,162. The ICC update covering the 11 August Ministerial Task Team meeting remains outstanding (more than three weeks overdue).

## Per-province latest figures (programme sources only)

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 1,786,510 (JOC; PC 1,527,230 held) | 1,378,088 (dose-count basis) | 498 outbreaks, 229 suspected | 20 Aug |
| FS | 1,741,840 | 1,512,319 | 772 (273 suspected) | 21 Aug |
| GP | 643,300 (approx 800,000 per 24 Jul minutes, unconfirmed) | 527,626 | 307 | 29 Jul |
| KZN | 1,329,112 (stale, 9 Jun) | 1,700,000 (MEC, rounded) | 336 (stale, 5 Jun) | 20 Aug |
| LP | 994,725 | 758,379 | 109 | 31 Jul |
| MP | 897,000 | 729,074 | 259 | 27 to 31 Jul |
| NW | 1,271,140 | 1,220,669* | 478 (115 suspected) | 11 Aug (cases); 25 Jul (received/vaccinated) |
| NC | 333,560 | 215,546 | 40 outbreaks (basis change) | 5 Aug |
| WC | 547,100 | 428,657 | 35 outbreaks (GIS 29 retained) | 30 to 31 Jul |

\* NW animals vaccinated: retaining the 25 Jul internal-spreadsheet figure (1,220,669) as the trend value. The 11 Aug FMD Portal figure (1,172,333) is lower and held as a separate, flagged data point -- see session 73 note above.

## Known data quality issues, carry forward awareness

1. NC 25 March: vaccinated 23,000 exceeds received 18,846 because of a pre-period stock draw. Expected behaviour.
2. EC `animals_vaccinated all/all` figures are dose-count totals and double-count animals receiving more than one dose. Corrected unique-animals figure pending past 7 May (309,935).
3. EC Alfred Nzo district: 450 doses labelled BVI in the xlsx, ARC in the pptx. Unresolved.
4. WC AWC/RPO methodology (449,370 received) versus WC-GIS portal (330,340 historically, 547,100 latest). Both held in master; GIS portal figure used in the dashboard.
5. WC dairy cows Week 28 vs Week 29 -- MPO methodology change (Week 28 included non-dairy species).
6. KZN suspected case in vaccinated herd (MPO) -- booster programme expected; monitor for confirmation.
7. FS 8 May DolVet 466,100 originally recorded as Bioaftogen. Flagged in notes, not corrected.
8. GP OBP distributed 1,700 versus administered 127,580 in a prior template upload -- likely a column-mapping issue, still unresolved.
9. **NW doses_received**: 1,271,140 (FMD-summary slide) versus 1,350,140 (internal allocation table incl. RPO) -- unresolved since 16 Jul, still present in the 11 Aug report (session 73).
10. **NW animals_vaccinated**: FMD Portal (1,172,333, 11 Aug) versus internal spreadsheet (1,220,669, 25 Jul) -- new gap flagged session 73, Portal figure is lower which should not happen for a cumulative count.
11. NW per-municipality case detail not machine-readable from the 11 Aug PDF; needs manual entry if district-level granularity is wanted (session 73).

## Automation health

Local Claude CLI still failing with 401 OAuth as of the last check (25-26 August); no successful local Claude-assisted runs since. The Windows scheduled task (`ingest.py`, no Claude involved) continues to run daily but only reprocesses the same static Mpumalanga file with a relabelled "effective date" -- it is not a functioning ingest and should not be trusted for data freshness. A separate "Update FMD dashboard 2026-08-28" / "Disable Jekyll processing" commit pair appeared on the GitHub remote this morning (09:00 SAST) from outside this session -- did not touch master_data.csv, no conflict with session 73's push. Cowork sessions remain the only reliable ingest path; re-authentication of the local CLI is still outstanding.

## Parked/outstanding

- ICC Update PDF covering the 11 August Ministerial Task Team meeting, plus the rollout plan for the Minister. More than three weeks overdue.
- KZN doses received and official case count (received stale since 9 Jun; cases since 5 Jun).
- Gauteng exact doses received (approximately 800,000 per 24 Jul minutes; last precise figure 643,300).
- EC unique-animals versus dose-count basis; EC internal 5,022 gap between used and vaccinated totals (5 Aug).
- Sarah Baartman kudu suspects (20 Aug) -- watch for confirmation.
- WC dairy cases near Rooiheuwel and Oudtshoorn (MPO) -- watch for WC-GIS/WC-DoA confirmation.
- Mpumalanga reconciliation queries (in-hand and loss totals; Bioaftogen 3 quantity).
- Biogenesis Bago 1.5 million provincial split; Section 10 follow-ups; ICC Terms of Reference.
- North West allocation confirmation (1,271,140 versus 1,350,140) -- persists in the 11 Aug report, still unreconciled.
- North West district-level 11 Aug case breakdown -- PDF extraction failed, needs manual re-check.
- North West Portal-vs-spreadsheet animals-vaccinated gap (1,172,333 vs 1,220,669) -- new, watch for a cleaner source.
- Consolidated AgriSA weekly xlsx, now more than 139 days outstanding.
- Limpopo incoming batches, the 2 million doses referenced in the 24 July minutes, and the two Section 11 district lines.
- Western Cape case-count basis (three counts held) and AWC/RPO methodology gap.
- NC booster campaign due to start August 2026; no booster figures seen yet.
- Re-authenticate the local Claude CLI and check the Windows scheduled task trigger.
- Republish the Claude Artifact alongside every future GitHub Pages push (see "Publishing" above).
- GitHub: session 73 pushed this session ("Session 73 -- NW RPO JIC 11 Aug ingest; 3,278 rows"); master 3,278 rows, dashboard and index.html byte-identical to local at push time. Commit hash to be confirmed by the next session's verification pass.
