from max_double_slice_sum import max_double_slice_sum


def test_max_double_slice_sum_3_elem():
    A = [3, 2, -6]
    assert max_double_slice_sum(A) == 0


def test_max_double_slice_sum_10():
    A = [3, 2, -6, -1, 4, 5, -1, 2]
    assert max_double_slice_sum(A) == 10


def test_max_double_slice_sum_17():
    A = [3, 2, 6, -1, 4, 5, -1, 2]
    assert max_double_slice_sum(A) == 17
