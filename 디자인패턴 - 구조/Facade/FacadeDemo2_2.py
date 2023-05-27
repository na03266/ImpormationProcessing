"""
개선 방법으로 기존 클라이언트 코드에서 3가지 관심사를 추출하고 그에 따른 클래스를 만들어줬다.
        메일을 보내기 위한 호스트를 설정하는 부분 (EmailHost)
        메일의 메세지를 설정하는 부분 (EmailMessage)
        메일을 보내는 부분 (EmailSender)
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailHost:
    def __init__(self, host):
        self.host = host
        self.session = None

    @property
    def session(self):
        if not self._session:
            self._session = smtplib.SMTP(self.host)
        return self._session

    def send_email(self, to_address, from_address, subject, message):
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject

        body = message
        msg.attach(MIMEText(body, 'plain'))

        try:
            self.session.sendmail(from_address, to_address, msg.as_string())
            print("이메일이 성공적으로 보내졌습니다.")
        except Exception as e:
            print("이메일 보내기 실패:", str(e))

    def close_session(self):
        if self._session:
            self._session.quit()
            self._session = None

if __name__ == "__main__":
    host = "127.0.0.1"
    email_host = EmailHost(host)

    to_address = "n00nietzsche@gmail.com"
    from_address = "admin@naver.com"
    subject = "Test Mail from Python Program"
    message = "This is a test email sent from a Python program."

    email_host.send_email(to_address, from_address, subject, message)
    email_host.close_session()

from dataclasses import dataclass
from email.mime.text import MIMEText

@dataclass
class EmailMessage:
    to: str
    from_: str
    title: str
    body: str
    host: 'EmailHost'

    def get_mime_message(self):
        message = MIMEText(self.body)
        message['From'] = self.from_
        message['To'] = self.to
        message['Subject'] = self.title
        return message
