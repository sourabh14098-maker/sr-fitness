import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Navbar improvements
css = css.replace(
    'padding: 0 2.5rem; height: 68px;',
    'padding: 0 4rem; height: 72px;'
)
css = css.replace(
    '.nav-links { display: flex; gap: 2rem; list-style: none; }',
    '.nav-links { display: flex; gap: 2.5rem; list-style: none; align-items: center; }'
)

# 2. Ticker fix
css = css.replace(
    'background: var(--red); padding: 8px 0;',
    'background: var(--red); padding: 12px 0; display: flex; align-items: center;'
)
css = css.replace(
    'letter-spacing: 0.1em; text-transform: uppercase; color: var(--black);',
    'letter-spacing: 0.1em; text-transform: uppercase; color: var(--black); line-height: 1;'
)

# 3. Hero improvements
css = css.replace(
    'font-size: clamp(5rem, 12vw, 11rem);',
    'font-size: clamp(4rem, 10vw, 9.5rem);'
)
css = css.replace(
    'line-height: 0.9; letter-spacing: 0.02em;',
    'line-height: 0.95; letter-spacing: 0.02em;'
)
css = css.replace(
    'margin-bottom: 2.5rem; font-weight: 300;',
    'margin-bottom: 3.5rem; font-weight: 300;'
)

# 4. Hero Stats proper padding
css = css.replace(
    'position: absolute; right: 2.5rem; bottom: 4rem;',
    'position: absolute; right: 4rem; bottom: 4rem;'
)

# 5. Append Media Queries if not present
media_queries = """
  /* RESPONSIVE DESIGN */
  @media (max-width: 1200px) {
    nav { padding: 0 2.5rem; }
    .hero-stats { right: 2.5rem; }
  }

  @media (max-width: 1024px) {
    .hero-stats { right: 2rem; bottom: 3rem; }
    .hero-title { font-size: clamp(3.5rem, 8vw, 7rem); }
    .stats-strip { grid-template-columns: repeat(2, 1fr); padding: 2.5rem 2rem; gap: 2.5rem; }
    .programs-grid, .trainers-grid, .plans-grid, .analysis-grid, .diet-panel.active { grid-template-columns: repeat(2, 1fr); }
    .footer-grid { grid-template-columns: repeat(2, 1fr); }
  }

  @media (max-width: 768px) {
    nav { padding: 0 1.5rem; height: 64px; }
    .nav-links { display: none; }
    .nav-logo-text { font-size: 13px; }
    
    .hero { padding: 7rem 1.5rem 4rem; justify-content: flex-start; }
    .hero-ticker { top: 64px; }
    .hero-content { margin-top: 4rem; }
    .hero-title { font-size: 3.5rem; margin-bottom: 1rem; }
    .hero-subtitle { font-size: 14px; margin-bottom: 2.5rem; }
    .hero-actions { flex-direction: column; align-items: flex-start; width: 100%; }
    .btn-primary, .btn-ghost { width: 100%; text-align: center; }
    
    .hero-stats { position: relative; right: 0; bottom: 0; margin-top: 4rem; flex-direction: row; flex-wrap: wrap; justify-content: flex-start; gap: 2rem; }
    .hero-stat { text-align: left; }
    .hero-stat-bar { margin-left: 0; }
    
    section { padding: 4rem 1.5rem; }
    .section-title { font-size: 2.5rem; }
    
    .stats-strip { grid-template-columns: 1fr; gap: 2rem; padding: 2rem 1.5rem; margin-top: 64px; }
    .programs-grid, .trainers-grid, .plans-grid, .analysis-grid, .diet-panel.active { grid-template-columns: 1fr; }
    .bmi-layout { grid-template-columns: 1fr; }
    .form-grid { grid-template-columns: 1fr; }
    
    .footer-grid { grid-template-columns: 1fr; gap: 2rem; }
    
    .live-feed { bottom: 1rem; padding: 8px 16px; font-size: 10px; width: 90%; justify-content: center; max-width: 320px; }
    .auth-section { padding: 3rem 1.5rem; margin-top: 64px; }
  }
"""

if "RESPONSIVE DESIGN" not in css:
    css += media_queries

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
