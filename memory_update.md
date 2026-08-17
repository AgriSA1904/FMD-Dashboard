As at 2026-08-14 (session 67 -- daily inbox ingest; Portfolio Committee packs, Free State stats and MPO Week 42):

- Master: **2,948 rows** (was 2,879; 69 added). Dashboard snapshot: **6 August 2026** (was 31 July); weekly points 71 (was 66). Rebuild via importlib, validation passed (264,826 bytes).
- Eight new files processed: the 4 to 5 August Portfolio Committee on Agriculture packs for EC, KZN, NC and WC plus the committee media statement (arrived 12 Aug), the Free State FMD STATS 6 AUGUST 2026 zip (xlsx, two media release images; arrived 11 Aug), and the MPO Week 42 dairy update (arrived 11 Aug).
- **KZN is official again at last.** The KZN-DARD Portfolio Committee report gives 1,567,971 animals vaccinated as of 26 July (55.0 percent coverage of 2.4 million; state 950,242, private 617,729; 247,000 dairy boosters), replacing the stale unofficial 648,609 of 9 June. KZN-DARD added to PROGRAMME_SOURCES.
- **Free State vaccination unstuck.** FS DARDLEA media release of 7 August: 1,458,124 cattle vaccinated (Biogenesis Bago and Dollvet), first official FS figure since 10 July. FS positive cases now 764 (543 resolved, 221 active). Note: vaccinated now exceeds the last known FS received figure of 1,272,180 (10 Jul); FS receipts need updating.
- WC-DoA added as a source org and to PROGRAMME_SOURCES (Western Cape Department of Agriculture Portfolio Committee deck; the WC-GIS portal remains the live channel).

**National programme headline (unchanged ICC basis, 4 August):** positive cases 2,725; doses distributed 8,529,687; administered 6,249,525; balance 2,280,162. Bottom-up sums across latest provincial programme figures now give roughly 8,606,235 received and 8,190,379 vaccinated; the vaccinated sum now exceeds the ICC administered figure and reconciliation with the next ICC update is the key check. The Portfolio Committee statement (5 Aug) confirms 17 million doses procured nationally with four million more expected.

**Per-province latest figures (programme sources only):**

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 1,527,230 | 1,284,333 (dose-count basis) | 483 outbreaks (basis change) | 5 Aug |
| FS | 1,272,180 (stale, 10 Jul) | 1,458,124 | 764 | 6 Aug |
| GP | 643,300 (approx 800,000 per 24 Jul minutes, unconfirmed) | 527,626 | 307 | 29 Jul |
| KZN | 1,329,112 (stale, 9 Jun) | 1,567,971 (OFFICIAL) | 336 (stale, 5 Jun) | 26 Jul |
| LP | 994,725 | 758,379 | 109 | 31 Jul |
| MP | 897,000 | 729,074 | 259 | 27 to 31 Jul |
| NW | 1,271,140 | 1,220,669 | 476 | 25 Jul |
| NC | 333,560 | 215,546 | 40 outbreaks (basis change) | 5 Aug |
| WC | 547,100 | 428,657 | 35 outbreaks (GIS 29 retained) | 30 to 31 Jul |

**New data quality flags (session 67):**

- EC internal conflict: doses used 1,279,311 (usage slide) versus 1,284,333 (sector slide); both held. EC dose-count caveat still applies to animals vaccinated.
- EC, NC and WC case figures now reported on an outbreaks basis, not individual positive cases; not directly comparable with prior positive_cases values. Flagged in notes.
- KZN district table has internal inconsistencies (Hluhluwe 130,807 duplicates the Jozini cattle column; uGu cattle exceeds its total); district rows nonetheless sum to 1,567,971.
- FS xlsx template again contained zero vaccination figures; the vaccination number came from the media release.

**Automation health (unchanged):** local Claude CLI still needs re-authentication (401 OAuth); Windows scheduled task trigger not firing at 08:00; xlsx pre-processing stall persists. This Cowork session remains the reliable ingest path.

**Parked/outstanding:**

- ICC Update PDF covering the 11 August meeting with the Ministerial Task Team veterinarians, plus the rollout plan for the Minister. Still not arrived (checked 17 Aug).
- FS doses received figure (stale since 10 Jul and now below animals vaccinated).
- KZN doses received and official case count (received stale since 9 Jun; cases since 5 Jun).
- Gauteng exact doses received (approximately 800,000 per 24 Jul minutes; last precise 643,300).
- EC unique-animals versus dose-count basis; EC internal 5,022 gap between used and vaccinated totals.
- Mpumalanga reconciliation queries (in-hand and loss totals; Bioaftogen 3 quantity).
- Biogenesis Bago 1.5 million provincial split; Section 9 and Section 10 follow-ups; ICC Terms of Reference.
- North West allocation confirmation (1,271,140 versus 1,350,140) and spreadsheet versus FMD Portal gap.
- Consolidated AgriSA weekly xlsx, now more than 130 days outstanding.
- Limpopo incoming batches, the 2 million doses referenced in the 24 July minutes, and the two Section 11 district lines.
- Western Cape case-count basis (now three counts: deck 35 outbreaks, GIS 29, weekly summary 39) and AWC/RPO methodology gap.
- NC booster campaign due to start August 2026; watch for the first booster figures.
- GitHub push: attempted this run from the sandbox; see change_log session 67 for the result.


---

## Session 68 addendum (17 Aug 2026)

- RMIS portal release 11 Aug ingested (live browser read): allocated 2.9M, distributed 2,578,470, 121 practices, 1,622 sites, full province/manufacturer/municipality detail, new Industry Allocation Log table (metric industry_allocation_batch).
- WC GIS live REST query 17 Aug: confirmed 36 / suspected 19; vaccinated 469,770 (2,497 records); received 597,080 (13 Aug). National headline received now 8,656,215, administered 8,231,492, positive 2,768.
- Minister era captured: Aucamp replaced Steenhuisen (official 1 Jul); 10 Jul settlement opened private vaccine imports/sales; 25 Jul self-vaccination portal; over 8M vaccinated as at 17 Jul (ministerial); 80% herd target by Dec 2026; 4M Dunevax landed week of 3 Aug. Ministerial dashboard section updated accordingly.
- Builder fix: RMIS sector/municipality panels now dedupe to latest release date and include dairy.
- Watch next: ICC 11 Aug update PDF; first booster figures (NC); whether procurement moves past 17M once the 4M landing is formally confirmed by DoA.
