from enum import Enum
from datetime import datetime


class TaskStatus(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Task:
    def __init__(self, id: int, title: str, priority: Priority):
        if not title:
            raise ValueError("El título no puede estar vacío")

        self.id = id
        self.title = title
        self.priority = priority
        self.status = TaskStatus.OPEN
        self.created_at = datetime.now()