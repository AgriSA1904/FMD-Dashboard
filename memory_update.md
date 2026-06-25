As at 2026-06-25 (session 45 -- null ingest; inbox clear):
- Master: **1,913 rows** (unchanged)
- Dashboard snapshot: **23 June 2026** (39 weekly points; 182,734 bytes; validation passed)
- Dashboard rebuilt: No -- no new data

**New data ingested (session 45):**
- None. Full inbox scan performed; no new files since session 44g (24 June 2026).
- 24 June FMD Weekly Engagement outcomes PDF still not in inbox (only agenda present).
- MPO Week 36 still not in inbox.

**National headlines (dashboard 23 June 2026):**
- Distributed (doses received): 6,635,041 (unchanged)
- Animals vaccinated: 4,742,044 (unchanged)
- Positive cases: 2,418 (unchanged)

**Per-province latest vaccine figures:**

| Province | Received | Animals vaccinated | Date |
|---|---|---|---|
| EC | 1,000,660 | 926,233 | 11 Jun |
| FS | 838,400 | 1,053,502 | 22 Jun |
| GP | 643,300 | 333,221 | 10 Jun |
| KZN | 1,329,112 | 648,609 | 21 May |
| LP | 775,660 | 495,102 | 21 Jun |
| MP | 732,489 | 344,629 | 8 Jun |
| NW | 895,120 | 527,337 | 1 Jun |
| NC | 200,600 | 114,443 | 10 Jun |
| WC | 497,100 | 299,969 | 15 Jun |

**Parked/outstanding (carry forward):**
- 24 June FMD Weekly Engagement outcomes -- meeting was 24 June; outcomes PDF not yet in inbox.
- LP PCM 6 July 2026 -- next meeting confirmed.
- Section 9 gazette: approximately 72 days overdue. Urgent.
- Consolidated AgriSA weekly xlsx: approximately 75 days outstanding. Urgent.
- 2 million DolVet doses expected approximately 15 June -- not confirmed in RMIS (10 days overdue).
- 7 million Biogenesis doses expected end July 2026 -- forward pipeline.
- KZN booster programme -- 240,000 done; resumption expected.
- MPO Week 36 -- not yet in inbox.
- LP DolVet 150,000 receipt -- outstanding.
- KZN animals vaccinated gap (DoA 1.16 million versus master 648,609).
- MPO Week 35 GP/MP dairy active case swap -- confirm with MPO.

---

As at 2026-06-24 (session 44g -- RMIS industry distribution tab update):
- Master: **1,913 rows** (+90 from session 44f: RMIS industry Excel province x manufacturer and municipality x sector rows)
- Dashboard snapshot: **23 June 2026** (39 weekly points; 182,734 bytes; validation passed)
- Dashboard rebuilt: Yes -- RMIS tab redesigned; build_dashboard.py and dashboard_template.html updated

**New data ingested (session 44g):**
- rmis_industry_allocated_fmd_vaccine_distribution_data_2026-06-24.xlsx: 90 rows.
  - Sheet 2 (provincial_distribution): 18 rows: province x manufacturer (Biogenesis/DolVet) breakdowns + 2 national manufacturer totals.
  - Sheet 3 (sector_distribution): 70 rows: province x municipality x sector (feedlot/commercial/stud) breakdown.
- Total industry doses distributed confirmed: 986,012 (39.4% of 2,500,000 allocated to industry).
- Sector split: feedlot 674,060 (68.4%) / commercial 263,373 (26.7%) / stud 48,579 (4.9%).
- Top districts: GP Sedibeng feedlot 151,990; FS Thabo Mofutsanyane feedlot 113,020; MP Nkangala feedlot 60,230.

**RMIS tab changes (dashboard):**
- Kicker updated to "Industry distribution view" (was "Feedlot sector view").
- Title updated to "RMIS: Industry vaccine distribution." (was "RMIS: Feedlot vaccine orders.").
- KPI cards: doses distributed 986,012; utilisation 39.4% of 2.5M; vet practices 64; GLN sites 650.
- New province x manufacturer stacked bar (Biogenesis vs DolVet per province).
- New sector donut: feedlot / commercial / stud with legend.
- New top-15 districts table with sector colour-coding and mini bar.
- Manufacturer split panel (Biogenesis vs DolVet with progress bars).
- Feedlot orders cumulative timeline retained.

**GitHub commit:** 514624b (session 44g)

---

As at 2026-06-24 (session 44f -- verification pass; null ingest):
- Master: **1,807 rows** (unchanged from session 44e)
- Dashboard snapshot: **23 June 2026** (39 weekly points; 168,451 bytes; validation passed)
- Dashboard rebuilt: No -- no new data

**New data ingested (session 44f):**
- None. Inbox fully clear as at 24 June 2026 (second daily pass).
- NW June 1 RPO confirmed already in master (all rows at 2026-06-01).
- RMIS June 18 file skipped (superseded by June 22 already in master).

**National headlines (dashboard 23 June 2026):**
- Distributed (doses received): 6,635,041 (unchanged)
- Animals vaccinated: 4,742,044 (unchanged)
- Positive cases: 2,418 (unchanged)

**Per-province latest vaccine figures:**

| Province | Received | Animals vaccinated | Date |
|---|---|---|---|
| EC | 1,000,660 | 926,233 | 11 Jun |
| FS | 838,400 | 1,053,502 | 22 Jun |
| GP | 643,300 | 333,221 | 10 Jun |
| KZN | 1,329,112 |