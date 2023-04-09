# 추상 구문 트리 노드 클래스
from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def interpret(self):
        pass

# 숫자 노드 클래스
class NumberNode(Node):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

# 덧셈 노드 클래스
class AddNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

# 뺄셈 노드 클래스
class SubtractNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

# 인터프리터 클래스
class Interpreter:
    def __init__(self, expression):
        self.expression = expression
        self.pos = 0

    def parse(self):
        tokens = self.expression.split()
        return self._parse_expression(tokens)

    def _parse_expression(self, tokens):
        token = tokens[self.pos]
        if token.isdigit():
            self.pos += 1
            return NumberNode(int(token))
        elif token == '+':
            self.pos += 1
            left = self._parse_expression(tokens)
            right = self._parse_expression(tokens)
            return AddNode(left, right)
        elif token == '-':
            self.pos += 1
            left = self._parse_expression(tokens)
            right = self._parse_expression(tokens)
            return SubtractNode(left, right)

    def interpret(self):
        syntax_tree = self.parse()
        return syntax_tree.interpret()

# 사용 예시
interpreter = Interpreter("3 + 2 - 5")
result = interpreter.interpret()
print("결과:", result)  # 출력 결과: 결과: 0
