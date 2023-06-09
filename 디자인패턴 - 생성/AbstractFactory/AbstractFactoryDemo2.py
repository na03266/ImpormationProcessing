# ElevatorFactory 인터페이스
class ElevatorFactory:
    def create_elevator(self):
        pass

# 각 업체에 대한 구체적인 팩토리 클래스
class LGElevatorFactory(ElevatorFactory):
    def create_elevator(self):
        return LGElevator()

class HyundaiElevatorFactory(ElevatorFactory):
    def create_elevator(self):
        return HyundaiElevator()

class SamsungElevatorFactory(ElevatorFactory):
    def create_elevator(self):
        return SamsungElevator()

# Elevator 클래스들
class LGElevator:
    def __init__(self):
        self.vendor = "LG"
        # LG 특정 엘리베이터 초기화 코드 추가

class HyundaiElevator:
    def __init__(self):
        self.vendor = "현대"
        # 현대 특정 엘리베이터 초기화 코드 추가

class SamsungElevator:
    def __init__(self):
        self.vendor = "삼성"
        # 삼성 특정 엘리베이터 초기화 코드 추가

# Factory Method 패턴 구현
class ElevatorFactoryFactory:
    @staticmethod
    def get_factory(vendor_id):
        factory = None

        if vendor_id == "LG":
            factory = LGElevatorFactory()
        elif vendor_id == "현대":
            factory = HyundaiElevatorFactory()
        elif vendor_id == "삼성":
            factory = SamsungElevatorFactory()

        return factory
