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
