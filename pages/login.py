import streamlit as st

def render():
    # Full-page mystic gradient background
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap');
    .stApp {
        background: linear-gradient(145deg, #0D0B14 0%, #1A1233 50%, #2A1B3D 100%) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    _, col, _ = st.columns([1, 1.1, 1])

    with col:
        st.markdown("<div style='height: 48px'></div>", unsafe_allow_html=True)

        # Oracle branding
        st.markdown("""
        <div style="text-align: center; margin-bottom: 40px;">
            <div style="
                width: 72px; height: 72px;
                background: linear-gradient(135deg, #C9A84C 0%, #A8872E 100%);
                border-radius: 20px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                font-size: 34px;
                margin-bottom: 20px;
                box-shadow: 0 8px 32px rgba(201,168,76,0.35), 0 0 60px rgba(201,168,76,0.12);
            ">🔮</div>
            <div style="
                font-family: 'Cinzel', serif;
                font-size: 28px;
                font-weight: 800;
                color: #F0EAD6;
                letter-spacing: 0.04em;
            ">The Oracle</div>
            <div style="
                font-family: 'Cormorant Garamond', serif;
                font-size: 15px;
                color: #B8A9CC;
                margin-top: 8px;
                font-style: italic;
            ">
                Competitive Intelligence &amp; Displacement Divination
            </div>
            <div style="
                font-family: 'Cinzel', serif;
                font-size: 10px;
                color: #C9A84C66;
                margin-top: 12px;
                letter-spacing: 0.3em;
            ">☽ ✦ ☾</div>
        </div>
        """, unsafe_allow_html=True)

        # Card wrapper — parchment style
        st.markdown("""
        <div style="
            background: linear-gradient(145deg, #1A1726 0%, #231F33 100%);
            border-radius: 16px;
            padding: 48px 44px;
            box-shadow: 0 12px 48px rgba(201,168,76,0.15), 0 0 80px rgba(123,45,139,0.08);
            border: 1px solid #C9A84C33;
            position: relative;
        ">
        <div style="
            position: absolute; top: 8px; left: 50%;
            transform: translateX(-50%);
            font-size: 10px; color: #C9A84C33;
            letter-spacing: 6px;
        ">✦ ✦ ✦</div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style="
            text-align:center;
            margin-bottom: 24px;
            letter-spacing: 0.15em;
            font-family: 'Cinzel', serif;
            font-size: 11px;
            font-weight: 600;
            color: #C9A84C;
            text-transform: uppercase;
        ">Enter the Oracle</p>
        """, unsafe_allow_html=True)

        email = st.text_input("Email address", placeholder="admin@agilisium.com", label_visibility="collapsed")
        st.markdown("<div style='height: 8px'></div>", unsafe_allow_html=True)
        password = st.text_input("Password", type="password", placeholder="Password", label_visibility="collapsed")
        st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)

        if st.button("Invoke Access", use_container_width=True):
            if email == "admin@agilisium.com" and password == "Agilis@2025":
                st.session_state["authenticated"] = True
                st.session_state["user_email"] = email
                st.session_state["page"] = "dashboard"
                st.rerun()
            else:
                st.error("The spirits reject these credentials. Try again.")

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <p style='text-align: center; color: #6B5B7B; font-size: 11px; margin-top: 28px;
                   letter-spacing: 0.02em; font-family: Cormorant Garamond, serif;'>
            © 2025 Agilisium AI · The Oracle · Confidential
        </p>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    render()
