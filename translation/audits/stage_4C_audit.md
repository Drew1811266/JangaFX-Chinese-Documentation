# Stage 4C Audit - LiquiGen Settings

## Scope

- `liquigen/pages/references/settings.html`

## Result

Status: Pass.

## Coverage

- Translated segments: 346 / 346.
- Shared settings text was reused from EmberGen settings only where the source text was identical, then LiquiGen-specific sections were translated separately.
- Exact UI/parameter labels are intentionally preserved, including `Project Settings`, `Tags`, `Shape default size scale`, `Read-Only`, `Save Read-Only Copy`, `Reset To Defaults`, `Capture From Viewport`, `Simulation Preemption`, `FPS Limit`, `Relative Asset Paths`, `.liquigen`, `Filepath`, `MIDI support`, `Bindings`, `Control Mapping`, `Orbit`, `Zoom`, `Pan`, `Pan (Alt.)`, `Fly`, `Tank`, `Pivot To Cursor`, `Pivot To Ground`, `Always Show Pivot`, `Orbit Sensitivity`, `Invert Vertical Orbit Direction`, `Zoom Input Axis`, `Mouse`, `Wheel`, `Pan Sensitivity`, `Distance to Pivot Scaling`, `Pan Plane`, `Fly Sensitivity`, and `WASD Fly Plane`.
- Product-specific wording was corrected during audit so the LiquiGen page refers to `.liquigen` project files and closing `LiquiGen` for post-export commands.

## Manual Spot Audit

- Project settings were checked for preset tags, shape default size scaling, read-only copies, changed-parameter auto-favorites, seed randomization, viewport visibility controls, reset confirmation, notes, and thumbnail setup.
- Preferences were checked for simulation preemption, graph background grid options, FPS limit, relative asset paths, MIDI support, minimap controls, shortcut controls, and detailed camera bindings.
- Camera binding sections were checked for bindings setup, control mappings, orbit/zoom/pan/fly/tank modes, pivot behavior, ground pivot modes, vertical orbit inversion, zoom input axis, pan plane, fly sensitivity, and WASD fly plane behavior.
- Visible-text audit fixed read-only quote boundaries, product-specific post-export wording, `.liquigen` extension, `Minimap Scale` range wording, and footer `and` wording after a broad replacement was corrected.
- Remaining English is limited to protected UI labels, node names, parameter names, software names, keyboard keys, code variables, file formats, footer tool names, and generated HTML attributes.

## Validation

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Decision

Stage 4C meets the translation and preservation gates. Proceed to Stage 4D.
