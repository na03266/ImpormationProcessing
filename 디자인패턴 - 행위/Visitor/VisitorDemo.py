# 비지터 인터페이스
from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_animal(self, animal):
        pass

    @abstractmethod
    def visit_human(self, human):
        pass

# 동물 클래스
class Animal:
    def accept(self, visitor):
        visitor.visit_animal(self)

# 사람 클래스
class Human:
    def accept(self, visitor):
        visitor.visit_human(self)

# 소리를 내는 행동을 추가하는 비지터 클래스
class SoundVisitor(Visitor):
    def visit_animal(self, animal):
        print("동물이 소리를 내었습니다!")

    def visit_human(self, human):
        print("사람이 소리를 내었습니다!")

# 사용 예시
animal = Animal()
human = Human()

sound_visitor = SoundVisitor()

animal.accept(sound_visitor)  # 출력 결과: 동물이 소리를 내었습니다!
human.accept(sound_visitor)   # 출력 결과: 사람이 소리를 내었습니다!
