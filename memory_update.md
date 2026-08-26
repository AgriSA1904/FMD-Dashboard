As at 2026-08-26 (session 71 -- early manual ingest requested by Jay; FS 21 Aug pack, MPO Weeks 43 and 44, RMIS 25 Aug. Session 72, the afternoon scheduled run of the same day, found no new submissions and verified the session 71 GitHub push. Session 71b, same day: web sweep for the WC GIS portal and post-June ministerial updates -- master now **3,264 rows**, three rows added):

**Session 71b additions (26 Aug, web sweep):**

- **Ministerial channel updated past early June.** Minister Willie Aucamp (FMD Symposium, Pretoria, 31 July, via African Farming and the departmental statement): by 17 July more than 9 million doses distributed and just over 8 million animals vaccinated (commercial 4,917,609; communal and emerging 3,107,234); 17 million doses imported to date; four million further doses due early August; target 80 percent of the national herd by December 2026. The national vaccinated row (8,024,843, 17 Jul) and a ROUNDED doses distributed row (9,000,000) are now in master under Ministry.
- **KZN unstuck.** KZN MEC kaMadlopha-Mthethwa (Mtubatuba engagement, via African Farming 21 Aug): 1.7 million cattle vaccinated (ROUNDED), more than two-thirds of the estimated 2.5 million herd, nine districts; uMzinyathi resumed 21 Aug targeting about 285,000 cattle. Replaces 1,567,971 of 26 Jul as the latest KZN vaccinated figure.
- **WC GIS portal could not be scraped this session.** The Experience Builder app is client-rendered; the Claude in Chrome extension was not connected and the sandbox cannot query the ArcGIS REST services directly. No fresh WC-GIS figures ingested; WC latest remains 30 to 31 Jul. An Elsenburg article of 22 June (328,876 vaccinated) is older than what we hold and was not ingested.
- Other checks: departmental newsroom has no FMD figures newer than the 5 Aug Portfolio Committee statement (Aug releases cover citrus and a Carte Blanche clarification on Act 36 matters); Minister Aucamp appointed Dr Theo de Jager and Dr Danie Odendaal to the ICC on 31 July and will expand the ICC Terms of Reference, with vaccine suppliers attending ad hoc.

- Master: **3,261 rows** (was 3,095; 166 added). Dashboard snapshot advanced to **21 August 2026**; weekly points 75. Rebuild via importlib, validation passed (292,754 bytes).
- New sources this session: FMD STATS 21 AUGUST 2026.zip (FS-DARDLEA xlsx plus media release), MPO Week 43 (snapshot 14 Aug) and Week 44 (snapshot 21 Aug) dairy updates, and the RMIS industry export of 25 August. The AgriSA Provincial Chamber minutes of 29 July (filed 25 Aug on the corporate SharePoint) were reviewed: policy context only (Free State Agriculture court action history, Section 10 promulgation, lessons-learned discussion deferred), no figures ingested.
- **FS received finally unstuck: 1,741,840** per the 21 August template summary, replacing the stale 1,272,180 of 10 July. This restores received above animals vaccinated for FS.
- **FS cases 772** (2 new: Heilbron 1, Bloemfontein 1), 577 resolved, 195 active. The media release and xlsx agree at 772 this week and the State Vet Area breakdown sums exactly -- no off-by-one for the first time in weeks. The template also reports a first FS **suspected cases figure: 273**.
- **FS animals vaccinated 1,512,319** (21 Aug), up 26,979 on the week.
- **MPO dairy programme:** national first vaccinations flat at 958,511 since Week 42; boosters climbing 449,060 (7 Aug) to 473,677 (14 Aug) to 504,804 (21 Aug). EC boosters 100,837 and WC boosters 37,129 at 21 Aug. Dairy farms affected: 175 reported, 128 active. Three new dairy cases in Week 44: one EC (Smoordrif), two WC (Rooiheuwel, Oudtshoorn).
- **RMIS industry channel** as at 24 August: 2,761,420 doses distributed (Biogenesis 2,066,984, Dollvet 694,436), up 181,105 on the 16 August export. Biggest weekly movers: FS +49,732, KZN +54,034, NW +28,106.
- **Gazette detail confirmed:** the FS media release cites Government Gazette No. 54969, Notice No. 7668 of 8 July 2026 (Section 9(1) control measures) -- closes out the parked Section 9 gazette question.

**National programme headline (unchanged ICC basis, 4 August):** positive cases 2,725; doses distributed 8,529,687; administered 6,249,525; balance 2,280,162. The ICC update covering the 11 August Ministerial Task Team meeting remains outstanding (three weeks overdue).

**Per-province latest figures (programme sources only):**

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 1,786,510 (JOC; PC 1,527,230 held) | 1,378,088 (dose-count basis) | 498 outbreaks, 229 suspected | 20 Aug |
| FS | 1,741,840 | 1,512,319 | 772 (273 suspected) | 21 Aug |
| GP | 643,300 (approx 800,000 per 24 Jul minutes, unconfirmed) | 527,626 | 307 | 29 Jul |
| KZN | 1,329,112 (stale, 9 Jun) | 1,700,000 (MEC, rounded) | 336 (stale, 5 Jun) | 20 Aug |
| LP | 994,725 | 758,379 | 109 | 31 Jul |
| MP | 897,000 | 729,074 | 259 | 27 to 31 Jul |
| NW | 1,271,140 | 1,220,669 | 476 | 25 Jul |
| NC | 333,560 | 215,546 | 40 outbreaks (basis change) | 5 Aug |
| WC | 547,100 | 428,657 | 35 outbreaks (GIS 29 retained) | 30 to 31 Jul |

**New data quality flags (session 71):**

- FS suspected cases (273) is a first-time figure with no municipality breakdown; treat with care until repeated.
- FS received (1,741,840) is a summary-cell figure; municipality receipt cells are blank except Mangaung Bioaftogen 370,000, so it cannot be cross-checked bottom-up.
- MPO national first-vaccination total has been flat at 958,511 for three weeks while boosters climb; the second-round count may exceed round one for FS per MPO's own note.
- RMIS 25 Aug export includes orders shipped same-day (through 25 Aug); effective date recorded as 24 Aug by convention.

**Automation health:** local Claude CLI still failing with 401 OAuth; no successful local runs. The local task log shows failures through 25 August and no entry at all for 26 August (the Windows task may not have fired, or the log has not synced). Cowork sessions remain the only working ingest path. Re-authentication still outstanding.

**Parked/outstanding:**

- ICC Update PDF covering the 11 August Ministerial Task Team meeting, plus the rollout plan for the Minister. Three weeks overdue.
- KZN doses received and official case count (received stale since 9 Jun; cases since 5 Jun).
- Gauteng exact doses received (approximately 800,000 per 24 Jul minutes; last precise 643,300).
- EC unique-animals versus dose-count basis; EC internal 5,022 gap between used and vaccinated totals (5 Aug).
- Sarah Baartman kudu suspects (20 Aug) -- watch for confirmation.
- WC dairy cases near Rooiheuwel and Oudtshoorn (MPO Week 44) -- watch for WC-GIS/WC-DoA confirmation and any change to the WC outbreak count.
- Mpumalanga reconciliation queries (in-hand and loss totals; Bioaftogen 3 quantity).
- Biogenesis Bago 1.5 million provincial split; Section 10 follow-ups; ICC Terms of Reference. (Section 9 gazette now identified: Gazette 54969, Notice 7668, 8 July 2026.)
- North West allocation confirmation (1,271,140 versus 1,350,140) and spreadsheet versus FMD Portal gap.
- Consolidated AgriSA weekly xlsx, now more than 137 days outstanding.
- Limpopo incoming batches, the 2 million doses referenced in the 24 July minutes, and the two Section 11 district lines.
- Western Cape case-count basis (three counts held) and AWC/RPO methodology gap.
- NC booster campaign due to start August 2026; no booster figures seen yet.
- Re-authenticate the local Claude CLI and check the Windows scheduled task trigger.
- GitHub: session 71 push verified on the remote in session 72 (commit e5b9690, master 3,261 rows, dashboard and index.html identical to local). No further verification outstanding.
