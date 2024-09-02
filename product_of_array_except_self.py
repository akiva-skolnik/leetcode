from typing import List


# https://leetcode.com/problems/product-of-array-except-self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
            elements of nums except nums[i].
            - You must write an algorithm that runs in O(n) time and without using the division operation!"""
        before = [1] * len(nums)
        after = [1] * len(nums)
        for i in range(1, len(nums)):
            before[i] = before[i - 1] * nums[i - 1]

        for i in reversed(range(len(nums) - 1)):
            after[i] = after[i + 1] * nums[i + 1]

        return [before[i] * after[i] for i in range(len(nums))]


def test_1():
    nums = [1, 2, 3, 4]
    result = Solution().productExceptSelf(nums)
    assert result == [24, 12, 8, 6]


def test_2():
    nums = [-1, 1, 0, -3, 3]
    result = Solution().productExceptSelf(nums)
    assert result == [0, 0, 9, 0, 0]
