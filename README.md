# quant-trading-system

## To start up application 
Use `streamlit run main_dashboard.py` to start the dashboard.

## To test application 
Use `pytest` to start the dashboard. 

## current file structure 

├── config
│   └── settings.py (368 B)
├── src
│   ├── journal
│   │   └── __init__.py (3 B)
│   ├── portfolio
│   │   ├── __init__.py (32 B)
│   │   ├── portfolio.py (411 B)
│   │   └── portfolio_tracker.py (0 B)
│   └── __init__.py (3 B)
├── test
│   ├── journal
│   ├── portfolio
│   │   ├── __init__.py (0 B)
│   │   └── test_portfolio.py (679 B)
│   └── __init__.py (3 B)
├── main_dashboard.py (896 B)
├── pytest.ini (26 B)
├── README.md (22 B)
├── requirements.txt (108 B)
└── show-tree.ps1 (2.3 KB)

## naming conventions 
- to stick to underscores for file names and camelCase for objs 
- split into src and test folder for easier readability 