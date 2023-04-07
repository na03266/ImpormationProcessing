# 연락처를 검색하는 추상 클래스
class ContactSearcher:
    def __init__(self, next_searcher=None):
        self.next_searcher = next_searcher

    def search_contact(self, name):
        contact = self._search(name)
        if contact is not None:
            return contact
        elif self.next_searcher is not None:
            return self.next_searcher.search_contact(name)
        else:
            return None

    def _search(self, name):
        pass

# 구체적으로 연락처를 검색하는 클래스
class EmailSearcher(ContactSearcher):
    def _search(self, name):
        if name == "Alice":
            return "alice@example.com"
        else:
            return None

class PhoneSearcher(ContactSearcher):
    def _search(self, name):
        if name == "Bob":
            return "555-1234"
        else:
            return None

# 사용 예시
email_searcher = EmailSearcher()
phone_searcher = PhoneSearcher()

email_result = email_searcher.search_contact("Alice")
print("이메일:", email_result)  # 출력 결과: 이메일: alice@example.com

phone_result = phone_searcher.search_contact("Bob")
print("전화번호:", phone_result)  # 출력 결과: 전화번호: 555-1234

unknown_result = email_searcher.search_contact("Unknown")
print("검색 결과:", unknown_result)  # 출력 결과: 검색 결과: None
