from fastapi import APIRouter, Path, HTTPException, status
from schemas import Task, TaskUpdate, TaskList

task_router = APIRouter()
task_list = []

@task_router.post("/tasks", status_code=201)
async def add_task(task: Task) -> dict:
    task_list.append(task)
    return {"message": "Задача успешно добавлена Ахроржоном!"}

@task_router.get("/tasks", response_model=TaskList)
async def get_all_tasks() -> dict:
    return {"tasks": task_list}

@task_router.get("/tasks/{task_id}")
async def get_task(task_id: int = Path(..., title="ID задачи для поиска", ge=1)) -> dict:
    for task in task_list:
        if task.id == task_id:
            return {"task": task}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Ошибка: Задача с таким ID не найдена в базе Ахроржона."
    )

@task_router.put("/tasks/{task_id}")
async def update_task(task_data: TaskUpdate, task_id: int = Path(..., title="ID задачи для обновления")) -> dict:
    for task in task_list:
        if task.id == task_id:
            task.item = task_data.item
            return {"message": "Задача успешно обновлена!"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Ошибка: Задача с таким ID не найдена."
    )

@task_router.delete("/tasks/{task_id}")
async def delete_task(task_id: int) -> dict:
    for index in range(len(task_list)):
        if task_list[index].id == task_id:
            task_list.pop(index)
            return {"message": "Задача успешно удалена."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Ошибка: Задача с таким ID не найдена."
    )

@task_router.delete("/tasks")
async def delete_all_tasks() -> dict:
    task_list.clear()
    return {"message": "Все задачи успешно удалены."}
