# 排版与媒体一致性审计 - JangaFX 中文 HTML 文档

日期：2026-07-06

## 目标

审查 `jangafx-docs-zh` 翻译后文档的整体排版、图片、GIF、视频等媒体元素是否与原始官方镜像 `jangafx-docs` 几乎保持一致。

## 审查范围

- 原始镜像：`jangafx-docs`
- 中文输出：`jangafx-docs-zh`
- HTML 页面：62 / 62
- 比较视口：
  - desktop：1366 x 768
  - mobile：390 x 844
- 浏览器：Google Chrome headless，通过 `playwright-core` 驱动
- 审查脚本：`tools/jangafx_layout_audit.cjs`
- 自动化报告：
  - `translation/reports/layout/layout_audit.json`
  - `translation/reports/layout/layout_audit.md`

## 方法

1. 以 `python3 tools/jangafx_translate.py apply --clean` 干净重建中文输出目录，确保中文目录仅来自原始镜像复制和翻译文本替换。
2. 运行结构校验，确认标签、本地链接和资源引用未损坏。
3. 启动两个本地静态服务器，分别服务原始镜像和中文镜像。
4. 用浏览器逐页打开原文/中文页面，提取渲染后的 DOM 指标：
   - 正文媒体元素数量、顺序、资源路径、尺寸和位置
   - 关键容器位置与宽度：正文、文章容器、侧栏、右侧目录等
   - 横向溢出情况
5. 对代表页面生成原文/中文截图证据，保存到 `output/playwright/layout-audit/`。

## 最终结构校验

```text
Applied 17648 translated segments across 62 pages.
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

## 自动化审查结果

```text
Compared 62 pages across 2 viewports.
Issues by severity: {"medium":28}
```

详细指标：

- 原始镜像页面数：62
- 中文镜像页面数：62
- 页面/视口比较数：124
- 正文显著媒体数量：1022 / 1022
- 正文全部媒体数量：3518 / 3518
- 高风险问题：0
- 中风险候选：28
- 低风险问题：0

## 通过项

- 页面数量一致，没有缺页或多页。
- 正文图片、GIF、视频等媒体总量一致。
- 显著正文媒体的资源路径、DOM 顺序和尺寸一致。
- 未发现媒体丢失、替换、乱序或尺寸被翻译破坏。
- 未发现关键页面容器宽度、侧栏、右侧目录等骨架布局被破坏。
- 未发现中文输出比原文多出的横向溢出回归。
- 移动端没有媒体水平漂移候选。

## 保留差异

最终剩余 28 个中风险候选全部属于桌面端 `significant_media_box`，即媒体水平位置与原文不同，但资源、顺序和尺寸仍一致。

这些差异集中在官方文档本身使用的浮动布局：

- `.float-right` 视频或图片
- 紧跟在右浮动图片之后的视频块
- 长页面中受前文浮动和文本长度影响的媒体块

原因是中文翻译后的段落长度与英文不同，浏览器浮动布局会根据当前文本流重新计算可用空间。部分中文段落更短，使后续右浮动视频更早遇到前一个未清除的右浮动图片，于是浏览器把视频排到左侧或中间。该差异来自 HTML/CSS 浮动布局与翻译文本长度的自然交互，不是翻译管线损坏标签或移动媒体节点。

典型候选页面：

- `embergen/pages/getting_started.html`
- `embergen/pages/references/node_list.html`
- `liquigen/pages/getting_started.html`
- `liquigen/pages/references/How-To Guides/animation.html`
- `liquigen/pages/references/How-To Guides/comment.html`
- `liquigen/pages/references/How-To Guides/diagnostics.html`
- `liquigen/pages/references/How-To Guides/modulation_curve.html`
- `liquigen/pages/references/node_list.html`

## 修复尝试与决定

曾测试过在中文输出中给视频容器增加全局清除浮动规则，以减少前序浮动对后续视频的影响。测试结果从 28 个中风险候选上升到 45 个，说明全局 CSS 修复会让更多页面偏离原始官方布局。因此该修复已撤回，最终中文输出不保留额外 CSS 排版覆盖。

当前更稳妥的判断是：

- 不做全局 CSS 改写。
- 保持官方 HTML/CSS 结构。
- 接受由翻译文本长度导致的少量桌面端浮动重排。
- 如需达到像素级一致，应逐页对 28 个候选媒体周边的文本或浮动结构做人工排版重写；这会牺牲 raw-preserving 翻译策略，不建议作为默认处理。

## 截图证据

代表页面截图保存于：

- `output/playwright/layout-audit/desktop__original__index.png`
- `output/playwright/layout-audit/desktop__zh__index.png`
- `output/playwright/layout-audit/desktop__original__licensing__index.png`
- `output/playwright/layout-audit/desktop__zh__licensing__index.png`
- `output/playwright/layout-audit/desktop__original__embergen__pages__references__node_list.png`
- `output/playwright/layout-audit/desktop__zh__embergen__pages__references__node_list.png`
- `output/playwright/layout-audit/desktop__original__liquigen__pages__references__node_list.png`
- `output/playwright/layout-audit/desktop__zh__liquigen__pages__references__node_list.png`
- `output/playwright/layout-audit/mobile__original__index.png`
- `output/playwright/layout-audit/mobile__zh__index.png`

完整截图清单见 `translation/reports/layout/layout_audit.md`。

## 结论

结论：有条件通过。

中文文档在页面骨架、HTML 结构、媒体资源、媒体顺序、媒体尺寸和移动端布局上与原官方镜像保持一致。它不是像素级完全一致；桌面端存在 28 个由官方浮动布局和中文文本重排共同造成的媒体水平位置差异。该差异不代表媒体丢失或版式损坏，但如果目标升级为“逐像素或逐媒体坐标一致”，需要对这些候选页面做人工排版级重写。
