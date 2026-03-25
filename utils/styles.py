import streamlit as st

# ──────────────────────────────────────────────────────────────────
#  Tarot Theme Tokens  🔮
# ──────────────────────────────────────────────────────────────────
LIGHT = {
    "app_bg":        "#F5F0E8",       # warm parchment
    "surface":       "#FFFDF7",       # ivory card
    "surface_alt":   "#EDE8DC",       # aged paper
    "border":        "#D4C9A8",       # antique gold edge
    "text_primary":  "#2A1B3D",       # deep mystic ink
    "text_secondary":"#6B5B7B",       # faded violet
    "text_muted":    "#A99BBD",       # ghost lavender
    "accent":        "#C9A84C",       # tarot gold
    "accent_dark":   "#A8872E",       # burnished gold
    "success":       "#2D9B5A",       # emerald fate
    "warning":       "#D4882A",       # amber oracle
    "danger":        "#A83240",       # crimson omen
    "sidebar_bg":    "#2A1B3D",       # midnight purple
    "sidebar_text":  "#F5F0E8",       # parchment on dark
    "tab_list_bg":   "#EDE8DC",
    "tab_active_bg": "#FFFDF7",
    "input_bg":      "#FFFDF7",
    "card_glow":     "rgba(201,168,76,0.12)",
    "star_overlay":  "rgba(201,168,76,0.04)",
}

DARK = {
    "app_bg":        "#0D0B14",       # void black
    "surface":       "#1A1726",       # midnight card
    "surface_alt":   "#231F33",       # deep purple
    "border":        "#3D3555",       # mystic border
    "text_primary":  "#F0EAD6",       # aged parchment
    "text_secondary":"#B8A9CC",       # spectral lilac
    "text_muted":    "#6B5B7B",       # ghost purple
    "accent":        "#D4AF37",       # divine gold
    "accent_dark":   "#B8962E",       # ancient gold
    "success":       "#34D399",       # emerald glow
    "warning":       "#F59E0B",       # amber flame
    "danger":        "#EF4444",       # blood omen
    "sidebar_bg":    "#12101C",       # abyss
    "sidebar_text":  "#F0EAD6",
    "tab_list_bg":   "#231F33",
    "tab_active_bg": "#3D3555",
    "input_bg":      "#1A1726",
    "card_glow":     "rgba(212,175,55,0.15)",
    "star_overlay":  "rgba(212,175,55,0.06)",
}


def get_theme():
    return DARK if st.session_state.get("dark_mode", False) else LIGHT


def apply_global_styles():
    t = get_theme()

    css = f"""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap');

      /* ── Reset & base ── */
      .stApp,
      [data-testid="stAppViewContainer"],
      [data-testid="stAppViewBlockContainer"] {{
          background-color: {t['app_bg']} !important;
          color: {t['text_primary']} !important;
          font-family: 'Cormorant Garamond', 'Georgia', serif !important;
      }}

      /* ── Force all text ── */
      p, span, label,
      [data-testid="stMarkdownContainer"],
      [data-testid="stMarkdownContainer"] *,
      .stMarkdown, .stMarkdown * {{
          color: {t['text_primary']} !important;
          font-family: 'Cormorant Garamond', serif !important;
      }}
      h1, h2, h3, h4, h5, h6 {{
          color: {t['text_primary']} !important;
          font-family: 'Cinzel', serif !important;
      }}
      .stMarkdown em, .stMarkdown strong {{ color: {t['text_primary']} !important; }}

      /* Hide clutter */
      #MainMenu {{ visibility: hidden; }}
      header {{ visibility: hidden; }}
      [data-testid="stSidebarNav"] {{ display: none !important; }}

      /* ── Sidebar (always dark mystic) ── */
      [data-testid="stSidebar"],
      [data-testid="stSidebar"] > div {{
          background: linear-gradient(180deg, {t['sidebar_bg']} 0%, #1A1233 100%) !important;
          border-right: 1px solid {t['border']} !important;
      }}
      [data-testid="stSidebar"] * {{
          color: {t['sidebar_text']} !important;
          font-family: 'Cormorant Garamond', serif !important;
      }}
      [data-testid="stSidebar"] h1,
      [data-testid="stSidebar"] h2,
      [data-testid="stSidebar"] h3 {{
          font-family: 'Cinzel', serif !important;
      }}
      [data-testid="stSidebar"] .stButton > button {{
          background: transparent !important;
          color: {t['sidebar_text']} !important;
          box-shadow: none !important;
          border-radius: 8px !important;
          text-align: left !important;
          justify-content: flex-start !important;
          font-family: 'Cormorant Garamond', serif !important;
          font-size: 15px !important;
          font-weight: 600 !important;
      }}
      [data-testid="stSidebar"] .stButton > button:hover {{
          background: rgba(201,168,76,0.12) !important;
          transform: none !important;
      }}

      /* ── Inputs ── */
      input, textarea, select,
      [data-baseweb="input"] input,
      [data-baseweb="textarea"] textarea {{
          background-color: {t['input_bg']} !important;
          color: {t['text_primary']} !important;
          border: 1px solid {t['border']} !important;
          border-radius: 8px !important;
          font-family: 'Cormorant Garamond', serif !important;
          font-size: 16px !important;
      }}
      input::placeholder, textarea::placeholder {{ color: {t['text_muted']} !important; }}
      input:focus, textarea:focus {{
          border-color: {t['accent']} !important;
          box-shadow: 0 0 0 3px {t['card_glow']} !important;
      }}
      [data-testid="stTextInput"] label,
      [data-testid="stFileUploader"] label {{
          color: {t['text_secondary']} !important;
          font-size: 14px !important;
          font-weight: 600 !important;
          font-family: 'Cinzel', serif !important;
      }}

      /* ── Primary buttons (Invoke the Reading) ── */
      div[data-testid="stAppViewContainer"] .main .stButton button[kind="primary"],
      div[data-testid="stAppViewContainer"] .main .stButton button[data-testid="stBaseButton-primary"],
      button[data-testid="stBaseButton-primary"] {{
          background: linear-gradient(135deg, {t['accent']} 0%, {t['accent_dark']} 100%) !important;
          color: #1A1B2E !important;
          border: none !important;
          border-radius: 8px !important;
          padding: 0.7rem 2rem !important;
          font-weight: 700 !important;
          font-family: 'Cinzel', serif !important;
          font-size: 14px !important;
          letter-spacing: 0.05em !important;
          box-shadow: 0 4px 20px {t['card_glow']}, 0 0 40px {t['star_overlay']} !important;
          text-transform: uppercase !important;
      }}
      div[data-testid="stAppViewContainer"] .main .stButton button[kind="primary"]:hover,
      button[data-testid="stBaseButton-primary"]:hover {{
          transform: translateY(-2px) !important;
          box-shadow: 0 6px 28px rgba(201,168,76,0.35) !important;
      }}

      /* ── Secondary buttons (View →) ── */
      div[data-testid="stAppViewContainer"] .main .stButton button[kind="secondary"],
      button[data-testid="stBaseButton-secondary"] {{
          background-color: transparent !important;
          color: {t['accent']} !important;
          border: 1px solid {t['accent']} !important;
          border-radius: 8px !important;
          font-family: 'Cinzel', serif !important;
          font-weight: 600 !important;
          font-size: 13px !important;
          letter-spacing: 0.04em !important;
          transition: all 0.3s ease !important;
      }}
      div[data-testid="stAppViewContainer"] .main .stButton button[kind="secondary"]:hover,
      button[data-testid="stBaseButton-secondary"]:hover {{
          background: linear-gradient(135deg, {t['accent']} 0%, {t['accent_dark']} 100%) !important;
          color: #1A1B2E !important;
      }}

      /* ── Default Streamlit buttons (no kind attr) ── */
      div[data-testid="stAppViewContainer"] .main .stButton > button:not([kind]) {{
          background: transparent !important;
          color: {t['accent']} !important;
          border: 1px solid {t['border']} !important;
          border-radius: 8px !important;
          font-family: 'Cinzel', serif !important;
          font-weight: 600 !important;
          transition: all 0.3s ease !important;
      }}
      div[data-testid="stAppViewContainer"] .main .stButton > button:not([kind]):hover {{
          border-color: {t['accent']} !important;
          background: {t['card_glow']} !important;
      }}

      /* ── Download button ── */
      [data-testid="stDownloadButton"] button {{
          background: linear-gradient(135deg, {t['accent']} 0%, {t['accent_dark']} 100%) !important;
          color: #1A1B2E !important;
          border: none !important;
          border-radius: 8px !important;
          font-weight: 700 !important;
          font-family: 'Cinzel', serif !important;
          padding: 10px 24px !important;
          text-transform: uppercase !important;
          letter-spacing: 0.05em !important;
      }}

      /* ── Tabs ── */
      .stTabs [data-baseweb="tab-list"] {{
          background: {t['surface_alt']} !important;
          border-radius: 8px !important;
          padding: 4px !important;
          gap: 2px !important;
          border-bottom: none !important;
          border: 1px solid {t['border']} !important;
      }}
      .stTabs [data-baseweb="tab"] {{
          background: transparent !important;
          color: {t['text_secondary']} !important;
          border-radius: 6px !important;
          border: none !important;
          font-weight: 600 !important;
          font-size: 13px !important;
          padding: 8px 16px !important;
          font-family: 'Cinzel', serif !important;
          letter-spacing: 0.02em !important;
      }}
      .stTabs [aria-selected="true"] {{
          background: {t['surface']} !important;
          color: {t['accent']} !important;
          box-shadow: 0 2px 12px {t['card_glow']} !important;
          border: 1px solid {t['accent']}44 !important;
      }}

      /* ── Metrics ── */
      [data-testid="stMetric"] {{
          background: {t['surface']} !important;
          border-radius: 12px !important;
          padding: 20px 24px !important;
          border: 1px solid {t['border']} !important;
          box-shadow: 0 2px 12px {t['card_glow']} !important;
      }}
      [data-testid="stMetricLabel"] p {{
          color: {t['text_muted']} !important;
          font-size: 12px !important;
          font-family: 'Cinzel', serif !important;
          text-transform: uppercase !important;
          letter-spacing: 0.06em !important;
      }}
      [data-testid="stMetricValue"] {{
          color: {t['accent']} !important;
          font-size: 26px !important;
          font-weight: 700 !important;
          font-family: 'Cinzel', serif !important;
      }}
      [data-testid="stMetricDelta"] {{ color: {t['success']} !important; font-weight: 600 !important; }}

      /* ── Alerts ── */
      [data-testid="stAlert"],
      [data-testid="stAlert"] * {{ border-radius: 8px !important; }}

      /* ── Expander ── */
      [data-testid="stExpander"] {{
          background: {t['surface']} !important;
          border-radius: 8px !important;
          border: 1px solid {t['border']} !important;
      }}
      [data-testid="stExpander"] summary,
      [data-testid="stExpander"] summary * {{
          color: {t['accent']} !important;
          font-weight: 600 !important;
          font-family: 'Cinzel', serif !important;
      }}
      [data-testid="stExpander"] [data-testid="stMarkdownContainer"] * {{ color: {t['text_secondary']} !important; }}

      /* ── DataFrames ── */
      [data-testid="stDataFrame"] {{
          border-radius: 8px !important;
          overflow: hidden !important;
          border: 1px solid {t['border']} !important;
      }}
      [data-testid="stDataFrame"] * {{ color: {t['text_primary']} !important; }}

      /* ── File uploader ── */
      [data-testid="stFileUploadDropzone"] {{
          background: {t['surface_alt']} !important;
          border: 1px dashed {t['accent']}66 !important;
          border-radius: 8px !important;
      }}
      [data-testid="stFileUploadDropzone"] * {{ color: {t['text_secondary']} !important; }}

      /* ── Progress ── */
      [data-testid="stProgressBar"] > div {{
          background: linear-gradient(90deg, {t['accent']}, {t['accent_dark']}) !important;
          border-radius: 4px !important;
      }}

      /* ── Bordered containers ── */
      [data-testid="stVerticalBlockBorderWrapper"] {{
          background: {t['surface']} !important;
          border-radius: 12px !important;
          border: 1px solid {t['border']} !important;
          padding: 20px !important;
      }}

      /* ── Login card ── */
      .login-card {{
          background: {t['surface']};
          border-radius: 16px;
          padding: 48px 44px;
          box-shadow: 0 8px 40px {t['card_glow']};
          border: 1px solid {t['accent']}33;
          position: relative;
      }}

      /* ── TAROT CARD COMPONENT ── */
      .tarot-card {{
          background: {t['surface']};
          border-radius: 12px;
          border: 1px solid {t['border']};
          padding: 28px 32px;
          box-shadow: 0 4px 20px {t['card_glow']};
          margin-bottom: 20px;
          position: relative;
          overflow: hidden;
      }}
      .tarot-card::before {{
          content: "✦";
          position: absolute;
          top: 8px;
          left: 12px;
          font-size: 10px;
          color: {t['accent']}44;
      }}
      .tarot-card::after {{
          content: "✦";
          position: absolute;
          bottom: 8px;
          right: 12px;
          font-size: 10px;
          color: {t['accent']}44;
      }}

      /* ── Arcana badges ── */
      .arcana-major {{
          background: linear-gradient(135deg, {t['danger']}, #8B1A2B);
          color: #FFF;
          padding: 3px 14px;
          border-radius: 4px;
          font-size: 11px;
          font-weight: 700;
          font-family: 'Cinzel', serif;
          letter-spacing: 0.06em;
          text-transform: uppercase;
      }}
      .arcana-high {{
          background: linear-gradient(135deg, {t['warning']}, #B87314);
          color: #FFF;
          padding: 3px 14px;
          border-radius: 4px;
          font-size: 11px;
          font-weight: 700;
          font-family: 'Cinzel', serif;
          letter-spacing: 0.06em;
          text-transform: uppercase;
      }}
      .arcana-medium {{
          background: linear-gradient(135deg, {t['accent']}, {t['accent_dark']});
          color: #1A1B2E;
          padding: 3px 14px;
          border-radius: 4px;
          font-size: 11px;
          font-weight: 700;
          font-family: 'Cinzel', serif;
          letter-spacing: 0.06em;
          text-transform: uppercase;
      }}
      .arcana-low {{
          background: linear-gradient(135deg, {t['success']}, #1A7A3E);
          color: #FFF;
          padding: 3px 14px;
          border-radius: 4px;
          font-size: 11px;
          font-weight: 700;
          font-family: 'Cinzel', serif;
          letter-spacing: 0.06em;
          text-transform: uppercase;
      }}

      /* ── Oracle label (replaces ci-label) ── */
      .oracle-label {{
          font-size: 11px !important;
          font-weight: 700 !important;
          text-transform: uppercase !important;
          letter-spacing: 0.12em !important;
          color: {t['accent']} !important;
          font-family: 'Cinzel', serif !important;
      }}
      .oracle-title {{
          font-size: 30px;
          font-weight: 800;
          letter-spacing: -0.01em;
          color: {t['text_primary']};
          line-height: 1.2;
          font-family: 'Cinzel', serif;
      }}
      .oracle-subtitle {{
          font-size: 16px;
          color: {t['text_secondary']};
          margin-top: 6px;
          font-family: 'Cormorant Garamond', serif;
          font-style: italic;
      }}
      .oracle-divider {{
          border: none;
          border-top: 1px solid {t['border']};
          margin: 20px 0;
      }}

      /* ── Slide card (Tarot style) ── */
      .slide-card {{
          background: {t['surface']};
          border: 1px solid {t['accent']}44;
          border-radius: 12px;
          padding: 48px 56px;
          min-height: 380px;
          box-shadow: 0 8px 32px {t['card_glow']};
          position: relative;
      }}
      .slide-card::before {{
          content: "☽ ✦ ☾";
          position: absolute;
          top: 12px;
          left: 50%;
          transform: translateX(-50%);
          font-size: 12px;
          color: {t['accent']}55;
          letter-spacing: 8px;
      }}

      /* ── Gap card grid ── */
      .gap-card {{
          background: {t['surface']};
          border: 1px solid {t['border']};
          border-radius: 10px;
          padding: 20px 24px;
          box-shadow: 0 2px 12px {t['card_glow']};
          height: 100%;
      }}

      /* ── PDF Section ── */
      .pdf-section {{
          background: {t['surface']};
          border: 1px solid {t['border']};
          border-radius: 10px;
          padding: 32px 36px;
          margin-bottom: 24px;
          box-shadow: 0 2px 12px {t['card_glow']};
      }}
      .pdf-page-break {{
          border: none;
          border-top: 2px dashed {t['accent']}33;
          margin: 32px 0;
          position: relative;
      }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def render_score_pill(risk_level):
    mapping = {
        "Critical": "arcana-major",
        "High":     "arcana-high",
        "Medium":   "arcana-medium",
    }
    cls = mapping.get(risk_level, "arcana-low")
    labels = {
        "Critical": "⚡ Major Arcana",
        "High":     "✦ High Arcana",
        "Medium":   "◇ Minor Arcana",
        "Low":      "○ The Fool",
    }
    label = labels.get(risk_level, risk_level)
    return f'<span class="{cls}">{label}</span>'
