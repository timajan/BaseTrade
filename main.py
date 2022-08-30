from Binance.spot import get_data_spot
from Binance.p2p import format_data_binance_p2p
from Whitebit.spot import format_data_whilebit_spot

import gspread
from app import app

sa = gspread.service_account(filename='service_account.json')
sh = sa.open("Base_Trade")

wks = sh.worksheet("Data")

# Binance spot
dictionary = {
    'USDT': 'B3',
    'BTC': 'D3',
    'BUSD': 'F3',
    'BNB': 'H3',
    'ETH': 'J3',
}

for key in dictionary.keys():
    wks.update(f'{dictionary.get(key)}', get_data_spot(f'{key}UAH'))

# Binance p2p & Whilebit
wks.update('B4:K5', [format_data_binance_p2p(), format_data_whilebit_spot()])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
