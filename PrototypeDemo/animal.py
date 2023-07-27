import copy

class Animal:
    # 프로토 타입 패턴 예제 연슴을 위한 기본 클래스 정의
    def __init__(self, species):
        self.species = species

    def clone(self):
        return copy.deepcopy(self)


class Dog(Animal):#강아지 하위 클래스
    def __init__(self, name):
        super().__init__('Dog')
        self.name = name

    def clone(self):
        cloned_dog = super().clone()
        cloned_dog.name = self.name + "_clone"
        return cloned_dog


class Cat(Animal):#고양이 하위 클래스
    def __init__(self, name):
        super().__init__('Cat')
        self.name = name

    def clone(self):
        cloned_cat = super().clone()
        cloned_cat.name = self.name + "_clone"
        return cloned_cat
