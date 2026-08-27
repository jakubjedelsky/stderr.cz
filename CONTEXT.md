# CONTEXT: stderr.cz modernization

Audit date: 2026-08-07. This file is for future agent sessions and for the
site owner. It records the current state, the problems found, and the agreed
plan. Update it as steps are done.

## What this repo is

A personal blog built with [Pelican](https://getpelican.com) (static site
generator, Python). Content is Markdown in `content/`. A custom theme lives
in `theme/`. Output is committed to the `gh-pages` branch and served by
GitHub Pages at `stderr.cz`.

- `pelicanconf.py` — base config (used for local dev, `SITEURL` = localhost).
- `publishconf.py` — imports `pelicanconf.py`, overrides `SITEURL` to the
  real domain. Used for the production build.
- `build.sh` — wraps `pelican` CLI: `html`, `clean`, `regenerate`, `serve`,
  `publish`.
- `theme/` — custom theme based on **Bootstrap 2** (`bootstrap.min.css`,
  `bootstrap-responsive.min.css`). An abandoned `bootstrap3` branch exists
  in git remotes but was never merged.
- `output/` — build artifact, present in the repo working tree but ignored
  by git (`.gitignore`).

## Problems found (2026-08-07 audit)

1. ~~**Local dev environment is broken.**~~ **Fixed 2026-08-07.** `.venv` was
   built against Homebrew's Python 3.13, which Homebrew has since dropped in
   favor of 3.14, leaving `pelican` unable to run. Recreated `.venv` on the
   current Python 3.14.6 and reinstalled `pelican[markdown]` fresh.
2. ~~**`requirements.txt` is hard-pinned and stale.**~~ **Fixed 2026-08-07.**
   Regenerated from a clean install (`pip freeze`): `pelican==4.12.0`,
   `Jinja2==3.1.6`, `Markdown==3.10.3`, `MarkupSafe==3.0.3`,
   `Pygments==2.19.2`, plus transitive deps pulled in by Pelican 4.12
   (`rich`, `watchfiles`, `markdown-it-py`, `anyio`, `idna`, `mdurl`,
   `ordered-set`). `pytz` is gone — Pelican now uses stdlib `zoneinfo`, as
   suspected.
3. **No CI, publishing is manual.** `build.sh publish` clones a second copy
   of the repo to `~/.stderr.cz`, builds there with `publishconf.py`, and
   pushes `gh-pages` by hand. This is currently kept up to date — verified
   2026-08-07: the last `gh-pages` publish (`3c89fe9`, 2026-01-04 21:43:16)
   landed 21 seconds after the last `master` content commit (`a0fa1f6`,
   21:42:55), i.e. right after `build.sh publish` was run. So the site is
   **not** stale; the risk is that this depends on the owner remembering to
   run the script every time, with no safety net if they forget.
4. **Theme is on Bootstrap 2**, which is over a decade old and unmaintained.
   Not urgent (it still renders), but worth a look eventually.

## Decisions made (2026-08-07)

- **Scope for this pass: audit + this file only.** No code, config, or
  dependency changes made yet. The owner will act on the plan below at
  their own pace.
- **Publishing target: GitHub Actions**, replacing the manual
  `build.sh publish` step. On push to `master`, CI should build with
  Pelican (`publishconf.py`) and deploy the output to `gh-pages`
  automatically. This removes the "forgetting to publish" risk noted in
  problem #3, even though it hasn't actually bitten yet.
- Bootstrap 2 → newer CSS is explicitly **not urgent**, out of scope for now.

## Recommended plan

1. ~~**Fix the local dev environment + `requirements.txt`.**~~ **Done
   2026-08-07** — see "Local dev environment (fixed 2026-08-07)" below.
2. **Add a GitHub Actions workflow** (e.g. `.github/workflows/publish.yml`)
   that, on push to `master`:
   - sets up Python,
   - installs `requirements.txt`,
   - runs `pelican content -o output -s publishconf.py`,
   - deploys `output/` to `gh-pages` (e.g. via `peaceiris/actions-gh-pages`
     or `actions/deploy-pages`).
   Once this is green, `build.sh publish` and the `~/.stderr.cz` clone-based
   workflow can be retired — keep `build.sh html`/`serve`/`regenerate` for
   local preview only.
3. **New design.** Do this last, once #1 and #2 are boring and invisible —
   redesigning needs fast local preview and a publish step you don't have
   to think about. Covers retiring the Bootstrap 2 theme (finish the
   abandoned `bootstrap3` branch, or a fresh smaller CSS pass).

## Local dev environment (fixed 2026-08-07)

- `.venv` recreated on Python 3.14.6 (`python3 -m venv .venv`).
- `requirements.txt` regenerated via `pip freeze` after a clean
  `pip install 'pelican[markdown]'` — see problem #2 above for the version
  list. To redo this bump in future: recreate `.venv`, `pip install
  'pelican[markdown]'`, then `pip freeze > requirements.txt`.
- `./build.sh html` verified working: builds 70 articles + 1 page cleanly.
- `./build.sh serve` fixed, **twice**. First pass: it called
  `python -m pelican.server`, which Pelican 4.12 flags as deprecated, so it
  was swapped for stdlib `python -m http.server`. That broke pretty URLs —
  this site uses `ARTICLE_URL = '{slug}'` / `PAGE_URL = '{slug}'`
  (`pelicanconf.py`), i.e. links like `/o-mne` that map to `o-mne.html` on
  disk. Stdlib `http.server` has no extension-guessing, so every article/
  page link 404'd; only the exact-match `/` (`index.html`) worked. Pelican's
  own dev server (`pelican/server.py::ComplexHTTPRequestHandler`) *does*
  guess `.html`/`/index.html` suffixes — that's what pretty URLs need.
  Fixed properly by using `pelican -l -p 8000 -o $OUTPUTDIR -s $CONFFILE`
  (the current non-deprecated invocation) instead of either the old module
  call or stdlib. Verified `/`, `/o-mne`, `/archives`, `/feed.atom.xml`,
  `/tags.html` all return 200 via real `GET` requests.
  Caveat: `pelican -l`'s pretty-URL matching only overrides `do_GET`, not
  `do_HEAD` — a `curl -I`/HEAD request to `/o-mne` still 404s even though
  a real browser `GET` works fine. That's an upstream Pelican quirk, not a
  bug in this repo; don't use `curl -I` to sanity-check pretty URLs here,
  use a plain `GET`.
- `build.sh` fixed to not depend on venv activation: it used
  `PY=$(which python3)` / `PELICAN="pelican"`, which only resolve if the
  venv is on `PATH` — so `./build.sh serve` failed with
  `pelican: command not found` for anyone who didn't manually
  `source .venv/bin/activate` first (this bit the owner immediately; the
  earlier verification here had always activated first and missed it).
  Now `PY`/`PELICAN` point at `$BASEDIR/.venv/bin/python3` and
  `$BASEDIR/.venv/bin/pelican` directly, and `BASEDIR` is derived from the
  script's own location (`dirname "$0"`) instead of `$(pwd)`, so it also
  works when invoked from another directory. Verified in a stripped shell
  (`env -i PATH="/usr/bin:/bin"`, no venv activation) that
  `clean`/`html`/`serve` all work and pretty URLs return 200.
- Usage: just `./build.sh html|clean|regenerate|serve` — no activation
  step needed any more. (`source .venv/bin/activate` still works too, if
  you want `pelican`/`pip` directly on `PATH` for other tasks.)

## Notes for future agent sessions

- Don't assume `.venv` works — check it (`.venv/bin/pelican --version`)
  before relying on it; Homebrew Python versions drift and can break it
  silently, as happened here.
- `pip index versions <pkg>` (no install needed) is a fast way to check
  what's current on PyPI before touching `requirements.txt`.
- **`gh-pages` is an orphan branch** (build output only, no shared history
  with `master`). `git log master ^origin/gh-pages` does **not** tell you
  what's unpublished — it just lists master's entire history, since the two
  branches share no ancestry. That produced a false "site is 2 years stale"
  finding in an earlier pass here. To check if the site is current, compare
  the timestamp of the latest `gh-pages` commit against the latest relevant
  `master` commit instead — and always `git fetch origin gh-pages` first,
  since the local ref goes stale.
