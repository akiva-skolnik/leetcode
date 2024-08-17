from typing import List


# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
            find two numbers such that they add up to a specific target number.
            Return the indices of the two numbers, index1 and index2, added by one.
            Assume there is exactly one solution. You may not use the same element twice."""
        # two pointers approach:
        left = 0
        right = len(numbers) - 1
        while left < right:
            t = numbers[left] + numbers[right]
            if t == target:
                return [left + 1, right + 1]
            elif t > target:
                right -= 1
            else:
                left += 1

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        # binary search approach:
        for i in range(len(numbers)):
            second_index = self.binary_search(numbers, i + 1, len(numbers), target - numbers[i])
            if second_index:
                return [i + 1, second_index + 1]

    @staticmethod
    def binary_search(numbers: List[int], left: int, right: int, item: int) -> int:
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] == item:
                return mid
            elif numbers[mid] < item:
                left = mid + 1
            else:
                right = mid


def test_1():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]


def test_2():
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]


def test_3():
    assert Solution().twoSum([-1, 0], -1) == [1, 2]


def test_4():
    assert Solution().twoSum([-1, -1] + 29998 * [1], -2) == [1, 2]
