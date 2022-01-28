def solution(A):
    n = len(A)
    dp = [[A[0]] * (n) for _ in range(6)]
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + A[i]

    for i in range(1, n):
        for j in range(1, 6):
            if j >= i:
                dp[j][i] = dp[j - 1][i]
            else:
                dp[j][i] = max([(dp[j][i - k - 1] + A[i]) for k in range(j + 1)])

    return dp[-1][-1]

def solution2(A):
    n = len(A)
    dp = [A[0]] * n
    for i in range(1, n):
        dp[i] = dp[i - 1] + A[i]

    for i in range(1, n):
        for j in range(1, 6):
            if j < i:
                dp[i] = max([(dp[i - k - 1] + A[i]) for k in range(j + 1)])

    return dp[-1]


A = [1, -2, 0, 9, -1, -2]
solution2(A)


# val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|
def min_val(A):
    n = len(A)
    if n == 0:
        return 0

    A = sorted([abs(a) for a in A])
    sum_of_abs = sum(A)
    if A[0] > sum_of_abs/2:
        return calculate_val(A[0], sum_of_abs)

    half_sum = int(sum_of_abs/2) + 1
    dp = [0] * half_sum
    dp[A[0]] = 1
    current_sum = A[0]
    for i in range(1, n):
        number = A[i]
        if number > sum_of_abs / 2:
            return calculate_val(number, sum_of_abs)

        update_dp_with_number(number, dp, current_sum, half_sum)
        current_sum += number

    return calculate_val(find_greatest_sum(dp), sum_of_abs)


def update_dp_with_number(number, dp_array, current_sum, dp_len):
    dp_array[number] = 1
    visited = [number]
    for j in range(min(current_sum + 1, dp_len - number)):
        if j not in visited:
            if dp_array[j] != 0 and dp_array[j + number] == 0:
                dp_array[j + number] += 1
                visited.append(j + number)


def find_greatest_sum(dp_array):
    for s in range(1, len(dp_array)):
        if dp_array[-s] != 0:
            return len(dp_array) - s


def calculate_val(approx_half, total):
    return abs(2 * approx_half - total)


A = [3, 3, 3, 4, 5]
print(min_val(A))

A = [3, 3, 3, 4, 5, 1]
print(min_val(A))

A = [1, 5, 2, -2]
print(min_val(A))

A = [-1]
print(min_val(A))

A = [11, 12, 13, 14, 15, 16, 17]
print(min_val(A))
