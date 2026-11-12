"""Streamlit wrapper for the multi-day backtest page.

The backtest runs entirely in the browser (index.html). This file only
embeds that page so it can be hosted on Streamlit Community Cloud.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Multi-Day Strategy Backtest", layout="wide")

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=2100, scrolling=True)
