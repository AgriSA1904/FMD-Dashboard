---
name: FMD daily run state
description: Latest master_data.csv row count, dashboard snapshot date, and run notes
type: project
---

As at 2026-06-03 (session 26 — automated daily ingest, two new sources):
- Master: **1,375 rows** (+23 new rows from 1,352)
- Dashboard snapshot: **2 June 2026** (advanced from 29 May — FS-DRDAR media release is programme source)
- Dashboard rebuilt: Yes — FMD_Dashboard.html updated (93,574 bytes, 23 weekly points, validation passed)

**Key highlights this run:**
- **FS-DRDAR public media release (2 June 2026) parsed from 4 WhatsApp images.** Official government confirmation: 604 total FS confirmed cases, 609,915 animals vaccinated. Adds a new state vet area (SVA) level breakdown across 15 areas.
- **New SVA breakdown for FS (15 rows):** Kroonstad 111, Heilbron 93, Frankfort 74, Bethlehem 67, Sasolburg 61, Welkom 43, Warden 40, Qwa-Qwa 28, Ladybrand 46, Bultfontein 10, Boshof 10, Fauresmith 8, Smithfield 7, Bloemfontein 4, Thaba Nchu 2 (total = 604 ✓).
- **FMD-Vaccine_Imported.xlsx (RMIS) added — national vaccine import tracker.** Total YTD imports = 8,012,900 doses. Breakdown: ARC Trivalent 12,900 (Feb), Biogenesis Bivalent 1,000,000 (Feb), DolVet Trivalent 1,500,000 (Feb), Biogenesis Trivalent 1,500,000 (Apr), DolVet Trivalent 2,000,000 (Apr), DolVet Trivalent 2,000,000 (May). Two June deliveries (DolVet + Biogenesis Trivalent) are listed without quantities — planned/pending.
- **Media release confirms Section 9 not yet applied** — references Government Gazette No. 51512 of 13 June 2025 (existing legislation), not a new Section 9 directive. Movement restrictions enforced under Section 11 of the Animal Diseases Act (Act 35 of 1984).
- **LP PCM meeting scheduled 4 June 2026 at 08:00 (Microsoft Teams)** — meeting pack was already ingested in session 25 (effective date 27 May). Attend for new figures or minutes.

**Inbox scan summary (03 June 2026):**

| Folder | New files found | Outcome |
|---|---|---|
| Root — "03 Jun 2026" dated weekly folder | Not found | No |
| inbox/Free State/02 June/ (WhatsApp images) | 4 JPEG images (parked from session 25) | **Ingested — 17 data rows** |
| inbox/RMIS/ | FMD-Vaccine_Imported.xlsx (parked from session 25) | **Ingested — 6 data rows** |
| inbox/MPO/ | No Week 32 | No |
| All other folders | No new files | No |

**Data quality notes (new):**
- FS SVA total (604) confirms FS-JOC 29 May province total; no new cases announced.
- Boshof SVA (10) and Bultfontein SVA (10) share the same case count but are distinct geographic areas; both held in master with SVA name in notes.
- National import total (8,012,900) exceeds current national distributed total (5,361,509) — delta (~2.65M) represents national stockpile not yet distributed.

**Parked/outstanding (updated):**
- Consolidated AgriSA weekly xlsx — still outstanding
- MPO Week 32 dairy update — not yet received
- Section 9 gazette — still unpublished (now ~12 days overdue). Urgent.
- ICC weekly engagement summary PDF for 19-20 May — still outstanding
- LP 4 June PCM: monitor for minutes and updated LP figures
- LP 3.5M Bioaftogen national consignment (arrived 25 May nationally): LP allocation outstanding
- June vaccine deliveries (DolVet + Biogenesis Trivalent): quantities not yet confirmed in import tracker
- LP: Vaalwater Sable FMD positive + 54 buffalo test results — monitor
- LP: Mokolo auction suspect case 28 May — results pending
- KZN booster programme confirmation — ongoing
- EC "Other / Artio-Preva" 1,250 duplication — pending
- GP OBP column-mapping discrepancy — ongoing

---

*Prior session record below (session 25, 02 June 2026):*

As at 2026-06-02 (session 25 — automated daily ingest, three new sources):
- Master: **1,352 rows** (+30 new rows from 1,322)
- Dashboard snapshot: **29 May 2026** (advanced from 22 May — FS 29 May xlsx is programme source)
- Dashboard rebuilt: Yes — FMD_Dashboard.html updated (84,857 bytes, 22 weekly points, validation passed)

**Key highlights this run:**
- **Three new sources ingested:** FS provincial xlsx (29 May), LP PCM meeting pack (4 Jun, containing 28 May minutes), RMIS feedlot orders export (2 Jun).
- **FS positive cases advanced 589 → 604** (+15 new cases, effective 29 May). Fezile Dabi remains the highest-burden district (339 cases).
- **FS animals vaccinated advanced 513,167 → 609,915** (+96,748). Significant acceleration.
- **LP animals vaccinated advanced 279,559 → 357,045** (+77,486, as at 27 May). LP-LDARD direct source; new LP total doses received = 611,680 — significantly higher than AgriSA-NAT 334,559 (methodology/timing difference; LDARD figure is authoritative).
- **LP doses administered = 359,327** (vs 203,576 AgriSA-NAT 21 May — methodology discrepancy flagged).
- **LP vaccine balance ~254,000 doses** (~4.5 weeks at current pace of 56,500/week). URGENT: Agri Limpopo flagged only 4.5 weeks of supply; 3.5M national consignment arrived 25 May but LP allocation not yet received as at 28 May.
- **Section 9 directive still unpublished** as at 28 May (confirmed in LP PCM minutes — Agri Limpopo and TLU flagged urgency; Minister expected to sign that week but not yet gazetted).
- **Mokolo auction suspect FMD case 28 May** — auction halted, samples submitted, animals quarantined.
- **Vaalwater game farm (Waterberg): FMD positive in Sable antelope**; ~54 buffalo on property to be tested.
- **RMIS: 199,752 cumulative feedlot DolVet doses ordered** across 46 orders (3 May–1 Jun 2026).
- **New Argentine vaccine consignment expected shortly** (confirmed by RMIS at 28 May PCM).
- **SA/Botswana Binational Commission 27 May**: Transboundary Animal Disease Plan by Jan 2027, coordinated vaccination/fence plan by Dec 2026.

**Inbox scan summary (02 June 2026 — re-scan):**

| Folder | New files found | Outcome |
|---|---|---|
| inbox/Free State/02 June/ | FS FMD Vaccine Data - 29.05.2026.xlsx + 4 WhatsApp images | **Ingested — 14 data rows** |
| inbox/Limpopo/ | FMD PCM MEETING PACK 20260604.pdf | **Ingested — 15 data rows** |
| inbox/RMIS/ | Vaccine Orders Export (2026-06-02).xlsx | **Ingested — 1 data row** |
| Root — "02 Jun 2026" dated weekly folder | Not found | No |
| inbox/MPO/ | Weeks 28–31 only; no Week 32 | No |
| All other folders | No new files | No |

**Data quality notes (new):**
- LP total received (611,680 LP-LDARD) vs AgriSA-NAT (334,559 as at 21 May): large discrepancy. LP-LDARD figure is authoritative — includes consignments not yet reflected in national template. Monitor for reconciliation.
- LP vaccine balance conflict: main LDARD presentation ~254,000; Decision Matrix item 260157 cites ~70,000. Both held in notes; 254,000 used as primary (internally consistent with doses received minus doses used).
- FS DolVet 466,100 data quality flag from 8 May persists — 29 May FS-JOC submission explicitly labels this as DolVet (not Bioaftogen). Original flag in master notes maintained.
- FS 29 May district positive cases sum (339+181+63+15 = 598) vs provincial total 604 — likely Mangaung Metro cases not broken down in submission.

**Parked/outstanding (updated):**
- Consolidated AgriSA weekly xlsx — still outstanding (no root dated folder found for 29 May or later)
- MPO Week 32 dairy update — not yet received
- Section 9 gazette — confirmed still unpublished as at 28 May; now ~9 days overdue. Urgent.
- ICC weekly engagement summary PDF for 19-20 May 2026 — still outstanding
- FS WhatsApp images (4 images, 02 Jun 08:43) — not yet parsed; may contain additional data
- LP 3.5M national Bioaftogen consignment arrived 25 May — LP allocation outstanding; monitor for receipt
- LP: 18 AHT positions closing 29 May — await appointment outcome
- LP: Vaalwater Sable FMD positive + 54 buffalo to be tested — monitor
- LP: Mokolo auction suspect case 28 May — results pending
- LP: Hoedspruit SAAF buffalo matter — unresolved at political level
- KZN booster programme confirmation — ongoing
- EC "Other / Artio-Preva" 1,250 duplication — still pending
- EC unique-animals figures (14 May / 21 May) — still pending
- GP OBP column-mapping discrepancy — ongoing
- MP xlsx in inbox — automated script re-scanning; archive recommended

---

*Prior session record below (session 21, 26 May 2026):*

As at 2026-05-26 (session 21 — automated daily ingest, MPO Week 31):
- Master: 1,322 rows (1,308 before this session + 14 added from MPO Week 31 PDF)
- Das