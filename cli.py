import argparse
import logging

from bot.client import BinanceClient
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logging


API_KEY = "aZ8MmIMlyezi8tn8SUJ6i0ZsdGb9zpZzMPKk8bPZ3qTXCIDL0aVkrBGxLVaUp1Yv"
API_SECRET = "5M2y38dMaT7911cWWZ7A170QtT7qU7B3xaP89HNLYlMcmfflWn1QQC834RIQlTw1"


setup_logging()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price", required=False)

args = parser.parse_args()

try:

    validate_side(args.side)
    validate_order_type(args.type)

    client = BinanceClient(API_KEY, API_SECRET).get_client()

    print("\nOrder Request Summary")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.quantity)

    if args.type == "MARKET":

        order = place_market_order(
            client,
            args.symbol,
            args.side,
            args.quantity
        )

    else:

        order = place_limit_order(
            client,
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    print("\nOrder Response")
    print("Order ID:", order["orderId"])
    print("Status:", order["status"])
    print("Executed Qty:", order["executedQty"])

    logging.info(order)

except Exception as e:

    print("Error:", e)
    logging.error(str(e))