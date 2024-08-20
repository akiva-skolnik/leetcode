from typing import List


# https://leetcode.com/problems/sort-colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same
            color are adjacent, with the colors in the order red, white, and blue.
        - We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
        - You must solve this problem without using the library's sort function."""
        left = 0
        right = len(nums) - 1
        right = self.flag_sort(nums, left, right, right_val=2)
        self.flag_sort(nums, left, right, right_val=1)

    def flag_sort(self, nums: List[int], left: int, right: int, right_val: int) -> int:
        while left < right:
            if nums[left] == right_val:
                if nums[right] != right_val:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                right -= 1
            else:
                left += 1
        return (left - 1) if nums[left] == right_val else left


def test_1():
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_2():
    nums = [2, 0, 1]
    Solution().sortColors(nums)
    assert nums == [0, 1, 2]


def test_3():
    nums = [0]
    Solution().sortColors(nums)
    assert nums == [0]


def test_4():
    nums = [1, 2]
    Solution().sortColors(nums)
    assert nums == [1, 2]


def test_5():
    nums = [2, 1]
    Solution().sortColors(nums)
    assert nums == [1, 2]


def test_6():
    nums = [2, 2, 2, 2, 2, 2]
    Solution().sortColors(nums)
    assert nums == [2, 2, 2, 2, 2, 2]
