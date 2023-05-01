"""
게임에서 상점 기능을 구현하려 한다.
게임에 인벤토리가 존재하고 인벤토리에는 아이템을 넣을 수 있다.
아이템 중에는 '가방' 이라는 아이템도 있다.
가방은 인벤토리의 효율을 높여주기 위한 아이템으로 내부에 여러 개의 아이템을 더 보관할 수 있다.
가방은 일종의 미니 인벤토리 기능을 하는 아이템이다.
게임 내에서 '아이템 다 팔기' 기능을 사용하면, 가방 내부에 존재하는 아이템과 가방까지 전부 처분해주어야 한다.
'인벤토리' 내부에 '가방' 이라는 것이 깊이 제한 없이 계속 중첩될 수 있는 트리 형태가 만들어진다.
"""
from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

class DefaultItem(Item):
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name
