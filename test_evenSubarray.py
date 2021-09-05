from utils import evenSubarray
import pytest


@pytest.mark.parametrize("numbers, k, expected_results", [([1], 1, 1),
                                                          ([1, 2, 3, 1, 2], 2, 10),
                                                          ([6, 3, 5, 8], 1, 6),
                                                          ([], 1, 0),
                                                          ([2, 3, 1, 4, 1, 5, 1, 6, 1, 6, 1, 5, 63, 52, 5, 3, 3, 51, 2,
                                                            3, 1, 4, 2, 3, 1], 2, 47)
                                                          ])
def test_even(numbers, k, expected_results):
    assert evenSubarray(numbers, k) == expected_results
