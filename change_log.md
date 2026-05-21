# FMD Dashboard Change Log

A running record of what changed in the master and dashboard, with dates and source attribution.

---

## 2026-05-15 (session 10) — ICC weekly engagement + KZN DMA gazette (manual trigger)

**Master grew from 942 to 954 rows (+12 new rows).**

**Dashboard rebuilt:** Yes — FMD_Dashboard.html updated (76,339 bytes, validation passed). Snapshot date remains 01 May 2026 (no consolidated AgriSA weekly xlsx received). Also completed the pending session 9 rebuild.

### Sources processed

| File | Effective Date | Source Org | Outcome |
|---|---|---|---|
| `inbox/AgriSA Summary and Outcomes - FMD Weekly Engagement/AgriSA_Summary and Outcomes_FMD Weekly Engagement_2026.05.11.pdf` | 2026-05-11 | AgriSA-ICC | Ingested — 11 rows |
| `inbox/Ministerial Updates/2026.05.15 Reg No 7484 of 15 May 2026 - Rescinding FMD management Area in KZN.pdf` | 2026-05-15 | Ministry | Ingested — 1 row |
| `inbox/AgriSA Summary and Outcomes - FMD Weekly Engagement/AgriSA Weekly FMD Engagement_ 2026.05.20.pdf` | — | AgriSA-ICC | Parked — agenda only; no data |

### Key figures added

**AgriSA ICC Weekly Engagement — 11 May 2026:**

| Metric | Value | Notes |
|---|---|---|
| Doses expected in-country (total, week of 11 May) | ~5,500,000 | 2M Dollvet + 3.5M Biogenesis Bago |
| Doses expected — Biogenesis Bago | 3,500,000 | Expected during week of 11 May |
| Doses expected — Dollvet | 2,000,000 | Scheduled for arrival; confirmed 12 May |
| Doses allocated to feedlots (private/Section 10) | 150,000 | Plus allocations to stud breeders and SAPPO |
| LP vaccination coverage — commercial | 54% | As at 11 May 2026 |
| LP vaccination coverage — communal | 40% | As at 11 May 2026 |
| LP vaccination coverage — emerging | 6% | As at 11 May 2026 |
| KZN last JOC meeting date | 2026-03-25 | ~7-week gap to 11 May; formally escalated to MTT |
| Section 9 target finalisation date | ~2026-05-25 | ~2 weeks from 11 May; confirmed at meeting |
| National FMD dashboard | Implemented | Officially presented to ICC by Jason at 11 May meeting |

**Government Gazette No. 54686 — 15 May 2026:**

| Metric | Value | Notes |
|---|---|---|
| KZN FMD Management Area | RESCINDED | Government Notice 7484; signed Minister JH Steenhuisen |
| Legal instrument | Animal Diseases Act 35/1984, Section 9(1) | — |
| Gazette number | 54686, Vol. 731 | — |
| Repeal target | GN 5997 of 17 March 2025 | Original KZN DMA declaration |

**Significance:** First formal DMA rescission of the 2026 FMD outbreak. KZN DMA was publicly announced as lifted by the Minister on 5 May 2026 but was formally gazetted only today. Resolves the operational uncertainty that was escalated at the 11 May ICC meeting.

### Data quality flags

1. **Doses expected vs received (Dollvet 2M):** The 11 May meeting describes "2 million Dollvet doses scheduled for arrival" and the 12 May ministerial statement confirms arrival. Both are now in master (different effective dates, different source_org). The ICC row (effective 11 May, source AgriSA-ICC) represents the expectation; the ministerial row (effective 12 May, source Ministry) represents the confirmation. No conflict.
2. **LP coverage percentages (54%/40%/6%):** These are calculated coverage rates, not absolute animal counts. Stored under metric `vaccination_coverage_pct_*` to distinguish from animal counts. No denominator provided in source — percentages are as reported at the ICC meeting.
3. **KZN JOC gap:** Last meeting 25 March. The 11 May meeting notes KZN had "not held a JOC meeting since 25 March." This confirms the absence of any KZN provincial submission in master for the period 25 March–11 May.

### Action items for next run

1. **08 May or 15 May consolidated AgriSA weekly xlsx** — still priority; advances snapshot date.
2. **MPO Week 30 PDF** — expected this week; MP Hazyview mass vaccination outcomes + EC post-flood dairy recovery.
3. **3.5 million Biogenesis Bago arrival confirmation** — expected week of 11 May; watch inbox.
4. **Section 9 gazette** — target ~25 May; watch Ministerial Updates folder.
5. **20 May 2026 ICC weekly engagement summary** — agenda already in inbox; summary to follow.
6. **GitHub push** — push master_data.csv and FMD_Dashboard.html.

---

## 2026-05-15 (session 9) — LP PCM meeting pack backfill (automated daily run)

**Master grew from 891 to 942 rows (+51 new rows).**

**Dashboard rebuilt:** No — bash workspace unavailable during this session. Dashboard rebuild is pending. Snapshot date remains 01 May 2026.

**GitHub push:** Pending — bash unavailable.

### Inbox scan summary

| Folder | Files checked | New since last run? |
|---|---|---|
| Root (dated weekly folder) | None — no `15 May 2026/` or `08 May 2026/` folder | No |
| inbox/MPO/ | Folder last modified 2026-05-09 (pre-session 8) | No new files |
| inbox/Ministerial Updates/ | Folder last modified 2026-05-07 | No new files |
| inbox/ICC Reports/ | Folder last modified 2026-05-06 | No new files |
| inbox/Eastern Cape/ | Folder last modified 2026-05-04 | No new files |
| inbox/Free State/ | Folder last modified 2026-04-30 (FMD STATISTICS sub-folder 2026-05-09) | No new files |
| inbox/Western Cape/ | 3 new WhatsApp JPEG images from 11 May 2026 | Parked — JPEG format |
| inbox/Gauteng/ | Folder last modified 2026-05-04 | No new files |
| inbox/Limpopo/ | `FMD PCM MEETING PACK 20260507 REV1.pdf` + 2 draft packs — not previously read | **YES — ingested** |

**Additional discovery:** ingest.py log (2026-05-14) revealed LP PCM MEETING PACK 20260514 REV0.pdf and Presentation LIMPOPO FMD OUTBREAK CURRENT STATUS PRIORITY MEETING 2026-05-14 were also listed in the manual ingestion queue, but could not be found via SharePoint search (likely OneDrive stubs not yet synced).

### Sources processed

| File | Effective Date | Source Org | Outcome |
|---|---|---|---|
| `inbox/Limpopo/FMD PCM MEETING PACK 20260507 REV1.pdf` | 2026-04-15 (embedded 16 Apr slides) | LP-LDARD | Ingested — 30 rows for LP 15 April data |
| `inbox/Limpopo/FMD PCM MEETING PACK 20260507 REV1.pdf` | 2026-04-22 (embedded 23 Apr minutes) | LP-LDARD | Ingested — 21 rows for LP 22 April data |
| `inbox/Limpopo/DRAFT FMD PCM MEETING PACK 20260423 REV0.pdf` | — | LP-LDARD | Read — confirmed same 16 Apr slides and 9 Apr minutes; no additional unique data |
| `inbox/Limpopo/DRAFT FMD PCM MEETING PACK 20260416 REV0.pdf` | — | LP-LDARD | URI obtained; data already captured from 7 May pack |
| `inbox/Western Cape/WhatsApp Image 2026-05-11 at 08.49.42.jpeg` | 2026-05-11 | WC | Parked — JPEG; not readable via SharePoint |
| `inbox/Western Cape/WhatsApp Image 2026-05-11 at 08.49.59.jpeg` | 2026-05-11 | WC | Parked — JPEG; not readable via SharePoint |
| `inbox/Western Cape/WhatsApp Image 2026-05-11 at 08.50.15.jpeg` | 2026-05-11 | WC | Parked — JPEG; not readable via SharePoint |

### Key figures added

**LP as on 15 April 2026 (from 16 April PCM LDARD presentation slides):**

| Metric | Value | Notes |
|---|---|---|
| Animals vaccinated (total) | 143,658 | Commercial 66,095; Communal 67,305; Emerging 10,258 |
| Animals vaccinated — Capricorn | 25,254 | Comm 15,377; Comml 8,392; Emrg 1,485 |
| Animals vaccinated — Mopani | 22,460 | Comm 2,169; Comml 16,344; Emrg 3,947 |
| Animals vaccinated — Sekhukhune | 16,697 | Comm 15,683; Comml 1,014 |
| Animals vaccinated — Vhembe | 35,286 | Comm 10,369; Comml 24,352; Emrg 565 |
| Animals vaccinated — Waterberg | 43,961 | Comm 38,180; Comml 2,534; Emrg 3,247 |
| Positive cases (provincial) | 42 | — |
| Suspected cases | 57 | — |
| Pending cases | 212 | High volume reflecting lab pressure |
| ArtioPREVA received + used | 18,860 | **NEW vaccine type** — first appearance in LP data |
| Bioaftogen SAT 1&2 received/used | 100,020 / 87,895 | Balance 12,125 |
| Bioaftogen SAT 1-2-3 received | 99,960 | Arrived 15 April; not yet issued (balance 99,960) |
| Dollvet-oil received/used | 50,000 / 35,807 | Balance 14,193 |
| FMD AFTOVAXPUR received + used | 1,176 | **NEW vaccine type** — first appearance in LP data |
| Onderstepoort FMD received/used | 1,700 / 1,315 | Balance 385 |
| Provincial dose balance | 26,703 | Total across all vaccine types |

**LP as at 22 April 2026 (from 23 April PCM meeting minutes):**

| Metric | Value | Notes |
|---|---|---|
| Animals vaccinated (total) | 158,347 | Commercial 76,249; Communal 71,138; Emerging 10,960 |
| Animals vaccinated — Capricorn | 29,618 | Comm 19,348; Comml 8,513; Emrg 1,757 |
| Animals vaccinated — Mopani | 24,317 | Comm 2,808; Comml 17,334; Emrg 4,175 |
| Animals vaccinated — Sekhukhune | 17,648 | Comm 16,634; Comml 1,014 |
| Animals vaccinated — Vhembe | 37,232 | Comm 11,159; Comml 25,508; Emrg 565 |
| Animals vaccinated — Waterberg | 49,532 | Comm 42,934; Comml 3,149; Emrg 3,449 |
| Positive cases (provincial) | 50 | National shows 55; discrepancy due to closures pending sync |
| Suspected cases | 63 | Significant increase — active virus circulation |
| Pending cases | 220 | High volume |
| Total in provincial system | 397 | All statuses: pos/suspect/pending/neg/day0/closed |
| Bioaftogen SAT 1-2-3 issued | 86,400 | Balance 13,560 |
| Settlers pig outbreak | ~24,000 | FMD pig outbreak in Settlers area; risk to surrounding cattle |
| New confirmed areas | 3 | Lepelle-Nkumpi; Vivo; Dwaalboom/Thabazimbi (border NW) |

### Data quality flags

1. **Two new vaccine types identified for LP**: ArtioPREVA and FMD AFTOVAXPUR — not seen in any prior provincial returns. These may be earlier Botswana-derived or ARC-trial vaccines; source_org LP-LDARD. Dashboard vaccine chart may need to accommodate these.
2. **LP district vaccinated rows use metric `animals_vaccinated_district` without a district sub-field** — district name is in the notes field. If dashboard ever renders district-level LP maps, a dedicated district column or structured notes parse will be needed.
3. **LP 22 April national discrepancy**: Provincial system shows 50 positive; national DAFF system shows 55. Five cases closed at provincial level pending sync to national system. Flagged in notes.
4. **LP 15 April vs 17 April crosscheck**: Prior MinMEC submission used 128,937 vaccinated as the "17 April" LP figure (actually carried from 2 April JOC). The actual LP-LDARD figure for 15 April was 143,658 — a gap of 14,721. The MinMEC used a lagged JOC figure, consistent with known timing discrepancies.

### Action items for next run

1. **Dashboard rebuild** — run `build_dashboard.py` as soon as bash workspace is restored. (Pending from this session.)
2. **GitHub push** — push master_data.csv and FMD_Dashboard.html after dashboard rebuild. (Pending from this session.)
3. **15 May or 08 May consolidated AgriSA weekly xlsx** — priority. Advances snapshot date from 01 May.
4. **MPO Week 30 PDF** — expected this week; MP mass vaccination outcomes and EC post-flood dairy recovery.
5. **LP PCM MEETING PACK 20260514 REV0.pdf** — listed in ingest.py log; not found via SharePoint search. Likely OneDrive stub. Check next run.
6. **WC WhatsApp images from 11 May (3 files)** — require manual visual session.
7. **5 million Dollvet arrival confirmation** — announced 12 May; still pending.
8. **Ministerial X.png** — not accessible via SharePoint search; visual review needed.

---

## 2026-05-13 (session 8) — Ministerial media statement ingested (automated daily run)

**Master grew from 887 to 891 rows (+4 new rows).**

**Dashboard rebuilt:** Yes — FMD_Dashboard.html updated (76,034 bytes, validation passed). Snapshot date remains 01 May 2026 (no consolidated AgriSA weekly xlsx received).

### Sources processed

| File | Effective Date | Source Org | Outcome |
|---|---|---|---|
| `inbox/Ministerial Updates/Media statement-Minister Steenhuisen announces arrival of additional 2 million doses of FMD vaccine.pdf` | 2026-05-12 / 2026-05-11 | Ministry | Ingested — 4 rows: dose arrival, cumulative imported total, expected incoming, Hazyview vaccination event |
| `inbox/ICC Reports/AgriSA_ ICC Communication_ Section 10 Scheme for FMD Routine Vaccination.zip` | — | FMD-ICC | Parked — policy/governance document; no quantitative data to extract |
| `inbox/ICC Reports/AgriSA_ ICC Communication_ Section 10 Scheme for FMD Routine Vaccination.msg` | — | FMD-ICC | Parked — email wrapper for the above zip; no additional data |

### Key figures added

**National supply update — as at 12 May 2026 (Ministry):**

| Metric | Value | Notes |
|---|---|---|
| doses_received (Dollvet, 12 May batch) | 2,000,000 | Arrived from Turkey morning of 12 May 2026 |
| doses_received_cumulative_imported (all types, since Feb) | 8,000,000 | Cumulative imported total since late February 2026 |
| doses_expected_incoming (Dollvet) | 5,000,000 | Expected shortly; will bring imported total to 13 million |
| animals_vaccinated (MP, Hazyview, 11 May event) | 300 | Cross-border demonstration with Eswatini + Mozambique |

**Announced trajectory:** 13 million imported + 2 million BVI (2025) = 15 million doses total landed by end May 2026. Government target: vaccinate 80% of national herd (~14 million cattle) by December 2026.

### Data quality flags

None for this session. All four rows are new supply/event data without conflicting prior entries.

### Action items for next run

1. **15 May 2026 consolidated AgriSA weekly xlsx** — priority; will advance snapshot date from 01 May 2026.
2. **MPO Week 30 PDF** — expected mid-week; watch for MP mass vaccination outcomes and EC post-flood recovery figures.
3. **5 million Dollvet arrival confirmation** — announced "shortly" on 12 May; watch inbox/Ministerial Updates/.
4. **SADC Ministers meeting (Zimbabwe, later May)** — watch for communique with regional data.
5. **FS 7-case district gap** (8 May) — confirm Mangaung Metropolitan at next FS JOC.
6. **GitHub push** — push master_data.csv and FMD_Dashboard.html to repo.

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

---

## 2026-05-18 (session 12) — LP PCM pack ingest + build_dashboard.py syntax fix

**Master grew from 973 to 988 rows (+15 new rows).**

**Dashboard rebuilt:** Yes — FMD_Dashboard.html updated (78,675 bytes, validation passed). Snapshot date remains 01 May 2026 (no consolidated AgriSA weekly xlsx received).

**build_dashboard.py fix:** Line 529 had a truncated dictionary key (`urce_label":` → `"source_label":`) causing a SyntaxError. Fixed before rebuild.

### Sources processed

| File | Effective Date | Source Org | Outcome |
|---|---|---|---|
| `archive/2026-05-14/FMD PCM MEETING PACK 20260514 REV0.pdf` | 2026-05-06 | LP-LDARD | Ingested — 15 rows |
| `inbox/AgriSA Summary and Outcomes - FMD Weekly Engagement/AgriSA Weekly FMD Engagement_ 2026.05.20.pdf` | — | AgriSA-ICC | Parked — agenda only (meeting on 20 May; summary not yet available) |
| WC WhatsApp images 2026-05-11 (3 JPEGs) | — | — | Parked — JPEG files not readable via SharePoint connector |
| FS WhatsApp images 2026-05-08 (4 JPEGs) | — | — | Parked — JPEG files not readable |
| Consolidated AgriSA weekly xlsx | — | AgriSA-NAT | Not received — snapshot stays at 01 May 2026 |

### Key figures added

**LP LDARD presentation — 7 May PCM meeting (data as at 6 May 2026):**

| Metric | Value | Notes |
|---|---|---|
| Total animals vaccinated (LP) | 192,485 | Up from 128,937 (24 Apr AgriSA-NAT) |
| Commercial sector vaccinated | 103,095 | 54% of total |
| Communal sector vaccinated | 77,516 | 40% of total |
| Emerging farmer sector vaccinated | 11,874 | 6% of total |
| Waterberg district vaccinated | 63,488 | Largest district; commercial-dominant (55,562) |
| Capricorn district vaccinated | 40,228 | |
| Vhembe district vaccinated | 38,872 | Communal-dominant (26,337) |
| Mopani district vaccinated | 29,569 | Communal-dominant (19,315) |
| Sekhukhune district vaccinated | 20,328 | Commercial-dominant (19,314) |
| Positive cases (LP) | 61 | 49 active + 12 Day 0 |
| Suspected cases (LP) | 74 | 65 active + 9 Day 0 |
| Negative results (LP) | 51 | |
| Pending results (LP) | 237 | Waterberg 129 dominant |
| Total investigations (LP) | 428 | Transcript cites 431 (likely one-day update) |
| DolVet doses expected (LP) | 150,000 | "To be issued soon" — 7 May statement; not yet confirmed received |

### Data quality flags

- **LP Biogenesis receipt discrepancy:** LDARD transcript 99,020 vs AgriSA-NAT xlsx 100,020 — minor rounding, same April shipment; both values documented in notes
- **LP total_investigations discrepancy:** Slide shows 428; verbal transcript cites 431 — likely one-day refresh; 428 recorded, 431 noted in row notes
- **build_dashboard.py corruption:** Line 529 had truncated dictionary key from a previous edit. Fixed this session.

### Action items for next run

- Watch for 22 May consolidated AgriSA weekly xlsx (will advance snapshot from 01 May)
- Watch for 20 May ICC weekly engagement summary (meeting today; summary typically uploaded same day)
- Confirm LP DolVet 150,000 doses received (stated "soon" on 7 May)
- Watch for Section 9 gazette (~25 May target)
- Push master_data.csv and FMD_Dashboard.html to GitHub (PENDING from previous sessions)

---

## 2026-05-18 (session 13) — FS 15 May JOC + WC GIS 9 May ingest

**Master grew from 988 to 1006 rows (+18 new rows).**

**Dashboard rebuilt:** Yes — FMD_Dashboard.html updated (78,928 bytes, validation passed). Snapshot date remains 01 May 2026 (no consolidated AgriSA weekly xlsx received).

### Sources processed

| File | Effective Date | Source Org | Outcome |
|---|---|---|---|
| `inbox/Free State/FMD STATS.zip` → `FMD STATS/FS FMD Vaccine Data - 15.05.2026.xlsx` | 2026-05-15 | FS-JOC | Ingested — 11 rows (disease + vaccine receipts + vaccination breakdown) |
| `inbox/Free State/FMD STATS/WhatsApp Image 2026-05-15 at 18.14.06.jpeg` (FS DRDAR media release) | 2026-05-15 | FS-DRDAR | Ingested — 2 rows (positive_cases 589 authoritative, animals_vaccinated_total 513167) |
| `inbox/Western Cape/WhatsApp Image 2026-05-11 at 08.49.42.jpeg` (WC GIS portal screenshot) | 2026-05-09 | WC-GIS | Ingested — 4 rows (cases, total vaccinations, doses received, sites) |
| `inbox/Western Cape/WhatsApp Image 2026-05-11 at 08.49.59.jpeg` (WC GIS portal — district detail) | 2026-05-09 | WC-GIS | Ingested — 2 rows (primary vaccinations, booster vaccinations) |
| `inbox/MPO/Willem Report 1.jpeg` + `Willem Report 2.jpeg` | — | N/A | Parked — NOT FMD data. NW DEDECT media release about illegal warthog hunting in Kraaipan Village (15 May). Misfiled in MPO folder. |
| `inbox/Eastern Cape/Reporting of cases & vaccines - 07.05.2026.xlsx` (user re-upload) | 2026-05-07 | EC-DRDAR | Already in master from session 8 (ingested 2026-05-08). No new rows added. |
| `inbox/Western Cape/WhatsApp Image 2026-05-11 at 08.50.15.jpeg` | 2026-05-09 | WC-GIS | Reviewed — Cases per district map (CW 5, CCT 8, GR 10, WC 3) already captured in positive_cases row above. |

### Key figures added

**Free State — 15 May 2026 (FS-JOC + FS-DRDAR):**

| Metric | Value | Notes |
|---|---|---|
| Positive cases (confirmed outbreaks) | 589 | Up from 473 (8 May). +116 new. Media release authoritative; xlsx shows 588. |
| Suspected cases | 363 | Down from 467 (8 May) — reclassification to confirmed. |
| Vaccines received — Bioaftogen | 370,000 | Unchanged. Clarifies 8 May: "Bioaftogen total 466,100" was DolVet. |
| Vaccines received — DolVet | 466,100 | Unchanged. |
| Vaccines received — OBP/LNR | 2,300 | Unchanged. |
| Vaccines received — all total | 838,400 | Unchanged. |
| Animals vaccinated Dose 1 (all) | 399,397 | |
| Animals vaccinated Dose 2 (all) | 63,007 | |
| Bioaftogen Dose 1 | 199,899 | |
| Bioaftogen Dose 2 | 89,785 | |
| DolVet Dose 1 | 193,164 | |
| Total cattle vaccinated (all incl. pre-2026) | 513,167 | Per DRDAR media release. |

District positive cases (xlsx): Fezile Dabi 339 | Thabo Mofutsanyana 172 | Lejweleputswa 59 | Xhariep 11 | Mangaung Metro 7 = 588 total (1 less than media release 589 — timing).

**Western Cape — 9 May 2026 (WC-GIS portal, photographed 11 May):**

| Metric | Value | Notes |
|---|---|---|
| Confirmed cases | 26 | CW 5 (last 22 Mar), CCT 8 (last 26 Mar), GR 10 (last 28 Apr), WC 3 (last 05 Mar) |
| Total vaccinations | 195,363 | Primary 183,844 + Booster 11,519 |
| Primary vaccinations | 183,844 | District breakdown in notes |
| Booster vaccinations | 11,519 | District breakdown in notes |
| Vaccines received | 330,140 | WC-GIS portal figure; note AWC/RPO 449,370 methodology difference |
| Vaccination sites | 858 | 29 private vets vaccinating |

### Data quality flags

- **FS vaccine classification (8 May vs 15 May):** The 8 May entry records 466,100 as `Bioaftogen total`, but the 15 May template correctly identifies this as DolVet 466,100. The 8 May rows are not retroactively corrected (version management pending) but notes are flagged in the 15 May rows. Total received (838,400) is consistent across both dates.
- **FS positive cases discrepancy:** xlsx shows 588; FS-DRDAR media release shows 589. The 1-case difference likely reflects a case confirmed after xlsx preparation. Media release figure (589) used as authoritative in master.
- **WC GIS vs RPO discrepancy:** Portal shows 330,140 doses received; AWC/RPO figure was 449,370. Both held by source — methodology difference confirmed and previously documented.
- **Willem Reports misfiled:** Two JPEG files in the MPO inbox folder (Willem Report 1.jpeg, Willem Report 2.jpeg, modified 2026-05-18 06:29) are North West DEDECT media releases about illegal warthog hunting. Not FMD-related. No action taken other than logging.

### Action items for next run

- Watch for 22 May consolidated AgriSA weekly xlsx (advances snapshot from 01 May)
- Watch for 20 May 2026 ICC weekly engagement summary (meeting scheduled 20 May)
- Watch for Section 9 gazette (~25 May target)
- Watch for MPO Week 30 PDF
- Confirm LP DolVet 150,000 doses receipt
- Confirm Biogenesis Bago 3.5M arrival
- GitHub push still pending (git repo not accessible from sandbox)


---

## 2026-05-18 (session 14) — build_dashboard.py refactored; snapshot advances automatically

**Dashboard rebuilt:** Yes — 79,107 bytes, snapshot 2026-05-15, validation passed.

### Change: build_dashboard.py now synthesises from provincial JOC sources

The dashboard previously required the consolidated AgriSA weekly xlsx to advance the snapshot date and time series. This was a dependency that meant the dashboard lagged a week or more behind available data.

**Root cause of old behaviour:** `latest_dates()` only returned dates present in `AgriSA-NAT` or `ICC` source rows. `build_weekly()` and `national_view()` looked up `province="national"` ICC rows, which only existed for consolidated weeks.

**Changes made:**
- Added `PROGRAMME_SOURCES` constant — all trusted JOC/provincial orgs
- Added `_ANCHOR_METRICS` constant — key vaccine/disease metrics that qualify a date for the weekly axis
- Rewrote `latest_dates()` — now includes any date where any province has programme data for an anchor metric
- Added `_best_received()` — finds most recent total doses_received for a province regardless of vet_channel variation across source schemas
- Added `_best_vaccinated()` — finds most recent animals vaccinated using aggregate metric or dose1+dose2 fallback
- Rewrote `build_weekly()` — sums per-province carry-forward values for each weekly point instead of looking up national rows
- Rewrote `national_view()` — sums per-province carry-forward values instead of looking up province="national" ICC rows

**Result:** The dashboard snapshot now advances to the most recent date with ANY provincial JOC submission. Currently 2026-05-15 (FS 15 May media release). Weekly chart now has 10 data points vs 9 previously.

### National figures as at 15 May 2026

| Metric | Value | Notes |
|---|---|---|
| Doses received | 3,088,640 | FS 838,400 now correctly carries forward |
| Animals vaccinated | 2,479,427 | FS 513,167 + EC 469,955 + others carry-forward |
| Positive cases | 1,273 | FS 589 + EC 282 + GP/other carry-forward |
| Suspected cases | 689 | |
| Balance (unadministered) | 609,213 | |

### Per-province latest vaccinated figures
EC 469,955 | FS 513,167 | GP 149,783 | KZN 648,609 | LP 128,937 | MP 176,811 | NW 168,748 | NC 28,054 | WC 195,363

### No new weekly AgriSA xlsx received
When the consolidated weekly xlsx arrives (expected 22 May 2026), it will be ingested normally and the snapshot will advance further. The carry-forward mechanism means each new provincial submission updates the national picture immediately.

---

## 2026-05-18 (session 14b) — GP JOC + MPO Week 30 ingested

**Master grew from 1,006 to 1,025 rows (+19 rows).**

**Dashboard rebuilt:** Yes — 79,525 bytes, snapshot 2026-05-15, validation passed.

### Sources processed

| File | Effective Date | Type | Source Org |
|---|---|---|---|
| JOC FMD Outbreak Minutes - 08 May 2026.doc | 2026-05-08 | GP JOC meeting minutes | GP-GDARD |
| Week 30 - Update on the state of FMD and vaccine rollouts in the dairy industry.pdf | 2026-05-15 | MPO weekly dairy update | MPO |
| FMD PCM MEETING PACK 20260507 REV1.pdf | 2026-05-07 | LP PCM pack | LP-LDARD |

**LP PDF:** Agenda + 23 April procedural minutes only. No new LP vaccination or disease figures extractable. LP PCM data presentation was image-based in the pack.

### GP key figures (08 May 2026)

| Metric | Value | Notes |
|---|---|---|
| Confirmed outbreaks | 294 | 3 closed, 291 open |
| Suspect cases | 2 | Under investigation |
| Animals vaccinated (late Feb – 6 May) | ~244,800 | Biogenesis 115,677 + OBP 127,580 |
| Total doses allocated | ~520,000 | 124,800 still outstanding with OBP |
| Doses issued to private vets | 176,500 | 55 approved PVs; 142,000 doses usage outstanding |
| Controlled slaughter | 231,244 | Feedlot depopulation, up from 223,840 (29 Apr) |
| Animals affected (estimated) | 318,700 | |

New Lesedi District outbreak reported 7 May. Vaccination campaigns intensified along Gauteng/NW border. GP impact assessment report due 15 May 2026.

### MPO Week 30 dairy cows vaccinated (15 May 2026)

| Province | Dairy Cows Vaccinated |
|---|---|
| KZN | 360,200 |
| EC | 216,597 |
| WC | 140,746 |
| GP | 14,832 |
| MP | 9,863 |
| NW | 6,342 |
| FS | 15,104 |
| LP | 5,475 |
| NC | 0 |
| **National** | **769,159** |

Active dairy farms: 124 of 171 total. KZN: suspected case in vaccinated herd despite prior vaccination — booster expected. EC: +39,467 this week. Final ministerial vaccination rollout held in Hazyview (MP) on 11 May.

### Updated national figures (15 May snapshot)
- Animals vaccinated: 2,574,444 (GP now 244,800, up from 149,783)
- Doses received: 3,323,920
- Positive cases: 1,278

---

## 2026-05-19 (session 15) — Inbox scan, state reconciliation, dashboard rebuild

**Master unchanged: 1,027 rows** (confirmed via wc -l; 2 additional EC rows post-14b not previously logged).

**Dashboard rebuilt:** Yes — FMD_Dashboard.html 80,368 bytes (up from 79,525 in session 14b), snapshot 2026-05-15, validation passed.

### Inbox scan result

No new unprocessed files found. All available inbox data already ingested as of 18 May orphaned sessions (14 + 14b).

| Folder/File | Status |
|---|---|
| `inbox/Eastern Cape/` | Last modified 04 May — no new files |
| `inbox/Free State/` | Last modified 30 Apr — no new files |
| `inbox/Gauteng/` | Last modified 04 May — no new files |
| `inbox/Limpopo/` | Last modified 07 May — no new files |
| `inbox/Western Cape/` | Last modified 04 May — no new files |
| `inbox/MPO/Week 30 *.pdf` | Already ingested (session 14b, 18 May) |
| `inbox/ICC Reports/` | Last modified 16 Apr — no new files |
| `inbox/Ministerial Updates/` | Last modified 15 May — no new files |
| `inbox/AgriSA Summary and Outcomes/AgriSA Weekly FMD Engagement_ 2026.05.20.pdf` | Parked — agenda only (last modified 15 May, no outcomes data; meeting was 19/20 May) |
| `GCIS EDITORIAL BRIEF fmd.docx` (7 May) | Reviewed — contains 23 Apr 2026 figures only, all already in master from earlier ingests. No new rows added. |
| `54686 15-5 Agriculture (1).pdf` | Duplicate of Reg 7484 KZN DMA gazette already ingested in session 10. No new rows. |
| Dated folder `19 May 2026/` | Not found — no consolidated weekly xlsx received today |

### State file reconciliation

Session 14b (18 May, post-14) added 19 rows but only updated change_log; memory_update.md was not updated (still read "1,006 rows, snapshot 01 May"). Two further EC rows (EC 7 May v1/v2) were added after session 14b without any log entry. Today's session corrects all state files:
- memory_update.md updated: 1,027 rows, snapshot 15 May 2026
- change_log.md: this entry

### Dashboard validation output

```
Building dashboard from snapshot 2026-05-15; 10 weekly points.
Wrote FMD_Dashboard.html (80,368 bytes) — validation passed
```

Snapshot remains 2026-05-15 (15 May 2026). No consolidated AgriSA weekly xlsx received yet for 22 May.

### Key data quality notes carried forward

1. NC 25 March: vaccinated (23,000) > received (18,846) — pre-period stock draw, expected
2. EC 01 May: total_received formula-cache — dashboard uses 24 Apr fallback (superseded by EC 7 May JOC xlsx now in master: 469,955 received, 309,935 vaccinated)
3. WC discrepancy: AWC/RPO 449,370 vs GIS portal 330,140 received — methodology difference; both held in master
4. EC Alfred Nzo: xlsx labels 450 doses as BVI but pptx labels same as ARC — unresolved
5. GP animals_vaccinated conflict: JOC 8 May (244,800) vs AgriSA-NAT 1 May (149,783) vs GDARD infographic (184,036) — JOC likely includes feedlot mega-allocations
6. KZN suspected case in vaccinated herd (MPO Week 30) — booster programme pending

### Action items for next run

- Watch for: 22 May consolidated AgriSA weekly xlsx (highest priority)
- Watch for: 20 May ICC weekly engagement summary PDF (meeting held 19/20 May)
- Watch for: Section 9 gazette (~25 May 2026)
- Watch for: LP DolVet 150,000 receipt confirmation
- GitHub push pending (git not accessible from sandbox)

---

## 2026-05-20 (session 16) — LP 18 May district pivot table ingested

**Master grew from 1,027 to 1,036 rows (+9 rows).**

**Dashboard rebuilt:** Yes — 80,432 bytes, snapshot 2026-05-15 (unchanged), validation passed.

### Sources processed

| File | Effective Date | Type | Source Org | Outcome |
|---|---|---|---|---|
| `inbox/Limpopo/WhatsApp Image 2026-05-18 at 13.32.24.jpeg` | 2026-05-18 | LP LDARD pivot table (district × sector animals vaccinated) | LP-LDARD | Ingested — 9 rows (5 districts + 3 sectors + 1 grand total) |
| `inbox/Eastern Cape/Reporting of cases & vaccines - 07.05.2026.xlsx` (file mtime refreshed 19 May 12:07) | 2026-05-07 | EC district vaccine xlsx (re-upload) | EC-DRDAR | No new rows — content matches master from session 8 / 14b corrections |

### LP 18 May 2026 key figures (LDARD pivot table)

| District | Commercial | Communal | Emerging | Grand Total |
|---|---|---|---|---|
| Capricorn | 34,075 | 11,522 | 3,773 | 49,370 |
| Mopani | 8,103 | 22,539 | 5,006 | 35,648 |
| Sekhukhune | 543 | 27,616 | 1,322 | 29,481 |
| Vhembe | 17,622 | 31,613 | 1,979 | 51,214 |
| Waterberg | 104,721 | 4,374 | 4,751 | 113,846 |
| **National (LP)** | **165,064** | **97,664** | **16,831** | **279,559** |

LP cumulative animals vaccinated up from 192,485 on 6 May 2026 — an increase of 87,074 over 12 days. Waterberg remains the dominant district (commercial sector driving the rollout); Vhembe and Sekhukhune dominated by communal sector.

### Inbox scan result

| Folder/File | Status |
|---|---|
| `inbox/Eastern Cape/Reporting of cases & vaccines - 07.05.2026.xlsx` | Re-uploaded 19 May 12:07; content unchanged — no new rows |
| `inbox/Limpopo/WhatsApp Image 2026-05-18 at 13.32.24.jpeg` | Ingested (above) |
| `inbox/Free State/FMD STATS/` (4 jpeg images dated 15 May 18:14) | Already ingested in session 14b (FS DRDAR 589 outbreaks, 513,167 vaccinated) |
| Other inbox subfolders | No new files since session 15 (19 May) |
| Dated folder `20 May 2026/` or `22 May 2026/` | Not found — no consolidated weekly AgriSA xlsx received |
| 20 May ICC weekly summary PDF | Not yet in inbox — meeting was 19/20 May; summary to follow |

### Data quality notes

- The new LP rows use source_org=LP-LDARD which is intentionally NOT in `PROGRAMME_SOURCES` in `scripts/build_dashboard.py`. The dashboard snapshot date and national time-series therefore do not advance to 2026-05-18, and LP carry-forward in the national view still uses the AgriSA-NAT 1 May figure (128,937). The new data is held in master for province-level analysis. Decision: do not modify build_dashboard.py during routine ingest. Reconsider including LP-LDARD as a programme source once additional LP LDARD submissions establish consistent reporting.
- LP 18 May total 279,559 conflicts with AgriSA-NAT 1 May 128,937 (older) — the LDARD value is the more recent measurement; both rows held by source.

### Action items for next run

- Watch for: 22 May consolidated AgriSA weekly xlsx (highest priority — will advance snapshot)
- Watch for: 20 May ICC weekly engagement summary PDF
- Watch for: Section 9 gazette (~25 May 2026)
- Watch for: LP DolVet 150,000 receipt confirmation
- Watch for: KZN booster programme confirmation
- GitHub push pending (git not accessible from sandbox): master_data.csv + FMD_Dashboard.html

---

## 2026-05-20 (session 16b) — Second-pass ingest: EC 14 May + MP 17 May + WC 19 May + LP 18 May case data

**Master grew from 1,036 to 1,085 rows (+49 rows).**

**Dashboard rebuilt:** Yes — 81,127 bytes, snapshot ADVANCED from 2026-05-15 to 2026-05-19, 12 weekly points, validation passed.

### Sources processed

| File | Effective Date | Type | Source Org | Outcome |
|---|---|---|---|---|
| `inbox/Eastern Cape/Reporting of cases & vaccines - 14.05.2026.xlsx` | 2026-05-14 | EC district vaccine xlsx | EC-DRDAR | Ingested — 18 rows (provincial totals + 6 district vaccinated + disease + NM Bay) |
| `inbox/Mpumalanga/MP FMD outbreak 17052026 -.pptx` | 2026-05-17 | MP provincial JOC presentation | MP-DVS | Ingested — 16 rows (6 vaccine receipts + admin totals + disease + 3 districts + controlled slaughter) |
| `inbox/Western Cape/20 May/WhatsApp Image 2026-05-20 at 08.26.42 / 08.26.57 / 08.27.12.jpeg` | 2026-05-19 | WC GIS portal screenshots (3 panels) | WC-GIS | Ingested — 8 rows (cases + total/primary/booster vaccinations + doses received + sites + private/state mix) |
| `inbox/Limpopo/Monday 18 May/WhatsApp Image 2026-05-18 at 13.36.35.jpeg` | 2026-05-18 | LP case status table (LDARD pivot) | LP-LDARD | Ingested — 5 rows (positive/suspect/neg/pending/total investigations) |
| `inbox/Limpopo/Monday 18 May/WhatsApp Image 2026-05-18 at 13.32.37.jpeg` (sector pivot) | 2026-05-18 | LP sector breakdown (same as 13.32.24) | LP-LDARD | No new rows — duplicate of 16a sector data |
| `inbox/Limpopo/Monday 18 May/WhatsApp Image 2026-05-18 at 13.34.49.jpeg` (vaccine-type x district) | 2026-05-18 | LP detailed vaccine x municipality pivot | LP-LDARD | No new rows — totals match 16a district figures; municipality-vaccine granularity not yet modelled in master schema |
| `inbox/Limpopo/Monday 18 May/WhatsApp Image 2026-05-18 at 13.37.08.jpeg` (cumulative monthly) | 2026-05-18 | LP cumulative monthly Pos/Suspect trend | LP-LDARD | Captured in notes of LP 18 May total_investigations row (Dec25-May26 trend) |

### EC 14 May 2026 key figures

| Metric | Value | Δ vs 7 May |
|---|---|---|
| Confirmed outbreaks | 295 | +13 |
| Suspected | 221 | +1 |
| Total doses administered (dose-count) | 489,979 | +20,024 |
| Bioaftogen used (state + private) | 300,899 | +16,721 |
| DollVet used (state + private) | 185,653 | +3,303 |

District deltas: OR Tambo 23,389 → 46,086 (+22,697); Amathole 81,490 → 91,231 (+9,741); Joe Gqabi 18,368 → 31,343 (+12,975). Alfred Nzo and Chris Hani roughly flat.

WARNING: 489,979 is a sum-of-doses (double-counts animals receiving multiple types/doses). Unique animals likely lower per session 8/14b methodology (the EC corrected figure for 7 May was 309,935 unique vs 469,955 dose-count).

### MP 17 May 2026 key figures (first MP-DVS provincial submission)

| Metric | Value |
|---|---|
| Confirmed outbreaks | 231 |
| Suspected | 104 |
| Unique cattle vaccinated | 312,886 |
| Doses administered (sum) | 419,066 |
| Doses received (all) | 545,489 |
| Wastage | 2,707 |
| In hand | 123,716 |
| Controlled slaughter | 24,291 |

Vaccines received: Artio-Preva 109,489 / ARC 2,000 / Bioaftogen Bivalent dose 1: 100,020 / Aftodoll dose 1: 95,000 / Bioaftogen Trivalent dose 2: 94,980 / Aftodoll dose 2: 144,000.

District vaccinated: Ehlanzeni 96,387 (24 outbreaks) / Gert Sibande 132,600 (137) / Nkangala 83,879 (70). Gert Sibande dominant for both outbreaks and vaccination volume.

### WC GIS 19 May 2026 key figures

| Metric | Value | Δ vs 9 May |
|---|---|---|
| Total vaccinations | 231,913 | +36,550 |
| Primary vaccinations | 219,790 | +35,946 |
| Booster vaccinations | 12,123 | +604 |
| Cases (cumulative) | 26 | 0 |
| Vaccination sites | 954 | +96 |
| Doses received | 330,140 | 0 |
| Private vet share | 160,719 (69%) | up |

Per-district vaccinations: Cape Winelands 29,594 / Central Karoo 12 / City of Cape Town 35,143 / Garden Route 76,318 / Overberg 24,224 / West Coast 66,622.

Garden Route still the most-recent-active district (22 days since last case); Cape Winelands 59, City of Cape Town 55, West Coast 76.

### LP 18 May 2026 case status table

| Status | LP Total | Δ vs 6 May |
|---|---|---|
| Positive | 68 | +7 |
| Suspect | 77 | +3 |
| Neg/Closed | 56 | +5 |
| Pending | 254 | +17 |
| Total investigations | 460 | +32 |

By district (positive/suspect): Capricorn 19/10 / Mopani 2/2 / Sekhukhune 8/12 / Vhembe 14/28 / Waterberg 25/25. Waterberg pending 127 (still dominant); Capricorn 33; Mopani 65 (high pending count growing).

Cumulative monthly trend (positive / suspect): Dec25 8/7 → Jan26 20/21 → Feb 38/33 → Mar 46/47 → Apr 64/70 → May 68/77.

### Dashboard snapshot advance

Snapshot moved from 15 May 2026 → 19 May 2026 driven by WC-GIS 19 May data (PROGRAMME_SOURCE with positive_cases and animals_vaccinated_total anchor metrics). EC-DRDAR 14 May added a new weekly point. Time series now 12 points (up from 10).

### Data quality notes

- MP-DVS is a new source_org not yet listed in `PROGRAMME_SOURCES` in build_dashboard.py. The MP 17 May data is in master but does not drive the time-series anchor for MP; MP carry-forward in national_view still falls back to AgriSA-NAT 1 May. Decision: leave build script unchanged for this routine ingest; flag for consideration in next dashboard refactor.
- LP-LDARD same exclusion remains — LP 18 May case figures held in master but not driving the carry-forward.
- EC 489,979 dose-count: matches xlsx total cell; flag in row notes that unique-animals figure not directly available from this xlsx (session 8/14b correction methodology should be reapplied when ICC issues a corrected figure).
- MP Ehlanzeni: district summary shows 12 suspects but municipality detail sums to 2 — flagged in notes; provincial total of 104 used.
- WC GIS booster column has no Central Karoo or Overberg values (zero implicit).

### Action items for next run

- Watch for: 22 May consolidated AgriSA weekly xlsx (highest priority)
- Watch for: 20 May ICC weekly engagement summary PDF
- Watch for: Section 9 gazette (~25 May 2026)
- Watch for: LP DolVet 150,000 receipt confirmation
- Watch for: KZN booster programme confirmation
- Watch for: MP follow-up provincial JOC submission
- Consider: adding MP-DVS and LP-LDARD to PROGRAMME_SOURCES in build_dashboard.py once additional submissions confirm consistent reporting (architectural decision; out of scope for routine ingest)
- GitHub push pending (git not accessible from sandbox): master_data.csv + FMD_Dashboard.html

---

## 2026-05-21 (session 17) — NW + LP 20 May + RMIS + EC 14 May receipts; PROGRAMME_SOURCES extended

**Master grew from 1,085 to 1,126 rows (+41 rows).**

**Dashboard rebuilt:** Yes — 82,367 bytes, snapshot ADVANCED from 2026-05-19 to 2026-05-20, **18 weekly points** (was 12), validation passed.

### Code change
`scripts/build_dashboard.py` — PROGRAMME_SOURCES extended to include **LP-LDARD** and **MP-DVS** (provincial state JOC equivalents to EC-DRDAR/GP-GDARD). NW-RPO remains excluded (commodity body, parallel to MPO/AWC-RPO).

### Sources processed

| File | Effective Date | Type | Source Org | Outcome |
|---|---|---|---|---|
| `inbox/North West/19 MAY 2026- RPO JIC FMD UPDATE.pdf` | 2026-05-19 | NW RPO JIC update | NW-RPO | Ingested — 19 rows |
| `inbox/Limpopo/FMD PCM 21 MAY 2026.zip` → `FMD PCM SAKELYS 20260521 REV0.pdf` | 2026-05-20 | LP LDARD priority committee pack | LP-LDARD | Ingested — 13 rows |
| `inbox/Limpopo/FMD PCM 21 MAY 2026.zip` → `FMD PCM MEETING PACK 20260514 REV0.pdf` | — | Duplicate of session 14b ingest | LP-LDARD | No new rows |
| `inbox/RMIS/06.05.2026_Final_Vaccine Orders Export (2026-05-06)_Feedlots.xlsx` | 2026-05-06 | RMIS feedlot vaccine orders | RMIS | Ingested — 8 rows (province aggregates) |
| `inbox/Eastern Cape/Reporting of cases & vaccines - 14.05.2026.xlsx` (post-session-16b doses_received row) | 2026-05-14 | EC 14 May doses_received proxy | EC-DRDAR | Ingested — 1 row |

### NW 19 May 2026 key figures (RPO JIC)

| Metric | Value |
|---|---|
| New cases week 11-15 May | 19 (Mahikeng 3, Kagisano 9, Lekwa-Taemane 1, Naledi 4, Ditsobotla 1, Greater Taung 1) |
| Total doses allocated | 176,000 |
| Total doses used | 171,561 (98%) |
| Balance | 4,439 |
| New consignment incoming | 267,700 |

Vaccine usage: Bioaftogen 99,678/100,000 (99.7%); Aftodoll 47,712/50,000 (95.4%); Aftodoll Emergency RM 24,171/26,000 (93.0%). District distribution (Bioaftogen 13 Apr + Aftodoll 30 Apr): DRSM 59,112 used / NMM 31,795 / Bojanala 25,705 / DKK 24,293. Feedlot Aftodoll usage 17,237 (Mushlendaw 10,891 dominant).

### LP 20 May 2026 key figures (LDARD priority committee SAKELYS pack)

| District | Commercial | Communal | Emerging | Grand Total | Δ vs 18 May |
|---|---|---|---|---|---|
| Capricorn | 34,951 | 12,381 | 3,773 | 51,105 | +1,735 |
| Mopani | 9,935 | 25,069 | 5,006 | 40,010 | +4,362 |
| Sekhukhune | 1,466 | 30,319 | 1,606 | 33,391 | +3,910 |
| Vhembe | 19,512 | 34,076 | 2,216 | 55,804 | +4,590 |
| Waterberg | 109,051 | 5,041 | 6,242 | 120,334 | +6,488 |
| **National (LP)** | **174,915** | **106,886** | **18,843** | **300,644** | **+21,085** |

Week 25 (19-25 May) disease summary: Positive 68 (unchanged from W24); Suspect 82 (+5); Day-0 27 (+4); Negative 52 (+1).

### RMIS 06 May 2026 feedlot vaccine orders

40 orders totalling 3,000 doses of Dollvet Biotech Trivalent across 8 provinces between 30 Apr and 6 May (OBP-supplied). Per province: GP 1,059 / FS 870 / MP 519 / NW 278 / LP 171 / KZN 64 / EC 20 / NC 19.

### EC 14 May 2026 doses_received row added

Set to 489,979 — equal to administered total — per the EC xlsx convention where "TOTAL Vaccines Received" matches "TOTAL Vaccines Administered" (the cell was left blank for 14 May; we mirrored the 7 May treatment). The dashboard's `doses_received` carry-forward for EC now reflects 14 May rather than 7 May.

### Dashboard impact — national totals

| Metric | Before (session 16b, snapshot 19 May) | After (session 17, snapshot 20 May) | Δ |
|---|---|---|---|
| Doses received | 3,253,995 | 3,622,508 | +368,513 |
| Animals vaccinated | 2,631,018 | 2,938,800 | +307,782 |

Per-province now-using values:
- EC: 489,979 received & vaccinated (was 469,955 / 489,979)
- LP: 300,644 vaccinated (was 128,937 AgriSA-NAT 1 May)
- MP: 312,886 vaccinated (was 176,811 AgriSA-NAT 24 Apr); 545,489 received (was 197,000 AgriSA-NAT 1 May)
- WC, FS, GP unchanged

### Data quality notes

- NW-RPO is intentionally NOT a PROGRAMME_SOURCE. NW headline figures still rely on AgriSA-NAT (177,400 received / 168,748 vaccinated 24 Apr) which is now significantly outdated vs the NW-RPO 19 May figures (176,000 / 171,561). If NW JIC moves to a DARD-led JOC source in future, the source filter should be revisited.
- LP 20 May Mopani row total sums to 73 in the PDF but the table header says 72 — minor off-by-one; we report 72 per the PDF total cell.
- Waterberg row had a PDF parse glitch (7 numbers vs 8 expected) — captured via the per-district aggregate animals_vaccinated_district figures rather than the raw status counts.
- EC 14 May 489,979 is a sum-of-doses (double-counts dose1+dose2 per session 8/14b correction methodology). Unique-animals figure pending an EC-DRDAR cumulative update.

### GitHub push

| Action | Status |
|---|---|
| Commit + push session 17 to AgriSA1904/FMD-Dashboard `main` | PENDING — to be pushed in this session |

### Action items for next run

- Watch for: 22 May (or later) consolidated AgriSA weekly xlsx
- Watch for: 20 May ICC weekly engagement summary PDF
- Watch for: Section 9 gazette (~25 May 2026)
- Watch for: NW new consignment 267,700 confirmation
- Watch for: KZN booster programme confirmation
- Consider: adding NW-RPO to PROGRAMME_SOURCES only if NW moves to a state-DARD-led JOC channel (currently RPO is a commodity body — kept consistent with MPO/AWC-RPO exclusion)
