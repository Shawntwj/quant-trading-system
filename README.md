# quant-trading-system

## To start up application 
Use `streamlit run main_dashboard.py` to start the dashboard.

## To test application 
Use `pytest` to start the dashboard. 

## current file structure 

```
quant-trading-system/
├── config/
│   └── settings.py
├── src/
│   ├── journal/
│   │   └── __init__.py
│   ├── portfolio/
│   │   ├── __init__.py
│   │   ├── portfolio.py
│   │   └── portfolio_tracker.py
│   └── __init__.py
├── test/
│   ├── portfolio/
│   │   ├── __init__.py
│   │   └── test_portfolio.py
│   └── __init__.py
├── main_dashboard.py
├── pytest.ini
├── README.md
└── requirements.txt
```

## naming conventions 
- to stick to underscores for file names and camelCase for objs 
- split into src and test folder for easier readability 
