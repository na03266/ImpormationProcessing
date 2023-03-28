import copy

class Animal:
    # 프로토 타입 패턴 예제 연슴을 위한 기본 클래스 정의
    def __init__(self, species):
        self.species = species

    def clone(self):
        return copy.deepcopy(self)


class Dog(Animal):#강아지 하위 클래스(동물클래스 상속)
    def __init__(self, name):
        super().__init__('Dog')  #상위 클래스 Animal 의 생성자 호출
        self.name = name

    def clone(self):
        cloned_dog = super().clone()  #상위클래스 복제 메서드 호출
        cloned_dog.name = self.name + "_clone" # 복제된 객체 이름 수정
        return cloned_dog


class Cat(Animal):#고양이 하위 클래스 (동물 클래스 상속)
    def __init__(self, name):
        super().__init__('Cat') #상위 클래스 Animal 의 생성자 호출
        self.name = name

    def clone(self):
        cloned_cat = super().clone() #상위클래스 복제 메서드 호출
        cloned_cat.name = self.name + "_clone" # 복제된 객체 이름 수정
        return cloned_cat
