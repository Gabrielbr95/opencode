#!/usr/bin/env python3

import argparse
import json
from datetime import datetime
from pathlib import Path


def read_json(path: Path):
    raw = path.read_bytes()
    for encoding in ("utf-16", "utf-8-sig", "utf-8"):
        try:
            return json.loads(raw.decode(encoding))
        except UnicodeDecodeError:
            continue
    return json.loads(raw.decode("utf-8", errors="replace"))


def fmt_time(ms):
    if not ms:
        return "00:00:00"
    return datetime.fromtimestamp(ms / 1000).strftime("%H:%M:%S")


def render_tool_part(part):
    lines = [f"**[TOOL: {part.get('tool', 'tool')}]**"]
    state = part.get("state", {})
    if "input" in state:
        lines.append("Input: " + json.dumps(state["input"], indent=2, ensure_ascii=False))
    return lines


def convert_session(data):
    info = data.get("info", {})
    title = info.get("title") or "Session Export"
    lines = [f"# Session Export: {title}", ""]

    for message in data.get("messages", []):
        meta = message.get("info", {})
        role = meta.get("role", "unknown").upper()
        created = meta.get("time", {}).get("created")

        lines.append("---")
        lines.append(f"## {role}  {fmt_time(created)}")
        lines.append("")

        for part in message.get("parts", []):
            ptype = part.get("type")
            if ptype == "text":
                text = part.get("text", "")
                lines.append(text.rstrip())
                lines.append("")
            elif ptype == "tool":
                lines.extend(render_tool_part(part))
                lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description="Convert OpenCode session JSON to markdown transcript.")
    parser.add_argument("input", help="Path to the session JSON export")
    parser.add_argument("-o", "--output", help="Output markdown path")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".md")

    data = read_json(input_path)
    output_path.write_text(convert_session(data), encoding="utf-8")


if __name__ == "__main__":
    main()
