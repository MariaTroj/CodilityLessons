"""
A non-empty array A consisting of N integers is given. A triplet (X, Y, Z), such that
0 ≤ X < Y < Z < N, is called a double slice. The sum of double slice (X, Y, Z) is the total of
A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A = [3, 2, 6, -1, 4, 5, -1, 2]
contains the following example double slices:
 - double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
 - double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
 - double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write an efficient algorithm for the following assumptions:
 - N is an integer within the range [3..100,000];
 - each element of array A is an integer within the range [−10,000..10,000].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# [3,   2,   -6,   -1,   4,    5,    -1,   2] (0, 2, 6) = 10
# [0,   0,    2,    0,   0,    4,     9,   8] i = Y
# [4,   2,    8,    9,   5,    0,     0,   0]

def max_double_slice_sum(A):
    n = len(A)
    max_x = [0]*n
    xy = [0]*n
    yz = [0]*n
    max_double_slice_sum = 0

    for i in range(1, n-2):
        max_x[i] = max(0, max_x[i-1] + A[i])
        xy[i + 1] = max_x[i]

    for i in range(n-3, 0, -1):
        yz[i] = max(0, yz[i+1] + A[i+1])

    for i in range(1, n-1):
        max_double_slice_sum = max(max_double_slice_sum, (xy[i] + yz[i]))

    return max_double_slice_sum
