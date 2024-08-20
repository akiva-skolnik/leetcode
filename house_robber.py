from functools import lru_cache
from typing import List


# https://leetcode.com/problems/house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        return self.rob_rec(-2, 0)

    @lru_cache
    def rob_rec(self, last_i: int, i: int) -> int:
        if i == len(self.nums):
            return 0
        if i == last_i + 1:
            return self.rob_rec(last_i, i + 1)
        return max(self.nums[i] + self.rob_rec(i, i + 1),
                   self.rob_rec(last_i, i + 1))


def test_1():
    assert Solution().rob([1, 2, 3, 1]) == 4

def test_2():
    assert Solution().rob([2, 7, 9, 3, 1]) == 12

def test_3():
    assert Solution().rob([2, 1, 1, 2]) == 4

