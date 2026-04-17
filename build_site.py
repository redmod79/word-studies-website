#!/usr/bin/env python3
"""Build script for the Word & Grammar Studies website.

Copies word study .md files from bible-studies/word-studies/ and grammar
reference .md files from bible-studies/grammar-reference/ into docs/ and
generates the mkdocs.yml nav sections.
"""

import shutil
import re
from pathlib import Path

WORD_STUDIES_DIR = Path(__file__).parent.parent / "bible-studies" / "word-studies"
GRAMMAR_REF_DIR = Path(__file__).parent.parent / "bible-studies" / "grammar-reference"
DOCS_DIR = Path(__file__).parent / "docs"
MKDOCS_YML = Path(__file__).parent / "mkdocs.yml"

# Files to skip (not word studies)
SKIP_FILES = {"INDEX.md", "TODO.md"}


def parse_title(filepath: Path) -> str:
    """Extract the first H1 heading from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    return filepath.stem


def sort_key_strongs(filename: str) -> tuple:
    """Sort key for Strong's-numbered files (H1121, G3551, etc.)."""
    m = re.match(r"[HAG](\d+)", filename)
    if m:
        return (int(m.group(1)),)
    return (999999,)


def collect_files():
    """Collect and categorize word study files."""
    hebrew = []
    aramaic = []
    greek = []
    traces = []
    word_groups = []

    for f in sorted(WORD_STUDIES_DIR.glob("*.md")):
        if f.name in SKIP_FILES:
            continue
        if f.name.endswith(".METADATA.yaml"):
            continue

        name = f.stem
        title = parse_title(f)

        entry = {"file": f, "name": f.name, "title": title}

        if name.startswith("H") and re.match(r"H\d+", name):
            hebrew.append(entry)
        elif name.startswith("A") and re.match(r"A\d+", name):
            aramaic.append(entry)
        elif name.startswith("G") and re.match(r"G\d+", name):
            greek.append(entry)
        elif name.startswith("TR-"):
            traces.append(entry)
        elif name.startswith("WG-"):
            word_groups.append(entry)
        else:
            # Unknown prefix — skip
            print(f"  Skipping unknown file: {f.name}")

    # Sort
    hebrew.sort(key=lambda e: sort_key_strongs(e["name"]))
    aramaic.sort(key=lambda e: sort_key_strongs(e["name"]))
    greek.sort(key=lambda e: sort_key_strongs(e["name"]))
    traces.sort(key=lambda e: e["title"].lower())
    word_groups.sort(key=lambda e: e["title"].lower())

    return hebrew, aramaic, greek, traces, word_groups


def collect_grammar():
    """Collect grammar-reference files from hebrew/, greek/, passages/ subdirs.

    Files are copied flat into docs/ with a prefix to avoid name collisions
    with the word-study Strong's files.
    """
    subdirs = [
        ("hebrew", "grammar-hebrew-"),
        ("greek", "grammar-greek-"),
        ("passages", "grammar-passage-"),
    ]

    hebrew_g, greek_g, passages_g = [], [], []
    buckets = {"hebrew": hebrew_g, "greek": greek_g, "passages": passages_g}

    if not GRAMMAR_REF_DIR.exists():
        return hebrew_g, greek_g, passages_g

    for sub, prefix in subdirs:
        subpath = GRAMMAR_REF_DIR / sub
        if not subpath.exists():
            continue
        for f in sorted(subpath.glob("*.md")):
            if f.name in SKIP_FILES:
                continue
            if f.name.endswith(".METADATA.yaml"):
                continue
            title = parse_title(f)
            out_name = f"{prefix}{f.name}"
            buckets[sub].append({"file": f, "name": out_name, "title": title})

    for lst in (hebrew_g, greek_g, passages_g):
        lst.sort(key=lambda e: e["title"].lower())

    return hebrew_g, greek_g, passages_g


def copy_files(entries_lists):
    """Copy study files into docs/ using each entry's declared ``name``."""
    count = 0
    for entries in entries_lists:
        for entry in entries:
            src = entry["file"]
            dst = DOCS_DIR / entry["name"]
            shutil.copy2(src, dst)
            count += 1
    print(f"  Copied {count} study files to docs/")


def generate_nav_section(entries, indent=8):
    """Generate YAML nav lines for a list of entries."""
    lines = []
    prefix = " " * indent
    for entry in entries:
        title = entry["title"].replace('"', '\\"')
        lines.append(f'{prefix}- "{title}": {entry["name"]}')
    return "\n".join(lines) if lines else f'{prefix}- "(none)": index.md'


def generate_mkdocs_yml(hebrew, aramaic, greek, traces, word_groups,
                       gram_hebrew, gram_greek, gram_passages):
    """Generate the full mkdocs.yml with nav."""

    hebrew_nav = generate_nav_section(hebrew)
    aramaic_nav = generate_nav_section(aramaic)
    greek_nav = generate_nav_section(greek)
    traces_nav = generate_nav_section(traces)
    wg_nav = generate_nav_section(word_groups)
    gh_nav = generate_nav_section(gram_hebrew)
    gg_nav = generate_nav_section(gram_greek)
    gp_nav = generate_nav_section(gram_passages)

    yml = f'''site_name: "Biblical Word & Grammar Studies"
site_url: "https://redmod79.github.io/word-studies-website/"
site_description: "A comprehensive library of Hebrew, Aramaic, and Greek word studies plus canonical grammar reference entries and passage-level grammar analyses."

theme:
  name: material
  custom_dir: overrides
  palette:
    - scheme: default
      primary: teal
      accent: deep orange
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: teal
      accent: deep orange
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - navigation.indexes
    - search.suggest
    - search.highlight
    - content.tabs.link
    - toc.follow
  font:
    text: Roboto
    code: Roboto Mono

plugins:
  - search

markdown_extensions:
  - abbr
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - tables
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true

extra:
  social:
    - icon: fontawesome/solid/book-bible
      link: /

extra_css:
  - stylesheets/extra.css

nav:
  - Home: index.md

  - "Word Studies":
    - "Hebrew":
{hebrew_nav}

    - "Aramaic":
{aramaic_nav}

    - "Greek":
{greek_nav}

    - "Cross-Testament Traces":
{traces_nav}

    - "Word Groups":
{wg_nav}

  - "Grammar Reference":
    - "Hebrew Grammar":
{gh_nav}

    - "Greek Grammar":
{gg_nav}

    - "Passage Analyses":
{gp_nav}
'''

    with open(MKDOCS_YML, "w", encoding="utf-8") as f:
        f.write(yml)
    print(f"  Generated mkdocs.yml")


def main():
    print("Building Word & Grammar Studies website...")

    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    print("Collecting word study files...")
    hebrew, aramaic, greek, traces, word_groups = collect_files()
    print(f"  Hebrew: {len(hebrew)}, Aramaic: {len(aramaic)}, Greek: {len(greek)}")
    print(f"  Traces: {len(traces)}, Word Groups: {len(word_groups)}")

    print("Collecting grammar reference files...")
    gram_hebrew, gram_greek, gram_passages = collect_grammar()
    print(f"  Hebrew grammar: {len(gram_hebrew)}, Greek grammar: {len(gram_greek)}, Passages: {len(gram_passages)}")

    total_word = len(hebrew) + len(aramaic) + len(greek) + len(traces) + len(word_groups)
    total_gram = len(gram_hebrew) + len(gram_greek) + len(gram_passages)
    print(f"  Total: {total_word} word + {total_gram} grammar = {total_word + total_gram}")

    print("Copying files to docs/...")
    copy_files([hebrew, aramaic, greek, traces, word_groups,
                gram_hebrew, gram_greek, gram_passages])

    print("Generating mkdocs.yml...")
    generate_mkdocs_yml(hebrew, aramaic, greek, traces, word_groups,
                        gram_hebrew, gram_greek, gram_passages)

    print("Done!")


if __name__ == "__main__":
    main()
