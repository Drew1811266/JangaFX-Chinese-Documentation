# Pause Checkpoint - 2026-07-06, Stage 6C

Paused during Stage 6C by user feedback that the current pace is slow.

## Stable State

- Active long-term goal: complete the full Chinese translation of the local JangaFX HTML documentation with Codex-authored translations, glossary consistency, raw-preserving HTML output, and validation/audit after each stage.
- Source mirror: `jangafx-docs`
- Chinese output: `jangafx-docs-zh`
- Translation helper: `tools/jangafx_translate.py`
- Current stage: Stage 6, EmberGen and LiquiGen Node List pages, complete.
- Stage 6B: `liquigen/pages/references/node_list.html` complete and audited.
- Stage 6C current page: `embergen/pages/references/node_list.html`
- Current translation state: 4220 / 4220 segments, `translated`
- Latest validated output: `jangafx-docs-zh/embergen/pages/references/node_list.html`

## Completed In Stage 6C

- Exact-source migration from completed LiquiGen Node List copied 756 conflict-free matching segments.
- Camera-specific sections translated.
- Collider groups translated through Visuals.
- `Emitter: Volume` translated through Activity, Transform, Emission, Pressure, Forces, and Visuals.
- `Emitter: Particles` translated through intro, connection overview, Emission, Transform, Freeze, Life, Initial forces, localized force, active forces, collisions, bounds, Shape, Rendering, color modes/modulation, alpha/color attenuation, Injection, and temperature/velocity injection.
- `Emitter: Particles` tail wording polish plus Export / Render, VDB, and Particles export nodes translated and spot-audited.
- Forces overview plus Line, Toroidal, Noise, Point, Vector Field, and Vorticles translated and spot-audited.
- Ground, Import, and Light node sections translated and spot-audited.
- Modulators tail, Scene, and Shading translated and spot-audited.
- Shapes `Primitive`, `Burst`, `Particles`, `Noise`, `Transform`, `Blend`, and `Modifier` translated, applied, validated, and spot-audited.
- Simulation sections from Domain through Slicing Mask translated, applied, validated, and spot-audited.

## Resume Point

- First untranslated segment:
  - none; `embergen/pages/references/node_list.html` is complete.
- Next intended batch:
  - Stage 7: licensing guide, search/index polish, and full cross-page terminology audit.
- Resolved patch detail:
  - The intended `bottom` segment id in `Six Point 2 (BBF)` was corrected to `6cc19163324e`.
  - The Export / Render patch was applied and validated.
  - Narrow post-apply polish rules were added to `tools/jangafx_translate.py` for inline Sphinx fragments that were not cleanly represented as standalone translation segments.

## Latest Validation

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

## Speed Adjustment

The previous per-fragment manual cadence is layout-safe but too slow for Node List pages. Resume with larger complete node-section batches, while keeping the same safety model:

- translate in JSON only, never by editing rendered HTML directly;
- keep tags, links, assets, code identifiers, UI labels, node names, and parameter names protected;
- apply the page after each larger batch;
- run structural validation after each batch;
- spot-audit representative visible text for natural Chinese and glossary consistency before marking a stage batch complete.

Suggested batch size for Stage 6C: complete node groups or render/export groups at roughly 250-500 segments per pass, instead of tens of segments.

## Resume Commands

```bash
python3 tools/jangafx_translate.py apply --page 'embergen/pages/references/node_list.html'
python3 tools/jangafx_translate.py validate
```
