"""
컵을 판매하는 회사가 있다.
컵의 재질은 플라스틱, 유리, 종이 등이 존재한다.
컵의 색상은 빨간색, 파란색, 노란색, 초록색 등이 존재한다.
컵을 클래스화 시켜서 파이썬 프로그램에 녹여넣고 싶은데, 어떤 방식이 좋을까?
"""
# 컵 추상화 인터페이스
class Cup:
    def fill(self, liquid):
        pass

    def drink(self):
        pass

# 재질 추상화 인터페이스
class Material:
    def get_material(self):
        pass

# 컵과 재질을 연결하는 브릿지
class CupWithMaterial(Cup):
    def __init__(self, material):
        self._material = material

    def fill(self, liquid):
        print(f"The {self._material.get_material()} cup is filled with {liquid}.")

    def drink(self):
        print(f"You drank from the {self._material.get_material()} cup.")

# 플라스틱 재질 구현
class Plastic(Material):
    def get_material(self):
        return "plastic"

# 유리 재질 구현
class Glass(Material):
    def get_material(self):
        return "glass"

# 종이 재질 구현
class Paper(Material):
    def get_material(self):
        return "paper"
