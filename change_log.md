# FMD Dashboard — Change Log

---

## 2026-05-08 — Ingest: EC DARD weekly report (07 May 2026)

**Source file:** `inbox/Eastern Cape/Reporting of cases & vaccines - 07.05.2026.xlsx`
**Source org:** EC-DARD (Eastern Cape Department of Agriculture, Land Reform & Rural Development)
**Effective date:** 2026-05-07
**Rows appended:** 12
**master_data.csv total rows:** 788

### New data

| Metric | Value | Notes |
|---|---|---|
| EC positive cases | **282** | Up from 166 on 01 May. Districts: SB=4, AN=46, AM=137, CH=38, JG=43, OT=13 + NMB Metro |
| EC suspected cases | **220** | Down from 258 on 01 May (suspected converting to confirmed) |
| EC negative cases | **14** | Unchanged from 01 May |
| EC animals vaccinated (total) | **469,955** | Up from 332,182 on 01 May (+137,773 in ~6 days) |
| EC commercial vaccinated | **284,178** | |
| EC communal vaccinated | **182,350** | |
| EC doses received — BVI | **1,250** | |
| EC doses received — OBP/ARC | **2,600** | |
| EC doses received — Bioaftogen | **150,000** | Unchanged from prior submission |
| EC doses received — DollVet | **150,000** | EC-DARD shows 150,000; RPO 28-Apr showed 152,000 — both held in master by source_org |

### Data quality notes

- **BVI allocation correction:** 01-May AgriSA-NAT submission showed BVI received = 2,600 (likely a formula-cache error where BVI and OBP/ARC allocations were swapped). 07-May EC-DARD file shows BVI allocation = 1,250 and OBP/ARC = 2,600. EC-DARD figure taken as authoritative for 07 May.
- **Vaccinated > received flag:** Dashboard quality flag raised (EC animals vaccinated 469,955 vs doses received 304,600). This is a known pre-existing issue — cumulative vaccination draws on pre-rollout stock and the received figure does not include historical stock. Not a new anomaly.
- **DollVet discrepancy:** EC-DARD 150,000 vs RPO 152,000. Both rows retained in master_data.csv under respective source_org values.

### Build changes

- `build_dashboard.py` updated: `EC-DARD` added to `prefer_org` lists (consistent with existing `GDARD` precedent for Gauteng). EC provincial government submissions now take priority alongside AgriSA-NAT, ICC, WC-GIS, and GDARD for all province-level metrics.


---

## 2026-05-08 — Correction + FS ingest (08 May 2026)

### EC correction
Added missing `doses_received / all / all` row for 2026-05-07 (EC-DARD). The first ingest
captured per-vaccine-type receipts but omitted the provincial total column. Dashboard now shows:

| Metric | Before | After |
|---|---|---|
| EC doses received | 304,600 (24-Apr) | **469,995** (07-May) |
| EC animals vaccinated | 469,955 ✓ | 469,955 ✓ (unchanged) |
| EC positive cases | 282 ✓ | 282 ✓ (unchanged) |

Note: text extraction from xlsx showed 469,955; user confirmed authoritative figure is 469,995.

### FS ingest — `FS FMD Vaccine Data - 8.05.2026.xlsx`
**Source:** `inbox/Free State/FMD STATISTICS 8 MAY 2026/FS FMD Vaccine Data - 8.05.2026.xlsx`
**Source org:** FS-DARD | **Effective date:** 2026-05-08 | **Rows appended:** 10

| Metric | Value | vs 01-May |
|---|---|---|
| FS positive cases | **473** | +17 (was 456) |
| FS suspected cases | **467** | — |
| FS doses received (total) | **838,400** | +441,060 — large new allocation |
| FS Bioaftogen received | **370,000** | up from 195,000 (01-May AgriSA-NAT) |
| FS DollVet received | **466,100** | up from 200,040 (01-May AgriSA-NAT) |
| FS OBP/ARC received | **2,300** | unchanged |
| FS animals vaccinated (Dose 1) | **399,397** | — |
| FS Bioaftogen Dose 1 | **199,899** | — |
| FS Dose 2 (booster) | **63,007** | — |

**Data quality note:** Large jump in FS doses received (397,340 → 838,400) reflects a significant
new DollVet allocation delivered during the week. Prior AgriSA-NAT figures (01-May) appeared to
have Bioaftogen/DollVet quantities swapped — FS-DARD submission is authoritative.

**FS positive cases by district:** Fezile Dabi=256, Thabo Mofutsanyana=158, Lejweleputswa=41,
Xhariep=11, Mangaung Metro=7 — Fezile Dabi remains the most affected district.

### Build script update
`FS-DARD` added to `prefer_org` lists in `build_dashboard.py`.

**master_data.csv total rows: 799**
