# Stage 6B Audit - LiquiGen Node List

Date: 2026-07-06

## Scope

- Page: `liquigen/pages/references/node_list.html`
- Translation JSON: `translation/pages/liquigen_2Fpages_2Freferences_2Fnode_list.html.json`
- Output HTML: `jangafx-docs-zh/liquigen/pages/references/node_list.html`

## Result

- Translation state: 2039 / 2039 segments
- JSON status: `translated`
- Stage result: pass

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

## Spot Audit

Reviewed generated visible text for the following representative sections:

- Whitewater and Whitewater Source.
- Camera, Camera: Look At, Import, and Export nodes.
- Render Passes, export variables, Render Settings, Export: Mesh, Export: VDB, and Export: Particles.
- Modulators: Constant, Oscillator, Cycle, Math, Time Shift, Combine, ADSR, MIDI, and Color nodes.
- Skybox, Ground, Scene, Simulation, Solver, resource limits, viscosity, pressure, density, mesh, liquid appearance, and render settings.

Checks performed:

- Confirmed all prose segments are translated; exact UI labels, node names, file formats, and technical identifiers remain protected.
- Confirmed common LiquiGen terms follow the glossary: `体素`, `白水粒子`, `飞溅`, `泡沫`, `气泡`, `碰撞体`, `发射器`, `表面张力`, `黏度`, `散度`, `SDF`, `VDB`.
- Ran visible-text scans for common untranslated English prose patterns such as `Used to`, `Controls`, `Defines`, `Determines`, `If checked`, and `This node`; no untranslated prose hits remained outside protected names/labels.

## Notes

- Many parameter names remain in English by policy because they are exact UI labels.
- Some inline UI labels naturally introduce spacing around English labels in visible text. This is acceptable and keeps protected labels intact.
- Stage 6C should reuse the completed LiquiGen Node List translations for identical EmberGen source segments before continuing manual EmberGen-specific translation.
