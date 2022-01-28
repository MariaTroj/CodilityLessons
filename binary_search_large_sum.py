'''
You are given integers K, M and a non-empty array A consisting of N integers.
Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements.
The size of the block is any integer between 0 and N.
Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y].
The sum of empty block equals 0.
The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array
A = [2, 1, 5, 1, 2, 2, 2]
The array can be divided, for example, into the following blocks:
 - [2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
 - [2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
 - [2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
 - [2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function solution(K, M, A) that, given integers K, M and a non-empty array A
consisting of N integers, returns the minimal large sum.

Write an efficient algorithm for the following assumptions:
 - N and K are integers within the range [1..100,000];
 - M is an integer within the range [0..10,000];
 - each element of array A is an integer within the range [0..M].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from math import ceil


def solution(K, M, A):
    n = len(A)
    min_max_block_len = ceil(n/K)
    begin_sum = 0
    end_sum = M * min_max_block_len
    solution = end_sum
    while begin_sum <= end_sum:
        middle = int((begin_sum + end_sum)/2)
        s = split_A(A, middle)
        if s <= K:
            end_sum = middle - 1
            solution = middle
        else:
            begin_sum = middle + 1
    return solution

def split_A(A, max_sum):
    n = len(A)
    split = 0
    block_sum = 0
    i = 0
    while i < n:
        block_sum+= A[i]
        if block_sum > max_sum:
            if block_sum - A[i] == 0:
                return 100001
            block_sum = A[i]
            split += 1
        elif block_sum == max_sum:
            block_sum = 0
            split += 1
        i += 1
    if block_sum > max_sum:
        return 100001
    split += int(block_sum != 0)
    return split

print(solution(2, 7, [4, 1, 2, 7]) == 7 )
print(solution(2, 5, [5, 3]) == 5)
print(solution(3, 5, [2, 1, 5, 1, 2, 2, 2]) == 6)
print(solution(1, 1, [0]) == 0)
print(solution(2, 5, [3, 5]) == 5)




