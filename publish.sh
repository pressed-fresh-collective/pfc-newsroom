#!/bin/bash
# Publish the newsroom: validate, rebuild the preview, commit, push.
# Usage: ./publish.sh "Add release: Artist Name - Single Title"
set -euo pipefail
cd "$(dirname "$0")"

MSG="${1:-Update newsroom}"

python3 tools/validate.py
python3 tools/build_preview.py

git add -A
if git diff --cached --quiet; then
  echo "Nothing to publish - no changes."
  exit 0
fi
git commit -m "$MSG"
git push origin main
echo ""
echo "Pushed. GitHub Pages redeploys in ~1 minute; the live newsroom"
echo "updates within about 10 minutes (CDN cache)."
