# 짖는 인터페이스
class Barkable:
    def bark(self):
        pass

# 동물들이 소리를 내는 인터페이스
class Soundable:
    def make_sound(self):
        pass

# 구체적으로 소리를 내는 클래스
class DogSound(Soundable):
    def make_sound(self):
        return "멍멍!"

# 강아지 클래스
class Dog(Barkable):
    def bark(self):
        return "멍멍!"

# 어댑터 클래스
class DogAdapter(Soundable):
    def __init__(self, dog):
        self.dog = dog

    def make_sound(self):
        return self.dog.bark()

# 어댑터를 사용하여 강아지를 동물들이 소리를 내는 인터페이스로 사용하기
dog = Dog()
dog_sound = DogSound()
adapter = DogAdapter(dog)

print(dog_sound.make_sound())  # 출력 결과: 멍멍!
print(adapter.make_sound())    # 출력 결과: 멍멍!
