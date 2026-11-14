
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="MiniTask DevOps Assessment", version="1.0.0")
TASKS: list[dict] = []

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=80)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def list_tasks():
    return {"tasks": TASKS}

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    new_task = {"id": len(TASKS) + 1, "title": task.title, "done": False}
    TASKS.append(new_task)
    return new_task
