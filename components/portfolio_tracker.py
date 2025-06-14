# components/portfolio_tracker.py
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime
import json
import os

class PortfolioTracker:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.portfolio_file = os.path.join(data_dir, "portfolio.json")
        
        os.makedirs(data_dir, exist_ok=True)
        
        if not os.path.exists(self.portfolio_file):
            self.init_portfolio()
    
    def init_portfolio(self):
        """Initialize portfolio with 80k SGD"""
        default_portfolio = {
            "cash": 80000,
            "positions": {},
            "total_deposits": 80000,
            "currency": "SGD"
        }
        self.save_portfolio(default_portfolio)
    
    def load_portfolio(self):
        with open(self.portfolio_file, 'r') as f:
            return json.load(f)
    
    def save_portfolio(self, portfolio):
        with open(self.portfolio_file, 'w') as f:
            json.dump(portfolio, f, indent=2)
    
    def add_position(self, symbol, quantity, price, action="BUY"):
        portfolio = self.load_portfolio()
        
        if symbol not in portfolio["positions"]:
            portfolio["positions"][symbol] = {"quantity": 0, "avg_cost": 0}
        
        pos = portfolio["positions"][symbol]
        
        if action == "BUY":
            total_cost = pos["quantity"] * pos["avg_cost"] + quantity * price
            pos["quantity"] += quantity
            pos["avg_cost"] = total_cost / pos["quantity"] if pos["quantity"] > 0 else 0
            portfolio["cash"] -= quantity * price
            
        elif action == "SELL" and pos["quantity"] >= quantity:
            pos["quantity"] -= quantity
            portfolio["cash"] += quantity * price
            if pos["quantity"] == 0:
                del portfolio["positions"][symbol]
        
        self.save_portfolio(portfolio)
        return True
    
    @st.cache_data(ttl=60)
    def get_current_prices(_self, symbols):
        if not symbols:
            return {}
        try:
            data = yf.download(symbols, period="1d", interval="1m")
            prices = {}
            for symbol in symbols:
                if len(symbols) == 1:
                    prices[symbol] = data['Close'].iloc[-1] if not data.empty else 0
                else:
                    prices[symbol] = data['Close'][symbol].iloc[-1] if symbol in data['Close'].columns else 0
            return prices
        except:
            return {symbol: 0 for symbol in symbols}
    
    def calculate_portfolio_value(self):
        portfolio = self.load_portfolio()
        
        if not portfolio["positions"]:
            return {
                "total_value": portfolio["cash"],
                "cash": portfolio["cash"],
                "positions_value": 0,
                "positions": {}
            }
        
        symbols = list(portfolio["positions"].keys())
        prices = self.get_current_prices(symbols)
        
        positions_value = 0
        positions_detail = {}
        
        for symbol, pos in portfolio["positions"].items():
            current_price = prices.get(symbol, 0)
            market_value = pos["quantity"] * current_price
            unrealized_pnl = market_value - (pos["quantity"] * pos["avg_cost"])
            
            positions_detail[symbol] = {
                "quantity": pos["quantity"],
                "avg_cost": pos["avg_cost"],
                "current_price": current_price,
                "market_value": market_value,
                "unrealized_pnl": unrealized_pnl
            }
            positions_value += market_value
        
        total_value = portfolio["cash"] + positions_value
        
        return {
            "total_value": total_value,
            "cash": portfolio["cash"],
            "positions_value": positions_value,
            "positions": positions_detail
        }
    
    def render_dashboard(self):
        st.header("💼 Portfolio Tracker")
        
        portfolio_value = self.calculate_portfolio_value()
        
        # Top metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            pnl = portfolio_value['total_value'] - 80000
            st.metric("Total Value", f"${portfolio_value['total_value']:,.0f}", f"${pnl:,.0f}")
        
        with col2:
            st.metric("Cash", f"${portfolio_value['cash']:,.0f}")
        
        with col3:
            st.metric("Positions", f"${portfolio_value['positions_value']:,.0f}")
        
        # Positions table
        if portfolio_value['positions']:
            st.subheader("Current Positions")
            df = pd.DataFrame.from_dict(portfolio_value['positions'], orient='index')
            st.dataframe(df.round(2))
        
        # Add position form
        st.subheader("Add Position")
        with st.form("add_position"):
            col1, col2 = st.columns(2)
            with col1:
                symbol = st.text_input("Symbol", "SPY")
                action = st.selectbox("Action", ["BUY", "SELL"])
            with col2:
                quantity = st.number_input("Quantity", min_value=1, value=10)
                price = st.number_input("Price", min_value=0.01, value=400.0, format="%.2f")
            
            if st.form_submit_button("Execute"):
                if self.add_position(symbol.upper(), quantity, price, action):
                    st.success(f"{action} {quantity} {symbol} at ${price}")
                    st.rerun()