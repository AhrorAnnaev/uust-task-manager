from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int
    item: str

class TaskUpdate(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Новый текст задачи"
            }
        }

class TaskList(BaseModel):
    tasks: List[TaskUpdate]
