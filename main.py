from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from task_factory import TaskFactory
from notification import NotificationService, AlwaysNotify

app = FastAPI()

# DTOs
class TaskCreateRequest(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str
    assignee_id: Optional[int] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    priority: str
    status: str
    created_at: datetime


# Service
notification_service = NotificationService(AlwaysNotify())


@app.post("/tasks", response_model=TaskResponse)
def create_task(request: TaskCreateRequest):
    try:
        task = TaskFactory.create_task(
            title=request.title,
            priority=request.priority
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Strategy
    notification_service.notify("TASK_CREATED")

    return TaskResponse(
        id=task.id,
        title=task.title,
        priority=task.priority,
        status=task.status,
        created_at=task.created_at
    )


@app.get("/")
def root():
    return {"message": "API funcionando"}