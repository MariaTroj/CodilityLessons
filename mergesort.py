import timeit

mysetup = '''
from math import ceil

def merge_sort(m: list):
    # Base case. A list of zero or one elements is sorted, by definition.
    if len(m) <= 1:
        return m

    # Recursive case. First, divide the list into equal-sized sublists
    # consisting of the first half and second half of the list.
    # This assumes lists start at index 0.
    middle: int = ceil(len(m)/2)
    left: list = m[:middle]
    right: list = m[middle:]

    # Recursively sort both sublists.
    left = merge_sort(left)
    right = merge_sort(right)

    # Then merge the now-sorted sublists.
    return merge(left, right)


def merge(left: list, right: list):
    result: list = []

    while len(left) != 0 and len(right) != 0:
        # if left[0] <= right[0]:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

        # else:
        #     result.append(right.pop(0))


    # Either left or right may have elements left; consume them.
    # (Only one of the following loops will actually be entered.)
    result += left
    result += right

    return result
m = [0, 2, 1, 1, 4, 0, 5, -3]

'''

mycode = '''merge_sort(m)'''

print ("The time of sorting with merge_sort method:",
       timeit.timeit(setup = mysetup,
                    stmt = mycode,
                    number = 10000))

mysetup = '''m = [0, 2, 1, 1, 4, 0, 5, -3]'''
mycode = '''m.sort()'''

print ("The time of sorting with built sort method:",
       timeit.timeit(setup = mysetup,
                    stmt = mycode,
                    number = 10000))


