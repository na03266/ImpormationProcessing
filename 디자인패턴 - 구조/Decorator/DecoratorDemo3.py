"""
Notifier 라는 기존 클래스가 존재한다.
등록된 회원의 이메일 주소에 일괄적으로 이메일을 보내주는 역할을 한다.
클라이언트는 초기 세팅 후 Notifier 클래스의 send() 메서드를 이메일을 마음껏 보낼 수 있었다.
"""

class Notifier:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)
        print(f'이메일 "{email}" 가 성공적으로 수신 이메일 목록에 추가되었습니다.')

    def send(self, message):
        for email in self.emails:
            self.send_email(email, message)

    def send_email(self, email, message):
        print(f'이메일 주소: "{email}" 로 내용: "{message}" 을 보냈습니다.')

# 예시 실행
if __name__ == "__main__":
    notifier = Notifier()
    notifier.add_email("john@example.com")
    notifier.add_email("jane@example.com")
    notifier.send("안녕하세요! 파이썬으로 이메일을 보내는 예제입니다.")

class Notifier:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)
        print(f'이메일 "{email}" 가 성공적으로 수신 이메일 목록에 추가되었습니다.')

    def send(self, message):
        for email in self.emails:
            self.send_email(email, message)

    def send_email(self, email, message):
        print(f'이메일 주소: "{email}" 로 내용: "{message}" 을 보냈습니다.')

class Client:
    def main(self):
        notifier = Notifier()

        notifier.add_email("n00nietzsche@gmail.com")
        notifier.add_email("billgates@microsoft.com")

        notifier.send("하이.")

# 예시 실행
if __name__ == "__main__":
    client = Client()
    client.main()
