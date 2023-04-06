# 원본 객체를 나타내는 클래스
class Internet:
    def connect(self, website):
        print(f"사이트 '{website}'에 접속되었습니다.")

# 프록시 역할을 수행하는 클래스
class InternetProxy:
    def __init__(self):
        self.internet = Internet()
        self.banned_sites = ["badsite1.com", "badsite2.com"]  # 차단된 사이트 리스트

    def connect(self, website):
        if website in self.banned_sites:
            print(f"차단된 사이트 '{website}'에 접속할 수 없습니다.")
        else:
            self.internet.connect(website)

# 사용 예시
proxy = InternetProxy()
proxy.connect("google.com")      # 출력 결과: 사이트 'google.com'에 접속되었습니다.
proxy.connect("badsite1.com")    # 출력 결과: 차단된 사이트 'badsite1.com'에 접속할 수 없습니다.
