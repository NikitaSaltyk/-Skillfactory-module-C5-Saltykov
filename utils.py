import requests
import json
from config import keys

class ConvertionExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}&apikey=Xe9hT2MWZR7FhqAfWq7kWSeLt1S7FMMJ')
        total_base = json.loads(r.content)['result']

        return total_base



#        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

# r = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}')