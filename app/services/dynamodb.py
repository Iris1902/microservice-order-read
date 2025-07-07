from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

mongo_url = os.getenv("MONGO_URL")
client = MongoClient(mongo_url)
db = client["orders"]  # Usa la base de datos 'orders'
cart_collection = db["carts"]

def get_orders_by_user_id(user_id):
    return list(cart_collection.find({"user_id": user_id}))

def get_order_by_id(order_id):
    # Buscar por id como string
    order = cart_collection.find_one({"id": order_id})
    if order:
        return order
    # Buscar por id como número (int)
    try:
        order = cart_collection.find_one({"id": int(order_id)})
        if order:
            return order
    except (ValueError, TypeError):
        pass
    # Buscar por _id (ObjectId)
    from bson import ObjectId
    try:
        order = cart_collection.find_one({"_id": ObjectId(order_id)})
        if order:
            return order
    except Exception:
        pass
    return None
