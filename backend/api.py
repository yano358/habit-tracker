import routes.habits as habits
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(habits.router, prefix="/habits", tags=["Habits"])
