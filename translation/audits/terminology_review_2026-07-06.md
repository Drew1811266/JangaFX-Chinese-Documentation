# Terminology Review Audit - JangaFX Chinese HTML Docs

Date: 2026-07-06

## Objective

Review the translated JangaFX HTML documentation for professional terminology accuracy and over-retained English. This audit focuses on whether technical terms were translated consistently, whether exact UI/product identifiers were preserved correctly, and whether Chinese prose avoided unnecessary English words.

## Scope

- Chinese output: `jangafx-docs-zh`
- Translation sources: `translation/pages/*.json` and `translation/segments/*.json`
- HTML files reviewed by scanner: 62
- Translation segments scanned: 17,655
- Translated segments applied: 17,648
- Review policy files:
  - `translation/glossary.zh-CN.md`
  - `translation/terminology_research.md`
  - `translation/translation_policy.md`
- Scanner:
  - `tools/jangafx_terminology_audit.py`

## Research Basis

The terminology policy was recalibrated before editing. Sources used:

- JangaFX product and documentation pages:
  - `https://jangafx.com/`
  - `https://jangafx.com/software/embergen`
  - `https://jangafx.com/software/liquigen`
  - `https://docs.jangafx.com/`
  - `https://jangafx.com/insights/vdb-a-deep-dive`
- OpenVDB documentation:
  - `https://www.openvdb.org/documentation/doxygen/overview.html`
- NVIDIA OpenVDB/NanoVDB/NeuralVDB Chinese material:
  - `https://developer.nvidia.cn/blog/optimizing-large-scale-sparse-volumetric-data-with-nvidia-neuralvdb-early-access/`
- SideFX Houdini references for FLIP, Pyro, VDB, pressure projection, and whitewater terminology:
  - `https://www.sidefx.com/docs/houdini/`
- Unity Chinese Sprite Atlas terminology:
  - `https://docs.unity3d.com/cn/`
- Unreal Engine Flipbook workflow terminology:
  - `https://dev.epicgames.com/documentation/unreal-engine/`

## Review Method

1. Calibrated the glossary from official JangaFX terminology and adjacent industry references.
2. Built and ran an HTML-aware terminology scanner over all extracted translation segments.
3. Reviewed scanner candidates manually by context, separating real terminology issues from protected labels and false positives caused by inline HTML fragment splitting.
4. Corrected high-risk and readability-affecting terms in the translation JSON, then regenerated `jangafx-docs-zh`.
5. Re-ran structural validation and terminology scanning after each correction batch.

## Term Decisions

- Product names and suite names stay English: `JangaFX`, `EmberGen`, `LiquiGen`, `IlluGen`, `GeoGen`, `Elemental Suite`.
- Exact UI labels, node names, option labels, file formats, code identifiers, and command/error messages are preserved, normally with Chinese explanation on first meaningful use.
- Ordinary prose terms are translated into Chinese:
  - `node graph` -> `节点图`
  - `viewport` -> `视口`
  - `render pass` -> `渲染通道`
  - `path tracer` -> `路径追踪器`
  - `rasterizer` -> `光栅化器`
  - `flipbook` -> `翻页动画` / `翻页序列` / `Flipbook 贴图`
  - `sprite sheet` -> `精灵图集`
  - `whitewater` -> `白水` / `白水粒子`
  - `advection` -> `平流`
  - `divergence` -> `散度`
  - `pressure projection` -> `压力投影`
  - `vorticity` -> `涡量`
  - `curl noise` -> `旋度噪声`
  - `multigrid` -> `多重网格`
  - `Vertex-stencil correction` -> `顶点模板校正`

## Corrections Applied

- Standardized `flipbook`, `mesh flipbook`, `PNG Flipbook`, and `sprite sheet` around `翻页序列/翻页动画贴图/精灵图集`.
- Standardized LiquiGen whitewater terms around `白水`, `白水粒子`, `飞溅`, `泡沫`, and `气泡`.
- Corrected simulation and solver terms including `平流`, `燃烧`, `涡量`, `撕裂`, `投影迭代`, `黏度`, `表面张力`, `散度`, `多重网格`, and `顶点模板校正`.
- Annotated UI-heavy labels where the exact English label should remain, for example `Node Details（节点详情）`, `Timeline（时间轴）`, `Render Passes（渲染通道）`, `Path Tracer（路径追踪器）`, `Rasterizer（光栅化器）`.
- Reduced over-retained English in explanatory prose while preserving exact UI labels, keyboard shortcuts, software names, and original error messages.

## Final Validation

Structural validation after the final terminology pass:

```text
Applied 17648 translated segments across 62 pages.
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

Final terminology scan:

```text
Pages scanned: 62
Segments scanned: 17655
Candidate findings: 14
Findings by severity: {'low': 14}
Findings by type: {'mixed_readability': 10, 'missing_preferred_translation': 4}
```

No high or medium severity terminology findings remain.

## Accepted Residual Low Findings

The remaining 14 low-severity scanner candidates were reviewed and accepted:

- Keyboard shortcuts: `Q`, `W`, `E`.
- Software and renderer identifiers: `Maya`, `Blender`, `aiStandardVolume`, `Principled Volume`, `3D`.
- Exact Windows error message:
  - `Failed to remove this service from the Windows Firewall. 0x80070057`
- Exact UI labels already annotated with Chinese, such as:
  - `Box Evenly Distributed On X,Y,Z（盒形按 X/Y/Z 均匀分布）`
  - `Temperature, Velocity, Smoke, Flames, Fuel dissipation (*)（温度、速度、烟雾、火焰、燃料耗散乘数）`
  - `Smoke, Temperature, Fuel, Flames（烟雾、温度、燃料、火焰）`
  - `Post Processed Smoke, Temperature, Fuel, Flames（后处理后的烟雾、温度、燃料、火焰）`
  - `Pre Processed Smoke, Temperature, Fuel, Flames（处理前的烟雾、温度、燃料、火焰）`
- Inline HTML segmentation false positives where `node` is split away from the adjacent translated fragment; rendered Chinese context remains readable.

## Result

Pass.

The JangaFX Chinese HTML documentation now has a calibrated terminology policy, a reproducible terminology scanner, updated glossary entries, and a validated output build. Remaining English is intentional and limited to protected product/software identifiers, exact UI labels, keyboard shortcuts, file/format-like identifiers, and literal error messages.
