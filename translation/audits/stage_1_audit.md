# Stage 1 Audit

## Scope

- `index.html`
- `embergen/index.html`
- `liquigen/index.html`
- `illugen/index.html`
- `geogen/index.html`
- `embergen/pages/FAQ.html`
- `liquigen/pages/FAQ.html`

## Result

Status: Pass.

## Checks

- Structural validation passed:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

- Remaining untranslated segments in this stage are protected terms:
  - Product names: EmberGen, LiquiGen, IlluGen, GeoGen
  - Sphinx/Furo footer names: Sphinx, @pradyunsg, Furo
  - Exact UI labels and node/parameter names in FAQ: Export, Timestep, Time Control, Simulation, FPS, Playback, Import, Override FPS, Backplate frame rate, Backplate, Camera, Frame Stride, Render, Export: Image

## Manual Spot Audit

- Product landing pages read naturally and preserve product names.
- FAQ pages preserve exact UI labels in English while translating explanatory prose around them.
- Footer wording is readable after fixing the split `@pradyunsg's Furo` text node.

## Decision

Stage 1 meets the translation and preservation gates. Proceed to Stage 2.

