from fastapi import FastAPI
from routes import task_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Добро пожаловать в Task Manager Ахроржона!"}

app.include_router(task_router)
