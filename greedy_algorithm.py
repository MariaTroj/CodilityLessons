def greedyCanoeistA(W, k):
    N = len(W)
    light = list()
    heavy = []
    for i in range(N - 1):
        if W[i] + W[-1] <= k:
            light.append(W[i])
        else:
            heavy.append(W[i])
    heavy.append(W[-1])
    canoes = 0
    while len(light) != 0 or len(heavy) != 0:
        if len(light) > 0:
            light.pop()
        heavy.pop()
        canoes += 1
        if len(heavy) == 0 and len(light) != 0:
            heavy.append(light.pop())
        while len(heavy) > 1 and heavy[-1] + heavy[0] <= k:
            light.append(heavy.pop(0))
    return canoes

print(greedyCanoeistA([2, 4, 6, 8, 9, 10], 13))


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def non_overlaping_segments(begins, ends):
    n = len(begins)
    if n in (0, 1):
        return n

    non_overlaping_set_size = 1
    last_segment_end = ends[0]
    i = 1
    while i < n:
        while i < n and begins[i] <= last_segment_end:
            i += 1
        if i == n:
            break
        non_overlaping_set_size += 1
        last_segment_end = ends[i]

    return non_overlaping_set_size


print(non_overlaping_segments([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]) == 3)


def tie_ropes_ge_K(K, A):
    n = len(A)
    ropes = 0
    current_rope = 0
    for i in range(n):
        current_rope += A[i]
        if current_rope >= K:
            ropes += 1
            current_rope = 0
    return ropes


print(tie_ropes_ge_K(4, [1, 2, 3, 4, 1, 1,3]) == 3)