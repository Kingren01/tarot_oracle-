import streamlit as st
import pandas as pd
from utils.charts import create_circular_gauge, create_timeline_chart
from utils.pdf_generator import generate_displacement_pdf
from utils.styles import get_theme
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))


def render():
    t = get_theme()
    if "crewai_output" not in st.session_state:
        st.markdown(f"""
        <div style="text-align:center; padding:80px 20px;">
            <div style="font-size:64px; margin-bottom:16px;">🔮</div>
            <div style="font-size:22px; font-weight:700; color:{t['accent']}; font-family:'Cinzel',serif; margin-bottom:8px;">No Reading Selected</div>
            <div style="color:{t['text_secondary']}; font-size:15px; font-family:'Cormorant Garamond',serif; font-style:italic;">
                Invoke a reading from The Spread to reveal the cards.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("← Return to The Spread"):
            st.session_state["page"] = "dashboard"
            st.rerun()
        return

    out = st.session_state["crewai_output"]
    metrics = out.get("dashboard_metrics_package", {})
    pptx = out.get("executive_powerpoint", [])
    pdf = out.get("formal_pdf_document", {})
    specs = out.get("export_specifications", {})
    impl = out.get("implementation_package", {})

    # ── Page header ──────────────────────────────────────────────────────
    if st.button("← The Spread"):
        st.session_state["page"] = "dashboard"
        st.rerun()

    st.markdown("<div style='height: 16px'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="margin-bottom: 28px;">
        <div class='oracle-label'>✦ THE READING ✦</div>
        <div class='oracle-title' style='color:{t["text_primary"]}'>{out.get('target_account', 'Unknown')}</div>
        <div class='oracle-subtitle'>Displacing <strong style="color:{t['accent']}">{out.get('competitor_name', 'Unknown')}</strong></div>
    </div>
    """, unsafe_allow_html=True)

    # ── Tabs ─────────────────────────────────────────────────────────────
    t1, t2, t3, t4, t5 = st.tabs([
        "🎴 Dashboard Metrics",
        "✦ Executive Slides",
        "📜 10-Page Summary",
        "⚙ Export Specs",
        "🗺 Implementation",
    ])

    # ══════════════════════════════════════════════════════════════════════
    #  Tab 1: Dashboard Metrics — FULL DATA RENDERING
    # ══════════════════════════════════════════════════════════════════════
    with t1:
        # ── Row 1: Gauge + Timeline ──
        col1, col2 = st.columns([1, 2])
        with col1:
            ds = metrics.get("displacement_score", {})
            st.plotly_chart(
                create_circular_gauge(ds.get("value", 0), max_val=100, title="Arcana Displacement Score"),
                use_container_width=True
            )
            # Benchmark comparison
            st.markdown(f"""
            <div style="text-align:center; margin-top:-8px;">
                <span style="font-family:'Cinzel',serif; font-size:11px; color:{t['text_muted']}; text-transform:uppercase; letter-spacing:0.08em;">
                    Industry Benchmark: {ds.get('benchmark', 'N/A')} / 100
                </span>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.plotly_chart(create_timeline_chart(), use_container_width=True)

        st.markdown("<div style='height: 12px'></div>", unsafe_allow_html=True)

        # ── Row 2: Primary Financial KPIs ──
        m1, m2, m3 = st.columns(3)
        roi = metrics.get("roi_projection", {})
        fin = metrics.get("financial_projections", {})
        m1.metric("Projected ROI", roi.get("value", "N/A"), f"Confidence: {roi.get('confidence', 'N/A')}")
        m2.metric("Year 1 Savings", fin.get("year_1_savings", "N/A"))
        m3.metric("Payback Period", fin.get("payback_period", "N/A"))

        st.markdown("<div style='height: 8px'></div>", unsafe_allow_html=True)

        # ── Row 3: Implementation Cost + Executive Summary Metrics ──
        m4, m5, m6 = st.columns(3)
        m4.metric("Implementation Cost", fin.get("implementation_cost", "N/A"))
        esm = metrics.get("executive_summary_metrics", {})
        m5.metric("Agilisium Value", esm.get("Agilisium_Value", "N/A"))
        m6.metric("Risk Avoidance", esm.get("Risk_Avoidance", "N/A"))

        st.markdown("<div style='height: 8px'></div>", unsafe_allow_html=True)

        # ── Row 4: Additional Executive Metrics ──
        extra_metrics = {k: v for k, v in esm.items() if k not in ("Agilisium_Value", "Risk_Avoidance")}
        if extra_metrics:
            ecols = st.columns(len(extra_metrics))
            for i, (key, val) in enumerate(extra_metrics.items()):
                label = key.replace("_", " ").title()
                ecols[i].metric(label, str(val))

        st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)

        # ── Row 5: Cost Savings Breakdown ──
        cost_savings = fin.get("cost_savings", {})
        revenue_impact = fin.get("revenue_impact", {})

        if cost_savings or revenue_impact:
            fc1, fc2 = st.columns(2)
            with fc1:
                st.markdown(f"<div class='oracle-label' style='margin-bottom:12px;'>💰 Cost Savings Breakdown</div>", unsafe_allow_html=True)
                if cost_savings:
                    for k, v in cost_savings.items():
                        label = k.replace("_", " ").title()
                        st.markdown(f"""
                        <div style="display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px solid {t['border']};">
                            <span style="color:{t['text_secondary']}; font-size:14px;">{label}</span>
                            <span style="color:{t['accent']}; font-weight:700; font-family:'Cinzel',serif; font-size:14px;">{v}</span>
                        </div>
                        """, unsafe_allow_html=True)
            with fc2:
                st.markdown(f"<div class='oracle-label' style='margin-bottom:12px;'>📈 Revenue Impact</div>", unsafe_allow_html=True)
                if revenue_impact:
                    for k, v in revenue_impact.items():
                        label = k.replace("_", " ").title()
                        st.markdown(f"""
                        <div style="display:flex; justify-content:space-between; padding:6px 0; border-bottom:1px solid {t['border']};">
                            <span style="color:{t['text_secondary']}; font-size:14px;">{label}</span>
                            <span style="color:{t['success']}; font-weight:700; font-family:'Cinzel',serif; font-size:14px;">{v}</span>
                        </div>
                        """, unsafe_allow_html=True)

        st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)

        # ── Row 6: Gap Analysis Cards ──
        gaps = metrics.get("gap_analysis", [])
        if gaps:
            st.markdown(f"<div class='oracle-label' style='margin-bottom:12px;'>🎴 Gap Analysis Cards</div>", unsafe_allow_html=True)
            gap_cols = st.columns(min(len(gaps), 3))
            for i, gap in enumerate(gaps):
                col_idx = i % min(len(gaps), 3)
                impact = gap.get("Impact", "Medium")
                impact_color = t['danger'] if impact == "Critical" else t['warning'] if impact == "High" else t['accent']
                gap_cols[col_idx].markdown(f"""
                <div class="gap-card">
                    <div style="font-size:10px; font-weight:700; color:{impact_color}; font-family:'Cinzel',serif; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:8px;">
                        {impact} Impact
                    </div>
                    <div style="font-size:15px; font-weight:700; color:{t['text_primary']}; font-family:'Cinzel',serif; margin-bottom:8px;">
                        {gap.get('Gap_Area', '')}
                    </div>
                    <div style="font-size:13px; color:{t['text_muted']}; margin-bottom:6px;">
                        Current: {gap.get('Current_State', '')}
                    </div>
                    <div style="font-size:13px; color:{t['accent']}; font-weight:600;">
                        → {gap.get('Agilisium_Accelerator', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)

        # ── Row 7: Market Benchmarks table ──
        benchmarks = metrics.get("market_benchmarks", [])
        if benchmarks:
            st.markdown(f"<div class='oracle-label' style='margin-bottom:12px;'>📊 Market Benchmarks</div>", unsafe_allow_html=True)
            bdf = pd.DataFrame(benchmarks)
            bdf.columns = [c.replace("_", " ").title() for c in bdf.columns]
            st.dataframe(bdf, hide_index=True, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════════
    #  Tab 2: Executive Slides — ALL 10 SLIDES
    # ══════════════════════════════════════════════════════════════════════
    with t2:
        if "slide_index" not in st.session_state:
            st.session_state["slide_index"] = 0

        total = len(pptx)
        if total == 0:
            st.info("No executive slides available for this reading.")
        else:
            idx = min(st.session_state["slide_index"], total - 1)
            slide = pptx[idx]

            # Slide card — Tarot style
            bullets_html = "".join([
                f"<li style='margin-bottom:8px; color:{t['text_primary']}; font-size:15px; font-family:Cormorant Garamond,serif;'>{b}</li>"
                for b in slide.get("bullets", [])
            ])

            st.markdown(f"""
            <div class="slide-card">
                <div style="
                    position:absolute; top:16px; right:20px;
                    font-size:11px; color:{t['accent']}; font-weight:700; letter-spacing:0.06em;
                    font-family:'Cinzel',serif;
                ">CARD {idx+1} / {total}</div>
                <div style="font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:0.12em; color:{t['accent']}; margin-bottom:10px; font-family:'Cinzel',serif;">
                    {slide.get("subtitle", "")}
                </div>
                <div style="font-size:28px; font-weight:800; color:{t['text_primary']}; letter-spacing:-0.01em; line-height:1.2; margin-bottom:10px; font-family:'Cinzel',serif;">
                    {slide.get("title", "No Title")}
                </div>
                <div style="font-size:16px; color:{t['accent']}; margin-bottom:16px; font-weight:600; font-family:'Cormorant Garamond',serif; font-style:italic;">
                    {slide.get("headline", "")}
                </div>
                <div style="font-size:15px; color:{t['text_secondary']}; margin-bottom:20px; line-height:1.7; font-family:'Cormorant Garamond',serif;">
                    {slide.get("content", "")}
                </div>
                <ul style="padding-left:20px; margin:0;">
                    {bullets_html}
                </ul>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

            # Navigation
            nc1, nc2, nc3 = st.columns([1, 3, 1])
            with nc1:
                if st.button("← Prev Card", disabled=(idx <= 0)):
                    st.session_state["slide_index"] -= 1
                    st.rerun()
            with nc2:
                st.progress((idx + 1) / total)
            with nc3:
                if st.button("Next Card →", disabled=(idx >= total - 1)):
                    st.session_state["slide_index"] += 1
                    st.rerun()

            # Visual Recommendations
            if slide.get("visual_recommendations"):
                st.markdown(f"""
                <div style="margin-top:16px; padding:12px 16px; background:{t['surface_alt']}; border-radius:8px; border-left:3px solid {t['accent']};">
                    <div style="font-size:10px; font-weight:700; color:{t['accent']}; font-family:'Cinzel',serif; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:4px;">
                        Visual Recommendation
                    </div>
                    <div style="font-size:14px; color:{t['text_secondary']}; font-family:'Cormorant Garamond',serif;">
                        {slide['visual_recommendations']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Speaker Notes & Citations
            with st.expander("📜 Speaker Notes & Citations"):
                st.markdown(f"**Notes:** {slide.get('speaker_notes', 'No notes provided.')}")
                if slide.get("citations"):
                    st.markdown("**Citations:**")
                    for c in slide["citations"]:
                        st.markdown(f"- {c}")

            # Slide overview (mini map)
            st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
            with st.expander("🗂 All Slides Overview"):
                for si, s in enumerate(pptx):
                    active = "→ " if si == idx else "  "
                    color = t['accent'] if si == idx else t['text_muted']
                    st.markdown(f"<span style='color:{color}; font-family:Cinzel,serif; font-size:13px; font-weight:{700 if si==idx else 400};'>{active}Card {si+1}: {s.get('title','Untitled')}</span>", unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════════
    #  Tab 3: 10-Page Executive Summary — FULL DOCUMENT
    # ══════════════════════════════════════════════════════════════════════
    with t3:
        st.markdown(f"""
        <div style="text-align:center; margin-bottom:28px;">
            <div class='oracle-label'>📜 COMPREHENSIVE EXECUTIVE PROPHECY</div>
            <div style="font-size:14px; color:{t['text_secondary']}; font-family:'Cormorant Garamond',serif; font-style:italic; margin-top:8px;">
                The full intelligence report as divined by the Oracle's agents.
            </div>
        </div>
        """, unsafe_allow_html=True)

        sections = [
            ("Table of Contents", pdf.get("table_of_contents"), "📋"),
            ("Executive Summary", pdf.get("executive_summary"), "✦"),
            ("Detailed Findings", pdf.get("detailed_findings"), "🔍"),
            ("Solution Mapping", pdf.get("solution_mapping"), "🗺"),
            ("Implementation Roadmap", pdf.get("implementation_roadmap"), "📅"),
            ("Methodology", pdf.get("methodology"), "⚗"),
            ("Appendices", pdf.get("appendices"), "📎"),
        ]
        for title, content, icon in sections:
            if content:
                st.markdown(f"""
                <div class="pdf-section">
                    <div style="display:flex; align-items:center; gap:10px; margin-bottom:16px;">
                        <span style="font-size:20px;">{icon}</span>
                        <span class='oracle-label' style='font-size:13px;'>{title.upper()}</span>
                    </div>
                    <div style="font-size:15px; line-height:1.8; color:{t['text_primary']}; white-space:pre-wrap; font-family:'Cormorant Garamond',serif;">
{content}</div>
                </div>
                <hr class='pdf-page-break'>
                """, unsafe_allow_html=True)

        # Download
        try:
            pdf_bytes = generate_displacement_pdf(out.get("target_account", ""), out.get("competitor_name", ""), pdf)
            st.download_button(
                label="⬇ Download Full Report (PDF)",
                data=pdf_bytes,
                file_name=f"{out.get('target_account', 'Report')}_Intelligence_Report.pdf",
                mime="application/pdf",
            )
        except Exception as e:
            st.caption(f"PDF generation unavailable: {e}")

    # ══════════════════════════════════════════════════════════════════════
    #  Tab 4: Export Specs
    # ══════════════════════════════════════════════════════════════════════
    with t4:
        e1, e2, e3 = st.columns(3)

        def spec_card(col, label, content, icon):
            col.markdown(f"""
            <div class='tarot-card'>
                <div style="font-size:20px; margin-bottom:8px;">{icon}</div>
                <div class='oracle-label' style='margin-bottom:8px;'>{label}</div>
                <div style='font-size:14px; line-height:1.7; color:{t['text_primary']}; font-family:Cormorant Garamond,serif;'>{content}</div>
            </div>
            """, unsafe_allow_html=True)

        formats_list = specs.get("formats", [])
        spec_card(e1, "SUPPORTED FORMATS", ", ".join(formats_list) if formats_list else "N/A", "📦")
        spec_card(e2, "INTEGRATION", specs.get("integration_instructions", "N/A"), "🔗")
        spec_card(e3, "QA VERIFICATION", specs.get("qa_verification", "N/A"), "✅")

    # ══════════════════════════════════════════════════════════════════════
    #  Tab 5: Implementation
    # ══════════════════════════════════════════════════════════════════════
    with t5:
        impl_items = [
            ("CROSS-FORMAT CONSISTENCY", impl.get("cross_format_consistency", "N/A"), "🔄"),
            ("USAGE RECOMMENDATIONS", impl.get("usage_recommendations", "N/A"), "📋"),
            ("NEXT STEPS", impl.get("next_steps", "N/A"), "🚀"),
        ]
        for label, content, icon in impl_items:
            st.markdown(f"""
            <div class='tarot-card'>
                <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
                    <span style="font-size:20px;">{icon}</span>
                    <span class='oracle-label'>{label}</span>
                </div>
                <div style='font-size:15px; line-height:1.8; color:{t['text_primary']}; white-space:pre-wrap; font-family:Cormorant Garamond,serif;'>
{content}</div>
            </div>
            """, unsafe_allow_html=True)


if __name__ == "__main__":
    render()
