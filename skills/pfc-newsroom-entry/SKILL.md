---
name: pfc-newsroom-entry
description: Publishes a finalized Pressed Fresh Collective press release directly to the PFC newsroom. Team members upload the final press release copy and its images (hero image, gallery images, streaming links, video links) in a Claude session, and this skill formats the entry, saves the images, validates, and pushes to the pfc-newsroom GitHub repo, which publishes the live site. Also handles fixes and updates to already-published releases. Trigger on "add this to the newsroom," "publish this press release," "update the newsroom," "fix the [artist] release," or any request to publish, correct, or take down a newsroom entry. Copy must be FINAL: this skill formats and publishes, it does not draft or edit press releases (use pfc-press-release for that) and does not check facts or brand voice (use citation-check and brand-check first). It flags and fixes em dashes, which house style forbids.
---

# PFC Newsroom Entry — direct publish

Turns a finished press release plus its assets into a published entry on the
PFC newsroom (pressedfreshcollective.com/newsroom). The GitHub repo
`pressedfreshcollective/pfc-newsroom` is the single source of truth: pushing
to `main` publishes the live site via GitHub Pages. Nobody ever edits
anything on Squarespace, and there is no Drive handoff folder anymore —
this session IS the publish pipeline.

## Before starting

1. **Confirm the copy is final.** If the release itself is still being
   drafted or edited, stop and point to the `pfc-press-release` skill.
   This skill publishes copy word for word; it never rewrites.
2. **Confirm repo access.** You need to be able to clone/pull and push
   `pressedfreshcollective/pfc-newsroom` and run its Python tools (a
   Claude Code session, or any session with the GitHub connector plus a
   shell). If you cannot, do NOT half-publish: build the entry JSON,
   show it, and tell the team member to re-run this in a Claude Code
   session or hand it to Dawn.
3. **Check for an embargo.** If the copy mentions an embargo or a "hold
   until" date in the future, STOP and tell the team member to come back
   and publish on that day. The repo is public the moment you push —
   there is no holding queue.

## What you need from the team member

**Required:**
- Final press release copy (doc upload or pasted text)
- Every image, with the main image named `hero` (or clearly identified);
  actual image files, not links to Drive/Slack previews
- **Music release date** — the date the single/EP/album goes live on
  streaming platforms. This drives the automatic Listen Now step (see
  below). For a performance recap or news item with no streaming
  release, there isn't one; skip the `listen` field entirely.
- **Artist name** as credited on streaming, for the `artist` field.
- **The exact track title**, for the `track` field. Take it from the
  release copy, where it is normally in quotation marks, and never from
  the headline. If the copy does not state it clearly, ASK. A `listen`
  entry without a correct `track` guarantees the release-day routine
  fails, silently, on release morning.
- **The artist's Spotify profile link**, for `spotifyArtistId`. Most
  releases already print it in the "Connect with" section, so look there
  before asking. Record only the 22-character id from the URL.

**Optional (include when available):**
- Spotify link, Apple Music link, YouTube link — if the music is
  ALREADY live on streaming, get the links now and build the buttons and
  player into the entry directly (see schema). The Listen Now routine is
  only for releases that are not out yet at publish time.
- Press contact if different from the default (Dawn Jones,
  dawn@pressedfreshpr.com)

Don't block on optional fields. Ask only when something required is
genuinely missing or ambiguous — and ask everything in ONE message, not
a drip of questions.

## Building the entry

Read `references/schema.md` FIRST — it is the exact live format: field
reference, every block type with real examples, the `listen` field
rules, Spotify share-link → embed-link conversion, image file rules.
The summary:

- `id`: `YYYYMMDDNN` — today's date plus a 2-digit counter within the
  day (`2026082001`, `2026082002`, …). Digits only, must be unique.
- `date`: ISO `YYYY-MM-DD`, the press release date.
- `lead`: the release's own opening/summary sentence. Never invent
  promotional language.
- `blocks`: the release body converted block by block, copy verbatim.
- `artist`, `track`, `spotifyArtistId`: required companions to
  `listen`. See schema.md. `track` is the song, `title` is the headline,
  and they are almost never the same string.
- `listen`: `{"releaseDate":"YYYY-MM-DD","status":"pending"}` when the
  music is not yet live on streaming. The release-day routine watches
  for this, finds the Spotify and Apple Music links on release morning,
  and adds the Listen Now button and player automatically. Omit the
  field when links are already in the entry or nothing is releasing.
- Images: save the actual files to `images/<id>/` (`hero.jpg`,
  `img-01.jpg`, `gallery-01.jpg`, …) and reference by relative path.
  NEVER embed base64 data URIs.

**House style:** no em dashes anywhere in post-migration entries.
Replace each with a comma, period, or hyphen as the sentence needs, and
report every swap. Change nothing else about the wording.

## Publishing

From the repo root (fresh clone or `git pull --rebase` first — the
Listen Now routine also pushes to this repo):

1. Prepend the entry to `pfc-newsroom-data.js` (newest first). Touch no
   other entry.
2. Save the images under `images/<id>/`.
3. `python3 tools/validate.py` — errors mean DO NOT PUSH. Fix and rerun
   until it prints "OK to publish".
4. `python3 tools/build_preview.py`
5. Commit as `Add release: <Artist> — <Title>` and push `main`
   (`./publish.sh "Add release: ..."` does 3–5 plus the pull in one
   step).
6. If Slack is available, post the live link in **#newsroom-queue** so
   the whole team sees it. Either way, give the team member:
   - Live: `https://pressedfreshcollective.com/newsroom#pfc-press=<id>`
   - Preview (updates in ~1 min): `https://pressedfreshcollective.github.io/pfc-newsroom/#pfc-press=<id>`
   - Note the live page can lag the push by up to 10 minutes (CDN).

## Fixing or updating a published release

Same pipeline, smaller change. Find the entry by artist/title in
`pfc-newsroom-data.js`, apply exactly the requested change, validate,
rebuild preview, commit (`Update release: <Artist> — <Title>: <what
changed>`), push. For a removal, delete the entry and its `images/<id>/`
folder. If it is ambiguous which release is meant, ask before touching
anything. Confirm back exactly what changed.

## Output to the team member

1. A one-line confirmation with the live and preview links.
2. Anything you inferred, guessed, or fixed (em dash swaps, image
   naming, missing fields) so it can be double-checked.
3. If the release is pre-release: confirm the `listen` field is set and
   say the Listen Now link will be added automatically on release
   morning (by around 7am Denver time) with a confirmation in
   #newsroom-queue.
