import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# ── Tarot palette ──────────────────────────────────────────────────
GOLD      = "#C9A84C"
GOLD_DARK = "#A8872E"
PURPLE    = "#7B2D8B"
MIDNIGHT  = "#1A1726"
PARCHMENT = "#F0EAD6"
EMERALD   = "#2D9B5A"


def create_circular_gauge(score, max_val=100, title="Displacement Vulnerability"):
    percent = (score / max_val) * 100
    if percent >= 80:   color = "#A83240"   # crimson omen
    elif percent >= 60: color = "#D4882A"   # amber oracle
    elif percent >= 40: color = GOLD
    else:               color = EMERALD

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'color': PARCHMENT, 'family': 'Cinzel, serif', 'size': 14}},
        number={'font': {'color': GOLD, 'family': 'Cinzel, serif', 'size': 42}},
        gauge={
            'axis': {'range': [0, max_val], 'tickcolor': PARCHMENT, 'tickfont': {'color': PARCHMENT}},
            'bar': {'color': color},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 2,
            'bordercolor': "rgba(201, 168, 76, 0.27)",
            'steps': [
                {'range': [0, max_val*0.39], 'color': 'rgba(45, 155, 90, 0.15)'},
                {'range': [max_val*0.4, max_val*0.59], 'color': 'rgba(201, 168, 76, 0.15)'},
                {'range': [max_val*0.6, max_val*0.79], 'color': 'rgba(212, 136, 42, 0.15)'},
                {'range': [max_val*0.8, max_val], 'color': 'rgba(168, 50, 64, 0.15)'}
            ]
        }
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'color': PARCHMENT, 'family': 'Cormorant Garamond, serif'},
        height=260,
        margin=dict(t=50, b=0, l=20, r=20)
    )
    return fig


def create_timeline_chart():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    probs = [2.5, 3.0, 2.8, 3.5, 4.2, 4.5, 5.5, 6.2, 6.0, 7.5, 8.2, 9.1]

    df = pd.DataFrame({'Month': months, 'Score / 10': probs})

    fig = px.line(df, x='Month', y='Score / 10', markers=True,
                  title="Vulnerability Trend (12 Months Trailing)")

    fig.update_traces(
        line=dict(color=GOLD, width=3),
        marker=dict(size=8, color=PURPLE, symbol='diamond',
                    line=dict(width=1, color=GOLD))
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'color': PARCHMENT, 'family': 'Cormorant Garamond, serif'},
        title_font={'family': 'Cinzel, serif', 'color': PARCHMENT, 'size': 14},
        xaxis=dict(showgrid=False, color=PARCHMENT, title="",
                   tickfont={'color': PARCHMENT}),
        yaxis=dict(showgrid=True, gridcolor="rgba(201, 168, 76, 0.13)", color=PARCHMENT,
                   range=[0, 100], tickfont={'color': PARCHMENT}),
        height=300,
        margin=dict(t=50, b=20, l=20, r=20)
    )
    return fig
