---
name: FMD daily run state
description: Latest master_data.csv row count, dashboard snapshot date, and run notes
type: project
---

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
- Dashboard snapshot: **22 May 2026** (unchanged — MPO is commodity-body source, does not advance programme snapshot)
- Dashboard rebuilt: Yes — FMD_Dashboard.html updated (84,390 bytes, 20 weekly points, validation passed)

**Key highlights this run:**
- **MPO Week 31 ingested** (snapshot 22 May 2026) — 14 new rows.
- **National dairy cows vaccinated advanced 769,159 (Week 30) → 831,143 (Week 31)** (+61,984).
- **EC dairy cows advanced 216,597 → 269,211** (+52,614). All EC dairy animals expected fully vaccinated by end of week of 22 May. Note: MPO direct communication on 15 May stated milestone of 313,890 (all EC dairy vaccinated) — Week 31 table figure of 269,211 is lower; methodology difference flagged in notes.
- **WC dairy cows advanced 140,746 → 150,116** (+9,370). Now 150,116 of ~240,000 WC dairy animals have received first vaccination.
- **KZN: 3 dairy farms reported FMD reinfection post-vaccination** — symptoms significantly less severe than pre-vaccination. All KZN dairy still fully vaccinated.
- **NW Lichtenburg reinfection confirmed** (1 farm) — confirms Week 30 suspected case.
- **No new consolidated AgriSA weekly xlsx received** — snapshot date remains 22 May 2026.

**Inbox scan summary (26 May 2026):**

| Folder | Status |
|---|---|
| Root — "26 May 2026" dated weekly folder | Not found — no new AgriSA consolidated xlsx yet |
| inbox/MPO/ | **Week 31 PDF ingested** (arrived 2026-05-25 09:31, after session 20) |
| inbox/Mpumalanga/ | MP xlsx (19 May data) already in master from session 19/22; email PDF (Robert, 21 May) confirms same figures — no new rows needed |
| inbox/Gauteng/ | No new files since session 20 |
| inbox/Free State/ | No new files since session 22 |
| inbox/Eastern Cape/ | No new files since session 22 |
| inbox/Limpopo/ | No new files since session 20 |
| inbox/North West/ | No new files |
| inbox/ICC Reports/ | No new ICC weekly summary |
| inbox/Ministerial Updates/ | No Section 9 gazette found |
| inbox/AgriSA Summary and Outcomes/ | No new ICC engagement summary |

**Data quality notes:**
- EC Week 31 MPO figure (269,211) vs EC milestone communication (313,890 on 15 May): discrepancy likely reflects MPO table methodology vs milestone count. Both held in master. Monitor for resolution.
- Automated xlsx ingest script (ingest.py) is finding the MP xlsx in inbox each morning and assigning today's date as effective_date — this is a script bug; master_data.csv is unaffected as rows are deduplicated correctly. The MP xlsx should be archived once confirmed no further updates expected.

**Parked/outstanding:**
- ICC weekly engagement summary PDF for 19-20 May 2026 — still not in inbox
- Section 9 gazette — expected ~25 May (now overdue); watch Ministerial Updates
- 26 May 2026 (or later) consolidated AgriSA weekly xlsx — not yet available
- 144,000 new batch received MP week of 19 May — confirm allocation in next MP submission
- GP OBP distributed (1,700) vs administered (127,580) column-mapping discrepancy — ongoing
- EC "Other / Artio-Preva" 1,250 cell duplication — still pending EC confirmation
- EC unique-animals figure for 14 May / 21 May — still pending from EC-DRDAR
- EC Week 31 MPO dairy count vs milestone figure — pending clarification
- KZN booster programme confirmation (following reinfection reports)
- LP DolVet 150,000 receipt confirmation
- MP xlsx in inbox: automated script re-scanning daily with wrong effective dates — archive after confirmation
- GitHub push: **completed this session**
