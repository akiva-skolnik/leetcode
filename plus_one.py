from typing import List


# https://leetcode.com/problems/plus-one
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Increment the integer (represented by digits) by one and return the resulting array of digits."""
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
            i -= 1
        if i < 0:
            digits.insert(0, 1)
        return digits

    def plusOne2(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

def test_1():
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]


def test_2():
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]


def test_3():
    assert Solution().plusOne([9]) == [1, 0]


def test_4():
    assert Solution().plusOne([0]) == [1]
