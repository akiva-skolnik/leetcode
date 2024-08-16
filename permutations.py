from itertools import permutations
from typing import List


# https://leetcode.com/problems/permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Given an array nums of distinct integers, return all the possible permutations."""
        return list(permutations(nums))


def test_1():
    assert Solution().permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]


def test_2():
    assert Solution().permute([0, 1]) == [[0, 1], [1, 0]]


def test_3():
    assert Solution().permute([1]) == [[1]]
