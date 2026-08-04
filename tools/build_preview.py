#!/usr/bin/env python3
"""Generate index.html — a standalone preview of the newsroom served by
GitHub Pages itself. Same renderer as the Squarespace code block, but
DATA_URL is swapped to the local copy so the preview always shows exactly
what is deployed. Run after any change to newsroom-code-block.html; the
publish script runs it automatically."""
import os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
block = open(os.path.join(REPO, "newsroom-code-block.html"), encoding="utf-8").read()

block = re.sub(r"var DATA_URL = '[^']*';",
               "var DATA_URL = './pfc-newsroom-data.js';", block, count=1)

page = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>PFC Newsroom — live preview</title>
<style>
  body { margin: 0; font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif; background: #fff; }
  .preview-note { background: #614DFF; color: #fff; font-size: 13px; padding: 8px 16px; text-align: center; }
  .preview-wrap { padding: 28px 20px 60px; }
</style>
</head>
<body>
<div class="preview-note">Preview of the PFC newsroom — the live page is on pressedfreshcollective.com</div>
<div class="preview-wrap">
""" + block + """
</div>
</body>
</html>
"""

out = os.path.join(REPO, "index.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(page)
print(f"Wrote {out} ({len(page)/1024:.0f} KB)")
