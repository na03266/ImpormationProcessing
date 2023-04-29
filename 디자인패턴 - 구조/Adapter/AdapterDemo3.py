from abc import ABC, abstractmethod

class SocialNetworkAuthTarget(ABC):
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

class KakaoAccount:
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

class InflearnAccount:
    INFLEARN_SECRET = "INF_SECRET"

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

    def login(self):
        # 인증 절차 생략
        print("인프런 로그인 성공")
        return self.email + InflearnAccount.INFLEARN_SECRET + self.password

class KakaoSocialNetworkAuthAdapter(SocialNetworkAuthTarget):
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

class InflearnSocialNetworkAuthAdapter(SocialNetworkAuthTarget):
    def __init__(self, inflearn_account):
        self.inflearn_account = inflearn_account

    def get_service_name(self):
        return "INFLEARN"

    def get_user_name(self):
        return self.inflearn_account.username

    def get_secret(self):
        return InflearnAccount.INFLEARN_SECRET

    def get_token(self):
        return self.inflearn_account.login()

class SocialNetworkAuthService:
    @staticmethod
    def social_login(social_network_auth_target):
        print("소셜 로그인을 시작합니다.")
        print("이용하는 서비스:", social_network_auth_target.get_service_name())
        print("이름:", social_network_auth_target.get_user_name())
        print("토큰:", social_network_auth_target.get_token())

def main():
    # Kakao 계정 생성
    kakao_account = KakaoAccount(id="kakaoman", password="kakaopassword", email="kakaoman@kakao.com", name="카카오제이크서")

    # Inflearn 계정 생성
    inflearn_account = InflearnAccount(email="me@naver.com", password="mypassword", username="인프런제이크서")

    # SocialNetworkAuthService를 사용하여 로그인
    SocialNetworkAuthService.social_login(KakaoSocialNetworkAuthAdapter(kakao_account))
    SocialNetworkAuthService.social_login(InflearnSocialNetworkAuthAdapter(inflearn_account))

if __name__ == "__main__":
    main()