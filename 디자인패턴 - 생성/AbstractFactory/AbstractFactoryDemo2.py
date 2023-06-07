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
