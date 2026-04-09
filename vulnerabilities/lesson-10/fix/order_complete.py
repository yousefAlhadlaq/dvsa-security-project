import json
import urllib3
import boto3
import os
import time
import decimal
from decimal import Decimal
from boto3.dynamodb.conditions import Key, Attr

# status list
# -----------
# 100: open
# 110: payment-failed
# 120: paid
# 200: processing
# 210: shipped
# 300: delivered
# 500: cancelled
# 600: rejected

def lambda_handler(event, context):
    try:
        class DecimalEncoder(json.JSONEncoder):
            def default(self, o):
                if isinstance(o, decimal.Decimal):
                    if o % 1 > 0:
                        return float(o)
                    else:
                        return int(o)
                return super(DecimalEncoder, self).default(o)

        orderId = event["orderId"]
        dynamodb = boto3.resource('dynamodb')

        orders_table = dynamodb.Table(os.environ["ORDERS_TABLE"])
        response = orders_table.query(
            KeyConditionExpression=Key('orderId').eq(orderId)
        ).get("Items", [None])

        if not response[0]:
            res = {"status": "err", "msg": "could not find order"}
        else:
            obj = response[0]
            status = int(json.dumps(obj['orderStatus'], cls=DecimalEncoder))
            if status == 120:
                res = {"status": "ok", "msg": "order completed sucessfully"}
            else:
                res = {"status": "err", "msg": "order was already processed"}

        return res

    except KeyError as e:
        print(f"Missing required field: {e}")
        return {"status": "err", "msg": "Bad request"}

    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"status": "err", "msg": "Internal server error"}