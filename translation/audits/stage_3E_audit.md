# Stage 3E Audit - Render Pass Mapping, Histogram, VDB Export

## Scope

- `embergen/pages/references/How-To Guides/render_passes_mapping.html`
- `liquigen/pages/references/How-To Guides/render_passes_mapping.html`
- `embergen/pages/references/How-To Guides/histogram.html`
- `embergen/pages/references/How-To Guides/exportVDB.html`

## Result

Status: Pass.

## Coverage

- Translated segments: 486 / 486 across the four Stage 3E pages.
- Exact UI/node/parameter labels are intentionally preserved, including `Source`, `Destination`, `HDR`, `RAW`, `Add Render Pass`, `Red`, `Green`, `Blue`, `Top`, `Left`, `Right`, `Mask`, `Alpha`, `Log Y`, `Coloring remap range`, `Coloring remap ramp`, `Export: VDB`, `Volume Processing`, `Post Modulation`, `Transform`, `Import`, `Timeline Editor`, `Controls`, `Density`, `Flames`, `Coordinate System`, `Z Up Right Handed`, `Y Up Right Handed`, `Length Unit`, `Export Now`, `Export All`, `Temperature Attribute`, `aiStandardVolume`, and `Principled Volume`.
- The raw-preserving generator now performs a narrow inline punctuation polish after replacement so untranslated punctuation nodes between inline tags render as Chinese punctuation without changing tag structure.

## Manual Spot Audit

- EmberGen and LiquiGen render pass mapping pages were checked for source/destination column wording, render pass ordering, HDR/RAW behavior, output names, channel pin mapping, and source/destination channel examples.
- Histogram wording was checked for density-range visualization, mouse/toolbar icon interactions, `Log Y`, coloring remap range, and `Coloring remap ramp` behavior.
- VDB export wording was checked for `Export: VDB` node setup, Volume output pin connection, `Volume Processing` inclusion, transform alignment, frame-range export, timeline range visibility, channel selection, coordinate system selection, unit settings, batch export, and shader setup in Maya/Blender.
- A visible-text audit fixed missing closing Chinese quotes around UI labels, removed the leaked source anchor marker `.. _vdb:`, normalized inline English-list punctuation, and preserved mouse/reset icons as linked image elements.
- Remaining English is limited to protected UI labels, node names, parameter names, software names, file formats, channel names, shader/attribute names, footer tool names, and generated HTML attributes.

## Validation

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Decision

Stage 3E meets the translation and preservation gates. Proceed to Stage 3F.
