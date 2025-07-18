import requests

def get_wallet_nfts(address: str):
    try:
        url = f"https://api.xrpldata.com/api/v1/nfts/{address}"
        data = requests.get(url).json()

        nfts = []
        for nft in data.get("nfts", []):
            token_id = nft.get("token_id")
            collection = nft.get("collection", {}).get("name")
            img = nft.get("image", None)
            buy_price = float(nft.get("buy_price", 0))
            floor_price = float(nft.get("floor_price_usd", 0))

            nfts.append({
                "token_id": token_id,
                "collection": collection,
                "image": img,
                "buy_price": buy_price,
                "floor_price_usd": floor_price,
                "profit_loss": floor_price - buy_price,
                "percent_change": ((floor_price - buy_price) / buy_price) * 100 if buy_price else 0
            })
        return { "address": address, "nfts": nfts }

    except Exception as e:
        return {"error": str(e)}