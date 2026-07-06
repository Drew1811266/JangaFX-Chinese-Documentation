# JangaFX Translation Stage Plan

Long-term goal: complete the Chinese translation of the local JangaFX HTML documentation with Codex-authored translations, glossary consistency, and raw-preserving HTML output.

## Stage Gate

Each stage must pass all checks before moving on:

1. All target pages in the stage have no untranslated prose segments except protected names and exact UI labels.
2. Exact product names, node names, parameter names, file formats, code identifiers, URLs, and environment variables remain protected.
3. Technical terms follow `translation/glossary.zh-CN.md`.
4. Output is regenerated with `python3 tools/jangafx_translate.py apply`.
5. Structural validation passes with `python3 tools/jangafx_translate.py validate`.
6. A manual spot audit checks at least one representative section per translated page for natural Chinese and UI-label safety.

## Stages

| Stage | Scope | Status |
| --- | --- | --- |
| 0 | Infrastructure, glossary, policy, extraction/apply/validate tooling | Complete |
| 1 | Homepage, product landing pages, FAQ pages, shared navigation/UI copy | Complete |
| 2 | EmberGen and LiquiGen Getting Started pages | Complete |
| 3 | How-To Guides shared between EmberGen and LiquiGen | Complete |
| 4 | UI Reference and Settings pages | Complete |
| 5 | LiquiGen-specific reference/specific pages | Complete |
| 6 | EmberGen and LiquiGen Node List pages | Complete |
| 7 | Licensing guide, search/index polish, full cross-page terminology audit | Complete |
| 8 | Final validation, visual spot checks, delivery summary | Complete |

## Current Stage

All stages are complete:

Stage 3: How-To Guides batches are complete:

- 3A: How-To Guides index, comments, notes, palettes, range sliders - Complete
- 3B: color guides, including EmberGen color mapping and LiquiGen gradient presets - Complete
- 3C: camera import, import animation, keyframe animation - Complete
- 3D: modulation curve, modulating parameters, randomization - Complete
- 3E: render pass mapping plus EmberGen `histogram` / `exportVDB` - Complete
- 3F: LiquiGen `diagnostics` / `expressions` - Complete

Stage 4: translate and audit references, UI reference, and settings pages in small batches:

- 4A: EmberGen and LiquiGen references index pages - Complete
- 4B: EmberGen settings page - Complete
- 4C: LiquiGen settings page - Complete
- 4D: EmberGen UI reference page - Complete
- 4E: LiquiGen UI reference page - Complete

Stage 5: translate and audit LiquiGen-specific reference/specific pages in small batches:

- 5A: high-overlap specific pages with already translated How-To Guide counterparts - Complete
- 5B: remaining LiquiGen-specific simulation/reference pages - Not needed; all `specific` pages were covered by 5A

Stage 6: translate and audit EmberGen and LiquiGen Node List pages in batches:

- 6A: inventory and high-overlap migration pass - Complete
- 6B: LiquiGen node-list pages - Complete
- 6C: EmberGen node-list pages - Complete

Stage 7: licensing guide, search/index polish, and full cross-page terminology audit - Complete

Stage 8: final validation, visual spot checks, and delivery summary - Complete

Special rules for Stage 3 and Stage 4:

- Keep exact UI node/parameter labels in English when wrapped by emphasis or used as click targets.
- Translate conceptual prose around UI labels into Chinese.
- Use `体素`, `体素网格`, `边界框`, `模拟域`, `发射器`, `碰撞体`, `白水粒子`, `泡沫`, `飞溅`, `气泡` according to the glossary.
- Reuse shared EmberGen/LiquiGen How-To Guide translations only when the source prose is semantically identical.
