from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/order-read/graphql")


@app.get("/order-read/health")
def health():
    return {"status": "ok"}
