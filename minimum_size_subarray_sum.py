from typing import List


# https://leetcode.com/problems/minimum-size-subarray-sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = high = 0
        global_min = float("inf")
        global_sum = sub_sum = nums[low]
        while low < len(nums):
            while sub_sum < target and high + 1 < len(nums):
                high += 1
                sub_sum += nums[high]

            if sub_sum < target:
                break

            while sub_sum - nums[low] >= target:
                sub_sum -= nums[low]
                low += 1

            sub_min = high - low + 1
            if sub_min < global_min:
                global_min = sub_min
                global_sum = sub_sum

            sub_sum -= nums[low]
            low += 1

        return global_min if global_min != float("inf") else 0


def test_1():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    assert Solution().minSubArrayLen(target, nums) == 2


def test_2():
    target = 4
    nums = [1, 4, 4]
    assert Solution().minSubArrayLen(target, nums) == 1


def test_3():
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    assert Solution().minSubArrayLen(target, nums) == 0
