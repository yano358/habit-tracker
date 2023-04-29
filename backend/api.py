import routes.todo_list as todo_lists
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(todo_lists.router, prefix="/todo", tags=["Todo Lists"])
