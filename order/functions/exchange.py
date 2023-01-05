import requests
from django.conf import settings


def buy_from_exchange(crypto_name, price):
    """ Call an API from exchange """

    data = {
        'crypto_name': crypto_name,
        'price': price
    }
    url = settings.BUY_FROM_EXCHANGE_URL
    # response = requests.post(url=url, data=data)
    # result = response.json()
    return True


