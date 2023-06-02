""" 연산자를 가능한 대로 공유시켜 메모리 낭비를 줄이는 방식 """
from abc import ABC, abstractmethod
import random

# 추상 베이스 클래스 (Abstract Base Class)
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# 구체적인 클래스 정의
class Circle(Shape):
    def __init__(self, color):
        self.color = color
        self.x = 0
        self.y = 0
        self.radius = 0

    def set_color(self, color):
        self.color = color

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_radius(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Circle [color={self.color}, x={self.x}, y={self.y}, radius={self.radius}]")

# ShapeFactory 클래스
class ShapeFactory:
    _circle_map = {}

    @classmethod
    def get_circle(cls, color):
        circle = cls._circle_map.get(color)

        if circle is None:
            circle = Circle(color)
            cls._circle_map[color] = circle
            print(f"==== 새로운 객체 생성 : {color}색 원 ====")

        return circle

def main():
    colors = ["Red", "Green", "Blue", "Yellow"]

    for _ in range(10):
        color = random.choice(colors)
        circle = ShapeFactory.get_circle(color)
        circle.set_x(random.randint(0, 100))
        circle.set_y(random.randint(0, 4))
        circle.set_radius(random.randint(0, 10))
        circle.draw()

if __name__ == "__main__":
    main()
