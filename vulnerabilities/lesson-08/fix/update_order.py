import json
import boto3
import os
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
  orderId = event["orderId"]
  itemList = event["items"]
  status = 100
  userId = event["user"]
  address = "{}"

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
    res = {"status": "err", "msg": "could not find order"}
    return res

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
