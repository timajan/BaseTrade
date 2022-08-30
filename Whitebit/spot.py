import requests

url = "https://whitebit.com/api/v2/public/ticker"

headers = {
  'Cookie': '__cf_bm=nt_8uSPqAkNoz9M73ewL2nW9JV8dJU7YhVfwIQkf2Wo-1655909976-0-AXIE+iH7P0gAayhORLJwewHwMjj/FVQFQDqLqyfV8s5o0pXwCzfMir5999eXAcgpf4/kZ0lY8BrXN2oET5s29vI='
}

response = requests.request("GET", url, headers=headers)
pairs = ['USDT_UAH', 'BTC_UAH', 'BUSD_UAH', 'BNB_UAH', 'ETH_UAH']


def get_data():
    dictionary = {}
    for item in response.json().get('result'):
        if item.get('tradingPairs') in pairs:
            dictionary[f"{item.get('tradingPairs')}"] = [item.get('highestBid'), item.get('lowestAsk')]
    return dictionary


def format_data_whilebit_spot():
    dictionary = get_data()
    prices = []
    for key in pairs:
        try:
            for i in dictionary.get(key):
                prices.append(i)
        except TypeError:
            prices.append('-')
            prices.append('-')
    return prices

