# Stage 3D Audit - Modulation Curve, Modulating Parameters, Randomization

## Scope

- `embergen/pages/references/How-To Guides/modulation_curve.html`
- `liquigen/pages/references/How-To Guides/modulation_curve.html`
- `embergen/pages/references/How-To Guides/modulating_parameters.html`
- `liquigen/pages/references/How-To Guides/modulating_parameters.html`
- `embergen/pages/references/How-To Guides/randomization.html`
- `liquigen/pages/references/How-To Guides/randomization.html`

## Result

Status: Pass.

## Coverage

- Translated segments: 1,458 / 1,458 across the six Stage 3D pages.
- Exact UI/node/parameter labels are intentionally preserved, including `Interpolation Mode`, `Bézier`, `Free`, `Linear`, `Reset Handle`, `Curve Generator`, `JangaFX Curve (.jfxcurve)`, `Mod: Oscillator`, `Pin Override`, `Randomize Override`, `Randomized`, `Randomize All`, `Export Variation`, `Export Variations`, `Directory`, `Filename`, `ADSR`, and `MIDI`.
- Product-specific examples were translated separately: EmberGen explosion variations and LiquiGen splat variations.

## Manual Spot Audit

- Modulation curve pages were checked for curve point editing, interpolation modes, Bezier handle types, curve save/load, Curve Generator controls, LiquiGen curve presets, and LiquiGen expression-based curve generation.
- Modulating parameter pages were checked for oscillator setup, range-slider mapping, frequency units, other modulator node descriptions, ADSR envelope wording, and MIDI setup.
- Randomization pages were checked for Randomized tab setup, parameter type handling, EmberGen explosion ranges, LiquiGen splat ranges, `$(variation)` export naming, and Export Variation window options.
- Remaining English is limited to protected UI labels, node names, parameter names, keyboard/mouse shortcuts, file formats, code variables, footer tool names, and generated HTML attributes.

## Validation

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Decision

Stage 3D meets the translation and preservation gates. Proceed to Stage 3E.
