from typing import List


# https://leetcode.com/problems/remove-element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1

        return i


def test():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert Solution().removeElement(nums, 2) == 5
    assert sorted(nums[:5]) == sorted([0, 1, 3, 0, 4])
