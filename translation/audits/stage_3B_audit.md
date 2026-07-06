# Stage 3B Audit - Color Guides

## Scope

- `embergen/pages/references/How-To Guides/color.html`
- `liquigen/pages/references/How-To Guides/color.html`

## Result

Status: Pass.

## Coverage

- Translated segments: 446 / 446 across the two Stage 3B pages.
- The extractor was updated to include standalone `by` because the Color pages use `by` between UI labels and mouse icons.
- Exact UI/node/parameter labels are intentionally preserved, including `Color: Constant`, `Color Picker`, `Color: Gradient`, `Color Gradient`, `Interpolation Color Space`, `Color Gradient Presets`, `Color Selector`, `Pin Override`, `Exposed Color Gradient`, `Smoke color`, `Fire color`, `Coloring remap range`, `Coloring remap ramp`, `JangaFX Color Gradient (.jfxcg)`, and `EmberGen Color Gradient (.embercg)`.

## Manual Spot Audit

- Shared Color Picker prose was checked in both EmberGen and LiquiGen pages.
- EmberGen-specific smoke/fire color mapping was translated with `体素密度`, `直方图`, and `gamma 运算` terminology.
- LiquiGen-specific gradient context menu and gradient preset management were translated separately from the EmberGen `.embercg` workflow.
- The UI Palette glossary correction from Stage 3A was preserved; color palettes remain translated as `色板` / `颜色渐变预设` where appropriate.
- A visible-text scan found no remaining English explanatory prose. Remaining English is limited to protected UI labels, node names, parameter names, file formats, menu names, and footer tool names.

## Validation

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Decision

Stage 3B meets the translation and preservation gates. Proceed to Stage 3C.
