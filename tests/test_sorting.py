from sorting.algorithms import bubble_sort, quick_sort, merge_sort
import pytest

@pytest.mark.parametrize("sort_func", [bubble_sort, quick_sort, merge_sort])
def test_sorting_algorithms(sort_func):
    data = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(data)
    assert sort_func(data) == expected

@pytest.mark.parametrize("sort_func", [bubble_sort, quick_sort, merge_sort])
def test_empty_and_single_element(sort_func):
    assert sort_func([]) == []
    assert sort_func([1]) == [1]

@pytest.mark.parametrize("sort_func", [bubble_sort, quick_sort, merge_sort])
def test_duplicate_elements(sort_func):
    data = [5, 1, 5, 2, 8, 1]
    assert sort_func(data) == sorted(data)
