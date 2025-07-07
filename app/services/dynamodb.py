import boto3
import os
from dotenv import load_dotenv
load_dotenv()

dynamodb = boto3.resource(
    'dynamodb',
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN")
)

table = dynamodb.Table(os.getenv("DYNAMODB_TABLE"))

def get_orders_by_user_id(user_id):
    response = table.query(
        IndexName='user_id-index',  # Asegúrate de tener este GSI en DynamoDB
        KeyConditionExpression=boto3.dynamodb.conditions.Key('user_id').eq(user_id)
    )
    return response.get('Items', [])

def get_order_by_id(order_id):
    response = table.get_item(Key={"id": order_id})
    return response.get('Item')
