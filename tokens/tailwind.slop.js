/**
 * Tailwind preset — AI-SLOP UI/UX PRO-MAX
 * -------------------------------------------------------------------------
 * Usage:
 *   module.exports = {
 *     presets: [require('./tokens/tailwind.slop.js')],
 *     content: ['./src/**\/*.{js,ts,jsx,tsx,html}'],
 *   };
 *
 * Provides: slop palette, gradients, glow shadows, 28px radius, font stacks,
 * and the mandatory keyframes/animations.
 *
 * MIT © 2026 romipq
 */

/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {
    extend: {
      colors: {
        slop: {
          bg: '#07070f',
          raised: '#0b0b18',
          panel: '#101024',
          surface: 'rgba(255, 255, 255, 0.045)',
          'surface-2': 'rgba(255, 255, 255, 0.075)',
          line: 'rgba(255, 255, 255, 0.09)',
          'line-strong': 'rgba(255, 255, 255, 0.16)',
          text: '#f6f4ff',
          muted: '#a9a6c9',
          dim: '#75729a',
        },
        brand: {
          violet: '#8b5cf6',
          indigo: '#6366f1',
          fuchsia: '#d946ef',
          pink: '#ec4899',
          cyan: '#22d3ee',
          sky: '#38bdf8',
          emerald: '#34d399',
          amber: '#fbbf24',
        },
      },
      fontFamily: {
        body: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        display: ['Poppins', 'Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        serif: ['"Instrument Serif"', 'Georgia', 'serif'],
      },
      backgroundImage: {
        'slop-grad': 'linear-gradient(135deg, #6366f1 0%, #a855f7 46%, #ec4899 100%)',
        'slop-product': 'linear-gradient(120deg, #22d3ee 0%, #6366f1 48%, #d946ef 100%)',
        'slop-text': 'linear-gradient(115deg, #e9d5ff 0%, #a78bfa 28%, #f0abfc 62%, #67e8f9 100%)',
        'slop-radial': 'radial-gradient(900px 500px at 12% -8%, rgba(124,58,237,.28), transparent 62%)',
      },
      boxShadow: {
        glow: '0 20px 60px -12px rgba(124, 58, 237, .55)',
        'glow-pink': '0 20px 60px -12px rgba(236, 72, 153, .45)',
        card: '0 24px 80px -32px rgba(0, 0, 0, .9), inset 0 1px 0 rgba(255, 255, 255, .06)',
        featured: '0 40px 100px -40px rgba(168, 85, 247, .7), inset 0 1px 0 rgba(255, 255, 255, .08)',
      },
      borderRadius: {
        slop: '20px',
        'slop-lg': '28px',
        'slop-xl': '32px',
      },
      backdropBlur: {
        slop: '18px',
      },
      letterSpacing: {
        slop: '-0.04em',
        eyebrow: '0.22em',
      },
      transitionTimingFunction: {
        slop: 'cubic-bezier(.22, 1, .36, 1)',
      },
      keyframes: {
        'gradient-pan': {
          '0%, 100%': { backgroundPosition: '0% 50%' },
          '50%': { backgroundPosition: '100% 50%' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-12px)' },
        },
        'pulse-glow': {
          '0%, 100%': { boxShadow: '0 18px 50px -12px rgba(168,85,247,.75)' },
          '50%': { boxShadow: '0 22px 70px -8px rgba(236,72,153,.85)' },
        },
        shimmer: {
          '0%': { transform: 'translateX(-120%) skewX(-18deg)' },
          '100%': { transform: 'translateX(220%) skewX(-18deg)' },
        },
        marquee: {
          from: { transform: 'translateX(0)' },
          to: { transform: 'translateX(-50%)' },
        },
        'spin-slow': {
          to: { transform: 'translateX(-50%) rotate(360deg)' },
        },
        'blob-drift': {
          '0%, 100%': { transform: 'translate3d(0,0,0) scale(1)' },
          '33%': { transform: 'translate3d(40px,-30px,0) scale(1.08)' },
          '66%': { transform: 'translate3d(-30px,20px,0) scale(.95)' },
        },
      },
      animation: {
        'gradient-pan': 'gradient-pan 6s ease infinite',
        float: 'float 6s ease-in-out infinite',
        'pulse-glow': 'pulse-glow 3.4s ease-in-out infinite',
        shimmer: 'shimmer 2.8s ease-in-out infinite',
        marquee: 'marquee 26s linear infinite',
        'spin-slow': 'spin-slow 18s linear infinite',
        'blob-drift': 'blob-drift 16s ease-in-out infinite',
      },
    },
  },
};
