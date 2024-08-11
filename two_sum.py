from typing import List


# https://leetcode.com/problems/two-sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return next([i, j]
                    for i in range(len(nums))
                    for j in range(i + 1, len(nums))
                    if nums[i] + nums[j] == target)


def test_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_2():
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


def test_3():
    assert Solution().twoSum([3, 3], 6) == [0, 1]
