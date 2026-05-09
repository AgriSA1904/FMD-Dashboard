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
    """All effective dates from canonical (AgriSA / ICC) sources only — used for the
    weekly time series. RPO and MPO commodity submissions don't drive the weekly axis."""
    return sorted(set(r["effective_date"] for r in rows
                      if r["source_org"] in ("AgriSA-NAT", "ICC")))

def latest_province_date(rows, code):
    """Most recent effective_date with any non-superseded data for this province."""
    dates = sorted(set(r["effective_date"] for r in rows
                       if r["province"] == code and r["superseded_by"] == ""))
    return dates[-1] if dates else None

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
    out = []
    for code, name in PROVINCES:
        # Each metric falls back to its most recent available value, independently.
        # This handles cases like the RPO submission supplying receipts but not cases.
        ed = latest_province_date(rows, code) or snapshot_date
        out.append({
            "code": code, "name": name,
            "as_of": ed,
            "herd": int(latest_metric(rows, province=code, metric="herd_cattle",
                                      prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "EC-DARD", "FS-DARD"]) or 0),
            "positive": int(latest_metric(rows, province=code, metric="positive_cases",
                                          prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "EC-DARD", "FS-DARD"]) or 0),
            "suspected": int(latest_metric(rows, province=code, metric="suspected_cases",
                                           prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "EC-DARD", "FS-DARD"]) or 0),
            "negative": int(latest_metric(rows, province=code, metric="negative_cases",
                                          prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "EC-DARD", "FS-DARD"]) or 0),
            "pending": int(latest_metric(rows, province=code, metric="pending_cases",
                                         prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "EC-DARD", "FS-DARD"]) or 0),
            "received": int(latest_metric(rows, province=code, metric="doses_received",
                                          vaccine_type="all", vet_channel="all",
                                          prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "EC-DARD", "FS-DARD"]) or 0),
            "vaccinated": int(latest_metric(rows, province=code, metric="animals_vaccinated",
                                            vaccine_type="all", vet_channel="all",
                                            prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "GDARD", "EC-DARD", "FS-DARD"]) or 0),
        })
    return out

def build_weekly(rows):
    out = []
    for ed in latest_dates(rows):
        recv = latest_value(rows, effective_date=ed, province="national",
                            metric="doses_received",
                            vaccine_type="all", vet_channel="all")
        adm = latest_value(rows, effective_date=ed, province="national",
                           metric="animals_vaccinated",
                           vaccine_type="all", vet_channel="all")
        pos = latest_value(rows, effective_date=ed, province="national",
                           metric="positive_cases")
        sus = latest_value(rows, effective_date=ed, province="national",
                           metric="suspected_cases")
        pend = latest_value(rows, effective_date=ed, province="national",
                            metric="pending_cases")
        out.append({
            "date": ed,
            "received": int(recv) if recv else None,
            "administered": int(adm) if adm else None,
            "positive": int(pos) if pos is not None else None,
            "suspected": int(sus) if sus is not None else None,
            "pending": int(pend) if pend is not None else None,
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
                              prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "EC-DARD", "FS-DARD"]) or 0
    sum_mfg = sum(out.values())
    out["unallocated"] = max(0, int(nat_total) - sum_mfg)
    return out

def build_rpo_classification(rows):
    """RPO commodity-level breakdown: Dairy / Commercial Beef / Pigs / Communal."""
    metrics = {
        "dairy_vaccinated": 0,
        "commercial_beef_vaccinated": 0,
        "pigs_vaccinated": 0,
        "communal_vaccinated": 0,
    }
    rpo_rows = [r for r in rows if r["source_org"] == "RPO" and r["superseded_by"] == ""
                and r["metric"] in metrics and r["province"] != "national"]
    by_prov = {}
    for r in rpo_rows:
        prov = r["province"]
        m = r["metric"]
        v = num(r["value"]) or 0
        by_prov.setdefault(prov, dict.fromkeys(metrics, 0))[m] = int(v)
        metrics[m] += int(v)
    return {"totals": metrics, "by_province": by_prov,
            "national_total": int(latest_value(rows, effective_date="2026-04-28",
                                               province="national",
                                               metric="animals_vaccinated",
                                               vaccine_type="all", vet_channel="all") or 0)}

def national_view(rows, snapshot):
    # Legacy: pull national-level rows (used for delta comparisons only).
    def nat_legacy(metric, vaccine_type="", vet_channel=""):
        return latest_metric(rows, province="national", metric=metric,
                             vaccine_type=vaccine_type, vet_channel=vet_channel,
                             prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "EC-DARD", "FS-DARD"]) or 0
    return {
        "_legacy_received":     int(nat_legacy("doses_received", "all", "all")),
        "_legacy_administered": int(nat_legacy("animals_vaccinated", "all", "all")),
        "_legacy_positive":     int(nat_legacy("positive_cases")),
    }

def national_view_from_provinces(province_list, rows):
    """Compute national totals by summing province card values.
    This guarantees national KPIs always equal the sum shown on province cards."""
    out = {
        "positive":     sum(p["positive"]   for p in province_list),
        "suspected":    sum(p["suspected"]  for p in province_list),
        "negative":     sum(p["negative"]   for p in province_list),
        "pending":      sum(p["pending"]    for p in province_list),
        "received":     sum(p["received"]   for p in province_list),
        "administered": sum(p["vaccinated"] for p in province_list),
        "herd_cattle":  sum(p["herd"]       for p in province_list),
    }
    out["balance"] = out["received"] - out["administered"]
    return out



def build_ministerial_comparison(rows):
    """Compare ministerial figures (23 Apr) vs JOC/AgriSA latest per province."""
    result = []
    for code, name in PROVINCES:
        joc = latest_metric(rows, province=code, metric="animals_vaccinated",
                            vaccine_type="all", vet_channel="all",
                            prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "GDARD", "EC-DARD", "FS-DARD"])
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
                                 prefer_org=["AgriSA-NAT", "ICC", "EC-DARD", "FS-DARD"])
        vaccinated = latest_metric(rows, province=code, metric="animals_vaccinated",
                                   vaccine_type="all", vet_channel="all",
                                   prefer_org=["AgriSA-NAT", "ICC", "WC-GIS", "GDARD", "EC-DARD", "FS-DARD"])
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

    provinces = build_provinces(rows, snapshot)
    nat       = national_view_from_provinces(provinces, rows)
    legacy    = national_view(rows, snapshot)   # for delta computation only

    # snapshot_date = most recent as_of date across any province (shows true data currency)
    live_snapshot = max((p["as_of"] for p in provinces), default=snapshot)

    payload = {
        "snapshot_date": live_snapshot,
        "build_date": str(date.today()),
        "provinces": provinces,
        "weekly": build_weekly(rows),
        "sources": build_source_mix(rows, live_snapshot),
        "national": nat,
        "rpo": build_rpo_classification(rows),
    }
    # Cross-source totals for the discrepancy panel
    rpo_nat_recv = next((num(r["value"]) for r in rows
                         if r["source_org"] == "RPO" and r["province"] == "national"
                         and r["metric"] == "doses_received" and r["vaccine_type"] == "all"
                         and r["superseded_by"] == ""), None)
    rpo_nat_adm = next((num(r["value"]) for r in rows
                        if r["source_org"] == "RPO" and r["province"] == "national"
                        and r["metric"] == "animals_vaccinated" and r["vaccine_type"] == "all"
                        and r["superseded_by"] == ""), None)
    payload["cross_source"] = {
        "agrisa_received": int(nat["received"]),         # province-summed
        "agrisa_administered": int(nat["administered"]), # province-summed
        "rpo_received": int(rpo_nat_recv or 0),
        "rpo_administered": int(rpo_nat_adm or 0),
    }

    # Week-on-week deltas vs prior weekly snapshot at national level
    # Deltas: current summed-province total vs prior AgriSA-NAT weekly snapshot.
    # Using AgriSA-NAT as the prior baseline gives a stable week-on-week comparison
    # even when the current figure comes from more recent per-province submissions.
    prior = dates[-2] if len(dates) >= 2 else None
    prior_snap = dates[-1]   # last AgriSA-NAT date (used as prior when provinces are newer)
    if prior:
        prior_recv = latest_value(rows, effective_date=prior, province="national",
                                  metric="doses_received",
                                  vaccine_type="all", vet_channel="all") or 0
        prior_adm  = latest_value(rows, effective_date=prior, province="national",
                                  metric="animals_vaccinated",
                                  vaccine_type="all", vet_channel="all") or 0
        prior_pos  = latest_value(rows, effective_date=prior, province="national",
                                  metric="positive_cases") or 0
        payload["national"]["delta_received"]     = int(nat["received"]     - prior_recv)
        payload["national"]["delta_administered"] = int(nat["administered"] - prior_adm)
        payload["national"]["delta_positive"]     = int(nat["positive"]     - prior_pos)
    else:
        payload["national"]["delta_received"] = 0
        payload["national"]["delta_administered"] = 0
        payload["national"]["delta_positive"] = 0
    # Store the prior-week baseline date for display
    payload["national"]["prior_snapshot"] = prior if prior else ""
    payload["national"]["live_snapshot"]  = live_snapshot

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

    # Provincial ministerial cattle vaccinated (23 Apr)
    prov_ministerial = {}
    for code, name in PROVINCES:
        m = [r for r in rows if r["source_org"] == "Ministry"
             and r["province"] == code and r["metric"] == "cattle_vaccinated_ministerial"
             and r["superseded_by"] == ""]
        if m:
            m.sort(key=lambda r: r["effective_date"], reverse=True)
            prov_ministerial[code] = {"value": int(num(m[0]["value"]) or 0),
                                      "as_of": m[0]["effective_date"]}

    # Policy events
    policy_events = []
    if any(r for r in rows if r["metric"] == "section10_scheme_published"):
        policy_events.append({
            "date": "2026-05-04",
            "title": "Section 10 Routine Vaccination Scheme gazetted",
            "detail": ("Farmers may now vaccinate voluntarily under private vet supervision "
                       "without waiting for the national rollout. Animals must be individually "
                       "traceable and digitally recorded.")
        })
    if any(r for r in rows if r["metric"] == "dma_lifted" and r["province"] == "KZN"):
        policy_events.append({
            "date": "2026-05-05",
            "title": "KwaZulu-Natal DMA formally lifted",
            "detail": ("The KZN Disease Management Area restrictions have been rescinded. "
                       "Movement controls will transition to a unified province-wide protocol "
                       "replacing the localised DMA rules.")
        })

    # Incoming supply pipeline
    incoming = []
    for r in rows:
        if r["metric"] == "doses_incoming" and r["superseded_by"] == "":
            incoming.append({"vaccine": r["vaccine_type"],
                             "doses": int(num(r["value"]) or 0),
                             "expected": r["effective_date"],
                             "notes": r["notes"]})
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
    payload["quality_flags"] = build_quality_flags(rows, live_snapshot, min_comparison)

    # Source attribution: every source file contributing to the current view
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
