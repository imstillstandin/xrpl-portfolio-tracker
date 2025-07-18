def calculate_pnl(data: dict):
    results = []

    for token in data.get("tokens", []):
        try:
            amount = float(token.get("amount"))
            buy_price = float(token.get("buy_price"))
            current_price = float(token.get("price_usd"))

            current_value = amount * current_price
            original_value = amount * buy_price
            profit_loss = current_value - original_value
            percent_change = ((current_price - buy_price) / buy_price) * 100

            results.append({
                "currency": token.get("currency"),
                "issuer": token.get("issuer"),
                "amount": amount,
                "buy_price": buy_price,
                "price_usd": current_price,
                "current_value": current_value,
                "original_value": original_value,
                "profit_loss": profit_loss,
                "percent_change": percent_change
            })
        except:
            continue

    return {"pnl": results}