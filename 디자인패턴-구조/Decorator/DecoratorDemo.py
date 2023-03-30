import time

# 함수 데코레이터 정의
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"함수 {func.__name__}의 실행 시간: {execution_time:.6f}초")
        return result
    return wrapper

# 데코레이터를 사용하여 함수 실행 시간 측정하기
@measure_time
def slow_function(delay):
    time.sleep(delay)

@measure_time
def fast_function():
    print("빠른 함수 실행")

# 함수 호출
slow_function(2)   # 실행 결과: 함수 slow_function의 실행 시간: 2.000XXX초
fast_function()    # 실행 결과: 빠른 함수 실행\n함수 fast_function의 실행 시간: 0.000000초
