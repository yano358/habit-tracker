from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class TodoList(SQLModel, table=True):
    __tablename__ = "todo_list"

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    created_on: datetime = Field(nullable=True, default=datetime.utcnow())
