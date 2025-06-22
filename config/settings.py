# config/settings.py
# Constants - UPPER_SNAKE_CASE
DEFAULT_CASH = 66000
CURRENCY = "SGD"
DATA_DIR = "data"
PORTFOLIO_FILE = "portfolio.json"

# API settings
YAHOO_FINANCE_TIMEOUT = 10
ALPHA_VANTAGE_API_KEY = "your_key_here"
MAX_API_CALLS_PER_MINUTE = 60

# Trading settings
MAX_POSITION_SIZE = 0.20  # 20% of portfolio
DEFAULT_COMMISSION = 0.005  # 0.5%