import json
import os

import boto3
from botocore.exceptions import ClientError

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
        orderId = event["orderId"]
        itemList = event["items"]
        userId = event["user"]

        # FIX: Reject any item with a zero or negative quantity
        for item_id, quantity in itemList.items():
            if not isinstance(quantity, (int, float)) or quantity <= 0:
                return {"status": "err", "msg": "Invalid quantity: all items must have a positive quantity"}

        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(os.environ["ORDERS_TABLE"])

        try:
            table.update_item(
                Key={"orderId": orderId, "userId": userId},
                UpdateExpression='SET itemList = :itemList',
                ConditionExpression='orderStatus <= :maxStatus',
                ExpressionAttributeValues={
                    ':itemList': itemList,
                    ':maxStatus': 100
                }
            )
            res = {"status": "ok", "msg": "cart updated"}
        except ClientError as e:
            if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
                res = {"status": "err", "msg": "order already paid, cannot update"}
            else:
                res = {"status": "err", "msg": "could not update cart"}

        return res

    except KeyError as e:
        print(f"Missing required field: {e}")
        return {"status": "err", "msg": "Bad request"}

    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"status": "err", "msg": "Internal server error"}