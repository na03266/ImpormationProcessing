# 옵저버 인터페이스
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, height):
        pass

# 옵저버들의 집합을 관리하는 클래스
class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, height):
        for observer in self.observers:
            observer.update(height)

# 풍선 클래스: 높이 변화를 모니터링하는 주체
class Balloon(Subject):
    def __init__(self):
        super().__init__()
        self.height = 0

    def set_height(self, height):
        self.height = height
        self.notify_observers(height)

# 출력 옵저버 클래스
class PrintObserver(Observer):
    def update(self, height):
        print(f"풍선의 높이가 {height}m로 올라갔습니다.")

class WarningObserver(Observer):
    def update(self, height):
        if height > 100:
            print("경고: 풍선의 높이가 100m를 초과했습니다!")

# 사용 예시
balloon = Balloon()

print_observer = PrintObserver()
warning_observer = WarningObserver()

balloon.add_observer(print_observer)
balloon.add_observer(warning_observer)

balloon.set_height(50)
balloon.set_height(80)
balloon.set_height(120)
