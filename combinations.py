from itertools import combinations
from typing import List


# https://leetcode.com/problems/combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n + 1), k))


def test_1():
    assert Solution().combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]


def test_2():
    assert Solution().combine(1, 1) == [[1]]
