from task import Task, Priority


class TaskFactory:
    _id = 0

    @classmethod
    def create_task(cls, title: str, priority: str) -> Task:
        cls._id += 1

        try:
            priority_enum = Priority(priority)
        except ValueError:
            raise ValueError("Prioridad inválida")

        return Task(
            id=cls._id,
            title=title,
            priority=priority_enum
        )