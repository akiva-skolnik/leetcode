from typing import List


# https://leetcode.com/problems/two-sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target,
            return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order."""
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in seen:
                seen[nums[i]] = i
            else:
                return [seen[diff], i]



def test_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_2():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


def test_3():
    assert Solution().twoSum([3, 3], 6) == [0, 1]
