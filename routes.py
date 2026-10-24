from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from schemas import Task, TaskUpdate, TaskList

task_router = APIRouter()
task_list = []

templates = Jinja2Templates(directory="jinja_templates")

@task_router.post("/tasks")
async def add_task(request: Request, todo: Task = Depends(Task.as_form)):
    todo.id = len(task_list) + 1
    task_list.append(todo)
    return templates.TemplateResponse("tasks_view.html", {
        "request": request,
        "todos": task_list
    })

@task_router.get("/tasks")
async def get_all_tasks(request: Request):
    return templates.TemplateResponse("tasks_view.html", {
        "request": request,
        "todos": task_list
    })

@task_router.get("/tasks/{task_id}")
async def get_task(request: Request, task_id: int = Path(..., title="ID задачи")):
    for todo in task_list:
        if todo.id == task_id:
            return templates.TemplateResponse("tasks_view.html", {
                "request": request,
                "todo": todo
            })
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача с таким ID не найдена."
    )
