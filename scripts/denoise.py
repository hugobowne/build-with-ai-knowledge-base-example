"""Apply ASR error corrections to cleaned transcripts.

Fixes known transcription errors: misspelled names, technical terms,
and speaker label capitalization.
"""

import re
from pathlib import Path

# Known ASR error corrections (case-sensitive where needed)
REPLACEMENTS = {
    # People names
    "Stefan Crouchik": "Stefan Krawczyk",
    "Carpathy": "Karpathy",
    # Technical terms
    "Robeita": "RoBERTa",
}

# Case-insensitive replacements (for names ASR gets phonetically wrong)
CI_REPLACEMENTS = {
    r"\bYugo\b": "Hugo",
    r"\bHugh\b": "Hugo",
    r"\bKathleen\b": "Katherine",
    r"\bVino\b": "Vinod",
    r"\bConrad\b": "Konrad",
}

# Speaker label normalization: lowercase → proper case
SPEAKER_NAMES = {
    "hugo bowne-anderson": "Hugo Bowne-Anderson",
    "brad w morris": "Brad W Morris",
}


def denoise(text: str) -> str:
    # Apply exact replacements
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)

    # Apply case-insensitive regex replacements
    for pattern, replacement in CI_REPLACEMENTS.items():
        text = re.sub(pattern, replacement, text)

    # Normalize speaker labels in **Speaker:** format
    for old_name, new_name in SPEAKER_NAMES.items():
        text = text.replace(f"**{old_name}:**", f"**{new_name}:**")

    return text


def main():
    raw_dir = Path(__file__).parent.parent / "raw"
    cleaned_dir = raw_dir / "_cleaned"

    # Process cleaned VTTs
    cleaned_files = sorted(cleaned_dir.glob("*.md"))
    # Process existing markdown transcripts
    md_files = sorted(raw_dir.glob("*.md"))

    all_files = cleaned_files + md_files
    total_fixes = 0

    for filepath in all_files:
        original = filepath.read_text()
        fixed = denoise(original)
        if fixed != original:
            filepath.write_text(fixed)
            # Count changes
            n_changes = sum(
                1 for a, b in zip(original.split(), fixed.split()) if a != b
            )
            print(f"Fixed {filepath.name} ({n_changes} words changed)")
            total_fixes += 1
        else:
            print(f"No changes: {filepath.name}")

    print(f"\nDone. Modified {total_fixes}/{len(all_files)} files.")


if __name__ == "__main__":
    main()
