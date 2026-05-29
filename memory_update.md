---
name: FMD daily run state
description: Latest master_data.csv row count, dashboard snapshot date, and run notes
type: project
---

As at 2026-05-29 (session 22 — automated daily ingest, no new data):
- Master: 1,322 rows (unchanged — no new inbox files found)
- Dashboard snapshot: **22 May 2026** (unchanged — no new programme data)
- Dashboard rebuilt: No — no new data; FMD_Dashboard.html unchanged

**Key highlights this run:**
- **No new files in inbox** since session 21 (26 May 2026). All inbox folders have modification dates of 25 May or earlier.
- No new dated weekly folder found ("27 May 2026", "28 May 2026", "29 May 2026" all absent).
- No MPO Week 32 PDF received yet (MPO folder last modified 25 May — Week 31 only).
- Section 9 gazette remains outstanding (expected ~25 May, now 4 days overdue).
- No ICC weekly engagement summary for 19-20 May received.
- State files updated; no dashboard rebuild or GitHub push of dashboard needed this session.

**Inbox scan summary (29 May 2026):**

| Folder | Status |
|---|---|
| Root — "27/28/29 May 2026" dated weekly folder | Not found — no new AgriSA consolidated xlsx |
| inbox/MPO/ | No new files (last modified 25 May — Week 31 already ingested) |
| inbox/Mpumalanga/ | No new files since session 21 |
| inbox/Gauteng/ | No new files since session 20 |
| inbox/Free State/ | No new files since session 21 |
| inbox/Eastern Cape/ | No new files since session 22 |
| inbox/Limpopo/ | No new files since session 20 |
| inbox/North West/ | No new files |
| inbox/ICC Reports/ | No new ICC weekly summary |
| inbox/Ministerial Updates/ | No Section 9 gazette found |
| inbox/AgriSA Summary and Outcomes/ | No new ICC engagement summary |

**Parked/outstanding (carried forward):**
- ICC weekly engagement summary PDF for 19-20 May 2026 — still not in inbox
- Section 9 gazette — expected ~25 May (now 4 days overdue); watch Ministerial Updates
- Consolidated AgriSA weekly xlsx (week of 29 May or later) — not yet available
- MPO Week 32 dairy update — expected this week
- 144,000 new batch received MP week of 19 May — confirm allocation in next MP submission
- GP OBP distributed (1,700) vs administered (127,580) column-mapping discrepancy — ongoing
- EC "Other / Artio-Preva" 1,250 cell duplication — still pending EC confirmation
- EC unique-animals figure for 14 May / 21 May — still pending from EC-DRDAR
- EC Week 31 MPO dairy count (269,211) vs milestone communication (313,890) — pending clarification
- KZN booster programme confirmation (following reinfection reports in vaccinated herds)
- LP DolVet 150,000 receipt confirmation
- MP xlsx in inbox: automated script re-scanning daily with wrong effective dates — archive after confirmation

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
- **WC dairy cows advanced 140,746 → 150,116** (+9,370). Now 150,116 of ~240,000 WC dairy animals have received first v