# JangaFX Documentation Translation Progress

## Current State

- Source mirror: `jangafx-docs`
- Chinese output: `jangafx-docs-zh`
- Translation workspace: `translation`
- Translation helper: `tools/jangafx_translate.py`
- Glossary: `translation/glossary.zh-CN.md`
- Policy: `translation/translation_policy.md`
- Translation memory: `translation/translation_memory.zh-CN.json`

## Completed

- Built a raw-preserving HTML extraction and replacement pipeline.
- Built the JangaFX Chinese glossary from official JangaFX, OpenVDB, Unreal, and SideFX terminology references.
- Extracted 17,655 text segments from 62 HTML files.
- Completed the full Chinese output copy in `jangafx-docs-zh`.
- All 62 translation page JSON files are marked `translated`.
- Translated and validated:
  - `index.html`
  - `embergen/index.html`
  - `liquigen/index.html`
  - `illugen/index.html`
  - `geogen/index.html`
  - `embergen/pages/FAQ.html`
  - `liquigen/pages/FAQ.html`
- Completed and audited Stage 2:
  - `embergen/pages/getting_started.html`
  - `liquigen/pages/getting_started.html`
- Completed and audited Stage 3A:
  - How-To Guides index, comment, note, palettes, and range slider pages for both EmberGen and LiquiGen
- Completed and audited Stage 3B:
  - Color guide pages for both EmberGen and LiquiGen
- Completed and audited Stage 3C:
  - Camera import, FBX/OBJ/ABC import, and keyframe animation pages for both EmberGen and LiquiGen
- Completed and audited Stage 3D:
  - Modulation curve, modulating parameters, and randomization pages for both EmberGen and LiquiGen
- Completed and audited Stage 3E:
  - Render pass mapping pages for EmberGen and LiquiGen
  - EmberGen histogram and VDB export pages
- Completed and audited Stage 3F:
  - LiquiGen diagnostics and expressions pages
- Completed Stage 3:
  - All EmberGen and LiquiGen How-To Guides pages are translated and structurally validated.
- Completed and audited Stage 4A:
  - EmberGen and LiquiGen references index pages
- Completed and audited Stage 4B:
  - EmberGen settings page
- Completed and audited Stage 4C:
  - LiquiGen settings page
- Completed and audited Stage 4D:
  - EmberGen UI reference page
- Completed and audited Stage 4E:
  - LiquiGen UI reference page
- Completed Stage 4:
  - UI Reference and Settings pages for EmberGen and LiquiGen are translated, audited, and structurally validated.
- Completed and audited Stage 5:
  - All LiquiGen `specific` reference pages are translated and structurally validated.
- Completed and audited Stage 6:
  - EmberGen and LiquiGen Node List pages are translated and structurally validated.
- Completed and audited Stage 7:
  - Licensing guide, search/index pages, and residual overview/FAQ/getting-started cleanup are translated and structurally validated.
- Completed and audited Stage 8:
  - Final validation, visible-text leak scan, and Playwright visual spot checks passed.
- Added narrow inline punctuation polish to the raw-preserving generator for Chinese punctuation around protected inline UI labels.
- Applied common navigation and UI text translations across the full documentation copy.

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

## Remaining Work

- None for the requested full local Chinese documentation translation.
- Future maintenance only: rerun extraction, translation, apply, and validation if the upstream JangaFX documentation mirror changes.

## Goal Mode

The long-term translation goal is complete. All stages in `translation/stage_plan.md` have passed audit and validation.

## Terminology Review Goal - 2026-07-06

- Started a new long-term goal for professional terminology review and over-retained English cleanup.
- Planning file: `translation/terminology_review_plan.md`
- Research notes: `translation/terminology_research.md`
- Added an automated candidate scanner: `tools/jangafx_terminology_audit.py`
- Updated the glossary policy for high-risk terms such as `flipbook`, `sprite sheet`, `texture atlas`, `mesh flipbook`, VDB/SDF terms, FLIP/whitewater terms, advection/projection terms, and rendering terms.

## Terminology Review Completion - 2026-07-06

- Completed the professional terminology review goal.
- Final audit: `translation/audits/terminology_review_2026-07-06.md`
- Final scanner report: `translation/reports/terminology_scan.md`
- Glossary updated: `translation/glossary.zh-CN.md`
- Final apply/validation:

```text
Applied 17648 translated segments across 62 pages.
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

- Final terminology scan:

```text
Pages scanned: 62
Segments scanned: 17655
Candidate findings: 14
Findings by severity: {'low': 14}
Findings by type: {'mixed_readability': 10, 'missing_preferred_translation': 4}
```

- No high or medium terminology findings remain.
- Remaining low findings were reviewed and accepted as keyboard shortcuts, software/product identifiers, exact UI labels with Chinese explanation, exact error messages, or inline HTML segmentation false positives.

## Layout And Media Review Goal - 2026-07-06

- Completed a full browser-rendered layout and media consistency review against the original local JangaFX mirror.
- Final audit: `translation/audits/layout_review_2026-07-06.md`
- Automated report: `translation/reports/layout/layout_audit.md`
- JSON data: `translation/reports/layout/layout_audit.json`
- Review tool: `tools/jangafx_layout_audit.cjs`
- Screenshot evidence: `output/playwright/layout-audit/`
- Final clean apply/validation:

```text
Applied 17648 translated segments across 62 pages.
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

- Browser comparison:

```text
Compared 62 pages across 2 viewports.
Issues by severity: {"medium":28}
```

- Result: conditional pass. Page count, media count, media source order, media dimensions, core containers, links, and assets match. The remaining 28 medium findings are desktop-only float-layout reflow differences caused by translated text length interacting with the official documentation's floating media layout.

## Stage 4D Completion - 2026-07-06

- Completed page: `embergen/pages/references/ui_reference.html`
- Translation state: 697 / 697 segments, `translated`
- Audit: `translation/audits/stage_4D_audit.md`
- Validation:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Stage 4E Completion - 2026-07-06

- Completed page: `liquigen/pages/references/ui_reference.html`
- Translation state: 688 / 688 segments, `translated`
- Audit: `translation/audits/stage_4E_audit.md`
- Validation:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Stage 5 Completion - 2026-07-06

- Completed pages: all 12 `liquigen/pages/references/specific/*.html` pages
- Translation state: all 12 pages `translated`
- Audit: `translation/audits/stage_5A_audit.md`
- Validation:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Stage 6 Progress - 2026-07-06

- Stage 6A inventory completed:
  - `liquigen/pages/references/node_list.html`: 493 / 2039 after migration, now 2039 / 2039 and complete.
  - `embergen/pages/references/node_list.html`: 739 / 4220 after migration.
- Stage 6B LiquiGen Node List manual batches completed:
  - Shape primitive and Appearance intro.
  - Collider, Drain, and Emitter through Velocity.
  - Force: Constant, Force: Shape, Force: Drag, Force: Turbulence, Force: Line, and Force: Toroidal.
  - Light: Directional, Light: Point, and Light: Area.
  - Whitewater main node through Appearance parameters.
  - Whitewater Source.
  - Camera, Camera: Look At, Import, and Export nodes.
  - Modulators, Color, Skybox, Ground, Scene, Simulation, and Render sections.
- Stage 6B audit completed:
  - Audit: `translation/audits/stage_6B_audit.md`
  - Page status: `translated`
- Stage 6C EmberGen Node List completed:
  - Exact-source migration from completed LiquiGen Node List copied 756 conflict-free segments.
  - `embergen/pages/references/node_list.html`: 739 / 4220 before migration, 1495 / 4220 after migration, now 4220 / 4220 and complete.
  - Audit: `translation/audits/stage_6C_audit.md`
  - Page status: `translated`
  - Latest completed batches in this continuation:
    - `Emitter: Particles` tail polish plus Export / Render, VDB, and Particles export nodes.
    - Forces overview plus Line, Toroidal, Noise, Point, Vector Field, and Vorticles.
    - Ground, Import, and Light node sections.
    - Modulators tail, Scene, and Shading translated and spot-audited.
    - Shapes `Primitive`, `Burst`, `Particles`, `Noise`, `Transform`, `Blend`, and `Modifier` translated, applied, validated, and spot-audited.
    - Simulation sections from Domain through Slicing Mask translated, applied, validated, and spot-audited.
- Stage 6 complete:
  - LiquiGen Node List audit: `translation/audits/stage_6B_audit.md`
  - EmberGen Node List audit: `translation/audits/stage_6C_audit.md`
- Latest validation:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Pause Checkpoint - 2026-07-06, Stage 6C

Paused after user feedback that the current pace is slow.

- Current page: `embergen/pages/references/node_list.html`
- Current translation state: 4220 / 4220 segments, `translated`
- Latest stable applied output: `jangafx-docs-zh/embergen/pages/references/node_list.html`
- Stage 6B remains complete and audited: `translation/audits/stage_6B_audit.md`
- Detailed checkpoint: `translation/checkpoints/2026-07-06_stage_6C_pause.md`
- Stage 6C audit: `translation/audits/stage_6C_audit.md`
- Next stage: Stage 7, licensing guide, search/index polish, and full cross-page terminology audit.

## Stage 7 Progress - 2026-07-06

- Stage 7 completed and audited:
  - Audit: `translation/audits/stage_7_audit.md`
  - `licensing/index.html`: 290 / 290, `translated`
  - Cleanup pages completed: `index.html`, product landing pages, EmberGen/LiquiGen FAQ pages, EmberGen Getting Started, `genindex.html`, and `search.html`.
- Latest validation after Stage 6 completion:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Stage 8 Final Completion - 2026-07-06

- Final audit: `translation/audits/stage_8_final_audit.md`
- Translation state: all 62 page JSON files are `translated`.
- Full apply:

```text
Applied 17648 translated segments across 62 pages.
```

- Full validation:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

- Visible-text scan: no long untranslated English prose findings outside protected code/path/product/UI-label contexts.
- Playwright visual spot checks:
  - `index.html`
  - `licensing/index.html`
  - `embergen/pages/references/node_list.html`
  - `liquigen/pages/references/node_list.html`
  - `search.html`
- Screenshot artifacts: `output/playwright/*.png`

## Pause Checkpoint - 2026-07-06, Stage 6B

Paused by user request during Stage 6B.

- Latest completed stage: Stage 5, all LiquiGen `specific` reference pages.
- Current stage: Stage 6, EmberGen and LiquiGen Node List pages.
- Current page: `liquigen/pages/references/node_list.html`
- Current translation state: 1021 / 2039 segments, `in_progress`
- Current page progress:
  - Shape primitive and Appearance intro translated.
  - Collider, Drain, and Emitter through Velocity translated.
  - Force: Constant, Force: Shape, Force: Drag, Force: Turbulence, Force: Line, and Force: Toroidal translated.
  - Light: Directional, Light: Point, and Light: Area translated.
  - Whitewater main node through Appearance parameters translated.
- Resume task:
  - Continue from `Whitewater Source` at segment index 698 in `translation/pages/liquigen_2Fpages_2Freferences_2Fnode_list.html.json`.
  - Apply `liquigen/pages/references/node_list.html`, run structural validation, then spot-audit Whitewater prose and protected UI labels.
- Speed note:
  - Current per-fragment manual translation is layout-safe but slow on Node List pages.
  - Next pass should translate by complete node section groups in larger JSON batches, then audit the rendered HTML per node group. This keeps tags protected while reducing command overhead.
- Latest validation at pause:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Pause Checkpoint - 2026-07-06

Paused by user request during Stage 4D.

- Latest completed stage: Stage 4C, LiquiGen settings page.
- Current page: `embergen/pages/references/ui_reference.html`
- Current translation state: 281 / 697 segments, `in_progress`
- Current page progress: Menubar complete; Viewport first half translated and applied.
- Known resume task: patch the Viewport mixed-parenthesis/incomplete sentence issues listed in `translation/checkpoints/2026-07-06_stage_4D_pause.md`, re-apply the page, then run validation.
- Latest validation before pause:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

Detailed checkpoint: `translation/checkpoints/2026-07-06_stage_4D_pause.md`

## Pause Checkpoint - 2026-07-03

Paused by user request during Stage 4B.

- Latest completed stage: Stage 4A, references index pages.
- Current page: `embergen/pages/references/settings.html`
- Current translation state: 78 / 282 segments, `in_progress`
- Validation at pause:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

Detailed checkpoint: `translation/checkpoints/2026-07-03_stage_4B_pause.md`
