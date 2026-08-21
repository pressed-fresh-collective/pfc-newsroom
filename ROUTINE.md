# PFC Listen Now Watch

The one scheduled routine. It adds streaming links to newsroom entries
on release morning. It never writes or edits press release copy.

- **Task name:** Release Day PR Updates - Newsroom
- **Repo:** `pressed-fresh-collective/pfc-newsroom`
- **Schedule:** `0 12-18 * * *` (UTC), which is 06:00 to 12:00
  America/Denver while Denver is on MDT.
- **Connected:** the repo (clone and push), Slack (posts to
  #newsroom-queue)

The routine's prompt lives in the task itself, not in this file. This
file explains the setup around it. **When the prompt changes, update
this file too.** Drift between the two has already cost the team a
morning.

## What it depends on

It fails, quietly or loudly, without all of these:

1. **`artist` and `track` on the entry.** The routine searches streaming
   platforms for a song. `title` is the press release headline, not the
   song name, so it cannot be used. Entries with a `listen` field and no
   `artist` or `track` now fail validation, on purpose.
2. **`spotifyArtistId` on the entry**, strongly recommended. It anchors
   the search to the right artist. Without it the routine searches by
   name and can hit an unrelated act. A Spotify profile called
   "Carranza" is a Latin world-music act with no connection to the
   Houston rock artist Rob Carranza.
3. **Push straight to `main`.** The live site publishes from `main`
   only. If the task is configured to work on a `claude/*` branch and
   open a pull request, the links land somewhere nobody merges at 6am
   and the release day passes with no button. Check this in the task's
   repository configuration.
4. **Network access to the streaming platforms.** The routine cannot
   verify a release it cannot load. If `open.spotify.com`,
   `music.apple.com`, `api.spotify.com` or `itunes.apple.com` are
   blocked by the organization's network policy, every run reports the
   block and changes nothing. That setting is in the Claude
   organization settings, under Capabilities, Code execution.
5. **The task being enabled.** It gets switched off during migrations
   and repo moves. Switch it back on.

## Daylight saving

The cron is UTC, so the local window shifts twice a year.

- MDT, roughly March to November: `0 12-18 * * *` gives 06:00 to 12:00
  Denver.
- MST, roughly November to March: use `0 13-19 * * *`.

Change it when the clocks change, or the routine drifts an hour early.

## How it reports

- Success: one Slack post per release, with the links it found and the
  newsroom URL, noting any platform it could not find.
- Failure: one Slack post naming the release and the reason, and
  stating that the newsroom has NOT changed. It checks the channel
  before posting so seven runs in a morning cannot produce seven
  identical messages.
- Nothing pending: it ends silently. No post, no commit.

## Optional: streaming APIs instead of page reads

The routine prefers the platform APIs when it can reach them, because
they return the artist and track as separate fields and turn a judgement
call into an exact comparison.

- **Apple Music** needs no credentials. The iTunes Search API at
  `itunes.apple.com/search?term=...&entity=song` returns `artistName`,
  `trackName` and `trackViewUrl` as JSON.
- **Spotify** needs a free developer app. Create one, then store its
  client id and secret as environment secrets named
  `SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET`. Without them the
  routine falls back to reading `open.spotify.com` pages, anchored by
  `spotifyArtistId`.

Note that API calls run through the shell and are therefore subject to
the network policy in point 4. Page reads through the fetch tool are
not.

## History

Earlier versions of this routine watched a Slack channel and a Drive
folder for publish requests. Both are retired. All publishing is direct
team sessions now, per TEAM-GUIDE.md. `queue-state.json` is a leftover
from that era; nothing reads it.
