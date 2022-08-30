from binance.client import Client
from datetime import datetime

# Getting the current date and time
dt = datetime.now()

# getting the timestamp
ts = datetime.timestamp(dt)

api_key = 'jeIT3CDRLiADGg9s7cv2uLa3kbNje1cEbQvJdG49RFmO9EBHHEyHaYMPMrvkLJOo'
api_secret = 'Cbe0q9dpDHeyd0w7aXX4U61YDlwTzcsNwHoCx8VNEgLBjXN722Qz2nvFQEoaTKuv'


# def get_data_spot(symbol):
#     client = Client(api_key, api_secret)
#     prices = client.get_avg_price(symbol=f'{symbol}')
#     return round(float(prices.get("price")), 2)

data = {
    "symbol": "USDTUAH",
    "side": "BUY",
    "type": "MARKET",
    "timestamp": f'{ts}'
}


def get_data_spot():
    client = Client(api_key, api_secret)
    prices = client.get_order(symbol="USDTUAH")
    return prices


print(get_data_spot())
