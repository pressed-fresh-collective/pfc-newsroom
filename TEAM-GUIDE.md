# PFC Newsroom: How to Publish and Update Press Releases

Publishing a press release is now one conversation with Claude. There is
no more Drive handoff folder, no more hourly robot, and no waiting — you
upload, Claude publishes, done. Nobody logs into Squarespace, ever.

## Publishing a new press release

1. Open Claude in our team workspace and start a new chat (a Claude
   Code session connected to the `pfc-newsroom` repo is the reliable
   way — bookmark it once and reuse it).
2. Upload the **final** press release document and **every image** —
   the actual files, with the main image named `hero` (hero.jpg or
   hero.png).
3. Say: **"Add this to the newsroom."** Include one thing in your
   message: **the music release date** — the day the single/EP/album
   goes live on streaming. If the music is already out, paste the
   Spotify and Apple Music links instead.
4. Claude formats the entry, publishes it, posts the live link in
   **#newsroom-queue**, and gives you the link directly. The website
   shows it about 10 minutes later.

The copy must be final. Claude publishes it word for word and never
rewrites it (the one exception: em dashes get swapped out, house
style — Claude will tell you about every swap). Still drafting? Ask
Claude to help with the press release first, then publish.

## The Listen Now link (automatic)

If the music isn't out yet when you publish, you don't need to do
anything. On release morning, a scheduled Claude task finds the release
on Spotify and Apple Music, adds the LISTEN NOW buttons and the Spotify
player to the press release, and posts a confirmation in
#newsroom-queue — usually by 7am Denver time. If it can't find the
release after a few days, it asks for help in #newsroom-queue; just
reply-thread the correct link and ask Claude in a chat to add it.

## Fixing or updating a published release

Same as publishing: open a Claude chat and ask. Be specific about which
release you mean:

> Update the newsroom: on the Rob Carranza "Money" release, the Spotify
> link should be [new link]

> Fix a typo in the Stephen Thomas release: "Woody Fest" should be
> "Woodie Fest"

> Take down the Hallie Marie release

Claude makes exactly the change, confirms exactly what it changed, and
the site updates about 10 minutes later. If it isn't sure which release
you mean, it asks first. New or replacement images work the same way —
upload the file in the chat and say what to swap.

Note: posting UPDATE/FIX messages in #newsroom-queue no longer
publishes anything — the robot that watched that channel is retired.
The channel is still where publish confirmations land, so keep an eye
on it.

## Embargoed releases

There is no holding queue anymore, and publishing is public
immediately. **Hold embargoed releases yourself and publish them on the
embargo day.** If your document mentions a future embargo date, Claude
will stop and remind you rather than publish early.

## Please do not

- Edit anything on the Squarespace site. The newsroom updates itself;
  editing the page can break it.
- Publish copy that isn't final.
- Assume something failed if the site hasn't changed yet — it takes
  about 10 minutes after Claude confirms.

## If something looks wrong

Tell Dawn. Every change is a recorded commit and reversible, so nothing
is ever lost or unfixable.
