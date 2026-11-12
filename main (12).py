from functools import lru_cache
import sys

calls = 0


def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_loop(n):
    if n <= 1:
        return 1

    first = 1
    second = 1

    for step in range(2, n + 1):
        result = first + second
        first = second
        second = result

    return second


for n in range(1, 7):
    print("Steps:", n, "Ways:", ways_loop(n))


calls = 0
print("Naive:", ways_naive(25), "Calls:", calls)

calls = 0
ways_memo.cache_clear()
print("Memo:", ways_memo(25), "Calls:", calls)

print("Recursion Limit:", sys.getrecursionlimit())

try:
    print("Memo for 1000:", ways_memo(1000))
except RecursionError:
    print("RecursionError")

print("Loop for 1000:", ways_loop(1000))