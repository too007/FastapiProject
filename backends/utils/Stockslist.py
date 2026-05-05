# backends/utils/stocks_service.py
from nsepython import *
import yfinance as yf

price_dict = {}


def fetch_stock(symbol: str):
    stock = yf.Ticker(symbol)
    df = stock.history(period="1mo")
    df.reset_index(inplace=True)
    df["Date"] = df["Date"].astype(str)
    return df.to_dict(orient="records")


def get_price(symbol: str):
    stock = yf.Ticker(symbol)
    return stock.info.get("regularMarketPrice")
stock =nse_eq_symbols()
result = {}



def all_stocks():
   
    for name in stock:
        key = name[0]
        result.setdefault(key, []).append(name)
    return result

    