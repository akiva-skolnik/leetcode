from typing import List


# https://leetcode.com/problems/search-insert-position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if low < len(nums) and nums[low] < target:
            return low + 1
        return low


def test_1():
    nums = [1, 3, 5, 6]
    assert Solution().searchInsert(nums, 5) == 2
    assert Solution().searchInsert(nums, 2) == 1
    assert Solution().searchInsert(nums, 7) == 4


def test_2():
    assert Solution().searchInsert([1, 3], 2) == 1
