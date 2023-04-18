# 짖는 인터페이스
class Barkable:
    def bark(self):
        pass

# 동물들이 소리를 내는 인터페이스
class Soundable:
    def make_sound(self):
        pass

# 구체적으로 소리를 내는 클래스들
class DogSound(Soundable):
    def make_sound(self):
        return "멍멍!"

class CatSound(Soundable):
    def make_sound(self):
        return "야옹!"

class CowSound(Soundable):
    def make_sound(self):
        return "음메~"

# 강아지 클래스
class Dog(Barkable):
    def bark(self):
        return "멍멍!"

# 고양이 클래스
class Cat(Barkable):
    def bark(self):
        return "야옹!"

# 소 클래스
class Cow(Barkable):
    def bark(self):
        return "음메~"

# 어댑터 클래스
class AnimalAdapter(Soundable):
    def __init__(self, animal):
        self.animal = animal

    def make_sound(self):
        return self.animal.bark()

# 어댑터를 사용하여 다양한 동물들이 소리를 내는 인터페이스로 사용하기
dog = Dog()
cat = Cat()
cow = Cow()

dog_sound = DogSound()
cat_sound = CatSound()
cow_sound = CowSound()

dog_adapter = AnimalAdapter(dog)
cat_adapter = AnimalAdapter(cat)
cow_adapter = AnimalAdapter(cow)

print(dog_sound.make_sound())     # 출력 결과: 멍멍!
print(cat_sound.make_sound())     # 출력 결과: 야옹!
print(cow_sound.make_sound())     # 출력 결과: 음메~

print(dog_adapter.make_sound())   # 출력 결과: 멍멍!
print(cat_adapter.make_sound())   # 출력 결과: 야옹!
print(cow_adapter.make_sound())   # 출력 결과: 음메~
