# Stage 2A Audit - EmberGen Getting Started

## Scope

- `embergen/pages/getting_started.html`

## Result

Status: Pass.

## Coverage

- Translated segments: 447 / 553
- Remaining untranslated segments are protected or exact UI/code items:
  - File names and paths: `embergen-latest.exe`, `.exe`, `EmberGen.exe`, `.ember`
  - Exact UI labels/buttons/menu paths: `Download EmberGen`, `Install`, `Finish`, `Launch EmberGen`, `Create a desktop shortcut`, `Help`, `License Manager…`, `Activate Key`, `Open Project`, `File > Save`, `Scene`, `Render`, `Export`, `View`, `Settings>Preferences`, `Domain`, `Simulation`, `Apply New Resolution`, `Emission`, `Render Passes`, etc.
  - Shortcuts and keys: `Alt`, `Ctrl`, `Shift`, `Ctrl+S`, `Ctrl + C`, `Ctrl + V`, `Ctrl + L`, `Ctrl + P`, `Enter`
  - Product/tool names and footer names: EmberGen, Sphinx, @pradyunsg, Furo

## Manual Spot Audit

- Download/install/licensing sections are natural Chinese and preserve exact installer/license UI labels.
- Timeline and node graph sections were adjusted for icon-split text nodes using colon-led phrasing.
- Voxel terminology follows the glossary: `体素`, `边界框`, `模拟`, `体素数量`.
- Node names remain in English with Chinese explanatory labels in headings, for example `Emitter（发射器）`.
- Render and Camera sections preserve exact node/parameter names while translating explanatory prose.

## Validation

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Decision

Stage 2A meets the translation and preservation gates. Proceed to Stage 2B.

