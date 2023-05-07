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

class ItemStorage(ABC):
    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def remove_item(self, item):
        pass

    @abstractmethod
    def get_all_price(self):
        pass

class DefaultItemStorage(ItemStorage):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_all_price(self):
        return sum(item.get_price() for item in self.items)

class ItemBag(DefaultItemStorage, Item):
    def __init__(self, price, name):
        super().__init__()
        self.name = name
        self.price = price

    def get_price(self):
        return self.get_all_price() + self.price

    def get_name(self):
        return self.name

class Inventory(DefaultItemStorage):
    pass

def get_price(item):
    return item.get_price()

def main():
    inventory = Inventory()
    long_sword = DefaultItem(350, "긴 검")
    inventory.add_item(long_sword)

    beginner_bag = ItemBag(100, "모험자의 가방")
    rare_sword = DefaultItem(400, "레어 검")
    unique_sword = DefaultItem(1000, "유니크 검")
    beginner_bag.add_item(rare_sword)
    beginner_bag.add_item(unique_sword)
    inventory.add_item(beginner_bag)

    print("롱소드의 가격:", get_price(long_sword))  # 롱소드의 가격: 350
    print("모험자의 가방과 내부 아이템들의 가격:", get_price(beginner_bag))  # 모험자의 가방과 내부 아이템들의 가격: 1500
    print("인벤토리 아이템 가격의 총 합계:", inventory.get_all_price())  # 인벤토리 아이템 가격의 총 합계: 1850

if __name__ == "__main__":
    main()
