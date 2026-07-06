# Pause Checkpoint - 2026-07-06 - Stage 4D

Paused by user request during Stage 4D. Do not advance translation until the user resumes.

## Goal Status

- Goal mode: active
- Long-term objective: complete the Chinese translation of the local JangaFX HTML documentation with Codex-authored translations, glossary consistency, raw-preserving HTML output, and staged audit/validation.
- Goal is not complete and is not blocked.

## Workspace

- Workspace: `/Users/patpat/Development projects/JangaFX`
- Source mirror: `jangafx-docs`
- Chinese output: `jangafx-docs-zh`
- Translation JSON directory: `translation/pages`
- Translation helper: `tools/jangafx_translate.py`

## Completed Stages

- Stage 0: infrastructure, glossary, extraction/apply/validate tooling - complete
- Stage 1: homepage, product landing pages, FAQ pages, shared navigation/UI copy - complete
- Stage 2: EmberGen and LiquiGen Getting Started pages - complete and audited
- Stage 3: all EmberGen and LiquiGen How-To Guides - complete and audited
- Stage 4A: EmberGen and LiquiGen references index pages - complete and audited
- Stage 4B: EmberGen settings page - complete and audited
- Stage 4C: LiquiGen settings page - complete and audited

## Current Stage

- Stage: 4D, EmberGen UI reference page
- Current page: `embergen/pages/references/ui_reference.html`
- Translation JSON: `translation/pages/embergen_2Fpages_2Freferences_2Fui_reference.html.json`
- Current translation state: 281 / 697 segments translated
- JSON status: `in_progress`
- Completed within this page:
  - Menubar section translated and applied.
  - Viewport section translated through the first half, including Scene tabs, Backplates, Masking, Manipulators, Camera Gizmo, Render Quality, and common viewport setting text.

## Latest Validation

Last full structural validation before the pause passed:

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

The final helper patch before this pause added an inline punctuation polish rule for `和` between inline emphasized labels, but the current Stage 4D page has not been re-applied after that last helper change.

## Known Pending Fixes On Resume

Before continuing new translation work, patch the current page JSON and re-apply the page:

- Replace Chinese full-width closing parentheses in mixed UI-label sequences with ASCII `)` for these IDs:
  - `e4168ded075f`
  - `19872393b141`
  - `86cb97c8b300`
  - `909252fab901`
  - `32f30aa44c32`
  - `0d3135ecb85b`
  - `e151321f96bd`
- Complete `ac0a1dfdfe6b` so the visible sentence reads naturally:
  - `Settings > Preferences... > Viewport Quality 中编辑的预设。`
- Optional polish: change `58fcad8e2bde` from a bare `Flames translucency` target to `Flames translucency（火焰半透明）` if the surrounding sentence still reads awkwardly after re-apply.

## Resume Commands

```bash
python3 tools/jangafx_translate.py apply --page 'embergen/pages/references/ui_reference.html'
python3 tools/jangafx_translate.py validate
```

Then run a visible-text spot audit around the Viewport lines before translating the next Stage 4D batch.

## Next Translation Batch After Fixes

Continue Stage 4D from the remaining Viewport / Render and Export viewer material:

- Render Quality
- View Mode
- Projection Quality
- Render Shapes
- Lock Camera
- Stats and stat descriptions
- Toggle panel fullscreen
- Sky, ground, force gizmo, bounds
- Render / Export viewer

After that, proceed to the Node Graph section within the same page.
