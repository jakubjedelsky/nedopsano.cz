# CONTEXT: nedopsano.cz

Created 2026-09-15, built out 2026-09-15 to 2026-09-17. This file is for
future agent sessions and for the site owner. Update it as things change.

## What this repo is

A site for Jakub's own poems, at `nedopsano.cz` (moved from `basne.stderr.cz` on 2026-09-23). Built with
[Pelican](https://getpelican.com), the same generator as the blog at
`stderr.cz`, and deliberately kept in that family: the colours are copied
from the blog's theme and the local tooling is the same.

Everything renders onto one page. One poem fills the screen, the neighbours
stay off it, and blur plus fade track the scroll so the poem you are on is
the only sharp thing. There is no JavaScript anywhere.

```
pelicanconf.py              local config, SITEURL = localhost
publishconf.py              production override, SITEURL = https://nedopsano.cz
build.sh                    html | clean | regenerate | serve  (copied from stderr.cz)
content/*.md                one poem per file, Pelican colon metadata
content/extra/CNAME         nedopsano.cz, copied to the output root
theme/templates/index.html  the only template
theme/static/css/style.css  the only stylesheet
.github/workflows/publish.yml   push to main → build → deploy to gh-pages
```

## Writing a poem

```
Title: Název básně
Slug: nazev-basne
Date: 2026-09-15

první řádek
druhý řádek

druhá strofa
```

One newline is a line break, a blank line starts a new stanza. Poems are
ordered newest first and each one is reachable at `nedopsano.cz/#slug`.

## Decisions and the reasons behind them

- **One page, anchors only.** `ARTICLE_SAVE_AS = ''` and
  `ARTICLE_URL = '#{slug}'`, `DIRECT_TEMPLATES = ['index']`,
  `DEFAULT_PAGINATION = False`. No page per poem, no archive, no tags.
- **`MARKDOWN` is overridden** to add `markdown.extensions.nl2br`, which is
  what keeps verse line breaks. Overriding `MARKDOWN` discards Pelican's
  defaults, so `markdown.extensions.meta` has to be listed again or
  metadata parsing breaks. Codehilite and `pygment.css` are both dropped —
  no code in poems, which also avoids the dark-mode gap the blog's
  `--code-bg`/`--code-fg` vars have.
- **Empty `*_SAVE_AS` rather than `rm -rf` in CI.** The blog's workflow
  deletes `author`/`category`/`tag`/`tags.html` after building; doing it in
  config is cheaper and the workflow here has no cleanup step.
- **One template, no `base.html`.** With a single page to render, a base
  template to extend would only be indirection.
- **Colours are the blog's, verbatim** — `--bg`, `--fg`, `--muted`,
  `--accent`, `--border` in both the light and `prefers-color-scheme: dark`
  blocks. Same system font stack, same `clamp()` body size.

## The scroll effect

`animation-timeline: view()` on `.poem` drives the blur and fade from the
poem's position in the viewport. `view()` runs from the element entering the
bottom of the viewport to leaving the top, so 50% of the timeline is dead
centre whatever the poem's height — that is the sharp point, and it means
the first poem at scroll 0 and the last at maximum scroll are both sharp
with no padding tricks.

Two arrows carry the affordance. `↓` bobs at the bottom centre and fades
over the last 15vh of the page; `↑` is hidden at the top and fades in over
the first 15vh. Both are driven by `animation-timeline: scroll(root block)`
and both are suppressed when there is only one poem.

Things that will bite whoever edits this next:

- **The `@supports` guards are load-bearing.** Without scroll-driven
  timelines, `animation: ... both` runs as a 0s animation and settles on its
  final keyframe: every poem would be permanently blurred and the down
  arrow permanently invisible. Keep the animations inside the guards, and
  keep `.hint-up { opacity: 0 }` in the unguarded base rule so browsers
  without support never offer to scroll up from the top of the page.
- **Fade ranges are fixed lengths, not percentages.** `15vh` rather than
  `12%`, so they behave the same with three poems as with thirty.
- **The reduced-motion override for the arrows is nested inside the
  `@supports` block** on purpose. Lifting it out would reintroduce the 0s
  animation problem above. It drops the bobbing and keeps the scroll-linked
  opacity, which is not motion.
- **`.poem p:last-of-type`, not `:last-child`** — the date footer is the
  last child now, and the closing stanza still needs its bottom margin
  dropped.

Two abandoned approaches, so they are not retried:

- **Scroll snapping.** `scroll-snap-type: y proximity` pulled the page back
  to the previous poem whenever the reader scrolled a little and stopped.
  Removed; the scroll now rests wherever it is left. `mandatory` would be
  worse, since it fights poems taller than the viewport.
- **Showing a slice of the next poem.** Tried at 80vh sections and then at
  auto-height poems 30vh apart. The first did nothing useful — a short poem
  centred in a fixed-height box leaves blank padding at both ends, so the
  visible slice of the next poem was that padding rather than its text. The
  second worked but the owner did not like the look. The arrows replaced it.

Knobs worth knowing: `blur(5px)` and the `35%`/`65%` plateau in `@keyframes
focus`, `min-height: 100vh` on `.poem`, and `bottom`/`top: 1.5rem`,
`font-size: 1.1rem`, the `1.8s` bob and the `15vh` ranges on `.hint`.

## Deploy

Push to `main` → `.github/workflows/publish.yml` builds with
`publishconf.py` and deploys `output/` to `gh-pages` via
`peaceiris/actions-gh-pages@v4`, same shape as the blog's workflow but
without its cleanup step. `content/extra/CNAME` lands at the output root.

Repo: `github.com/jakubjedelsky/nedopsano.cz`, created 2026-09-23 as
private. The free GitHub plan does not serve Pages from a private repo, so
Pages needs either a public repo or GitHub Pro. DNS is at Wedos: four `A`
records on the apex to GitHub Pages IPs, `www` CNAME to
`jakubjedelsky.github.io`. Enforce HTTPS after GitHub issues the
certificate. Commits in this repo use `jakub.jedelsky@gmail.com`.

## Local dev

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./build.sh html
./build.sh serve        # http://localhost:8000
./build.sh regenerate
```

`requirements.txt` is the blog's pinned set, Pelican 4.12.0 on Python 3.14.
`build.sh` calls `.venv/bin/pelican` directly, so no activation is needed.

## Notes for future agent sessions

- The blog repo at `/Users/j.jedelsky/Develop/personal/stderr.cz` is where
  the colours, tooling and workflow came from, and its own `CONTEXT.md`
  explains why the palette looks the way it does.
- `pelican -l`'s pretty-URL handling only overrides `do_GET`, so a
  `curl -I` HEAD request can 404 on a URL a browser loads fine. Use a plain
  `GET` to sanity-check. Not much of an issue here, since the site is one
  page.
- The whole design has only ever been verified by reading the generated
  HTML and CSS. No browser automation was available in the session that
  built it, so every visual judgement so far is the owner's.
