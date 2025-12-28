# AETHER Brand Integration Guide for Claude

Use this file to easily integrate AETHER brand assets into any project with Claude's help.

## Quick Start

Copy and paste this prompt to Claude when you need to integrate brand assets:

---

### Integration Prompt

```
I'm working with the AETHER brand assets from MASTERCODEX. Here's my brand manifest:

Brand: AETHER Kemetic Alchemy UI
Primary Color: #667eea
Dark Color: #102b8e
Teal Accent: #008080

Available themes: Ethereal Chrome, Alchemist, SkyMatrix, Iridescent Glass

Asset categories:
- brand-ui/ - 6 JPG files (UI mockups)
- ethereal/ - 2 JPG files (orb designs)
- photography/ - 9 JPEG + 1 WEBP files
- screenshots/ - 2 PNG files
- svg-components/ - 4 SVG files (web popups)
- animations/ - 1 GIF (AlchemistInstaStory1.gif)

Latest HTML: MASTERSITEAETHERPXRKEMETIC333_v36_BRAND_FIXED.html

Please help me [YOUR REQUEST HERE]
```

---

## Color Variables (CSS)

```css
:root {
  /* Primary Brand Colors */
  --aether-primary: #667eea;
  --aether-dark: #102b8e;
  --aether-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

  /* Accent Colors */
  --aether-teal: #008080;
  --aether-blue-secondary: #4a90e2;
  --aether-gray: #5a6c7d;
  --aether-text-dark: #2c3e50;

  /* Status Colors */
  --aether-success: #00ff00;
  --aether-error: #ff0000;
  --aether-warning: #ffff00;
  --aether-info: #00ffff;

  /* UI Colors */
  --aether-bg: #c0c0c0;
  --aether-white: #ffffff;
  --aether-black: #000000;
}
```

---

## Asset Reference Table

| Asset ID | File | Category | Purpose |
|----------|------|----------|---------|
| `aether-ui-core` | AETHERUI.jpg | brand-ui | Core UI element |
| `aether-kemetic-ui` | AETHERKEMETICUI.jpg | brand-ui | Main brand mockup |
| `aether-kemetic-ui-333` | AETHERKEMETICUI333.jpg | brand-ui | Variant UI |
| `aether-kemetic-ui-byte` | AETHERKEMETICUIBYTE111.jpg | brand-ui | Tech UI |
| `aether-kemetic-ui-enter` | AETHERKEMETICUIEINTER.jpg | brand-ui | Enhanced UI |
| `aether-kemetic-ui-wavy` | AETHERKEMETICUIWAYVY.jpg | brand-ui | Wavy design |
| `bliss-ethereal` | BLISSETHEREAL.jpg | ethereal | Ethereal branding |
| `ui-orb-ethereal` | UIORBETHEREAL.jpg | ethereal | Orb element |
| `alchemist-story` | AlchemistInstaStory1.gif | animations | Social media |
| `web-popup-6` | WebAssetPortsoftwarepopup6.svg | svg | Web component |
| `web-popup-7` | WebAssetPortsoftwarepopup7.svg | svg | Web component |
| `web-popup-8` | WebAssetPortsoftwarepopup8.svg | svg | Web component |
| `web-popup-9` | WebAssetPortsoftwarepopup9.svg | svg | Web component |

---

## Common Integration Requests

### 1. Add AETHER branding to a website

```
Using the AETHER brand manifest, add brand colors and styling to my website.
Use the primary color #667eea and create a header with the gradient.
```

### 2. Create a React component with brand assets

```
Create a React component that displays the AETHER brand UI images from
the brand-ui folder. Use the brand color palette for styling.
```

### 3. Generate branded social media assets

```
I need social media assets matching the AETHER brand. Reference the
AlchemistInstaStory1.gif style and use the Ethereal Chrome theme colors.
```

### 4. Add brand colors to an existing project

```
Add the AETHER CSS variables to my project's stylesheet. Include all
primary, accent, and status colors from the brand palette.
```

### 5. Create a branded loading animation

```
Create a CSS loading animation using AETHER brand colors (#667eea, #764ba2)
with an ethereal, alchemist-inspired design.
```

---

## File Paths

```
MASTERCODEX/
├── brand-assets.json          # Full manifest (query this for details)
├── CLAUDE_BRAND_INTEGRATION.md # This file
├── consolidate-assets.sh      # Run to organize assets
├── assets/                    # Organized assets (after running script)
│   ├── brand-ui/             # UI mockups
│   ├── ethereal/             # Ethereal designs
│   ├── photography/          # Photos
│   ├── screenshots/          # PNGs
│   ├── svg-components/       # SVGs
│   └── animations/           # GIFs
├── *.jpg, *.JPEG, *.PNG...   # Original files (root)
└── *.html                    # HTML versions
```

---

## JSON Query Examples

To get specific asset info, ask Claude:

```
From brand-assets.json, get all assets in the "brandUI" category
```

```
What are the AETHER primary brand colors from brand-assets.json?
```

```
List all SVG components with their file sizes from brand-assets.json
```

---

## Git Commands

```bash
# Add all brand files
git add brand-assets.json CLAUDE_BRAND_INTEGRATION.md consolidate-assets.sh

# Run consolidation first
chmod +x consolidate-assets.sh
./consolidate-assets.sh

# Then add organized assets
git add assets/

# Commit
git commit -m "Add consolidated AETHER brand assets"

# Push
git push
```
