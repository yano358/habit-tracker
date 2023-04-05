from sqlmodel import Field, SQLModel
from typing import Optional


class Habit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
