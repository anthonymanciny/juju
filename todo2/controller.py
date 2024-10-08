from sqlalchemy.orm import Session
from models import Todo
from schemas import TodoCreate, TodoUpdate

def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def get_todos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Todo).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: TodoUpdate):
    db_todo = get_todo(db, todo_id)
    if db_todo:
        db_todo.title = todo.title
        db_todo.description = todo.description
        db_todo.completed = todo.completed
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo(db, todo_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
