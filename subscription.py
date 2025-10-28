from abc import ABC, abstractmethod


class Subject:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, event):
        for sub in self.subscribers:
            sub.send_notification(self.name, event)


class Subscriber(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def send_notification(self, event):
        pass


class GameStateSub(Subscriber):
    def __init__(self, name):
        super().__init__(name)

    def send_notification(self, event):
        pass
