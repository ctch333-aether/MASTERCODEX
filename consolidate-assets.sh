#!/bin/bash
# AETHER Brand Assets Consolidation Script
# Organizes, converts, and deduplicates brand assets

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSETS_DIR="$SCRIPT_DIR/assets"

echo "=== AETHER Brand Assets Consolidation ==="
echo "Working directory: $SCRIPT_DIR"
echo ""

# Create organized directory structure
create_directories() {
    echo "[1/5] Creating organized directory structure..."
    mkdir -p "$ASSETS_DIR/brand-ui"
    mkdir -p "$ASSETS_DIR/photography"
    mkdir -p "$ASSETS_DIR/ios-originals"
    mkdir -p "$ASSETS_DIR/screenshots"
    mkdir -p "$ASSETS_DIR/svg-components"
    mkdir -p "$ASSETS_DIR/animations"
    mkdir -p "$ASSETS_DIR/ethereal"
    echo "  Created: assets/brand-ui, photography, ios-originals, screenshots, svg-components, animations, ethereal"
}

# Remove duplicates
remove_duplicates() {
    echo ""
    echo "[2/5] Removing duplicate files..."
    if [ -f "$SCRIPT_DIR/IMG_7187 (2).JPEG" ]; then
        rm "$SCRIPT_DIR/IMG_7187 (2).JPEG"
        echo "  Removed: IMG_7187 (2).JPEG (duplicate of IMG_7187 (1).JPEG)"
    else
        echo "  No duplicates found (already cleaned)"
    fi
}

# Organize files into directories
organize_files() {
    echo ""
    echo "[3/5] Organizing files into directories..."

    # Brand UI images
    for f in AETHERUI.jpg AETHERKEMETICUI.jpg AETHERKEMETICUI333.jpg AETHERKEMETICUIBYTE111.jpg AETHERKEMETICUIEINTER.jpg AETHERKEMETICUIWAYVY.jpg; do
        [ -f "$SCRIPT_DIR/$f" ] && cp "$SCRIPT_DIR/$f" "$ASSETS_DIR/brand-ui/" && echo "  Copied: $f -> assets/brand-ui/"
    done

    # Ethereal images
    for f in BLISSETHEREAL.jpg UIORBETHEREAL.jpg; do
        [ -f "$SCRIPT_DIR/$f" ] && cp "$SCRIPT_DIR/$f" "$ASSETS_DIR/ethereal/" && echo "  Copied: $f -> assets/ethereal/"
    done

    # Animations
    [ -f "$SCRIPT_DIR/AlchemistInstaStory1.gif" ] && cp "$SCRIPT_DIR/AlchemistInstaStory1.gif" "$ASSETS_DIR/animations/" && echo "  Copied: AlchemistInstaStory1.gif -> assets/animations/"

    # Photography (JPEG files)
    for f in "$SCRIPT_DIR"/IMG_*.JPEG "$SCRIPT_DIR"/production-photo-*.webp; do
        [ -f "$f" ] && cp "$f" "$ASSETS_DIR/photography/" && echo "  Copied: $(basename "$f") -> assets/photography/"
    done

    # iOS originals (HEIC)
    for f in "$SCRIPT_DIR"/IMG_*.HEIC; do
        [ -f "$f" ] && cp "$f" "$ASSETS_DIR/ios-originals/" && echo "  Copied: $(basename "$f") -> assets/ios-originals/"
    done

    # Screenshots (PNG)
    for f in "$SCRIPT_DIR"/IMG_*.PNG; do
        [ -f "$f" ] && cp "$f" "$ASSETS_DIR/screenshots/" && echo "  Copied: $(basename "$f") -> assets/screenshots/"
    done

    # SVG components
    for f in "$SCRIPT_DIR"/WebAssetPort*.svg; do
        [ -f "$f" ] && cp "$f" "$ASSETS_DIR/svg-components/" && echo "  Copied: $(basename "$f") -> assets/svg-components/"
    done
}

# Generate asset index
generate_index() {
    echo ""
    echo "[4/5] Generating asset index..."

    cat > "$ASSETS_DIR/index.json" << 'EOF'
{
  "generated": "$(date -Iseconds)",
  "structure": {
    "brand-ui": "Core AETHER brand UI mockups and designs",
    "ethereal": "Ethereal and orb-themed design elements",
    "animations": "GIF and animated assets for social media",
    "photography": "JPEG/WEBP photographs and imagery",
    "ios-originals": "Original HEIC files from iOS devices",
    "screenshots": "PNG screenshots and high-res mockups",
    "svg-components": "SVG web UI components and vectors"
  },
  "usage": "Import this index to navigate the organized asset structure"
}
EOF
    echo "  Generated: assets/index.json"
}

# Print summary
print_summary() {
    echo ""
    echo "[5/5] Consolidation complete!"
    echo ""
    echo "=== SUMMARY ==="
    echo "Brand UI:      $(ls -1 "$ASSETS_DIR/brand-ui" 2>/dev/null | wc -l) files"
    echo "Ethereal:      $(ls -1 "$ASSETS_DIR/ethereal" 2>/dev/null | wc -l) files"
    echo "Animations:    $(ls -1 "$ASSETS_DIR/animations" 2>/dev/null | wc -l) files"
    echo "Photography:   $(ls -1 "$ASSETS_DIR/photography" 2>/dev/null | wc -l) files"
    echo "iOS Originals: $(ls -1 "$ASSETS_DIR/ios-originals" 2>/dev/null | wc -l) files"
    echo "Screenshots:   $(ls -1 "$ASSETS_DIR/screenshots" 2>/dev/null | wc -l) files"
    echo "SVG Components:$(ls -1 "$ASSETS_DIR/svg-components" 2>/dev/null | wc -l) files"
    echo ""
    echo "Assets organized in: $ASSETS_DIR"
    echo "Manifest file: $SCRIPT_DIR/brand-assets.json"
    echo ""
    echo "To add to git:"
    echo "  git add assets/ brand-assets.json"
    echo "  git commit -m 'Consolidate brand assets'"
    echo "  git push"
}

# Run all steps
create_directories
remove_duplicates
organize_files
generate_index
print_summary
