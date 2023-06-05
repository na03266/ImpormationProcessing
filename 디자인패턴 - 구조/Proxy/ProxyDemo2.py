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
from time import sleep

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

class PrinterRealSubject(PrintableSubject):
    def __init__(self, name: str):
        self.name = name
        self.heavy_job(f"PrinterRealSubject[{name}] 인스턴스 생성중..")

    def heavy_job(self, string: str):
        print(string)
        sleep(3)
        print("생성 완료...")

    def set_printer_name(self, name: str):
        self.name = name

    def get_printer_name(self) -> str:
        return self.name

    def print(self, string: str):
        print(string)

class PrinterProxy(PrintableSubject):
    def __init__(self, name: str):
        self.name = name
        self.real = None

    def set_printer_name(self, name: str):
        if self.real is not None:
            self.real.set_printer_name(name)
        self.name = name

    def get_printer_name(self) -> str:
        return self.name

    def print(self, string: str):
        self.realize().print(string)

    def realize(self):
        if self.real is None:
            self.real = PrinterRealSubject(self.name)
        return self.real

def main():
    p = PrinterProxy("Simple")

    # 프록시가 실행 됨
    print(p.get_printer_name())

    # realSubject가 실행 
    p.print("프린트 요청")

if __name__ == "__main__":
    main()
