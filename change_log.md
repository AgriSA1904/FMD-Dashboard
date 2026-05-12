# FMD Dashboard Change Log

A running record of what changed in the master and dashboard, with dates and source attribution.

---

## 2026-05-12 (session 7) — MPO Week 29 ingested (automated daily run)

**Master grew from 873 to 887 rows (+14 new rows).**

**Dashboard rebuilt:** Yes — FMD_Dashboard.html updated (75,897 bytes, validation passed). Snapshot date remains 01 May 2026 (no consolidated AgriSA weekly xlsx received).

### Inbox scan summary

| Folder | Files checked | New since last run? |
|---|---|---|
| Root (dated weekly folder) | None — no `12 May 2026/` folder | No |
| inbox/MPO/ | Week 29 PDF | **YES — ingested** |
| inbox/Free State/FMD STATISTICS 8 MAY 2026/ | 4 WhatsApp JPEG images | Parked (cannot read JPEGs via SharePoint connector) |
| inbox/Eastern Cape/ | No new files | No |
| inbox/Gauteng/ | No new files | No |
| inbox/Limpopo/ | No new files | No |
| inbox/Western Cape/ | No new files | No |
| inbox/ICC Reports/ | No new files since last run | No |
| inbox/Portfolio Committee Presentations/ | No new files | No |
| inbox/Ministerial Updates/ | No new files | No |

### Source processed

| File | Effective Date | Source Org | Outcome |
|---|---|---|---|
| `inbox/MPO/Week 29- Update on the state of FMD and vaccine rollouts in the dairy industry.pdf` | 2026-05-08 | MPO | Ingested — 14 rows added |
| `inbox/Free State/FMD STATISTICS 8 MAY 2026/WhatsApp Image 2026-05-08 at 15.35.37–41 (x4)` | 2026-05-08 | FS-JOC | Parked — JPEG format, unreadable via SharePoint connector |

### Key figures added — MPO Week 29 (as at 8 May 2026)

**Dairy cows vaccinated per province:**

| Province | Week 29 | Week 28 | Change |
|---|---|---|---|
| KZN | 360,200 | 360,159 | +41 |
| EC | 177,130 | 168,142 | +8,988 |
| FS | 15,104 | 15,104 | — |
| LP | 5,475 | 5,475 | — |
| GP | 14,832 | 14,832 | — |
| MP | 9,863 | 9,863 | — |
| NW | 6,342 | 6,342 | — |
| WC | 140,746 | 167,124 | -26,378 ⚠ |
| NC | 0 | 0 | — |
| **National** | **729,692** | **579,917** | **+149,775** |

**National dairy farm case counts:**
- Confirmed FMD farms: 171 (up from 169)
- Active FMD farms: 124 (up from 122)
- EC note: 10 cases, 8 farms on KZN border placed under EC surveillance

**Other rows added:**
- KZN new cases: 2 (Greytown and Nottingham Road; both vaccinated herds; milder clinical signs)
- EC additional doses received: 28,000 (ensures full dairy herd coverage; flooding disrupted rollout)
- MP mass vaccination event (11 May 2026): held today; feedback expected in Week 30 report

### Data quality flags

1. **WC dairy cows vaccinated DOWN**: 140,746 (Week 29) vs 167,124 (Week 28) — a decrease of 26,378. Likely Week 28 included non-dairy species and Week 29 corrected to dairy-only count. Flagged in master notes. Verify with MPO at next ICC session.
2. **National total jump**: 579,917 → 729,692 (+149,775). This jump is partly driven by the WC correction and EC progress. May need reconciliation against AgriSA-NAT totals when 08 May consolidated xlsx arrives.
3. **EC flooding disruption**: EC vaccination paused during flooding; Week 29 EC figure (177,130) likely understates actual progress as of 12 May; Week 30 report will reflect resumed rollout.
4. **MP mass vaccination (11 May)**: Event confirmed held; no outcome figures yet. Watch for MPO Week 30 PDF and any MP JOC report in inbox.

### Action items for next run

1. **Watch for 08 May or 15 May consolidated AgriSA weekly xlsx** — this will advance the dashboard snapshot date from 01 May.
2. **MPO Week 30 PDF** — will contain MP mass vaccination outcome figures and updated EC dairy progress post-flooding.
3. **4 WhatsApp JPEG images** (FS STATISTICS 8 MAY 2026 folder) — require a manual Cowork session with visual review.
4. **WC discrepancy** — Week 29 dairy figure (140,746) vs Week 28 (167,124) — confirm methodology with MPO.
5. **EC pptx ARC/BVI Alfred Nzo discrepancy** — still outstanding; confirm with EC-DRDAR.
6. **FS 7-case gap at 8 May** — confirm Mangaung Metropolitan at next FS JOC.

---

## 2026-05-08 — EC Provincial JOC Report (07.05.2026) ingested

**Master grew from 771 to 835 rows (+64 new rows).**

### Sources processed

| File | Effective Date | Type | Source Org |
|---|---|---|---|
| `inbox/Eastern Cape/Reporting of cases & vaccines - 07.05.2026.xlsx` | 2026-05-07 | EC district vaccine data spreadsheet | EC-DRDAR |
| `inbox/Eastern Cape/EC FMD Update 07.05.2026.pptx` | 2026-05-07 | EC provincial JOC presentation (13 image-only slides) | EC-DRDAR |

### Key figures added — Eastern Cape as at 07 May 2026

**Disease (provincial):**
- Confirmed outbreaks (cumulative, Dec 2025 to date): **282** (previous: 241; 41 new this period)
- Suspected: 220 (previous: 232; some converted to confirmed)
- Negative: 14

**Disease per district (cumulative):**

| District | Confirmed | Suspected | Negative |
|---|---|---|---|
| Amathole | 137 (22 new) | 96 | — |
| Alfred Nzo | 46 | 30 | 7 |
| Chris Hani | 38 (14 new) | 16 | 2 |
| Joe Gqabi | 43 (5 new) | 6 | — |
| OR Tambo | 13 | 70 | — |
| Sarah Baartman (incl. NMB) | 5 | 2 | 1 |
| **TOTAL** | **282** | **220** | **14** |

**Vaccines used (cumulative, as at 07 May 2026):**

| Vaccine | State channel | Private/MPO | Total |
|---|---|---|---|
| BVI | 1 250 | — | **1 250** |
| OBP/ARC | 2 177 | — | **2 177** (423 remaining) |
| Biogenesis Bago | 170 652 | 113 526 | **284 178** |
| DollVet | 133 888 | 48 462 | **182 350** |
| **Grand total** | **307 967** | **161 988** | **469 955** |

**Vaccines received (allocation):**
- ARC-OVI: 2 600 doses
- Bioaftogen Bivalent: 150 000 doses (28 700 to MPO; further 117 000 expected)
- DollVet: 174 380 doses total received (152 000 + 10 000 emergency + additional)
- MPO separately received: 100 000 BB Trivalent + 100 000 DollVet via national allocation

**Per-district animals vaccinated (first granular district-level breakdown for EC):**

| District | Bio (state) | DollVet (state) | ARC | BVI | Total vaccinated |
|---|---|---|---|---|---|
| Amathole | 31 216 | 51 489 | 965 | 800 | **84 470** |
| Alfred Nzo | 64 349 | 32 601 | — | 450* | **97 400** |
| Chris Hani | 41 617 | 18 974 | — | — | **60 591** |
| Joe Gqabi | 15 791 | 14 486 | — | — | **30 277** |
| OR Tambo | 14 864 | 15 288 | — | — | **30 152** |
| Sarah Baartman | 2 815 | 1 050 | 1 212 | — | **5 077** |
| MPO (private) | 113 526 | 48 462 | — | — | **161 988** |

*Alfred Nzo 450 is BVI per xlsx; slide 8 labels it as ARC — discrepancy noted in master.

### Other inbox files reviewed — no new data ingested

| File | Finding |
|---|---|
| `inbox/Free State/Screenshot 2026-05-04 100411.png` | Email from Free State Agriculture CEO confirming no FS JOC held on 1 May (public holiday). Next JOC 8 May 2026. Contextual event logged to master. |
| `inbox/Gauteng/WhatsApp Image 2026-05-04 at 14.29.29.jpeg` | GP WhatsApp figures already in master (ingested 2026-05-05). |
| `inbox/Gauteng/689472003_*.jpg` + `689472179_*.jpg` | GDARD social media infographics (29 Apr 2026) already in master (ingested 2026-05-07). |

### Known data quality flags
- EC pptx slide 8 labels Alfred Nzo's 450 doses as "ARC" but xlsx schema confirms it is BVI. Both noted in master notes.
- 282 "reported_outbreaks" in EC-DRDAR report = cumulative farms/villages since Dec 2025. This differs from the AgriSA national "positive_cases" metric (166 as at 01 May). Both are valid but count different things.
- Dashboard snapshot remains at 2026-05-01 (latest consolidated AgriSA/ICC national week). New EC district data is in master and will appear in the next national week once consolidated.

### Action items
1. **FS JOC today (8 May)** — Gernie Botha confirmed a FS update will come from today's JOC meeting. Ingest when received.
2. **EC pptx slide 8 ARC/BVI discrepancy** — Confirm with EC-DRDAR which vaccine was used in Alfred Nzo (BVI or OBP/ARC).
3. **EC expected doses** — 117 000 more Bioaftogen Bivalent and 20 000 emergency doses still expected by EC. Ingest receipt confirmation when it arrives.

---

## 2026-05-08 (weekly run — pass 2) — GP GDARD infographic 1 and FS .msg resolved

**New rows added to master:** 7 (770 → 777 rows)

**Dashboard rebuild:** Pending — shell temporarily unavailable; will rebuild on next session start.

### Sources resolved this pass

**`inbox/Gauteng/689472003_1403107838515160_3276233086600452208_n.jpg` — GDARD Infographic 1, 29 April 2026**

This is the first of the two GDARD infographic cards (the second was already ingested on 2026-05-07). It covers the GP outbreak summary with a Rand West Municipality focus.

| Metric | Value |
|---|---|
| Confirmed outbreaks (total) | 293 |
| Outbreaks open | 288 |
| Outbreaks closed | 3 |
| Susceptible population (Apr 2025–Apr 2026) | 319,708 |
| Animals vaccinated in 2026 (total) | 184,036 |
| — of which Biogenesis Bago | 65,985 |
| — of which Aftodoll | 116,518 |
| — of which ARC-OVR (local pentavalent) | 1,533 |

District breakdown captured in row notes (district drill-down remains parked):
- Pretoria: BB 25,855 / Aftodoll 36,698
- Randfontein: BB 16,048 / Aftodoll 6,944
- Germiston: BB 24,082 / Aftodoll 42,876 (+30,000 pending allocation)

**`inbox/Free State/FMD STATS.msg` — resolved via `extract-msg`**

Email from Gernie Botha, CEO Vrystaat Landbou, dated 4 May 2026. No quantitative FMD data. Body confirms: **FS FMD JOC did not meet on 1 May 2026 due to the public holiday. No updated figures for that reporting week. Next meeting scheduled 8 May 2026.** Recorded as an operational event row (joc_cancelled) against FS / 2026-05-01.

This explains the absence of a Free State update in the 1 May consolidated xlsx — not a data gap, but a known calendar gap.

### Still unresolved (OneDrive stubs — sync required)

- `inbox/FS FMD Vaccine Data - 24.04.2026.xlsx`
- `inbox/JOC FMD Outbreak 17 April Minutes.doc`

---

## 2026-05-08 (weekly run) — LP PCM meeting pack and GP JOC minutes ingested

**New rows added to master:** 10 (760 → 770 rows)

**Dashboard rebuilt:** Yes — FMD_Dashboard.html updated

**Sources scanned this run:**

| File | Status | Notes |
|---|---|---|
| `inbox/Limpopo/FMD PCM MEETING PACK 20260409 REV0.pdf` | Ingested | LP district vaccination and case data as at 2 April 2026 |
| `inbox/JOC - FMD OUTBREAK april.docx` | Ingested | GP JOC meeting 17 April — operational metrics extracted |
| `inbox/AgriSA Summary and Outcomes - FMD Weekly Engagement/Summary and Outcomes_FMD Weekly Engagement_2026.04.22.pdf` | Scanned — no new structured data | Narrative meeting summary; qualitative inputs only |
| `inbox/FS FMD Vaccine Data - 24.04.2026.xlsx` | Cannot read (OneDrive stub) | Needs user to open/download before next run |
| `inbox/Draft Summary and Outcomes FMD Weekly Engagement .zip` | Cannot read (OneDrive stub) | — |
| `inbox/JOC FMD Outbreak 17 April Minutes.doc` | Cannot read (OneDrive stub) | — |
| `inbox/Eastern Cape/EC FMD Update 07.05.2026.pptx` | Previously noted as image-only | Already flagged in 2026-05-08 earlier run |
| `inbox/Free State/FMD STATS.msg` | Unreadable (.msg format) | Needs manual review |
| `inbox/54476 10-4 Agriculture.pdf` | Skipped — parliamentary Q&A | No new quantitative FMD data |
| `inbox/REVISED_Guidelines for Hunting in EC_Current FMD_Apr_2026.pdf` | Skipped — regulatory/guidance doc | No new case/vaccine data |
| `inbox/Gauteng/689472003_1403107838515160_3276233086600452208_n.jpg` | Not read this run | Requires visual review |
| `inbox/Gauteng/WhatsApp Image 2026-05-04 at 14.29.29.jpeg` | Previously ingested (2026-05-07) | — |
| `inbox/Western Cape/Screenshot 2026-05-04 084158.png` | Previously ingested | — |
| `inbox/Free State/WhatsApp images (6 files)` | Previously ingested or held | Earlier FS images already in master |

### New data ingested

**Limpopo PCM Meeting Pack (data effective 2 April 2026)**

LP animals vaccinated by sector (as at 2 April 2026):
- Commercial: 57,220
- Communal: 62,688
- Emerging farming: 9,029
- **Total: 128,937**

Note: These sector-level figures are distinct from the Apr-24 AgriSA consolidated figures (commercial 50,332 / communal 65,749) — the LP PCM reporting uses slightly different sector definitions and the totals are the same (128,937).

LP case status by district (as at 2 April 2026):
- **Waterberg:** 193 total — 128 pending, 26 suspect, 13 pos, 23 neg, 2 Day0, 1 closed (dominant district)
- **Vhembe:** 47 total — 15 suspect, 13 neg, 11 pos, 6 Day0, 2 closed
- **Capricorn:** 53 total — 28 neg, 10 pos, 7 suspect, 7 Day0, 1 closed
- **Sekhukhune:** 33 total — 12 neg, 8 suspect, 7 Day0, 5 pos, 1 closed
- **Mopani:** 9 total — 8 neg, 1 pending
- **Provincial total: 40 confirmed positive, 56 suspect, 189 pending**

District data is stored in master row notes (district drill-down dashboard build remains parked pending JOC reporting template update).

LP RFID ear tag logistics (effective 25 March 2026): 20,000 tags received; 15,000 distributed to Waterberg, Sekhukhune and Capricorn.

**Gauteng JOC 17 April 2026 minutes**

- Interprovincial movement permits issued to date: **4,298**
- Private vet vaccine bottles issued: **1,686** (as at 17 April; Apr-29 figure of 3,529 in master is more current)
- ~40,000 animals vaccinated by private vets (reconciliation outstanding at time of meeting)
- ~50% compliance at auctions and roadblocks with required documentation
- 126 Kebani/cultural slaughter sites identified for targeted intervention

**Source discrepancy flagged — Gauteng outbreak counts:**

The GP JOC 17 April reports **289 confirmed outbreaks (286 open, 3 new that week)** at the provincial level. The national MinMEC/Portfolio Committee data shows **243 outbreaks for GP at April 17**. This gap (289 vs 243) likely reflects different counting methodologies — provincial system counts all cases including suspect/pending, national reporting may count only lab-confirmed. Dashboard uses national figures as canonical; provincial JOC figures retained in notes for context.

### No new weekly JOC xlsx received yet for 8 May 2026

The AgriSA consolidated weekly xlsx (which drives the headline snapshot date on the dashboard) has not yet been submitted. Current snapshot remains **1 May 2026**. Expected from provincial JOCs after Friday 8 May meetings.

### Files requiring manual handling next session

- `inbox/FS FMD Vaccine Data - 24.04.2026.xlsx` — OneDrive stub; open in Excel to download, then re-run
- `inbox/Draft Summary and Outcomes FMD Weekly Engagement .zip` — OneDrive stub
- `inbox/JOC FMD Outbreak 17 April Minutes.doc` — OneDrive stub (older .doc format)
- `inbox/Free State/FMD STATS.msg` — Outlook message format, not auto-readable
- `inbox/Gauteng/689472003_1403107838515160_3276233086600452208_n.jpg` — first GP image, needs visual review

---

## 2026-05-08 — MinMEC 7 May 2026 presentation ingested (automated daily run)

**New rows added to master:** 99 (661 → 760 rows, after deduplication)

**Dashboard rebuilt:** Yes — FMD_Dashboard.html updated

**Source:** `inbox/Portfolio Committee Presentations/FOOT AND MOUTH PRESENTATION TO MINMEC (7 MAY 2026).pptx`

**Files scanned (no structured data extractable):**
- `inbox/Eastern Cape/EC FMD Update 07.05.2026.pptx` — image-only slides, no text extractable
- `inbox/Ministerial Updates/GCIS EDITORIAL BRIEF fmd.docx` — editorial brief, no new quantitative data beyond what was already in master from ministerial briefing (05 May)
- `inbox/Free State/FMD STATS.msg` — .msg format, not extractable

### New data ingested

**Slide 5 — Per-province cumulative reported outbreaks (8 dates × 10 provinces = 80 rows)**

| Province | 2 Mar | 10 Mar | 13 Mar | 20 Mar | 27 Mar | 10 Apr | 17 Apr | 24 Apr |
|---|---|---|---|---|---|---|---|---|
| Eastern Cape | 33 | 33 | 35 | 55 | 69 | 71 | 104 | 110 |
| Free State | 277 | 307 | 316 | 316 | 321 | 328 | 414 | 462 |
| Gauteng | 195 | 196 | 215 | 219 | 230 | 241 | 243 | 245 |
| KwaZulu-Natal | 202 | 202 | 222 | 225 | 225 | 225 | 257 | 309 |
| Limpopo | 23 | 28 | 36 | 42 | 46 | 49 | 55 | 63 |
| Mpumalanga | 79 | 81 | 105 | 108 | 108 | 140 | 144 | 159 |
| North West | 119 | 123 | 161 | 175 | 209 | 247 | 268 | 279 |
| Northern Cape | 1 | 1 | 2 | 2 | 2 | 3 | 4 | 5 |
| Western Cape | 3 | 6 | 10 | 10 | 13 | 13 | 13 | 20 |
| **NATIONAL** | **932** | **957** | **1 102** | **1 152** | **1 223** | **1 317** | **1 502** | **1 642** |

**Slide 8 — Provincial vaccine allocation totals (as at 23 April 2026, 9 rows)**

| Province | Total Doses Allocated |
|---|---|
| Eastern Cape | 440,600 |
| Free State | 566,812 |
| Gauteng | 393,140 |
| KwaZulu-Natal | 1,137,112 |
| Limpopo | 261,720 |
| Mpumalanga | 291,736 |
| North West | 248,940 |
| Northern Cape | 100,600 |
| Western Cape | 150,340 |

**Slide 9 — Dollvet Trivalent industry allocations (29 April 2026, 4 rows)**

| Sector | Doses |
|---|---|
| Feedlot | 150,000 |
| Dairy | 100,000 |
| Stud | 50,000 |
| Pig | 20,000 |

**Slide 10 — Dairy cows vaccinated per province (as at 23 April 2026, 10 rows)**

| Province | Dairy Cows Vaccinated |
|---|---|
| Eastern Cape | 124,303 |
| Western Cape | 98,808 |
| KwaZulu-Natal | 360,159 |
| Free State | 15,104 |
| North West | 6,342 |
| Mpumalanga | 9,863 |
| Limpopo | 5,475 |
| Gauteng | 14,832 |
| Northern Cape | 0 |
| **NATIONAL** | **634,886** |

**Policy / capacity events recorded (3 rows):**
- MinMEC noted the presentation (2026-05-07)
- 358 AHTs required nationally for rollout
- RMIS to employ 20 AHTs on 1-year contract at R10,000/month

### Current snapshot (01 May 2026 — unchanged, awaiting 08 May weekly xlsx)

No updated provincial JOC xlsx available yet for 8 May 2026. Next expected: Friday 8 May (today) or early next week.

- **EC FMD Update 07.05.2026.pptx** was image-only — no structured data extracted. Manual review recommended.
- **FS JOC** noted as cancelled 1 May (public holiday per earlier screenshot); status of 8 May meeting unknown.

---

## 2026-05-07 — Gauteng GDARD (image 2) and WC AWC/RPO update ingested (automated daily run)

**New rows added to master:** 16 (644 → 660 rows)

**Dashboard rebuilt:** Yes — FMD_Dashboard.html updated

**Sources processed:**

| File | Date | Province | Type |
|---|---|---|---|
| `inbox/Gauteng/689472179_1403112188514725_9185104008803752555_n.jpg` | 29 Apr 2026 | GP | GDARD infographic — depopulation, private vet, doses issued |
| `inbox/Western Cape/AWC and RPO FMD update 4 Mei 2026.pdf` | 4 May 2026 | WC | AWC/RPO media update — total vaccinated, district progress, new case |

### Gauteng — GDARD supplementary figures (29 April 2026)

Data from the second GDARD infographic card (Rand West Municipality focus). Primary vaccination figures were already ingested in the 2026-05-04 session. Additional operational metrics now added:

| Metric | Value | Notes |
|---|---|---|
| Cattle slaughtered (depopulation) | 223 840 | Control measure under Section 10; Rand West municipality |
| Outbreaks closed | 3 | Of 293 total outbreaks |
| Outbreaks open | 288 | Of 293 total outbreaks |
| Susceptible animals on affected farms | 319 708 | 1 Apr 2025 – 29 Apr 2026; Rand West |
| Private vets applied to vaccinate | 48 | 18 Tshwane, 10 Germiston, 20 Randfontein |
| Farmer applications approved | 308 | Applications for private vaccination |
| Vaccine bottles issued to private vets | 3 529 | |
| FMD doses issued (GP total) | 177 050 | |
| Private vet doses administered | 42 461 | 134 589 awaiting reconciliation from PVs |

### Western Cape — AWC/RPO update (4 May 2026)

**Key figures:**

| Metric | Value | Notes |
|---|---|---|
| Total cattle vaccinated (WC) | 449 370 | AWC/RPO figure as at 4 May 2026 |
| New confirmed FMD case | 1 | Garden Route district; De Rust/Oudtshoorn area; herd of 59 cattle; confirmed 29 Apr 2026 |

**District vaccination progress:**
- West Coast: 65%
- City of Cape Town: 58%
- Garden Route: 42%
- Cape Winelands: 37%
- Central Karoo & Overberg: 0%

**⚠ DISCREPANCY — WC vaccinated figures:**
- AWC/RPO (4 May): 449 370 cattle vaccinated
- WC-GIS portal (1 May): 176 079 vaccinations recorded
- Gap: 273 291

Likely explanation: AWC/RPO figures include all vaccination channels (state vet, private vets, community); WC GIS portal may reflect only state-vet-recorded or registered-site vaccinations. Both figures held in master and labelled by source. **Verify methodology at next ICC session.**

**WC positive case update:** The new Garden Route case (confirmed 29 Apr 2026) means WC positive cases may exceed the 25 recorded in the 1 May GIS snapshot. This was not quantified — cannot confirm the exact cumulative positive count from this source alone.

### Next expected data
- **08 May 2026 folder** (Friday) — weekly consolidated AgriSA xlsx submission
- FS JOC cancelled on 1 May (public holiday); next FS JOC meeting 8 May — may affect completeness of 08 May submission

---

## 2026-05-06 — Ministerial media briefing ingested (automated daily run)

**New rows added to master:** 18 (626 -> 644 rows)

**Dashboard rebuilt:** Yes — FMD_Dashboard.html updated; new Ministerial Update section added

**Source:** Ministerial media briefing, Minister Steenhuisen, 5 May 2026 (Latin America outcomes, Section 10 scheme, FMD update)

### Key figures from ministerial briefing

| Metric | Value | Notes |
|---|---|---|
| Total doses procured nationally | 6 000 000 | Biogenesis Bago 2.5M + Dollvet 3.5M |
| Doses distributed to provinces | 5 229 966 | As of 5 May 2026 |
| Animals vaccinated (ministerial) | 2 590 016 | As of 23 April 2026; all cloven-hoofed animals |

**Ministerial vs ICC discrepancy:** doses_received 6M vs ICC 2 828 860 (ministerial = total national procurement; ICC = provincial allocation); animals_vaccinated 2 590 016 vs ICC 2 148 494 (methodology differs). Both figures held in master and displayed side-by-side on dashboard.

### Policy milestones captured

- **2026-05-04:** Section 10 Routine Vaccination Scheme gazetted; private voluntary vaccination enabled under state vet supervision
- **2026-05-05:** KZN Disease Management Area (DMA) formally lifted

### Upcoming vaccine supply pipeline

- 4 million Dollvet doses in transit; expected ~2026-05-15
- 5 million Biogenesis Bago doses; import procedures underway; expected ~2026-05-20

### No new weekly submission

No new dated folder present. Next expected: Friday 8 May 2026 (folder `08 May 2026/`)

---

## 2026-05-03 — Dashboard rebuild (automated scheduled run)

**New rows added to master:** 0 (master already up to date at 383 rows)

**Dashboard rebuilt:** Yes — FMD_Dashboard.html rebuilt from 8 weekly snapshots (latest: 2026-05-01)

**Cowork artifact created:** `fmd-dashboard` — live dashboard now available in Cowork sidebar

### Summary of current data (as at 01 May 2026)

| Metric | Value |
|---|---|
| Doses received (national) | 2 828 860 |
| Animals vaccinated (national) | 2 148 494 |
| Vaccine balance (unadministered) | 680 366 |
| Positive cases | 1 474 |
| Suspected cases | 868 |
| Provinces with data | All 9 (EC, FS, GP, KZN, LP, MP, NC, NW, WC) |

### Week-on-week change (17 Apr → 01 May 2026)
- Doses received: +149 960
- Animals vaccinated: +94 961
- Positive cases: +126

---

## 2026-05-02 — Weekly inbox scan (automated scheduled run)

**New rows added to master:** 0 (master unchanged at 373 rows / 366 current)

**Dashboard rebuilt:** No (no new data)

**Files in inbox:** 16 files + 1 subfolder (Free State WhatsApp images)

### Auto-parsed (ingest pipeline)
None. No consolidated xlsx with a `National` sheet was readable this week.

### Files successfully read — contextual/reference documents (no structured data extracted yet)
These files were opened and confirmed readable, but require a manual Cowork session to extract and ingest structured observations:

| File | Date | Type | Priority |
|---|---|---|---|
| `04-17-2026_FMD ICC Update.pdf` | 17 Apr 2026 | ICC national rollout dashboard + policy updates | HIGH — contains per-province figures not yet in master as a standalone row set |
| `04-24-2026_FMD ICC Update.pdf` | 24 Apr 2026 | ICC national rollout dashboard + Dollvet clearance news | Medium — national figures already in master; confirms 2 828 860 doses / 2 119 020 vaccinated / 1 474 positive |
| `17042026_FMD Graphics_V1.pdf` | 17 Apr 2026 | FMD Vaccine Rollout graphics deck (all provinces) | Medium — confirms 17 Apr figures already in master |
| `24042026_FMD Graphics_V2.pdf` | 24 Apr 2026 | FMD Vaccine Rollout graphics deck (all provinces) | Medium — confirms 24 Apr figures already in master |
| `01042026_FMD Graphics_V2.pdf` | 1 Apr 2026 | FMD Vaccine Rollout graphics deck (all provinces) | Medium — confirms 1 Apr figures already in master |
| `25032026_FMD Graphics.pdf` | 25 Mar 2026 | FMD Vaccine Rollout graphics deck (all provinces) | Medium — shows 25 Mar national: 2 077 682 received / 828 868 vaccinated / 1 067 positive; slightly predates the 26 Mar backfill row |
| `FMD PCM MEETING PACK 20260409 REV0.pdf` | 9 Apr 2026 | PCM meeting pack (7.3 MB) | HIGH — likely contains 9 April provincial data not currently in master |
| `54476 10-4 Agriculture.pdf` | 10 Apr 2026 | Agriculture document | Medium — date suggests possible 10 April data |
| `Media Statement Minister Steenhuisen announces progress in Foot and mouth disease vaccination strategy.pdf` | Apr 2026 | Ministerial media statement | Low — narrative only |
| `Media Statement More vaccines arrive to strengthen war against foot and mouth disease_22042026_.pdf` | 22 Apr 2026 | Media statement re: Dollvet consignment | Low — confirms Dollvet arrival; narrative only |
| `REVISED_Guidelines for Hunting in EC_Current FMD_Apr_2026 - UPDATED (003).pdf` | Apr 2026 | EC hunting guidelines under FMD | Low — policy/regulatory reference |

**Key figure cross-check from ICC PDFs (confirms master is correct for 17 and 24 April):**
- 17 Apr: national received 2 678 900 / vaccinated 2 053 533 / positive 1 348 / suspected 818 ✓
- 24 Apr: national received 2 828 860 / vaccinated 2 119 020 / positive 1 474 / suspected 868 ✓

### Files that are OneDrive placeholders — cannot be read until synced
These returned `Invalid argument` on both initial copy and retry (5-second delay):

| File | Issue |
|---|---|
| `FS FMD Vaccine Data - 24.04.2026.xlsx` | **PERSISTENT** — also unreadable in the 2026-04-28 and 2026-04-30 runs. Contains Free State provincial data for 24 April. Please open in OneDrive to force sync. |
| `EC FMD Update - 23.04.2026 Final.pptx` | OneDrive placeholder. Contains EC provincial FMD update 23 April. |
| `JOC - FMD OUTBREAK april.docx` | OneDrive placeholder. JOC outbreak notes (April). |
| `JOC FMD Outbreak 17 April Minutes.doc` | OneDrive placeholder. 17 April JOC meeting minutes. |
| `260421Presentation_to_the_Portfolio_Committee_on_Agriculture_21st_April_2026_FINAL.pdf` | OneDrive placeholder. Portfolio Committee presentation 21 April. |

### Free State subfolder (`inbox/Free State/`)
Contains 6 WhatsApp images (JPEG, dated 23 April 2026) — photographs of what appear to be handwritten or printed vaccine data sheets. **Need manual review** to transcribe figures and ingest.

### Provincial changes week-on-week
None — master unchanged this run.

### Backdated revisions
None — master unchanged this run.

### Action items for next manual Cowork session
1. **Force-sync** `FS FMD Vaccine Data - 24.04.2026.xlsx` in OneDrive on your machine, then re-run ingest.
2. **Force-sync** the 4 other OneDrive placeholder files listed above.
3. **Ask Cowork to read** `FMD PCM MEETING PACK 20260409 REV0.pdf` to extract 9 April provincial figures (a week currently absent from master).
4. **Ask Cowork to transcribe** the 6 WhatsApp images in `inbox/Free State/` to add FS provincial vaccination observations.
5. **Ask Cowork to read** `04-17-2026_FMD ICC Update.pdf` and extract per-province rows for 17 April into master (currently master only has national-level data for that week).

---

## 2026-04-30 — 01 May 2026 weekly submission ingested (automated daily run)

**Sources processed:**
- `01 May 2026/AgriSA - FMD Vaccination Data - 01.05.26.xlsx` — AgriSA consolidated weekly workbook for the 01 May reporting period. All 9 provincial sheets successfully read. **100 new rows added to master** (273 → 373).

**Dashboard snapshot updated to: 01 May 2026**

**National headline figures (01 May, from ICC/presentation):**
- Total doses received: 2 828 860 (unchanged from 24 April — no new vaccines arrived this week)
- Animals vaccinated: 2 148 494 (+29 474 vs 24 April — slowest weekly intake to date)
- Vaccine balance: 680 366
- Positive cases: 1 474 (national ICC figure; see data quality note below)
- Suspected cases: 868

**Provincial data added (01 May):**
- Disease data now available for all 9 provinces
- EC: vaccinated 332 182 (+29 631 vs 24 Apr); positive 166; suspected 258
- FS: received 397 340; positive 456 (highest province); suspected 361
- GP: received 284 720; vaccinated 149 783; positive 289; suspected 2
- KZN: received 760 040; positive/suspected 0 (no new cases this week)
- LP: received 126 720; no cases reported
- MP: received 197 000; positive 203; suspected 104
- NW, NC, WC: received data updated; no cases reported

**Data quality notes for manual attention:**

1. **EC total_received formula not cached in xlsx.** EC's total_received column reads 0 because the Excel formula was not recalculated before saving. Component values are present (Bioaftogen 150 000 + Dolvet 152 000 + OBP/ARC 2 600 + BVI 2 600 = 307 200). Dashboard falls back to the 24 April EC figure (304 600). Correct 01 May EC received is approximately 307 200.

2. **Several provinces show lower received values vs prior week** (FS: 547 300 → 397 340; KZN: 775 040 → 760 040; LP: 151 720 → 126 720; NW: 177 400 → 161 420; WC: 230 140 → 150 340). Inconsistent with a cumulative data model — suggests either weekly-only reporting or data corrections. National ICC total (2 828 860) is unaffected.

3. **National disease figure held from ICC.** Xlsx TOTAL row shows 1 114 positive (EC+FS+GP+MP only). ICC national figure of 1 474 retained as canonical. Difference of 360 cases from provinces not reporting this week (LP, NW, NC, KZN, WC). Verify at next ICC meeting.

4. **FS FMD Vaccine Data - 24.04.2026.xlsx still unreadable.** File shows 19 645 bytes in metadata but returns OS error — still likely an OneDrive Files-on-Demand placeholder.

**Inbox status:** All xlsx attempted; 1 unreadable (FS). Remaining inbox items are PDFs/docs held for manual review.

---

## 2026-05-02 — Free State WhatsApp images ingested (automated daily run)

**Sources processed:**
- `inbox/Free State/WhatsApp Image 2026-04-23 at 08.27.08.jpeg` — FS DARDLEA media release, 17 April 2026
- `inbox/Free State/WhatsApp Image 2026-04-23 at 08.27.09.jpeg` — FSP status map, 16 April 2026
- `inbox/Free State/WhatsApp Image 2026-04-23 at 08.27.33 (2).jpeg` — VS BKS JOC feedback, 17 April 2026
- `inbox/Free State/WhatsApp Image 2026-04-23 at 08.27.34.jpeg` — VS BKS facts sheet, 17 April 2026

**10 new rows added to master** (373 → 383), effective_date 2026-04-17, province FS.

**FS figures as at 17 April 2026:**
- Positive cases: 443 (outbreaks confirmed in 18 municipalities; FS highest province nationally at this date)
- Suspected farms: 346
- Vaccine received: 637 300 doses total (440 000 Biogenesis Bago + 195 000 Dolvet + 2 300 LNR) — Vrystaat Landbou JOC
- Animals vaccinated: 353 447 cattle — FS DARDLEA media release (canonical); JOC breakdown: 191 016 BB + 162 431 Dolvet + 2 300 LNR

**Context captured from images (not structured data):**
- No vaccinations in FS mid-Dec 2025 to 25 Feb 2026 — explains the case surge visible in the FS timeline chart
- Hotspot municipalities: Viljoensdorp/Vredefort, OD/Welkom/Ventersburg, QwaQwa/Harrismith, Winburg
- FMD abattoirs approved: Sernick-Kroonstad & SPARTA-Welkom
- 150 000 additional Biogenesis Bago doses arrived in FS on 15 April 2026

**Dashboard rebuilt:** Snapshot date remains 01 May 2026 (national headline). FS 17 April data enriches the province-level historical series.

**No new weekly submission detected** — no files added to the OneDrive root or dated folders since the 2026-04-30 run. Next expected submission: Friday 8 May 2026.

**Held/skipped this run:**
- `inbox/Free State/WhatsApp Image 2026-04-23 at 08.27.33.jpeg` — FS FMD timeline chart (Jul 2025 – Apr 2026); graphical, no new structured numbers
- `inbox/Free State/WhatsApp Image 2026-04-23 at 08.27.33 (1).jpeg` — Cases per infected region chart; municipality-level, held for potential deep-dive analysis

---

## 2026-04-28 — RPO and MPO commodity submissions ingested

**Sources processed and archived:**
- `RPO Info/Vaccine Rollout Stats.xlsx` (RPO national-by-province summary)
- `RPO Info/Fw_ ENTINGS - KOMMUNAAL _ KOMMERSIEEL/*.xlsx` (4 NW district workbooks: Bojanala, DKK, DRSM, NMMD — held for manual review, too granular for dashboard rollup)
- `RPO Info/Screenshot 2026-04-28 145339.png` (held for manual review)
- `MPO Info/Copy of FMD Vaccination Data 17 April 2026.xlsx` (district-level, totals match AgriSA's existing 17 April submission)
- `04-10-2026_FMD ICC Update.pdf` (narrative update referencing 1 April vaccine figures; no new week)

**New rows added to master:** 73 (197 → 270)

**New dimensions surfaced on dashboard:**
- RPO classification breakdown by animal type: Dairy, Commercial Beef, Pigs, Communal
- New section "Commodity organisation view" with RPO classification doughnut and cross-source comparison table
- Sources used list now includes RPO and MPO references

**Cross-source discrepancy flagged:**
- AgriSA national vaccines received: 2 828 860
- RPO national vaccines received:    2 532 849 (gap: 296 011)
- AgriSA national animals vaccinated: 2 148 494
- RPO national animals vaccinated:    1 214 088 (gap: 934 406)
- The animals-vaccinated gap is the larger concern. RPO appears to count commercial cattle classifications only; AgriSA total includes broader provincial returns including communal stock and possibly other species. The dashboard now shows both side by side rather than picking one as canonical.

**10 April ICC Industry Update — narrative only:**
- No JOC submissions were received for the 8 April reporting cycle. ICC held over 1 April figures.
- This is itself worth flagging at the next ICC meeting: a four-week gap in JOC reporting between 1 April and 17 April is the underlying cause of the dashboard's "Pace slowing" indicator.

**Held in inbox for manual handling (not auto-ingested this run):**
- 6 weekly graphics PDFs (25 March, 1 April, 17 April, 24 April) — already covered by their xlsx counterparts in the master
- 2 ICC update PDFs (17 April, 24 April) — already covered by xlsx returns
- Portfolio Committee briefing (21 April), MinMEC presentation (23 April), Media Statements from Minister's office, EC FMD Update pptx, JOC minutes (DOC and DOCX), FMD PCM Meeting Pack — these contain narrative context useful for the gap memo to the ICC, but no new structured numbers
- `FS FMD Vaccine Data - 24.04.2026.xlsx` is currently a 0-byte OneDrive Files-on-Demand placeholder; will retry on next sync
- `RPO Info/Screenshot 2026-04-28 145339.png` — needs visual interpretation in a future session
- 4 NW district vaccination workbooks — farm-level granularity, useful for an NW deep-dive but not for the national dashboard

---

---

## 2026-05-04 — Daily automated run

**New rows added to master:** 44 (master: 383 → 427 rows)

**Dashboard rebuilt:** Yes — FMD_Dashboard.html updated

**Trigger:** Backfill of 8 missing provinces for 17 April 2026 from HIGH-priority source flagged in previous run

### New data ingested

**Source:** `inbox/04-17-2026_FMD ICC Update.pdf` (FMD ICC weekly update, 17 April 2026)

Provinces previously missing 17 Apr data — now added:

| Province | Received | Vaccinated (D1) | Pos Cases | Susp Cases |
|---|---|---|---|---|
| Eastern Cape | 304,600 | 296,255 | 136 | 222 |
| Gauteng | 285,000 | 133,004 | 262 | 13 |
| KwaZulu-Natal | 775,040 | 648,609 | 69 | 72 |
| Limpopo | 151,720 | 128,937 | 40 | 56 |
| Mpumalanga | 197,020 | 176,811 | 203 | 104 |
| North West | 177,400 | 168,748 | 190 | — |
| Northern Cape | 85,640 | 28,054 | 2 | 2 |
| Western Cape | 230,140 | 160,701 | 13 | 17 |

Province totals vaccinated sum to **2,053,533** — matches confirmed national ICC total exactly.

### No new files found
- No `08 May 2026/` folder yet (next weekly xlsx expected Friday 9 May 2026)
- Inbox FS xlsx (`FS FMD Vaccine Data - 24.04.2026.xlsx`) still unreadable — permission issue on mount persists

### Current snapshot (01 May 2026 — unchanged)
- Doses received: 2,828,860
- Animals vaccinated: 2,148,494
- Balance: 680,366
- Positive cases: 1,474

---

## 2026-05-04 — Manual inbox ingest (session 2)

**New rows added to master:** 77 (427 → 504 rows)

**Dashboard rebuilt:** Yes

**New files processed:**

| File | Type | Data extracted |
|---|---|---|
| `inbox/Western Cape/Screenshot 2026-05-04 084158.png` | WC GIS portal screenshot | WC 1 May: 330,140 received, 176,079 vaccinated, 25 cases, 784 sites, 29 private vets |
| `inbox/260428FOOT_AND_MOUTH_PRESENTATION_TO_THE_PORTFOLIO_COMMITTEE_ON_AGRICULTURE_28_APRIL_2026.pdf` | Portfolio Committee presentation 28 Apr | Per-province outbreak counts (02 Mar → 17 Apr); provincial vaccination as at 17 Apr |
| `inbox/Free State/Screenshot 2026-05-04 100411.png` | Email screenshot (Gernie Botha, Vrystaat Landbou) | Contextual note only — FS JOC cancelled 1 May (public holiday); next meeting 8 May |

**Key changes:**
- WC 1 May doses_received updated: 150,340 (AgriSA allocation) → 330,140 (WC GIS actual receipts)
- WC 1 May animals_vaccinated added: 176,079
- WC 1 May positive_cases corrected: 0 → 25
- Historical per-province outbreak data added for 9 provinces across 7 dates (02 Mar to 17 Apr)
- Provincial vaccination figures as at 17 Apr added from Ministry/PCM source (corroborating data)

**Bug fixes:**
- Dashboard templ
---

## 2026-05-08 (session 5) — FS district disease data ingested; dashboard rebuilt

**Master grew from 835 to 843 rows (+8 new rows).**

**Dashboard rebuilt:** Yes — FMD_Dashboard.html updated (75 610 bytes, 11:25 UTC)

### Source resolved

| File | Effective Date | Type | Source Org |
|---|---|---|---|
| `inbox/FS FMD Vaccine Data - 24.04.2026.xlsx` | 2026-04-24 | FS provincial JOC district disease report | FS-JOC |

Previously stuck as an OneDrive Files-on-Demand stub in all prior sessions. Now accessible via the SharePoint connector.

### New data added

**Provincial conflict row (positive_cases):**
- FS-JOC submission: **456 confirmed** cases as at 24 April 2026
- AgriSA-NAT consolidated (already in master): **433 confirmed**
- Gap of 23 cases likely reflects timing lag between provincial JOC returns and the national consolidation. Both figures held in master. FS-JOC figure is more current.

**Provincial conflict row (suspected_cases):**
- FS-JOC: **361 suspected** vs AgriSA-NAT: **346 suspected**

**District-level confirmed positive cases (first FS district breakdown in master):**

| District | Confirmed Cases | Sub-district detail |
|---|---|---|
| Fezile Dabi | 249 | Mafube 35, Metsimaholo 46, Moqhaka 95, Ngwathe 73 |
| Thabo Mofutsanyana | 147 | Dihlabeng 21, Maluti-A-Phofung 24, Mantsopa 3, Nketoana 20, Phumelela 36, Setsoto 43 |
| Lejweleputswa | 39 | Masilonyana 3, Matjhabeng 17, Nala 7, Tokologo 5, Tswelopele 7 |
| Xhariep | 11 | Kopanong 7, Letsemeng 1, Mohokare 3 |
| Mangaung Metropolitan | 5 | No sub-municipal breakdown in source |
| **Unallocated gap** | **5** | District totals sum to 451 vs provincial 456; 5 cases unassigned |

### Data quality flag
- Fezile Dabi (249 cases) is the dominant FS hotspot — Ventersburg/Sasolburg belt. Moqhaka LM alone has 95 confirmed cases.
- District totals sum to 451; provincial figure is 456. Gap of 5 flagged as `positive_cases_district_gap` row. Likely a 6th district with delayed return or a rounding/lag issue. Monitor at next JOC.

### Snapshot date
Still **2026-05-01**. No new weekly consolidated xlsx received. FS JOC met today (8 May) — submission expected. Check OneDrive for `08 May 2026/` folder before next dashboard presentation.

### Action items
1. **Watch for 08 May 2026 weekly xlsx** — ingest and advance snapshot date when received.
2. **FS 5-case gap** — confirm missing district at next FS JOC.
3. **EC ARC/BVI Alfred Nzo discrepancy** — still outstanding.

---

## 2026-05-11 (session 6) — FS JOC 8 May + MPO Week 28 ingested (automated daily run)

**Master grew from 843 to 873 rows (+30 new rows).**

**Dashboard rebuilt:** Yes — FMD_Dashboard.html updated (75 797 bytes, validation passed). Snapshot date remains 01 May 2026 (no new consolidated AgriSA weekly xlsx received).

### Sources processed

| File | Effective Date | Source Org | Outcome |
|---|---|---|---|
| `inbox/Free State/FMD STATISTICS 8 MAY 2026/FS FMD Vaccine Data - 8.05.2026.xlsx` | 2026-05-08 | FS-JOC | Ingested — disease + vaccination + district breakdown (27 rows) |
| `inbox/Free State/FMD STATISTICS 8 MAY 2026/WhatsApp Image 2026-05-08 (x4 JPEGs)` | 2026-05-08 | FS-JOC | Parked — JPEG images, no text extraction; likely district maps/handwritten figures |
| `inbox/MPO/Week 28- Update on the state of FMD and vaccine rollouts in the dairy industry.pdf` | 2026-05-01 | MPO | Ingested — dairy cows vaccinated per province + national farm count (3 rows from append) |

### Key figures added

**Free State — as at 8 May 2026 (FS-JOC submission):**

| Metric | Value | Change from last FS-JOC (24 Apr) |
|---|---|---|
| Positive cases (provincial) | 473 | +17 vs 456 |
| Suspected cases (provincial) | 467 | +106 vs 361 |
| Bioaftogen received (total) | 466,100 | — |
| Bioaftogen received (state vet) | 370,000 | — |
| OBP/LNR received | 2,300 | unchanged |
| Total received (state vet all types) | 838,400 | — |
| Animals vaccinated Dose 1 (all types) | 399,397 | +45,950 vs 353,447 (17 Apr DARDLEA) |
| Animals vaccinated Dose 2 (all types) | 63,007 | First Dose 2 figure in master for FS |
| Bioaftogen Dose 1 (state vet) | 69,341 | — |
| Bioaftogen Dose 1 (total) | 193,164 | — |

**FS District breakdown — positive cases (8 May 2026):**

| District | Cases | Sub-district detail |
|---|---|---|
| Fezile Dabi | 256 | Mafube 37, Metsimaholo 46, Moqhaka 98, Ngwathe 75 |
| Lejweleputswa | 41 | Masilonyana 3, Matjhabeng 17, Nala 9, Tokologo 5, Tswelopele 7 |
| Thabo Mofutsanyana | 158 | Dihlabeng 15, Maluti-A-Phofung 27, Mantsopa 3, Nketoana 30, Phumelela 40, Setsoto 43 |
| Xhariep | 11 | Kopanong 7, Letsemeng 1, Mohokare 3 |
| Unaccounted gap | 7 | Likely Mangaung Metropolitan; monitor next JOC |
| **Provincial total** | **473** | — |

**MPO Week 28 — dairy cows vaccinated as at 1 May 2026:**

| Province | Dairy Cows Vaccinated | Notes |
|---|---|---|
| KZN | 360,159 | ALL dairy cows in KZN now received first round — milestone |
| EC | 168,142 | Up from MinMEC 23Apr (124,303); 100K doses delivered 1 May |
| FS | 15,104 | Confirms MinMEC figure |
| LP | 5,475 | Confirms MinMEC figure |
| GP | 14,832 | Confirms MinMEC figure |
| MP | 9,863 | Mass vacc postponed from 16 Apr to 11 May |
| NW | 6,342 | Confirms MinMEC figure |
| WC | 167,124 | Not exclusively dairy |
| NC | 0 | — |
| **National** | **579,917** | DISCREPANCY vs MinMEC 634,886 — methodology difference; both held |

MPO national: 169 dairy farms confirmed FMD, 122 active as at 1 May 2026.
EC: ~157,258 unvaccinated dairy animals remain; ~30,000 more doses needed.

### Data quality flags

1. **FS district gap**: District subtotals sum to 466; provincial total 473 → gap of 7 cases unassigned, likely Mangaung Metropolitan. Monitor at next FS JOC.
2. **MPO vs MinMEC dairy total**: MPO 579,917 vs MinMEC 634,886 (23 Apr). MinMEC data is slightly older date but larger — likely methodology difference (MPO dairy-only vs MinMEC broader category). Both held in master.
3. **FS private vet doses (199,899)**: Parsing uncertain from text extraction of xlsx — may represent DolVet private total or combined private figure. Flagged as indicative in notes.
4. **Dashboard snapshot unchanged**: No consolidated AgriSA weekly xlsx received for 8 May reporting period. Dashboard remains on 01 May 2026 data.

### Action items for next run

1. **Watch for 08 May 2026 consolidated AgriSA xlsx** — this will advance the dashboard snapshot date; expect from provincial JOCs via AgriSA Secretariat.
2. **4 WhatsApp images in FS STATISTICS 8 MAY 2026 folder** — JPEG format; need visual review to extract any quantitative data (likely JOC handout or summary sheet).
3. **MP mass vaccination 11 May** — MPO flagged rescheduled Ministerial event; watch for outcome report.
4. **EC pptx ARC/BVI discrepancy** — still outstanding; confirm with EC-DRDAR.
5. **FS 5-case gap at 24 Apr** (from session 5) and **7-case gap at 8 May** — confirm Mangaung Met figures at next FS JOC.
