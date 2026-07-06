# Stage 5A Audit - LiquiGen Specific Reference Pages

Date: 2026-07-06

## Scope

- `liquigen/pages/references/specific/animation.html`
- `liquigen/pages/references/specific/camera_import.html`
- `liquigen/pages/references/specific/color.html`
- `liquigen/pages/references/specific/comment.html`
- `liquigen/pages/references/specific/expressions.html`
- `liquigen/pages/references/specific/import_animation.html`
- `liquigen/pages/references/specific/modulating_parameters.html`
- `liquigen/pages/references/specific/modulation_curve.html`
- `liquigen/pages/references/specific/note.html`
- `liquigen/pages/references/specific/randomization.html`
- `liquigen/pages/references/specific/rangeSlider.html`
- `liquigen/pages/references/specific/render_passes_mapping.html`

## Translation State

All 12 pages are `translated` with full segment coverage:

- `animation.html`: 280 / 280
- `camera_import.html`: 94 / 94
- `color.html`: 246 / 246
- `comment.html`: 105 / 105
- `expressions.html`: 101 / 101
- `import_animation.html`: 96 / 96
- `modulating_parameters.html`: 205 / 205
- `modulation_curve.html`: 319 / 319
- `note.html`: 98 / 98
- `randomization.html`: 216 / 216
- `rangeSlider.html`: 88 / 88
- `render_passes_mapping.html`: 113 / 113

## Validation

Command:

```bash
python3 tools/jangafx_translate.py validate
```

Result:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Review Checks

- Reused already-audited same-source translations from the corresponding LiquiGen How-To Guide pages.
- Filled the remaining page-specific fragments manually, including `Curve Generator`, expression examples, randomization examples, interaction terms, and page-local navigation.
- Full Stage 5A source phrase scan found no remaining hits for:
  - `This`
  - `Here`
  - `Clicking`
  - `click`
  - `will`
  - `where you`
  - `For more information`
  - `Sorry, your browser`
  - English `section`, `page`, `tab`, or `window` suffixes in prose
- Spot-audited `animation`, `modulation_curve`, and `randomization` visible text after the final patches.
- Exact UI labels, file extensions, expressions, variables, node names, and code-like values remain protected.

## Outcome

Stage 5A passes. Since all LiquiGen `specific` reference pages are covered by this batch, Stage 5 is complete.
