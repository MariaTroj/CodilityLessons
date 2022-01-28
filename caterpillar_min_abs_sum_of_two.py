# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from bisect import bisect_left
from datetime import datetime
from random import shuffle

def timeit(n_of_calls):
    def inner(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            for i in range(n_of_calls):
                result = func(*args, **kwargs)
            end = datetime.now()
            delta = (end - start)/n_of_calls
            print(f'Duration of call of function {func.__name__}:'
                  f' {delta.microseconds} microseconds')
            return result
        return wrapper
    return inner


@timeit(n_of_calls = 10000)
def solution_prev(A):
    A = list(set(A))
    A.sort()
    n = len(A)
    first_positive = bisect_left(A, 0)
    if first_positive == 0:
        return A[0] * 2
    elif first_positive == n:
        return abs(A[n - 1] * 2)

    min_abs_of_two = min(abs(A[first_positive] * 2),
                         abs(A[first_positive - 1] * 2))

    for p in range(first_positive):
        prev_sum = abs(A[p] + A[first_positive])
        q = first_positive + 1

        while q < n and abs(A[p] + A[q]) <= prev_sum:
            prev_sum = abs(A[p] + A[q])
            q += 1
        min_abs_of_two = min(min_abs_of_two, prev_sum)

    return min_abs_of_two


@timeit(n_of_calls = 10000)
def solution_best(A):
    A.sort()
    if A[0] >= 0:
        return A[0] + A[0]
    if A[-1] <= 0:
        return -A[-1] - A[-1]
    front = len(A) - 1
    back = 0
    minAbs = A[-1] + A[-1]
    while back <= front:
        temp = abs(A[back] + A[front])
        if temp < minAbs:
            minAbs = temp

        if back == front:
            break
        elif abs(A[back + 1] + A[front]) <= temp:
            back += 1
        elif abs(A[back] + A[front - 1]) <= temp:
            front -= 1
        else:
            back += 1
            front -= 1
    return minAbs

A = [i for i in range(-100, 0)] + [i for i in range(101, 500)]
shuffle(A)
print(A)
print(solution_prev(A))

print(solution_best(A))