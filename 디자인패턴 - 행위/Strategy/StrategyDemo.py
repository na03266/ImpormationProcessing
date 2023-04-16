# 스트레이티지 인터페이스
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

# 정액 할인 스트레이티지
class FixedDiscount(DiscountStrategy):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, price):
        return price - self.discount_amount

# 비율 할인 스트레이티지
class PercentageDiscount(DiscountStrategy):
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def apply_discount(self, price):
        return price * (1 - self.discount_rate)

# 가격 클래스
class Price:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def get_discounted_price(self, price):
        return self.strategy.apply_discount(price)

# 사용 예시
fixed_discount_strategy = FixedDiscount(1000)
percentage_discount_strategy = PercentageDiscount(0.2)

price = Price(fixed_discount_strategy)
print("할인된 가격:", price.get_discounted_price(5000))  # 출력 결과: 할인된 가격: 4000

price.set_strategy(percentage_discount_strategy)
print("할인된 가격:", price.get_discounted_price(5000))  # 출력 결과: 할인된 가격: 4000.0
