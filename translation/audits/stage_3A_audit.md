# Stage 3A Audit - How-To Guide Basics

## Scope

- `embergen/pages/references/How-To Guides/index.html`
- `liquigen/pages/references/How-To Guides/index.html`
- `embergen/pages/references/How-To Guides/comment.html`
- `liquigen/pages/references/How-To Guides/comment.html`
- `embergen/pages/references/How-To Guides/note.html`
- `liquigen/pages/references/How-To Guides/note.html`
- `embergen/pages/references/How-To Guides/palettes.html`
- `liquigen/pages/references/How-To Guides/palettes.html`
- `embergen/pages/references/How-To Guides/rangeSlider.html`
- `liquigen/pages/references/How-To Guides/rangeSlider.html`

## Result

Status: Pass.

## Coverage

- Translated segments: 995 / 995 across the 10 Stage 3A pages.
- A terminology correction was applied globally: `Palettes` in the Command/Parameter/Project Palette context is now `快捷面板`, not `调色板`.
- Exact UI labels and shortcuts are intentionally preserved, including `Create Comment`, `Create Note`, `Set Comment Text`, `Select Content`, `Set Color`, `Tidy Up`, `Delete`, `Command Palette`, `Parameter Palette`, `Project Palette`, `Ctrl + Return`, `Ctrl + P`, `Ctrl + Shift + O`, `Return`, and `Esc`.

## Manual Spot Audit

- Comment and Note guides were checked for icon-split phrasing. The visible HTML keeps mouse-button icons in the right grammatical position.
- Palette terminology was corrected and spot-checked in both EmberGen and LiquiGen pages.
- Range Slider pages were checked as full Chinese prose because they contain few protected English labels.
- A visible-text scan found no remaining English explanatory prose in the Stage 3A pages. Remaining English is limited to protected UI labels, shortcuts, product names, URLs, and footer tool names.
- Remaining `Palettes` matches are in HTML metadata/title attributes on pages outside this batch and are deferred to the final metadata polish stage.

## Validation

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Decision

Stage 3A meets the translation and preservation gates. Proceed to Stage 3B.
