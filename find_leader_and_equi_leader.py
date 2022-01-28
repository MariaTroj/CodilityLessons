"""
A non-empty array A consisting of N integers is given.
The leader of this array is the value that occurs in more than half of the elements of A.
An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and
A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:
 - 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
 - 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function: def solution(A) that, given a non-empty array A consisting of N integers,
returns the number of equi leaders.

For above example the function should return 2.

Write an efficient algorithm for the following assumptions:
 - N is an integer within the range [1..100,000];
 - each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def find_leader(A):
    n = len(A)
    size = 0
    for k in range(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
                candidate = -1
    if (size > 0):
        candidate = value
        counts = count_occurences(candidate, A)
        if (counts[-1] > n // 2):
            return (candidate, counts)
    return (-1, [])

def count_occurences(lead, A):
    n = len(A)
    counts = [int(A[0] == lead)] * n

    for i in range(1, n):
        counts[i] = counts[i-1] + int(A[i] == lead)

    return counts

def solution(A):
    leader, occurences = find_leader(A)

    if leader == -1 and len(occurences) == 0:
        return 0

    total_occurences = occurences[-1]
    n = len(A)
    equi_leader = 0

    for i in range(0, n-1):
        first_split_occurences = occurences[i]
        second_split_occurences = total_occurences - first_split_occurences
        if first_split_occurences > (i+1)/2 and second_split_occurences > (n-1-i)/2:
            equi_leader += 1

    return equi_leader