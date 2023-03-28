from abc import ABC, abstractmethod

# 추상 동물 팩토리 인터페이스
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# 추상 동물 클래스
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# 강아지 클래스
class Dog(Animal):
    def speak(self):
        return "멍멍!"

# 고양이 클래스
class Cat(Animal):
    def speak(self):
        return "야옹!"

# 강아지 팩토리 클래스
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

# 고양이 팩토리 클래스
class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# 동물을 생성하는 추상 팩토리를 사용하는 클라이언트 코드
def create_and_speak_animal(factory):
    animal = factory.create_animal()
    print(animal.speak())

# 클라이언트 코드에서 강아지와 고양이 객체 생성 및 실행
dog_factory = DogFactory()
create_and_speak_animal(dog_factory)  # 출력 결과: 멍멍!

cat_factory = CatFactory()
create_and_speak_animal(cat_factory)  # 출력 결과: 야옹!
