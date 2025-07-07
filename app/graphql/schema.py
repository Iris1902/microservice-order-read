import strawberry
from app.services.dynamodb import get_orders_by_user_id, get_order_by_id

@strawberry.type
class Order:
    id: str
    userId: str
    productIds: list[str]

@strawberry.type
class Query:
    @strawberry.field(name="ordersByUser")
    def orders_by_user(self, userId: str) -> list[Order]:
        orders = get_orders_by_user_id(userId)
        return [Order(id=str(o.get('id', o.get('_id'))), userId=o.get('userId', o.get('user_id')), productIds=o.get('productIds', o.get('product_ids', []))) for o in orders]

    @strawberry.field(name="orderById")
    def order_by_id(self, orderId: str) -> Order | None:
        order = get_order_by_id(orderId)
        if order:
            return Order(id=str(order.get('id', order.get('_id'))), userId=order.get('userId', order.get('user_id')), productIds=order.get('productIds', order.get('product_ids', [])))
        return None

schema = strawberry.Schema(query=Query)
