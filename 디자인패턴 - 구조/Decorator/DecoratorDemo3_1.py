""" 
추가 요구사항 
많은 알람 채널을 지원해야될 필요
새로운 메세징 시스템이 지속적으로 추가되고 있어 이에 대비할 필요
"""

from abc import ABC, abstractmethod
from typing import List, Type, Union

class NotifierInterface(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class NotifierBaseDecorator(NotifierInterface):
    def __init__(self, notifier: 'Notifier'):
        self.notifier = notifier

    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotifierDecorator(NotifierBaseDecorator):
    def __init__(self, notifier: 'Notifier'):
        super().__init__(notifier)

    def send(self, message: str):
        for email in self.notifier.get_emails():
            print(f"[이메일 발신] \"{email}\" 로 내용: \"{message}\" 을 보냈습니다.")

class SlackNotifierDecorator(NotifierBaseDecorator):
    def __init__(self, notifier: 'Notifier'):
        super().__init__(notifier)

    def send(self, message: str):
        for email in self.notifier.get_emails():
            print(f"[슬랙 메세지 발신] \"{email}\" 로 내용: \"{message}\" 을 보냈습니다.")

class Notifier(NotifierInterface):
    def __init__(self):
        self.notifiers: List[Union[NotifierBaseDecorator, NotifierInterface]] = []
        self.emails: List[str] = []

    def get_emails(self) -> List[str]:
        return self.emails

    def add_notifier(self, notifier: NotifierInterface):
        self.notifiers.append(notifier)

    def remove_notifier(self, notifier_class: Type[NotifierBaseDecorator]):
        found_notifier = self.find_notifier(notifier_class)

        if found_notifier is not None:
            self.notifiers.remove(found_notifier)

    def find_notifier(self, notifier_class: Type[NotifierBaseDecorator]) -> Union[NotifierBaseDecorator, None]:
        for notifier in self.notifiers:
            if isinstance(notifier, notifier_class):
                return notifier

        return None

    def contain_notifier(self, notifier_class: Type[NotifierBaseDecorator]) -> bool:
        return any(isinstance(notifier, notifier_class) for notifier in self.notifiers)

    def decorate(self, decorator: Type[NotifierBaseDecorator]):
        if self.contain_notifier(decorator):
            print("이미 추가된 발신 타입입니다.")
            return

        try:
            constructor = decorator.__init__
            self.add_notifier(decorator(self))
        except Exception as e:
            print("예외 발생:", e)

    def facebook_enabled(self, bool_value: bool):
        if bool_value:
            if self.contain_notifier(FacebookNotifierDecorator):
                print("이미 활성화된 상태입니다.")
                return

            self.add_notifier(FacebookNotifierDecorator(self))
        else:
            self.remove_notifier(FacebookNotifierDecorator)

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


def main():
    notifier = Notifier()

    notifier.add_email("n00nietzsche@gmail.com")
    notifier.add_email("billgates@microsoft.com")

    # 사용자 친화적인 방법
    notifier.facebook_enabled(True)

    # 공통화를 쉽게 할 수 있는 방법
    notifier.decorate(EmailNotifierDecorator)
    notifier.decorate(SlackNotifierDecorator)

    notifier.send("하이.")

if __name__ == "__main__":
    main()
