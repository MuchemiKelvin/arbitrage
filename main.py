
import asyncio
import logging
import aiohttp
from api_clients import fetch_binance_prices, fetch_coinbase_prices
from cache import PriceCache
from arbitrage_logic import detect_arbitrage
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

async def main():
    price_cache = PriceCache()
    symbols = ['BTCUSDT', 'ETHUSDT', 'LTCUSDT', 'XRPUSDT', 'BCHUSDT', 'ADAUSDT', 'DOTUSDT', 'LINKUSDT']
    async with aiohttp.ClientSession() as session:
        binance_prices = await price_cache.async_get_or_fetch(
            'binance_prices',
            lambda: fetch_binance_prices(session, symbols),
            ttl_seconds=60
        )
        coinbase_prices = await price_cache.async_get_or_fetch(
            'coinbase_prices',
            lambda: fetch_coinbase_prices(session, symbols),
            ttl_seconds=60
        )
        for symbol in symbols:
            binance_price = binance_prices.get(symbol)
            coinbase_price = coinbase_prices.get(symbol)
            detect_arbitrage(symbol, binance_price, coinbase_price)

if __name__ == "__main__":
    asyncio.run(main())
        