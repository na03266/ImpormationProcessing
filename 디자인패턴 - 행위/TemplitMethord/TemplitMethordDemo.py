# 템플릿 메소드를 포함한 게임 캐릭터 클래스
from abc import ABC, abstractmethod

class Character(ABC):
    def create_character(self):
        self.set_name()
        self.set_health()
        self.set_attack()

    @abstractmethod
    def set_name(self):
        pass

    @abstractmethod
    def set_health(self):
        pass

    @abstractmethod
    def set_attack(self):
        pass

    def show_info(self):
        print(f"캐릭터 이름: {self.name}")
        print(f"체력: {self.health}")
        print(f"공격력: {self.attack}")


# 서브클래스: 전사
class Warrior(Character):
    def set_name(self):
        self.name = "전사"

    def set_health(self):
        self.health = 100

    def set_attack(self):
        self.attack = 30


# 서브클래스: 마법사
class Mage(Character):
    def set_name(self):
        self.name = "마법사"

    def set_health(self):
        self.health = 80

    def set_attack(self):
        self.attack = 40


# 사용 예시
warrior = Warrior()
warrior.create_character()
warrior.show_info()
print()

mage = Mage()
mage.create_character()
mage.show_info()
