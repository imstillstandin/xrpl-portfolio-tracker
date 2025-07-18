import requests
from functools import lru_cache

@lru_cache(maxsize=1000)
def get_token_price(currency: str, issuer: str):
    try:
        url = f"https://api.xpmarket.com/api/v1/token/{currency}:{issuer}"
        data = requests.get(url).json()
        return float(data.get("price", {}).get("USD", 0))
    except:
        return 0

@lru_cache(maxsize=1000)
def get_token_metadata(currency: str, issuer: str):
    try:
        url = f"https://api.firstledger.xyz/api/token/{currency}:{issuer}"
        data = requests.get(url).json()
        return {
            "name": data.get("name", currency),
            "logo": data.get("logoURI")
        }
    except:
        return {"name": currency, "logo": None}