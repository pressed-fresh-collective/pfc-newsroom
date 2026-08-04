#!/usr/bin/env python3
"""Validate pfc-newsroom-data.js before publishing.

Checks: file parses, ids unique & numeric, dates ISO and newest-first,
every repo-relative image path exists, no base64 data URIs, and flags
em dashes in releases dated after the Prowly migration (house style).

Exit code 0 = safe to publish, 1 = broken (do not publish).
"""
import json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "pfc-newsroom-data.js")
MIGRATION_CUTOFF = "2026-07-29"  # releases before this came from Prowly as-is

errors, warnings = [], []

raw = open(DATA, encoding="utf-8").read()
prefix = "window.PFC_RELEASES="
if not raw.startswith(prefix):
    print("FATAL: data file does not start with window.PFC_RELEASES=")
    sys.exit(1)
try:
    releases = json.loads(raw[len(prefix):].rstrip().rstrip(";"))
except json.JSONDecodeError as e:
    print(f"FATAL: data file is not valid JSON: {e}")
    sys.exit(1)

ids = [r.get("id") for r in releases]
if len(ids) != len(set(ids)):
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    errors.append(f"duplicate ids: {dupes}")

prev = None
for r in releases:
    rid = r.get("id", "?")
    if not re.fullmatch(r"\d+", str(rid)):
        errors.append(f"{rid}: id must be digits only")
    date = r.get("date", "")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        errors.append(f"{rid}: bad date {date!r}")
    elif prev and date > prev:
        warnings.append(f"{rid}: dated {date}, out of newest-first order")
    prev = date if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date) else prev
    for k in ("title", "lead"):
        if not r.get(k):
            errors.append(f"{rid}: missing {k}")
    if not r.get("hero"):
        # renderer shows a placeholder; one legacy Prowly release (430026) has no hero
        warnings.append(f"{rid}: no hero image")

    def check_url(u, what):
        if not isinstance(u, str):
            return
        if u.startswith("data:"):
            errors.append(f"{rid}: {what} is a base64 data URI — save it under images/{rid}/ instead")
        elif u and not re.match(r"^(https?:|//)", u):
            if not os.path.exists(os.path.join(REPO, u)):
                errors.append(f"{rid}: {what} points to missing file {u}")

    check_url(r.get("hero"), "hero")
    texts = [r.get("title", ""), r.get("lead", "")]
    for b in r.get("blocks", []):
        t = b.get("t")
        if t == "img":
            check_url(b.get("src"), "img block")
        elif t == "gallery":
            for it in b.get("items", []):
                check_url(it.get("thumb"), "gallery thumb")
                check_url(it.get("full"), "gallery full")
        elif t == "linkcard":
            check_url(b.get("img"), "linkcard img")
        for k in ("html", "label", "cite"):
            if b.get(k):
                texts.append(str(b[k]))
        texts += [str(x) for x in b.get("items", []) if isinstance(x, str)]
    if r.get("date", "") >= MIGRATION_CUTOFF and any("—" in t for t in texts):
        warnings.append(f"{rid}: contains an em dash (house style forbids them)")

size_mb = len(raw) / 1e6
print(f"{len(releases)} releases, data file {size_mb:.2f} MB")
if size_mb > 5:
    warnings.append(f"data file is {size_mb:.1f} MB — consider archiving old years into a second file")

for w in warnings:
    print(f"  WARN  {w}")
for e in errors:
    print(f"  ERROR {e}")
print("OK to publish" if not errors else "BROKEN — fix errors before publishing")
sys.exit(1 if errors else 0)
