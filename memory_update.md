As at 2026-06-30 (session 49 -- FS-Landbou WhatsApp timeline chart 26 Jun):
- Master: **1,997 rows** (+1 from session 49)
- Dashboard snapshot: **26 June 2026** (43 weekly points; 194,305 bytes; validation passed)
- Dashboard rebuilt: Yes — FS positive_cases updated to 648 (26 Jun); snapshot advanced from 25 Jun to 26 Jun

**New files ingested (session 49):**
- `inbox/Free State/WhatsApp Image 2026-06-29 at 12.50.17.jpeg` (FS-Landbou; chart to 26 Jun): 1 row. FS cumulative positive cases 648 as at 26 Jun 2026.

**National headlines (dashboard 26 June 2026):**
- Total positive cases (latest per province): 2,512 (EC 411, FS 648, GP 300, KZN 336, LP 84, MP 261, NW 414, NC 20, WC 38)
- Total animals vaccinated (programme sources, JOC-tracked): 4,780,875

**Data quality notes:**
- FS 648 is from FS-Landbou commodity chart — read from graph; +14 cases from 634 (FS-DARDLEA 23 Jun).
- LP vaccine_balance row in master shows 0 from 2026-06-01 (stale). LP received 775,660, administered 497,363 = implied balance ~278,297.
- EC animals_vaccinated (696,408 JOC) vs 1,001,292 incl MPO dairy — dashboard uses 696,408.

**Per-province latest figures (as at 30 June 2026):**

| Province | Received | Animals vaccinated | Positive cases | Date |
|---|---|---|---|---|
| EC | 1,117,680 | 696,408 (JOC) / 1,001,292 (all) | 411 | 25 Jun |
| FS | 838,400 | 1,053,502 | 648 | 26 Jun |
| GP | 643,300 | 333,221 | 300 | 12 Jun |
| KZN | 1,329,112 | 648,609 | 336 | 21 May / 5 Jun |
| LP | 775,660 | 495,102 (LDARD 21 Jun) | 84 | 21-24 Jun |
| MP | 747,000 | 344,629 | 261 | 22 Jun |
| NW | 1,021,140 | 876,483 | 414 | 18 Jun |
| NC | 200,600 | 114,443 | 20 | 16 Jun |
| WC | 497,100 | 299,969 | 38 | 22 Jun |

**Parked/outstanding (carry forward):**
- 1 July FMD Weekly Engagement: meeting held 1 July 2026; outcomes PDF expected in inbox.
- Section 9 gazette: Announced 25 June 2026 by Minister Steenhuisen; gazette publication still pending.
- LP PCM 6 July 2026 — next meeting confirmed; await pack and update.
- Consolidated AgriSA weekly xlsx: ~84 days outstanding. Urgent.
- 2 million DolVet doses expected mid-June — not yet confirmed in RMIS data.
- 7 million Biogenesis doses expected end July 2026 — forward pipeline.
- KZN booster programme — 240,000 done per MPO Week 36; resumption expected.
- LP DolVet 150,000 receipt — outstanding.
- KZN animals vaccinated gap (DoA 1.16 million versus master 648,609).
- MPO Week 37 — not yet in inbox.

---

As at 2026-06-29 (session 48 -- EC 25 Jun; MPO Week 36; 24 Jun outcomes; Ministerial Section 9 announcement):
- Master: **1,996 rows** (+40 from session 48)
- Dashboard snapshot: **25 June 2026** (42 weekly points; 190,849 bytes; validation passed)
- Dashboard rebuilt: Yes — snapshot advanced from 23 Jun to 25 Jun; EC and MPO data updated

**New files ingested (session 48):**
- `inbox/Eastern Cape/EC FMD Update - 25.06.2026.pptx` (EC-DRDAR; 17 image slides): 17 rows. Positive cases 411, suspected 235. Total vaccinations 1,001,292 (incl MPO dairy 304,884); JOC state+private 696,408. Doses received 1,117,680. Balance 116,388. Vaccine utilisation 89.5%.
- `inbox/MPO/Week 36 - Update on the state of FMD and vaccine rollouts in the dairy industry.pdf` (MPO; snapshot 26 Jun): 16 rows. National dairy first vaccinations 935,918; boosters 250,328. 171 dairy farms with FMD cases; 124 still active.
- `inbox/AgriSA Summary and Outcomes/24-june-2026-outcomes.pdf` (AgriSA-NAT; 24 Jun): 6 rows. GLN registrations ~12,500; ~650 vaccination sites; ~260,000 dairy boosters nationally; industry expecting to dispatch ~1.9M doses by end of week following meeting; LP 84 positive cases and ~500,000 vaccinated confirmed.
- `inbox/Ministerial Updates/MEDIA STATEMENT NEW FMD CONTROL MEASURES...pdf` (Ministry; 25 Jun): 1 row (classification event). New FMD control measures approved by Minister Steenhuisen — replaces Section 9 directives incl 2019 FMD Contingency Plan. Gazette publication pending.
- `inbox/AgriSA Summary and Outcomes/AgriSA Weekly FMD Engagement_ 2026.07.01.pdf`: Agenda only; no data rows.

**National headlines (dashboard 25 June 2026):**
- Total positive cases (latest per province): 2,498 (EC 411, FS 634, GP 300, KZN 336, LP 84, MP 261, NW 414, NC 20, WC 38)
- Total animals vaccinated (programme sources, JOC-tracked): 4,780,875

**Data quality notes:**
- EC animals_vaccinated total on slide 16 is 1,001,292 including MPO dairy (304,884). JOC-tracked state+private excl MPO: 696,408. Dashboard uses 696,408 for EC to avoid double-counting with MPO rows.
- LP vaccine_balance row in ma