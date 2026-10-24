from fastapi import APIRouter, Path
from schemas import Task

task_router = APIRouter()
task_list = []

@task_router.post("/tasks")
async def add_task(task: Task) -> dict:
    task_list.append(task)
    return {"message": "Задача успешно добавлена в менеджер Ахроржона!"}

@task_router.get("/tasks")
async def get_all_tasks() -> dict:
    return {"tasks": task_list}

@task_router.get("/tasks/{task_id}")
async def get_task(
    task_id: int = Path(..., title="ID задачи для поиска", ge=1)
) -> dict:
    for task in task_list:
        if task.id == task_id:
            return {"task": task}
    return {"message": "Задача с таким ID не найдена в базе."}
