
import aiohttp
import logging

async def fetch_binance_prices(session, symbols):
    url = 'https://api.binance.com/api/v3/ticker/price'
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            return {item['symbol']: float(item['price']) for item in data if item['symbol'] in symbols}
    except Exception as e:
        logging.error(f"Error fetching Binance prices: {e}")
        return {}

async def fetch_coinbase_prices(session, symbols):
    url = 'https://api.coinbase.com/v2/prices'
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            return {item['base']: float(item['amount']) for item in data['data'] if item['base'] in symbols}
    except Exception as e:
        logging.error(f"Error fetching Coinbase prices: {e}")
        return {}
        