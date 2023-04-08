# 커맨드 인터페이스
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# 덧셈 커맨드
class AddCommand(Command):
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        self.calculator.add(self.value)

    def undo(self):
        self.calculator.subtract(self.value)

# 뺄셈 커맨드
class SubtractCommand(Command):
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        self.calculator.subtract(self.value)

    def undo(self):
        self.calculator.add(self.value)

# 곱셈 커맨드
class MultiplyCommand(Command):
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        self.calculator.multiply(self.value)

    def undo(self):
        self.calculator.divide(self.value)

# 나눗셈 커맨드
class DivideCommand(Command):
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        self.calculator.divide(self.value)

    def undo(self):
        self.calculator.multiply(self.value)

# 계산기 클래스
class Calculator:
    def __init__(self):
        self.current_value = 0

    def add(self, value):
        self.current_value += value

    def subtract(self, value):
        self.current_value -= value

    def multiply(self, value):
        self.current_value *= value

    def divide(self, value):
        self.current_value /= value

# 사용 예시
calculator = Calculator()

commands = [
    AddCommand(calculator, 5),
    SubtractCommand(calculator, 2),
    MultiplyCommand(calculator, 3),
    DivideCommand(calculator, 2)
]

for command in commands:
    command.execute()

print("결과:", calculator.current_value)  # 출력 결과: 결과: 6

# 커맨드 취소
for command in reversed(commands):
    command.undo()

print("취소 후 결과:", calculator.current_value)  # 출력 결과: 취소 후 결과: 0
