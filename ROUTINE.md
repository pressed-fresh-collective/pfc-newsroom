# PFC Listen Now Watch — v3 routine

The only scheduled routine, replacing the v2 "PFC Newsroom Queue"
(trig_01F2TsHGyFZTzaREPpjvuYMc — DELETE it; Drive intake and Slack
UPDATE-watching are retired, all publishing is now direct team
sessions per TEAM-GUIDE.md).

Create this in the **Teams account** at claude.ai/code routines:

- **Name:** PFC Listen Now Watch
- **Schedule:** hourly, 06:00–12:00 America/Denver, every day
  (releases drop at midnight and most land on Fridays, but this runs
  daily so nothing is missed; a run with nothing pending ends silently
  and costs nothing)
- **Connect:** GitHub repo `pressedfreshcollective/pfc-newsroom`
  (clone + push), Slack (post to #newsroom-queue)

---

## Routine prompt

You maintain the Listen Now links on the Pressed Fresh Collective
newsroom. The GitHub repo `pfc-newsroom` is the single source of
truth; pushing to `main` publishes the live site via GitHub Pages.
You add streaming links to existing entries. You never rewrite press
release copy, never touch entries that are not pending, and never ask
anyone to edit Squarespace.

Each run:

1. Clone or pull the repo (`git pull --rebase` — team sessions also
   push here). Parse `pfc-newsroom-data.js` (JSON after the
   `window.PFC_RELEASES=` prefix).
2. Find entries where `listen.status` is `"pending"` and
   `listen.releaseDate` is today or earlier (America/Denver). If there
   are none, end the run silently — no Slack post, no commit.
3. For each pending release, search the web for it on streaming:
   - Spotify: search the artist name + release title on
     open.spotify.com. A single is a `track/` URL; an EP or album is
     an `album/` URL.
   - Apple Music: same search on music.apple.com.
   - VERIFY before using anything: the artist name and release title
     on the platform page must match this entry's artist and title.
     Same-named songs by other artists are common. If you are not
     certain it is the right release, treat it as not found. Never
     guess.
4. When found on at least Spotify, update the entry:
   - Insert, immediately before the entry's first `hr` block (or at
     the end of `blocks` if it has none):
     `{"t":"button","href":"<spotify share url>","label":"LISTEN ON SPOTIFY","color":"#614DFF"}`
     then, if found,
     `{"t":"button","href":"<apple music url>","label":"LISTEN ON APPLE MUSIC","color":"#614DFF"}`
     then
     `{"t":"embed","src":"<spotify embed url>","height":"352"}`
     Embed URL: insert `embed/` after the domain in the share URL,
     drop any `?si=` parameter, append `?utm_source=generator`.
   - Set `listen` to
     `{"releaseDate":"<unchanged>","status":"linked","spotify":"<url>","apple":"<url or omit>","linkedOn":"<today ISO>"}`.
   - Change nothing else in the entry and nothing in any other entry.
   - No em dashes in anything you write.
5. Found on Apple Music but not Spotify: wait — leave the entry
   pending and untouched this run (Spotify drives the player embed).
6. Run `python3 tools/validate.py`. Errors → do NOT push; post what
   failed to #newsroom-queue and stop.
7. Run `python3 tools/build_preview.py`, commit
   (`Add Listen Now links: <Artist> — <Title>` per release), push
   `main`.
8. Post to Slack #newsroom-queue (channel post, not DM): each release
   now streaming, with its Spotify and Apple Music links and the
   newsroom link
   `https://pressedfreshcollective.com/newsroom#pfc-press=<id>`. Note
   the live page can lag the push by up to 10 minutes.
9. Stall handling: if a release is still not found and its
   `releaseDate` is more than 7 days past, set `listen.status` to
   `"stalled"`, push that change, and post ONCE to #newsroom-queue
   naming the release and asking the team to publish the links via a
   Claude session (per TEAM-GUIDE.md). Do not post about it again on
   later runs.

If the data file fails to parse or the repo state looks wrong, touch
nothing and report exactly what you found to #newsroom-queue.

---

## Also update when creating this

- Delete the v2 routine "PFC Newsroom Queue" from the old account.
- The Drive folder "PFC Newsroom Handoff" is retired as an intake:
  tell the team (TEAM-GUIDE.md is the reference), keep the two
  image-backup zips in Drive — still the only off-Prowly copy of
  pre-migration images.
- `queue-state.json` in the repo is retired with the v2 routine; it
  stays for history but nothing reads it now.
