"""
Proxy
Subject(주체)의 역할
    Proxy 역할과 RealSubject 역할을 동일시하기 위한 인터페이스(API)를 결정합니다. 이 덕분에 클라이언트는 둘의 역할 차이를 몰라도 됩니다.
Proxy(대리인)의 역할
    Client의 요구를 할 수 있을 만큼 처리하고, 필요할 경우 RealSubject에게 처리를 맡깁니다.
RealSubject(실제의 주체)의 역할
    Proxy에서 요청이 들어왔을때 요청에 대한 응답을 합니다.

"""
from abc import ABC, abstractmethod

class PrintableSubject(ABC):
    @abstractmethod
    def set_printer_name(self, name: str):
        pass

    @abstractmethod
    def get_printer_name(self) -> str:
        pass

    @abstractmethod
    def print(self, string: str):
        pass
    