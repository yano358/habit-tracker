from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, ForeignKey


class Task(SQLModel, table=True):
    __tablename__ = "task"
    id: Optional[int] = Field(primary_key=True, default=None)
    list_id: int = Field(
        sa_column=Column(ForeignKey("todo_list.id", ondelete="CASCADE"))
    )
    text: str
    created_on: datetime = Field(nullable=True, default=datetime.utcnow())
