#!/usr/bin/env python3
"""Check that Article Visual Grammar keeps its image quality harness wired in."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "references/image-quality-harness.md",
    "references/composition-stability-presets.md",
    "references/action-character-system.md",
    "references/prompt-builder.md",
    "references/qa-checklist.md",
    "references/figure-spec-schema.md",
    "references/aesthetic-quality-bar.md",
]

REQUIRED_TERMS = {
    "SKILL.md": [
        "image-quality-harness.md",
        "composition-stability-presets.md",
        "action-character-system.md",
        "default-generation smoke",
        "world-class",
    ],
    "references/prompt-builder.md": [
        "Image quality harness",
        "Composition stability preset",
        "Action character system",
        "anti-default-AI",
        "material family",
    ],
    "references/qa-checklist.md": [
        "default-generation smoke",
        "generic AI output",
        "beauty score",
        "composition stability preset",
        "Paper Operator",
    ],
    "references/figure-spec-schema.md": [
        "image_quality",
        "composition_stability",
        "action_character",
        "material_family",
        "anti_default_ai",
    ],
    "references/image-quality-harness.md": [
        "composition stability preset",
        "Hero Object With State Marks",
        "Carrier Through Gate",
    ],
    "references/composition-stability-presets.md": [
        "One image = one preset",
        "First-Glance Test",
        "Stability Prompt Add-On",
    ],
    "references/action-character-system.md": [
        "Paper Operators",
        "Thread Runner",
        "Lens Keeper",
        "Gate Builder",
        "what breaks if removed",
    ],
}


def main() -> int:
    failures: list[str] = []

    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.exists():
            failures.append(f"missing required file: {relative}")
            continue
        if path.stat().st_size == 0:
            failures.append(f"empty required file: {relative}")

    for relative, terms in REQUIRED_TERMS.items():
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                failures.append(f"{relative} does not mention {term!r}")

    if failures:
        print("quality harness check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("quality harness check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
