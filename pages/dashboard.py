import streamlit as st
import pandas as pd
from utils.styles import render_score_pill, get_theme
import time
import traceback
import sys
import os
import re
from utils.persistence import load_intelligence_records, save_intelligence_record, get_record_by_name

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from life_sciences_competitive_intelligence_multi_format_export_automation.crew import LifeSciencesCompetitiveIntelligenceMultiFormatExportAutomationCrew


def render():
    t = get_theme()

    # ── Page header ─────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="margin-bottom: 36px;">
        <div class='oracle-label'>🔮 TAROT CARDS DASHBOARD</div>
        <div class='oracle-title' style='color:{t["text_primary"]}'>Market Intelligence</div>
        <div class='oracle-subtitle' style='color:{t["text_secondary"]}'>Conduct research. Review the cards. Displace the incumbent.</div>
    </div>
    """, unsafe_allow_html=True)

    # ── KPI Summary Bar ─────────────────────────────────────────────────
    saved_records = load_intelligence_records()

    if saved_records:
        total = len(saved_records)
        avg_score = sum(float(r["score"]) for r in saved_records) / total
        critical = sum(1 for r in saved_records if float(r["score"]) >= 80)
        high = sum(1 for r in saved_records if 60 <= float(r["score"]) < 80)

        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Total Accounts", str(total))
        k2.metric("Avg Displacement Score", f"{avg_score:.1f}")
        k3.metric("⚡ Critical Priority", str(critical))
        k4.metric("✦ High Priority", str(high))

        st.markdown("<div style='height: 12px'></div>", unsafe_allow_html=True)

    # ── Invoke a New Reading Card ────────────────────────────────────────
    st.markdown("<div class='tarot-card'>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <div style="font-size:18px; font-weight:700; color:{t["accent"]}; font-family:'Cinzel',serif;">
            ✦ Start New Research
        </div>
        <div style="font-size:14px; color:{t["text_secondary"]}; margin-top:6px; font-family:'Cormorant Garamond',serif; font-style:italic;">
            Activate the AI research agents to generate a full displacement strategy and executive report.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    target_account = col1.text_input("Target Account", placeholder='e.g., "MedLife Systems"')
    competitor_name = col2.text_input("Incumbent / Competitor", placeholder='e.g., "Deloitte LS"')

    st.file_uploader(
        "Supporting Scrolls (optional)",
        accept_multiple_files=True,
        help="Financials, contracts, benchmarks — attach any relevant documents."
    )

    st.markdown("<div style='height: 8px'></div>", unsafe_allow_html=True)

    if st.button("Generate Intelligence Report →", use_container_width=True):
        if target_account and competitor_name:
            with st.spinner("AI agents are conducting research — verifying competitive data & solution mapping…"):
                try:
                    inputs = {"target_account": target_account, "competitor_name": competitor_name}
                    result = LifeSciencesCompetitiveIntelligenceMultiFormatExportAutomationCrew().crew().kickoff(inputs=inputs)

                    if result.pydantic:
                        output = result.pydantic.model_dump()
                    else:
                        import json
                        raw_text = result.raw.strip().replace("```json", "").replace("```", "")
                        output = json.loads(raw_text)

                    displacement_score = float(
                        output.get("dashboard_metrics_package", {})
                              .get("displacement_score", {})
                              .get("value", 0)
                    )
                    save_intelligence_record(target_account, competitor_name, displacement_score, output)

                    st.session_state["crewai_output"] = output
                    st.session_state["selected_account"] = {"name": target_account, "incumbent": competitor_name}
                    st.session_state["page"] = "displacement_detail"
                    st.rerun()
                except Exception as e:
                    st.error(f"Research process interrupted: {e}")
                    print(traceback.format_exc())
        else:
            st.warning("Please provide both a target account and an incumbent to begin research.")

    st.markdown("</div>", unsafe_allow_html=True)  # close tarot-card

    # ── Ranked Cards (Opportunities Table) ───────────────────────────────
    st.markdown("<div style='height: 28px'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="margin-bottom: 16px;">
        <div style="font-size:22px; font-weight:800; color:{t["accent"]}; font-family:'Cinzel',serif; letter-spacing:0.02em;">
            Market Research Index
        </div>
        <div style="font-size:14px; color:{t["text_secondary"]}; margin-top:6px; font-family:'Cormorant Garamond',serif; font-style:italic;">
            Past research ranked by Displacement Score — highest priority first.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if not saved_records:
        st.markdown(f"""
        <div style="background:{t["surface"]}; border:1px dashed {t["accent"]}44; border-radius:12px; padding:48px; text-align:center; color:{t["text_muted"]}; font-size:15px; font-family:'Cormorant Garamond',serif; font-style:italic;">
            No research reports have been generated yet. Start your first research above to populate the index.
        </div>
        """, unsafe_allow_html=True)
        return

    acc_df = pd.DataFrame(saved_records)

    # Header row
    st.markdown(f"""
    <div style="
        display:grid; grid-template-columns: 2fr 1.5fr 1.5fr 1.5fr 1fr 1fr;
        padding: 8px 16px;
        font-size: 10px; font-weight: 700; text-transform: uppercase;
        letter-spacing: 0.12em; color: {t["accent"]};
        font-family: 'Cinzel', serif;
    ">
        <div>Account</div><div>Incumbent</div><div>Industry</div>
        <div>Contract Value</div><div>Priority</div><div></div>
    </div>
    <hr style="border:none; border-top:1px solid {t['accent']}33; margin: 0 0 4px 0;">
    """, unsafe_allow_html=True)

    for i, row in acc_df.iterrows():
        cols = st.columns([2, 1.5, 1.5, 1.5, 1, 1])
        raw_name = str(row['account_name'])
        display_name = re.sub(r'^[*_\s]+|[*_\s]+$', '', raw_name)
        safe_key = re.sub(r'[^a-zA-Z0-9]', '_', display_name)

        cols[0].markdown(f"**{display_name}**")
        cols[1].markdown(f"<span style='color:{t['text_secondary']}'>{row['incumbent']}</span>", unsafe_allow_html=True)
        cols[2].markdown(f"<span style='color:{t['text_secondary']}'>{row['industry']}</span>", unsafe_allow_html=True)
        cols[3].markdown(f"<span style='color:{t['accent']}'>{row['value']}</span>", unsafe_allow_html=True)

        risk_val = float(row["score"])
        risk = "Critical" if risk_val >= 80 else "High" if risk_val >= 60 else "Medium" if risk_val >= 40 else "Low"
        cols[4].markdown(render_score_pill(risk), unsafe_allow_html=True)

        with cols[5]:
            if st.button("Review Details →", key=f"btn_view_{safe_key}_{i}"):
                output = get_record_by_name(row["account_name"])
                st.session_state["crewai_output"] = output
                st.session_state["selected_account"] = row.to_dict()
                st.session_state["page"] = "displacement_detail"
                st.rerun()

        st.markdown(f"<hr style='border:none; border-top:1px solid {t['border']}; margin:4px 0;'>", unsafe_allow_html=True)


if __name__ == "__main__":
    render()
