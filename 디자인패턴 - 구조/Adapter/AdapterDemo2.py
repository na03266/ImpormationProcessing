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

"""
서로 호환되지 않는 인터페이스를 가진 클래스들을 함께 동작하도록 해주는 구조적인 패턴입니다.
주로 기존의 코드나 라이브러리를 재사용해야 할 때, 인터페이스 호환성이 없는 경우에 유용하게 활용됩니다.

구성요소

1. Target(대상) 인터페이스: 어댑터가 이용하려는 클라이언트가 사용하는 인터페이스입니다.
    클라이언트는 이 Target 인터페이스를 통해 서비스를 이용합니다.

2. Adaptee(적응자) 클래스: 이미 구현되어 있는 기존 클래스로, 
    클라이언트가 사용하려는 Target 인터페이스와는 호환되지 않는 인터페이스를 가지고 있습니다.

3. Adapter(어댑터) 클래스: Target 인터페이스를 구현하면서, 그 안에서 Adaptee 클래스의 기능을 호출하여 클라이언트가 요구하는 서비스를 제공합니다.
    즉, 어댑터 클래스는 Adaptee 클래스를 Target 인터페이스에 맞게 "적응"시켜주는 역할을 합니다.

어댑터 패턴의 주요 목적은 클라이언트가 기존의 코드나 라이브러리를 수정하지 않고도 새로운 인터페이스를 이용할 수 있도록 해주는 것입니다. 
이로써 기존 코드의 재사용성이 향상되고 유지보수 비용이 줄어듭니다. 
또한, 새로운 인터페이스를 기존 코드에 무리 없이 적용할 수 있게 되므로, 코드의 유연성과 확장성도 증가합니다.
"""
