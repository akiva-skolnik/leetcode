from typing import List


# https://leetcode.com/problems/maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_sums = [nums[0]]
        for i in range(1, len(nums)):
            sub_sums.append(max(nums[i], sub_sums[i - 1] + nums[i]))

        return max(sub_sums)


def test_1():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6
    assert Solution().maxSubArray(nums) == expected


def test_2():
    nums = [1]
    expected = 1
    assert Solution().maxSubArray(nums) == expected


def test_3():
    nums = [5, 4, -1, 7, 8]
    expected = 23
    assert Solution().maxSubArray(nums) == expected
