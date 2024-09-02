from typing import List


# https://leetcode.com/problems/jump-game-ii
class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jump = [0] * len(nums)
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] + 1 >= len(nums):
                min_jump[i] = 1
            elif nums[i] == 0:
                min_jump[i] = len(nums) + 1
            else:
                min_jump[i] = 1 + min(min_jump[i + 1:i + nums[i] + 1])
        return min_jump[0]


def test():
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
    assert Solution().jump([2, 3, 0, 1, 4]) == 2
