# ElevatorFactory 인터페이스
class ElevatorFactory:
    def create_motor(self):
        pass

    def create_door(self):
        pass

# 각 업체에 대한 구체적인 팩토리 클래스
class LGElevatorFactory(ElevatorFactory):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LGElevatorFactory, cls).__new__(cls)
            cls._instance._init_factory()
        return cls._instance

    def _init_factory(self):
        pass

    def create_motor(self):
        return LGMotor()

    def create_door(self):
        return LGDoor()

class HyundaiElevatorFactory(ElevatorFactory):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HyundaiElevatorFactory, cls).__new__(cls)
            cls._instance._init_factory()
        return cls._instance

    def _init_factory(self):
        pass

    def create_motor(self):
        return HyundaiMotor()

    def create_door(self):
        return HyundaiDoor()

class SamsungElevatorFactory(ElevatorFactory):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SamsungElevatorFactory, cls).__new__(cls)
            cls._instance._init_factory()
        return cls._instance

    def _init_factory(self):
        pass

    def create_motor(self):
        return SamsungMotor()

    def create_door(self):
        return SamsungDoor()

# Elevator 클래스들
class LGElevator:
    def __init__(self):
        self.vendor = VendorID.LG
        # LG 특정 엘리베이터 초기화 코드 추가

class HyundaiElevator:
    def __init__(self):
        self.vendor = VendorID.HYUNDAI
        # 현대 특정 엘리베이터 초기화 코드 추가

class SamsungElevator:
    def __init__(self):
        self.vendor = VendorID.SAMSUNG
        # 삼성 특정 엘리베이터 초기화 코드 추가

# Elevator 부품 클래스들
class LGMotor:
    def __init__(self):
        self.vendor = VendorID.LG
        # LG 모터 초기화 코드 추가

class LGDoor:
    def __init__(self):
        self.vendor = VendorID.LG
        # LG 도어 초기화 코드 추가

class HyundaiMotor:
    def __init__(self):
        self.vendor = VendorID.HYUNDAI
        # 현대 모터 초기화 코드 추가

class HyundaiDoor:
    def __init__(self):
        self.vendor = VendorID.HYUNDAI
        # 현대 도어 초기화 코드 추가

class SamsungMotor:
    def __init__(self):
        self.vendor = VendorID.SAMSUNG
        # 삼성 모터 초기화 코드 추가

class SamsungDoor:
    def __init__(self):
        self.vendor = VendorID.SAMSUNG
        # 삼성 도어 초기화 코드 추가

# Factory Method 패턴 구현
class ElevatorFactoryFactory:
    @staticmethod
    def get_factory(vendor_id):
        factory = None

        if vendor_id == VendorID.LG:
            factory = LGElevatorFactory()
        elif vendor_id == VendorID.HYUNDAI:
            factory = HyundaiElevatorFactory()
        elif vendor_id == VendorID.SAMSUNG:
            factory = SamsungElevatorFactory()

        return factory

class VendorID:
    LG = "LG"
    HYUNDAI = "현대"
    SAMSUNG = "삼성"

def main():
    vendor_name = input("업체 이름을 입력하세요 (LG, Samsung, Hyundai): ").lower()

    if vendor_name not in [VendorID.LG, VendorID.SAMSUNG, VendorID.HYUNDAI]:
        print("유효하지 않은 업체 이름입니다.")
        return

    factory = ElevatorFactoryFactory.get_factory(vendor_name)

    if factory:
        motor = factory.create_motor()
        door = factory.create_door()

        print(f"{vendor_name} 엘리베이터 부품이 생성되었습니다.")
    else:
        print("유효하지 않은 업체 이름입니다.")


if __name__ == "__main__":
    main()
