from itertools import combinations

def fib_sequence(n):
    fib = [0, 1]
    i = 2
    while fib[i - 1] <= n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib


def solution(A: list):
    A.append(1)
    n = len(A)
    fib = fib_sequence(n)
    reachable = [0]*n
    leaves = []
    if n in fib:
        return 1
    for i in range(n):
        if A[i] == 1:
            reachable[i] = 1 if i + 1 in fib else -1
            leaves.append(i)
    if len(leaves) == 1:
        return reachable[-1]
    pos = -1
    best = 100001
    for i in range(len(leaves)):
        if reachable[leaves[i]] > 0:
            if pos == -1:
                pos = leaves[i]
            for j in leaves[(i + 1) :]:
                if j - pos in fib:
                    if reachable[j] == -1:
                        reachable[j] = reachable[pos] + 1
                    else:
                        reachable[j] = min(reachable[j], reachable[pos] + 1)
                    if reachable[j] > best:
                        break
                    if j + 1 == n:
                        best = min(best, reachable[j])
            pos = -1
    return best if best != 100001 else -1



A = [0, 0, 0, 1, 1, 1]
print(solution(A) == 2)
A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
print(solution(A) == 3)
A = [1, 1, 1]
print(solution(A) == 2)



# bad performance
def my_solution(A):
    n = len(A) + 1
    fib = fib_sequence(n)
    if n in fib:
        return 1
    if set(A) == {0}:
        return -1
    leaves = [i + 1 for i in range(n - 1) if A[i] == 1]
    while leaves[0] in fib:
        leaves.pop(0)

    n_leaves = len(leaves)
    if n_leaves == 0:
        return -1
    for i in range(1, n_leaves + 1):
        comb = combinations(leaves, i)
        for c in comb:
            pos = 0
            for l in c + (n,):
                if l - pos not in fib:
                    break
                pos = l
            else:
                return len(c) + 1
    return -1