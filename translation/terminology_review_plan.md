# JangaFX Terminology Review Plan

Goal: audit the completed Chinese JangaFX HTML documentation for technical term accuracy, glossary consistency, and excessive English retention. This review is separate from the original full-translation goal: the HTML structure is already preserved, so this pass focuses on terminology quality and Chinese readability.

## Review Principles

1. Keep exact product names, file formats, code identifiers, environment variables, shortcuts, and true UI labels unchanged.
2. Translate common technical prose into natural Chinese. Do not leave ordinary words in English just because they appear in a technical document.
3. For first-class VFX/game workflow concepts, preserve the English term only when it is a format, UI label, or industry abbreviation; otherwise pair it with Chinese or translate it.
4. Do not batch-replace terms blindly. Each risky term must be reviewed in source/target context before editing.
5. After each edit batch, regenerate the affected HTML and run structural validation.

## Key Policy Changes To Audit Against

| English term | Previous risk | Review policy |
| --- | --- | --- |
| flipbook | Often over-retained as plain `Flipbook` | Exact UI/workflow label may keep `Flipbook`; prose should normally use `翻页动画`, `翻页序列`, or `Flipbook 贴图/序列` depending on context. |
| sprite sheet | Must not remain English in prose | Use `精灵图集`, consistent with Unity Chinese docs. |
| texture atlas | Must not be confused with flipbook | Use `纹理图集`; sprite-specific atlas is `精灵图集`. |
| mesh flipbook | Risk of half-English phrasing | Use `网格翻页序列`; keep `Mesh Flipbook` only for exact UI/export label. |
| VAT | Abbreviation can stay, but prose needs meaning | Use `VAT（顶点动画纹理）` on explanatory mentions; `VAT` alone is acceptable for exact labels. |
| Pyro | Risk of ambiguous transliteration | Keep `Pyro` for product/node/category labels; use `火焰烟雾模拟` in explanatory prose. |
| node/parameter/viewport/timeline | Ordinary docs terms may be over-retained | Use `节点`, `参数`, `视口`, `时间轴` unless exact UI label. |

## Stages

| Stage | Scope | Gate |
| --- | --- | --- |
| T1 | Research official terminology sources and update review policy/glossary | Research notes and glossary delta are committed locally. |
| T2 | Run automated terminology scan over all translation JSON files | `translation/reports/terminology_scan.md` lists candidate issues by severity. |
| T3 | Review high-risk candidates page by page | Each accepted issue has a target edit; false positives are documented. |
| T4 | Apply first correction batch and regenerate HTML | `python3 tools/jangafx_translate.py validate` passes. |
| T5 | Full post-edit terminology rescan and visual spot checks | No unresolved high-severity findings; audit report is written. |

## Current Stage

Stage T1 is in progress.

## Source Priority

1. JangaFX product pages and JangaFX documentation.
2. JangaFX technical articles, especially VDB material.
3. OpenVDB official documentation and ASWF/NVIDIA material for sparse volume vocabulary.
4. SideFX Houdini documentation for FLIP, whitewater, pyro, SDF, field, advection, and projection vocabulary.
5. Unity and Unreal official documentation for game VFX export terms such as sprite atlas, flipbook, Sub UV, Sprite Renderer, texture atlas, and particle workflows.

## Automated Scan Categories

- `missing_preferred_translation`: source contains a glossary term but the Chinese target lacks the preferred Chinese equivalent.
- `english_retention`: target contains English terms that are not protected product names, file formats, abbreviations, code tokens, or exact UI labels.
- `mixed_readability`: target has a high English-token density inside otherwise Chinese prose.
- `term_conflict`: the same English source term maps to multiple Chinese variants across pages.
- `protected_label_risk`: a likely exact UI/node/parameter label may have been translated in a way that no longer matches the interface.

## Review Batches

1. Global workflow terms: flipbook, sprite sheet, texture atlas, VAT, image sequence, channel packing.
2. VDB/volume terms: voxel, sparse volume, VDB volume, grid, tile, leaf node, level set, SDF, isosurface, isovalue.
3. Fluid simulation terms: FLIP, whitewater, foam, spray, bubbles, viscosity, surface tension, pressure projection, divergence, advection, volume conservation.
4. Pyro/volume-rendering terms: fuel, smoke, temperature, vorticity, curl noise, dissipation, combustion, scattering, absorption, emissive, albedo.
5. Rendering/export terms: rasterizer, path tracer, denoiser, photon mapping, caustics, motion vectors, normal maps, depth maps, samples, bounces.
6. UI/common prose terms: node, parameter, viewport, timeline, inspector, gizmo, panel, tab, dropdown, checkbox.

