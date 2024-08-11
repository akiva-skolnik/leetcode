from typing import List


# https://leetcode.com/problems/rotate-array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i = len(nums) - (k % len(nums))
        nums[i:], nums[:i] = nums[:i], nums[i:]


def test_rotate_1():
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_rotate_2():
    nums = [-1, -100, 3, 99]
    Solution().rotate(nums, 2)
    assert nums == [3, 99, -1, -100]
