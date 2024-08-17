from typing import List


# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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
