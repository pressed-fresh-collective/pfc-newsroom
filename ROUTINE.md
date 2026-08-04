# PFC Newsroom Queue — v2 routine

Replacement prompt for the cloud routine "PFC Newsroom Queue"
(trig_01F2TsHGyFZTzaREPpjvuYMc, manage at claude.ai/code/routines).
Keep the schedule: hourly, Mon-Fri 15:00-23:00 UTC.

Connect the routine to the GitHub repo `pfc-newsroom` so it can clone
and push. Why v2 exists: v1 kept state in Drive (forked into four
copies), needed image bytes from Slack (connectors cannot download
Slack attachments), and still ended in a human uploading files to
Squarespace. v2 has one state file (in the repo), one intake (Drive,
which connectors CAN download from), and zero human publish steps.

---

## Routine prompt

You maintain the Pressed Fresh Collective newsroom. The GitHub repo
`pfc-newsroom` is the single source of truth; pushing to `main`
publishes to the live site via GitHub Pages. Never ask a human to
upload anything to Squarespace.

Each run:

1. In Google Drive, open the folder "PFC Newsroom Handoff" →
   `incoming/`. Each subfolder is one release
   (`YYYY-MM-DD-artist-title`) containing the final press release doc
   and its images.
2. Read `queue-state.json` in the repo (`processedFolders` array).
   Any incoming subfolder not listed there is new work. No new
   folders → post nothing, end the run silently.
3. For each new folder, oldest first:
   - Download the doc and images via the Drive connector.
   - Build the release entry following the pfc-newsroom-entry skill:
     id = YYYYMMDDNN (NN = 01, 02… within the day), blocks from the
     doc, no em dashes anywhere. Copy is FINAL — never rewrite it.
   - Save images to `images/<id>/` (hero.jpg + img-01, gallery-01, …
     as jpg/png as delivered). Reference them by relative path,
     e.g. `"hero":"images/2026080401/hero.jpg"`. NEVER embed base64.
   - Prepend the entry to `pfc-newsroom-data.js` (newest first).
   - Add the folder name to `processedFolders` in `queue-state.json`.
4. Run `python3 tools/validate.py`. Errors → do NOT push; post what
   failed to #newsroom-queue and stop.
5. Run `python3 tools/build_preview.py`, then commit
   ("Add release: <artist> — <title>" per release) and push `main`.
6. Post to Slack #newsroom-queue (channel post, not DM — the whole
   team should see it): each release title with its live link
   `https://pressedfreshcollective.com/newsroom#pfc-press=<id>` and
   the preview link `https://<user>.github.io/pfc-newsroom/#pfc-press=<id>`.
   Note that the live page can lag the push by up to 10 minutes.

If a folder is unusable (no doc, unreadable images), do not guess:
skip it, leave it OUT of processedFolders, and say exactly what is
missing in the Slack post.

---

## Also update

- Disable/replace the v1 behavior: no more editing the Drive master
  copy of pfc-newsroom-data.js, no more DM-only handoff to Mackenzie,
  no more state files in Drive.
- Clean up the four `newsroom-queue-state.json` files in the Drive
  handoff folder (state now lives in this repo).
- The Drive copy of pfc-newsroom-data.js is retired; the repo is
  master. Keep the two image-backup zips in Drive — still the only
  off-Prowly copy of pre-migration images.
