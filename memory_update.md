As at 2026-07-13 (session 56 -- EC-DRDAR 9 Jul JOC; RMIS industry export 8 Jul; ICC/Ministerial statement + AgriSA Weekly Engagement outcomes reviewed):
- Master: **2,550 rows** (+136: 30 EC-DRDAR, 106 RMIS)
- Dashboard snapshot: **9 July 2026** (56 weekly points; 239,130 bytes; validation passed)
- Dashboard rebuilt: Yes -- Eastern Cape now current to 9 Jul 2026.
- This run closes a real gap: the unattended local automation has failed with a 401 authentication error on every attempt since 2026-07-06 (8 straight failures through 2026-07-13); this Cowork scheduled task is the only path that has actually ingested data since session 55 (8 Jul).

**New data ingested (session 56):**
- `EC FMD Update - 09.07.2026.pptx` (EC-DRDAR, effective 9 Jul 2026): 30 rows. Teams-recording capture, 10 full-slide images, read via vision.
  - Confirmed outbreaks 434 (up from 423, +11). Suspected 233 (down from 234, -1; source's own header arithmetic is internally inconsistent).
  - Animals vaccinated (dose-count, all channels incl static MPO 311,449) 1,037,900 (up from 1,026,694, +11,206). Biogenesis 436,282 (+8,462), DolVet 598,191 (+2,744), ARC-OVI/BVI unchanged.
  - Vaccine received stated total 1,063,530 -- **reconciles exactly** to the sum of the 11 batches logged individually back on 2 Jul, resolving a 700-dose gap against the 2 Jul session's recorded 1,064,230 (minor source-side tally error, not a real movement).
  - New 12th batch, Dolvet 5 (250,000 doses, received 7 Jul), is shown on the slide but explicitly **not yet included** in the 1,063,530 total -- independently confirmed via an EC FMD Ops WhatsApp message ("received 250 000 doses yesterday, not included in above"). Its own district distribution (228,000) falls 22,000 short of the 250,000 batch total -- unresolved.
  - EC's farming-sector per-district table and vaccine-type per-district table disagree materially for at least 2 of 6 districts (e.g. Amathole 242,992 vs 299,746) -- unresolved, flagged for EC-DRDAR.
  - EC's estimated cattle population fell from 4,595,393 (2 Jul) to 3,002,959 (9 Jul) with no explanation on the slide -- treated as a corrected denominator, not a real change; vaccine coverage rose 22.3% -> 34.5% accordingly.
- `rmis_industry_allocated_fmd_vaccine_distribution_data_2026-07-08.xlsx` (RMIS, as at 7 Jul 2026): 106 rows across all 9 provinces (province x manufacturer + municipality x sector). National industry-distributed total 2,105,105 doses -- cross-checks almost exactly against the AgriSA outcomes minutes' "more than 2.1 million of 2.5 million" claim. RMIS is a non-programme source; does not move dashboard headline.
- Ministerial media statement "New FMD control measures give farmers a clearer path to recovery..." (25 Jun 2026): narrative only, no data rows. This is the Section 9 replacement framework, approved by the Minister, pending Gazette publication.
- AgriSA Weekly FMD Engagement outcomes (8 Jul) + agenda (15 Jul): narrative only, no data rows added. Key points: possible **Minister of Agriculture change** referenced twice as "the new Minister" (unconfirmed elsewhere -- do not treat as fact); Section 9 gazette publication "expected during the current week" (6-10 Jul, not yet seen); 1.5m further Biogenesis doses shipped/expected shortly; Section 21 approval reportedly granted for a further 14m Biogenesis doses; positive kudu case (wildlife spillover) confirmed in EC; sheep infections reported elsewhere.

**National (programme sources only) as at this run:**
- Doses received 7,799,622 (-700 vs prior run, EC reconciliation); animals vaccinated 5,679,229 (+11,206); positive cases 2,584 (+11); suspected cases 962 (-1).

**Per-province latest figures (13 July 2026):**

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 1,063,53