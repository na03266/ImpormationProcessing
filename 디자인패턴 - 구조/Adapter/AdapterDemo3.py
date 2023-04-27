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


class KakaoAccount: #클라이언트 코드 구성
    def __init__(self, id, password, email, name):
        self.id = id
        self.password = password
        self.email = email
        self.name = name

class InflearnAccount:
    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

class KakaoSocialNetworkAuthAdapter(SocialNetworkAuthTarget):
    def __init__(self, kakao_account):
        self.kakao_account = kakao_account

class InflearnSocialNetworkAuthAdapter(SocialNetworkAuthTarget):
    def __init__(self, inflearn_account):
        self.inflearn_account = inflearn_account


class SocialNetworkAuthService:
    @staticmethod
    def social_login(social_network_auth_target):
        print("소셜 로그인을 시작합니다.")
        print("이용하는 서비스:", social_network_auth_target.get_service_name())
        print("이름:", social_network_auth_target.get_user_name())
        print("토큰:", social_network_auth_target.get_token())

# 파이썬에서도 main 함수를 사용하여 동일한 동작을 수행합니다.
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
