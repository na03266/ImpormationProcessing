class KakaoAccount: #카카오 계정 살펴보기
    KAKAO_SECRET = "KA_SECRET"

    def __init__(self, id, password, name, email):
        self.id = id
        self.password = password
        self.name = name
        self.email = email

    def get_auth_token(self):
        # 인증 절차 생략
        print("카카오 로그인 성공")
        return self.id + KakaoAccount.KAKAO_SECRET + self.password

# 객체 생성 및 초기화
account = KakaoAccount(id="my_id", password="my_password", name="John Doe", email="john@example.com")

# 메서드 호출
auth_token = account.get_auth_token()
print(auth_token)
