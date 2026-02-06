from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="FastAPI project")


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


db: List[Task] = [
    Task(
        id=1, title="Learn FastAPI", description="Finish the tutorial", completed=False
    ),
    Task(id=2, title="Buy groceries", completed=True),
]


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return db


@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    if any(t.id == task.id for t in db):
        raise HTTPException(status_code=400, detail="Task id already exists.")
    db.append(task)
    return task


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    for task in db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
