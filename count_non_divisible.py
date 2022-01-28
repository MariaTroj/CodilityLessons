# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# [1, 2, 3, 6]
# [1, 1, 2, 1]
# [4, 4, 3, 4]

def solution(A):
    n = len(A)

    A_elems_count = {}
    for e in A:
        A_elems_count.setdefault(e, 0)
        A_elems_count[e] += 1

    A_elems = list(A_elems_count.keys())
    A_elems.sort()

    A_elems_nondivisors = {k: n for k in A_elems_count}

    for d in range(0, len(A_elems)):
        divisor = A_elems[d]
        for e in range(d, len(A_elems)):
            elem = A_elems[e]
            if elem % divisor == 0:
                A_elems_nondivisors[elem] -= A_elems_count[divisor]

    return [A_elems_nondivisors[e] for e in A]

A = [3, 1, 2, 3, 6]
assert solution(A) == [2, 4, 3, 2, 0]