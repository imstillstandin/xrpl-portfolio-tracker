import requests
from services.price_fetcher import get_token_price, get_token_metadata

def get_wallet_tokens(address: str):
    balances_url = f"https://api.xrpscan.com/api/v1/account/{address}/balances"
    balances_response = requests.get(balances_url)
    if balances_response.status_code != 200:
        return {"error": "Failed to fetch balances"}

    tokens_raw = balances_response.json()
    tokens = []

    for token in tokens_raw:
        if token.get("currency") == "XRP":
            continue

        currency = token.get("currency")
        issuer = token.get("issuer")
        amount = float(token.get("value"))

        price = get_token_price(currency, issuer)
        meta = get_token_metadata(currency, issuer)

        tokens.append({
            "currency": currency,
            "issuer": issuer,
            "amount": amount,
            "price_usd": price,
            "name": meta.get("name", currency),
            "logo": meta.get("logo", None)
        })

    return {
        "address": address,
        "tokens": tokens
    }