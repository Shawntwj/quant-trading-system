# main_dashboard.py
import streamlit as st
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import from your new structure
from portfolio import Portfolio

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
        st.header("💼 Portfolio")
        
        # Create portfolio instance
        if 'portfolio' not in st.session_state:
            st.session_state.portfolio = Portfolio()
        
        portfolio = st.session_state.portfolio
        
        # Display current cash balance
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Cash Balance", f"${portfolio.getCashBalance():,.2f}")
        
        with col2:
            st.metric("Total Value", f"${portfolio.getCashBalance():,.2f}")
            
        with col3:
            st.metric("P&L", "$0.00")
        
        # Add cash form
        st.subheader("💰 Add Cash")
        with st.form("add_cash"):
            amount = st.number_input("Amount to add", min_value=0.01, value=1000.0, step=100.0)
            if st.form_submit_button("Add Cash"):
                new_balance = portfolio.addCash(amount)
                st.success(f"Added ${amount:,.2f}. New balance: ${new_balance:,.2f}")
                st.rerun()
        
        # Portfolio operations
        st.subheader("🔧 Portfolio Operations")
        col1, col2 = st.columns(2)
        
        with col1:
            test_amount = st.number_input("Test affordability", min_value=0.01, value=50000.0)
            if st.button("Check if affordable"):
                if portfolio.canAfford(test_amount):
                    st.success(f"✅ Can afford ${test_amount:,.2f}")
                else:
                    st.error(f"❌ Cannot afford ${test_amount:,.2f}")
        
        with col2:
            st.info("More portfolio features coming soon!")
    
    elif page == "Market Analysis":
        st.header("📈 Market Analysis")
        st.info("Coming soon - Will include:")
        st.markdown("""
        - Real-time market data
        - Technical indicators
        - Price charts
        - Market sentiment
        """)
        
    elif page == "Trade Logger":
        st.header("📝 Trade Logger") 
        st.info("Coming soon - Will include:")
        st.markdown("""
        - Trade execution logging
        - Performance tracking
        - Trade history
        - Analytics dashboard
        """)

if __name__ == "__main__":
    main()