import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {elapsed_time:.6f} секунд")
        return result
    return wrapper

# Тестоввые функции:

@measure_time
def test_function_1(n):
    return sum(range(n))

@measure_time
def test_function_2(n):
    result = 0
    for i in range(n):
        result += i
    return result

# Основной код:

n = 1000000
print(f"Сума первых {n} чисел:")
result1 = test_function_1(n)
print(f"Результат: {result1}")

print()

result2 = test_function_2(n)
print(f"Результат: {result2}")