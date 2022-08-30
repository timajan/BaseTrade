import requests


def get_data_p2p(symbol):
    data_buy = {
      "asset": f"{symbol}",
      "fiat": "UAH",
      "merchantCheck": False,
      "page": 1,
      "payTypes": [],
      "publisherType": None,
      "rows": 10,
      "tradeType": "BUY"
    }

    data_sell = {
        "asset": f"{symbol}",
        "fiat": "UAH",
        "merchantCheck": False,
        "page": 1,
        "payTypes": [],
        "publisherType": None,
        "rows": 10,
        "tradeType": "SELL",
        "transAmount": "5000"
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "123",
        "content-type": "application/json",
        "Host": "p2p.binance.com",
        "Origin": "https://p2p.binance.com",
        "Pragma": "no-cache",
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }

    req_buy = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
                            headers=headers, json=data_buy)
    req_sell = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
                             headers=headers, json=data_sell)

    # price_buy = req_buy.json().get('data')[0].get('adv').get('price')
    price_buy = req_buy.json()
    print(price_buy)
    price_sell = req_sell.json().get('data')[0].get('adv').get('price')
    return [price_buy, price_sell]


def format_data_binance_p2p():
    trade = ['USDT', 'BTC', 'BUSD', 'BNB', 'ETH']
    result = []
    for key in trade:
        for i in get_data_p2p(f'{key}'):
            result.append(i)
    return result


get_data_p2p('USDT')
