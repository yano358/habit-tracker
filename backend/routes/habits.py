from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlmodel import Session, select
from core.db import get_session
from models.Habit import Habit
from typing import List, Optional

router = APIRouter()


class HabitIn(BaseModel):
    name: str
    description: str


@router.post("", response_model=Habit)
async def create_new_habit(
    habit: HabitIn,
    session: Session = Depends(get_session),
):
    new_habit = Habit(**habit.dict())
    session.add(new_habit)
    session.commit()
    session.refresh(new_habit)

    return new_habit


@router.get("", response_model=List[Habit])
async def get_habits(
    search: Optional[str] = None,
    session: Session = Depends(get_session),
):
    habits = session.exec(select(Habit)).all()
    return habits
