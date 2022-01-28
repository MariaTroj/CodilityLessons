# A array that represents holes in the roof (1 is a hole)
# k is number of boards

def boards(A, n_of_boards):
    n = len(A)
    beg = 1
    end = n
    result = -1
    while (beg <= end):
        mid = (beg + end) / 2
        if (check(A, mid) <= n_of_boards):
            end = mid - 1
            result = mid
        else:
            beg = mid + 1
    return result

def check(A, board_size):
    n = len(A)
    boards = 0
    last = -1
    for i in range(n):
        if A[i] == 1 and last < i:
            boards += 1
            last = i + board_size - 1
    return boards

print(boards([0, 1, 0, 1, 0], 3))