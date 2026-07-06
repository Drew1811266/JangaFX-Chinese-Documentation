# Stage 4E Audit - LiquiGen UI Reference

Date: 2026-07-06

## Scope

- `liquigen/pages/references/ui_reference.html`

## Translation State

- Translation JSON: `translation/pages/liquigen_2Fpages_2Freferences_2Fui_reference.html.json`
- Status: `translated`
- Segment coverage: 688 / 688

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

## Review Checks

- Reused already-audited EmberGen UI reference translations only when the source segment was identical and unambiguous.
- Manually translated LiquiGen-specific sections:
  - Path tracing
  - Liquid Mesh
  - Whitewater
  - LiquiGen simulation statistics
  - Diagnostics, Manipulator, and Preview/Export sections
  - LiquiGen-specific Properties Panel differences
  - LiquiGen Project Manager differences
- Full-page source phrase scan found no remaining untranslated prose hits for:
  - `This`
  - `Here`
  - `Clicking`
  - `click`
  - `will`
  - `where you`
  - `For more information`
  - `Sorry, your browser`
- Spot-audited visible text across Viewport, Node Graph, Timeline Editor, Properties Panel, and Project Manager.
- Exact UI labels, shortcuts, product names, node names, file extensions, and code-like strings were preserved.
- Terms follow the glossary for `白水`, `液体网格`, `投影`, `divergence`, `体素`, `时间轴编辑器`, `曲线编辑器`, `关键帧`, `预设`, `VRAM`, and licensing terms.

## Notes

- Some audit text still shows spaces around inline icon/link positions, such as `可以 单击`; this comes from the text extractor stripping icons and is acceptable in the rendered page.
- Source-side labels such as `24-gb`, `8-gb`, `Render Pass`, `Export: Image`, and `Timeline Override` were preserved as exact UI or code-like labels.

## Outcome

Stage 4E passes. Stage 4 is complete and the plan can move to Stage 5.
