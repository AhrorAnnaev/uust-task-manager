from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Сдать отчет по практике"
            }
        }
