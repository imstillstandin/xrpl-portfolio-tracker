import requests
from functools import lru_cache

@lru_cache(maxsize=10)
def get_rates():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=usd&vs_currencies=aud,eur"
    try:
        data = requests.get(url).json()
        return data.get("usd", {})
    except:
        return {}

def convert_to_currency(amount: float, to: str):
    rates = get_rates()
    rate = rates.get(to.lower())
    if rate:
        return round(amount * rate, 4)
    return None