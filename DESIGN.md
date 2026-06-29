# Design System — standefer.com

## Product Context
- **What this is:** Personal website for Robert Standefer — a paragraph intro, open-source projects, LinkedIn, and email contact. Not info-dense.
- **Who it's for:** People who want to know who Robert is and walk away feeling he's charming, wicked smart, and creative.
- **Space/industry:** Technologist / creative personal sites. Peers: leerob.io (ultra-minimal text), brittg.com (playful personal), rauno.me, paco.me.
- **Project type:** Single-page personal/marketing site.
- **Memorable thing:** "Super smart, super creative — and I want to know him." Every decision serves intellect + creativity + magnetism.

## Aesthetic Direction
- **Direction:** Industrial/editorial hybrid — "engineered but personable."
- **Decoration level:** Intentional — film grain so flat dark never reads as a template; asymmetric editorial pacing; one signature microinteraction.
- **Mood:** Confident and technical, but warm. Smart enough to signal intellect, human enough to invite connection. Not minimal-bland, not toy-playful.
- **Reference sites:** leerob.io, brittg.com, rauno.me

## Typography
- **Display/Hero:** Archivo (700–900) — grotesk that reads engineered and assured.
- **Body:** Archivo (400–500) — single family keeps it coherent.
- **UI/Labels:** JetBrains Mono — labels, meta, kickers. The "builder" signal.
- **Data/Tables:** JetBrains Mono (tabular-nums) — rare on this site.
- **Code:** JetBrains Mono.
- **Loading:** Google Fonts — `Archivo:wght@400;500;600;700;800;900` + `JetBrains+Mono:wght@400;500;700`.
- **Scale:** hero clamp(3rem,9vw,6.5rem)/0.94/-0.03em; h2-tag 0.72rem mono uppercase; body 17px/1.6; lead 1.18rem.

## Color
- **Approach:** Restrained — one saturated accent, cool neutrals, color is rare and meaningful.
- **Primary:** `#6A30FE` electric violet — accent only (links, kicker, primary CTA, selection). Never a gradient.
- **Secondary:** none — drop the pink; the single accent carries the brand.
- **Neutrals:** bg `#1C1C1F`, bg-2 `#27272B`, panel `#2F2F34`, paper `#DFDCDF`, paper-dim 74%, paper-faint 50%, line 16%.
- **Semantic:** success `#07f57b`, warning `#FB89CC`, error `#ff5a5a`, info `#6A30FE`.
- **Dark mode:** dark is default; light flips to paper `#f3f1ef` / ink `#1c1c1f`, accent unchanged.

## Spacing
- **Base unit:** 8px
- **Density:** comfortable
- **Scale:** 2xs(2) xs(4) sm(8) md(16) lg(24) xl(32) 2xl(48) 3xl(64)

## Layout
- **Approach:** Creative-editorial — asymmetric, name-as-poster hero, projects as a structured hover list (never a 3-col icon grid).
- **Grid:** single column, max content 1080px.
- **Max content width:** 1080px (gutters 2rem).
- **Border radius:** sm:5px, md:6px, lg:8px, none on text blocks.

## Motion
- **Approach:** Intentional — subtle entrance, one signature interaction (list rows nudge + go violet on hover).
- **Easing:** enter(ease-out) exit(ease-in) move(ease-in-out)
- **Duration:** micro 50–100ms, short 150–250ms, medium 250–400ms.

## Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-06-28 | Initial design system created | /design-consultation. Engineered-but-personable to land "smart + creative + want to know him." |
| 2026-06-28 | Single violet accent #6A30FE, drop pink | One saturated accent on cool neutrals; avoids AI-slop multi-tone gradient. |
| 2026-06-28 | Archivo + JetBrains Mono | Grotesk + mono = intellect + builder credibility; matches existing stack. |
