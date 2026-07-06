#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const http = require("http");
const { pathToFileURL } = require("url");
const { chromium } = require("playwright-core");

const ROOT = process.cwd();
const SRC_DIR = path.join(ROOT, "jangafx-docs");
const ZH_DIR = path.join(ROOT, "jangafx-docs-zh");
const REPORT_DIR = path.join(ROOT, "translation", "reports", "layout");
const SCREENSHOT_DIR = path.join(ROOT, "output", "playwright", "layout-audit");
const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

const VIEWPORTS = [
  { name: "desktop", width: 1366, height: 768 },
  { name: "mobile", width: 390, height: 844 },
];

const SCREENSHOT_PAGES = [
  "index.html",
  "licensing/index.html",
  "embergen/pages/references/node_list.html",
  "liquigen/pages/references/node_list.html",
  "embergen/pages/references/ui_reference.html",
  "liquigen/pages/references/How-To Guides/diagnostics.html",
];

const MIME = new Map([
  [".html", "text/html; charset=utf-8"],
  [".css", "text/css; charset=utf-8"],
  [".js", "application/javascript; charset=utf-8"],
  [".json", "application/json; charset=utf-8"],
  [".png", "image/png"],
  [".jpg", "image/jpeg"],
  [".jpeg", "image/jpeg"],
  [".gif", "image/gif"],
  [".svg", "image/svg+xml"],
  [".ico", "image/x-icon"],
  [".mp4", "video/mp4"],
  [".webm", "video/webm"],
  [".woff", "font/woff"],
  [".woff2", "font/woff2"],
]);

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function walkHtml(dir, prefix = "") {
  const out = [];
  for (const entry of fs.readdirSync(path.join(dir, prefix), { withFileTypes: true })) {
    const rel = path.join(prefix, entry.name);
    if (entry.isDirectory()) out.push(...walkHtml(dir, rel));
    else if (entry.isFile() && entry.name.endsWith(".html")) out.push(rel.split(path.sep).join("/"));
  }
  return out.sort();
}

function startServer(rootDir) {
  return new Promise((resolve, reject) => {
    const server = http.createServer((req, res) => {
      try {
        const url = new URL(req.url, "http://127.0.0.1");
        let pathname = decodeURIComponent(url.pathname);
        if (pathname.endsWith("/")) pathname += "index.html";
        const rawPath = path.normalize(path.join(rootDir, pathname));
        if (!rawPath.startsWith(rootDir)) {
          res.writeHead(403);
          res.end("Forbidden");
          return;
        }
        fs.stat(rawPath, (statErr, stat) => {
          if (statErr || !stat.isFile()) {
            res.writeHead(404);
            res.end("Not found");
            return;
          }
          const ext = path.extname(rawPath).toLowerCase();
          res.writeHead(200, {
            "content-type": MIME.get(ext) || "application/octet-stream",
            "cache-control": "no-store",
          });
          fs.createReadStream(rawPath).pipe(res);
        });
      } catch (error) {
        res.writeHead(500);
        res.end(String(error && error.stack ? error.stack : error));
      }
    });
    server.on("error", reject);
    server.listen(0, "127.0.0.1", () => {
      const address = server.address();
      resolve({
        server,
        baseUrl: `http://127.0.0.1:${address.port}`,
      });
    });
  });
}

function roundRect(rect) {
  if (!rect) return null;
  const out = {};
  for (const key of ["x", "y", "width", "height", "top", "left", "right", "bottom"]) {
    out[key] = Number(rect[key].toFixed(2));
  }
  return out;
}

function pctDelta(a, b) {
  if (!a && !b) return 0;
  const base = Math.max(Math.abs(a || 0), Math.abs(b || 0), 1);
  return Math.abs((a || 0) - (b || 0)) / base;
}

function normalizeSrc(src) {
  if (!src) return "";
  try {
    const url = new URL(src);
    return decodeURIComponent(url.pathname).replace(/^\/+/, "");
  } catch (_) {
    return src.replace(/^\/+/, "");
  }
}

function compareBoxes(a, b, options = {}) {
  if (!a || !b) return null;
  const xThreshold = options.xThreshold || 16;
  const sizeThreshold = options.sizeThreshold || 6;
  const widthPctThreshold = options.widthPctThreshold || 0.03;
  const heightPctThreshold = options.heightPctThreshold || 0.05;
  const dx = Math.abs(a.x - b.x);
  const dy = Math.abs(a.y - b.y);
  const dw = Math.abs(a.width - b.width);
  const dh = Math.abs(a.height - b.height);
  return {
    dx: Number(dx.toFixed(2)),
    dy: Number(dy.toFixed(2)),
    dw: Number(dw.toFixed(2)),
    dh: Number(dh.toFixed(2)),
    widthPct: Number(pctDelta(a.width, b.width).toFixed(4)),
    heightPct: Number(pctDelta(a.height, b.height).toFixed(4)),
    horizontalMismatch: dx > xThreshold,
    sizeMismatch:
      (dw > sizeThreshold && pctDelta(a.width, b.width) > widthPctThreshold) ||
      (dh > sizeThreshold && pctDelta(a.height, b.height) > heightPctThreshold),
  };
}

function severityRank(severity) {
  return { high: 3, medium: 2, low: 1, info: 0 }[severity] || 0;
}

async function pageLayout(page) {
  return page.evaluate(() => {
    const box = (el) => {
      if (!el) return null;
      const r = el.getBoundingClientRect();
      const cs = window.getComputedStyle(el);
      return {
        x: r.x,
        y: r.y,
        width: r.width,
        height: r.height,
        top: r.top,
        left: r.left,
        right: r.right,
        bottom: r.bottom,
        display: cs.display,
        visibility: cs.visibility,
      };
    };
    const one = (selector) => box(document.querySelector(selector));
    const srcOf = (el) => {
      if (el.tagName.toLowerCase() === "video") {
        const source = el.querySelector("source[src]");
        const lazySource = el.querySelector("source[data-src]");
        const raw = source ? source.src : (lazySource ? lazySource.getAttribute("data-src") : el.currentSrc || el.src || "");
        return raw ? new URL(raw, document.baseURI).href : "";
      }
      return el.currentSrc || el.src || "";
    };
    const nearestContainerSignature = (el) => {
      const parts = [];
      let node = el;
      for (let i = 0; i < 5 && node && node !== document.body; i += 1) {
        const tag = node.tagName ? node.tagName.toLowerCase() : "";
        if (!tag) break;
        const id = node.id ? `#${node.id}` : "";
        const cls = node.className && typeof node.className === "string"
          ? "." + node.className.trim().split(/\s+/).slice(0, 3).join(".")
          : "";
        parts.push(`${tag}${id}${cls}`);
        node = node.parentElement;
      }
      return parts.reverse().join(">");
    };
    const media = Array.from(document.querySelectorAll('article[role="main"] img, article[role="main"] video')).map((el, index) => {
      const r = el.getBoundingClientRect();
      const tag = el.tagName.toLowerCase();
      const src = srcOf(el);
      const widthAttr = el.getAttribute("width") || "";
      const heightAttr = el.getAttribute("height") || "";
      const cls = el.getAttribute("class") || "";
      const alt = el.getAttribute("alt") || "";
      const significant =
        tag === "video" ||
        cls.includes("align-") ||
        (el.closest("a.image-reference") !== null) ||
        r.width >= 80 ||
        r.height >= 80;
      return {
        index,
        tag,
        src,
        alt,
        className: cls,
        widthAttr,
        heightAttr,
        rect: {
          x: r.x,
          y: r.y,
          width: r.width,
          height: r.height,
          top: r.top,
          left: r.left,
          right: r.right,
          bottom: r.bottom,
        },
        significant,
        container: nearestContainerSignature(el),
      };
    });
    const html = document.documentElement;
    const body = document.body;
    const scrolling = document.scrollingElement || html;
    return {
      title: document.title,
      metrics: {
        innerWidth: window.innerWidth,
        innerHeight: window.innerHeight,
        scrollWidth: scrolling.scrollWidth,
        scrollHeight: scrolling.scrollHeight,
        clientWidth: scrolling.clientWidth,
        clientHeight: scrolling.clientHeight,
        bodyScrollWidth: body ? body.scrollWidth : 0,
        bodyScrollHeight: body ? body.scrollHeight : 0,
      },
      boxes: {
        content: one("div.content"),
        articleContainer: one("div.article-container"),
        article: one('article[role="main"]'),
        sidebar: one(".sidebar-drawer, .sidebar-container"),
        toc: one(".toc-drawer"),
        contentIcons: one(".content-icon-container"),
        footer: one(".bottom-of-page, footer"),
      },
      mediaAll: media,
      mediaSignificant: media.filter((item) => item.significant),
    };
  });
}

async function loadLayout(page, baseUrl, relPath) {
  const url = `${baseUrl}/${relPath.split("/").map(encodeURIComponent).join("/")}`;
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
  await page.waitForLoadState("load", { timeout: 45000 }).catch(() => {});
  await page.evaluate(() => document.fonts && document.fonts.ready ? document.fonts.ready : null).catch(() => {});
  await page.waitForTimeout(120);
  const layout = await pageLayout(page);
  layout.url = url;
  return layout;
}

function addIssue(issues, severity, page, viewport, type, message, detail = {}) {
  issues.push({ severity, page, viewport, type, message, detail });
}

function comparePage(relPath, viewport, original, translated, issues, stats) {
  const srcSig = original.mediaSignificant.map((m) => normalizeSrc(m.src));
  const zhSig = translated.mediaSignificant.map((m) => normalizeSrc(m.src));
  const srcAll = original.mediaAll.map((m) => normalizeSrc(m.src));
  const zhAll = translated.mediaAll.map((m) => normalizeSrc(m.src));

  stats.pagesCompared += 1;
  stats.significantMediaOriginal += srcSig.length;
  stats.significantMediaTranslated += zhSig.length;
  stats.allMediaOriginal += srcAll.length;
  stats.allMediaTranslated += zhAll.length;

  if (srcSig.length !== zhSig.length) {
    addIssue(issues, "high", relPath, viewport.name, "significant_media_count", `Significant media count differs: original ${srcSig.length}, translated ${zhSig.length}`, {
      original: srcSig,
      translated: zhSig,
    });
  }
  if (srcAll.length !== zhAll.length) {
    addIssue(issues, "medium", relPath, viewport.name, "all_media_count", `All article media count differs: original ${srcAll.length}, translated ${zhAll.length}`);
  }

  const count = Math.min(srcSig.length, zhSig.length);
  for (let i = 0; i < count; i += 1) {
    const a = original.mediaSignificant[i];
    const b = translated.mediaSignificant[i];
    const aSrc = normalizeSrc(a.src);
    const bSrc = normalizeSrc(b.src);
    if (a.tag !== b.tag || aSrc !== bSrc) {
      addIssue(issues, "high", relPath, viewport.name, "significant_media_order", `Significant media #${i + 1} differs`, {
        original: { tag: a.tag, src: aSrc },
        translated: { tag: b.tag, src: bSrc },
      });
      continue;
    }
    const diff = compareBoxes(roundRect(a.rect), roundRect(b.rect), {
      xThreshold: viewport.name === "mobile" ? 10 : 16,
      sizeThreshold: 6,
      widthPctThreshold: 0.03,
      heightPctThreshold: 0.05,
    });
    stats.maxSignificantMediaVerticalDelta = Math.max(stats.maxSignificantMediaVerticalDelta, diff.dy);
    stats.maxSignificantMediaHorizontalDelta = Math.max(stats.maxSignificantMediaHorizontalDelta, diff.dx);
    if (diff.horizontalMismatch || diff.sizeMismatch) {
      addIssue(issues, diff.sizeMismatch ? "high" : "medium", relPath, viewport.name, "significant_media_box", `Significant media #${i + 1} layout differs`, {
        src: aSrc,
        diff,
        originalRect: roundRect(a.rect),
        translatedRect: roundRect(b.rect),
      });
    }
  }

  for (const key of ["content", "articleContainer", "article", "sidebar", "toc", "contentIcons"]) {
    const a = roundRect(original.boxes[key]);
    const b = roundRect(translated.boxes[key]);
    if (!a && !b) continue;
    if (!a || !b) {
      addIssue(issues, "medium", relPath, viewport.name, "container_presence", `Container ${key} presence differs`, { original: a, translated: b });
      continue;
    }
    const diff = compareBoxes(a, b, {
      xThreshold: viewport.name === "mobile" ? 10 : 16,
      sizeThreshold: 8,
      widthPctThreshold: 0.03,
      heightPctThreshold: 1,
    });
    if (diff.horizontalMismatch || diff.sizeMismatch) {
      addIssue(issues, "medium", relPath, viewport.name, "container_box", `Container ${key} horizontal/width layout differs`, {
        key,
        diff,
        originalRect: a,
        translatedRect: b,
      });
    }
  }

  const srcOverflow = original.metrics.scrollWidth - original.metrics.clientWidth;
  const zhOverflow = translated.metrics.scrollWidth - translated.metrics.clientWidth;
  stats.maxTranslatedHorizontalOverflow = Math.max(stats.maxTranslatedHorizontalOverflow, zhOverflow);
  if (zhOverflow > Math.max(srcOverflow + 8, 8)) {
    addIssue(issues, "high", relPath, viewport.name, "horizontal_overflow", `Translated page has extra horizontal overflow: original ${srcOverflow}px, translated ${zhOverflow}px`, {
      originalMetrics: original.metrics,
      translatedMetrics: translated.metrics,
    });
  }

  const heightDelta = translated.metrics.scrollHeight - original.metrics.scrollHeight;
  stats.maxScrollHeightAbsDelta = Math.max(stats.maxScrollHeightAbsDelta, Math.abs(heightDelta));
}

function assetExists(rootDir, normalizedSrc) {
  if (!normalizedSrc || /^https?:/i.test(normalizedSrc) || normalizedSrc.startsWith("data:")) return true;
  const pathname = normalizedSrc.split("#")[0].split("?")[0];
  return fs.existsSync(path.join(rootDir, pathname));
}

async function screenshotPair(browser, servers, relPath, viewport) {
  const context = await browser.newContext({ viewport, deviceScaleFactor: 1 });
  const page = await context.newPage();
  for (const side of ["original", "zh"]) {
    const baseUrl = side === "original" ? servers.original.baseUrl : servers.zh.baseUrl;
    const url = `${baseUrl}/${relPath.split("/").map(encodeURIComponent).join("/")}`;
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
    await page.waitForLoadState("load", { timeout: 45000 }).catch(() => {});
    await page.evaluate(() => document.fonts && document.fonts.ready ? document.fonts.ready : null).catch(() => {});
    await page.waitForTimeout(120);
    const safeName = relPath.replace(/[\/\\]/g, "__").replace(/\.html$/, "");
    await page.screenshot({
      path: path.join(SCREENSHOT_DIR, `${viewport.name}__${side}__${safeName}.png`),
      fullPage: false,
    });
  }
  await context.close();
}

function writeReports(result) {
  ensureDir(REPORT_DIR);
  fs.writeFileSync(path.join(REPORT_DIR, "layout_audit.json"), JSON.stringify(result, null, 2));

  const issuesBySeverity = result.issues.reduce((acc, issue) => {
    acc[issue.severity] = (acc[issue.severity] || 0) + 1;
    return acc;
  }, {});
  const topIssues = result.issues
    .slice()
    .sort((a, b) => severityRank(b.severity) - severityRank(a.severity))
    .slice(0, 40);

  const lines = [];
  lines.push("# JangaFX Layout And Media Consistency Report");
  lines.push("");
  lines.push("This is an automated browser-rendered comparison between `jangafx-docs` and `jangafx-docs-zh`.");
  lines.push("");
  lines.push("## Summary");
  lines.push("");
  lines.push(`- Pages in original mirror: ${result.summary.pagesOriginal}`);
  lines.push(`- Pages in translated mirror: ${result.summary.pagesTranslated}`);
  lines.push(`- Viewports: ${result.summary.viewports.join(", ")}`);
  lines.push(`- Page/viewport comparisons: ${result.stats.pagesCompared}`);
  lines.push(`- Significant media original/translated: ${result.stats.significantMediaOriginal} / ${result.stats.significantMediaTranslated}`);
  lines.push(`- All article media original/translated: ${result.stats.allMediaOriginal} / ${result.stats.allMediaTranslated}`);
  lines.push(`- Issues by severity: ${JSON.stringify(issuesBySeverity)}`);
  lines.push(`- Max significant media horizontal delta: ${result.stats.maxSignificantMediaHorizontalDelta.toFixed(2)} px`);
  lines.push(`- Max significant media vertical delta: ${result.stats.maxSignificantMediaVerticalDelta.toFixed(2)} px`);
  lines.push(`- Max translated horizontal overflow: ${result.stats.maxTranslatedHorizontalOverflow.toFixed(2)} px`);
  lines.push(`- Max scroll-height absolute delta: ${result.stats.maxScrollHeightAbsDelta.toFixed(2)} px`);
  lines.push("");
  lines.push("## Interpretation");
  lines.push("");
  lines.push("- `significant media` includes videos and substantive images in the main article body. Tiny inline icons are tracked separately as `all article media` but are not treated as layout-critical content images.");
  lines.push("- Horizontal position and size mismatches are treated as possible layout regressions.");
  lines.push("- Vertical deltas are reported because translated text can naturally reflow; they are not considered failures when media order, source, width, and horizontal alignment remain stable.");
  lines.push("");
  lines.push("## Top Issues");
  lines.push("");
  if (!topIssues.length) {
    lines.push("No layout or media consistency issues were detected by the automated browser comparison.");
  } else {
    for (const issue of topIssues) {
      lines.push(`### ${issue.severity.toUpperCase()} - ${issue.type}`);
      lines.push("");
      lines.push(`- Page: \`${issue.page}\``);
      lines.push(`- Viewport: \`${issue.viewport}\``);
      lines.push(`- Message: ${issue.message}`);
      if (issue.detail && Object.keys(issue.detail).length) {
        lines.push(`- Detail: \`${JSON.stringify(issue.detail).slice(0, 500)}\``);
      }
      lines.push("");
    }
  }
  lines.push("## Screenshot Artifacts");
  lines.push("");
  for (const shot of result.screenshots) {
    lines.push(`- \`${shot}\``);
  }
  lines.push("");
  fs.writeFileSync(path.join(REPORT_DIR, "layout_audit.md"), lines.join("\n"));
}

async function main() {
  ensureDir(REPORT_DIR);
  ensureDir(SCREENSHOT_DIR);

  const srcPages = walkHtml(SRC_DIR);
  const zhPages = walkHtml(ZH_DIR);
  const zhSet = new Set(zhPages);
  const pages = srcPages.filter((rel) => zhSet.has(rel));
  const missingInZh = srcPages.filter((rel) => !zhSet.has(rel));
  const extraInZh = zhPages.filter((rel) => !srcPages.includes(rel));

  const original = await startServer(SRC_DIR);
  const zh = await startServer(ZH_DIR);
  const servers = { original, zh };
  const browser = await chromium.launch({
    executablePath: fs.existsSync(CHROME) ? CHROME : undefined,
    headless: true,
    args: ["--disable-gpu", "--no-sandbox", "--autoplay-policy=no-user-gesture-required"],
  });

  const issues = [];
  const stats = {
    pagesCompared: 0,
    significantMediaOriginal: 0,
    significantMediaTranslated: 0,
    allMediaOriginal: 0,
    allMediaTranslated: 0,
    maxSignificantMediaVerticalDelta: 0,
    maxSignificantMediaHorizontalDelta: 0,
    maxTranslatedHorizontalOverflow: 0,
    maxScrollHeightAbsDelta: 0,
  };

  for (const relPath of missingInZh) {
    addIssue(issues, "high", relPath, "all", "page_missing", "Page exists in original mirror but not translated mirror");
  }
  for (const relPath of extraInZh) {
    addIssue(issues, "low", relPath, "all", "page_extra", "Page exists in translated mirror but not original mirror");
  }

  const assetSeen = new Set();
  for (const viewport of VIEWPORTS) {
    const context = await browser.newContext({ viewport, deviceScaleFactor: 1 });
    const originalPage = await context.newPage();
    const translatedPage = await context.newPage();
    for (const relPath of pages) {
      const originalLayout = await loadLayout(originalPage, original.baseUrl, relPath);
      const translatedLayout = await loadLayout(translatedPage, zh.baseUrl, relPath);
      comparePage(relPath, viewport, originalLayout, translatedLayout, issues, stats);

      for (const item of [...originalLayout.mediaAll, ...translatedLayout.mediaAll]) {
        const normalized = normalizeSrc(item.src);
        if (!normalized || assetSeen.has(normalized)) continue;
        assetSeen.add(normalized);
        if (!assetExists(SRC_DIR, normalized)) {
          addIssue(issues, "high", relPath, viewport.name, "asset_missing_original", `Referenced asset missing in original mirror: ${normalized}`);
        }
        if (!assetExists(ZH_DIR, normalized)) {
          addIssue(issues, "high", relPath, viewport.name, "asset_missing_translated", `Referenced asset missing in translated mirror: ${normalized}`);
        }
      }
    }
    await context.close();
  }

  const screenshots = [];
  for (const viewport of VIEWPORTS) {
    for (const relPath of SCREENSHOT_PAGES) {
      if (!pages.includes(relPath)) continue;
      await screenshotPair(browser, servers, relPath, viewport);
      const safeName = relPath.replace(/[\/\\]/g, "__").replace(/\.html$/, "");
      screenshots.push(path.join("output", "playwright", "layout-audit", `${viewport.name}__original__${safeName}.png`));
      screenshots.push(path.join("output", "playwright", "layout-audit", `${viewport.name}__zh__${safeName}.png`));
    }
  }

  await browser.close();
  await new Promise((resolve) => original.server.close(resolve));
  await new Promise((resolve) => zh.server.close(resolve));

  const result = {
    generatedAt: new Date().toISOString(),
    summary: {
      pagesOriginal: srcPages.length,
      pagesTranslated: zhPages.length,
      pagesCompared: pages.length,
      missingInZh,
      extraInZh,
      viewports: VIEWPORTS.map((v) => `${v.name} ${v.width}x${v.height}`),
    },
    stats,
    issues,
    screenshots,
  };
  writeReports(result);

  const bySeverity = issues.reduce((acc, issue) => {
    acc[issue.severity] = (acc[issue.severity] || 0) + 1;
    return acc;
  }, {});
  console.log(`Compared ${pages.length} pages across ${VIEWPORTS.length} viewports.`);
  console.log(`Issues by severity: ${JSON.stringify(bySeverity)}`);
  console.log(`Wrote ${path.relative(ROOT, path.join(REPORT_DIR, "layout_audit.json"))}`);
  console.log(`Wrote ${path.relative(ROOT, path.join(REPORT_DIR, "layout_audit.md"))}`);
}

main().catch((error) => {
  console.error(error && error.stack ? error.stack : error);
  process.exitCode = 1;
});
