// Huisstijl per merk, overgenomen uit brands/<slug>/brand.css (Loveke: loveke/marketing/instagram/brand.css).
// Paden zijn relatief aan de public-map die render.sh opbouwt: brands/ = nomadix-socials/brands, loveke/ = loveke/marketing.
export type Theme = {
  bg: string; bg2: string; fg: string; mute: string; accent: string; accent2: string;
  title: string; text: string; titleUpper: boolean; titleWeight: number; radius: number;
  logo?: string; logoDark?: string; fonts: {family: string; url: string; weight?: string}[];
};
const f = (family: string, url: string, weight = '400') => ({family, url, weight});
export const THEMES: Record<string, Theme> = {
  vanxcel: {bg: '#0A0A0A', bg2: '#141414', fg: '#FFFFFF', mute: '#A3A3A3', accent: '#008894', accent2: '#F59E0B',
    title: 'Bebas Neue', text: 'Inter', titleUpper: true, titleWeight: 400, radius: 18, logo: 'brands/vanxcel/logo-white.svg', logoDark: 'brands/vanxcel/logo-black.svg',
    fonts: [f('Bebas Neue', 'brands/vanxcel/fonts/bebas-neue-latin-400-normal.woff2'), f('Inter', 'brands/vanxcel/fonts/inter-latin-500-normal.woff2', '500'), f('Inter', 'brands/vanxcel/fonts/inter-latin-700-normal.woff2', '700')]},
  fonske: {bg: '#110C08', bg2: '#1D1711', fg: '#F4F1EC', mute: '#B7A894', accent: '#F4A434', accent2: '#D45A4F',
    title: 'Bebas Neue', text: 'Space Grotesk', titleUpper: true, titleWeight: 400, radius: 22, logo: 'brands/fonske/logo-mark.png',
    fonts: [f('Bebas Neue', 'brands/fonske/fonts/bebas-neue-latin-400-normal.woff2'), f('Space Grotesk', 'brands/fonske/fonts/space-grotesk-latin-500-normal.woff2', '500'), f('Space Grotesk', 'brands/fonske/fonts/space-grotesk-latin-700-normal.woff2', '700')]},
  sellqo: {bg: '#0A1033', bg2: '#00145B', fg: '#FFFFFF', mute: '#8A93B8', accent: '#FD7B5B', accent2: '#FFF7F2',
    title: 'Poppins', text: 'Inter', titleUpper: false, titleWeight: 800, radius: 28, logo: 'brands/sellqo/logo-white.png', logoDark: 'brands/sellqo/logo-navy.png',
    fonts: [f('Poppins', 'brands/sellqo/fonts/poppins-latin-700-normal.woff2', '700'), f('Poppins', 'brands/sellqo/fonts/poppins-latin-800-normal.woff2', '800'), f('Inter', 'brands/sellqo/fonts/inter-latin-500-normal.woff2', '500'), f('Inter', 'brands/sellqo/fonts/inter-latin-700-normal.woff2', '700')]},
  'studio-akke': {bg: '#0F1729', bg2: '#211438', fg: '#FFFFFF', mute: '#94A3B8', accent: '#2BD4BD', accent2: '#F2456D',
    title: 'Inter', text: 'Inter', titleUpper: false, titleWeight: 900, radius: 24, logo: 'brands/studio-akke/logo-white.svg',
    fonts: [f('Inter', 'brands/studio-akke/fonts/inter-latin-500-normal.woff2', '500'), f('Inter', 'brands/studio-akke/fonts/inter-latin-800-normal.woff2', '800'), f('Inter', 'brands/studio-akke/fonts/inter-latin-900-normal.woff2', '900')]},
  loveke: {bg: '#FFF8F0', bg2: '#FF85A1', fg: '#1A1A1A', mute: '#6b6b6b', accent: '#FF7033', accent2: '#FFD43D',
    title: 'Lilita One', text: 'DM Sans', titleUpper: false, titleWeight: 400, radius: 34,
    fonts: [f('Lilita One', 'loveke/instagram/fonts/lilita-one-latin-400-normal.woff2'), f('DM Sans', 'loveke/instagram/fonts/dm-sans-latin-600-normal.woff2', '600'), f('DM Sans', 'loveke/instagram/fonts/dm-sans-latin-700-normal.woff2', '700'), f('Caveat', 'loveke/instagram/fonts/caveat-latin-700-normal.woff2', '700')]},
};
