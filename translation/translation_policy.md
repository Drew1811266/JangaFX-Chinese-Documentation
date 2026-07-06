# JangaFX HTML Translation Policy

## Chosen Framework

Use a local XLIFF-style protected text pipeline controlled by Codex:

1. Extract only visible text nodes from `jangafx-docs/**/*.html`.
2. Skip `script`, `style`, `code`, `pre`, `kbd`, `samp`, `svg`, math, and `notranslate` blocks.
3. Keep the original English mirror untouched.
4. Write translated output to `jangafx-docs-zh`.
5. Apply translations by byte-range replacement against the original HTML source.
6. Validate that the HTML tag sequence is unchanged and all local links/assets resolve. The only allowed tag-level change is setting the root `<html lang="en">` to `<html lang="zh-CN">` in translated output.

This is intentionally stricter than a normal DOM rewrite. The parser is used only to locate text ranges; it never serializes or reformats the page.

## Translation Rules

- Do not translate product names: JangaFX, EmberGen, LiquiGen, IlluGen, GeoGen, VectorayGen, Elemental Suite.
- Keep file formats, extensions, APIs, env vars, and code unchanged: VDB, OpenVDB, EXR, FBX, OBJ, ABC, Alembic, OGAWA, VAT, PNG, TGA, HDR, EXE, ZIP.
- Prefer established Chinese VFX/game-development terms from the glossary.
- Preserve UI labels when they refer to exact interface labels, and translate the descriptive word around them. Example: `Render` node -> `Render 节点`.
- Keep node names and parameter names in English when they are exact UI strings, unless the source is generic prose.
- Do not invent new product terms.
- Translate for technical clarity, not marketing flourish.
- Keep placeholder-like terms, keyboard shortcuts, numeric values, units, and frame rates unchanged.
- If a source segment is too fragmented by inline icons, translate it locally without changing the surrounding tags.

## Validation Gates

Before a page is considered complete:

- `python3 tools/jangafx_translate.py apply --page <path>`
- `python3 tools/jangafx_translate.py validate`
- Source and target tag sequences must match exactly after normalizing the root `<html lang>` value.
- Missing local links/assets must be zero.
- Spot-check the rendered page in a browser for layout regressions.
