import json
import boto3
import datetime
import time

def lambda_handler(event, context):
    try:
        dynamoDB = boto3.resource("dynamodb")
        table = dynamoDB.Table("")# DynamoDB Table ID
        if event['id'] != "":
            return {
                'statusCode': 200,
                'body': 'ok',
                'type': 'show',
                'headers': {
                  "Access-Control-Allow-Origin" : "*"
                }
            }
        else:
            results = table.scan()["Items"]
            results = sorted(results, key=lambda x:x['createdAt'])
            return {
                'statusCode': 200,
                'body': results,
                'type': 'index',
                'headers': {
                    "Access-Control-Allow-Origin": "*"
                }
            }
    except Exception as e:
        print(e)
