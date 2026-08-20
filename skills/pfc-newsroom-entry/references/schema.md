# PFC newsroom entry schema (live format)

The data file is `pfc-newsroom-data.js` at the repo root:

```
window.PFC_RELEASES=[ {entry}, {entry}, ... ];
```

One line, valid JSON after the `window.PFC_RELEASES=` prefix, entries
newest first. `tools/validate.py` enforces most of what follows — run it
before every push.

## Top-level fields

```json
{
  "id": "2026082001",
  "title": "Artist Name Releases Debut Single 'Song Title'",
  "date": "2026-08-20",
  "lead": "One-sentence summary drawn from the release's own opening.",
  "hero": "images/2026082001/hero.jpg",
  "listen": {"releaseDate": "2026-09-12", "status": "pending"},
  "contact": {"name": "Dawn Jones", "role": "", "email": "dawn@pressedfreshpr.com", "phone": ""},
  "blocks": [ ... ]
}
```

- `id` — digits only, `YYYYMMDD` + 2-digit counter within that day
  (`01`, `02`, …). Must be unique across the whole file.
- `date` — ISO `YYYY-MM-DD`, the press release date (not the music
  release date). Entries must stay in newest-first order.
- `lead` — plain text, no HTML. Also repeated as the first block.
- `hero` — repo-relative path. The file must exist. No base64, ever.
- `listen` — OPTIONAL, see "The listen field" below.
- `contact` — defaults to Dawn unless the release names someone else.

## The `listen` field

Only for entries whose music is **not yet live on streaming** at
publish time:

```json
"listen": {"releaseDate": "2026-09-12", "status": "pending"}
```

- `releaseDate` — ISO date the single/EP/album drops on streaming.
- `status` — `"pending"` when written by this skill. The release-day
  routine flips it to `"linked"` (with `spotify`, `apple`, and
  `linkedOn` fields) after it finds the release and inserts the Listen
  Now blocks. `"stalled"` means the routine could not find it within a
  week and asked the team for help; `"skipped"` means a human decided
  no link is coming.

Do NOT add `listen` when:
- the streaming links are already known — build the buttons and player
  into `blocks` directly (shapes below) and leave `listen` out, or
- the entry is a recap/news item with nothing releasing.

## Block types (real shapes from the live file)

Every block has `"t"`. HTML strings may contain `<strong>`, `<em>`,
`<a href target="_blank" rel="noopener">`, `<br>`.

```json
{"t": "lead", "html": "Same sentence as the top-level lead."}
{"t": "p", "html": "<strong>CITY, ST</strong> (Month D, YYYY) - Body paragraph, copied verbatim."}
{"t": "h3", "html": "About Artist Name:"}
{"t": "quote", "html": "The pulled quote itself.", "cite": "- Artist Name"}
{"t": "img", "src": "images/2026082001/img-01.jpg", "alt": "Descriptive alt text"}
{"t": "caption", "html": "Images by Photographer Name"}
{"t": "gallery", "items": [{"full": "images/2026082001/gallery-01.jpg", "thumb": "images/2026082001/gallery-01.jpg", "alt": "Alt text"}]}
{"t": "button", "href": "https://open.spotify.com/track/...", "label": "LISTEN ON SPOTIFY", "color": "#614DFF"}
{"t": "embed", "src": "https://open.spotify.com/embed/track/...?utm_source=generator", "height": "352"}
{"t": "linkcard", "href": "https://example.com/", "img": "https://.../preview.jpg", "title": "Page title", "desc": "Short description"}
{"t": "list", "items": ["Vocals: Name", "Produced by: Name"]}
{"t": "instagram", "href": "https://www.instagram.com/handle/", "handle": "@handle", "post": false}
{"t": "tiktok", "href": "https://www.tiktok.com/@handle/video/123", "handle": "@handle"}
{"t": "hr"}
```

Typical block order: `lead`, body `p`s (dateline bolded in the first
one), `quote`s where the release has them, images/gallery where they
sit in the doc, then `hr`, `h3` "About ..." boilerplate sections, and a
final `hr`.

## Streaming link conversion (easy to get wrong)

Share link and embed link use different paths:

- Share: `https://open.spotify.com/track/4LvFXEimQgTJYHhByRSCls?si=...`
- Embed: `https://open.spotify.com/embed/track/4LvFXEimQgTJYHhByRSCls?utm_source=generator`

Insert `embed/` after the domain, drop the `?si=` param, add
`?utm_source=generator`. Works the same for `album` and `artist` paths.
A single uses `track/`; an EP or album uses `album/`.

The standard Listen Now set, inserted **before the first `hr` block**
(or appended at the end if there is none):

```json
{"t": "button", "href": "<spotify share url>", "label": "LISTEN ON SPOTIFY", "color": "#614DFF"},
{"t": "button", "href": "<apple music url>", "label": "LISTEN ON APPLE MUSIC", "color": "#614DFF"},
{"t": "embed", "src": "<spotify embed url>", "height": "352"}
```

YouTube embeds use `https://www.youtube.com/embed/<video-id>` as the
`src` with `"height": "315"`.

## Image files

- Directory: `images/<id>/` — `hero.jpg` (or `.png`), then `img-01`,
  `gallery-01`, … in delivery order, keeping the delivered format.
- Reference by relative path only. `validate.py` errors on missing
  files and on any `data:` URI.
- Pre-migration entries (before 2026-07-29) hot-link Prowly S3 URLs —
  leave those alone.

## House style

- **No em dashes** in any entry dated 2026-07-29 or later — title,
  lead, blocks, alt text, anywhere. Replace with comma, period, or
  hyphen; report each swap.
- Copy is verbatim. Formatting into blocks is your job; wording is not.
