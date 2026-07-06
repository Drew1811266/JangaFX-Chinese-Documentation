# Stage 7 Audit - Licensing, Search, Index, And Cleanup

Date: 2026-07-06

## Scope

- Main page: `licensing/index.html`
- Cleanup pages:
  - `index.html`
  - `embergen/index.html`
  - `liquigen/index.html`
  - `geogen/index.html`
  - `illugen/index.html`
  - `embergen/pages/FAQ.html`
  - `embergen/pages/getting_started.html`
  - `liquigen/pages/FAQ.html`
  - `genindex.html`
  - `search.html`

## Result

- All 62 translation page JSON files are marked `translated`.
- `licensing/index.html`: 290 / 290 segments, `translated`.
- Stage result: pass.

## Validation

Command:

```bash
python3 tools/jangafx_translate.py apply
python3 tools/jangafx_translate.py validate
```

Result:

```text
Applied 17648 translated segments across 62 pages.
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Spot Audit

Reviewed generated visible text for:

- JangaFX Floating Server: version requirements, download table, overview, command-line launch, options, and Windows service sections.
- Client quick start: License Manager workflow, environment variables, and lease behavior.
- Legacy Floating Server: quick start commands, offline activation, logs, troubleshooting, custom paths, and firewall-rule uninstall issue.
- Search/index cleanup pages and landing-page residual labels.

Checks performed:

- Confirmed licensing terminology follows the glossary: `许可证`, `浮动许可证`, `许可证服务器`, `租约`, `激活`, `停用`, `环境变量`, and `防火墙规则`.
- Confirmed command names, flags, paths, executable names, environment variables, URLs, and exact product names remain protected.
- Confirmed search/index pages have Chinese titles and visible UI fallback text.
- Ran a visible-text scan for obvious untranslated English prose; remaining hits were command examples, paths, URLs, product names, or exact UI/code labels.

## Notes

- Some exact UI labels remain in English by policy, such as `License Manager`, command flags, executable names, and environment variable names.
- `tools/jangafx_translate.py` includes narrow post-apply polish for inline Sphinx fragments and code/link punctuation, preserving the original HTML tag sequence.
