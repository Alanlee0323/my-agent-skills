#!/usr/bin/env python3
"""Skill library consistency validator (stdlib only, no dependencies).

Enforces the invariants documented in skills/meta/maintaining-skill-library/SKILL.md:
  1.  Every skill folder has an uppercase SKILL.md with parseable frontmatter.
  2.  frontmatter `name` is lowercase-hyphen, <=64 chars, no agent brand names.
  3.  `name` == folder name (the identifier invariant).
  4.  Names are unique across the library.
  5.  Gerund-form naming (warning; exceptions listed below).
  6.  description present, <=1024 chars; body <=500 lines.
  7.  Every skill referenced by bundles/*.yaml exists.
  8.  Every hyphenated code-span token in global-rules.md resolves to a skill.
  9.  File paths referenced inside a SKILL.md exist (supports trailing globs).
  10. Local markdown links in readme.md resolve.
  11. Every skill is in >=1 bundle (warning; meta skills exempt).

Exit code: 0 = clean (warnings allowed), 1 = errors found.
Usage: python tools/validate_skills.py [--strict]   (--strict: warnings also fail)
"""

from __future__ import annotations

import glob as globmod
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
BUNDLES_DIR = ROOT / "bundles"

BRAND_NAMES = {"claude", "gemini", "copilot", "codex", "anthropic", "openai"}
GERUND_EXCEPTIONS = {"sdd-driven-development"}  # documented naming exceptions
BUNDLE_EXEMPT_DOMAINS = {"meta"}  # meta skills are invoked on demand, not bundled
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
# candidate skill tokens inside code spans: lowercase, at least one hyphen
ROUTE_TOKEN_RE = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`")
# path-like references inside skill bodies
PATH_REF_RE = re.compile(
    r"(?:^|[\s`(\[])((?:references|resources|examples|scripts|tone-example|agents)"
    r"/[A-Za-z0-9_.\-/*]+)"
)

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def parse_frontmatter(text: str, where: str) -> dict[str, str]:
    """Minimal YAML frontmatter parser: scalar keys + `|` block scalars only."""
    if not text.startswith("---"):
        err(f"{where}: missing YAML frontmatter (must start with ---)")
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        err(f"{where}: unterminated frontmatter")
        return {}
    fm: dict[str, str] = {}
    lines = text[3:end].splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val == "|":  # block scalar: consume indented continuation lines
                block: list[str] = []
                i += 1
                while i < len(lines) and (lines[i].startswith(("  ", "\t")) or not lines[i].strip()):
                    block.append(lines[i].strip())
                    i += 1
                fm[key] = " ".join(b for b in block if b)
                continue
            fm[key] = val
        i += 1
    return fm


def discover_skills() -> dict[str, Path]:
    """Return {skill_name: skill_dir} while validating structure."""
    names: dict[str, Path] = {}
    for domain_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        for skill_dir in sorted(p for p in domain_dir.iterdir() if p.is_dir()):
            rel = skill_dir.relative_to(ROOT).as_posix()
            # exact-case check (Windows fs is case-insensitive; compare listing)
            actual = {f.name for f in skill_dir.iterdir() if f.is_file()}
            if "SKILL.md" not in actual:
                lower = [n for n in actual if n.lower() == "skill.md"]
                if lower:
                    err(f"{rel}: file is named '{lower[0]}' — must be exactly 'SKILL.md'")
                else:
                    err(f"{rel}: missing SKILL.md")
                continue
            skill_md = skill_dir / "SKILL.md"
            text = skill_md.read_text(encoding="utf-8")
            fm = parse_frontmatter(text, rel)
            name = fm.get("name", "")
            desc = fm.get("description", "")
            if not name:
                err(f"{rel}: frontmatter missing `name`")
                continue
            if not NAME_RE.match(name):
                err(f"{rel}: name '{name}' violates ^[a-z0-9][a-z0-9-]{{0,63}}$")
            for token in name.split("-"):
                if token in BRAND_NAMES:
                    err(f"{rel}: name '{name}' contains agent brand '{token}'")
            if name != skill_dir.name:
                err(f"{rel}: name '{name}' != folder name '{skill_dir.name}' "
                    f"(identifier invariant: name == folder == routing token)")
            if name in names:
                err(f"{rel}: duplicate name '{name}' (also in "
                    f"{names[name].relative_to(ROOT).as_posix()})")
            names[name] = skill_dir
            if name not in GERUND_EXCEPTIONS:
                if not any(t.endswith("ing") for t in name.split("-")[:2]):
                    warn(f"{rel}: name '{name}' is not gerund-form "
                         f"(add to GERUND_EXCEPTIONS if intentional)")
            if not desc:
                err(f"{rel}: frontmatter missing `description`")
            elif len(desc) > 1024:
                err(f"{rel}: description is {len(desc)} chars (max 1024)")
            n_lines = text.count("\n") + 1
            if n_lines > 500:
                err(f"{rel}: SKILL.md is {n_lines} lines (max 500 — use progressive "
                    f"disclosure into references/)")
            check_path_refs(skill_dir, text, rel)
    return names


def check_path_refs(skill_dir: Path, text: str, rel: str) -> None:
    for m in PATH_REF_RE.finditer(text):
        ref = m.group(1).rstrip(".,)")
        if "*" in ref:
            base = ref.split("*")[0].rstrip("/")
            target = skill_dir / base
            if not target.exists():
                err(f"{rel}: references '{ref}' but '{base}/' does not exist")
            elif not globmod.glob(str(skill_dir / ref)):
                warn(f"{rel}: glob '{ref}' matches no files (corpus TODO?)")
        else:
            if not (skill_dir / ref).exists():
                err(f"{rel}: references '{ref}' which does not exist")


def parse_bundle(path: Path) -> tuple[str, list[str]]:
    """Minimal parser: extracts `name:` and the `skills:` list items."""
    name, skills, in_skills = path.stem, [], False
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("#") or not stripped:
            continue
        if re.match(r"^name:\s*", line):
            name = stripped.split(":", 1)[1].strip()
        if re.match(r"^skills:\s*$", line):
            in_skills = True
            continue
        if in_skills:
            m = re.match(r"^\s+-\s+(\S+)", line)
            if m:
                skills.append(m.group(1))
            elif not line.startswith((" ", "\t")):
                in_skills = False
    return name, skills


def check_bundles(known: dict[str, Path]) -> dict[str, list[str]]:
    bundles: dict[str, list[str]] = {}
    for bundle_path in sorted(BUNDLES_DIR.glob("*.yaml")):
        bname, bskills = parse_bundle(bundle_path)
        bundles[bname] = bskills
        rel = bundle_path.relative_to(ROOT).as_posix()
        seen: set[str] = set()
        for s in bskills:
            if s not in known:
                err(f"{rel}: references unknown skill '{s}'")
            if s in seen:
                err(f"{rel}: duplicate entry '{s}'")
            seen.add(s)
    return bundles


def check_global_rules(known: dict[str, Path]) -> None:
    gr = ROOT / "global-rules.md"
    if not gr.exists():
        warn("global-rules.md not found")
        return
    for i, line in enumerate(gr.read_text(encoding="utf-8").splitlines(), 1):
        for token in ROUTE_TOKEN_RE.findall(line):
            if token not in known:
                err(f"global-rules.md:{i}: routes to '{token}' but no skill has that name")


def check_readme_links() -> None:
    readme = ROOT / "readme.md"
    if not readme.exists():
        return
    link_re = re.compile(r"\]\(([^)#]+?)(?:#[^)]*)?\)")
    for i, line in enumerate(readme.read_text(encoding="utf-8").splitlines(), 1):
        for target in link_re.findall(line):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (ROOT / target).exists():
                err(f"readme.md:{i}: broken link '{target}'")


def check_bundle_coverage(known: dict[str, Path], bundles: dict[str, list[str]]) -> None:
    bundled = {s for skills in bundles.values() for s in skills}
    for name, skill_dir in sorted(known.items()):
        domain = skill_dir.parent.name
        if name not in bundled and domain not in BUNDLE_EXEMPT_DOMAINS:
            warn(f"{skill_dir.relative_to(ROOT).as_posix()}: '{name}' is in no bundle "
                 f"(intentional? note it in the skill's Evolution Log)")


def main() -> int:
    strict = "--strict" in sys.argv
    known = discover_skills()
    bundles = check_bundles(known)
    check_global_rules(known)
    check_readme_links()
    check_bundle_coverage(known, bundles)

    print(f"skills discovered: {len(known)} | bundles: {len(bundles)}")
    for w in warnings:
        print(f"[WARN] {w}")
    for e in errors:
        print(f"[FAIL] {e}")
    if errors or (strict and warnings):
        print(f"\nRESULT: FAIL ({len(errors)} errors, {len(warnings)} warnings)")
        return 1
    print(f"\nRESULT: OK ({len(warnings)} warnings)")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    sys.exit(main())
