from email_utils import EmailHost, EmailMessage, EmailSender

def main():
    host = EmailHost("127.0.0.1")
    email_message = EmailMessage(
        to="n00nietzsche@gmail.com",
        from_="admin@naver.com",
        title="안녕하세요.",
        body="내용입니다.",
        host=host
    )
    EmailSender.send(email_message)

if __name__ == "__main__":
    main()
