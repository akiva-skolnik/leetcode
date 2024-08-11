from typing import List


# https://leetcode.com/problems/remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        nums[:len(s)] = s
        return len(s)


def test_1():
    nums = [1, 1, 2]
    assert Solution().removeDuplicates(nums) == 2
    assert nums[:2] == [1, 2]


def test_2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert Solution().removeDuplicates(nums) == 5
    assert nums[:5] == [0, 1, 2, 3, 4]
