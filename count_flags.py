def find_peaks(A):
    n = len(A)
    peaks = []
    first = n
    i = 1
    while i < n - 1:
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            first = min(i, first)
            peaks.append(i - first)
            i += 1
        i += 1
    return peaks


def find_max_n_of_flags(last_peak):
    max_n_of_flags = 1
    while max_n_of_flags ** 2 <= last_peak:
        max_n_of_flags += 1
    return max_n_of_flags


def solution(A):
    peaks = find_peaks(A)
    n_of_peaks = len(peaks)

    if n_of_peaks < 2:
        return n_of_peaks

    max_n_of_flags = find_max_n_of_flags(peaks[-1])

    for f in range(max_n_of_flags, 0, -1):
        i = 0
        count_flags = 1
        prev_peak = 0
        for peak in peaks:
            dist = peak - prev_peak
            if dist >= f:
                count_flags += 1
                prev_peak = peak
            i += 1
        if count_flags >= f:
            return f


