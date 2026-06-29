# Copilot instructions — standefer.com

Personal website for Robert Standefer, served as a static GitHub Pages site at the
custom domain in `CNAME` (standefer.com). There is **no build system, package
manager, framework, or test suite** — files are hand-authored and pushed straight to
the default branch, which GitHub Pages serves directly.

## Working in this repo

- Preview by opening `index.html` in a browser, or run a static server from the repo
  root (e.g. `python3 -m http.server`) and visit `http://localhost:8000`.
- Deploy = commit to the default branch and push. No CI step.
- Do not add a bundler, dependencies, or test tooling without explicit approval; the
  whole point is a self-contained handwritten site.

## Architecture

- `index.html` — the entire homepage: HTML, all CSS in one `<style>` block, and all JS
  in inline `<script>` at the bottom. CSS custom properties (`:root`) define the design
  tokens; sections are nav / hero / projects / contact / footer.
- `agent-platform-comic/` — standalone sub-page (`index.html`, `about.html`) with its
  own self-contained styles; not wired to the homepage's design tokens.
- `images/` — static assets (e.g. `images/comic/`).
- `params.json` — legacy GitHub Pages generator metadata; safe to ignore.
- `base prompt.md` — the original brief used to generate the site (project goals,
  required links, candidate color palettes). Useful for intent, not for editing.

## Conventions

- **Read `DESIGN.md` before any visual/UI change** — fonts, colors, spacing, layout,
  and motion are defined there and changes need explicit user approval (see `CLAUDE.md`).
- Site identity: Archivo (display/body) + JetBrains Mono (labels/meta), single violet
  accent `#6A30FE` on cool-neutral dark, film-grain overlay so flat color avoids a
  template look. Avoid AI-slop gradients/multi-tone palettes.
- CSS token names in `index.html` are legacy from an earlier palette (`--green`,
  `--yellow` both currently map to violet/pink) — change the value, not every consumer.
- JS is progressive enhancement: scroll reveals and the canvas node-grid degrade
  gracefully and respect `prefers-reduced-motion`. Keep new JS optional, not required.
- Keep everything in-file (inline CSS/JS) rather than splitting into asset files.
