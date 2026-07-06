# Stage 3F Audit - LiquiGen Diagnostics And Expressions

## Scope

- `liquigen/pages/references/How-To Guides/diagnostics.html`
- `liquigen/pages/references/How-To Guides/expressions.html`

## Result

Status: Pass.

## Coverage

- Translated segments: 495 / 495 across the two Stage 3F pages.
- Diagnostics terminology was added to the glossary, including `liquid mesh`, `trapped air`, `wave crests`, `SDF`, `normal`, `voxel size`, `tile`, `sparsity`, `slice`, `field shading`, `remap range`, `force velocity`, `stickiness`, and `dynamic viscosity coefficient`.
- Exact UI/parameter labels and expression syntax tokens are intentionally preserved, including `Liquid Mesh`, `Realistic`, `Field Shading`, `Trapped Air`, `Wave Crests`, `Show Normals`, `Voxel size`, `Simulation`, `Whitewater`, `SDF smoothing`, `Liquid Particles`, `Voxels`, `Pixels`, `Albedo`, `Unique ID`, `Stickiness`, `Behaviour`, `Emitter`, `Dynamic viscosity coefficient`, `Field Shading`, `Color: Gradient`, `Remap Range`, `Stats`, `View`, `Show SDF`, `Force`, `Transform`, `Arrow`, `Select All`, `Ignore disabled forces`, `Visual mode`, `Sparsity`, `Hide Empty`, `Thickness`, `Min/Max`, `Bounding Box`, `Tiles`, `Add`, `Sub`, `Mul`, `Quo`, `Rem`, `Pow`, `Open_Paren`, `Close_Paren`, `Comma`, and expression function names.

## Manual Spot Audit

- Diagnostics `Liquid` sections were checked for liquid mesh, particle visualization, trapped air, wave crests, normals, SDF smoothing, particle sizing, Field Shading attributes, color gradients, remap ranges, and whitewater particle visibility.
- `Models`, `Forces`, `Velocity`, and `Domain` sections were checked for imported-model SDF wording, force-list filtering, 2D/3D arrow visualization, slice controls, velocity visualization, simulation tiles, and bounding-box behavior.
- Expressions page was checked for expression usage prose, `curveExpressions`, operator labels, constants, function arity sections, and code token preservation.
- Visible-text audit fixed incorrect `Remap Range` split wording, preserved protected UI labels, normalized skipped technical punctuation such as `Min/Max:`, `Open_Paren:`, and `Close_Paren:`, and verified that remaining English is limited to protected UI labels, exact expression tokens, software/tool names, code identifiers, footer tool names, and generated HTML attributes.

## Validation

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Decision

Stage 3F meets the translation and preservation gates. Proceed to the next Stage 3 batch.
