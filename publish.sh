#!/bin/bash
# Publish the newsroom: validate, rebuild the preview, commit, push.
# Usage: ./publish.sh "Add release: Artist Name - Single Title"
set -euo pipefail
cd "$(dirname "$0")"

MSG="${1:-Update newsroom}"

# The cloud routine also pushes to this repo - always sync down first
# so local edits land on top of the latest published state.
git pull --rebase --autostash origin main

python3 tools/validate.py
python3 tools/build_preview.py

git add -A
if git diff --cached --quiet; then
  echo "Nothing to publish - no changes."
  exit 0
fi
git commit -m "$MSG"

# Push what we actually committed, not the local `main` ref. Sessions
# usually run on a generated `claude/*` branch, and `git push origin
# main` from there pushes an untouched local main and prints
# "Everything up-to-date" while the commit never reaches the live site.
git push origin HEAD:main

# Never trust that silently. Confirm the commit is the remote tip.
LOCAL="$(git rev-parse HEAD)"
REMOTE="$(git ls-remote origin main | cut -f1)"
if [ "$LOCAL" != "$REMOTE" ]; then
  echo ""
  echo "FAILED: the commit did not reach main on the remote."
  echo "  local HEAD:  $LOCAL"
  echo "  remote main: $REMOTE"
  echo "The newsroom has NOT changed. Do not report this as published."
  exit 1
fi

echo ""
echo "Pushed and verified. main is now $LOCAL"
echo "GitHub Pages redeploys in ~1 minute; the live newsroom"
echo "updates within about 10 minutes (CDN cache)."
