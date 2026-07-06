# Stage 6C Audit - EmberGen Node List

Date: 2026-07-06

## Scope

- Page: `embergen/pages/references/node_list.html`
- Translation JSON: `translation/pages/embergen_2Fpages_2Freferences_2Fnode_list.html.json`
- Output HTML: `jangafx-docs-zh/embergen/pages/references/node_list.html`

## Result

- Translation state: 4220 / 4220 segments
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

Reviewed generated visible text for representative EmberGen node-list sections:

- Camera, Collider, `Emitter: Volume`, `Emitter: Particles`, Export / Render, VDB, and Particles export.
- Forces: Line, Toroidal, Noise, Point, Vector Field, and Vorticles.
- Ground, Import, Light, Modulators, Scene, Shading, and all Shape nodes through `Modifier`.
- Simulation: Domain, Simulation Mode, Time Control, Projection, Combustion, Dissipation, Diffusion, Vorticity, Force, Wind, Shredding, Mask, Visual, Particles, Skybox, Volume Processing, Post Process, Post Modulation, and Slicing Mask.

Checks performed:

- Confirmed the page translation JSON is complete and marked `translated`.
- Confirmed exact UI labels, node names, parameter names, file formats, paths, and code-like identifiers remain protected.
- Confirmed EmberGen simulation terms follow the glossary: `体素`, `涡量`, `平流`, `散度`, `不可压缩性`, `碰撞体`, `发射器`, `燃烧`, `烟雾`, `燃料`, `火焰`, `VDB`, and `SDF`.
- Ran structural validation with zero tag mismatches and zero missing local links/assets.
- Ran a visible-text heuristic scan for obvious untranslated English prose. Only protected UI labels and one Windows path example remained.

## Notes

- `tools/jangafx_translate.py` gained narrow post-apply polish rules for inline Sphinx fragments that were not cleanly represented as standalone translation segments.
- The page still intentionally preserves exact English UI strings such as `Projection Quality`, `Control Mode`, `Emitter: Particles`, and parameter names.
