# backends/api/v1/endpoints/stocks.py

from fastapi import APIRouter
import asyncio

from backends.utils.Stockslist import fetch_stock, get_price,all_stocks

router = APIRouter()

@router.get("/history/{symbol}")
async def stock_history(symbol: str):
    data = await asyncio.to_thread(fetch_stock, symbol)
    return data


@router.get("/price/{symbol}")
async def stock_price(symbol: str):
    price = await asyncio.to_thread(get_price, symbol)
    return {"symbol": symbol, "price": price}

@router.get("/stocks")
async def stock():
    stocks =await asyncio.to_thread(all_stocks)
    return stocks
