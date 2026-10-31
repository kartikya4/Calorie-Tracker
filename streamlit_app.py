"""Ring Szn on Streamlit.

Ring Szn is a self-contained web app (index.html). Streamlit shows it in a
full-window frame, and everything you log is saved in your browser's storage
for this site.
"""
from pathlib import Path

import streamlit as st

APP_FILE = Path(__file__).parent / "index.html"

st.set_page_config(
    page_title="Ring Szn",
    page_icon="🟣",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own header, toolbar and padding so Ring Szn fills the window.
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], [data-testid="stToolbar"],
      [data-testid="stDecoration"], #MainMenu, footer { display: none !important; }
      .block-container, [data-testid="stMainBlockContainer"] {
        padding: 0 !important; max-width: 100% !important;
      }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      iframe[title="Ring Szn"] {
        display: block; border: 0; width: 100%;
        height: 100vh !important; height: 100dvh !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

if hasattr(st, "iframe"):
    # Current Streamlit: embeds the local HTML file with scripts and storage enabled.
    st.iframe(APP_FILE, height=900, alt="Ring Szn")
else:
    # Older Streamlit versions.
    import streamlit.components.v1 as components

    components.html(APP_FILE.read_text(encoding="utf-8"), height=900, scrolling=True)
