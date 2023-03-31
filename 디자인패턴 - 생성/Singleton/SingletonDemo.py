class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# 사용 예시
singleton_instance1 = Singleton()
singleton_instance2 = Singleton()

print(singleton_instance1 is singleton_instance2)  # 출력 결과: True
