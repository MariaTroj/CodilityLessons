"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N
non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn
with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at
least one common point (assuming that the discs contain their borders).

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

There are eleven (unordered) pairs of discs that intersect, namely:
 - discs 1 and 4 intersect, and both intersect with all the other discs;
 - disc 2 also intersects with discs 0 and 3.

Write a function def solution(A)  that, given an array A describing N discs as explained above,
returns the number of (unordered) pairs of intersecting discs. The function should return −1 if
the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
"""
from bisect import bisect_left, bisect_right
def solution(A):
    disc_range = [(i - A[i], i + A[i]) for i in range(0, len(A))]
    disc_range.sort(key = lambda x: x[0])
    discs_left_border = [x[0] for x in disc_range]
    discs_right_border = [x[1] for x in disc_range]
    discs_right_border.sort()
    intersections = 0

    for (left, right) in disc_range:
        disc_left_index = bisect_left(discs_left_border, left)
        discs_left_border.pop(disc_left_index)
        intersecting_on_right = bisect_right(discs_left_border, right) - disc_left_index

        disc_right_index = bisect_right(discs_right_border, right) - 1
        discs_right_border.pop(disc_right_index)
        intersecting_on_left = disc_right_index - bisect_left(discs_right_border, left)

        intersections += max(intersecting_on_left, intersecting_on_right)

        if intersections > 10000000:
            return -1

    return intersections


def count_borders(max_val, borders):
    borders_count = [0]*(max_val+2)
    for i in range(1, max_val+2):
        borders_count[i] = borders_count[i-1] + borders.count(i-1)
    return borders_count

def solution2(A):
    if len(A) < 2:
        return 0

    disc_range = [(i - A[i], i + A[i]) for i in range(0, len(A))]
    disc_range.sort(key=lambda x: x[0])
    min_val = disc_range[0][0]
    left_borders = [x[0] - min_val for x in disc_range]
    right_borders = [x[1] - min_val for x in disc_range]
    left_count = count_borders(max(right_borders), left_borders)
    right_count = count_borders(max(right_borders), right_borders)

    intersections = {}

    for i, b in enumerate(disc_range):
        l, r = b
        intersections[(l, r)] = max(0, (left_count[r] - i) - max(0, left_count[l] - i) - 1)

    disc_range.sort(key=lambda x: x[1])
    for i, b in enumerate(disc_range):
        l, r = b
        intersections[(l, r)] = max(0, intersections[(l, r)], ((right_count[r] - i) -
                                                               max(0, right_count[l] - i) - 1))

    n_of_intersections = sum(intersections.values())

    if n_of_intersections > 10000000:
        return -1

    return n_of_intersections



