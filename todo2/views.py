from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from controller import get_todo, get_todos, create_todo, update_todo, delete_todo
from schemas import TodoCreate, TodoUpdate, TodoResponse
from database import get_db
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/todos/", response_model=List[TodoResponse])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    todos = get_todos(db, skip=skip, limit=limit)
    return todos

@router.get("/todos/{todo_id}", response_model=TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/todos/", response_model=TodoResponse)
def create_new_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    created_todo = create_todo(db=db, todo=todo)
    if created_todo is None:
        raise HTTPException(status_code=404, detail="Todo not created")
    return JSONResponse(content={"message": "Tarefa criada com sucesso!"}, status_code=200)

@router.put("/todos/{todo_id}", response_model=TodoResponse)
def update_existing_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    updated_todo = update_todo(db=db, todo_id=todo_id, todo=todo)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not updated")
    return JSONResponse(content={"message": "Tarefa atualizada com sucesso!"}, status_code=200)

@router.delete("/todos/{todo_id}", response_model=TodoResponse)
def delete_existing_todo(todo_id: int, db: Session = Depends(get_db)):
    deleted_todo = delete_todo(db=db, todo_id=todo_id)
    if deleted_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    return JSONResponse(content={"message": "Tarefa deletada com sucesso!"}, status_code=200)
