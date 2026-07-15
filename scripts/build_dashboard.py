"""
Rebuild FMD_Dashboard.html from master_data.csv.

Reads the master CSV, applies "latest non-superseded version wins" per
(effective_date, province, metric, vaccine_type, vet_channel) tuple,
collapses to dashboard-ready data shapes, and re-injects them into
the HTML template's <script> block.

Run after every ingest:
    python3 scripts/build_dashboard.py
"""
import csv
import json
import os
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "master_data.csv")
DASHBOARD = os.path.join(ROOT, "FMD_Dashboard.html")
TEMPLATE = os.path.join(ROOT, "scripts", "dashboard_template.html")

PROVINCES = [
    ("EC", "Eastern Cape"),
    ("FS", "Free State"),
    ("GP", "Gauteng"),
    ("KZN", "KwaZulu-Natal"),
    ("LP", "Limpopo"),
    ("MP", "Mpumalanga"),
    ("NW", "North West"),
    ("NC", "Northern Cape"),
    ("WC", "Western Cape"),
]

# Sources that represent actual vaccination programme data (national or provincial JOC).
# RPO, MPO and administrative/metadata rows are excluded from driving the weekly axis.
PROGRAMME_SOURCES = frozenset({
    "AgriSA-NAT", "Ministry", "FMD-ICC", "Ministry",
    "FS-JOC", "FS-DRDAR", "FS-DARDLEA", "FS-DARDEA", "FS-Landbou",
    "EC-DRDAR", "GP-GDARD", "WC-GIS",
    "LP-LDARD", "MP-DVS", "MP-AgriMP", "AgriMP", "NW-RPO",
    "NC-DALRRD",
})

# Metrics that indicate real vaccination or disease data (not policy or metadata)
_ANCHOR_METRICS = frozenset({
    "doses_received", "animals_vaccinated", "animals_vaccinated_total",
    "animals_vaccinated_dose1", "positive_cases",
})

# The FMD Industry Coordination Council is a task team established by the Minister
# of Agriculture, so ICC updates and Ministerial updates are the same data stream.
# We normalise all ICC-family source codes onto a single canonical source so they
# are treated as one source everywhere in the build (weekly axis, source preference,
# provenance lists and the dashboard tab).
MINISTRY_ICC_ALIASES = frozenset({"ICC", "FMD-ICC", "AgriSA-ICC", "Ministerial", "DAFF"})
MINISTRY_ICC_CANON = "Ministry"          # internal canonical source_org
MINISTRY_ICC_LABEL = "Ministerial and ICC"   # display label for provenance lists

def load_master():
    if not os.path.exists(MASTER):
        return []
    with open(MASTER, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    # Unify the Ministerial/ICC family onto a single canonical source code.
    for r in rows:
        if r.get("source_org") in MINISTRY_ICC_ALIASES:
            r["source_org"] = MINISTRY_ICC_CANON
    return rows

def num(v):
    try: return float(v)
    except (TypeError, ValueError): return None

def latest_value(rows, *, effective_date, province, metric,
                 vaccine_type="", vet_channel="", skip_zero=True):
    """Return the best value for an exact (effective_date, province, metric) lookup.
    skip_zero=True: if the stored value is 0, treat it as unreported and fall back
    to the most recent earlier non-zero value so the time series never drops to zero
    mid-rollout due to a blank cell in a source spreadsheet."""
    matches = [r for r in rows if (
        r["effective_date"] == effective_date and
        r["province"] == province and
        r["metric"] == metric and
        r["vaccine_type"] == vaccine_type and
        r["vet_channel"] == vet_channel and
        r["superseded_by"] == ""
    )]
    if not matches:
        return None
    matches.sort(key=lambda r: int(r["version"]), reverse=True)
    val = num(matches[0]["value"])
    if skip_zero and (val is None or val == 0):
        # Carry forward: find the most recent non-zero value across all dates
        fallback = [r for r in rows if (
            r["effective_date"] < effective_date and
            r["province"] == province and
            r["metric"] == metric and
            r["vaccine_type"] == vaccine_type and
            r["vet_channel"] == vet_channel and
            r["superseded_by"] == "" and
            (num(r["value"]) or 0) != 0
        )]
        if fallback:
            fallback.sort(key=lambda r: (r["effective_date"], int(r["version"])), reverse=True)
            return num(fallback[0]["value"])
    return val

def latest_dates(rows):
    """All weekly snapshot dates for the time series.
    A date qualifies if at least one province has programme-level data
    (JOC, AgriSA-NAT, or equivalent) for a key vaccine or disease metric.
    RPO and MPO commodity rows do not drive the weekly axis.
    Provincial district-level breakdown rows (positive_cases_district etc.) are
    also excluded — only province-level anchor metrics count."""
    return sorted(set(
        r["effective_date"] for r in rows
        if r["source_org"] in PROGRAMME_SOURCES
        and r["metric"] in _ANCHOR_METRICS
        and r["province"] not in ("", "national")
        and r["superseded_by"] == ""
    ))

def latest_province_date(rows, code):
    """Most recent effective_date with any non-superseded data for this province."""
    dates = sorted(set(r["effective_date"] for r in rows
                       if r["province"] == code and r["superseded_by"] == ""))
    return dates[-1] if dates else None

def _best_received(rows_as_of, province):
    """Latest total doses received for a province.
    Collects ALL rows with metric=doses_received and vaccine_type=all (regardless of
    vet_channel) and returns the most recent non-zero value.  This avoids an early-exit
    bug where the older AgriSA-NAT all/all row would be returned before checking the
    more recent FS-JOC all/state row."""
    candidates = [r for r in rows_as_of
                  if r["province"] == province
                  and r["metric"] == "doses_received"
                  and r["vaccine_type"] == "all"
                  and r["superseded_by"] == ""
                  and (num(r["value"]) or 0) > 0]
    if not candidates:
        return 0
    candidates.sort(key=lambda r: (r["effective_date"], int(r["version"])), reverse=True)
    return num(candidates[0]["value"]) or 0

def _best_vaccinated(rows_as_of, province):
    """Latest total animals vaccinated for a province.
    Collects ALL aggregate rows (animals_vaccinated or animals_vaccinated_total,
    vaccine_type all/empty, any vet_channel) and returns the most recent non-zero
    value.  Falls back to dose1+dose2 sum if no aggregate row exists."""
    candidates = [r for r in rows_as_of
                  if r["province"] == province
                  and r["metric"] in ("animals_vaccinated", "animals_vaccinated_total")
                  and r["vaccine_type"] in ("all", "")
                  and r["superseded_by"] == ""
                  and (num(r["value"]) or 0) > 0]
    if candidates:
        candidates.sort(key=lambda r: (r["effective_date"], int(r["version"])), reverse=True)
        return num(candidates[0]["value"]) or 0
    # Fallback: dose1 + dose2
    d1c = [r for r in rows_as_of if r["province"] == province
           and r["metric"] == "animals_vaccinated_dose1"
           and r["vaccine_type"] in ("all", "") and r["superseded_by"] == ""
           and (num(r["value"]) or 0) > 0]
    d2c = [r for r in rows_as_of if r["province"] == province
           and r["metric"] == "animals_vaccinated_dose2"
           and r["vaccine_type"] in ("all", "") and r["superseded_by"] == ""
           and (num(r["value"]) or 0) > 0]
    d1 = num(max(d1c, key=lambda r: r["effective_date"])["value"]) if d1c else 0
    d2 = num(max(d2c, key=lambda r: r["effective_date"])["value"]) if d2c else 0
    return (d1 + d2) if (d1 or d2) else 0

def latest_metric(rows, *, province, metric, vaccine_type="", vet_channel="",
                  prefer_org=None, skip_zero=True):
    """Find the most recent non-superseded value for this (province, metric, ...) tuple.
    If prefer_org is set, rows from that source are STRICTLY preferred — we only fall
    back to other organisations when the preferred source has no value at all.
    skip_zero=True (default): treat 0 as 'not reported' and carry forward the most
    recent non-zero value. This prevents blank/unfilled cells in source spreadsheets
    (ingested as 0) from wiping out the last known figure on the dashboard.

    Fallback: if vaccine_type="" is requested and no matches are found, the lookup
    is retried with vaccine_type="all" (and vet_channel="all" if vet_channel="" was
    requested). This handles rows ingested with explicit "all" markers for metrics
    such as positive_cases where vaccine_type is semantically irrelevant."""
    # When no specific vaccine_type is requested, merge rows with vaccine_type in
    # ("", "all") so that newer rows ingested with explicit "all" markers are not
    # hidden behind older rows ingested with empty strings.
    if vaccine_type == "" and vet_channel == "":
        matches = [r for r in rows if (
            r["province"] == province and
            r["metric"] == metric and
            r["vaccine_type"] in ("", "all") and
            r["vet_channel"] in ("", "all", "total") and
            r["superseded_by"] == ""
        )]
    elif vaccine_type == "":
        matches = [r for r in rows if (
            r["province"] == province and
            r["metric"] == metric and
            r["vaccine_type"] in ("", "all") and
            r["vet_channel"] == vet_channel and
            r["superseded_by"] == ""
        )]
    else:
        matches = [r for r in rows if (
            r["province"] == province and
            r["metric"] == metric and
            r["vaccine_type"] == vaccine_type and
            r["vet_channel"] == vet_channel and
            r["superseded_by"] == ""
        )]
    if not matches:
        return None

    def pick_best(candidates):
        candidates.sort(key=lambda r: (r["effective_date"], int(r["version"])), reverse=True)
        if skip_zero:
            # Prefer the most recent non-zero value; only fall back to zero if
            # that is truly all we have (i.e. every historical row is also zero).
            non_zero = [r for r in candidates if (num(r["value"]) or 0) != 0]
            if non_zero:
                return num(non_zero[0]["value"])
        return num(candidates[0]["value"])

    if prefer_org:
        prefs = [prefer_org] if isinstance(prefer_org, str) else list(prefer_org)
        preferred = [r for r in matches if r["source_org"] in prefs]
        if preferred:
            return pick_best(preferred)
    return pick_best(matches)

def build_provinces(rows, snapshot_date):
    # Filter to programme sources only — same as national_view — so RPO/MPO
    # commodity submissions don't overwrite JOC figures in the province table.
    prog = [r for r in rows
            if r["source_org"] in PROGRAMME_SOURCES and r["superseded_by"] == ""]
    out = []
    for code, name in PROVINCES:
        ed = latest_province_date(prog, code) or snapshot_date
        out.append({
            "code": code, "name": name,
            "as_of": ed,
            # herd_cattle is static reference data — AgriSA-NAT is canonical
            "herd": int(latest_metric(prog, province=code, metric="herd_cattle",
                                      prefer_org=["AgriSA-NAT", "Ministry"]) or 0),
            # Disease counts: most recent from any programme source (no prefer_org)
            # so JOC submissions (GP-GDARD, EC-DRDAR, etc.) beat a stale AgriSA-NAT value.
            "positive":  int(latest_metric(prog, province=code, metric="positive_cases") or 0),
            "suspected": int(latest_metric(prog, province=code, metric="suspected_cases") or 0),
            "negative":  int(latest_metric(prog, province=code, metric="negative_cases",
                                           skip_zero=False) or 0),
            "pending":   int(latest_metric(prog, province=code, metric="pending_cases",
                                           skip_zero=False) or 0),
            # Vaccine figures: use the _best_* helpers (consistent with national_view)
            "received":  int(_best_received(prog, code)),
            "vaccinated": int(_best_vaccinated(prog, code)),
        })
    return out

def build_weekly(rows):
    """Build the weekly time series by summing per-province carry-forward values.

    For each snapshot date, we take only rows up to that date and pick the most
    recent value per province per metric (carry-forward). This means a weekly point
    for 15 May will show FS's 15 May figures alongside 01 May carry-forwards for
    provinces that have not yet submitted — giving the best available national picture
    rather than waiting for the consolidated AgriSA xlsx to arrive.
    """
    out = []
    prog_rows = [r for r in rows
                 if r["source_org"] in PROGRAMME_SOURCES and r["superseded_by"] == ""]
    for ed in latest_dates(rows):
        rows_as_of = [r for r in prog_rows if r["effective_date"] <= ed]

        total_recv = sum(_best_received(rows_as_of, code)    for code, _ in PROVINCES)
        total_adm  = sum(_best_vaccinated(rows_as_of, code)  for code, _ in PROVINCES)
        total_pos  = sum(
            latest_metric(rows_as_of, province=code, metric="positive_cases") or 0
            for code, _ in PROVINCES
        )
        total_sus  = sum(
            latest_metric(rows_as_of, province=code, metric="suspected_cases") or 0
            for code, _ in PROVINCES
        )
        out.append({
            "date":         ed,
            "received":     int(total_recv) if total_recv else None,
            "administered": int(total_adm)  if total_adm  else None,
            "positive":     int(total_pos),
            "suspected":    int(total_sus),
            "pending":      None,
        })
    return out

def build_source_mix(rows, snapshot_date):
    """Per-manufacturer source mix, using AgriSA as canonical."""
    out = {}
    for vt in ["bioaftogen", "dolvet", "obp_arc", "bvi"]:
        total = 0
        for code, _ in PROVINCES:
            # Restrict to AgriSA rows so we don't double-count RPO submissions
            agrisa_rows = [r for r in rows if (
                r["province"] == code and
                r["metric"] == "doses_received" and r["vaccine_type"] == vt and
                r["vet_channel"] == "total" and r["superseded_by"] == "" and
                r["source_org"] == "AgriSA-NAT"
            )]
            if agrisa_rows:
                agrisa_rows.sort(key=lambda r: (r["effective_date"], int(r["version"])), reverse=True)
                v = num(agrisa_rows[0]["value"])
                if v: total += v
        out[vt] = int(total)
    nat_total = latest_metric(rows, province="national", metric="doses_received",
                              vaccine_type="all", vet_channel="all",
                              prefer_org=["AgriSA-NAT", "Ministry", "WC-GIS"]) or 0
    sum_mfg = sum(out.values())
    out["unallocated"] = max(0, int(nat_total) - sum_mfg)
    return out

def build_mpo(rows):
    """MPO dairy tracking: weekly dairy cows vaccinated per province and national farm stats."""
    mpo_rows = [r for r in rows if r["source_org"] == "MPO" and r["superseded_by"] == ""]

    # All dates with dairy_cows_vaccinated data
    dairy_dates = sorted(set(r["effective_date"] for r in mpo_rows
                             if r["metric"] == "dairy_cows_vaccinated"))

    prov_codes = [c for c, _ in PROVINCES]

    weekly = []
    for ed in dairy_dates:
        week_data = {"date": ed}
        total = 0
        for code in prov_codes:
            matches = [r for r in mpo_rows if r["effective_date"] == ed
                       and r["province"] == code and r["metric"] == "dairy_cows_vaccinated"]
            val = int(num(matches[0]["value"]) or 0) if matches else 0
            week_data[code] = val
            total += val
        week_data["national"] = total
        weekly.append(week_data)

    latest_w = weekly[-1] if weekly else {}
    prev_w   = weekly[-2] if len(weekly) >= 2 else {}

    def get_nat_mpo(metric):
        matches = [r for r in mpo_rows
                   if r["province"] == "national" and r["metric"] == metric]
        if not matches:
            return None, None
        matches.sort(key=lambda r: r["effective_date"], reverse=True)
        return int(num(matches[0]["value"]) or 0), matches[0]["effective_date"]

    farms_confirmed, farms_confirmed_date = get_nat_mpo("dairy_farms_confirmed_fmd")
    farms_active,    farms_active_date    = get_nat_mpo("dairy_farms_active_fmd")

    provinces = []
    for code, name in PROVINCES:
        cur = latest_w.get(code, 0)
        prv = prev_w.get(code, 0)
        provinces.append({"code": code, "name": name,
                          "current": cur, "previous": prv, "change": cur - prv})

    # Per-province active dairy farm counts — most recent available per province.
    # Stored in master as dairy_farms_active_fmd_prov; carry-forward if Week 30
    # had no per-province breakdown.
    active_by_province = []
    for code, name in PROVINCES:
        prov_rows = [r for r in mpo_rows
                     if r["province"] == code
                     and r["metric"] == "dairy_farms_active_fmd_prov"
                     and r["superseded_by"] == ""]
        if prov_rows:
            prov_rows.sort(key=lambda r: r["effective_date"], reverse=True)
            val = int(num(prov_rows[0]["value"]) or 0)
        else:
            val = 0
        active_by_province.append({"code": code, "name": name, "active": val})

    # Weekly trend of confirmed and active farms (national)
    farms_trend = []
    farm_dates = sorted(set(
        r["effective_date"] for r in mpo_rows
        if r["metric"] in ("dairy_farms_active_fmd", "dairy_farms_confirmed_fmd",
                           "dairy_farms_total_fmd")
        and r["province"] == "national"
    ))
    for fd in farm_dates:
        active_m  = [r for r in mpo_rows if r["effective_date"] == fd
                     and r["province"] == "national"
                     and r["metric"] == "dairy_farms_active_fmd"]
        conf_m    = [r for r in mpo_rows if r["effective_date"] == fd
                     and r["province"] == "national"
                     and r["metric"] in ("dairy_farms_confirmed_fmd", "dairy_farms_total_fmd")]
        a = int(num(active_m[0]["value"])  or 0) if active_m else None
        c = int(num(conf_m[0]["value"])    or 0) if conf_m  else None
        farms_trend.append({
            "date": fd,
            "active": a,
            "confirmed": c,
            "resolved": (c - a) if (c is not None and a is not None) else None,
        })

    # Post-vaccination reinfections per province
    reinfections = []
    for code, name in PROVINCES:
        ri_rows = [r for r in mpo_rows
                   if r["province"] == code
                   and r["metric"] == "reinfection_post_vaccination"
                   and r["superseded_by"] == ""]
        if ri_rows:
            ri_rows.sort(key=lambda r: r["effective_date"], reverse=True)
            val  = int(num(ri_rows[0]["value"]) or 0)
            note = ri_rows[0].get("notes", "")
            reinfections.append({"code": code, "name": name, "farms": val,
                                  "date": ri_rows[0]["effective_date"], "note": note})
    reinfections.sort(key=lambda x: -x["farms"])

    farms_resolved = None
    if farms_confirmed is not None and farms_active is not None:
        farms_resolved = farms_confirmed - farms_active

    return {
        "weekly":                  weekly,
        "latest_date":             dairy_dates[-1] if dairy_dates else None,
        "provinces":               provinces,
        "farms_confirmed":         farms_confirmed,
        "farms_confirmed_date":    farms_confirmed_date,
        "farms_active":            farms_active,
        "farms_active_date":       farms_active_date,
        "farms_resolved":          farms_resolved,
        "farms_trend":             farms_trend,
        "reinfections":            reinfections,
        "national_current":        latest_w.get("national", 0),
        "national_previous":       prev_w.get("national", 0),
        "active_by_province":      active_by_province,
    }

def build_rmis(rows):
    """RMIS industry vaccine distribution tracking.
    Combines:
      - Feedlot order timeline (feedlot_vaccine_orders metric, from per-order xlsx exports)
      - Industry distribution breakdown (doses_distributed_industry metric, from Shiny portal + Excel export)
    Falls back gracefully if data is absent.
    """
    import json as _json, re as _re
    from collections import defaultdict
    rmis_json = os.path.join(ROOT, "rmis_orders.json")

    all_rmis = [r for r in rows if r["source_org"] == "RMIS" and r["superseded_by"] == ""]

    # ── 1. Feedlot order timeline ──────────────────────────────────────────────
    feedlot_rows = [r for r in all_rmis if r["metric"] == "feedlot_vaccine_orders"]
    if not feedlot_rows and not os.path.exists(rmis_json):
        # check if we at least have industry distribution data
        if not any(r["metric"] == "doses_distributed_industry" for r in all_rmis):
            return None

    totals = defaultdict(int)
    for r in feedlot_rows:
        totals[r["effective_date"]] += int(num(r["value"]) or 0)
    timeline = [{"date": d, "doses": totals[d]} for d in sorted(totals)]
    latest_t = timeline[-1] if timeline else {}
    prev_t   = timeline[-2] if len(timeline) >= 2 else {}

    # Rich per-order breakdown from JSON (legacy; kept for vet/destination drilldown)
    detail = {}
    if os.path.exists(rmis_json):
        with open(rmis_json, "r", encoding="utf-8") as f:
            jdata = _json.load(f)
        exports = jdata.get("exports", [])
        if exports:
            exports.sort(key=lambda x: x["export_date"])
            detail = exports[-1]

    # ── 2. Industry distribution — allocated vs distributed ───────────────────
    dist_rows = [r for r in all_rmis if r["metric"] == "doses_distributed_industry"]

    alloc_rows = [r for r in all_rmis
                  if r["metric"] == "doses_allocated_industry"
                  and r["province"] == "national"]
    allocated = 0
    if alloc_rows:
        alloc_rows.sort(key=lambda r: r["effective_date"])
        allocated = int(num(alloc_rows[-1]["value"]) or 0)

    # national total distributed (all, private)
    nat_dist = [r for r in dist_rows
                if r["province"] == "national"
                and r["vaccine_type"] == "all"
                and r["vet_channel"] == "private"]
    nat_dist.sort(key=lambda r: r["effective_date"])
    distributed = int(num(nat_dist[-1]["value"]) or 0) if nat_dist else 0
    industry_date = nat_dist[-1]["effective_date"] if nat_dist else latest_t.get("date", "")

    utilisation_pct = round(distributed / allocated * 100, 1) if allocated else 0

    # ── 3. Province x total (all manufacturers) ───────────────────────────────
    prov_total_rows = [r for r in dist_rows
                       if r["province"] not in ("national", "NAT")
                       and r["vaccine_type"] == "all"
                       and r["vet_channel"] == "private"]
    # take most recent per province
    prov_best = {}
    for r in prov_total_rows:
        p = r["province"]
        if p not in prov_best or r["effective_date"] > prov_best[p]["effective_date"]:
            prov_best[p] = r
    by_province_total = {p: int(num(r["value"]) or 0) for p, r in prov_best.items()}

    # ── 4. Province x manufacturer ────────────────────────────────────────────
    def _prov_mfr(vtype):
        rows_m = [r for r in dist_rows
                  if r["province"] not in ("national", "NAT")
                  and r["vaccine_type"] == vtype
                  and r["vet_channel"] == "private"]
        best = {}
        for r in rows_m:
            p = r["province"]
            if p not in best or r["effective_date"] > best[p]["effective_date"]:
                best[p] = r
        return {p: int(num(r["value"]) or 0) for p, r in best.items()}

    by_province_bio    = _prov_mfr("bioaftogen")
    by_province_dolvet = _prov_mfr("dolvet")

    # ── 5. Sector breakdown (national: stud / commercial / feedlot) ───────────
    sector_rows = [r for r in dist_rows
                   if r["province"] == "national"
                   and r["vaccine_type"] == "all"
                   and r["vet_channel"] in ("stud", "commercial", "feedlot")]
    by_sector = {r["vet_channel"]: int(num(r["value"]) or 0) for r in sector_rows}

    # ── 6. Municipality breakdown (province x municipality x sector) ──────────
    munic_rows = [r for r in dist_rows
                  if r["province"] not in ("national", "NAT")
                  and r["vaccine_type"] == "all"
                  and r["vet_channel"] in ("stud", "commercial", "feedlot")]
    munic_list = []
    for r in munic_rows:
        m = _re.search(r"Municipality: ([^.]+)", r.get("notes", ""))
        munic = m.group(1).strip() if m else "Unknown"
        munic_list.append({
            "province":     r["province"],
            "municipality": munic,
            "sector":       r["vet_channel"],
            "doses":        int(num(r["value"]) or 0),
        })
    munic_list.sort(key=lambda x: x["doses"], reverse=True)

    # ── 7. Operations metrics ─────────────────────────────────────────────────
    vet_rows  = [r for r in all_rmis if r["metric"] == "vet_practices_ordering"]
    site_rows = [r for r in all_rmis
                 if r["metric"] == "vaccination_sites" and r["province"] == "national"]
    vet_count  = int(num(vet_rows[-1]["value"]) or 0)  if vet_rows  else 0
    site_count = int(num(site_rows[-1]["value"]) or 0) if site_rows else 0

    return {
        # ── industry distribution (new) ──
        "allocated":          allocated,
        "distributed":        distributed,
        "utilisation_pct":    utilisation_pct,
        "industry_date":      industry_date,
        "by_province_total":  by_province_total,
        "by_province_bio":    by_province_bio,
        "by_province_dolvet": by_province_dolvet,
        "by_sector":          by_sector,
        "by_municipality":    munic_list,
        "vet_practices":      vet_count,
        "vaccination_sites":  site_count,
        # ── feedlot order timeline (retained) ──
        "timeline":            timeline,
        "latest_date":         detail.get("export_date") or industry_date,
        "latest_doses":        detail.get("total_doses") or latest_t.get("doses", 0),
        "previous_doses":      prev_t.get("doses", 0),
        "total_orders":        detail.get("total_orders", 0),
        "unique_vets":         detail.get("unique_vets", 0),
        "unique_destinations": detail.get("unique_destinations", 0),
        "by_province":         detail.get("by_province", by_province_total),
        "by_district":         detail.get("by_district", {}),
        "by_location_type":    detail.get("by_location_type", {}),
        "by_commodity":        detail.get("by_commodity", {}),
        "by_supplier":         detail.get("by_supplier", {}),
        "by_vaccine_type":     detail.get("by_vaccine_type", {}),
        "by_vet":              detail.get("by_vet", {}),
    }

def national_view(rows, snapshot):
    """Compute the headline national figures by summing the most recent per-province
    values from any PROGRAMME_SOURCES (carry-forward). This replaces the prior approach
    of looking up province='national' ICC rows, which only updated when the consolidated
    AgriSA xlsx arrived. The dashboard now synthesises the national picture from
    individual provincial JOC submissions, which is the whole point of the system."""
    prog_rows = [r for r in rows
                 if r["source_org"] in PROGRAMME_SOURCES and r["superseded_by"] == ""]

    total_recv = sum(_best_received(prog_rows, code)   for code, _ in PROVINCES)
    total_adm  = sum(_best_vaccinated(prog_rows, code) for code, _ in PROVINCES)
    total_pos  = sum(
        latest_metric(prog_rows, province=code, metric="positive_cases") or 0
        for code, _ in PROVINCES
    )
    total_sus  = sum(
        latest_metric(prog_rows, province=code, metric="suspected_cases") or 0
        for code, _ in PROVINCES
    )
    total_neg  = sum(
        latest_metric(prog_rows, province=code, metric="negative_cases",
                      skip_zero=False) or 0
        for code, _ in PROVINCES
    )
    total_pend = sum(
        latest_metric(prog_rows, province=code, metric="pending_cases",
                      skip_zero=False) or 0
        for code, _ in PROVINCES
    )
    herd = sum(
        latest_metric(prog_rows, province=code, metric="herd_cattle",
                      prefer_org=["AgriSA-NAT", "Ministry", "WC-GIS"]) or 0
        for code, _ in PROVINCES
    )

    # National doses procured into South Africa from manufacturers (Ministerial figure)
    procured_rows = [r for r in rows
                     if r["province"] == "national"
                     and r["metric"] == "doses_procured"
                     and r["source_org"] == "Ministry"
                     and r["superseded_by"] == ""]
    procured = 0
    if procured_rows:
        procured_rows.sort(key=lambda r: r["effective_date"], reverse=True)
        procured = int(num(procured_rows[0]["value"]) or 0)

    out = {
        "positive":     int(total_pos),
        "suspected":    int(total_sus),
        "negative":     int(total_neg),
        "pending":      int(total_pend),
        "procured":     int(procured),
        "distributed":  int(total_recv),
        "received":     int(total_recv),  # legacy alias retained for backwards compatibility
        "administered": int(total_adm),
        "herd_cattle":  int(herd),
    }
    out["balance"] = out["distributed"] - out["administered"]
    return out



def build_ministerial_comparison(rows):
    """Compare ministerial figures (23 Apr) vs JOC/AgriSA latest per province."""
    result = []
    for code, name in PROVINCES:
        joc = latest_metric(rows, province=code, metric="animals_vaccinated",
                            vaccine_type="all", vet_channel="all",
                            prefer_org=list(PROGRAMME_SOURCES))
        joc_date = latest_province_date(rows, code)

        min_rows = [r for r in rows if r["source_org"] == "Ministry"
                    and r["province"] == code
                    and r["metric"] == "cattle_vaccinated_ministerial"
                    and r["superseded_by"] == ""]
        min_val, min_date = None, None
        if min_rows:
            min_rows.sort(key=lambda r: r["effective_date"], reverse=True)
            min_val = num(min_rows[0]["value"])
            min_date = min_rows[0]["effective_date"]

        joc_int = int(joc) if joc else None
        min_int = int(min_val) if min_val else None
        diff = (joc_int - min_int) if (joc_int is not None and min_int is not None) else None

        flag = None
        if diff is not None:
            if diff < -5000:
                flag = "critical"
            elif diff == 0:
                flag = "warning"

        result.append({
            "code": code, "name": name,
            "joc": joc_int, "joc_date": joc_date,
            "ministerial": min_int, "ministerial_date": min_date,
            "diff": diff, "flag": flag
        })
    return result


def build_quality_flags(rows, snapshot, min_comparison):
    """Detect data quality issues and generate actionable flags."""
    from datetime import datetime, timedelta
    flags = []

    for code, name in PROVINCES:
        received = latest_metric(rows, province=code, metric="doses_received",
                                 vaccine_type="all", vet_channel="all",
                                 prefer_org=["AgriSA-NAT", "Ministry"])
        vaccinated = latest_metric(rows, province=code, metric="animals_vaccinated",
                                   vaccine_type="all", vet_channel="all",
                                   prefer_org=["AgriSA-NAT", "Ministry", "WC-GIS", "GDARD"])
        if received and vaccinated and vaccinated > received:
            flags.append({
                "severity": "critical", "province": code,
                "title": f"{name}: Animals vaccinated exceeds doses received",
                "detail": (f"JOC reports {int(vaccinated):,} animals vaccinated but only "
                            f"{int(received):,} doses received in province. Likely a cumulative "
                            f"vs period reporting mismatch, or draw on pre-rollout stock."),
                "action": ("Confirm whether provincial figures are cumulative from rollout start "
                            "or period-only. Request reconciliation of receipt and administration logs."),
                "owner": f"{name} AgriSA affiliate / JOC"
            })

    for item in min_comparison:
        if item["flag"] == "critical" and item["ministerial"] and item["joc"]:
            flags.append({
                "severity": "critical", "province": item["code"],
                "title": f"{item['name']}: JOC figure lower than ministerial briefing",
                "detail": (f"Ministerial ({item['ministerial_date']}) reported "
                            f"{item['ministerial']:,} cattle vaccinated; current JOC/AgriSA "
                            f"figure is {item['joc']:,} — gap of {abs(item['diff']):,}. "
                            f"Impossible if both are cumulative."),
                "action": ("Reconcile AgriSA provincial return against ministerial figure. "
                            "Determine whether ministerial count includes additional species "
                            "(pigs, sheep) beyond cattle only."),
                "owner": f"{item['name']} AgriSA affiliate"
            })

    snapshot_dt = datetime.strptime(snapshot, "%Y-%m-%d")
    two_weeks_ago = (snapshot_dt - timedelta(days=14)).strftime("%Y-%m-%d")
    for code, name in PROVINCES:
        prov_dates = [r["effective_date"] for r in rows
                      if r["province"] == code and r["superseded_by"] == ""]
        if prov_dates and max(prov_dates) < two_weeks_ago:
            flags.append({
                "severity": "warning", "province": code,
                "title": f"{name}: No submission in more than 14 days",
                "detail": f"Most recent data for {name} is {max(prov_dates)}, more than 14 days ago.",
                "action": f"Follow up with {name} affiliate for outstanding JOC submission.",
                "owner": f"{name} AgriSA affiliate"
            })

    has_spoilage = any(r for r in rows if r["metric"] == "doses_spoiled"
                       and (num(r["value"]) or 0) > 0)
    if not has_spoilage:
        flags.append({
            "severity": "critical", "province": "national",
            "title": "National: Spoilage data absent across all provinces",
            "detail": ("No province has reported non-zero vaccine spoilage in any submission. "
                        "Cold chain failures and near-expiry stock are almost certainly occurring."),
            "action": ("Add spoilage/wastage field to all provincial JOC templates. "
                        "Request immediate ad-hoc return from all provinces on doses spoiled to date."),
            "owner": "FMD ICC Secretariat"
        })

    return flags

def validate_output(html, path):
    """Raise if the built HTML looks malformed so we never write a broken file."""
    errors = []
    if not html.strip().endswith('</html>'):
        errors.append("HTML does not end with </html>")
    if '/* DATA_PLACEHOLDER */' in html:
        errors.append("DATA_PLACEHOLDER was not replaced (template injection failed)")
    if 'const DASHBOARD_DATA' not in html:
        errors.append("DASHBOARD_DATA constant not found in output")
    # Count all <script...> opening tags (with or without attributes)
    import re as _re
    open_tags  = len(_re.findall(r'<script[\s>]', html))
    close_tags = html.count('</script>')
    if open_tags != close_tags:
        errors.append(f"Mismatched script tags: {open_tags} open vs {close_tags} close")
    script_start = html.rfind('<script')
    script_end   = html.rfind('</script>')
    if script_start > script_end:
        errors.append("Last <script> block has no matching </script>")
    if errors:
        raise ValueError(f"Dashboard output validation FAILED for {path}:\n  " + "\n  ".join(errors))
    return True

VAX_LABELS = {
    "bioaftogen": "Bioaftogen", "dolvet": "DolVet", "obp_arc": "OBP / ARC",
    "bvi": "BVI", "artio_preva": "Artio-PREVA", "artio_preva_other": "Artio-PREVA",
    "emergency_stock": "Emergency stock", "bioaftogen_biv1": "Bioaftogen Bivalent",
    "bioaftogen_triv2": "Bioaftogen Trivalent", "dolvet_emergency": "DolVet (emergency)",
    "aftodoll1": "Aftodoll dose 1", "aftodoll2": "Aftodoll dose 2",
}
CHANNEL_LABELS = {
    "state": "State vet", "private": "Private vet", "state_vet": "State vet",
    "feedlot": "Feedlot", "communal": "Communal", "commercial": "Commercial",
    "emerging": "Emerging", "total": "Total",
}
CLASS_LABELS = {
    "commercial_vaccinated": "Commercial cattle",
    "communal_vaccinated": "Communal cattle",
    "dairy_vaccinated": "Dairy cattle",
    "pigs_vaccinated": "Pigs",
    "emerging_vaccinated": "Emerging farmers",
}
# commercial_beef_vaccinated is a subset of commercial_vaccinated reported by some provinces.
# It is merged into the "Commercial cattle" bucket below to avoid double-counting.
EXTRA_LABELS = {
    "vaccine_wastage": "Vaccine wastage", "primary_vaccinations": "Primary vaccinations",
    "booster_vaccinations": "Booster vaccinations", "private_vet_vaccinations": "Private vet vaccinations",
    "state_vet_vaccinations": "State vet vaccinations", "vaccination_sites": "Vaccination sites",
    "private_vets_active": "Private vets active", "controlled_slaughter": "Controlled slaughter",
    "animals_vaccinated_dose1": "Dose 1 animals", "animals_vaccinated_dose2": "Dose 2 animals",
    "vaccine_balance": "Vaccine balance on hand", "rfid_tags_received": "RFID tags received",
    "animals_eartagged_district": "Animals eartagged",
}

def build_provincial_detail(rows):
    prog = [r for r in rows if r["superseded_by"] == ""]
    detail = {}

    def latest_prov(prov, metric, vt="", vc=""):
        cands = [r for r in prog if r["province"] == prov and r["metric"] == metric
                 and r["vaccine_type"] in ([vt] if vt else ("", "all", "total"))
                 and r["vet_channel"] in ([vc] if vc else ("", "all", "total"))
                 and (num(r["value"]) or 0) > 0]
        if not cands: return None, None
        cands.sort(key=lambda r: (r["effective_date"], int(r["version"])), reverse=True)
        return num(cands[0]["value"]), cands[0]["effective_date"]

    for code, name in PROVINCES:
        prov_rows = [r for r in prog if r["province"] == code]
        if not prov_rows:
            continue

        # Vaccine type breakdown
        vax_types = {}
        for r in prov_rows:
            vt = r["vaccine_type"]
            if (r["metric"] == "doses_received"
                    and vt not in ("", "all", "total")
                    and not vt[0].isupper()           # skip raw-label duplicates
                    and r["vet_channel"] in ("", "all", "total")):
                val = num(r["value"]) or 0
                if val > 0:
                    cur = vax_types.get(vt)
                    if cur is None or r["effective_date"] > cur["date"]:
                        vax_types[vt] = {"type": vt, "label": VAX_LABELS.get(vt, vt),
                                          "doses": int(val), "date": r["effective_date"]}
        vax_list = sorted(vax_types.values(), key=lambda x: -x["doses"])

        # Vet channel split
        channels = {}
        for vc in ("state", "private", "state_vet", "communal", "commercial", "emerging"):
            entry = {}
            for metric in ("doses_received", "animals_vaccinated"):
                v, dt = latest_prov(code, metric, vc=vc)
                if v:
                    entry[metric] = int(v)
                    entry["date"] = dt
            if entry:
                label = CHANNEL_LABELS.get(vc, vc)
                # Merge state and state_vet
                key = "state" if vc == "state_vet" else vc
                if key in channels:
                    for k, v2 in entry.items():
                        if k not in channels[key]:
                            channels[key][k] = v2
                else:
                    channels[key] = {"label": label, **entry}
        chan_list = [{"key": k, **v} for k, v in channels.items()]

        # Animal classification — merge commercial_beef_vaccinated into commercial_vaccinated
        # to avoid double-counting when both metrics appear for the same province.
        cls_list = []
        for metric, label in CLASS_LABELS.items():
            v, dt = latest_prov(code, metric)
            # If commercial_vaccinated is missing, fall back to commercial_beef_vaccinated
            if metric == "commercial_vaccinated" and not v:
                v, dt = latest_prov(code, "commercial_beef_vaccinated")
            if v:
                cls_list.append({"category": metric, "label": label,
                                  "value": int(v), "date": dt})
        cls_list.sort(key=lambda x: -x["value"])

        # District breakdown — include vaccinated, cases, suspected, pending and reported_outbreaks.
        # Notes field often contains rich context including embedded case counts
        # in the pattern "X positive / Y suspect / Z negative" (e.g. EC district rows).
        import re as _re

        def _parse_district_name(note, metric):
            """Extract a clean district name from the notes field."""
            # Pattern: "EC district [NAME] as at ..." or "district=[NAME]" or "District: [NAME] | ..."
            m = _re.search(r'district=([^;,\n]+)', note)
            if m: return m.group(1).strip()
            m = _re.search(r'[A-Z]{2,3} district ([A-Za-z\s]+?) (?:as at|dated|–|-)', note)
            if m: return m.group(1).strip()
            m = _re.search(r'(?:District|State Vet Area):\s*([^|;,\n]+?)(?:\s*\||\.|$)', note)
            if m: return m.group(1).strip()
            # Fallback: first segment before pipe, period or 50 chars
            seg = note.split(" | ")[0] if " | " in note else note.split(".")[0]
            seg = _re.sub(r'\b(District|State Vet Area|SVA|LM|Local Municipality):\s*', '', seg)
            return seg[:45].strip()

        def _parse_embedded_cases(note):
            """Extract 'X positive / Y suspect / Z negative' from a notes string."""
            m = _re.search(r'(\d+)\s+positive\s*/\s*(\d+)\s+suspect\s*/\s*(\d+)\s+negative', note, _re.IGNORECASE)
            if m:
                return int(m.group(1)), int(m.group(2)), int(m.group(3))
            return None, None, None

        # Only include metrics that are definitively district/municipal breakdowns.
        # reported_outbreaks is excluded — it contains provincial totals from MinMEC,
        # GDARD infographics etc. that are not district-level and pollute this section.
        dist_metrics = (
            "animals_vaccinated_district", "positive_cases_district",
            "suspected_cases_district", "pending_cases_district",
        )
        dist_rows = [r for r in prov_rows if r["metric"] in dist_metrics]

        dist_map = {}
        # Keywords that indicate a row is a source reference, not a geographic district
        _source_noise = ("infographic", "slide", "minmec", "pcm", "joc", "via whatsapp",
                         "cumulative", "briefing", "presentation", "report", "template",
                         "email", "media statement", "ministerial", "gdard", "drdar")

        for r in dist_rows:
            note  = r.get("notes", "")
            dname = _parse_district_name(note, r["metric"])
            if not dname or len(dname) < 2:
                continue
            # Reject rows where the parsed name looks like a source reference
            if any(kw in dname.lower() for kw in _source_noise):
                continue
            key = (r["effective_date"], dname[:45])
            if key not in dist_map:
                dist_map[key] = {"name": dname[:45], "date": r["effective_date"],
                                  "vaccinated": None, "cases": None,
                                  "suspected": None, "pending": None,
                                  "outbreaks": None, "negative": None,
                                  "notes": note}
            metric = r["metric"]
            val = int(num(r["value"]) or 0)
            if metric == "animals_vaccinated_district":
                dist_map[key]["vaccinated"] = val
                # Parse embedded case counts from notes (common in EC rows)
                pos, sus, neg = _parse_embedded_cases(note)
                if pos is not None and dist_map[key]["cases"] is None:
                    dist_map[key]["cases"]    = pos
                    dist_map[key]["suspected"] = sus
                    dist_map[key]["negative"]  = neg
            elif metric == "positive_cases_district":
                dist_map[key]["cases"] = val
            elif metric == "suspected_cases_district":
                dist_map[key]["suspected"] = val
            elif metric == "pending_cases_district":
                dist_map[key]["pending"] = val
            elif metric == "reported_outbreaks":
                dist_map[key]["outbreaks"] = val

        # Prefer the most recent date per district name
        latest_by_name = {}
        for (dt, nm), entry in sorted(dist_map.items()):
            latest_by_name[nm] = entry

        dist_list = sorted(
            latest_by_name.values(),
            key=lambda x: (-(x["vaccinated"] or 0), -(x["cases"] or x["outbreaks"] or 0))
        )

        # Extra indicators
        extra = {}
        for metric, label in EXTRA_LABELS.items():
            v, dt = latest_prov(code, metric)
            if v:
                extra[metric] = {"label": label, "value": int(v) if v == int(v) else round(v, 2), "date": dt}

        # Sources (relabel the canonical Ministry/ICC source for display)
        sources = sorted(set(
            (MINISTRY_ICC_LABEL if r["source_org"] == MINISTRY_ICC_CANON else r["source_org"])
            for r in prov_rows))

        detail[code] = {
            "name": name,
            "latest_date": latest_province_date(prog, code),
            "vaccine_types": vax_list,
            "vet_channels": chan_list,
            "classification": cls_list,
            "districts": dist_list[:30],
            "extra": extra,
            "sources": sources,
        }

    return detail


def build_dashboard():
    rows = load_master()
    if not rows:
        print("No master data — nothing to build.")
        return
    dates = latest_dates(rows)
    snapshot = dates[-1]
    print(f"Building dashboard from snapshot {snapshot}; {len(dates)} weekly points.")

    nat = national_view(rows, snapshot)
    payload = {
        "snapshot_date": snapshot,
        "build_date": str(date.today()),
        "provinces": build_provinces(rows, snapshot),
        "weekly": build_weekly(rows),
        "sources": build_source_mix(rows, snapshot),
        "national": nat,
        "mpo":  build_mpo(rows),
        "rmis": build_rmis(rows),
    }

    # Week-on-week deltas — derived from the already-computed weekly series so that
    # deltas are always consistent with what the chart shows, even when the prior
    # week has no province="national" ICC row (JOC-only dates).
    weekly_series = payload["weekly"]
    if len(weekly_series) >= 2:
        cur  = weekly_series[-1]
        prev = weekly_series[-2]
        payload["national"]["delta_received"]     = int((cur["received"]     or 0) - (prev["received"]     or 0))
        payload["national"]["delta_distributed"]  = int((cur["received"]     or 0) - (prev["received"]     or 0))
        payload["national"]["delta_administered"] = int((cur["administered"] or 0) - (prev["administered"] or 0))
        payload["national"]["delta_positive"]     = int((cur["positive"]     or 0) - (prev["positive"]     or 0))
    else:
        payload["national"]["delta_received"] = 0
        payload["national"]["delta_distributed"] = 0
        payload["national"]["delta_administered"] = 0
        payload["national"]["delta_positive"] = 0

    # Ministerial / DAFF figures — most recent Ministry-sourced totals
    def min_nat(metric, vaccine_type="", vet_channel=""):
        matches = [r for r in rows if r["source_org"] == "Ministry"
                   and r["province"] == "national" and r["metric"] == metric
                   and r["vaccine_type"] == vaccine_type and r["superseded_by"] == ""]
        if not matches:
            return None
        matches.sort(key=lambda r: r["effective_date"], reverse=True)
        return num(matches[0]["value"]), matches[0]["effective_date"]

    min_recv = min_nat("doses_procured", "all", "all")
    min_dist = min_nat("doses_distributed", "all", "all")
    min_adm  = min_nat("animals_vaccinated_ministerial", "all", "all")

    prov_ministerial = {}
    for code, name in PROVINCES:
        m = [r for r in rows if r["source_org"] == "Ministry"
             and r["province"] == code
             and r["metric"] == "cattle_vaccinated_ministerial"
             and r["superseded_by"] == ""]
        if m:
            m.sort(key=lambda r: r["effective_date"], reverse=True)
            prov_ministerial[code] = {
                "value": int(num(m[0]["value"]) or 0),
                "as_of": m[0]["effective_date"],
            }

    policy_events = []
    if any(r["metric"] == "section10_scheme_published" for r in rows):
        policy_events.append({
            "date": "2026-05-04",
            "title": "Section 10 Routine Vaccination Scheme gazetted",
            "detail": ("Farmers may now vaccinate voluntarily under private vet supervision "
                       "without waiting for the national rollout. Animals must be individually "
                       "traceable and digitally recorded.")
        })
    if any(r["metric"] == "dma_lifted" and r["province"] == "KZN" for r in rows):
        policy_events.append({
            "date": "2026-05-05",
            "title": "KwaZulu-Natal DMA formally lifted",
            "detail": ("The KZN Disease Management Area restrictions have been rescinded. "
                       "Movement controls will transition to a unified province-wide protocol "
                       "replacing the localised DMA rules.")
        })

    incoming = []
    # Vaccine supply pipeline — hardcoded from ministerial briefings and RMIS import tracker.
    # Updated as at 1 June 2026 (Minister Steenhuisen, Parliament).
    # Do not regenerate from doses_incoming rows (stale format). Update here manually.
    incoming = [
        {"vaccine": "ARC Trivalent",        "doses": 12900,    "date": "2026-02-01", "status": "Arrived",  "notes": "Initial emergency stock."},
        {"vaccine": "Biogenesis Bivalent",  "doses": 1000000,  "date": "2026-02-01", "status": "Arrived",  "notes": ""},
        {"vaccine": "DolVet Trivalent",     "doses": 1500000,  "date": "2026-02-01", "status": "Arrived",  "notes": ""},
        {"vaccine": "Biogenesis Trivalent", "doses": 1500000,  "date": "2026-04-01", "status": "Arrived",  "notes": ""},
        {"vaccine": "DolVet Trivalent",     "doses": 2000000,  "date": "2026-04-01", "status": "Arrived",  "notes": ""},
        {"vaccine": "DolVet Trivalent",     "doses": 2000000,  "date": "2026-05-01", "status": "Arrived",  "notes": ""},
        {"vaccine": "Biogenesis Bago",      "doses": 3500000,  "date": "2026-05-28", "status": "Arrived",  "notes": "Distributed: 1.5M feedlots; 500 000 RMPO; 200 000 MPO; 100 000 stud breeders; 1.05M provinces; balance for border vaccination."},
        {"vaccine": "DolVet (Dunevax)",     "doses": 4000000,  "date": "2026-06-30", "status": "Expected", "notes": "First consignment of 14M SAHPRA Section 21-approved Dollvet doses. Enables booster programme."},
        {"vaccine": "DolVet (Dunevax)",     "doses": 10000000, "date": "2026",       "status": "Pipeline", "notes": "Remaining balance of 14M SAHPRA Section 21 approval. Delivery schedule to be confirmed."},
    ]

    payload["ministerial"] = {
        "doses_procured":          int(min_recv[0]) if min_recv else None,
        "doses_procured_asof":     min_recv[1] if min_recv else None,
        "doses_distributed":       int(min_dist[0]) if min_dist else None,
        "animals_vaccinated":      int(min_adm[0]) if min_adm else None,
        "animals_vaccinated_asof": min_adm[1] if min_adm else None,
        "provincial_cattle":       prov_ministerial,
        "policy_events":           policy_events,
        "incoming_supply":         incoming,
        "source_date":             "2026-06-04",
        "source_label":            "DoA Portfolio Committee briefing, 9 June 2026 (data as at 4 June 2026)",
    }

    min_comparison = build_ministerial_comparison(rows)
    payload["ministerial_comparison"] = min_comparison
    payload["quality_flags"] = build_quality_flags(rows, snapshot, min_comparison)

    payload["provincial_detail"] = build_provincial_detail(rows)

    # SAPPO pork-sector dispatch data — updated from email 5 June 2026 (Thandi Chiappero)
    # 5 new rows vs 3 June email: LP +345 (13 May), KZN +20 (18 May) +6 (3 Jun),
    # FS +56 (4 Jun), and 62 bottles on 25 May with no province listed.
    payload["sappo"] = {
        "source": "Email — Dr Thandi Chiappero, SAPPO Head: Consumer Assurance, 5 June 2026",
        "vaccine": "Aftodoll (Dollvet)",
        "note": ("Some bottles were used for cattle on the same farms to reduce FMD risk to pigs. "
                 "The cattle/pig split is not available at dispatch level. "
                 "KZN volume is elevated because KZN state veterinary services were not allocating vaccine to pig producers. "
                 "62 bottles dispatched on 25 May 2026 have no province recorded — excluded from provincial totals."),
        "total_bottles": 2075,
        "dispatches": [
            {"date": "2026-04-30", "rep": "ML", "bottles": 600, "province": "LP",  "province_name": "Limpopo"},
            {"date": "2026-05-05", "rep": "TC", "bottles": 80,  "province": "NW",  "province_name": "North West"},
            {"date": "2026-05-05", "rep": "TC", "bottles": 37,  "province": "NW",  "province_name": "North West"},
            {"date": "2026-05-07", "rep": "TC", "bottles": 130, "province": "LP",  "province_name": "Limpopo"},
            {"date": "2026-05-12", "rep": "ML", "bottles": 8,   "province": "FS",  "province_name": "Free State"},
            {"date": "2026-05-13", "rep": "TC", "bottles": 508, "province": "KZN", "province_name": "KwaZulu-Natal"},
            {"date": "2026-05-13", "rep": "ML", "bottles": 345, "province": "LP",  "province_name": "Limpopo"},
            {"date": "2026-05-14", "rep": "ML", "bottles": 74,  "province": "EC",  "province_name": "Eastern Cape"},
            {"date": "2026-05-18", "rep": "TC", "bottles": 20,  "province": "KZN", "province_name": "KwaZulu-Natal"},
            {"date": "2026-05-22", "rep": "TC", "bottles": 15,  "province": "WC",  "province_name": "Western Cape"},
            {"date": "2026-05-25", "rep": "ML", "bottles": 62,  "province": "?",   "province_name": "Unspecified"},
            {"date": "2026-05-27", "rep": "ML", "bottles": 34,  "province": "MP",  "province_name": "Mpumalanga"},
            {"date": "2026-06-03", "rep": "TC", "bottles": 100, "province": "KZN", "province_name": "KwaZulu-Natal"},
            {"date": "2026-06-03", "rep": "ML", "bottles": 6,   "province": "KZN", "province_name": "KwaZulu-Natal"},
            {"date": "2026-06-04", "rep": "TC", "bottles": 56,  "province": "FS",  "province_name": "Free State"},
        ],
        "by_province": {"LP": 1075, "KZN": 634, "NW": 117, "EC": 74, "FS": 64, "MP": 34, "WC": 15},
        "by_rep": {"TC": 1404, "ML": 609},
    }

    payload["sources_used"] = sorted(set(r["source_file"] for r in rows
                                         if r["superseded_by"] == ""))

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read().replace("\x00", "")  # strip null bytes left by some editors
    json_block = json.dumps(payload, indent=2)
    out_html = template.replace("/* DATA_PLACEHOLDER */",
                                "const DASHBOARD_DATA = " + json_block + ";")


    # Ministerial comparison date — derived from the latest cattle_vaccinated_ministerial row
    # Ministerial comparison date — derived from the latest cattle_vaccinated_ministerial row
   
    min_dates = [r["effective_date"] for r in rows
                 if r["metric"] == "cattle_vaccinated_ministerial"
                 and r["source_org"] == "Ministry" and r["superseded_by"] == ""]
    if min_dates:
        latest_min_date = max(min_dates)
        try:
            from datetime import datetime as _dt
            _d = _dt.strptime(latest_min_date, "%Y-%m-%d")
            _long  = _d.strftime("%-d %B %Y")
            _short = _d.strftime("%-d %b")
        except Exception:
            _long  = latest_min_date
            _short = latest_min_date
    else:
        _long  = "n/a"
        _short = "n/a"
    out_html = out_html.replace("__MINISTERIAL_DATE_LONG__",  _long)
    out_html = out_html.replace("__MINISTERIAL_DATE_SHORT__", _short)

    validate_output(out_html, DASHBOARD)
    with open(DASHBOARD, "w", encoding="utf-8") as f:
        f.write(out_html)
    print(f"Wrote {DASHBOARD} ({len(out_html)} bytes) - validation passed")


if __name__ == "__main__":
    build_dashboard()
