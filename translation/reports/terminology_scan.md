# JangaFX Terminology Scan Report

This is an automated candidate list. Each finding still needs contextual review before any translation edit.

## Summary

- Pages scanned: 62
- Segments scanned: 17655
- Translated segments: 17648
- Candidate findings: 14
- Findings by severity: {'low': 14}
- Findings by type: {'mixed_readability': 10, 'missing_preferred_translation': 4}

## Top Candidates

### LOW - mixed_readability - Q, W, E

- Page: `embergen/pages/getting_started.html`
- Segment index: `322`
- Source: Q, W, and E
- Target: Q、W 和 E
- Expected: reduce English-token density in Chinese prose

### LOW - mixed_readability - Maya, aiStandardVolume, Blender

- Page: `embergen/pages/references/How-To Guides/exportVDB.html`
- Segment index: `121`
- Source: When using the aiStandardVolume in Maya or the Principled Volume in Blender you have to change the 
- Target: 在 Maya 中使用 aiStandardVolume 或在 Blender 中使用 Principled Volume（Principled 体积着色器）时，需要将 
- Expected: reduce English-token density in Chinese prose

### LOW - missing_preferred_translation - node

- Page: `embergen/pages/references/node_list.html`
- Segment index: `2715`
- Source:  node which should be used to connect a 
- Target: 应将 
- Expected: 节点

### LOW - missing_preferred_translation - node

- Page: `embergen/pages/references/node_list.html`
- Segment index: `2789`
- Source:  node which should be used to connect a 
- Target: 应将 
- Expected: 节点

### LOW - mixed_readability - Box, Evenly, Distributed, On, X, Y

- Page: `embergen/pages/references/node_list.html`
- Segment index: `3054`
- Source: Box Evenly Distributed On X,Y,Z: Shapes will be spawned randomly within the box shape but evenly distibuted over the specified axis. This can reduce cluttering in the specified axis.
- Target: Box Evenly Distributed On X,Y,Z（盒形按 X/Y/Z 均匀分布）：形状会在盒形内随机生成，但会沿指定轴均匀分布。这可以减少指定轴上的堆积。
- Expected: reduce English-token density in Chinese prose

### LOW - mixed_readability - Temperature, Velocity, Smoke, Flames, Fuel, dissipation

- Page: `embergen/pages/references/node_list.html`
- Segment index: `3737`
- Source: Temperature, Velocity, Smoke, Flames, Fuel dissipation (*):
- Target: Temperature, Velocity, Smoke, Flames, Fuel dissipation (*)（温度、速度、烟雾、火焰、燃料耗散乘数）：
- Expected: reduce English-token density in Chinese prose

### LOW - mixed_readability - Smoke, Temperature, Fuel

- Page: `embergen/pages/references/node_list.html`
- Segment index: `3979`
- Source: Smoke, Temperature, Fuel, Flames: Modulation based on a simulation channel. This is after post-processing (like sharpen,motion blur, dilation) and post-modulation if there is another post modulation before this one.
- Target: Smoke, Temperature, Fuel, Flames（烟雾、温度、燃料、火焰）：基于模拟通道的调制。它位于后处理之后（例如 sharpen（锐化）、motion blur（运动模糊）、dilation（膨胀））；如果前面还有另一个 post modulation（后调制），则也位于该后调制之后。
- Expected: reduce English-token density in Chinese prose

### LOW - mixed_readability - Post, Processed, Smoke, Temperature, Fuel

- Page: `embergen/pages/references/node_list.html`
- Segment index: `3983`
- Source: Post Processed Smoke, Temperature, Fuel, Flames: Channel after post-processing but before post-modulation.
- Target: Post Processed Smoke, Temperature, Fuel, Flames（后处理后的烟雾、温度、燃料、火焰）：后处理之后、后调制之前的通道。
- Expected: reduce English-token density in Chinese prose

### LOW - mixed_readability - Pre, Processed, Smoke, Temperature, Fuel

- Page: `embergen/pages/references/node_list.html`
- Segment index: `3984`
- Source: Pre Processed Smoke, Temperature, Fuel, Flames: Channel before any processing.
- Target: Pre Processed Smoke, Temperature, Fuel, Flames（处理前的烟雾、温度、燃料、火焰）：任何处理之前的通道。
- Expected: reduce English-token density in Chinese prose

### LOW - missing_preferred_translation - node

- Page: `embergen/pages/references/ui_reference.html`
- Segment index: `339`
- Source:  tab of certain force nodes.
- Target:  选项卡中。
- Expected: 节点

### LOW - mixed_readability - Failed, to, remove, this, service, from, the

- Page: `licensing/index.html`
- Segment index: `256`
- Source: In case of error message:
* Failed to remove this service from the Windows Firewall. 0x80070057
- Target: 如果出现错误消息：
* Failed to remove this service from the Windows Firewall. 0x80070057
- Expected: reduce English-token density in Chinese prose

### LOW - mixed_readability - Q, W, E

- Page: `liquigen/pages/getting_started.html`
- Segment index: `317`
- Source: Q, W, and E
- Target: Q、W 和 E
- Expected: reduce English-token density in Chinese prose

### LOW - mixed_readability - D, Maya, Blender

- Page: `liquigen/pages/getting_started.html`
- Segment index: `497`
- Source: With this node, you can export your liquid mesh as a 3D file format for use in other software like Maya or Blender.
- Target: 使用该节点，可以将液体网格导出为 3D 文件格式，以便在 Maya 或 Blender 等其他软件中使用。
- Expected: reduce English-token density in Chinese prose

### LOW - missing_preferred_translation - node

- Page: `liquigen/pages/references/ui_reference.html`
- Segment index: `331`
- Source:  tab of certain force nodes.
- Target:  选项卡中。
- Expected: 节点

## Term Variant Counters

- `flipbook`: {'翻页': 38, '序列': 37, '动画': 2, '贴图': 4}
- `mesh flipbook`: {'网格': 1, '翻页': 1}
