#!/usr/bin/env python3
"""
AETHER BRAND ASSET CONSOLIDATOR
================================
Consolidates all brand images and assets into one unified format (WebP).
Removes duplicates, creates manifest for Claude integration.

Usage:
    python consolidate_assets.py

Output:
    - /assets/brand/       - Brand UI mockups
    - /assets/portfolio/   - Portfolio/work images
    - /assets/vectors/     - SVG vector assets
    - /assets/animated/    - GIF/animated assets
    - brand_manifest.json  - Complete asset manifest for Claude queries
"""

import os
import json
import hashlib
import shutil
from pathlib import Path
from datetime import datetime

# Try to import PIL for image conversion
try:
    from PIL import Image
    HAS_PIL = True
    # Register HEIC support
    try:
        from pillow_heif import register_heif_opener
        register_heif_opener()
        HAS_HEIF = True
    except ImportError:
        HAS_HEIF = False
except ImportError:
    HAS_PIL = False
    HAS_HEIF = False
    print("Note: Install Pillow for WebP conversion: pip install Pillow pillow-heif")

# Configuration
ROOT_DIR = Path("/home/user/MASTERCODEX")
ASSETS_DIR = ROOT_DIR / "assets"
MANIFEST_FILE = ROOT_DIR / "brand_manifest.json"

# Asset categories
CATEGORIES = {
    "brand": ["AETHERKEMETICUI", "AETHERUI", "BLISS", "UIORB"],
    "portfolio": ["IMG_"],
    "vectors": [".svg"],
    "animated": [".gif"]
}

# Image formats to convert
CONVERTIBLE = {".jpg", ".jpeg", ".png", ".heic", ".webp", ".HEIC", ".JPEG", ".JPG", ".PNG"}
KEEP_AS_IS = {".svg", ".gif", ".SVG", ".GIF"}  # Don't convert these

# Brand color palette (from HTML analysis)
BRAND_COLORS = {
    "primary": {
        "gold": "#D4AF37",
        "gold_light": "#CFB53B",
        "platinum": "#E5E4E2",
        "platinum_pure": "#F4F4F4"
    },
    "gems": {
        "sapphire": "#0F52BA",
        "sapphire_light": "#4169E1",
        "emerald": "#2E8B57",
        "emerald_light": "#3CB371",
        "amethyst": "#9966CC",
        "turquoise": "#40E0D0"
    },
    "kemetic": {
        "lapis_dark": "#1E3A5F",
        "lapis_light": "#2E5A8F",
        "obsidian": "#0f0f1a",
        "obsidian_deep": "#1a1a2e"
    },
    "retro": {
        "terminal_green": "#33FF33",
        "amber": "#FFB000",
        "crt_blue": "#00BFFF",
        "win95_gray": "#c0c0c0"
    },
    "glass": {
        "chrome_sky": "rgba(255, 255, 255, 0.1)",
        "iridescent": "linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05))"
    }
}

# Font stack
BRAND_FONTS = {
    "primary": {
        "family": "Inter",
        "weights": [400, 500, 600, 700],
        "url": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700"
    },
    "display": {
        "family": "Space Grotesk",
        "weights": [400, 500, 600, 700],
        "url": "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700"
    },
    "mono": {
        "family": "JetBrains Mono",
        "weights": [400, 500],
        "url": "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500"
    }
}


def get_file_hash(filepath):
    """Get MD5 hash of file for duplicate detection."""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


def categorize_file(filename):
    """Determine category based on filename."""
    name_upper = filename.upper()
    ext = Path(filename).suffix.lower()

    if ext == ".svg":
        return "vectors"
    if ext == ".gif":
        return "animated"

    for cat, patterns in CATEGORIES.items():
        for pattern in patterns:
            if pattern.upper() in name_upper or pattern.lower() == ext:
                return cat

    return "portfolio"  # Default


def convert_to_webp(src_path, dst_path, quality=85):
    """Convert image to WebP format."""
    if not HAS_PIL:
        # Just copy if PIL not available
        shutil.copy2(src_path, dst_path.with_suffix(src_path.suffix))
        return dst_path.with_suffix(src_path.suffix)

    try:
        with Image.open(src_path) as img:
            # Convert to RGB if necessary (for RGBA/P modes)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGBA')
            elif img.mode != 'RGB':
                img = img.convert('RGB')

            webp_path = dst_path.with_suffix('.webp')
            img.save(webp_path, 'WebP', quality=quality, optimize=True)
            return webp_path
    except Exception as e:
        print(f"  Warning: Could not convert {src_path.name}: {e}")
        # Copy original as fallback
        shutil.copy2(src_path, dst_path.with_suffix(src_path.suffix))
        return dst_path.with_suffix(src_path.suffix)


def process_assets():
    """Main processing function."""
    print("\n" + "="*60)
    print("AETHER BRAND ASSET CONSOLIDATOR")
    print("="*60 + "\n")

    # Create directory structure
    for category in ["brand", "portfolio", "vectors", "animated"]:
        (ASSETS_DIR / category).mkdir(parents=True, exist_ok=True)

    # Find all image files
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".heic"}
    all_files = []

    for ext in image_extensions:
        all_files.extend(ROOT_DIR.glob(f"*{ext}"))
        all_files.extend(ROOT_DIR.glob(f"*{ext.upper()}"))

    # Remove duplicates from list
    all_files = list(set(all_files))

    print(f"Found {len(all_files)} image files\n")

    # Track files by hash for duplicate detection
    hash_map = {}
    duplicates = []
    processed = []
    manifest_assets = []

    for filepath in sorted(all_files):
        if not filepath.is_file():
            continue

        file_hash = get_file_hash(filepath)
        category = categorize_file(filepath.name)

        # Check for duplicates
        if file_hash in hash_map:
            duplicates.append({
                "file": str(filepath),
                "duplicate_of": hash_map[file_hash]["original"],
                "hash": file_hash
            })
            print(f"  [DUPLICATE] {filepath.name}")
            continue

        # Process file
        ext = filepath.suffix.lower()
        clean_name = filepath.stem.replace(" ", "_").replace("(", "").replace(")", "")
        dest_dir = ASSETS_DIR / category
        dest_path = dest_dir / clean_name

        if ext in KEEP_AS_IS:
            # Copy SVG/GIF as-is
            final_path = dest_path.with_suffix(ext)
            shutil.copy2(filepath, final_path)
            print(f"  [COPIED] {filepath.name} -> {category}/")
        elif ext in CONVERTIBLE:
            # Convert to WebP
            final_path = convert_to_webp(filepath, dest_path)
            print(f"  [CONVERTED] {filepath.name} -> {final_path.name}")
        else:
            continue

        # Track for manifest
        hash_map[file_hash] = {"original": str(filepath), "processed": str(final_path)}

        asset_entry = {
            "id": clean_name,
            "original_name": filepath.name,
            "category": category,
            "path": str(final_path.relative_to(ROOT_DIR)),
            "format": final_path.suffix[1:],
            "size_bytes": final_path.stat().st_size if final_path.exists() else 0,
            "hash": file_hash
        }

        # Add dimensions for images
        if HAS_PIL and ext in CONVERTIBLE:
            try:
                with Image.open(filepath) as img:
                    asset_entry["width"] = img.width
                    asset_entry["height"] = img.height
            except:
                pass

        manifest_assets.append(asset_entry)
        processed.append(str(final_path))

    # Create comprehensive manifest
    manifest = {
        "name": "AETHER KEMETIC BRAND ASSETS",
        "version": "1.0.0",
        "created": datetime.now().isoformat(),
        "description": "Consolidated brand assets for MASTERCODEX - Glass Chrome Sky Iridescent aesthetic",
        "brand": {
            "name": "AETHER KEMETIC ALCHEMY",
            "tagline": "Digital Alchemy for the Modern Age",
            "aesthetic": ["glass-morphism", "chrome-sky", "iridescent", "kemetic", "sacred-geometry"],
            "colors": BRAND_COLORS,
            "fonts": BRAND_FONTS,
            "symbols": {
                "primary": "ankh",
                "unicode": "\u2625",
                "meaning": "Life, Immortality, Digital Eternity"
            }
        },
        "assets": manifest_assets,
        "categories": {
            "brand": [a for a in manifest_assets if a["category"] == "brand"],
            "portfolio": [a for a in manifest_assets if a["category"] == "portfolio"],
            "vectors": [a for a in manifest_assets if a["category"] == "vectors"],
            "animated": [a for a in manifest_assets if a["category"] == "animated"]
        },
        "statistics": {
            "total_assets": len(manifest_assets),
            "duplicates_removed": len(duplicates),
            "by_category": {
                cat: len([a for a in manifest_assets if a["category"] == cat])
                for cat in ["brand", "portfolio", "vectors", "animated"]
            }
        },
        "duplicates_log": duplicates,
        "integration": {
            "css_import": """
/* AETHER Brand Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* AETHER Brand CSS Variables */
:root {
    --aether-gold: #D4AF37;
    --aether-platinum: #E5E4E2;
    --aether-sapphire: #0F52BA;
    --aether-emerald: #2E8B57;
    --aether-amethyst: #9966CC;
    --aether-lapis: #1E3A5F;
    --aether-obsidian: #0f0f1a;
    --aether-terminal: #33FF33;
    --aether-font-primary: 'Inter', sans-serif;
    --aether-font-display: 'Space Grotesk', sans-serif;
    --aether-font-mono: 'JetBrains Mono', monospace;
}
""",
            "html_component": """
<!-- AETHER Asset Container Component -->
<div class="aether-asset-container" data-category="{category}">
    <img src="assets/{category}/{filename}"
         alt="{id}"
         class="aether-asset"
         loading="lazy"
         decoding="async">
</div>
""",
            "react_component": """
// AETHER Asset Component
import React from 'react';
import manifest from './brand_manifest.json';

export const AetherAsset = ({ id, category = 'brand', className = '' }) => {
  const asset = manifest.assets.find(a => a.id === id);
  if (!asset) return null;

  return (
    <img
      src={`/${asset.path}`}
      alt={asset.id}
      width={asset.width}
      height={asset.height}
      className={`aether-asset ${className}`}
      loading="lazy"
    />
  );
};

// Usage: <AetherAsset id="AETHERKEMETICUI" category="brand" />
""",
            "claude_query_examples": [
                "Query: 'Get all brand assets' -> manifest.categories.brand",
                "Query: 'Find asset by name' -> manifest.assets.find(a => a.id.includes('name'))",
                "Query: 'Get brand colors' -> manifest.brand.colors",
                "Query: 'Get font stack' -> manifest.brand.fonts",
                "Query: 'Portfolio images' -> manifest.categories.portfolio"
            ]
        }
    }

    # Write manifest
    with open(MANIFEST_FILE, 'w') as f:
        json.dump(manifest, f, indent=2)

    print("\n" + "="*60)
    print("CONSOLIDATION COMPLETE")
    print("="*60)
    print(f"\n  Total assets processed: {len(manifest_assets)}")
    print(f"  Duplicates removed: {len(duplicates)}")
    print(f"  Manifest created: brand_manifest.json")
    print(f"\n  Asset directories:")
    print(f"    assets/brand/     - {manifest['statistics']['by_category']['brand']} files")
    print(f"    assets/portfolio/ - {manifest['statistics']['by_category']['portfolio']} files")
    print(f"    assets/vectors/   - {manifest['statistics']['by_category']['vectors']} files")
    print(f"    assets/animated/  - {manifest['statistics']['by_category']['animated']} files")

    if duplicates:
        print(f"\n  Duplicates found (not copied):")
        for dup in duplicates:
            print(f"    - {Path(dup['file']).name}")

    print("\n" + "="*60)
    print("HOW TO USE WITH CLAUDE")
    print("="*60)
    print("""
  1. Add to git:
     git add assets/ brand_manifest.json
     git commit -m "Consolidate brand assets"
     git push

  2. Query Claude:
     "Read brand_manifest.json and integrate the AETHER brand assets"
     "Use the brand colors from the manifest for the component"
     "Show me all portfolio images from the manifest"

  3. Import in code:
     import manifest from './brand_manifest.json';
     const colors = manifest.brand.colors;
     const assets = manifest.assets;
""")

    return manifest


if __name__ == "__main__":
    manifest = process_assets()
