""" 
추가 요구사항 
많은 알람 채널을 지원해야 될 필요
새로운 메세징 시스템이 지속적으로 추가되고 있어 이에 대비할 필요
"""

from abc import ABC, abstractmethod
from typing import List

class NotifierInterface(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class Notifier(NotifierInterface):
    def __init__(self):
        self.notifiers: List[NotifierInterface] = []
        self.emails: List[str] = []

    def get_emails(self) -> List[str]:
        return self.emails

    def add_notifier(self, notifier: NotifierInterface):
        self.notifiers.append(notifier)

    def remove_notifier(self, notifier: NotifierInterface):
        if notifier in self.notifiers:
            self.notifiers.remove(notifier)

    def decorate(self, notifier: NotifierInterface):
        if notifier not in self.notifiers:
            self.notifiers.append(notifier)

    def add_email(self, email: str):
        self.emails.append(email)
        print(f'이메일 "{email}" 가 성공적으로 수신 이메일 목록에 추가되었습니다.')

    def send(self, message: str):
        if not self.notifiers:
            print("등록된 NotifierInterface 가 없습니다.")
            return

        if not self.emails:
            print("등록된 수신자가 없습니다.")
            return

        for notifier in self.notifiers:
            notifier.send(message)

class NotifierBaseDecorator(NotifierInterface):
    def __init__(self, notifier: NotifierInterface):
        self.notifier = notifier

    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotifierDecorator(NotifierBaseDecorator):
    def send(self, message: str):
        for email in self.notifier.get_emails():
            print(f"[이메일 발신] \"{email}\" 로 내용: \"{message}\" 을 보냈습니다.")

class SlackNotifierDecorator(NotifierBaseDecorator):
    def send(self, message: str):
        for email in self.notifier.get_emails():
            print(f"[슬랙 메세지 발신] \"{email}\" 로 내용: \"{message}\" 을 보냈습니다.")

def main():
    notifier = Notifier()

    notifier.add_email("n00nietzsche@gmail.com")
    notifier.add_email("billgates@microsoft.com")

    # 사용자 친화적인 방법
    notifier.decorate(EmailNotifierDecorator(notifier))
    notifier.decorate(SlackNotifierDecorator(notifier))

    notifier.send("하이.")

if __name__ == "__main__":
    main()

