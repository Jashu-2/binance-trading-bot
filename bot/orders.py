def place_market_order(client, symbol, side, quantity):

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    return order


def place_limit_order(client, symbol, side, quantity, price):

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    return order