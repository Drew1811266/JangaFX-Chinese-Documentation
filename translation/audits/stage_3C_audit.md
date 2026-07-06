# Stage 3C Audit - Camera Import, Import Animation, Keyframe Animation

## Scope

- `embergen/pages/references/How-To Guides/camera_import.html`
- `liquigen/pages/references/How-To Guides/camera_import.html`
- `embergen/pages/references/How-To Guides/import_animation.html`
- `liquigen/pages/references/How-To Guides/import_animation.html`
- `embergen/pages/references/How-To Guides/animation.html`
- `liquigen/pages/references/How-To Guides/animation.html`

## Result

Status: Pass.

## Coverage

- Translated segments: 976 / 976 across the six Stage 3C pages.
- The extractor was updated to include standalone `If` because the keyframe animation pages use it before emphasized UI labels.
- Stage 3C increased the corpus from 17,644 to 17,655 extracted segments.
- Exact UI/node/parameter labels are intentionally preserved, including `Import`, `Camera`, `Control`, `Asset`, `Transform`, `Scale and center to fit`, `Master Scale`, `Geometry`, `Shapes`, `Emitter`, `Collider`, `Mask`, `Mask Shapes`, `Shape: Primitive`, `Position`, `Node Details`, `Timeline Override`, `No Override`, `Create Key When Parameter Exposed`, `Toggle Timeline Autokey`, `Snap keys to frames`, `Timeline Editor`, `Curve Editor`, `Interpolation Mode`, `Timeline Recording`, `Fit View`, `Snap To Frames`, and `Reset Handle`.

## Manual Spot Audit

- Camera import prose was checked in both EmberGen and LiquiGen pages; `FBX`, `ABC`, camera output pins, `Control` pins, orientation offsets, and clipping planes use glossary-consistent wording.
- Import animation prose was checked separately for EmberGen and LiquiGen; EmberGen-specific `Scale and center to fit` / `Master Scale` workflow and LiquiGen-specific closed-geometry / voxel-size simulation warning were translated independently.
- Keyframe animation prose was checked across setup, timeline editor controls, curve editor controls, interpolation modes, Bezier handle types, and timeline recording.
- Short-fragment fixes were applied for `If` and context-sensitive mouse-operation phrases so no English explanatory prose remains from skipped short text nodes.
- Remaining English is limited to protected UI labels, node names, parameter names, keyboard/mouse shortcuts, file formats, footer tool names, and generated HTML attributes.

## Validation

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Decision

Stage 3C meets the translation and preservation gates. Proceed to Stage 3D.
