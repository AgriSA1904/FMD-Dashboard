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
    "AgriSA-NAT", "ICC", "FMD-ICC", "Ministry",
    "FS-JOC", "FS-DRDAR", "FS-DARDLEA", "FS-Landbou",
    "EC-DRDAR", "GP-GDARD", "WC-GIS",
    "LP-LDARD", "MP-DVS", "NW-RPO",
})

# Metrics that indicate real vaccination or disease data (not policy or metadata)
_ANCHOR_METRICS = frozenset({
    "doses_received", "animals_vaccinated", "animals_vaccinated_total",
    "animals_vaccinated_dose1", "positive_cases",
})

def load_master():
    if not os.path.exists(MASTER):
        return []
    with open(MASTER, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

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
    (ingested as 0) from wiping out the last known figure on the dashboard."""
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
                                      prefer_org=["AgriSA-NAT", "ICC"]) or 0),
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
                              prefer_org=["AgriSA-NAT", "ICC", "WC-GIS"]) or 0
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

    return {
        "weekly":                  weekly,
        "latest_date":             dairy_dates[-1] if dairy_dates else None,
        "provinces":               provinces,
        "farms_confirmed":         farms_confirmed,
        "farms_confirmed_date":    farms_confirmed_date,
        "farms_active":            farms_active,
        "farms_active_date":       farms_active_date,
        "national_current":        latest_w.get("national", 0),
        "national_previous":       prev_w.get("national", 0),
        "active_by_province":      active_by_province,
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
                      prefer_org=["AgriSA-NAT", "ICC", "WC-GIS"]) or 0
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
                            prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "GDARD"])
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
                                 prefer_org=["AgriSA-NAT", "ICC"])
        vaccinated = latest_metric(rows, province=code, metric="animals_vaccinated",
                                   vaccine_type="all", vet_channel="all",
                                   prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "GDARD"])
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
        "mpo": build_mpo(rows),
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

    min_recv = min_nat("doses_received", "all", "all")
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
    for r in rows:
        if r["metric"] == "doses_incoming" and r["superseded_by"] == "":
            incoming.append({
                "vaccine":  r["vaccine_type"],
                "doses":    int(num(r["value"]) or 0),
                "expected": r["effective_date"],
                "notes":    r["notes"],
            })
    incoming.sort(key=lambda x: x["expected"])

    payload["ministerial"] = {
        "doses_procured":          int(min_recv[0]) if min_recv else None,
        "doses_procured_asof":     min_recv[1] if min_recv else None,
        "doses_distributed":       int(min_dist[0]) if min_dist else None,
        "animals_vaccinated":      int(min_adm[0]) if min_adm else None,
        "animals_vaccinated_asof": min_adm[1] if min_adm else None,
        "provincial_cattle":       prov_ministerial,
        "policy_events":           policy_events,
        "incoming_supply":         incoming,
        "source_date":             "2026-05-05",
        "source_label":            "Minister Steenhuisen media briefing, 5 May 2026",
    }

    min_comparison = build_ministerial_comparison(rows)
    payload["ministerial_comparison"] = min_comparison
    payload["quality_flags"] = build_quality_flags(rows, snapshot, min_comparison)

    payload["sources_used"] = sorted(set(r["source_file"] for r in rows
                                         if r["superseded_by"] == ""))

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    json_block = json.dumps(payload, indent=2)
    out_html = template.replace("/* DATA_PLACEHOLDER */",
                                "const DASHBOARD_DATA = " + json_block + ";")
    out_html = out_html.replace("__SNAPSHOT_DATE__", snapshot)
    out_html = out_html.replace("__BUILD_DATE__", str(date.today()))

    validate_output(out_html, DASHBOARD)
    with open(DASHBOARD, "w", encoding="utf-8") as f:
        f.write(out_html)
    print(f"Wrote {DASHBOARD} ({len(out_html)} bytes) — validation passed")


if __name__ == "__main__":
    build_dashboard()
