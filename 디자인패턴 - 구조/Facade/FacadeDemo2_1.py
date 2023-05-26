"""
라이브러리 혹은 프레임워크에 간소화된 인터페이스를 제공하는 패턴이다.
    클래스의 복잡한 시스템에 간소화된 인터페이스를 제공한다.
    클래스를 직접 사용하지 않는 것이 포인트이다.
퍼사드란 건물의 대문같은 입구를 말한다.
    또 여기엔 내부 구조를 숨긴다는 의미도 내포되어 있다.
복잡한 서브 시스템을 최대한 숨겨 의존성을 최소화하는 방법이다.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_address, from_address, host, subject, message):
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(host)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print("이메일이 성공적으로 보내졌습니다.")
    except Exception as e:
        print("이메일 보내기 실패:", str(e))

if __name__ == "__main__":
    to_address = "n00nietzsche@gmail.com"
    from_address = "admin@naver.com"
    host = "127.0.0.1"

    subject = "Test Mail from Python Program"
    message = "This is a test email sent from a Python program."

    send_email(to_address, from_address, host, subject, message)
