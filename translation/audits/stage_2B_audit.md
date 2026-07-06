# Stage 2B Audit - LiquiGen Getting Started

## Scope

- `liquigen/pages/getting_started.html`

## Result

Status: Pass.

## Coverage

- Translated segments: 566 / 566
- Exact UI labels, node names, parameter names, shortcuts, paths, URLs, product names, and footer tool names are intentionally preserved where appropriate.
- Protected examples include `Download LiquiGen`, `Launch LiquiGen`, `License Manager…`, `Simulation`, `Mesh`, `Liquid Appearance`, `Liquid Mesh`, `Liquid Particles`, `Shape: Primitive`, `Emitter`, `Collider`, `Force: Turbulence`, `Export: Image`, `Export: Mesh`, `Ctrl + T`, `Sphinx`, `@pradyunsg`, and `Furo`.

## Manual Spot Audit

- Installation and licensing sections preserve exact installer and license-manager UI labels; the installer `Next` buttons were corrected after audit to avoid the navigation meaning “下一页”.
- Project Manager and UI sections were checked for icon-split phrasing. The Home icon sentence was corrected so the clickable icon remains in the right grammatical position.
- LiquiGen simulation terminology follows the glossary: `混合求解器`, `粒子`, `体素`, `网格化`, `液体网格`, `液体着色器`, `稀疏求解器`, `速度`, `压力`, `散度`, and `力场`.
- Node headings keep the English node label and add Chinese clarification, for example `Emitter（发射器）`, `Collider（碰撞体）`, `Force（力）`, `Drain（排水）`, and `Export: Mesh（导出网格）`.
- Render, Export, Camera, and Mesh Export sections preserve exact UI and parameter labels while translating explanatory prose.
- A visible-text scan found no remaining English prose paragraphs; remaining English is limited to protected labels, product names, URLs, shortcuts, file names, and Sphinx/Furo footer names.

## Validation

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## Decision

Stage 2B meets the translation and preservation gates. Stage 2 is complete. Proceed to Stage 3.
