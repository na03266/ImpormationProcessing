from abc import ABC, abstractmethod
#추상적인 소리 클래스 / 구체적인 소리 클래스를 나눠 표현을 달리함

# 추상 동물 종류 클래스
class AnimalType(ABC):
    def __init__(self, sound):
        self.sound = sound

    @abstractmethod
    def animal_type(self):
        pass

# 추상 소리 클래스
class Sound(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# 구체적인 동물 종류 클래스
class Dog(AnimalType):
    def animal_type(self):
        return "개"

# 구체적인 소리 클래스
class DogSound(Sound):
    def make_sound(self):
        return "멍멍!"

# 브릿지를 형성하는 클래스
class DogWithSound(AnimalType):
    def __init__(self):
        self.sound = DogSound()

    def animal_type(self):
        return self.sound.make_sound()

# 사용 예시
dog = DogWithSound()
print(dog.animal_type())  # 출력 결과: 멍멍!
