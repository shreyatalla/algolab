from exercises.lesson02_lists_loops import (
    count_down,
    count_evens,
    find_max,
    remove_duplicates,
    reverse_list,
    sum_list,
    two_sum,
)


def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([10]) == 10
    assert sum_list([-1, 1]) == 0
    assert sum_list([]) == 0


def test_count_evens():
    assert count_evens([1, 2, 4, 7]) == 2
    assert count_evens([1, 3, 5]) == 0
    assert count_evens([0, -2, 8]) == 3
    assert count_evens([]) == 0


def test_find_max():
    assert find_max([3, 9, 2]) == 9
    assert find_max([9, 3, 2]) == 9
    assert find_max([7]) == 7
    assert find_max([-5, -2, -8]) == -2
    assert find_max([]) is None


def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([5]) == [5]
    assert reverse_list([]) == []


def test_reverse_list_does_not_change_original():
    original = [1, 2, 3]
    assert reverse_list(original) == [3, 2, 1]
    assert original == [1, 2, 3]


def test_count_down():
    assert count_down(3) == [3, 2, 1]
    assert count_down(1) == [1]
    assert count_down(0) == []


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 1, 3, 2]) == [1, 2, 3]
    assert remove_duplicates([4, 4, 4]) == [4]
    assert remove_duplicates([3, 1, 2]) == [3, 1, 2]
    assert remove_duplicates([]) == []


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([4, 1, 9, -3], 6) == [2, 3]
