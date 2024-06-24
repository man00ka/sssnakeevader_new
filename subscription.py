from abc import ABC, abstractmethod

class Subject():
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)


class Subscriber(ABC):
    def __init__(self, name: str):
        self.name = name
    @abstractmethod
    def sendNotification(self, event):
        pass

class gamestate_sub(Subscriber):
    def __init__(self, name):
        self.name = name



