import json
import uuid
import boto3
import os

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
        address = event["shipping"]
        userId = event["user"]

        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(os.environ["ORDERS_TABLE"])

        response = table.get_item(
            Key={
                "orderId": orderId,
                "userId": userId
            },
            AttributesToGet=['orderStatus']
        )
        if 'Item' not in response:
            return {"status": "err", "msg": "could not find order"}

        if response["Item"]["orderStatus"] >= 200:
            return {"status": "err", "msg": "too late to update order"}

        update_expr = 'SET {} = :address'.format("address")
        response = table.update_item(
            Key={"orderId": orderId, "userId": userId},
            UpdateExpression=update_expr,
            ExpressionAttributeValues={
                ':address': address
            }
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            res = {"status": "ok", "msg": "address updated"}
        else:
            res = {"status": "err", "msg": "could not update address"}

        return res

    except KeyError as e:
        print(f"Missing required field: {e}")
        return {"status": "err", "msg": "Bad request"}

    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"status": "err", "msg": "Internal server error"}