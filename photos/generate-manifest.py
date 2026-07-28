#!/usr/bin/env python3
"""Regenerate photos/manifest.json from the images in this folder.

Usage (from the repo root or the photos/ folder):

    python3 photos/generate-manifest.py

Drop image files into the photos/ folder, run this script, then commit and
push. The gallery at /photos.html reads manifest.json to know what to show.
"""

import json
import os
import re

EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif"}
EXCLUDED = {
    "ferrari-412-2.jpeg",
    "ferrari-412-4.jpeg",
}

here = os.path.dirname(os.path.abspath(__file__))


def natural_key(name):
    return [
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", name)
    ]


photos = sorted(
    (
        name
        for name in os.listdir(here)
        if os.path.splitext(name)[1].lower() in EXTS
        and name.lower() not in EXCLUDED
    ),
    key=natural_key,
)

out = os.path.join(here, "manifest.json")
with open(out, "w") as f:
    json.dump(photos, f, indent=2)
    f.write("\n")

print(f"Wrote {len(photos)} photo(s) to {os.path.relpath(out)}")
for p in photos:
    print(f"  - {p}")
