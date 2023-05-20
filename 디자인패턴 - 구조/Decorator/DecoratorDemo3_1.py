""" 
추가 요구사항 
많은 알람 채널을 지원해야될 필요
새로운 메세징 시스템이 지속적으로 추가되고 있어 이에 대비할 필요
"""

from abc import ABC, abstractmethod

class NotifierInterface(ABC):
    @abstractmethod
    def send(self, message):
        pass

from typing import Type

class NotifierInterface(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class NotifierBaseDecorator(NotifierInterface):
    def __init__(self, notifier: Type[Notifier]):
        self.notifier = notifier

    @abstractmethod
    def send(self, message: str):
        pass

from typing import List, Type
from .notifier_base_decorator import NotifierBaseDecorator

class EmailNotifierDecorator(NotifierBaseDecorator):
    def __init__(self, notifier: Type[Notifier]):
        super().__init__(notifier)

    def send(self, message: str):
        for email in self.notifier.get_emails():
            print(f"[이메일 발신] \"{email}\" 로 내용: \"{message}\" 을 보냈습니다.")


class SlackNotifierDecorator(NotifierBaseDecorator):
    def __init__(self, notifier: Type[Notifier]):
        super().__init__(notifier)

    def send(self, message: str):
        for email in self.notifier.get_emails():
            print(f"[슬랙 메세지 발신] \"{email}\" 로 내용: \"{message}\" 을 보냈습니다.")
