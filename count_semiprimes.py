"""
A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers.
You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent
queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]),
where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P = [1, 4, 16], Q = [26, 10, 20]
The number of semiprimes within each of these ranges is as follows:
    (1, 26) is 10,
    (4, 10) is 4,
    (16, 20) is 0.

Write a function def solution(N, P, Q) that, given an integer N and two non-empty arrays P and Q
consisting of M integers, returns an array consisting of M elements specifying the consecutive
answers to all the queries.

For above example the function should return the values [10, 4, 0].

Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..50,000];
    M is an integer within the range [1..30,000];
    each element of arrays P and Q is an integer within the range [1..N];
    P[i] ≤ Q[i].
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def array_F(n):
    F = [0] * (n + 1)
    i = 2
    while (i * i <= n):
        if (F[i] == 0):
            k = i * i
            while (k <= n):
                if (F[k] == 0):
                    F[k] = i
                k += i
        i += 1
    return F


def is_semiprime(a, F):
    if F[a] != 0:
        return int(F[int(a / F[a])] == 0)
    return 0


def count_semiprimes(n):
    F = array_F(n)
    semi = [0] * (n + 1)
    for i in range(4, n + 1):
        semi[i] = semi[i - 1] + is_semiprime(i, F)
    return semi


def solution(N, P, Q):
    semiprimes = count_semiprimes(N)
    n_of_semiprimes = []
    for i in range(0, len(P)):
        n_of_semiprimes.append(semiprimes[Q[i]] - semiprimes[P[i] - 1])
    return n_of_semiprimes