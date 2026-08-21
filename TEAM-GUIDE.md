# PFC Newsroom: How to Publish and Update Press Releases

Publishing a press release is one conversation with Claude. You upload,
Claude publishes, done. Nobody logs into Squarespace, ever.

The repo `pressed-fresh-collective/pfc-newsroom` IS the newsroom.
Pushing to `main` publishes the live site.

---

## Before your first publish

You need two things set up once. Skip either and your session will fail
at the last step with a 403.

1. **A GitHub account added to the organization**, with write access to
   `pfc-newsroom`. Ask Dawn.
2. **The Claude app authorized for the organization on your account.**
   Go to `github.com/settings/applications`, find Claude, and under
   Organization access click **Grant** next to
   `pressed-fresh-collective`.

Being a repository collaborator is not enough on its own. Both steps
matter.

---

## Publishing a new press release

1. Open Claude and start a new chat, with a session connected to the
   `pfc-newsroom` repo. Bookmark it once and reuse it.
2. Upload the **final** press release document and **every image**, as
   actual files, with the main image named `hero` (hero.jpg or
   hero.png).
3. Say: **"Add this to the newsroom."** Include these four things:
   - **The music release date**, the day it goes live on streaming.
   - **The artist name** as they are credited on streaming.
   - **The exact track title.** Not the headline. The headline is a
     marketing line; the track is the song. "When the Anger Becomes the
     Healing" is a headline, "A Small Man's Pride" is the song.
   - **The artist's Spotify profile link.** Usually already in the
     release's own "Connect with" section.
   If the music is already out, paste the Spotify and Apple Music
   links instead of the release date.
4. Claude formats the entry, publishes it, posts the live link in
   **#newsroom-queue**, and gives you the link. The website shows it
   about 10 minutes later.

The copy must be final. Claude publishes it word for word and never
rewrites it. The one exception is em dashes, which house style forbids;
Claude swaps them and tells you about every swap. Still drafting? Ask
Claude to help with the press release first, then publish.

### Why those four things matter

On release morning a scheduled routine finds the song on Spotify and
Apple Music and adds the LISTEN NOW buttons and the player for you. It
can only do that if the entry says who the artist is and what the song
is called. For most of this year those fields did not exist, which is
why no Listen Now button ever appeared on its own. Give Claude the four
items above and the automation works.

---

## The Listen Now link

If the music is not out yet when you publish, you do not need to do
anything else. On release morning the routine adds the buttons and the
Spotify player and posts a confirmation in #newsroom-queue, normally by
7am Denver time.

If it cannot find the release, or cannot reach the platforms, it says so
in #newsroom-queue once and leaves the entry alone. It will never invent
a link. If you see that message, find the Spotify and Apple Music URLs
yourself and ask Claude in a chat to add them.

After a week with nothing found it marks the release stalled and asks
for help in the channel once.

---

## Fixing or updating a published release

Same as publishing: open a Claude chat and ask. Be specific about which
release you mean.

> Update the newsroom: on the Rob Carranza "Realign" release, the
> Spotify link should be [new link]

> Fix a typo in the Stephen Thomas release: "Woody Fest" should be
> "Woodie Fest"

> Take down the Hallie Marie release

Claude makes exactly the change, confirms exactly what it changed, and
the site updates about 10 minutes later. If it is not sure which release
you mean, it asks first. New or replacement images work the same way:
upload the file in the chat and say what to swap.

---

## Never edit the data file on github.com

`pfc-newsroom-data.js` holds all 365 press releases in a single line of
text, about 2.5 MB. GitHub's browser file editor cannot open a file that
size. It loads **completely blank**, showing "Enter file contents here",
while leaving the green **Commit changes** button active.

Committing from that screen replaces every press release with an empty
file and takes the live site down. It is recoverable from history, but
it turns an afternoon into an emergency. Never open that file with the
pencil icon. All changes go through a Claude session.

---

## Images: keep them web sized

Photos straight off a camera are often 20 MB or more, too large to move
through the connectors and too large for a web page. Before uploading,
save a web copy: JPEG, under about 3 MB. If a photo is rejected for
size, that is why.

---

## Embargoed releases

There is no holding queue, and publishing is public immediately. **Hold
embargoed releases yourself and publish them on the embargo day.** If
your document mentions a future embargo date, Claude will stop and
remind you rather than publish early.

---

## Please do not

- Edit anything on the Squarespace site. The newsroom updates itself,
  and editing the page can break it.
- Edit `pfc-newsroom-data.js` in the GitHub web editor. See above.
- Publish copy that is not final.
- Guess a track title. Ask.
- Assume something failed if the site has not changed yet. It takes
  about 10 minutes after Claude confirms.

## If something looks wrong

Tell Dawn. Every change is a recorded commit and reversible, so nothing
is ever lost or unfixable.
