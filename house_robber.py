from functools import lru_cache
from typing import List


# https://leetcode.com/problems/house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        """Given an integer array nums representing the amount of money of each house,
            return the maximum amount of money you can rob without robbing two adjacent houses."""
        # dynamic programming - O(n) solution
        if len(nums) <= 2:
            return max(nums or [0])
        # history[i] = max rob from i to n
        history = [0] * len(nums)
        history[-1] = nums[-1]
        history[-2] = max(nums[-1], nums[-2])
        for i in range(len(nums) - 3, -1, -1):
            # we better rob current house and forget about the prv.
            history[i] = max(history[i + 1], history[i + 2] + nums[i])

        return history[0]

    def rob_2(self, nums: List[int]) -> int:
        self.nums = nums
        return self.rob_rec(-2, 0)

    @lru_cache
    def rob_rec(self, last_i: int, i: int) -> int:
        # n^2 solution
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

