from fastapi import APIRouter, Depends
from models.todo_list import TodoList
from typing import List
from pydantic import BaseModel
from sqlmodel import Session, select
from core.db import get_db_session

router = APIRouter()


class TodoListResponse(TodoList):
    pass


class CreateTodoListRequest(BaseModel):
    name: str


@router.post("", response_model=TodoListResponse)
async def create_todo_list(
    todo_list_data: CreateTodoListRequest, db_session: Session = Depends(get_db_session)
):
    new_todo_list = TodoList(
        name=todo_list_data.name
    )  # TodoList(**todo_list_data.dict())

    db_session.add(new_todo_list)
    db_session.commit()
    db_session.refresh(new_todo_list)

    return TodoListResponse(**new_todo_list.dict())


@router.get("", response_model=List[TodoListResponse])
async def get_todo_lists(db_session: Session = Depends(get_db_session)):
    todo_lists = db_session.exec(select(TodoList)).all()
    return todo_lists
