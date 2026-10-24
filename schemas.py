from pydantic import BaseModel
from fastapi import Form
from typing import List, Optional

class Task(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)

class TaskUpdate(BaseModel):
    item: str

class TaskList(BaseModel):
    tasks: List[TaskUpdate]
