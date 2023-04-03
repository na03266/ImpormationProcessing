# 서브시스템: 덧셈, 뺄셈, 곱셈, 나눗셈을 제공하는 클래스
class Adder:
    def add(self, x, y):
        return x + y

class Subtractor:
    def subtract(self, x, y):
        return x - y

class Multiplier:
    def multiply(self, x, y):
        return x * y

class Divider:
    def divide(self, x, y):
        return x / y

# 퍼싸드(Facade): 간단한 인터페이스를 제공하는 클래스
class Calculator:
    def __init__(self):
        self.adder = Adder()
        self.subtractor = Subtractor()
        self.multiplier = Multiplier()
        self.divider = Divider()

    def add(self, x, y):
        return self.adder.add(x, y)

    def subtract(self, x, y):
        return self.subtractor.subtract(x, y)

    def multiply(self, x, y):
        return self.multiplier.multiply(x, y)

    def divide(self, x, y):
        return self.divider.divide(x, y)

# 사용 예시
calculator = Calculator()
result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(5, 3)
result_multiply = calculator.multiply(5, 3)
result_divide = calculator.divide(5, 3)

print("덧셈 결과:", result_add)          # 출력 결과: 덧셈 결과: 8
print("뺄셈 결과:", result_subtract)    # 출력 결과: 뺄셈 결과: 2
print("곱셈 결과:", result_multiply)    # 출력 결과: 곱셈 결과: 15
print("나눗셈 결과:", result_divide)    # 출력 결과: 나눗셈 결과: 1.6666666666666667
