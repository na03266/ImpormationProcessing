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
        # 이곳에서 LG 팩토리의 초기화 작업을 수행합니다.
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
        # 이곳에서 현대 팩토리의 초기화 작업을 수행합니다.
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
        # 이곳에서 삼성 팩토리의 초기화 작업을 수행합니다.
        pass

    def create_motor(self):
        return SamsungMotor()

    def create_door(self):
        return SamsungDoor()

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

# Elevator 부품 클래스들
class LGMotor:
    def __init__(self):
        self.vendor = "LG"
        # LG 모터 초기화 코드 추가

class LGDoor:
    def __init__(self):
        self.vendor = "LG"
        # LG 도어 초기화 코드 추가

class HyundaiMotor:
    def __init__(self):
        self.vendor = "현대"
        # 현대 모터 초기화 코드 추가

class HyundaiDoor:
    def __init__(self):
        self.vendor = "현대"
        # 현대 도어 초기화 코드 추가

class SamsungMotor:
    def __init__(self):
        self.vendor = "삼성"
        # 삼성 모터 초기화 코드 추가

class SamsungDoor:
    def __init__(self):
        self.vendor = "삼성"
        # 삼성 도어 초기화 코드 추가

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


vendor_id = "LG"  # 원하는 업체 ID로 변경하세요
factory = ElevatorFactoryFactory.get_factory(vendor_id)

if factory:
    elevator = factory.create_elevator()
    print(f"{elevator.vendor} 엘리베이터를 생성했습니다.")
else:
    print("유효하지 않은 업체 ID입니다.")

class Client:
    @staticmethod
    def main(vendor_name):
        vendor_id = None

        # 업체 이름에 따라 VendorID를 설정합니다.
        if vendor_name.lower() == "lg":
            vendor_id = "LG"
        elif vendor_name.lower() == "samsung":
            vendor_id = "삼성"
        elif vendor_name.lower() == "hyundai":
            vendor_id = "현대"
        else:
            print("유효하지 않은 업체 이름입니다.")
            return

        factory = ElevatorFactoryFactory.get_factory(vendor_id)

        # 생성된 팩토리를 사용하여 부품 생성 및 사용
        if factory:
            motor = factory.create_motor()
            door = factory.create_door()

            # 생성된 부품들을 사용하여 엘리베이터를 조립하거나 동작시키는 등의 작업 수행
            print(f"{vendor_name} 엘리베이터 부품이 생성되었습니다.")
        else:
            print("유효하지 않은 업체 이름입니다.")


if __name__ == "__main__":
    vendor_name = "LG"  # 테스트할 업체 이름을 변경해주세요.
    Client.main(vendor_name)
