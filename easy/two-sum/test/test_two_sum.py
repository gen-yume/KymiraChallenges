from two_sum import two_sum
from typing import List
import pytest

@pytest.mark.parametrize("nums, target, expected", [
	([3, 4], 7, [0, 1]),
	([4, 3], 7, [0, 1]),
	([3, 3], 6, [0, 1]),
	([3, 2, 4], 6, [1, 2]),
	([2, 7, 11, 15], 9, [0, 1]),
])
def test_two_sum(nums: List[int], target: int, expected: List[int]):
	# Since the indices can be returned in either order, sort the returned
	#   indices before comparing them to the expected indices.
	actual = two_sum(nums, target)
	actual.sort()
	assert actual == expected
