---
name: FMD daily run state
description: Latest master_data.csv row count, dashboard snapshot date, and run notes
type: project
---

As at 2026-06-02 (session 24 — automated daily ingest, no new data):
- Master: 1,322 rows (unchanged — no new inbox files found)
- Dashboard snapshot: **22 May 2026** (unchanged — no new programme data)
- Dashboard rebuilt: No — no new data; FMD_Dashboard.html unchanged

**Key highlights this run:**
- **No new files in inbox** since session 23 (01 June 2026). All inbox folders remain unchanged.
- No new dated weekly folder found ("02 Jun 2026" absent).
- MPO folder confirmed to contain only weeks 28–31; no Week 32 PDF.
- Section 9 gazette remains outstanding (expected ~25 May, now 8 days overdue).
- No ICC weekly engagement summary for 19–20 May received.
- Automated ingest script continues running but only re-processing old MP xlsx — known bug, unchanged.
- State files updated; no dashboard rebuild or GitHub push of dashboard needed this session.

**Inbox scan summary (02 June 2026):**

| Folder | Status |
|---|---|
| Root — "02 Jun 2026" dated weekly folder | Not found — no new AgriSA consolidated xlsx |
| inbox/MPO/ | Weeks 28–31 only; no Week 32 PDF |
| inbox/Mpumalanga/ | Last modified 20 May — no new files |
| inbox/Gauteng/ | Last modified 4 May — no new files |
| inbox/Free State/ | Last modified 18 May — no new files |
| inbox/Eastern Cape/ | Last modified 4 May — no new files |
| inbox/Limpopo/ | Last modified 21 May — no new files |
| inbox/North West/ | Last modified 21 May — no new files |
| inbox/ICC Reports/ | Last modified 6 May — no new ICC weekly summary |
| inbox/Ministerial Updates/ | Last modified 7 May — no Section 9 gazette found |
| inbox/AgriSA Summary and Outcomes/ | Last modified 4 May — no new ICC engagement summary |
| inbox/Western Cape/ | Last modified 20 May — no new files |
| inbox/RMIS/ | Last modified 21 May — no new files |

**Parked/outstanding (carried forward):**
- ICC weekly engagement summary PDF for 19-20 May 2026 — still not in inbox
- Section 9 gazette — expected ~25 May (now 8 days overdue); urgent follow-up recommended
- Consolidated AgriSA weekly xlsx (week of 29 May or later) — not yet available (now significantly overdue; dashboard is 11 days behind)
- MPO Week 32 dairy update — expected by Friday cadence; now overdue
- 144,000 new batch received MP week of 19 May — confirm allocation in next MP submission
- GP OBP distributed (1,700) vs administered (127,580) column-mapping discrepancy — ongoing
- EC "Other / Artio-Preva" 1,250 cell duplication — still pending EC confirmation
- EC unique-animals figure for 14 May / 21 May — still pending from EC-DRDAR
- EC Week 31 MPO dairy count (269,211) vs milestone communication (313,890) — pending clarification
- KZN booster programme confirmation (following reinfection reports in vaccinated herds)
- LP DolVet 150,000 receipt confirmation
- MP xlsx in inbox: automated script re-scanning daily with wrong effective dates — archive after confirmation (persistence flag)

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
- MP xlsx in inbox: automated scr