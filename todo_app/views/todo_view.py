from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from controllers import todo_controller
from schemas import TodoCreate  # Importa o modelo Pydantic

router = APIRouter()

@router.get("/todos/")
def read_todos(db: Session = Depends(get_db)):
    return todo_controller.get_todos(db)

@router.get("/todos/{todo_id}")
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = todo_controller.get_todo_by_id(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/todos/")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return todo_controller.create_todo(db, todo.title, todo.description)

@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str, description: str, completed: bool, db: Session = Depends(get_db)):
    return todo_controller.update_todo(db, todo_id, title, description, completed)

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    return todo_controller.delete_todo(db, todo_id)
