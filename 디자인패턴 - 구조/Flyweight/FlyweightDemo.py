# 플라이웨이트 패턴을 구현한 색깔 클래스
class Color:
    def __init__(self, name):
        self.name = name

# 플라이웨이트 패턴을 관리하는 팩토리 클래스
class ColorFactory:
    colors = {}

    def get_color(self, name):
        color = self.colors.get(name)
        if color is None:
            color = Color(name)
            self.colors[name] = color
        return color

# 사용 예시
factory = ColorFactory()

color1 = factory.get_color("빨강")
color2 = factory.get_color("파랑")
color3 = factory.get_color("빨강")

print(color1 is color2)  # 출력 결과: False (서로 다른 객체)
print(color1 is color3)  # 출력 결과: True (동일한 객체, 공유됨)
