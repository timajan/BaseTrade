import requests
import json

API_TOKEN = "bebf4578-3931-4529-aa23-51afe6e4d435"


headers = {'Authorization': f'Bearer {API_TOKEN}'}


def get_data():
    with open('config.json', 'rb') as file:
        symbols = json.load(file)['symbols']

    result = []
    for source in symbols:
        data = []
        print(f'{source}')
        for target in symbols:
            url = f"https://api.transferwise.com/v1/rates?source={source}&target={target}"
            response = requests.get(url=url, headers=headers)
            for text in response.json():
                data.append(text.get('rate'))
        result.append(data)
    return result
