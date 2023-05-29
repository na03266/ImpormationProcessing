"""
개선 방법으로 기존 클라이언트 코드에서 3가지 관심사를 추출하고 그에 따른 클래스를 만들어줬다.
        메일을 보내기 위한 호스트를 설정하는 부분 (EmailHost)
        메일의 메세지를 설정하는 부분 (EmailMessage)
        메일을 보내는 부분 (EmailSender)
"""
import smtplib
from email.mime.text import MIMEText

class EmailHost:
    def __init__(self, host):
        self.host = host

class EmailMessage:
    def __init__(self, to, from_, title, body, host):
        self.to = to
        self.from_ = from_
        self.title = title
        self.body = body
        self.host = host

    def get_mime_message(self):
        message = MIMEText(self.body)
        message["To"] = self.to
        message["From"] = self.from_
        message["Subject"] = self.title
        return message

class EmailSender:
    @staticmethod
    def send(email_message):
        mime_message = email_message.get_mime_message()

        try:
            with smtplib.SMTP(email_message.host.host) as server:
                server.send_message(mime_message)
        except smtplib.SMTPException as e:
            print("메일 전송 중 오류가 발생했습니다:", e)
