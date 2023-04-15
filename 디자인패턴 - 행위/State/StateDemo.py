# 스테이트 인터페이스
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def switch(self, lamp):
        pass

# ON 상태 클래스
class OnState(State):
    def switch(self, lamp):
        print("램프를 끄겠습니다.")
        lamp.set_state(OffState())

# OFF 상태 클래스
class OffState(State):
    def switch(self, lamp):
        print("램프를 켭니다.")
        lamp.set_state(OnState())

# 램프 클래스
class Lamp:
    def __init__(self):
        self.state = OffState()

    def set_state(self, state):
        self.state = state

    def switch(self):
        self.state.switch(self)

# 사용 예시
lamp = Lamp()

# 램프를 켭니다.
lamp.switch()

# 램프를 끄겠습니다.
lamp.switch()

# 램프를 켭니다.
lamp.switch()
