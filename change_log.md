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

