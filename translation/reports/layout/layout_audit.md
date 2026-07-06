# JangaFX Layout And Media Consistency Report

This is an automated browser-rendered comparison between `jangafx-docs` and `jangafx-docs-zh`.

## Summary

- Pages in original mirror: 62
- Pages in translated mirror: 62
- Viewports: desktop 1366x768, mobile 390x844
- Page/viewport comparisons: 124
- Significant media original/translated: 1022 / 1022
- All article media original/translated: 3518 / 3518
- Issues by severity: {"medium":28}
- Max significant media horizontal delta: 532.00 px
- Max significant media vertical delta: 30926.55 px
- Max translated horizontal overflow: 170.00 px
- Max scroll-height absolute delta: 30975.00 px

## Interpretation

- `significant media` includes videos and substantive images in the main article body. Tiny inline icons are tracked separately as `all article media` but are not treated as layout-critical content images.
- Horizontal position and size mismatches are treated as possible layout regressions.
- Vertical deltas are reported because translated text can naturally reflow; they are not considered failures when media order, source, width, and horizontal alignment remain stable.

## Top Issues

### MEDIUM - significant_media_box

- Page: `embergen/pages/getting_started.html`
- Viewport: `desktop`
- Message: Significant media #22 layout differs
- Detail: `{"src":"_static/videos/fireColor.mp4","diff":{"dx":410,"dy":960,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":1098,"y":8603.7,"width":150,"height":150,"top":8603.7,"left":1098,"right":1248,"bottom":8753.7},"translatedRect":{"x":688,"y":7643.7,"width":150,"height":150,"top":7643.7,"left":688,"right":838,"bottom":7793.7}}`

### MEDIUM - significant_media_box

- Page: `embergen/pages/getting_started.html`
- Viewport: `desktop`
- Message: Significant media #26 layout differs
- Detail: `{"src":"_static/videos/captureTypesMappingShowcase.mp4","diff":{"dx":155,"dy":1104,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":898,"y":9764.48,"width":350,"height":302.02,"top":9764.48,"left":898,"right":1248,"bottom":10066.5},"translatedRect":{"x":743,"y":8660.48,"width":350,"height":302.02,"top":8660.48,"left":743,"right":1093,"bottom":8962.5}}`

### MEDIUM - significant_media_box

- Page: `embergen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #11 layout differs
- Detail: `{"src":"_static/videos/emissionGradient.mp4","diff":{"dx":305,"dy":720,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":948,"y":7358.2,"width":300,"height":330,"top":7358.2,"left":948,"right":1248,"bottom":7688.2},"translatedRect":{"x":643,"y":6638.2,"width":300,"height":330,"top":6638.2,"left":643,"right":943,"bottom":6968.2}}`

### MEDIUM - significant_media_box

- Page: `embergen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #19 layout differs
- Detail: `{"src":"_static/videos/particleCone.mp4","diff":{"dx":460,"dy":1056.79,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":998,"y":11271.13,"width":250,"height":714.28,"top":11271.13,"left":998,"right":1248,"bottom":11985.41},"translatedRect":{"x":538,"y":10214.34,"width":250,"height":714.28,"top":10214.34,"left":538,"right":788,"bottom":10928.63}}`

### MEDIUM - significant_media_box

- Page: `embergen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #56 layout differs
- Detail: `{"src":"_static/videos/ground.mp4","diff":{"dx":155,"dy":4344.78,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":848,"y":39317.92,"width":400,"height":347.19,"top":39317.92,"left":848,"right":1248,"bottom":39665.11},"translatedRect":{"x":693,"y":34973.14,"width":400,"height":347.19,"top":34973.14,"left":693,"right":1093,"bottom":35320.33}}`

### MEDIUM - significant_media_box

- Page: `embergen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #77 layout differs
- Detail: `{"src":"_static/videos/flamesContribution.mp4","diff":{"dx":205,"dy":6000.78,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":1048,"y":53192.8,"width":200,"height":253.39,"top":53192.8,"left":1048,"right":1248,"bottom":53446.19},"translatedRect":{"x":843,"y":47192.02,"width":200,"height":253.39,"top":47192.02,"left":843,"right":1043,"bottom":47445.41}}`

### MEDIUM - significant_media_box

- Page: `embergen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #93 layout differs
- Detail: `{"src":"_static/videos/particlesRotation.mp4","diff":{"dx":305,"dy":7344.78,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":948,"y":66688.03,"width":300,"height":300,"top":66688.03,"left":948,"right":1248,"bottom":66988.03},"translatedRect":{"x":643,"y":59343.25,"width":300,"height":300,"top":59343.25,"left":643,"right":943,"bottom":59643.25}}`

### MEDIUM - significant_media_box

- Page: `embergen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #94 layout differs
- Detail: `{"src":"_static/videos/particlesAdvectionIntensity.mp4","diff":{"dx":305,"dy":7256.78,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":593,"y":66900.03,"width":350,"height":320.83,"top":66900.03,"left":593,"right":943,"bottom":67220.86},"translatedRect":{"x":898,"y":59643.25,"width":350,"height":320.83,"top":59643.25,"left":898,"right":1248,"bottom":59964.08}}`

### MEDIUM - significant_media_box

- Page: `embergen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #95 layout differs
- Detail: `{"src":"_static/videos/particlesTightnessIntensity.mp4","diff":{"dx":355,"dy":7440.78,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":898,"y":67288.03,"width":350,"height":233,"top":67288.03,"left":898,"right":1248,"bottom":67521.03},"translatedRect":{"x":543,"y":59847.25,"width":350,"height":233,"top":59847.25,"left":543,"right":893,"bottom":60080.25}}`

### MEDIUM - significant_media_box

- Page: `embergen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #96 layout differs
- Detail: `{"src":"_static/videos/particlesChaosRange.mp4","diff":{"dx":355,"dy":7344.78,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":393,"y":67508.03,"width":500,"height":166,"top":67508.03,"left":393,"right":893,"bottom":67674.03},"translatedRect":{"x":748,"y":60163.25,"width":500,"height":166,"top":60163.25,"left":748,"right":1248,"bottom":60329.25}}`

### MEDIUM - significant_media_box

- Page: `embergen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #113 layout differs
- Detail: `{"src":"_static/videos/forceDiffusionComparison.mp4","diff":{"dx":255,"dy":8736.78,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":318,"y":77070.3,"width":900,"height":180,"top":77070.3,"left":318,"right":1218,"bottom":77250.3},"translatedRect":{"x":63,"y":68333.52,"width":900,"height":180,"top":68333.52,"left":63,"right":963,"bottom":68513.52}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/getting_started.html`
- Viewport: `desktop`
- Message: Significant media #3 layout differs
- Detail: `{"src":"_static/videos/hose_vs_hose_LG.mp4","diff":{"dx":532,"dy":72,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":848,"y":1246,"width":400,"height":225,"top":1246,"left":848,"right":1248,"bottom":1471},"translatedRect":{"x":316,"y":1174,"width":400,"height":225,"top":1174,"left":316,"right":716,"bottom":1399}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/getting_started.html`
- Viewport: `desktop`
- Message: Significant media #18 layout differs
- Detail: `{"src":"_static/videos/drain.mp4","diff":{"dx":405,"dy":799,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":848,"y":7690.83,"width":400,"height":200,"top":7690.83,"left":848,"right":1248,"bottom":7890.83},"translatedRect":{"x":443,"y":6891.83,"width":400,"height":200,"top":6891.83,"left":443,"right":843,"bottom":7091.83}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/getting_started.html`
- Viewport: `desktop`
- Message: Significant media #28 layout differs
- Detail: `{"src":"_static/videos/diver.mp4","diff":{"dx":165.98,"dy":967,"dw":0.03,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":368,"y":11376.14,"width":800,"height":416.66,"top":11376.14,"left":368,"right":1168,"bottom":11792.8},"translatedRect":{"x":202.02,"y":10409.14,"width":799.97,"height":416.66,"top":10409.14,"left":202.02,"right":1001.98,"bottom":10825.8}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/How-To Guides/animation.html`
- Viewport: `desktop`
- Message: Significant media #16 layout differs
- Detail: `{"src":"_static/videos/editingBezierHandle.mp4","diff":{"dx":305,"dy":416,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":948,"y":4507.31,"width":300,"height":142.88,"top":4507.31,"left":948,"right":1248,"bottom":4650.19},"translatedRect":{"x":643,"y":4091.31,"width":300,"height":142.88,"top":4091.31,"left":643,"right":943,"bottom":4234.19}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/How-To Guides/comment.html`
- Viewport: `desktop`
- Message: Significant media #2 layout differs
- Detail: `{"src":"_static/videos/scaleComment_LG.mp4","diff":{"dx":405,"dy":72,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":848,"y":490,"width":400,"height":382.05,"top":490,"left":848,"right":1248,"bottom":872.05},"translatedRect":{"x":443,"y":418,"width":400,"height":382.05,"top":418,"left":443,"right":843,"bottom":800.05}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/How-To Guides/diagnostics.html`
- Viewport: `desktop`
- Message: Significant media #10 layout differs
- Detail: `{"src":"_static/videos/diagnostics_velocity_view.mp4","diff":{"dx":355,"dy":624,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":898,"y":7203.13,"width":350,"height":624.33,"top":7203.13,"left":898,"right":1248,"bottom":7827.45},"translatedRect":{"x":543,"y":6579.13,"width":350,"height":624.33,"top":6579.13,"left":543,"right":893,"bottom":7203.45}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/How-To Guides/diagnostics.html`
- Viewport: `desktop`
- Message: Significant media #12 layout differs
- Detail: `{"src":"_static/videos/diagnostics_velocity_transform.mp4","diff":{"dx":305,"dy":528,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":898,"y":8663.13,"width":350,"height":239.64,"top":8663.13,"left":898,"right":1248,"bottom":8902.77},"translatedRect":{"x":593,"y":8135.13,"width":350,"height":239.64,"top":8135.13,"left":593,"right":943,"bottom":8374.77}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/How-To Guides/modulation_curve.html`
- Viewport: `desktop`
- Message: Significant media #8 layout differs
- Detail: `{"src":"_static/videos/modulationCurveEndGraphic_LG.mp4","diff":{"dx":227.48,"dy":792,"dw":0.03,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":368,"y":5485.14,"width":800,"height":539.39,"top":5485.14,"left":368,"right":1168,"bottom":6024.53},"translatedRect":{"x":140.52,"y":4693.14,"width":799.97,"height":539.39,"top":4693.14,"left":140.52,"right":940.48,"bottom":5232.53}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #6 layout differs
- Detail: `{"src":"_static/videos/lifetime_LG.mp4","diff":{"dx":305,"dy":384,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":1038,"y":3362.34,"width":210,"height":420,"top":3362.34,"left":1038,"right":1248,"bottom":3782.34},"translatedRect":{"x":733,"y":2978.34,"width":210,"height":420,"top":2978.34,"left":733,"right":943,"bottom":3398.34}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #7 layout differs
- Detail: `{"src":"_static/videos/DynamicViscosityCoefficient_LG.mp4","diff":{"dx":152.48,"dy":312,"dw":0.03,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":310.5,"y":3649.47,"width":700,"height":170.44,"top":3649.47,"left":310.5,"right":1010.5,"bottom":3819.91},"translatedRect":{"x":158.02,"y":3337.47,"width":699.97,"height":170.44,"top":3337.47,"left":158.02,"right":857.98,"bottom":3507.91}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #19 layout differs
- Detail: `{"src":"_static/videos/line_force_push_LG.mp4","diff":{"dx":405,"dy":1032,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":848,"y":9245.52,"width":400,"height":415.19,"top":9245.52,"left":848,"right":1248,"bottom":9660.7},"translatedRect":{"x":443,"y":8213.52,"width":400,"height":415.19,"top":8213.52,"left":443,"right":843,"bottom":8628.7}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #27 layout differs
- Detail: `{"src":"_static/videos/whitewater_source_LG.mp4","diff":{"dx":405,"dy":1488,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":848,"y":13750.92,"width":400,"height":396.38,"top":13750.92,"left":848,"right":1248,"bottom":14147.3},"translatedRect":{"x":443,"y":12262.92,"width":400,"height":396.38,"top":12262.92,"left":443,"right":843,"bottom":12659.3}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #29 layout differs
- Detail: `{"src":"_static/videos/whitewater_spray_bouyancy_LG.mp4","diff":{"dx":405,"dy":1488,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":848,"y":14560.33,"width":400,"height":400,"top":14560.33,"left":848,"right":1248,"bottom":14960.33},"translatedRect":{"x":443,"y":13072.33,"width":400,"height":400,"top":13072.33,"left":443,"right":843,"bottom":13472.33}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #33 layout differs
- Detail: `{"src":"_static/videos/field_of_view_perspective_LG.mp4","diff":{"dx":305,"dy":1560,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":948,"y":16826.17,"width":300,"height":648,"top":16826.17,"left":948,"right":1248,"bottom":17474.17},"translatedRect":{"x":643,"y":15266.17,"width":300,"height":648,"top":15266.17,"left":643,"right":943,"bottom":15914.17}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #49 layout differs
- Detail: `{"src":"_static/videos/export_mesh_LG.mp4","diff":{"dx":355,"dy":2592,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":898,"y":26734.05,"width":350,"height":350,"top":26734.05,"left":898,"right":1248,"bottom":27084.05},"translatedRect":{"x":543,"y":24142.05,"width":350,"height":350,"top":24142.05,"left":543,"right":893,"bottom":24492.05}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #75 layout differs
- Detail: `{"src":"_static/videos/render_bounces_LG.mp4","diff":{"dx":155,"dy":4200,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":898,"y":42859.97,"width":350,"height":380.75,"top":42859.97,"left":898,"right":1248,"bottom":43240.72},"translatedRect":{"x":743,"y":38659.97,"width":350,"height":380.75,"top":38659.97,"left":743,"right":1093,"bottom":39040.72}}`

### MEDIUM - significant_media_box

- Page: `liquigen/pages/references/node_list.html`
- Viewport: `desktop`
- Message: Significant media #76 layout differs
- Detail: `{"src":"_static/videos/render_denoise_LG.mp4","diff":{"dx":155,"dy":4200,"dw":0,"dh":0,"widthPct":0,"heightPct":0,"horizontalMismatch":true,"sizeMismatch":false},"originalRect":{"x":543,"y":43225.97,"width":350,"height":446.08,"top":43225.97,"left":543,"right":893,"bottom":43672.05},"translatedRect":{"x":388,"y":39025.97,"width":350,"height":446.08,"top":39025.97,"left":388,"right":738,"bottom":39472.05}}`

## Screenshot Artifacts

- `output/playwright/layout-audit/desktop__original__index.png`
- `output/playwright/layout-audit/desktop__zh__index.png`
- `output/playwright/layout-audit/desktop__original__licensing__index.png`
- `output/playwright/layout-audit/desktop__zh__licensing__index.png`
- `output/playwright/layout-audit/desktop__original__embergen__pages__references__node_list.png`
- `output/playwright/layout-audit/desktop__zh__embergen__pages__references__node_list.png`
- `output/playwright/layout-audit/desktop__original__liquigen__pages__references__node_list.png`
- `output/playwright/layout-audit/desktop__zh__liquigen__pages__references__node_list.png`
- `output/playwright/layout-audit/desktop__original__embergen__pages__references__ui_reference.png`
- `output/playwright/layout-audit/desktop__zh__embergen__pages__references__ui_reference.png`
- `output/playwright/layout-audit/desktop__original__liquigen__pages__references__How-To Guides__diagnostics.png`
- `output/playwright/layout-audit/desktop__zh__liquigen__pages__references__How-To Guides__diagnostics.png`
- `output/playwright/layout-audit/mobile__original__index.png`
- `output/playwright/layout-audit/mobile__zh__index.png`
- `output/playwright/layout-audit/mobile__original__licensing__index.png`
- `output/playwright/layout-audit/mobile__zh__licensing__index.png`
- `output/playwright/layout-audit/mobile__original__embergen__pages__references__node_list.png`
- `output/playwright/layout-audit/mobile__zh__embergen__pages__references__node_list.png`
- `output/playwright/layout-audit/mobile__original__liquigen__pages__references__node_list.png`
- `output/playwright/layout-audit/mobile__zh__liquigen__pages__references__node_list.png`
- `output/playwright/layout-audit/mobile__original__embergen__pages__references__ui_reference.png`
- `output/playwright/layout-audit/mobile__zh__embergen__pages__references__ui_reference.png`
- `output/playwright/layout-audit/mobile__original__liquigen__pages__references__How-To Guides__diagnostics.png`
- `output/playwright/layout-audit/mobile__zh__liquigen__pages__references__How-To Guides__diagnostics.png`
