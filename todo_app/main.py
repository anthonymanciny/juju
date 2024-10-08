from fastapi import FastAPI
from models.todo_model import Base
from database import engine
from views import todo_view

app = FastAPI()

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

# Inclui as rotas de todos
app.include_router(todo_view.router)

@app.get("/")
def read_root():
    return {"message": "Todo List API with FastAPI"}
