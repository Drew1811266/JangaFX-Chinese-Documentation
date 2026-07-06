# Stage 4B Audit - EmberGen Settings

## Scope

- `embergen/pages/references/settings.html`

## Result

Status: Pass.

## Coverage

- Translated segments: 282 / 282.
- Settings terminology was added to the glossary, including `Preferences`, `auto-favorite`, `read-only copy`, `thumbnail`, `shortcut`, `key-bind`, `minimap`, `user variable`, and `autosave`.
- Exact UI/parameter labels are intentionally preserved, including `Project Settings`, `Tags`, `Save Read-Only Copy`, `Auto-Favorite Changed Parameters`, `Load`, `Randomize All Seeds`, `Randomize`, `Randomize Override`, `Seed`, `Project Notes`, `Home Screen`, `PNG flipbook`, `Preview`, `Clear`, `Capture`, `Render`, `Capture Types`, `Import File`, `Import`, `Frame Count`, `Frame Rate`, `UI Scale`, `Vsync`, `Unlit`, `Smooth UI`, `Play Project On Load`, `Export Warning On Overwrite`, `Disable Warning`, `Cancel`, `Overwrite`, `UI Layout`, `Graph Background Grid Type`, `Mouse Compatibility Mode`, `Middle-Click Emulation`, `Scroll-Wheel Emulation`, `Max Undo History`, `Recovery Autosave Interval`, `Frame Limiter`, `Show Floating Viewport`, `Create Key When Parameter Exposed`, `Show Modulator Output On Timeline`, `Mod: Oscillator`, `Sine`, `Template Project`, `File > New`, `Post-Export Command`, `$quit`, `MIDI`, `Minimap`, `Control Mapping`, `Mouse-Y`, `Orbit/Rotation Sensitivity`, and `Reset To Default`.
- The raw-preserving generator punctuation polish was tightened for Chinese spacing and skipped strong-label colons without changing tag structure.

## Manual Spot Audit

- `Project Settings` sections were checked for preset tags, read-only copies, changed-parameter auto-favorites, seed randomization, settings search/category controls, reset confirmation, notes, and thumbnail capture/import setup.
- `Preferences` sections were checked for general UI preferences, export overwrite warnings, mouse/tablet compatibility, timeline keyframe behavior, modulator timeline output, custom template project setup, post-export command, MIDI support, minimap controls, viewport quality, shortcuts, camera controls, and user variables.
- Icon-adjacent mouse-operation text was reviewed and adjusted so the Chinese remains readable even when visible-text extraction omits inline mouse icons.
- Remaining English is limited to protected UI labels, node names, parameter names, software names, code variables, file formats, footer tool names, and generated HTML attributes.

## Validation

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Decision

Stage 4B meets the translation and preservation gates. Proceed to Stage 4C.
