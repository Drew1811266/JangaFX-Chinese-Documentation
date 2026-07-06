# JangaFX Terminology Research Notes

This file records the sources used to recalibrate the terminology review. The goal is not to quote external material into the translation, but to ground term choices before editing the local HTML documents.

## Official Sources Consulted

- JangaFX homepage: describes EmberGen as a real-time volumetric fluid simulation tool that exports flipbooks, image sequences, and VDB volumes; describes LiquiGen as generating flipbooks, image sequences, Alembic caches, foam, spray, and bubbles.
- JangaFX EmberGen product page: frames EmberGen around real-time fire, smoke, explosions, game-ready flipbooks/sprite sheets, image sequence export, VDB export, FBX/Alembic import, volume rendering, and GPU simulation.
- JangaFX LiquiGen product page: frames LiquiGen around real-time liquid simulation, real-time meshing, sparse simulation domains, path tracing, VAT export, mesh flipbooks, and game-ready exports.
- JangaFX EmberGen and LiquiGen Node List pages: primary source for exact node names, parameter labels, and product-specific meanings.
- JangaFX VDB deep-dive article: confirms VDB vocabulary around voxel data, sparse volumes, tree-like data structures, node levels, masks, tiles, grids, transforms, and index/world space.
- OpenVDB overview and tools documentation: confirms sparse volumetric data, grids, active voxels, level sets, signed-distance fields, fog volumes, tiles, topology, and VDB data interpretation.
- NVIDIA OpenVDB/NanoVDB/NeuralVDB material: confirms Chinese usage of `稀疏体积数据`, `体积数据集`, `体素`, `分层网格结构`, and OpenVDB as an industry standard for high-resolution volume data.
- SideFX Houdini FLIP documentation: confirms FLIP as a hybrid particle/volume fluid method with temporary velocity fields and pressure projection.
- SideFX Houdini whitewater documentation: confirms whitewater as secondary liquid effects made of spray, foam, and bubbles; particles are advected through the velocity field and governed by buoyancy, surface tension, adhesion, density control, and lifecycle rules.
- SideFX Houdini Pyro documentation: confirms Pyro as fire/smoke simulation, with density, combustion, flames, smoke, temperature, fuel, dissipation, disturbance, shredding, turbulence, confinement, projection, and advection.
- Unity Chinese Sprite Atlas documentation: confirms `Sprite Atlas` as `精灵图集`; this supports translating `sprite sheet` as `精灵图集` in prose.
- Unreal Engine Flipbook documentation: confirms flipbook textures are used in particle/material workflows; Chinese translation should clarify the concept rather than leaving every mention as bare English.

## Calibrated Chinese Terms

| Domain | English | Preferred Chinese / policy |
| --- | --- | --- |
| Product | JangaFX, EmberGen, LiquiGen, IlluGen, GeoGen | Keep English. |
| Product suite | Elemental Suite | Keep English as a suite name. |
| Game VFX | real-time VFX | `实时 VFX`; expand to `实时视觉特效` where readability improves. |
| Game VFX | flipbook | Prose: `翻页动画`, `翻页序列`, `Flipbook 贴图/序列`; exact UI/export label may keep `Flipbook`. |
| Game VFX | sprite sheet | `精灵图集`; avoid bare English. |
| Game VFX | texture atlas | `纹理图集`. |
| Game VFX | image sequence | `图像序列`. |
| Game VFX | channel packing | `通道打包`. |
| Game VFX | Vertex Animated Texture / VAT | `顶点动画纹理（VAT）`; `VAT` can stay for labels. |
| Volume | volumetric fluid simulation | `体积流体模拟`. |
| Volume | voxel | `体素`. |
| Volume | sparse volume | `稀疏体积`. |
| Volume | VDB volume | `VDB 体积`. |
| Volume | level set | `水平集`. |
| Volume | SDF / signed distance field | `SDF（符号距离场）`. |
| Volume | isosurface | `等值面`. |
| Volume | isovalue | `等值`. |
| VDB | leaf node | `叶节点`. |
| VDB | active voxel | `活动体素`. |
| VDB | background value | `背景值`. |
| Fluid | FLIP | Keep `FLIP`; explain as particle/volume hybrid when needed. |
| Fluid | pressure projection | `压力投影`. |
| Fluid | divergence | `散度`. |
| Fluid | non-divergent | `无散度`. |
| Fluid | volume conservation | `体积守恒`. |
| Fluid | incompressibility | `不可压缩性`. |
| Fluid | advection / advect | `平流`; in particle prose `随速度场平流/输运`. |
| Fluid | velocity field | `速度场`. |
| Fluid | scalar field | `标量场`. |
| Fluid | vector field | `矢量场`. |
| Fluid | whitewater | Category/system: `白水`; particles/system prose: `白水粒子`. |
| Fluid | foam | `泡沫`. |
| Fluid | spray | `飞溅`. |
| Fluid | bubbles | `气泡`. |
| Fluid | viscosity | `黏度`. |
| Fluid | dynamic viscosity coefficient | `动态黏度系数`. |
| Fluid | surface tension | `表面张力`. |
| Fluid | buoyancy | `浮力`. |
| Pyro | pyro | UI/category: keep `Pyro`; prose: `火焰烟雾模拟`. |
| Pyro | combustion | `燃烧`. |
| Pyro | fuel | `燃料`. |
| Pyro | smoke | `烟雾`. |
| Pyro | temperature | `温度`. |
| Pyro | vorticity | `涡量`. |
| Pyro | vortex confinement | `涡旋约束`. |
| Pyro | curl noise | `旋度噪声`. |
| Pyro | dissipation | `耗散`. |
| Pyro | shredding | `撕裂`. |
| Rendering | rasterizer | `光栅化器`. |
| Rendering | path tracer | `路径追踪器`. |
| Rendering | denoiser | `降噪器`. |
| Rendering | photon mapping | `光子映射`. |
| Rendering | caustics | `焦散`. |
| Rendering | sample / samples per pixel | `样本` / `每像素样本数`. |
| Rendering | ray bounce | `光线反弹`. |
| Rendering | Subpixel Morphological Antialiasing | `子像素形态抗锯齿`; acronym `SMAA` stays. |
| UI prose | node | `节点`; exact node names remain English with `节点`. |
| UI prose | parameter | `参数`; exact parameter labels remain English. |
| UI prose | viewport | `视口`. |
| UI prose | timeline | `时间轴`. |
| UI prose | inspector | `检查器`. |

## Over-Retention Heuristic

A translated segment is suspicious when it contains Chinese prose plus multiple non-protected English tokens. The scan should not automatically fail exact UI label lists, node headings, file paths, code fragments, format names, product names, or option names. It should flag prose where English words are doing sentence work, such as:

- `在 Viewport 中调整 simulation parameter`
- `这个 node 会 export flipbook`
- `使用 Path Tracer render caustics`

These should normally become:

- `在视口中调整模拟参数`
- `这个节点会导出翻页序列`
- `使用路径追踪器渲染焦散`

