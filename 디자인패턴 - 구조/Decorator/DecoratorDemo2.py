"""
데코레이션 패턴 설명
래퍼 객체를 이용해 모듈과 비슷한 방식으로 기존 객체에 기능을 추가할 수 있다.
런타임에 객체에 '행위' 혹은 '기능'을 추가할 수 있게 해준다.
기존 객체를 '행위'를 가진 특별한 래퍼 객체 (데코레이터)에 넣어서 객체가 그 '행위'를 할 수 있게 만든다.
캐싱, 로깅, 검증과 같은 기능에 쓰일 수 있다.
"""

from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def pizza_name(self):
        pass

class DefaultPizza(Pizza):
    def pizza_name(self):
        return "피자"

class PizzaDecorator(Pizza, ABC):
    def __init__(self, pizza):
        self.pizza = pizza

    @abstractmethod
    def pizza_name(self):
        pass

class CheeseDecorator(PizzaDecorator):
    def pizza_name(self):
        return "치즈 " + self.pizza.pizza_name()

class BulgogiDecorator(PizzaDecorator):
    def pizza_name(self):
        return "불고기 " + self.pizza.pizza_name()

def main():
    enabled_bulgogi = True
    enabled_cheese = True

    pizza = DefaultPizza()

    if enabled_bulgogi:
        pizza = BulgogiDecorator(pizza)

    if enabled_cheese:
        pizza = CheeseDecorator(pizza)

    print(pizza.pizza_name())

if __name__ == "__main__":
    main()
