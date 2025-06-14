# main_dashboard.py
import streamlit as st
import sys
import os

# Add components to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from components import PortfolioTracker

st.set_page_config(
    page_title="Trading Dashboard",
    page_icon="📈",
    layout="wide"
)

def main():
    st.title("🚀 Trading Dashboard")
    
    # Sidebar navigation
    page = st.sidebar.selectbox(
        "Navigate",
        ["Portfolio", "Market Analysis", "Trade Logger"]
    )
    
    if page == "Portfolio":
        tracker = PortfolioTracker()
        tracker.render_dashboard()
    
    elif page == "Market Analysis":
        st.header("📈 Market Analysis")
        st.info("Coming soon")
        
    elif page == "Trade Logger":
        st.header("📝 Trade Logger") 
        st.info("Coming soon")

if __name__ == "__main__":
    main()