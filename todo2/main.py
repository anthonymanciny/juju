from fastapi import FastAPI
from database import engine, Base
from views import router as todo_router

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir as rotas de todos
app.include_router(todo_router, prefix="/api")
