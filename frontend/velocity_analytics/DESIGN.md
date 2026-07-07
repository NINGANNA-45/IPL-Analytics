---
name: Velocity Analytics
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c6c6cd'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#909097'
  outline-variant: '#45464d'
  surface-tint: '#bec6e0'
  primary: '#bec6e0'
  on-primary: '#283044'
  primary-container: '#0f172a'
  on-primary-container: '#798098'
  inverse-primary: '#565e74'
  secondary: '#d3bbff'
  on-secondary: '#3f0689'
  secondary-container: '#592da2'
  on-secondary-container: '#c8aaff'
  tertiary: '#dec29a'
  on-tertiary: '#3e2d11'
  tertiary-container: '#231500'
  on-tertiary-container: '#957d5a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#ebdcff'
  secondary-fixed-dim: '#d3bbff'
  on-secondary-fixed: '#260059'
  on-secondary-fixed-variant: '#572ba0'
  tertiary-fixed: '#fcdeb5'
  tertiary-fixed-dim: '#dec29a'
  on-tertiary-fixed: '#271901'
  on-tertiary-fixed-variant: '#574425'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#353436'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-max: 1440px
  gutter: 20px
---

## Brand & Style

The brand personality is high-stakes, analytical, and elite. It is designed for professional cricket analysts, franchise scouts, and data-driven sports journalists who require deep insights into IPL performance metrics. The UI must evoke a sense of "Command Center" authority—combining the precision of fintech with the kinetic energy of professional sports.

The design style is **Glassmorphism**, leveraging depth through transparency and background blurs to keep the user oriented within a dense data environment. Elements should feel like high-tech overlays on a live stream. Surfaces are layered to establish hierarchy without using heavy shadows, relying instead on light-refracting borders and variable opacity to distinguish the functional "glass" from the expansive "pitch" of the data background.

## Colors

This design system uses a palette rooted in deep cosmic blues and royal purples to maintain a "night-match" atmosphere, synonymous with the IPL.

- **Primary & Background:** The foundation is an ultra-dark navy. Most surfaces use the primary midnight blue with varying levels of transparency.
- **Secondary:** Royal Purple is used for secondary actions, active states, and to highlight "home team" or premium data segments.
- **Accent:** Vibrant Gold is reserved for critical insights, winning probabilities, and high-performance markers (e.g., boundaries, wickets, or MVP status).
- **Functional Colors:** 
    - Success: Emerald Green (#10B981) for positive run rates and strike rates.
    - Danger: Crimson Red (#EF4444) for wickets lost or falling behind the required rate.

## Typography

The typography strategy balances high-impact headlines with dense, technical data readability. 

- **Primary Typeface (Inter):** Used for all UI controls, headings, and body copy. It provides a clean, neutral canvas that doesn't distract from complex charts. Use tighter letter spacing for large display headings to create a sense of urgency.
- **Data Typeface (JetBrains Mono):** Monospaced numerals and labels are essential for tables and KPI cards. This ensures that changing values (like a live scoreboard) do not cause layout shifts and align perfectly in vertical columns.
- **Hierarchy:** Use bold weights (700+) for scores and primary metrics. Use labels (JetBrains Mono) for units (e.g., "KPH", "SR", "AVG") to give the dashboard a technical, calibrated feel.

## Layout & Spacing

The layout follows a **fluid grid** model optimized for high-density information display. 

- **Grid:** A 12-column grid is used for the main dashboard. KPI cards typically span 3 columns, while primary charts span 6 or 9. 
- **Sidebar:** A narrow, collapsed navigation sidebar (80px) that expands on hover (240px) maximizes screen real estate for data visualizations.
- **Margins:** Large 40px outer margins on desktop provide visual breathing room, reducing to 16px on mobile.
- **Consistency:** All spacing—from padding inside cards to the gap between chart elements—must be a multiple of the 4px base unit to maintain a rigorous, mathematical rhythm.

## Elevation & Depth

Depth in this system is achieved through "Stacking Glass" rather than traditional shadows.

- **Background:** Solid Very Dark Navy (#020617).
- **Level 1 (Sub-surface):** Used for large content containers. `background: rgba(15, 23, 42, 0.4)`, `backdrop-filter: blur(8px)`.
- **Level 2 (Interactive Cards):** Used for KPI cards and player profiles. `background: rgba(30, 41, 59, 0.6)`, `backdrop-filter: blur(12px)`. These feature a 1px solid border at 10% white opacity on the top and left to simulate a "light catch" edge.
- **Level 3 (Modals/Popovers):** Highest elevation. `background: rgba(30, 41, 59, 0.9)`, `backdrop-filter: blur(20px)`.
- **Contrast Shadows:** Only use extremely subtle, large-radius shadows (`0 20px 50px rgba(0,0,0,0.5)`) on Level 3 elements to separate them from the complex background charts.

## Shapes

The shape language is "Soft-Technical." Elements are predominantly rectangular with small radii to maintain a professional, structured look. 

- **Cards & Containers:** Use `rounded-lg` (0.5rem) for a modern feel that isn't too "bubbly."
- **Buttons & Chips:** Use `rounded-md` (0.25rem) to differentiate interactive elements from static containers.
- **Data Points:** In line charts or scatter plots, use circular markers for players and diamond markers for key events (wickets/boundaries) to create a clear visual taxonomy.

## Components

- **KPI Cards:** Display a single large metric (e.g., "Run Rate") in JetBrains Mono. Include a mini sparkline chart at the bottom of the card using the accent Gold color.
- **Charts:** Use high-contrast colors for data series. Primary team = Secondary Purple; Opponent = Slate Grey. Accent Gold is used for the "In-Focus" data point.
- **Data Tables:** Row-based hover states using a 5% white overlay. Use `label-sm` for headers in all-caps with 0.1em letter spacing.
- **Buttons:**
    - Primary: Solid Royal Purple with white text.
    - Secondary: Ghost style with a 1px border of `border_color_hex` and a subtle blur background.
- **Player Profiles:** Use a large glassmorphic card with a clipped headshot. Background of the card should feature a subtle gradient of the team's secondary color at 10% opacity.
- **Filters:** Horizontal bar at the top of the dashboard using a "segmented control" style for season/match selection.
- **Live Indicator:** A small, pulsing Emerald Green dot next to the "Live Match" header to signify real-time data streaming.