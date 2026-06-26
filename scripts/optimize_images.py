#!/usr/bin/env python3
"""
Optimize Nexara website images.

- Photos used in the embed (and other large PNGs) are resized to a sensible
  max dimension (2x their on-screen display size) and re-encoded.
- Photos WITHOUT transparency  -> JPEG (quality 82, progressive)  [much smaller]
- Images WITH transparency      -> WebP (quality 82) preserving alpha
- Originals are backed up to images/_originals/ before being replaced.

Run with --report to only print current sizes/dims and exit.
"""
import os
import sys
import glob
import shutil
from PIL import Image

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "images")
BACKUP_DIR = os.path.join(IMG_DIR, "_originals")

# Max longest-edge (px) per file. Tuned to ~2x the largest on-screen render.
# Default for anything not listed:
DEFAULT_MAX = 1400
MAX_EDGE = {
    # embed photos
    "on-site-power-generators.png": 1400,   # HOW photo (~395w) + WHAT card
    "power-houses.png": 1400,                # Lifecycle photo (~520w) + WHAT card
    "microgrids-and-hybrid-solutions.png": 1000,  # WHAT card only (~300w)
    "custom-electrical-solutions.png": 1000,      # WHAT card only
    "Battery Energy Storage Systems.png": 1400,   # unused but kept
    # hero layers (Phase 2) — keep larger + alpha
    "middle.png": 1600,
    "top-right.png": 1600,
    "top-left.png": 1600,
    "bottom.png": 1600,
}

JPEG_QUALITY = 82
WEBP_QUALITY = 82


def has_alpha(im):
    if im.mode in ("RGBA", "LA", "PA"):
        # Check if alpha channel actually varies (not fully opaque)
        alpha = im.getchannel("A")
        lo, hi = alpha.getextrema()
        return lo < 255
    return "transparency" in im.info


def human(n):
    for unit in ("B", "KB", "MB"):
        if n < 1024:
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} GB"


def report():
    rows = []
    for f in sorted(glob.glob(os.path.join(IMG_DIR, "*.png"))):
        im = Image.open(f)
        rows.append((os.path.getsize(f), im.size, im.mode, os.path.basename(f)))
    rows.sort(reverse=True)
    for size, dims, mode, name in rows:
        print(f"{human(size):>9}  {dims[0]}x{dims[1]}  {mode:<5}  {name}")


def optimize():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    total_before = 0
    total_after = 0
    results = []

    for path in sorted(glob.glob(os.path.join(IMG_DIR, "*.png"))):
        name = os.path.basename(path)
        before = os.path.getsize(path)
        total_before += before

        im = Image.open(path)
        orig_dims = im.size

        # Resize (downscale only) to max edge
        max_edge = MAX_EDGE.get(name, DEFAULT_MAX)
        scale = min(1.0, max_edge / max(im.size))
        if scale < 1.0:
            new_size = (round(im.size[0] * scale), round(im.size[1] * scale))
            im = im.resize(new_size, Image.LANCZOS)

        alpha = has_alpha(im)

        # Back up original
        shutil.copy2(path, os.path.join(BACKUP_DIR, name))

        if alpha:
            # Keep transparency -> WebP, replace .png with .webp
            out_name = os.path.splitext(name)[0] + ".webp"
            out_path = os.path.join(IMG_DIR, out_name)
            if im.mode != "RGBA":
                im = im.convert("RGBA")
            im.save(out_path, "WEBP", quality=WEBP_QUALITY, method=6)
            os.remove(path)  # remove the old .png
            kind = "webp(alpha)"
        else:
            # Opaque photo -> JPEG, replace .png with .jpg
            out_name = os.path.splitext(name)[0] + ".jpg"
            out_path = os.path.join(IMG_DIR, out_name)
            if im.mode != "RGB":
                im = im.convert("RGB")
            im.save(out_path, "JPEG", quality=JPEG_QUALITY,
                    optimize=True, progressive=True)
            os.remove(path)
            kind = "jpeg"

        after = os.path.getsize(out_path)
        total_after += after
        pct = (1 - after / before) * 100
        results.append((name, out_name, orig_dims, im.size, before, after, pct, kind))

    # Print table
    print(f"{'ORIGINAL':<38}{'OUTPUT':<38}{'DIMS':<14}{'BEFORE':>9}{'AFTER':>9}{'SAVED':>7}")
    print("-" * 115)
    for name, out, od, nd, b, a, pct, kind in results:
        dims = f"{nd[0]}x{nd[1]}"
        print(f"{name:<38}{out:<38}{dims:<14}{human(b):>9}{human(a):>9}{pct:>6.0f}%")
    print("-" * 115)
    tot_pct = (1 - total_after / total_before) * 100
    print(f"{'TOTAL':<90}{human(total_before):>9}{human(total_after):>9}{tot_pct:>6.0f}%")

    # Emit a rename map for updating the embed
    print("\nRENAME MAP (old -> new):")
    for name, out, *_ in results:
        if name != out:
            print(f"  {name} -> {out}")


if __name__ == "__main__":
    if "--report" in sys.argv:
        report()
    else:
        optimize()
