#!/usr/bin/env python3
"""Read or search P1-P4/YZ videos and Zhoulan image/video records (ZLI/ZLV)."""
import argparse
import json
import re
import sys
from pathlib import Path

SOURCES = {f"P{i}": f"029-p{i}-media-prompts.md" for i in range(1, 5)}
SOURCES["YZ"] = "yizhong-ep4-original-prompts.md"
SOURCES["ZLI"] = "zhoulan-image-prompts.md"
SOURCES["ZLV"] = "zhoulan-video-prompts.md"
HEADER = re.compile(r"^### (.+?) · (v-[A-Za-z0-9]+)\s*$", re.MULTILINE)
PROMPT = re.compile(r"^~~~~text[^\n]*\n(.*?)^~~~~\s*$", re.MULTILINE | re.DOTALL)
YZ_HEADER = re.compile(r"^## (YZ\d{2})｜(.+)$", re.MULTILINE)
YZ_PROMPT = re.compile(r"^```text\n(.*?)\n```[ \t]*$", re.MULTILINE | re.DOTALL)
ZL_HEADER = re.compile(r"^### (ZL[IV]\d{3})｜(.+?) · ([A-Za-z0-9-]+)[ \t]*$", re.MULTILINE)
ZL_PROMPT = re.compile(r"^~~~~text\n(.*?)\n~~~~[ \t]*$", re.MULTILINE | re.DOTALL)


def zhoulan_records(raw, filename, source):
    """Retain every current node, including explicitly empty prompt records."""
    headings = list(ZL_HEADER.finditer(raw))
    if not headings:
        raise ValueError(f"No Zhoulan records found in {filename}")
    for i, heading in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(raw)
        section = raw[heading.start():end]
        # The following record's HTML anchor belongs to that record, not this one.
        section = re.split(r'\n<a id="zl[iv]\d{3}"></a>', section, maxsplit=1)[0].rstrip()
        match = ZL_PROMPT.search(section)
        if not match and "提示词为空；无可读取的生成正文。" not in section:
            raise ValueError(f"Incomplete archived record: {filename} {heading.group(1)}")
        if not heading.group(1).startswith(source):
            raise ValueError(f"Wrong archive type: {filename} {heading.group(1)}")
        yield {
            "source": source, "file": filename,
            "caseId": heading.group(1), "title": heading.group(2),
            "nodeKey": heading.group(3),
            "line": raw.count("\n", 0, heading.start()) + 1,
            "prompt": match.group(1) if match else "",
            "raw": section, "empty": not match,
        }


def yizhong_records(raw, filename):
    """Read each distinct full text; retain every same-text nodeKey as an alias."""
    headings = list(YZ_HEADER.finditer(raw))
    if not headings:
        raise ValueError(f"No YZ records found in {filename}")
    for i, heading in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(raw)
        section = raw[heading.start():end]
        match = YZ_PROMPT.search(section)
        representative = re.search(r"代表节点：`(v-[A-Za-z0-9]+)`", section)
        aliases = re.search(r"同正文节点：([^\n]+)。", section)
        if not match or not representative or not aliases:
            raise ValueError(f"Incomplete archived record: {filename} {heading.group(1)}")
        yield {
            "source": "YZ", "file": filename,
            "caseId": heading.group(1), "title": heading.group(2),
            "nodeKey": representative.group(1),
            "nodeKeys": re.findall(r"v-[A-Za-z0-9]+", aliases.group(1)),
            "line": raw.count("\n", 0, heading.start()) + 1,
            "prompt": match.group(1), "raw": section[:match.end()].rstrip(),
        }


def records(root, source=None):
    """Preserve the archive's raw record and prompt; no rewriting or deduplication."""
    for key, filename in SOURCES.items():
        if source and key != source:
            continue
        path = root / "references" / filename
        if not path.is_file():
            raise ValueError(f"Missing source: {path}")
        if key in ("ZLI", "ZLV"):
            # Some original prompts contain CRLF; do not normalize their bytes.
            with path.open(encoding="utf-8-sig", newline="") as handle:
                raw = handle.read()
        else:
            raw = path.read_text(encoding="utf-8-sig")
        if key == "YZ":
            yield from yizhong_records(raw, filename)
            continue
        if key in ("ZLI", "ZLV"):
            yield from zhoulan_records(raw, filename, key)
            continue
        headings = list(HEADER.finditer(raw))
        for i, heading in enumerate(headings):
            end = headings[i + 1].start() if i + 1 < len(headings) else len(raw)
            section = raw[heading.start():end]
            match = PROMPT.search(section)
            if not match or not match.group(1).strip():
                continue
            yield {
                "source": key, "file": filename, "title": heading.group(1),
                "nodeKey": heading.group(2),
                "line": raw.count("\n", 0, heading.start()) + 1,
                "prompt": match.group(1), "raw": section[:match.end()].rstrip(),
            }


def search(items, terms, limit):
    hits = []
    for item in items:
        haystack = item["title"] + "\n" + item["prompt"]
        found = [term for term in terms if term.casefold() in haystack.casefold()]
        if not found:
            continue
        snippets = []
        for term in found:
            at = haystack.casefold().find(term.casefold())
            snippets.append(haystack[max(0, at - 45):at + len(term) + 85].replace("\n", " "))
        hits.append({k: item[k] for k in ("source", "file", "title", "nodeKey", "line")} | {
            "matched_terms": found, "snippets": snippets,
        } | ({"caseId": item["caseId"], "nodeKeys": item["nodeKeys"]} if item["source"] == "YZ" else {})
          | ({"caseId": item["caseId"], "empty": item["empty"]} if item["source"] in ("ZLI", "ZLV") else {}))
    hits.sort(key=lambda hit: -len(hit["matched_terms"]))
    return {"matching_records": len(hits), "returned": hits[:limit],
            "note": "Exact local term matches; snippets are not a complete reading or a quality ranking."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", choices=list(SOURCES))
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--case", help="Exact title, nodeKey, YZ01-YZ31, ZLI001-ZLI163, or ZLV001-ZLV050; no fuzzy selection")
    group.add_argument("--search", nargs="+", help="Literal terms, any-match; more matching terms rank first")
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    root = Path(__file__).resolve().parents[1]
    try:
        items = list(records(root, args.source))
        if args.search:
            print(json.dumps(search(items, args.search, args.limit), ensure_ascii=False, indent=2))
            return 0
        selected = [item for item in items if args.case in
                    [item["title"], item["nodeKey"], item.get("caseId"), *item.get("nodeKeys", [])]]
        if len(selected) != 1:
            identities = [{k: item[k] for k in ("source", "file", "title", "nodeKey")} for item in selected]
            print(json.dumps({"error": "Case missing or ambiguous; specify exact nodeKey and --source.",
                              "candidates": identities}, ensure_ascii=False), file=sys.stderr)
            return 2
        print(f"Source: {selected[0]['file']}:{selected[0]['line']}\n")
        print(selected[0]["raw"])
        return 0
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    sys.exit(main())
