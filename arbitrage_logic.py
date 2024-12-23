
import logging
import requests

def send_trading_signal(signal):
    api_url = 'https://your-trading-app.com/api/trading_signals'
    payload = {'signal': signal}
    headers = {'Authorization': 'Bearer your_api_token'}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.status_code

def detect_arbitrage(symbol, binance_price, coinbase_price):
    transaction_cost = 0.001  # Example transaction cost
    if binance_price and coinbase_price:
        binance_price_with_cost = binance_price * (1 + transaction_cost)
        coinbase_price_with_cost = coinbase_price * (1 - transaction_cost)
        if binance_price_with_cost < coinbase_price_with_cost:
            profit = coinbase_price_with_cost - binance_price_with_cost
            logging.info(f"Arbitrage Opportunity for {symbol}: Buy on Binance at ${binance_price:.2f} "
                         f"and sell on Coinbase at ${coinbase_price:.2f} | Profit: ${profit:.2f}")
        else:
            logging.info(f"No arbitrage opportunity for {symbol}")
        