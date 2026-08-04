#!/bin/bash
# One-time GitHub setup. Run AFTER creating an empty public repo named
# "pfc-newsroom" on github.com (no README, no .gitignore).
# Usage: ./setup.sh <your-github-username>
set -euo pipefail
cd "$(dirname "$0")"

if [ $# -lt 1 ]; then
  echo "Usage: ./setup.sh <your-github-username>"
  exit 1
fi
USER="$1"
PAGES_URL="https://${USER}.github.io/pfc-newsroom"

# Point the Squarespace code block at the GitHub Pages data file
python3 - "$USER" <<'EOF'
import re, sys
user = sys.argv[1]
path = "newsroom-code-block.html"
s = open(path, encoding="utf-8").read()
s = re.sub(r"var DATA_URL = '[^']*';",
           f"var DATA_URL = 'https://{user}.github.io/pfc-newsroom/pfc-newsroom-data.js';",
           s, count=1)
open(path, "w", encoding="utf-8").write(s)
print(f"DATA_URL set to https://{user}.github.io/pfc-newsroom/pfc-newsroom-data.js")
EOF

python3 tools/validate.py
python3 tools/build_preview.py

git add -A
git commit -m "Configure GitHub Pages URL for ${USER}" || true
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/${USER}/pfc-newsroom.git"

echo ""
echo "Now push (you'll be asked to log in the first time - username is"
echo "${USER}, password is a Personal Access Token from"
echo "https://github.com/settings/tokens - macOS remembers it after that):"
echo ""
echo "  git push -u origin main"
echo ""
echo "Then on github.com: repo Settings -> Pages -> Source: 'Deploy from a"
echo "branch' -> Branch: main, folder / (root) -> Save."
echo ""
echo "A few minutes later your newsroom preview is live at:"
echo "  ${PAGES_URL}/"
echo "and the data file at:"
echo "  ${PAGES_URL}/pfc-newsroom-data.js"
