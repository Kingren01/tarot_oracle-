import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="The Oracle — Agilisium CI",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

if not os.getenv("OPENAI_API_KEY") and not os.getenv("OPENROUTER_API_KEY"):
    st.error("⚠️ **OpenRouter API Key not configured.** Please add `OPENROUTER_API_KEY` to your `.env` file.")
    st.stop()

from utils.styles import apply_global_styles, get_theme


def render_sidebar():
    if "dark_mode" not in st.session_state:
        st.session_state["dark_mode"] = True  # Default to dark for tarot theme

    t = get_theme()

    with st.sidebar:
        # Oracle branding header
        st.markdown(f"""
        <div style="padding: 16px 8px 24px 8px;">
            <div style="display:flex; align-items:center; gap: 12px; margin-bottom: 4px;">
                <div style="
                    width:40px; height:40px;
                    background: linear-gradient(135deg, #C9A84C, #A8872E);
                    border-radius: 12px;
                    display:flex; align-items:center; justify-content:center;
                    font-size:20px;
                    flex-shrink:0;
                    box-shadow: 0 4px 16px rgba(201,168,76,0.3);
                ">🔮</div>
                <div>
                    <div style="font-weight:800; font-size:16px; color:{t['sidebar_text']}; line-height:1.1; font-family:'Cinzel',serif;">The Oracle</div>
                    <div style="font-size:10px; color:#C9A84C; letter-spacing:0.08em; font-family:'Cinzel',serif;">AGILISIUM CI v3.0</div>
                </div>
            </div>
        </div>
        <hr style="border:none; border-top:1px solid {t['accent']}33; margin: 0 0 16px 0;">
        """, unsafe_allow_html=True)

        # Nav buttons
        current = st.session_state.get("page", "dashboard")

        def nav_btn(label, page_id, icon):
            active = current == page_id
            clicked = st.button(f"{icon}  {label}", use_container_width=True, key=f"nav_{page_id}")
            if clicked and not active:
                st.session_state["page"] = page_id
                st.rerun()

        nav_btn("The Spread", "dashboard", "🎴")
        nav_btn("The Reading", "displacement_detail", "✦")

        st.markdown("<div style='height: 8px'></div>", unsafe_allow_html=True)
        st.button("Analytics  ›", use_container_width=True, disabled=True)
        st.button("Settings  ›", use_container_width=True, disabled=True)

        st.markdown(f"""<hr style="border:none; border-top:1px solid {t['accent']}22; margin: 16px 0;">""", unsafe_allow_html=True)

        # ── Day / Night Vision toggle ──────────────────────────────────
        mode_label = "☀️  Day Vision" if st.session_state["dark_mode"] else "🌙  Night Vision"
        if st.button(mode_label, use_container_width=True):
            st.session_state["dark_mode"] = not st.session_state["dark_mode"]
            st.rerun()

        st.markdown(f"""<hr style="border:none; border-top:1px solid {t['accent']}22; margin: 16px 0;">""", unsafe_allow_html=True)

        # Decorative ornament
        st.markdown("""
        <div style="text-align:center; margin: 8px 0 16px 0;">
            <span style="font-size:10px; color:#C9A84C44; letter-spacing:8px;">☽ ✦ ☾</span>
        </div>
        """, unsafe_allow_html=True)

        user = st.session_state.get("user_email", "User")
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:10px; margin-bottom: 12px;">
            <div style="
                width:32px; height:32px;
                background: linear-gradient(135deg, #C9A84C, #7B2D8B);
                border-radius:50%;
                display:flex; align-items:center; justify-content:center;
                color:#0D0B14; font-weight:800; font-size:13px;
                font-family:'Cinzel',serif;
            ">{user[0].upper()}</div>
            <div>
                <div style="font-size:13px; font-weight:600; color:{t['sidebar_text']}; font-family:'Cinzel',serif;">{user.split('@')[0].capitalize()}</div>
                <div style="font-size:11px; color:#6B5B7B;">{user}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Sign Out", use_container_width=True):
            st.session_state["authenticated"] = False
            st.session_state["page"] = "login"
            st.rerun()


def main():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "page" not in st.session_state:
        st.session_state["page"] = "login"

    # Apply global styles every run to ensure theme responsiveness
    apply_global_styles()

    if not st.session_state["authenticated"] or st.session_state["page"] == "login":
        from pages import login
        login.render()
    else:
        render_sidebar()
        page = st.session_state.get("page", "dashboard")

        if page == "dashboard":
            from pages import dashboard
            dashboard.render()
        elif page == "displacement_detail":
            from pages import displacement_detail
            displacement_detail.render()
        else:
            st.error("Page not found")


if __name__ == "__main__":
    main()
