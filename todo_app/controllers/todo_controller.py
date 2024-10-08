from sqlalchemy.orm import Session
from models.todo_model import TodoItem

def get_todos(db: Session):
    return db.query(TodoItem).all()

def get_todo_by_id(db: Session, todo_id: int):
    return db.query(TodoItem).filter(TodoItem.id == todo_id).first()

def create_todo(db: Session, title: str, description: str):
    todo_item = TodoItem(title=title, description=description)
    db.add(todo_item)
    db.commit()
    db.refresh(todo_item)
    return todo_item

def update_todo(db: Session, todo_id: int, title: str, description: str, completed: bool):
    todo_item = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if todo_item:
        todo_item.title = title
        todo_item.description = description
        todo_item.completed = completed
        db.commit()
        db.refresh(todo_item)
    return todo_item

def delete_todo(db: Session, todo_id: int):
    todo_item = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if todo_item:
        db.delete(todo_item)
        db.commit()
    return todo_item
