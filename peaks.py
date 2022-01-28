def find_peaks(A):
    n = len(A)
    peaks = []
    i = 1
    while i < n - 1:
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)
            i += 1
        i += 1
    return peaks


def blocks(n, max_n_of_blocks):
    b = 1
    blocks = []
    while b * 2 < n:
        if b > max_n_of_blocks:
            break
        if n % b == 0:
            blocks.append(b)
        b += 1
    return blocks[::-1]


def solution(A):
    n = len(A)
    peaks = find_peaks(A)
    n_of_peaks = len(peaks)
    possible_n_of_blocks = blocks(n, n_of_peaks)
    max_n_of_blocks = 0
    for bn in possible_n_of_blocks:
        block_len = n / bn
        pi = 0

        for i in range(0, bn):
            block = (i * block_len, (i + 1) * block_len)

            if pi == n_of_peaks or peaks[pi] >= block[1]:
                break

            while peaks[pi] < block[1]:
                pi += 1
                if pi == n_of_peaks:
                    if i == bn - 1:
                        return bn
                    break

    return max_n_of_blocks

A = [1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1]
A = [1]
A = [1, 1, 1]
A = [1, 2, 1]
A = [2, 1, 2]
A = [1, 2, 3]
A = [1, 2, 1, 2, 1, 1]
A = [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1]
print(solution(A))