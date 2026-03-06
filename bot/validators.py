def validate_side(side):

    valid_sides = ["BUY", "SELL"]

    if side not in valid_sides:
        raise ValueError("Invalid side. Use BUY or SELL.")


def validate_order_type(order_type):

    valid_types = ["MARKET", "LIMIT"]

    if order_type not in valid_types:
        raise ValueError("Invalid order type. Use MARKET or LIMIT.")