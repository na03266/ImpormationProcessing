"""
데코레이션 패턴 설명
래퍼 객체를 이용해 모듈과 비슷한 방식으로 기존 객체에 기능을 추가할 수 있다.
런타임에 객체에 '행위' 혹은 '기능'을 추가할 수 있게 해준다.
기존 객체를 '행위'를 가진 특별한 래퍼 객체 (데코레이터)에 넣어서 객체가 그 '행위'를 할 수 있게 만든다.
캐싱, 로깅, 검증과 같은 기능에 쓰일 수 있다.
"""

class Pizza:
    def pizza_name(self):
        return "피자"

class CheesePizza(Pizza):
    def pizza_name(self):
        return "치즈 " + super().pizza_name()

class BulgogiPizza(Pizza):
    def pizza_name(self):
        return "불고기 " + super().pizza_name()


from abc import ABC, abstractmethod

class PizzaService(ABC):
    @abstractmethod
    def pizza_name(self):
        pass

class DefaultPizza(PizzaService):
    def pizza_name(self):
        return "피자"


class PizzaDecorator(PizzaService, ABC):
    def __init__(self, pizza_service):
        self.pizza_service = pizza_service

    @abstractmethod
    def pizza_name(self):
        pass

class PizzaService(ABC):
    @abstractmethod
    def pizza_name(self):
        pass

class CheeseDecorator(PizzaDecorator):
    def __init__(self, pizza_service):
        super().__init__(pizza_service)

    def pizza_name(self):
        return "치즈 " + super().pizza_name()

class BulgogiDecorator(PizzaDecorator):
    def __init__(self, pizza_service):
        super().__init__(pizza_service)

    def pizza_name(self):
        return "불고기 " + super().pizza_name()
