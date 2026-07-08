As at 2026-07-08 (session 55 -- MP-DVS 7 Jul provincial JOC):
- Master: **2,414 rows** (+61: all MP-DVS, 17th FMD JOC 7 Jul 2026)
- Dashboard snapshot: **7 July 2026** (55 weekly points; 227,296 bytes; validation passed)
- Dashboard rebuilt: Yes -- Mpumalanga now current to 7 Jul 2026.
- Prior run same day (session 54) ingested NW-RPO 7 Jul (+35 rows).

**New data ingested (session 55):**
- `Mpumalanga Provincial JOC 07 July 2026.pdf` (MP-DVS, effective 7 Jul 2026): 61 rows. 20-page JOC minutes with an embedded slide deck; narrative read via pypdf, all data tables read via page-image vision (slides are images, no extractable text).
  - Outbreaks 259 confirmed (down 2 from 261 at 22 Jun, reclassification). By district: Gert Sibande 150, Nkangala 78, Ehlanzeni South 29, Ehlanzeni North 2. Suspects 127 (Gert Sibande 93, Nkangala 31, Ehlanzeni North 2, Ehlanzeni South 1).
  - New this period: 1 confirmed outbreak, Kromdraai (Nkangala). Thaba Chweu 6 of 7 blood samples NSP-positive (Feb samples, PCR negative).
  - Cattle vaccinated cumulative 654,409 (Commercial 343,115 / 1,363 owners; Communal 311,294 / 22,542 owners). Large but genuine rise from 344,537 at 19 May; corroborated by doses administered 653,374. Full 17-municipality breakdown captured for outbreaks and cattle vaccinated.
  - Vaccine: total allocation 747,000 (unchanged from 22 Jun); administered 653,374 (87pct); wastage 4,490 (0.6pct); in-hand 89,867 (of which Bioaftogen 3 63,752 still being deployed, plus 20,000 storage). Per-batch usage: ARC 1,805; Bioaftogen 1 97,554; Aftodoll 1 93,972; Bioaftogen 2 94,061; Aftodoll 2 138,148; Aftodoll 3 123,410; Bioaftogen 3 103,228.
  - Special categories: sheep 1,391; goats 493; pigs 2,958; dairy 25,249; stud 21,085; feedlot 12,838.
  - Controlled slaughter 33,222 at 3 designated abattoirs (Karan Beef, Volkrust Meat Co, Ramburg Beef); 2 new abattoir applications.
  - RPO note: 61,000 doses received, 27,700 orders still waiting; OBP delivery slow; private sector under-utilised.
  - No confirmed FMD in small stock. Next JOC 21 July 2026.

**National (programme sources only) as at this run:**
- Doses received 7,800,322; animals vaccinated 5,668,023; positive cases 2,573; suspected cases 963.

**Per-province latest figures (8 July 2026):**

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 1,064,230 | 1,026,694 | 423 | 2 Jul |
| FS | 1,272,180 | 1,106,191 | 648 | 26 Jun |
| GP | 643,300 | 405,404 | 306 | 24 Jun |
| KZN | 1,329,112 | 648,609 (UNOFFICIAL) | 336 | 9 Jun |
| LP | 775,660 | 520,185 | 95 | 26 Jun |
| MP | 747,000 | 654,409 | 259 | 7 Jul |
| NW | 1,271,140 | 892,119 (internal) | 445 | 3 Jul |
| NC | 200,600 | 114,443 | 22 | 26 Jun |
| WC | 497,100 | 299,969 | 39 | 29 Jun |

**Parked/outstanding (carry forward):**
- Two other files newer than master were NOT ingested this session (user asked for Mpumalanga only): `inbox/ICC Reports/MEDIA STATEMENT NEW FMD CONTROL MEASURES...pdf` and `inbox/RMIS/rmis_industry_allocated_fmd_vaccine_distribution_data_2026-07-08.xlsx`. Ingest next run.
- MP cattle-vaccinated jump (344k to 654k since mid-May) is genuine per doses administered, but worth a sanity note to the ICC given the size.
- MP outbreaks dropped 261 to 259 (reclassification) -- confirm.
- NW internal animals-vaccinated (892,119) unchanged from 30 Jun -- possibly stale.
- 8 July FMD Weekly Engagement outcomes (agenda received; outcomes pending).
- Section 9 gazette: approved by Minister (per NW and MP updates), awaiting gazetting.
- Consolidated AgriSA weekly xlsx: ~100+ days outstanding.
- KZN official JOC documents outstanding; figures UNOFFICIAL and stale (9 Jun); 1.5m more doses requested.
- LP DolVet 150,000 receipt still unconfirmed; LP Biogenesis 99,020 vs 100,020 discrepancy unresolved.
