from fastapi import FastAPI
from fastapi.routing import APIRoute
from sqlmodel.sql.expression import Select, SelectOfScalar
from api import api_router


def simplify_operation_ids(app: FastAPI) -> None:
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


app = FastAPI()
app.include_router(api_router, prefix="/api")
simplify_operation_ids(app)

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True
