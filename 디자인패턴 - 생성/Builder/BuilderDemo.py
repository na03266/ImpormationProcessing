# 빌더 패턴을 구현한 Puppy 클래스
class Puppy:
    def __init__(self):
        self.name = None
        self.age = None
        self.breed = None

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_breed(self, breed):
        self.breed = breed

    def __str__(self):
        return f"Puppy: {self.name}, Age: {self.age}, Breed: {self.breed}"

# 빌더 클래스
class PuppyBuilder:
    def __init__(self):
        self.puppy = Puppy()

    def set_name(self, name):
        self.puppy.set_name(name)
        return self

    def set_age(self, age):
        self.puppy.set_age(age)
        return self

    def set_breed(self, breed):
        self.puppy.set_breed(breed)
        return self

    def build(self):
        return self.puppy

# 빌더 패턴을 사용하여 객체 생성하기
puppy_builder = PuppyBuilder()
puppy = puppy_builder.set_name("초코").set_age(2).set_breed("Labrador").build()
print(puppy)  # 출력 결과: Puppy: 초코, Age: 2, Breed: Labrador
