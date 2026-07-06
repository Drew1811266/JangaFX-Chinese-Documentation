# Pause Checkpoint - Stage 6B

Date: 2026-07-06

Status: paused by user request.

## Goal

Complete the full Chinese translation of the local JangaFX HTML documentation with Codex-authored translations, glossary consistency, raw-preserving HTML output, and validation/audit after each stage.

## Current Stage

- Stage: 6, EmberGen and LiquiGen Node List pages
- Substage: 6B, LiquiGen Node List
- Current page: `liquigen/pages/references/node_list.html`
- Translation JSON: `translation/pages/liquigen_2Fpages_2Freferences_2Fnode_list.html.json`
- Output HTML: `jangafx-docs-zh/liquigen/pages/references/node_list.html`

## Current Counts

- LiquiGen Node List: 1021 / 2039 translated, `in_progress`
- EmberGen Node List: 739 / 4220 translated, `in_progress`

## Completed Since Stage 6 Start

- Stage 6A inventory and high-overlap migration pass.
- LiquiGen node-list manual batches:
  - Shape primitive and Appearance intro.
  - Collider, Drain, and Emitter through Velocity.
  - Force: Constant, Force: Shape, Force: Drag, Force: Turbulence, Force: Line, and Force: Toroidal.
  - Light: Directional, Light: Point, and Light: Area.
  - Whitewater main node through Appearance parameters.

## Resume Point

Continue at the first untranslated LiquiGen Node List segment:

- Segment index: 698
- Segment id: `3213907aa4dc`
- Source: `Whitewater Source`

The next node section to translate is `Whitewater Source`, followed by the remaining LiquiGen node-list sections.

## Validation

Latest command:

```bash
python3 tools/jangafx_translate.py validate
```

Latest result:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Speed Adjustment For Resume

The current raw-preserving workflow is correct but slow because the Node List pages contain thousands of short segments. On resume, use larger node-section batches:

1. Translate one complete node group at a time, not individual label fragments.
2. Keep HTML tags, emphasis wrappers, links, node names, parameter names, and UI labels protected in the JSON layer.
3. Apply and validate after each node group or after a small cluster of related node groups.
4. Spot-audit rendered visible text for the group before advancing.

This should improve throughput while keeping the same structural safety guarantees.
