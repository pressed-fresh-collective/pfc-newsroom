# PFC Newsroom: How to Publish and Update Press Releases

Our newsroom on pressedfreshcollective.com now updates itself. Nobody
logs into Squarespace, nobody uploads files to the website, and nobody
waits on a handoff. Here is everything you need to know.

The newsroom robot checks for new work every hour, Monday to Friday,
9am to 5pm Denver time.

## Publishing a new press release

1. Open the Google Drive folder **PFC Newsroom Handoff > incoming**
2. Create one folder for the release, named with the date first:
   `2026-08-10-artist-name-song-title`
3. Put two things in it:
   - The final press release document (copy must be final; the robot
     publishes it word for word and never rewrites)
   - Every image, with the main image named `hero` (hero.jpg or
     hero.png)
4. Done. Within the hour, the robot formats it, publishes it, and
   posts the link in **#newsroom-queue** so everyone knows it is live.

The release appears on the website about 10 minutes after the robot
posts the link.

If something is missing (no final copy, no hero image), the robot will
not publish. Instead it posts in #newsroom-queue telling you exactly
what it needs. After you fix the folder, rename it with `-v2` on the
end so the robot looks at it again.

**Embargoed releases:** just mention the embargo date in the document.
The robot holds the release and publishes it automatically once the
date arrives.

## Fixing or updating a published release

**For any text change, just ask in #newsroom-queue.** Start your
message with UPDATE (or FIX, CHANGE, REMOVE) and name the artist or
release. Examples:

> UPDATE: Rob Carranza "Money" release, the Spotify link should be
> [new link]

> FIX: typo in the Stephen Thomas release, "Woody Fest" should be
> "Woodie Fest"

> REMOVE: take down the Hallie Marie release

The robot applies the change, replies in your thread confirming
exactly what it changed, and the site updates about 10 minutes later.
If it is not sure which release you mean, it will ask in the thread
before touching anything.

**For a new or replacement image**, Slack cannot deliver the file to
the robot, so use Drive: drop a folder in **incoming** named
`artist-title-update-2026-08-10` containing the new image(s) and a
short note saying what to swap. The robot handles the rest.

## Please do not

- Edit anything on the Squarespace site. The newsroom updates itself;
  editing the page can break it.
- Edit or replace files in the PFC Newsroom Handoff folder outside of
  the incoming folder.
- Assume something failed if the site has not changed yet. The robot
  runs hourly and the site takes about 10 minutes to refresh after it
  confirms in Slack.

## If something looks wrong

Tell Dawn. Every change the robot makes is recorded and reversible, so
nothing is ever lost or unfixable.
