# Stage 4D Audit - EmberGen UI Reference

Date: 2026-07-06

## Scope

- `embergen/pages/references/ui_reference.html`

## Translation State

- Translation JSON: `translation/pages/embergen_2Fpages_2Freferences_2Fui_reference.html.json`
- Status: `translated`
- Segment coverage: 697 / 697

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

- Raw-preserving HTML generation remained intact.
- Full-page source phrase scan found no remaining untranslated prose hits for:
  - `This`
  - `Here`
  - `Clicking`
  - `click`
  - `will`
  - `where you`
  - `For more information`
  - `Sorry, your browser`
- Spot-audited visible text in:
  - Menubar
  - Viewport
  - Render and Export viewer
  - Node Graph
  - Timeline Editor
  - Properties Panel
  - Project Manager
- Exact UI labels, shortcuts, file formats, node names, and protected product/tool names were preserved where they identify the UI or a specific control.
- Terminology follows the current glossary for `节点图`, `时间轴编辑器`, `曲线编辑器`, `关键帧`, `体素`, `边界框`, `预设`, `收藏项`, `自动收藏`, and licensing terms.

## Notes

- Some inline icon positions produce visible audit text such as `可以 单击` when the icon itself is stripped by the text extractor. The rendered page keeps the icon between those words, so this is acceptable.
- Source-side literal labels/typos such as `8BG` and `.liquigen` in the EmberGen UI reference were preserved rather than silently corrected.
- The postprocessor was extended for Chinese punctuation around inline labels and links, then the page was regenerated and revalidated.

## Outcome

Stage 4D passes and is ready to hand off to Stage 4E.
