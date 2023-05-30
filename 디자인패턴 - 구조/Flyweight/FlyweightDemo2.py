from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Shape 인터페이스를 상속받아 구체적인 클래스를 정의합니다.
class Circle(Shape):
    def draw(self):
        print("원 그리기")

class Square(Shape):
    def draw(self):
        print("사각형 그리기")

# Shape 인터페이스의 메서드를 구현하지 않은 클래스를 정의하면 에러가 발생합니다.
# class Triangle(Shape):
#     pass

# 다음과 같이 사용할 수 있습니다.
circle = Circle()
square = Square()

circle.draw()  # 출력 결과: 원 그리기
square.draw()  # 출력 결과: 사각형 그리기
