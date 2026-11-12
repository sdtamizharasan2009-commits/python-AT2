import time


def original_ways(n):
    if n <= 1:
        return 1

    return original_ways(n - 1) + original_ways(n - 2)


def redesigned_ways(n):
    if n <= 1:
        return 1

    first = 1
    second = 1

    for step in range(2, n + 1):
        result = first + second
        first = second
        second = result

    return second


n = 30

start = time.perf_counter()
original_result = original_ways(n)
original_time = time.perf_counter() - start

start = time.perf_counter()
redesigned_result = redesigned_ways(n)
redesigned_time = time.perf_counter() - start

print("Original Result:", original_result)
print("Redesigned Result:", redesigned_result)
print(f"Original Time: {original_time:.6f} seconds")
print(f"Redesigned Time: {redesigned_time:.6f} seconds")
print("Results Match:", original_result == redesigned_result)