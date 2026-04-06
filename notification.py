from abc import ABC, abstractmethod


class NotificationPolicy(ABC):

    @abstractmethod
    def should_notify(self, event: str) -> bool:
        pass


class AlwaysNotify(NotificationPolicy):
    def should_notify(self, event: str) -> bool:
        return event in ["TASK_CREATED", "STATUS_CHANGED", "TASK_DONE"]


class NotifyOnDoneOnly(NotificationPolicy):
    def should_notify(self, event: str) -> bool:
        return event == "TASK_DONE"


class NotificationService:

    def __init__(self, policy: NotificationPolicy):
        self.policy = policy

    def notify(self, event: str):
        if self.policy.should_notify(event):
            print(f"Notificación enviada para evento: {event}")