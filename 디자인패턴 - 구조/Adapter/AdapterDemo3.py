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

class InflearnAccount: # 인프런 계정정보 살펴보기
    INFLEARN_SECRET = "INF_SECRET"

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

    def login(self):
        # 인증 절차 생략
        print("인프런 로그인 성공")
        return self.email + InflearnAccount.INFLEARN_SECRET + self.password

from abc import ABC, abstractmethod

class SocialNetworkAuthTarget(ABC): #타겟 인터페이스
    @abstractmethod
    def get_service_name(self):
        pass

    @abstractmethod
    def get_user_name(self):
        pass

    @abstractmethod
    def get_secret(self):
        pass

    @abstractmethod
    def get_token(self):
        pass

class InflearnSocialNetworkAuthAdapter(SocialNetworkAuthTarget): # 인프런 어댑터 구현
    def __init__(self, inflearn_account):
        self.inflearn_account = inflearn_account

    def get_service_name(self):
        return "INFLEARN"

    def get_user_name(self):
        return self.inflearn_account.get_user_name()

    def get_secret(self):
        return InflearnAccount.INFLEARN_SECRET

    def get_token(self):
        return self.inflearn_account.login()

class KakaoSocialNetworkAuthAdapter(SocialNetworkAuthTarget): #카카오 어댑터 구현
    def __init__(self, kakao_account):
        self.kakao_account = kakao_account

    def get_service_name(self):
        return "KAKAO"

    def get_user_name(self):
        return self.kakao_account.name

    def get_secret(self):
        return KakaoAccount.KAKAO_SECRET

    def get_token(self):
        return self.kakao_account.get_auth_token()

class SocialNetworkAuthService: # 로그인 메서드 생성
    @staticmethod
    def social_login(social_network_auth_target):
        print("소셜 로그인을 시작합니다.")
        print("이용하는 서비스:", social_network_auth_target.get_service_name())
        print("이름:", social_network_auth_target.get_user_name())
        print("토큰:", social_network_auth_target.get_token())
