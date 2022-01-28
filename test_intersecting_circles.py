from intersecting_circles import solution, solution2


def test_solution_0_discs():
    A = []
    assert solution(A) == 0


def test_solution_over_10000000_intersections():
    A = list(range(0, 10000))
    assert solution(A) == -1


def test_solution_nonintersecting():
    A = [0, 0]
    assert solution(A) == 0

def test_solution_random():
    A = [1, 5, 2, 1, 4, 0]
    assert solution(A) == 11


def test_solution_random_2():
    A = list(range(0, 100))
    assert solution(A) == 4950