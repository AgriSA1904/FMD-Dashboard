---
name: FMD daily run state
description: Latest master_data.csv row count, dashboard snapshot date, and run notes
type: project
---

As of 2026-05-21 (session 18 — uploaded weekly template ingested for 21 May):
- Master: 1,245 rows (1,126 after session 17 + 119 added from uploaded template)
- Dashboard snapshot: **21 May 2026** (advanced from 20 May)
- Dashboard rebuilt: Yes — FMD_Dashboard.html updated (83,145 bytes, 19 weekly points, validation passed)

**Key code change:**
- `scripts/build_dashboard.py` PROGRAMME_SOURCES now also includes **NW-RPO**. The user submitted complete NW provincial figures via the consolidated AgriSA weekly template; NW-RPO is the de-facto NW data channel since there is no NW-DARD JOC equivalent.

**Key highlights this run:**
- **User filled FMD_Master_Template_v2.xlsx with 21 May figures across all 9 provinces** and uploaded it back. Ingested as cumulative position effective 2026-05-21.
- **All provinces now using 21 May data.** Snapshot advanced 20 May → 21 May 2026.
- **National doses distributed: 5,361,509** (was 3,622,508 in session 17 — +1,738,001).
- **National animals vaccinated: 2,920,528** (was 2,938,800 in session 17; slight downward correction in LP and minor methodology shifts).
- **New per-vaccine distribution figures** captured for every province (BVI, OBP/ARC, Bioaftogen, DolVet, Artio-Preva/other, Emergency stock).
- **New doses_administered metric** introduced — per-vaccine cumulative administration figures for all provinces.
- **New vaccine_balance and vaccine_wastage** rows for every province.
- **New disease counts** for KZN (Pos 69, Susp 72), NC (Pos 7), NW (Pos 332), FS Suspect 363, GP dairy cows 40,000.
- **Doses distributed total (5,361,509) now within ~130k of the Ministerial figure** (5,229,966 distributed per GCIS 7 May brief).

**How to apply:** Next run should watch for: (1) 20-21 May ICC weekly engagement summary PDF; (2) Section 9 gazette (~25 May 2026); (3) further weekly template uploads; (4) MPO Week 31 dairy update.

**Parked/outstanding:**
- ICC weekly engagement summary PDF for 20-21 May — not yet in inbox
- Section 9 gazette — target ~25 May 2026
- KZN: new suspected FMD case in vaccinated herd (MPO Week 30) — monitor for confirmation and booster rollout
- LP 20 May LDARD detailed per-municipality per-vaccine-sub-type figures are not captured in main master schema (district level only)
- Source classification reminder: NW-RPO now elevated to PROGRAMME_SOURCE because no NW-DARD JOC channel exists; revisit if a state-vet-led NW JOC begins reporting
- Dose-count vs unique-animals: EC 489,979 administered is still a sum-of-doses (double-counts dose1+dose2); EC has not yet published an updated unique-animals figure since 7 May 2026
- GitHub push status: pending in this session
