#!/usr/bin/env python3
"""Terminology and English-retention audit for the JangaFX Chinese docs."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRANSLATION_DIR = ROOT / "translation"
PAGES_DIR = TRANSLATION_DIR / "pages"
SEGMENTS_DIR = TRANSLATION_DIR / "segments"
REPORTS_DIR = TRANSLATION_DIR / "reports"

CJK_RE = re.compile(r"[\u4e00-\u9fff]")
LATIN_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_+./#:-]*")

PROTECTED_TOKENS = {
    "JangaFX",
    "EmberGen",
    "LiquiGen",
    "IlluGen",
    "GeoGen",
    "VectorayGen",
    "Elemental",
    "Suite",
    "OpenVDB",
    "VDB",
    "NanoVDB",
    "NeuralVDB",
    "FBX",
    "OBJ",
    "ABC",
    "Alembic",
    "OGAWA",
    "EXR",
    "PNG",
    "TGA",
    "HDR",
    "VAT",
    "SDF",
    "SMAA",
    "ADSR",
    "MIDI",
    "FPS",
    "RGB",
    "RGBA",
    "GPU",
    "CPU",
    "UI",
    "UX",
    "VFX",
    "FAQ",
    "Windows",
    "Linux",
    "macOS",
    "Unity",
    "Unreal",
    "Houdini",
    "Sphinx",
    "Furo",
}

COMMON_UI_LABELS = {
    "Render",
    "Preview",
    "Export",
    "Import",
    "Settings",
    "Preferences",
    "Project",
    "Timeline",
    "Override",
    "Recording",
    "Curve",
    "Editor",
    "Fit",
    "View",
    "Snap",
    "Frames",
    "Reset",
    "Handle",
    "Constant",
    "Linear",
    "Smooth",
    "Bezier",
    "Bézier",
    "Aligned",
    "Free",
    "Auto",
    "Clamped",
    "Vectored",
    "Command",
    "Parameter",
    "Palette",
    "Min",
    "Max",
    "Open_Paren",
    "Close_Paren",
}

PROTECTED_TOKENS.update(COMMON_UI_LABELS)


@dataclass(frozen=True)
class TermRule:
    name: str
    source_pattern: str
    expected: tuple[str, ...]
    severity: str = "medium"
    allow_english_target: tuple[str, ...] = ()
    min_source_words: int = 3


TERM_RULES = [
    TermRule("flipbook", r"\bflipbooks?\b", ("翻页", "序列", "动画", "贴图"), "high", ("Flipbook",), 4),
    TermRule("sprite sheet", r"\bsprite sheets?\b", ("精灵图集",), "high", (), 2),
    TermRule("texture atlas", r"\btexture atlas(?:es)?\b", ("纹理图集",), "medium", (), 2),
    TermRule("mesh flipbook", r"\bmesh flipbooks?\b", ("网格", "翻页"), "high", ("Mesh Flipbook",), 2),
    TermRule("vertex animated texture", r"\bvertex animated textures?\b", ("顶点动画纹理", "VAT"), "medium", ("VAT",), 2),
    TermRule("image sequence", r"\bimage sequences?\b", ("图像序列",), "medium", (), 2),
    TermRule("channel packing", r"\bchannel packing\b|\bchannel packed\b", ("通道打包",), "medium", (), 2),
    TermRule("node graph", r"\bnode graph\b", ("节点图",), "medium", (), 2),
    TermRule("node", r"\bnodes?\b", ("节点",), "low", (), 5),
    TermRule("parameter", r"\bparameters?\b", ("参数",), "medium", (), 4),
    TermRule("viewport", r"\bviewport\b", ("视口",), "medium", (), 3),
    TermRule("timeline", r"\btimeline\b", ("时间轴",), "medium", ("Timeline",), 4),
    TermRule("keyframe", r"\bkeyframes?\b", ("关键帧",), "medium", (), 3),
    TermRule("render pass", r"\brender passes?\b", ("渲染通道",), "medium", (), 2),
    TermRule("rasterizer", r"\brasterizer\b", ("光栅化器",), "medium", ("Rasterizer",), 2),
    TermRule("path tracer", r"\bpath tracer\b", ("路径追踪器",), "medium", ("Path Tracer",), 2),
    TermRule("denoiser", r"\bdenoiser\b", ("降噪器",), "medium", ("Denoiser",), 2),
    TermRule("photon mapping", r"\bphoton mapping\b", ("光子映射",), "medium", ("Photon Mapping",), 2),
    TermRule("caustics", r"\bcaustics?\b", ("焦散",), "medium", (), 2),
    TermRule("motion vector", r"\bmotion vectors?\b", ("运动矢量",), "medium", (), 2),
    TermRule("normal map", r"\bnormal maps?\b", ("法线贴图",), "medium", (), 2),
    TermRule("depth map", r"\bdepth maps?\b", ("深度贴图",), "medium", (), 2),
    TermRule("volumetric fluid simulation", r"\bvolumetric fluid simulations?\b", ("体积流体模拟",), "high", (), 2),
    TermRule("voxel", r"\bvoxels?\b", ("体素",), "medium", (), 3),
    TermRule("sparse volume", r"\bsparse volumes?\b", ("稀疏体积",), "medium", (), 2),
    TermRule("level set", r"\blevel sets?\b", ("水平集",), "medium", (), 2),
    TermRule("signed distance field", r"\bsigned[- ]distance fields?\b", ("符号距离场", "SDF"), "medium", ("SDF",), 2),
    TermRule("isosurface", r"\bisosurfaces?\b", ("等值面",), "medium", (), 2),
    TermRule("isovalue", r"\bisovalue\b", ("等值",), "medium", (), 2),
    TermRule("whitewater", r"\bwhitewater\b|\bwhite water\b", ("白水",), "high", (), 2),
    TermRule("foam", r"\bfoam\b", ("泡沫",), "medium", (), 3),
    TermRule("spray", r"\bspray\b", ("飞溅",), "medium", (), 3),
    TermRule("bubbles", r"\bbubbles?\b", ("气泡",), "medium", (), 3),
    TermRule("viscosity", r"\bviscosity\b", ("黏度",), "medium", (), 2),
    TermRule("dynamic viscosity coefficient", r"\bdynamic viscosity coefficient\b", ("动态黏度系数",), "medium", (), 2),
    TermRule("surface tension", r"\bsurface tension\b", ("表面张力",), "medium", (), 2),
    TermRule("pressure projection", r"\bpressure projection\b", ("压力投影",), "medium", (), 2),
    TermRule("projection iterations", r"\bprojection iterations?\b", ("投影迭代",), "medium", (), 2),
    TermRule("divergence", r"\bdivergence\b", ("散度",), "medium", (), 2),
    TermRule("non-divergent", r"\bnon[- ]divergent\b", ("无散度",), "medium", (), 2),
    TermRule("volume conservation", r"\bvolume conservation\b", ("体积守恒",), "medium", (), 2),
    TermRule("incompressibility", r"\bincompressibility\b", ("不可压缩",), "medium", (), 2),
    TermRule("advection", r"\badvection\b|\badvected\b|\badvect\b", ("平流", "输运"), "medium", (), 3),
    TermRule("velocity field", r"\bvelocity field\b", ("速度场",), "medium", (), 2),
    TermRule("scalar field", r"\bscalar field\b", ("标量场",), "medium", (), 2),
    TermRule("vector field", r"\bvector field\b", ("矢量场",), "medium", (), 2),
    TermRule("buoyancy", r"\bbuoyancy\b", ("浮力",), "medium", (), 2),
    TermRule("combustion", r"\bcombustion\b", ("燃烧",), "medium", (), 2),
    TermRule("vorticity", r"\bvorticity\b", ("涡量",), "medium", (), 2),
    TermRule("vortex confinement", r"\bvortex confinement\b", ("涡旋约束", "涡量约束"), "medium", (), 2),
    TermRule("curl noise", r"\bcurl noise\b", ("旋度噪声",), "medium", (), 2),
    TermRule("dissipation", r"\bdissipation\b", ("耗散",), "medium", (), 2),
    TermRule("shredding", r"\bshredding\b", ("撕裂",), "medium", (), 2),
    TermRule("scattering", r"\bscattering\b", ("散射",), "medium", (), 3),
    TermRule("absorption", r"\babsorption\b", ("吸收",), "medium", (), 3),
    TermRule("emissive", r"\bemissive\b", ("自发光",), "medium", ("Emissive",), 3),
    TermRule("antialiasing", r"\bantialiasing\b|\banti-aliasing\b", ("抗锯齿",), "medium", ("SMAA",), 2),
]

TERM_PATTERNS = [(rule, re.compile(rule.source_pattern, re.IGNORECASE)) for rule in TERM_RULES]

COMMON_ENGLISH_PROSE = {
    "simulation",
    "simulations",
    "fluid",
    "volumetric",
    "parameter",
    "parameters",
    "viewport",
    "timeline",
    "keyframe",
    "keyframes",
    "node",
    "nodes",
    "graph",
    "render",
    "renderer",
    "rendering",
    "export",
    "import",
    "flipbook",
    "flipbooks",
    "sprite",
    "sprites",
    "sheet",
    "sheets",
    "texture",
    "textures",
    "atlas",
    "mesh",
    "meshing",
    "voxel",
    "voxels",
    "volume",
    "volumes",
    "grid",
    "field",
    "fields",
    "whitewater",
    "foam",
    "spray",
    "bubbles",
    "viscosity",
    "divergence",
    "advection",
    "buoyancy",
    "scattering",
    "absorption",
    "emissive",
    "rasterizer",
    "denoiser",
    "caustics",
}


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def page_name_to_segment_file(page_file: Path) -> Path:
    return SEGMENTS_DIR / page_file.name


def source_word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z]+", text))


def has_cjk(text: str) -> bool:
    return bool(CJK_RE.search(text))


def latin_tokens(text: str) -> list[str]:
    return LATIN_TOKEN_RE.findall(text)


def strip_annotated_english(text: str) -> str:
    # Treat "English Label（中文解释）" as reviewed rather than over-retained.
    return re.sub(r"[A-Za-z][A-Za-z0-9_+./#:\- ]*（[^）]*[\u4e00-\u9fff][^）]*）", "", text)


def protected_token(token: str) -> bool:
    if token in PROTECTED_TOKENS:
        return True
    if token.upper() in PROTECTED_TOKENS:
        return True
    if re.fullmatch(r"[A-Z]{2,}[0-9]*", token):
        return True
    if re.fullmatch(r"[A-Za-z]+[0-9]+", token):
        return True
    if "." in token or "/" in token or "_" in token:
        return True
    return False


def context_is_likely_label(source: str, target: str) -> bool:
    stripped_source = source.strip()
    stripped_target = target.strip()
    if not stripped_source or not stripped_target:
        return True
    if len(stripped_source.split()) <= 3 and stripped_source[:1].isupper():
        return True
    if stripped_source.endswith(":") and len(stripped_source.split()) <= 5:
        return True
    if stripped_source == stripped_target and len(stripped_source.split()) <= 4:
        return True
    return False


def neighboring_targets(translations: list[dict[str, object]], index: int, radius: int = 4) -> str:
    start = max(0, index - radius)
    end = min(len(translations), index + radius + 1)
    return " ".join(str(translations[item].get("target", "")) for item in range(start, end))


def may_be_split_inline_fragment(source: str, target: str) -> bool:
    return source[:1].isspace() or source[-1:].isspace() or target[:1].isspace() or target[-1:].isspace()


def severity_rank(severity: str) -> int:
    return {"high": 0, "medium": 1, "low": 2}.get(severity, 3)


def audit() -> dict[str, object]:
    findings: list[dict[str, object]] = []
    term_targets: dict[str, Counter[str]] = defaultdict(Counter)
    totals = {
        "pages": 0,
        "segments": 0,
        "translated_segments": 0,
    }

    for page_file in sorted(PAGES_DIR.glob("*.json")):
        page_payload = read_json(page_file)
        segment_payload = read_json(page_name_to_segment_file(page_file))
        meta_by_id = {item["id"]: item for item in segment_payload.get("segments", [])}
        path = page_payload["path"]
        totals["pages"] += 1
        translations_list = list(page_payload.get("translations", []))
        for index, item in enumerate(translations_list):
            totals["segments"] += 1
            source = str(item.get("source", ""))
            target = str(item.get("target", ""))
            if target.strip():
                totals["translated_segments"] += 1
            meta = meta_by_id.get(item.get("id"), {})
            line = meta.get("line")
            source_words = source_word_count(source)
            likely_label = context_is_likely_label(source, target)

            for rule, pattern in TERM_PATTERNS:
                if not pattern.search(source):
                    continue
                if source_words < rule.min_source_words and likely_label:
                    continue
                if any(expected in target for expected in rule.expected):
                    for expected in rule.expected:
                        if expected in target:
                            term_targets[rule.name][expected] += 1
                    continue
                if any(allowed in target for allowed in rule.allow_english_target) and likely_label:
                    continue
                if may_be_split_inline_fragment(source, target):
                    nearby = neighboring_targets(translations_list, index)
                    if any(expected in nearby for expected in rule.expected):
                        continue
                findings.append(
                    {
                        "type": "missing_preferred_translation",
                        "severity": rule.severity,
                        "term": rule.name,
                        "path": path,
                        "line": line,
                        "index": index,
                        "source": source,
                        "target": target,
                        "expected": list(rule.expected),
                    }
                )

            if has_cjk(target):
                english_scan_target = strip_annotated_english(target)
                tokens = latin_tokens(english_scan_target)
                unprotected = [token for token in tokens if not protected_token(token)]
                prose_tokens = [token for token in unprotected if token.lower() in COMMON_ENGLISH_PROSE]
                latin_chars = sum(len(token) for token in unprotected)
                cjk_chars = len(CJK_RE.findall(target))
                if prose_tokens and not likely_label:
                    findings.append(
                        {
                            "type": "english_retention",
                            "severity": "medium",
                            "term": ", ".join(sorted(set(prose_tokens), key=str.lower)),
                            "path": path,
                            "line": line,
                            "index": index,
                            "source": source,
                            "target": target,
                            "expected": ["translate prose English unless it is an exact UI label"],
                        }
                    )
                if len(unprotected) >= 3 and cjk_chars and latin_chars / max(cjk_chars, 1) >= 0.35 and not likely_label:
                    findings.append(
                        {
                            "type": "mixed_readability",
                            "severity": "low",
                            "term": ", ".join(unprotected[:8]),
                            "path": path,
                            "line": line,
                            "index": index,
                            "source": source,
                            "target": target,
                            "expected": ["reduce English-token density in Chinese prose"],
                        }
                    )

    deduped = []
    seen = set()
    for finding in findings:
        key = (
            finding["type"],
            finding.get("term"),
            finding["path"],
            finding["index"],
            tuple(finding.get("expected", [])),
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(finding)

    deduped.sort(key=lambda item: (severity_rank(str(item["severity"])), str(item["path"]), int(item["index"])))

    conflicts = []
    for term, counter in sorted(term_targets.items()):
        if len(counter) <= 1:
            continue
        conflicts.append({"term": term, "variants": dict(counter)})

    return {
        "totals": totals,
        "finding_count": len(deduped),
        "findings_by_type": dict(Counter(str(item["type"]) for item in deduped)),
        "findings_by_severity": dict(Counter(str(item["severity"]) for item in deduped)),
        "term_conflicts": conflicts,
        "findings": deduped,
    }


def write_markdown(report: dict[str, object], limit: int) -> None:
    findings = list(report["findings"])
    totals = report["totals"]
    lines = [
        "# JangaFX Terminology Scan Report",
        "",
        "This is an automated candidate list. Each finding still needs contextual review before any translation edit.",
        "",
        "## Summary",
        "",
        f"- Pages scanned: {totals['pages']}",
        f"- Segments scanned: {totals['segments']}",
        f"- Translated segments: {totals['translated_segments']}",
        f"- Candidate findings: {report['finding_count']}",
        f"- Findings by severity: {report['findings_by_severity']}",
        f"- Findings by type: {report['findings_by_type']}",
        "",
        "## Top Candidates",
        "",
    ]

    for finding in findings[:limit]:
        expected = ", ".join(finding.get("expected", []))
        lines.extend(
            [
                f"### {str(finding['severity']).upper()} - {finding['type']} - {finding.get('term', '')}",
                "",
                f"- Page: `{finding['path']}`",
                f"- Segment index: `{finding['index']}`",
                f"- Source: {finding['source']}",
                f"- Target: {finding['target']}",
                f"- Expected: {expected}",
                "",
            ]
        )

    if report["term_conflicts"]:
        lines.extend(["## Term Variant Counters", ""])
        for conflict in report["term_conflicts"]:
            lines.append(f"- `{conflict['term']}`: {conflict['variants']}")
        lines.append("")

    (REPORTS_DIR / "terminology_scan.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=160, help="Number of findings to include in the markdown report.")
    args = parser.parse_args()

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report = audit()
    (REPORTS_DIR / "terminology_scan.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(report, args.limit)

    print(f"Pages scanned: {report['totals']['pages']}")
    print(f"Segments scanned: {report['totals']['segments']}")
    print(f"Candidate findings: {report['finding_count']}")
    print(f"Findings by severity: {report['findings_by_severity']}")
    print(f"Findings by type: {report['findings_by_type']}")
    print("Wrote translation/reports/terminology_scan.json")
    print("Wrote translation/reports/terminology_scan.md")


if __name__ == "__main__":
    main()
