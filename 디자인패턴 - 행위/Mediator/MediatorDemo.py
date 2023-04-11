# 미디에이터 인터페이스
from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def send_message(self, sender, message):
        pass

# 구체적인 미디에이터 클래스
class ChatRoomMediator(Mediator):
    def __init__(self):
        self.users = {}

    def register_user(self, user, username):
        self.users[username] = user

    def send_message(self, sender, message):
        for username, user in self.users.items():
            if user != sender:
                user.receive_message(sender, message)

# 사용자 클래스
class User:
    def __init__(self, mediator, username):
        self.mediator = mediator
        self.username = username

    def send_message(self, message):
        self.mediator.send_message(self, message)

    def receive_message(self, sender, message):
        print(f"{self.username}이(가) {sender.username}로부터 메시지 수신: {message}")

# 사용 예시
mediator = ChatRoomMediator()

alice = User(mediator, "Alice")
bob = User(mediator, "Bob")
charlie = User(mediator, "Charlie")

mediator.register_user(alice, "Alice")
mediator.register_user(bob, "Bob")
mediator.register_user(charlie, "Charlie")

alice.send_message("안녕하세요!")    # 출력 결과: Bob이(가) Alice로부터 메시지 수신: 안녕하세요!
bob.send_message("반갑습니다!")     # 출력 결과: Alice이(가) Bob로부터 메시지 수신: 반갑습니다!
charlie.send_message("저도 참여할게요!")  # 출력 결과: Alice이(가) Charlie로부터 메시지 수신: 저도 참여할게요!
