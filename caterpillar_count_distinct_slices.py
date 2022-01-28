def count_distinct_slices(M, A):
    the_sum = 0
    front = back = 0
    seen = [False] * (M + 1)
    while (front < len(A) and back < len(A)):
        while (front < len(A) and seen[A[front]] != True):
            the_sum += (front - back + 1)
            seen[A[front]] = True
            front += 1
        else:
            while front < len(A) and back < len(A) and A[back] != A[front]:
                seen[A[back]] = False
                back += 1
            seen[A[back]] = False
            back += 1
    return min(the_sum, 1000000000)

print(count_distinct_slices(3, [1, 2, 1]) == 5)

def count_triangles(A):
    A.sort()
    n = len(A)
    n_of_triplets = 0
    for p in range(n - 2):
        r = p + 1
        for q in range(p + 1, n - 1):
            while r < n - 1 and A[p] + A[q] > A[r + 1]:
                r += 1
            n_of_triplets += r - q
    return n_of_triplets

print(count_triangles([5, 2, 1, 8, 10, 12]) == 4)