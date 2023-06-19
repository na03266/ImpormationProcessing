# AbstractFactory 인터페이스
class AbstractFactory:
    def create_operation(self):
        """IProduct를 생성하는 메서드를 정의하는 인터페이스입니다."""
        pass

# ConcreteFactoryA 클래스
class ConcreteFactoryA(AbstractFactory):
    def create_operation(self):
        """IProduct의 구체적인 구현인 ConcreteProductA를 생성합니다."""
        return ConcreteProductA()

# ConcreteFactoryB 클래스
class ConcreteFactoryB(AbstractFactory):
    def create_operation(self):
        """IProduct의 구체적인 구현인 ConcreteProductB를 생성합니다."""
        return ConcreteProductB()

# IProduct 인터페이스
class IProduct:
    pass

# ConcreteProductA 클래스
class ConcreteProductA(IProduct):
    def __init__(self):
        print("ConcreteProductA 생성")

# ConcreteProductB 클래스
class ConcreteProductB(IProduct):
    def __init__(self):
        print("ConcreteProductB 생성")

if __name__ == "__main__":
    # 공장 객체 생성 (리스트)
    factories = [
        ConcreteFactoryA(),
        ConcreteFactoryB()
    ]

    # 제품A 생성 (안에서 createOperation()와 생성 후처리 실행)
    productA = factories[0].create_operation()

    # 제품B 생성 (안에서 createOperation()와 생성 후처리 실행)
    productB = factories[1].create_operation()
