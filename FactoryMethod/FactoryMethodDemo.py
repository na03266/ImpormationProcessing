# 동물 클래스
class Animal:
    def speak(self):
        pass

# 개 클래스
class Dog(Animal):
    def speak(self):
        return "멍멍!"

# 고양이 클래스
class Cat(Animal):
    def speak(self):
        return "야옹!"

# 팩토리 메소드
def create_animal(animal_type):
    if animal_type == "개":
        return Dog()
    elif animal_type == "고양이":
        return Cat()
    else:
        raise ValueError("지원하지 않는 동물입니다.")

# 팩토리 메소드를 사용하여 동물 객체 생성하기
animal_type = "개"
animal = create_animal(animal_type)
print(animal.speak())  # 출력 결과: 멍멍!

animal_type = "고양이"
animal = create_animal(animal_type)
print(animal.speak())  # 출력 결과: 야옹!
