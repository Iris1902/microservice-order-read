import strawberry
from app.services.dynamodb import get_orders_by_user_id, get_order_by_id

@strawberry.type
class Order:
    id: str
    user_id: str
    product_ids: list[str]

@strawberry.type
class Query:
    @strawberry.field
    def orders_by_user(self, user_id: str) -> list[Order]:
        orders = get_orders_by_user_id(user_id)
        return [Order(id=o['id'], user_id=o['user_id'], product_ids=o.get('product_ids', [])) for o in orders]

    @strawberry.field
    def order_by_id(self, order_id: str) -> Order | None:
        order = get_order_by_id(order_id)
        if order:
            return Order(id=order['id'], user_id=order['user_id'], product_ids=order.get('product_ids', []))
        return None

schema = strawberry.Schema(query=Query)
