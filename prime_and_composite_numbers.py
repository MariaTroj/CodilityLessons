def count_factors(N):
    factor = 1
    n_of_factors = 0
    while factor * factor < N:
        if N % factor == 0:
            n_of_factors += 2
        factor += 1
    if factor * factor == N:
        n_of_factors += 1

    return n_of_factors

