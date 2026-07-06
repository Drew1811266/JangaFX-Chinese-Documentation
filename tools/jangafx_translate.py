#!/usr/bin/env python3
"""Raw-preserving HTML translation helpers for the mirrored JangaFX docs.

The script deliberately does not serialize HTML through a DOM library. It uses
HTMLParser only to locate translatable text nodes, then applies translated text
back to the original byte ranges. This keeps tags, attributes, whitespace around
tags, scripts, styles, links, and Sphinx/Furo structure untouched.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
from dataclasses import dataclass, asdict
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import quote, urljoin, urlparse, urldefrag, unquote


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "jangafx-docs"
TARGET_DIR = ROOT / "jangafx-docs-zh"
TRANSLATION_DIR = ROOT / "translation"
SEGMENTS_DIR = TRANSLATION_DIR / "segments"
PAGES_DIR = TRANSLATION_DIR / "pages"
REPORTS_DIR = TRANSLATION_DIR / "reports"
MEMORY_FILE = TRANSLATION_DIR / "translation_memory.zh-CN.json"

SKIP_TAGS = {
    "script",
    "style",
    "code",
    "pre",
    "kbd",
    "samp",
    "textarea",
    "svg",
    "math",
}
SKIP_CLASSES = {
    "notranslate",
    "highlight",
    "linenos",
    "linenodiv",
}
TRANSLATABLE_ALPHA_RE = re.compile(r"[A-Za-z]")
ONLY_TECHNICAL_RE = re.compile(r"^[A-Za-z0-9_./:#%+(){}\[\], \\-]+$")


@dataclass(frozen=True)
class Segment:
    id: str
    path: str
    start: int
    end: int
    line: int
    parent_path: str
    source_raw: str
    source_text: str


def html_files(root: Path = SOURCE_DIR) -> list[Path]:
    return sorted(root.rglob("*.html"))


def safe_page_name(rel_path: str) -> str:
    return quote(rel_path, safe="").replace("%", "_") + ".json"


def line_offsets(text: str) -> list[int]:
    offsets = [0]
    for match in re.finditer("\n", text):
        offsets.append(match.end())
    return offsets


def should_translate(text: str) -> bool:
    stripped = " ".join(text.split())
    if not stripped:
        return False
    if stripped in {"'s", "’s", "to", "or", "by", "If", "if"}:
        return True
    if not TRANSLATABLE_ALPHA_RE.search(stripped):
        return False
    if len(stripped) <= 2:
        return False
    # Keep env vars, IDs, and code-like fragments out of the translation queue.
    if ONLY_TECHNICAL_RE.fullmatch(stripped) and any(
        token in stripped for token in ("_", "/", "\\", "::", ".com", ".html", "http")
    ) and len(stripped.split()) <= 3:
        return False
    return True


class SegmentParser(HTMLParser):
    def __init__(self, rel_path: str, text: str):
        super().__init__(convert_charrefs=True)
        self.rel_path = rel_path
        self.text = text
        self.offsets = line_offsets(text)
        self.segments: list[Segment] = []
        self.skip_depth = 0
        self.stack: list[str] = []

    def absolute_offset(self) -> int:
        line, col = self.getpos()
        if line <= 0 or line > len(self.offsets):
            return 0
        return self.offsets[line - 1] + col

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        self.stack.append(tag)
        class_value = " ".join(value or "" for name, value in attrs if name.lower() == "class")
        classes = set(class_value.split())
        if self.skip_depth or tag in SKIP_TAGS or classes.intersection(SKIP_CLASSES):
            self.skip_depth += 1

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        # Self-closing tags do not contain text. Attribute translation is not
        # enabled here because preserving markup takes priority for this corpus.
        return

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self.skip_depth:
            self.skip_depth -= 1
        if tag in self.stack:
            for index in range(len(self.stack) - 1, -1, -1):
                if self.stack[index] == tag:
                    del self.stack[index:]
                    break

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if not should_translate(data):
            return
        start = self.absolute_offset()
        end = self.text.find("<", start)
        if end == -1:
            end = len(self.text)
        raw = self.text[start:end]
        source_text = html.unescape(raw)
        if not should_translate(source_text):
            return
        digest = hashlib.sha1(f"{self.rel_path}:{start}:{raw}".encode("utf-8")).hexdigest()[:12]
        self.segments.append(
            Segment(
                id=digest,
                path=self.rel_path,
                start=start,
                end=end,
                line=self.getpos()[0],
                parent_path="/".join(self.stack[-5:]),
                source_raw=raw,
                source_text=source_text,
            )
        )


def extract_segments_for_file(path: Path) -> list[Segment]:
    rel = path.relative_to(SOURCE_DIR).as_posix()
    text = path.read_text(encoding="utf-8", errors="replace")
    parser = SegmentParser(rel, text)
    parser.feed(text)
    return parser.segments


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def command_extract(args: argparse.Namespace) -> None:
    SEGMENTS_DIR.mkdir(parents=True, exist_ok=True)
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    manifest = []
    total_segments = 0
    for html_path in html_files():
        rel = html_path.relative_to(SOURCE_DIR).as_posix()
        segments = extract_segments_for_file(html_path)
        total_segments += len(segments)
        page_payload = {
            "path": rel,
            "segment_count": len(segments),
            "segments": [asdict(segment) for segment in segments],
        }
        segment_file = SEGMENTS_DIR / safe_page_name(rel)
        write_json(segment_file, page_payload)
        page_file = PAGES_DIR / safe_page_name(rel)
        existing_by_id = {}
        existing_by_source = {}
        existing_status = "pending"
        if page_file.exists() and not args.force:
            existing_payload = read_json(page_file)
            existing_status = existing_payload.get("status", "pending")
            for item in existing_payload.get("translations", []):
                existing_by_id[item.get("id")] = item
                existing_by_source.setdefault(item.get("source"), item)
        translation_items = []
        for segment in segments:
            existing = existing_by_id.get(segment.id) or existing_by_source.get(segment.source_text) or {}
            translation_items.append(
                {
                    "id": segment.id,
                    "source": segment.source_text,
                    "target": existing.get("target", ""),
                    "note": existing.get("note", ""),
                }
            )
        translation_payload = {
            "path": rel,
            "status": existing_status,
            "translations": translation_items,
        }
        write_json(page_file, translation_payload)
        manifest.append(
            {
                "path": rel,
                "segments": len(segments),
                "segment_file": segment_file.relative_to(ROOT).as_posix(),
                "translation_file": page_file.relative_to(ROOT).as_posix(),
            }
        )

    write_json(
        TRANSLATION_DIR / "manifest.json",
        {
            "source_dir": SOURCE_DIR.relative_to(ROOT).as_posix(),
            "target_dir": TARGET_DIR.relative_to(ROOT).as_posix(),
            "html_files": len(manifest),
            "segments": total_segments,
            "pages": manifest,
        },
    )
    print(f"Extracted {total_segments} segments from {len(manifest)} HTML files.")


def translated_text_for_page(rel: str) -> dict[str, str]:
    page_file = PAGES_DIR / safe_page_name(rel)
    if not page_file.exists():
        return {}
    payload = read_json(page_file)
    translations = {}
    for item in payload.get("translations", []):
        target = item.get("target", "")
        if isinstance(target, str) and target.strip():
            translations[item["id"]] = target
    return translations


def escape_text_node(target: str, source_raw: str) -> str:
    leading = re.match(r"^\s*", source_raw).group(0)
    trailing = re.search(r"\s*$", source_raw).group(0)
    normalized = target.strip()
    return leading + html.escape(normalized, quote=False) + trailing


def normalize_cjk_inline_punctuation(text: str) -> str:
    """Polish punctuation left between translated CJK text and inline tags."""
    inline_close = r"</(?:em|strong|code|span)>"
    text = re.sub(rf"({inline_close})[ \t]*,[ \t]*(<em\b)", r"\1、\2", text)
    text = re.sub(rf"({inline_close})[ \t]*或[ \t]*(<em\b)", r"\1 或 \2", text)
    text = re.sub(rf"({inline_close})[ \t]*和[ \t]*(<em\b)", r"\1 和 \2", text)
    text = re.sub(rf"({inline_close})[ \t]*\.(?=</p>|</li>|</dd>|</dt>|</h[1-6]>|\s*</)", r"\1。", text)
    text = re.sub(rf"({inline_close})\.[ \t]*(<cite\b)", r"\1。\2", text)
    text = re.sub(rf"({inline_close})[ \t]+([，。！？；：、（）”])", r"\1\2", text)
    text = re.sub(r"(</a>)[ \t]*([，。！？；：、）])", r"\1\2", text)
    text = re.sub(r"(</a>)\)", r"\1）", text)
    text = re.sub(r"(</a>)\.(?=</p>|</li>|</dd>|</dt>|</h[1-6]>|\s*</)", r"\1。", text)
    text = re.sub(r"(</a>)!(?=</p>|</li>|</dd>|</dt>|</h[1-6]>|\s*</)", r"\1！", text)
    text = re.sub(r"([（《“])[ \t]+(<(?:em|strong|code|span)\b)", r"\1\2", text)
    text = re.sub(r"(</a>)[ \t]*的\b", r"\1 的", text)
    text = re.sub(r"([，。！？；：、])\s+(?=[\u4e00-\u9fff])", r"\1", text)
    text = re.sub(r"([\u4e00-\u9fff])\s+(?=[\u4e00-\u9fff])", r"\1", text)
    text = re.sub(r"([\u4e00-\u9fff])\s+([，。！？；：、])", r"\1\2", text)
    text = re.sub(r"([\u4e00-\u9fff])\s+(<em>[\u4e00-\u9fff]+</em>)", r"\1\2", text)
    text = re.sub(r"([A-Za-z0-9…)])\s+：", r"\1：", text)
    text = re.sub(r"([\u4e00-\u9fff])\s+(<strong>[\u4e00-\u9fff]+</strong>)\s+(?=[\u4e00-\u9fff])", r"\1\2", text)
    text = re.sub(r"\b(Min/Max|Open_Paren|Close_Paren):", r"\1：", text)
    text = re.sub(r"(<strong>[^<]{1,80}):</strong>", r"\1：</strong>", text)
    text = re.sub(r"(</code>|</em>)(?=的|位置|选项|标志|配置文件|与|可以|会)", r"\1 ", text)
    text = re.sub(r"(</code>)\s+；", r"\1；", text)
    text = re.sub(r"(</code>)\)", r"\1）", text)
    text = re.sub(r"默认：\s+(<code\b)", r"默认：\1", text)
    text = re.sub(r"到\s+(<a\b[^>]*>此处</a>)", r"到\1", text)
    text = text.replace("@pradyunsg的", "@pradyunsg 的")
    text = text.replace("cmd ；", "cmd；")
    text = text.replace("此处，", "此处，")
    text = text.replace("Timeline Editor中", "Timeline Editor 中")
    text = text.replace("当 Grouping size 不为 1:", "当 Grouping size 不为 1 时：")
    text = text.replace("我们的 调制曲线 页面", "我们的调制曲线页面")
    text = text.replace("不同， Volume Processing", "不同，Volume Processing")
    text = re.sub(r"(当\s*<em>Grouping size</em>\s*不为\s*<em>1</em>):", r"\1 时：", text)
    text = re.sub(
        r"我们的\s+(<a[^>]+href=\"[^\"]*modulation_curve[^\"]*\"[^>]*>.*?</a>)\s+页面",
        r"我们的\1页面",
        text,
        flags=re.DOTALL,
    )
    text = text.replace("节点不同， <a", "节点不同，<a")
    text = text.replace("</a> <em>Volume Processing</em>", "</a><em>Volume Processing</em>")
    text = text.replace(
        "用于在 <em>Remapping curve</em>。",
        "用于在 <em>Remapping curve</em> 曲线各点之间进行插值的方法。",
    )
    text = text.replace("Powerful combustion/explosions", "强燃烧/爆炸")
    return text


def apply_page(rel: str, segments: list[dict[str, object]], translations: dict[str, str]) -> int:
    source_file = SOURCE_DIR / rel
    target_file = TARGET_DIR / rel
    text = source_file.read_text(encoding="utf-8", errors="replace")
    edits = []
    for segment in segments:
        target = translations.get(str(segment["id"]))
        if not target:
            continue
        start = int(segment["start"])
        end = int(segment["end"])
        source_raw = str(segment["source_raw"])
        if text[start:end] != source_raw:
            raise RuntimeError(f"Source range mismatch in {rel} at {start}:{end}")
        edits.append((start, end, escape_text_node(target, source_raw)))
    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]
    text = re.sub(r'(<html\b[^>]*\blang=")en(")', r"\1zh-CN\2", text, count=1)
    text = normalize_cjk_inline_punctuation(text)
    target_file.parent.mkdir(parents=True, exist_ok=True)
    target_file.write_text(text, encoding="utf-8")
    return len(edits)


def command_apply(args: argparse.Namespace) -> None:
    if not SOURCE_DIR.exists():
        raise SystemExit(f"Missing source docs: {SOURCE_DIR}")
    if TARGET_DIR.exists() and args.clean:
        shutil.rmtree(TARGET_DIR)
    if not TARGET_DIR.exists():
        shutil.copytree(SOURCE_DIR, TARGET_DIR)

    manifest = read_json(TRANSLATION_DIR / "manifest.json")
    applied_pages = 0
    applied_segments = 0
    for page in manifest["pages"]:
        rel = page["path"]
        if args.page and rel != args.page:
            continue
        segment_payload = read_json(ROOT / page["segment_file"])
        translations = translated_text_for_page(rel)
        if not translations:
            continue
        count = apply_page(rel, segment_payload["segments"], translations)
        applied_pages += 1
        applied_segments += count
    print(f"Applied {applied_segments} translated segments across {applied_pages} pages.")


def command_memory(args: argparse.Namespace) -> None:
    if not MEMORY_FILE.exists():
        raise SystemExit(f"Missing translation memory: {MEMORY_FILE}")
    memory = read_json(MEMORY_FILE)
    if not isinstance(memory, dict):
        raise SystemExit("Translation memory must be a JSON object.")

    updated_files = 0
    updated_segments = 0
    for page_file in sorted(PAGES_DIR.glob("*.json")):
        payload = read_json(page_file)
        changed = False
        for item in payload.get("translations", []):
            if item.get("target", "").strip():
                continue
            source = item.get("source", "")
            target = memory.get(source)
            if isinstance(target, str) and target.strip():
                item["target"] = target
                item["note"] = "translation memory"
                changed = True
                updated_segments += 1
        if changed:
            payload["status"] = "in_progress"
            write_json(page_file, payload)
            updated_files += 1
    print(f"Filled {updated_segments} segments across {updated_files} page files from memory.")


TAG_RE = re.compile(r"<!--.*?-->|<![^>]*>|<[^>]+>", re.DOTALL)


def tag_sequence(text: str) -> list[str]:
    tags = []
    for tag in TAG_RE.findall(text):
        if tag.lower().startswith("<html"):
            tag = re.sub(r'\blang=(["\']).*?\1', r"lang=\1__LANG__\1", tag, count=1)
        tags.append(tag)
    return tags


def iter_local_links(html_text: str, rel_path: str) -> Iterable[tuple[str, str]]:
    for match in re.finditer(r"""(?:href|src|data-src|poster)=["']([^"']+)["']""", html_text):
        raw = match.group(1)
        if not raw or raw.startswith(("#", "mailto:", "tel:", "javascript:", "data:", "http://", "https://")):
            continue
        url, _ = urldefrag(urljoin("https://docs.jangafx.com/" + rel_path, raw))
        parsed = urlparse(url)
        path = unquote(parsed.path)
        if not path or path == "/":
            path = "/index.html"
        if path.endswith("/"):
            path += "index.html"
        yield raw, path.lstrip("/")


def command_validate(args: argparse.Namespace) -> None:
    if not TARGET_DIR.exists():
        raise SystemExit(f"Missing target docs: {TARGET_DIR}")
    tag_mismatches = []
    missing_links = []
    html_count = 0
    for source_file in html_files():
        rel = source_file.relative_to(SOURCE_DIR).as_posix()
        target_file = TARGET_DIR / rel
        if not target_file.exists():
            tag_mismatches.append((rel, "missing target file"))
            continue
        html_count += 1
        source_text = source_file.read_text(encoding="utf-8", errors="replace")
        target_text = target_file.read_text(encoding="utf-8", errors="replace")
        if tag_sequence(source_text) != tag_sequence(target_text):
            tag_mismatches.append((rel, "tag sequence changed"))
        for raw, local_target in iter_local_links(target_text, rel):
            if not (TARGET_DIR / local_target).exists():
                missing_links.append((rel, raw, local_target))

    report = {
        "html_files_checked": html_count,
        "tag_mismatches": tag_mismatches,
        "missing_local_links": missing_links,
    }
    write_json(REPORTS_DIR / "validate.json", report)
    print(f"HTML files checked: {html_count}")
    print(f"Tag mismatches: {len(tag_mismatches)}")
    print(f"Missing local links/assets: {len(missing_links)}")
    if tag_mismatches or missing_links:
        raise SystemExit(1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    extract = subparsers.add_parser("extract", help="Extract translatable text segments.")
    extract.add_argument("--force", action="store_true", help="Overwrite existing page translation files.")
    extract.set_defaults(func=command_extract)

    apply = subparsers.add_parser("apply", help="Apply translated segments into jangafx-docs-zh.")
    apply.add_argument("--clean", action="store_true", help="Recreate the target directory before applying.")
    apply.add_argument("--page", help="Apply a single relative HTML path.")
    apply.set_defaults(func=command_apply)

    memory = subparsers.add_parser("memory", help="Fill blank page translations from translation memory.")
    memory.set_defaults(func=command_memory)

    validate = subparsers.add_parser("validate", help="Validate that tags and local links are preserved.")
    validate.set_defaults(func=command_validate)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
