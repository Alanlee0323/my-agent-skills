#!/usr/bin/env python3
"""Regenerate SKILL_INDEX.md from SKILL.md frontmatter (stdlib only).

SKILL_INDEX.md is a generated artifact — never hand-edit it; edit the skill
frontmatter and re-run this script. See skills/meta/maintaining-skill-library.

Usage: python tools/generate_skill_index.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_skills import ROOT, SKILLS_DIR, parse_frontmatter  # noqa: E402

DOMAIN_TITLES = {
    "shared": "Shared（跨領域共用）",
    "engineer": "Engineer（工程）",
    "finance": "Finance（金融投資）",
    "career": "Career（留學與職涯）",
    "meta": "Meta（技能開發與治理）",
}


def main() -> None:
    rows_by_domain: dict[str, list[tuple[str, str, str, str]]] = {}
    total = 0
    for domain_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        for skill_dir in sorted(p for p in domain_dir.iterdir() if p.is_dir()):
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"), str(skill_dir))
            desc = fm.get("description", "").replace("|", "\\|").strip()
            if len(desc) > 180:
                desc = desc[:177] + "..."
            rel = skill_md.relative_to(ROOT).as_posix()
            version = fm.get("version", "—")
            rows_by_domain.setdefault(domain_dir.name, []).append(
                (fm.get("name", skill_dir.name), rel, desc, version)
            )
            total += 1

    out = [
        "# Skill Index",
        "",
        "> **此檔案由 `tools/generate_skill_index.py` 自動生成**，",
        "> 請勿手動編輯；修改 skill frontmatter 後重新執行腳本（CI 會驗證同步）。",
        "",
        f"共 **{total}** 個 skill。",
        "",
    ]
    order = ["shared", "meta", "engineer", "finance", "career"]
    for domain in order + [d for d in rows_by_domain if d not in order]:
        if domain not in rows_by_domain:
            continue
        rows = rows_by_domain[domain]
        out.append(f"## {DOMAIN_TITLES.get(domain, domain)}（{len(rows)}）")
        out.append("")
        out.append("| Skill | Version | Description |")
        out.append("|---|---|---|")
        for name, rel, desc, version in rows:
            out.append(f"| [`{name}`]({rel}) | {version} | {desc} |")
        out.append("")

    (ROOT / "SKILL_INDEX.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"SKILL_INDEX.md regenerated: {total} skills")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    main()
