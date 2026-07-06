# JangaFX Chinese Glossary

This glossary is for translating the local JangaFX documentation with Codex. It is intentionally conservative: exact product names, UI labels, node names, file formats, and code-like identifiers stay in English unless noted.

## Sources Consulted

- JangaFX home and product pages: https://jangafx.com/
- EmberGen product page: https://jangafx.com/software/embergen
- LiquiGen product page: https://jangafx.com/software/liquigen
- IlluGen product page: https://jangafx.com/software/illugen
- GeoGen product page: https://jangafx.com/software/geogen
- JangaFX documentation mirror: https://docs.jangafx.com/
- JangaFX VDB article: https://jangafx.com/insights/vdb-a-deep-dive
- OpenVDB overview: https://www.openvdb.org/documentation/doxygen/overview.html
- Unreal Niagara Flipbook Baker documentation: https://dev.epicgames.com/documentation/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine
- SideFX Houdini VDB/FLIP references: https://www.sidefx.com/docs/houdini/

## Protected Product Names

| English | Chinese policy | Note |
| --- | --- | --- |
| JangaFX | JangaFX | Company/brand, do not translate. |
| EmberGen | EmberGen | Product name, do not translate. |
| LiquiGen | LiquiGen | Product name, do not translate. |
| IlluGen | IlluGen | Product name, do not translate. |
| GeoGen | GeoGen | Product name, do not translate. |
| VectorayGen | VectorayGen | Product name, do not translate. |
| Elemental Suite | Elemental Suite | Suite name, do not translate. |
| TurboFloat Server | TurboFloat Server | Licensing component name. |

## Core VFX Terms

| English | Preferred Chinese | Notes |
| --- | --- | --- |
| real-time VFX | 实时 VFX | Keep VFX. |
| visual effects | 视觉特效 | Use in prose. |
| tech art | 技术美术 | |
| asset generation | 资产生成 | |
| procedural | 程序化 | |
| node-based | 基于节点的 | |
| node graph | 节点图 | |
| node | 节点 | UI node names can stay English, e.g. `Render 节点`. |
| graph | 图 | Usually `节点图`. |
| parameter | 参数 | |
| preset | 预设 | |
| viewport | 视口 | |
| timeline | 时间轴 | |
| keyframe | 关键帧 | |
| animation | 动画 | |
| loop / looping | 循环 | |
| inspector | 检查器 | |
| gizmo | 操控器 | In 3D UI context. |
| manipulator | 变换操控器 | |
| backplate | 背景板 | VFX plate/backplate. |
| live-action plate | 实拍素材板 | |
| render | 渲染 | UI node label can remain `Render`. |
| renderer | 渲染器 | |
| render pass | 渲染通道 | |
| tonemapping | 色调映射 | |
| color grading | 调色 | |
| alpha | Alpha | Keep in channel context. |
| channel | 通道 | |
| mask | 遮罩 | |
| normal map | 法线贴图 | |
| flowmap | 流向贴图 | |
| caustics | 焦散 | |
| distortion | 扭曲 | |
| tiling noise | 平铺噪声 | |
| texture | 纹理 | |
| sprite sheet | 精灵图集 | Avoid bare English in prose. |
| texture atlas | 纹理图集 | Distinguish from sprite sheet / sprite atlas. |
| flipbook | 翻页动画 / 翻页序列 / Flipbook 贴图 | Keep `Flipbook` for exact UI/export labels; avoid bare English in ordinary prose. |
| image sequence | 图像序列 | |
| sequence | 序列 | |
| frame | 帧 | |
| frame rate / FPS | 帧率 / FPS | Keep FPS. |
| frame stride | 帧步长 | |
| cache | 缓存 | |
| Alembic cache | Alembic 缓存 | |
| vertex animated texture | 顶点动画纹理 | VAT stays VAT in abbreviation; explain as `顶点动画纹理（VAT）` in prose when helpful. |
| VAT | VAT | Do not expand every time. |
| mesh flipbook | 网格翻页序列 | Keep `Mesh Flipbook` only for exact UI/export labels. |
| pivot baked mesh | 烘焙枢轴的网格 | |
| RGBA packed | RGBA 打包 | |
| channel packed | 通道打包 | |
| rasterizer | 光栅化器 | |
| path tracer | 路径追踪器 | |
| denoiser | 降噪器 | |
| photon mapping | 光子映射 | |
| sample / samples per pixel | 样本 / 每像素样本数 | |
| ray bounce | 光线反弹 | |
| pixel footprint | 像素足迹 / 像素覆盖范围 | Choose by readability. |
| antialiasing | 抗锯齿 | |
| Subpixel Morphological Antialiasing | 子像素形态抗锯齿 | Acronym `SMAA` stays. |
| scattering | 散射 | |
| absorption | 吸收 | |
| emissive | 自发光 | Preserve `Emissive` as exact UI option label. |

## Simulation And Fluid Terms

| English | Preferred Chinese | Notes |
| --- | --- | --- |
| simulation | 模拟 | |
| fluid simulation | 流体模拟 | |
| volumetric fluid simulation | 体积流体模拟 | |
| volumetric | 体积式 / 体积 | Choose by context. |
| pyro | Pyro / 火焰烟雾模拟 | Keep Pyro for tool/category labels. |
| fire | 火焰 | |
| smoke | 烟雾 | |
| explosion | 爆炸 | |
| wisps | 缕状烟雾 / 飘带状烟雾 | Context dependent. |
| liquid simulation | 液体模拟 | |
| liquid mesh | 液体网格 | |
| foam | 泡沫 | |
| spray | 飞溅 | Whitewater particle type. |
| bubbles | 气泡 | |
| whitewater | 白水 / 白水粒子 | Use `白水` for the category/system and `白水粒子` when referring to particles. |
| trapped air | 受困空气 | LiquiGen diagnostics term for bubble spawn regions. |
| wave crests | 波峰 | LiquiGen diagnostics term for foam spawn regions. |
| particles | 粒子 | |
| voxel | 体素 | |
| voxel size | 体素大小 | Preserve `Voxel size` when used as an exact parameter label. |
| voxel grid | 体素网格 | |
| sparse volume | 稀疏体积 | |
| volume | 体积 | |
| VDB volume | VDB 体积 | |
| OpenVDB | OpenVDB | Do not translate. |
| VDB | VDB | Do not translate. |
| grid | 网格 | For OpenVDB, `体素网格` if clearer. |
| active voxel | 活动体素 | OpenVDB/VDB context. |
| leaf node | 叶节点 | OpenVDB data structure. |
| tile value | 图块值 | OpenVDB term. |
| background value | 背景值 | OpenVDB term. |
| level set | 水平集 | Volume/SDF context. |
| isosurface | 等值面 | |
| isovalue | 等值 | Preserve `Isovalue` only as an exact parameter label. |
| density | 密度 | |
| temperature | 温度 | |
| velocity | 速度 | |
| velocity field | 速度场 | |
| scalar field | 标量场 | |
| vector field | 矢量场 | |
| vorticity | 涡量 | |
| vortex confinement | 涡旋约束 | `涡量约束` is acceptable only if context strongly favors it. |
| curl noise | 旋度噪声 | |
| normal / normals | 法线 | Geometry/mesh direction vectors. |
| SDF | SDF（符号距离场） | Source docs may contain typos; use the standard signed-distance-field term. |
| divergence | 散度 | |
| non-divergent | 无散度 | |
| pressure | 压力 | |
| pressure projection | 压力投影 | |
| viscosity | 黏度 | |
| dynamic viscosity coefficient | 动态黏度系数 | |
| stickiness | 黏附性 | Preserve `Stickiness` when used as an exact parameter label. |
| surface tension | 表面张力 | |
| reflectivity | 反射率 | |
| refraction / refractive | 折射 / 折射的 | |
| buoyancy | 浮力 | |
| dissipation | 耗散 | |
| diffusion | 扩散 | |
| shredding | 撕裂 | Fluid shaping term. |
| advection / advect | 平流 | In particle prose, `随速度场平流/输运` may read better. |
| combustion | 燃烧 | |
| timestep | 时间步长 | |
| substep | 子步 | |
| solver | 求解器 | |
| projection iterations | 投影迭代次数 | |
| multigrid | 多重网格 | 压力投影/求解器上下文；不要在中文说明句中裸保留英文。 |
| SOR | SOR | 求解器算法缩写，可保留。 |
| Vertex-stencil correction | 顶点模板校正 | 求解器说明上下文。 |
| divergence target | 散度目标 | |
| volume conservation | 体积守恒 | |
| incompressibility | 不可压缩性 | |
| collider | 碰撞体 | |
| emitter | 发射器 | |
| holdout object | 遮挡对象 | Rendering holdout. |
| force | 力 | |
| force velocity | 力场速度 | Diagnostics visualization context. |
| wind | 风 | |
| falloff | 衰减 | |
| domain | 域 | Simulation domain. |
| bounds | 边界范围 | |
| tile | 图块 | LiquiGen diagnostics: 8 x 8 x 8 voxel simulation tile. |
| bounding box | 边界框 | |

## UI And Workflow Terms

| English | Preferred Chinese | Notes |
| --- | --- | --- |
| Getting Started | 入门 | Page title. |
| References | 参考 | Page title. |
| User Interface | 用户界面 | |
| Settings | 设置 | |
| Preferences | 首选项 | Use for application-level preferences. |
| Node List | 节点列表 | |
| How-To Guides | 操作指南 | |
| FAQ | 常见问题 | |
| Floating License Guide | 浮动许可证指南 | |
| Search | 搜索 | |
| Contents | 目录 | |
| Back to top | 返回顶部 | |
| Next | 下一页 | |
| Previous | 上一页 | |
| Toggle | 切换 | |
| dropdown menu | 下拉菜单 | |
| checkbox | 复选框 | |
| slider | 滑块 | |
| range slider | 范围滑块 | |
| text field | 文本字段 | |
| button | 按钮 | |
| tab | 选项卡 | |
| panel | 面板 | |
| properties panel | 属性面板 | |
| node details | 节点详情 | |
| favorites | 收藏项 | |
| auto-favorite | 自动收藏 | |
| randomized | 随机化 | |
| diagnostics | 诊断 | |
| diagnostics panel | 诊断面板 | |
| histogram | 直方图 | |
| modulation curve | 调制曲线 | |
| modulator | 调制器 | |
| oscillator | 振荡器 | |
| ADSR | ADSR | Attack（起音）、Decay（衰减）、Sustain（延音）、Release（释音），保留缩写。 |
| MIDI | MIDI | Do not translate. |
| expression | 表达式 | |
| operator | 运算符 | Expressions page. |
| constant | 常量 | Expressions page. |
| function | 函数 | Expressions page. |
| argument | 参数 | Function argument count. |
| randomization | 随机化 | |
| read-only copy | 只读副本 | Project settings workflow. |
| thumbnail | 缩略图 | |
| shortcut | 快捷键 | |
| key-bind | 按键绑定 | |
| minimap | 小地图 | Node graph overview. |
| user variable | 用户变量 | Export path variable. |
| autosave | 自动保存 | |
| field shading | 场着色 | Preserve `Field Shading` when used as an exact UI label. |
| remap range | 重映射范围 | |
| sparsity | 稀疏度 | Diagnostics arrow density control. |
| slice | 切片 | Diagnostics 2D visualization plane. |
| arrow | 箭头 | Diagnostics vectors. |
| albedo | Albedo / 反照率 | Preserve `Albedo` for exact UI/color labels. |
| color palette | 调色板 / 色板 | Use for saved colors or color swatches. |
| Command / Parameter / Project Palette | 命令面板 / 参数面板 / 项目面板 | These are quick popup windows in the JangaFX UI, not color palettes. |
| import | 导入 | |
| export | 导出 | |
| camera import | 摄像机导入 | |
| render pass mapping | 渲染通道映射 | |
| Interpolation Color Space | 插值颜色空间 | Preserve exact UI label with Chinese explanation. |
| RGB Mode | RGB 模式 | Red（红）、Green（绿）、Blue（蓝）。 |
| HSV Mode | HSV 模式 | Hue（色相）、Saturation（饱和度）、Value（明度）。 |
| VDB export | VDB 导出 | |
| FBX, OBJ, ABC Import | FBX、OBJ、ABC 导入 | |
| Timeline Editor | 时间轴编辑器 | Preserve the exact UI label when it appears as a control name. |
| Timeline Override | Timeline Override（时间轴覆盖） | Preserve UI label; add Chinese explanation when useful. |
| Timeline Recording | 时间轴录制 | Preserve exact icon/button label when adjacent to an icon. |
| Toggle Timeline Autokey | Toggle Timeline Autokey（切换时间轴自动关键帧） | Preserve UI label. |
| Snap keys to frames | Snap keys to frames（将关键帧吸附到帧） | Preserve UI label. |
| Curve Editor | 曲线编辑器 | Preserve exact UI label when it appears as a control name. |
| Interpolation Mode | 插值模式 | |
| Constant / Linear / Smooth / Bézier | Constant / Linear / Smooth / Bézier | Preserve UI option labels; explain in Chinese prose. |
| Aligned / Free / Auto Clamped / Auto Vectored | Aligned / Free / Auto Clamped / Auto Vectored | Preserve Bézier handle type labels. |
| Fit View | Fit View（适配视图） | Preserve UI label. |
| Snap To Frames | Snap To Frames（吸附到帧） | Preserve UI label. |
| Reset Handle | Reset Handle（重置手柄） | Preserve UI label. |
| clipping plane | 裁剪平面 | Camera near/far clipping range. |
| skybox | 天空盒 | Preserve `skybox` in exact UI labels, add Chinese explanation in prose. |

## File Formats And Software Terms

| English | Preferred Chinese | Notes |
| --- | --- | --- |
| FBX | FBX | Do not translate. |
| OBJ | OBJ | Do not translate. |
| ABC | ABC | Alembic extension, do not translate. |
| Alembic | Alembic | Do not translate. |
| OGAWA | OGAWA | Alembic backend, do not translate. |
| EXR | EXR | Do not translate. |
| multi-layer EXR | 多层 EXR | |
| multi-part EXR | 多 Part EXR | Keep Part if referring to EXR structure. |
| PNG | PNG | Do not translate. |
| TGA | TGA | Do not translate. |
| HDR | HDR | Do not translate. |
| macOS | macOS | Use Apple's casing. |
| Windows | Windows | |
| Linux | Linux | |
| 3D package | 3D 软件包 | |
| Unreal Engine | Unreal Engine | |
| Unity | Unity | |
| Houdini | Houdini | |

## Licensing Terms

| English | Preferred Chinese | Notes |
| --- | --- | --- |
| license | 许可证 | |
| floating license | 浮动许可证 | |
| license server | 许可证服务器 | |
| activation | 激活 | |
| seat | 席位 | |
| server address | 服务器地址 | |
| environment variable | 环境变量 | |
| firewall rule | 防火墙规则 | |
