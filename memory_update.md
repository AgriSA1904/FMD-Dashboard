As at 2026-09-24 (session 78c -- Cowork, user-triggered RMIS ingest -- master now **3,850 rows**, 143 rows added; **dashboard rebuilt, snapshot unchanged at 18 September 2026, 84 weekly points, validation passed**):

**Session 78c (24 Sep, RMIS export 22 Sep and RMIS stats update):**

- RMIS industry channel 3,591,419 doses to 22 Sep (up 777,413 since 3 Sep); feedlot 2,490,576. GP Sedibeng feedlot jump of 500,020 needs confirming.
- GLN registrations 14,209; tags 192,199 (national only, provincial table missing from the message); 20 AHTs have vaccinated 165,104 cattle. Stats recorded at 24 Sep, as-at date not stated.
- Fixed three stale RMIS display paths (municipality list pooling all exports, June province totals, June vet/site cards) and added a traceability row to the RMIS tab.

As at 2026-09-22 (session 77b -- Cowork, fifth run of the day -- master now **3,707 rows**, 2 rows added; **dashboard rebuilt, snapshot unchanged at 18 September 2026, 84 weekly points, validation passed, 1,979,725 bytes**):

**Session 77b (22 Sep, Ministerial private-sector vaccine manufacturing statement):**

- Ingested `inbox/Ministerial Updates/Media Statement Minister Aucamp announces private sector to assist in ARC vaccine production.pdf` (Ministry, 22 Sep): 2 policy rows, no quantitative figures.
- The ARC Board unanimously agreed on 21 Sep 2026 to let qualifying private companies (local and/or international) use the ARC's IP and manufacture the ARC's FMD vaccine at scale under conditional licensing agreements, addressing the ARC's manufacturing-scale constraint. Licensing income is ringfenced for the ARC's own capacity expansion.
- On the Minister's request, the ARC will also submit FMD field-circulating virus isolates to the Pirbright Institute (UK) in October for a second round of vaccine-matching assessments.
- **New minister named:** this statement names Willie Aucamp as Minister of Agriculture. Every earlier Ministry-sourced row in this master names John Steenhuisen. Flagged in the row notes and in Parked/outstanding below; held as an open flag rather than corrected retroactively pending a second source.
- These policy rows are not wired into the dashboard's hardcoded `policy_events` banner list, same convention as the 18 Sep ICC update (session 76b note). Worth revisiting whether this should surface as a banner.
- Dashboard rebuilt via importlib (no headline or snapshot-date change; policy-only ingest). See Publishing section below for the GitHub push outcome.

As at 2026-09-22 (session 77 -- Cowork, fourth run of the day -- inbox check only, no new submissions, master unchanged at 3,705 rows, dashboard and GitHub already in sync from session 76c):

**Session 77 (22 Sep, empty inbox check):** scanned every inbox subfolder; nothing newer than session 76c's ingest. The files with today's timestamps (MPO Week 48, the ICC update, the Portfolio Committee presentation, the Vaccine_Process documents) were already processed in sessions 76b/76c. No rows added, no rebuild, no push. Confirmed `origin/main` still at `bf8c610`. See change_log.md, session 77, for detail.

As at 2026-09-22 (session 76c -- Cowork, third run of the day -- master now **3,705 rows**; **dashboard rebuilt, snapshot 18 September 2026, 84 weekly points, validation passed, 1,979,595 bytes**):

**Session 76c (22 Sep, MPO Week 48 / 18 Sep):**

- MPO Week 48 ingested, 28 rows. Week 47 was never received, so this follows Week 46 (4 Sep) directly.
- Dairy cows vaccinated first round 960,295 nationally (up 153, all Western Cape). Boosters 638,336 (up 71,902: EC +59,699 to 210,792, WC +12,203 to 60,706). Limpopo, Mpumalanga, North West and Northern Cape still report no boosters.
- Dairy farms: 175 cumulative, 128 active. Per-province active from the MPO map: KZN 62, EC 20, GP 17, FS 10, WC 9, NW 6, MP 3, LP 1, NC 0 (sums exactly to 128). EC's 20 includes eight KZN-border farms under EC surveillance; EC's own positive count is twelve.
- KZN reports all dairy animals boosted, beef animals on dairy farms still outstanding, and a further 42,000 doses delivered to five veterinary practices.
- **Fixed a four-month-old bug:** the dairy farm headline cards and trend chart were reading the May-era metric names (`dairy_farms_confirmed_fmd`, `dairy_farms_active_fmd`) while data had been landing under `dairy_farms_fmd_total` and `dairy_farms_active_fmd_prov` since June. The cards had been frozen on 171 confirmed / 124 active since May, and the trend chart had only four points. Now treated as aliases in build_dashboard.py, with carry-forward of the last cumulative confirmed figure. Cards read 175 / 128 as at 18 Sep; trend chart now has 17 points.
- **Standing lesson:** two stale-figure bugs found in one day (this and the August consignment row). Both were display paths quietly serving an old value rather than surfacing that the newer one was not being picked up. Remaining dashboard lookups should be audited for the same alias pattern.

As at 2026-09-22 (session 76b -- Cowork, same-day follow-up -- master now 3,677 rows, 7 rows added; new "Vaccine order process" dashboard tab added):

**Session 76b (22 Sep, new dashboard tab + ICC Update 18 Sep):**

- Built a new "Vaccine order process" tab on the dashboard from three user-supplied documents (`Vaccine Process.docx`, the RMIS ordering-process PDF, the Buffalo Analytics user manual) plus web research confirming current live links: Government route (`fmd.nda.gov.za`), Industry route (`rmis.co.za/services/traceability/`), Private route (`buffalo.vet/fmd`). Includes a six-step order-and-delivery infographic and two downloadable guides embedded as base64 PDFs (RMIS guide, Buffalo Analytics manual) so the dashboard stays a single self-contained file.
- Ingested `inbox/ICC Reports/09-18-2026_FMD ICC Update.pdf` (FMD-ICC, 18 Sep): 7 policy rows, no quantitative figures -- outstanding Section 10 Committee appointment, outstanding compulsory-vaccination/state-funding decision, outstanding verified-doses-imported statement request, outstanding vaccine-allocation-criteria request (MTT/vet working group meeting was scheduled 21 Sep to settle this), an overdue data-consolidation meeting the Minister instructed the Department to arrange at the 2 Sep Joint Working Group, the tabled Vaccination Rollout Plan, and a note that the ICC update itself cites our dashboard (https://agrisa1904.github.io/FMD-Dashboard/) as its live reference.
- These policy rows are held in master_data.csv for the audit trail but are not wired into the dashboard's hardcoded `policy_events` banner list (which only covers the Section 10 scheme and KZN DMA lift). Consider extending that list if ICC governance updates should surface as a banner going forward.
- **Readability pass on the new tab:** first build used 13px copy, which is too small for the farmer audience. Rebuilt with large numbered step circles joined by drawn arrows, 17px step copy, a "choose this if" strip on each route card, and full-width call-to-action buttons. Same treatment applied to the six-step journey strip. House rule for anything farmer-facing on this dashboard: 16px minimum body copy, visible step numbering, arrows between steps.
- **Incoming supply table corrected:** the 4,000,000-dose "Further consignment" row announced for early August was still showing as "Expected" in late September, and the footer was summing every row into a misleading single total of 31,000,000. The eight arrived rows already sum to exactly 17,000,000, matching the 5 Aug Portfolio Committee figure, so the 4 million is most likely already inside that total. Re-statused to "Unconfirmed", excluded from the arrived total, and the footer now shows three separate lines (arrived 17,000,000, announced but unconfirmed 4,000,000, pipeline 10,000,000). The "Expected" badge also moved off lime, which was off-brand on a light background.

**Session 76 (22 Sep, FS 18 Sep pack, MP 19th JOC / 14 Sep, NW RPO / 14 Sep, Portfolio Committee mass-vaccination presentation / 14 Sep):**

- Free State: positive cases 796 (xlsx template) versus 798 (media release text, 2 new cases) -- conflicting, both held; the xlsx per-SVA breakdown is unchanged from 11 Sep. Animals vaccinated 1,671,316. New metric: 115 farmer notifications of intent to self-vaccinate via the National FMD Reporting System.
- Mpumalanga: 262 cumulative outbreaks (137 open, 125 closed). 823,655 primary vaccinated plus 64,772 boosters = 888,427 total administered, up sharply from 729,074 (27 Jul). Controlled slaughter 37,849.
- North West: doses received jumped to 1,665,100 (from 1,271,140, 11 Aug); doses administered 1,482,307 (91.3 percent usage). Animals vaccinated (FMD Portal) 1,347,844 -- now exceeds the internal-spreadsheet figure, resolving the Portal-vs-spreadsheet gap flagged in sessions 73-75.
- National (Ministry Portfolio Committee table, data as at 14 Sep): 16,000,000 doses procured (down from 17,000,000 stated 5 Aug, both held), 11.8m received / 9.67m administered across the 9 provinces, 15.4m estimated cattle population, 63 percent coverage. 25 vets and 186 AHTs employed; only the WC lab operational. Independent province-level doses_received/administered/herd_cattle rows added for all 9 provinces.
- Resolved a long-parked item: Government Gazette No. 54969 / Notice No. 7668 (Section 9(1) national control measures), published 8 July 2026 -- learned via the FS media release, backdated to its actual date.
- **Fixed a dashboard bug found this session:** an MP-DVS industry-received row (59,500 doses, private channel) had been filed under the generic `doses_received` metric and was being picked up ahead of MP's true 1,116,940 state-channel total because both shared an effective date. Renamed to `doses_received_industry`; dashboard rebuilt clean. Worth checking for the same pattern with any future small industry/private receipt sharing a date with a provincial total.
- Dashboard rebuilt via importlib: snapshot 11 Sep -> 18 Sep 2026, 84 weekly points, 314,063 bytes. National: positive 2,841, suspected 890, distributed 11,815,120, administered 9,286,829, balance 2,528,291.
- GitHub push and Artifact republish: see Publishing section below for the outcome recorded this session.

## Publishing

- **GitHub Pages** (primary public site): https://AgriSA1904.github.io/FMD-Dashboard/. Push per the pattern in CLAUDE.md (clone `AgriSA1904/FMD-Dashboard`, copy `FMD_Dashboard.html` as both itself and `index.html` plus `master_data.csv`, `change_log.md`, `memory_update.md`, `scripts/build_dashboard.py`, commit, push to `main`).
- **Claude Artifact** (added session 73): https://claude.ai/code/artifact/c6f5c0bc-212c-4ac9-8946-8fe3f2c5a9f4. Republish by taking the freshly rebuilt `FMD_Dashboard.html`, stripping the outer `<!DOCTYPE>`/`<html>`/`<head>`/`<body>` wrapper, and republishing to the same URL. As with session 75, the hosted Artifact tool was not available in this session type; still needs an interactive Cowork session to republish.

## National programme headline (dashboard, 18 September)

Positive cases 2,841; suspected 890; doses distributed 11,815,120; administered 9,286,829; balance 2,528,291; procured 16,000,000 (Ministry). Last ICC-basis figure remains 4 August (positive 2,725); the ICC update covering the 11 August Ministerial Task Team meeting is now more than six weeks overdue. The 22 September Portfolio Committee presentation is the most current Ministerial-level source and now partly substitutes for the missing ICC update.

## Per-province latest figures (programme sources only)

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 2,174,510 | 1,615,211 (dose-count basis) | 506 outbreaks, 228 suspected | 10 Sep |
| FS | 1,961,840 | 1,671,316 | 796 / 798 (conflicting, see flag) | 18 Sep |
| GP | 757,320 (Ministry) / 643,300 (JOC) | 563,694 (Ministry) / 527,626 (JOC) | 307 | 14 Sep / 29 Jul |
| KZN | 2,414,120 (Ministry) / stale JOC figures | 1,758,367 (Ministry) / 1,700,000 (MEC, rounded) | 336 (stale, 5 Jun) | 14 Sep |
| LP | 1,225,650 | 971,866 (Ministry) / 956,974 (JOC) | 101 (73 suspected; 136 incl closed) | 14 Sep / 11 Sep |
| MP | 1,116,940 | 888,427 | 262 (137 open, 125 closed) | 14 Sep |
| NW | 1,665,100 | 1,482,307 (doses) / 1,347,844 (animals, Portal) | 482 (115 suspected, likely stale) | 14 Sep |
| NC | 383,560 (Ministry) / 333,560 (JOC) | 253,462 (Ministry) / 215,546 (JOC) | 40 outbreaks (dashboard positive_cases 22) | 14 Sep / 5 Aug |
| WC | 647,080 (Ministry) / 547,100 (JOC) | 522,004 (Ministry) / 428,657 (JOC) | 35 outbreaks (GIS 29 retained) | 14 Sep / 31 Jul |

Note: the 14 Sep Ministry figures (Portfolio Committee table) are now held alongside the provincial JOC figures for every province; the dashboard's per-metric tie-break picks whichever row sorts last for a given date, so the two sources should be read together rather than assuming the dashboard always shows the JOC figure.

## Known data quality issues, carry forward awareness

1. NC 25 March: vaccinated 23,000 exceeds received 18,846 because of a pre-period stock draw. Expected behaviour.
2. EC `animals_vaccinated all/all` figures are dose-count totals and double-count animals receiving more than one dose.
3. EC Alfred Nzo district: 450 doses labelled BVI in the xlsx, ARC in the pptx. Unresolved.
4. WC AWC/RPO methodology (449,370 received) versus WC-GIS portal (547,100) versus Ministry (647,080, 14 Sep). Three figures now held.
5. WC dairy cows Week 28 vs Week 29 -- MPO methodology change.
6. KZN suspected case in vaccinated herd (MPO) -- booster programme expected; monitor.
7. FS 8 May DolVet 466,100 originally recorded as Bioaftogen. Flagged in notes, not corrected.
8. GP OBP distributed 1,700 versus administered 127,580 in a prior template upload -- likely column mapping, unresolved.
9. NW doses_received: three figures now held -- 1,271,140 (11 Aug summary slide), 1,350,140 (11 Aug allocation table), 1,665,100 (14 Sep usage table). The 14 Sep figure is the most current and highest.
10. NW animals_vaccinated (Portal): now exceeds the internal spreadsheet (1,347,844 vs 1,220,669) -- see session 76 note; treated as resolved in the Portal's favour rather than a new gap.
11. NW per-municipality case detail still not machine-readable from the RPO PDF (sessions 73, 75, 76 all hit this).
12. EC internal inconsistencies (session 75): 10 Sep summary slide shows 501 outbreaks versus 506 in the outbreak-control table.
13. LP received basis (session 75): 11 Sep row uses register total received (1,225,660); the Ministry Portfolio Committee table (14 Sep) shows 1,225,650, essentially confirming this basis.
14. LP positive_cases falls as cases close (110 -> 101) because closed cases are held separately; use confirmed-incl-closed (136) when comparing with other provinces' cumulative counts.
15. FS template gaps: provincial received cell blank on 28 Aug and 11 Sep; suspected n/a on those dates.
16. **FS positive_cases conflict (session 76):** 18 Sep media release text states 798 (2 new cases); the accompanying xlsx template's provincial total and full district breakdown are unchanged from 11 Sep (796). Both held; watch the next FS pack to see which is confirmed.
17. **MP industry-received metric renamed (session 76):** a small Nkangala industry-received figure (59,500) had been sharing the `doses_received` metric name with MP's true state total and was being picked up incorrectly by the dashboard; renamed to `doses_received_industry`. Check for the same pattern if a future province's industry/private receipt shares an effective date with its provincial total.
18. **National doses_procured conflict (session 76):** 16,000,000 (22 Sep Portfolio Committee, itemised) versus 17,000,000 (5 Aug Ministerial statement). Both held.

## Automation health

Cowork sessions (scheduled and user-triggered) are the only reliable ingest path. The local Claude CLI was still failing with 401 OAuth at last check (late August). The Windows scheduled task (`ingest.py`) runs daily but only reprocesses the same static Mpumalanga file and pushes empty "Update FMD dashboard" commits to GitHub; it does not advance data.

## Parked/outstanding

- Confirm with the Department whether the 4 million doses announced for early August actually arrived, and whether they sit inside the 16 to 17 million already reported as procured. Held as "Unconfirmed" on the dashboard until answered.
- Outcome of the 21 September MTT/veterinary working group meeting on vaccine allocation criteria -- watch the next ICC update.
- Whether the Section 10 Committee has finally been appointed (nominations submitted May 2026, still outstanding as at 18 Sep).
- ICC Update PDF covering the 11 August Ministerial Task Team meeting -- now more than six weeks overdue; the 22 Sep Portfolio Committee presentation partially substitutes at national level.
- MPO Week 47 was skipped entirely (Week 46 on 4 Sep, then Week 48 on 18 Sep). Chase it or confirm none was issued.
- Ask the MPO whether the per-province active dairy case map is still being refreshed; it has been identical to the 19 June breakdown for every province except EC (18 to 20) and WC (7 to 9).
- Audit the remaining dashboard lookups for stale metric-name aliases, after two frozen-figure bugs were found on 22 September.
- FS 798-versus-796 case count needs confirmation from the next FS pack.
- EC, LP, WC, GP, NC, KZN, RMIS files for the week of 18-22 September not yet in the inbox.
- Confirm whether Ministry (Portfolio Committee) province-level figures should be preferred over provincial JOC figures going forward, or continue to be held side by side.
- NW per-municipality case detail still needs manual entry if granular district data is wanted.
- LP: Mopani lab backlog (66 outstanding), Capricorn/Vhembe transfer reconciliation, booster campaign launch figures.
- Mpumalanga reconciliation queries; Biogenesis Bago 1.5 million provincial split; Section 10 follow-ups; ICC Terms of Reference.
- Consolidated AgriSA weekly xlsx, now more than 150 days outstanding.
- NC booster campaign due to start August 2026; no booster figures seen yet (though general observations slide of the 22 Sep PC deck says NC has already started boosters -- watch for provincial confirmation).
- Re-authenticate the local Claude CLI; disable or fix the Windows scheduled task's empty commits.
- Republish the Claude Artifact alongside every GitHub Pages push -- needs an interactive Cowork session with the Artifact tool.
- Confirm the ministerial transition: the 22 Sep private-sector manufacturing statement names Willie Aucamp as Minister of Agriculture; every earlier Ministry-sourced row in this master names John Steenhuisen. Establish when the change took effect.
- Watch for the named private-sector partner(s) in ARC FMD vaccine manufacturing (ARC Board agreed 21 Sep) and for the outcome of the ARC's October submission of FMD isolates to the Pirbright Institute for a second vaccine-matching round.
