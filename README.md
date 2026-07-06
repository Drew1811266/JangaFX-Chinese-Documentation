# JangaFX 中文文档本地镜像

这是一个针对 JangaFX 官方 HTML 文档的中文本地化项目。项目保留原始文档的 HTML/CSS/图片/GIF/视频等资源结构，通过一套 raw-preserving 翻译管线只替换可翻译文本节点，从而最大程度降低翻译过程对页面结构和版式的破坏。

> 说明：本项目不是 JangaFX 官方项目。原始文档、产品名称、图像、视频和相关素材版权归 JangaFX 及其权利方所有。本仓库仅用于本地学习、翻译审校和文档阅读工作流验证。

## 项目状态

| 项目 | 状态 |
| --- | --- |
| 原始文档镜像 | 已下载到 `jangafx-docs` |
| 中文文档输出 | 已生成到 `jangafx-docs-zh` |
| 翻译覆盖范围 | 62 个 HTML 页面，17,655 个文本片段 |
| 结构校验 | 通过，0 个标签不匹配，0 个本地链接/资源缺失 |
| 术语审查 | 通过，无高/中风险术语问题 |
| 排版与媒体审查 | 有条件通过，媒体数量、顺序、路径、尺寸一致 |

## 功能特点

- 保留原始 JangaFX 文档站点结构，包括 Sphinx/Furo 页面框架、侧栏、目录、搜索页、图片、SVG、GIF 和视频资源。
- 使用文本节点级翻译替换，不通过 DOM 序列化重写整页 HTML。
- 维护 JangaFX/VFX/流体模拟/体积数据/渲染相关中文术语库。
- 提供结构校验、术语审查、排版与媒体一致性审查脚本。
- 保留分阶段翻译计划、进度记录、审计报告和机器可读 JSON 报告。

## 目录结构

```text
.
├── jangafx-docs/                  # 原始英文文档镜像
├── jangafx-docs-zh/               # 已生成的中文文档
├── tools/
│   ├── jangafx_translate.py       # 文本提取、应用翻译、结构校验
│   ├── jangafx_terminology_audit.py
│   └── jangafx_layout_audit.cjs
├── translation/
│   ├── pages/                     # 每页翻译 JSON
│   ├── segments/                  # 从 HTML 提取的文本片段
│   ├── audits/                    # 阶段审计与专项审计
│   ├── reports/                   # 自动化报告
│   ├── glossary.zh-CN.md          # 中文术语库
│   ├── translation_policy.md      # 翻译策略
│   ├── stage_plan.md              # 分阶段计划
│   └── progress.md                # 当前进度记录
└── output/playwright/             # 浏览器截图审查证据
```

## 快速开始

在项目根目录启动本地静态服务器：

```bash
python3 -m http.server 8765 --bind 127.0.0.1 --directory jangafx-docs-zh
```

然后在浏览器打开：

```text
http://127.0.0.1:8765/index.html
```

如果只想直接打开本地文件，也可以打开：

```text
jangafx-docs-zh/index.html
```

建议优先使用本地 HTTP 服务器，因为搜索页、脚本和部分静态资源在网页服务环境下更接近真实文档站点行为。

## 常用命令

重新生成中文文档：

```bash
python3 tools/jangafx_translate.py apply --clean
```

校验 HTML 标签和本地链接/资源：

```bash
python3 tools/jangafx_translate.py validate
```

运行术语与英文残留审查：

```bash
python3 tools/jangafx_terminology_audit.py --limit 220
```

运行排版与媒体一致性审查：

```bash
NODE_PATH="$PWD/.codex-layout-deps/node_modules" node tools/jangafx_layout_audit.cjs
```

如果 `.codex-layout-deps` 不存在，可先安装浏览器自动化依赖：

```bash
pnpm add --dir .codex-layout-deps playwright-core
```

排版审查需要本机可用的 Google Chrome。

## 翻译工作流

1. 从 `jangafx-docs` 提取 HTML 文本片段。
2. 在 `translation/pages/*.json` 中维护每页译文。
3. 使用 `tools/jangafx_translate.py apply` 将译文应用到 `jangafx-docs-zh`。
4. 使用 `validate` 校验标签、链接和资源引用。
5. 使用术语审查脚本检查专业名词准确性和过度保留英文问题。
6. 使用浏览器布局审查脚本对比原文与中文文档的媒体和布局表现。
7. 将阶段结论记录到 `translation/audits/` 和 `translation/progress.md`。

## 质量审查结果

### 结构校验

最新结构校验结果：

```text
HTML files checked: 62
Tag mismatches: 0
Missing local links/assets: 0
```

### 术语审查

术语库参考了 JangaFX、OpenVDB、SideFX Houdini、Unreal Engine、Unity 等相关资料，重点校准了以下领域：

- 实时 VFX 与游戏特效导出
- Flipbook、Sprite Sheet、VAT、VDB、OpenVDB
- 流体模拟、FLIP、Whitewater、Pyro
- 体素、SDF、水平集、速度场、散度、压力投影
- 光栅化、路径追踪、渲染通道、抗锯齿、焦散
- JangaFX 节点图、参数、面板和 UI 标签

最终术语扫描无高/中风险问题，剩余低风险项均已人工接受，主要是快捷键、软件名、精确 UI 标签、原始错误消息和 HTML 片段切分误报。

详细报告：

- `translation/audits/terminology_review_2026-07-06.md`
- `translation/reports/terminology_scan.md`
- `translation/glossary.zh-CN.md`

### 排版与媒体审查

浏览器级审查比较了 62 个页面在桌面与移动视口下的渲染表现：

- 页面数量一致
- 正文显著媒体数量一致：1022 / 1022
- 正文全部媒体数量一致：3518 / 3518
- 媒体资源路径、DOM 顺序和尺寸一致
- 未发现媒体丢失、替换、乱序或尺寸破坏
- 移动端无媒体水平漂移候选

桌面端保留 28 个中风险候选，原因是官方文档使用浮动媒体布局，中文文本长度变化会导致浏览器重新计算浮动元素落位。这不是媒体节点损坏，也不是资源丢失；如需像素级一致，需要逐页进行人工排版级重写。

详细报告：

- `translation/audits/layout_review_2026-07-06.md`
- `translation/reports/layout/layout_audit.md`
- `translation/reports/layout/layout_audit.json`

## 设计原则

- 优先保护 HTML 结构，而不是追求文本替换速度。
- 产品名、文件格式、代码标识符、环境变量、路径、URL 和精确 UI 标签默认保留。
- 普通说明性文字尽量使用自然中文，避免整句夹杂大量英文术语。
- 专业术语遵循 `translation/glossary.zh-CN.md`。
- 不对原始 CSS 做全局重写，除非审计证明收益明确且不会扩大版式偏差。

## 维护指南

如果上游 JangaFX 文档更新，建议按以下顺序维护：

1. 更新或重新下载 `jangafx-docs`。
2. 运行 `python3 tools/jangafx_translate.py extract` 更新片段。
3. 复用已有翻译记忆和页面 JSON，补齐新增片段。
4. 运行 `python3 tools/jangafx_translate.py apply --clean`。
5. 运行 `python3 tools/jangafx_translate.py validate`。
6. 运行术语审查和排版审查。
7. 更新 `translation/progress.md` 与对应审计报告。

## 参考资料

README 的组织方式参考了常见 GitHub 项目文档实践，尤其是项目简介、快速开始、使用方式、质量状态、维护指南和许可证说明等结构：

- GitHub Docs：`https://docs.github.com/`
- Make a README：`https://www.makeareadme.com/`
- Awesome README：`https://github.com/matiassingers/awesome-readme`
- README Best Practices：`https://github.com/jehna/readme-best-practices`

项目术语和翻译策略主要参考：

- JangaFX 官方网站与文档：`https://jangafx.com/`、`https://docs.jangafx.com/`
- OpenVDB 文档：`https://www.openvdb.org/documentation/doxygen/overview.html`
- SideFX Houdini 文档：`https://www.sidefx.com/docs/houdini/`

## 版权与使用说明

本项目包含从 JangaFX 官方文档镜像而来的页面和媒体资源。请在使用、发布或分发前确认你拥有相应授权。中文翻译、术语库、审查脚本和本地工作流记录仅用于本地化、学习和审校目的。
