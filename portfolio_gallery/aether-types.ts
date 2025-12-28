// AETHER Brand Assets - Auto-generated TypeScript Types
// Generated: 2025-12-28T21:58:10.716413

export type AssetCategory = "characters" | "concept-art" | "environments" | "experiences" | "founder-story" | "logos" | "misc" | "portfolio" | "production" | "set-design" | "ui-elements";

export interface BrandAsset {
  id: string;
  path: string;
  category: AssetCategory;
  originalName: string;
  format: 'webp' | 'svg';
  size: number;
  hash: string;
  width?: number;
  height?: number;
}

export interface AssetManifest {
  version: string;
  generated: string;
  description: string;
  total_assets: number;
  categories: Record<AssetCategory, number>;
  assets: BrandAsset[];
}

// Asset IDs for type-safe imports
export const ASSET_IDS = {
  RX_LOGO_META: "rx-logo-meta",
  SITE_COLLAGE14_1: "site-collage14-1",
  PROJECT51HINT_3: "project51hint-3",
  WEBASSETPORTSOFTWAREPOPUP7: "webassetportsoftwarepopup7",
  33_02936_2025PD: "33-02936-2025pd",
  WEBASSETPORTSOFTWAREPOPUP9: "webassetportsoftwarepopup9",
  COLLAGE1KMP1_1_1_1: "collage1kmp1-1-1-1",
  BELIEVE: "believe",
  SET_DESIGN_LAYOUT: "set-design-layout",
  ARTIFACTS_ROOM: "artifacts-room",
  WEBASSETPORTSOFTWAREPOPUP6: "webassetportsoftwarepopup6",
  MJ_CHARACTER: "mj-character",
  WEBASSETPORTSOFTWAREPOPUP8: "webassetportsoftwarepopup8",
  BAYOUBBQLOGO: "bayoubbqlogo",
  SITE_COLLAGE: "site-collage",
  COLLAGE1KMP1_1_1: "collage1kmp1-1-1",
  51POPUPLOGO: "51popuplogo",
  PHYGITAL_WORDMARK: "phygital-wordmark",
  PHYGITAL_LOGO_TEXT: "phygital-logo-text",
  PEGGY_CHARACTER: "peggy-character",
  WARRIOR_PRINCESS: "warrior-princess",
  TV_DISPLAY_LAYOUT: "tv-display-layout",
  ABSTRACT_DESIGN: "abstract-design",
  CLOUD_TYPOGRAPHY: "cloud-typography",
  TIPSY_TREE_INSTALLATION: "tipsy-tree-installation",
  SKILLS_SHOWCASE_ALT: "skills-showcase-alt",
  PROJECT_TYPES: "project-types",
  ABOUT_PAGE_PREVIEW: "about-page-preview",
  SKILLS_SHOWCASE: "skills-showcase",
  CANDLELIGHT_CONCERT: "candlelight-concert",
  VINTAGE_PORTRAIT_VIDEO_THUMB: "vintage-portrait-video-thumb",
  CHILDHOOD_PHOTO: "childhood-photo",
  VINTAGE_PORTRAIT: "vintage-portrait",
  CHILDHOOD_VIDEO_THUMB: "childhood-video-thumb",
  BELIEVE_INSTALLATION: "believe-installation",
  ALCHEMIST_INSTA_STORY: "alchemist-insta-story",
  DRAGON_VIDEO_THUMB: "dragon-video-thumb",
  DRAGON_WATERCOLOR: "dragon-watercolor",
  AETHERKEMETICUIWAYVY: "aetherkemeticuiwayvy",
  AETHERKEMETICUIEINTER: "aetherkemeticuieinter",
  AETHERUI: "aetherui",
  AETHERKEMETICUIBYTE111: "aetherkemeticuibyte111",
  BLISSETHEREAL: "blissethereal",
  UIORBETHEREAL: "uiorbethereal",
  AETHERKEMETICUI: "aetherkemeticui",
} as const;

export type AssetId = typeof ASSET_IDS[keyof typeof ASSET_IDS];

// Helper function to get asset by ID
export function getAsset(manifest: AssetManifest, id: AssetId): BrandAsset | undefined {
  return manifest.assets.find(a => a.id === id);
}

// Helper to get assets by category
export function getAssetsByCategory(manifest: AssetManifest, category: AssetCategory): BrandAsset[] {
  return manifest.assets.filter(a => a.category === category);
}

// Helper to build full asset URL
export function getAssetUrl(asset: BrandAsset, basePath: string = '/assets'): string {
  return `${basePath}/${asset.path}`;
}
