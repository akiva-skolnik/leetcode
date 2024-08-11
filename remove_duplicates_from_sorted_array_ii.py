from typing import List


# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Given an integer array nums sorted in non-decreasing order,
            remove some duplicates in-place such that each unique element appears at most twice.
            The relative order of the elements should be kept the same."""
        n = len(nums)
        if n <= 2:
            return n
        k = 2

        while k < n:
            if nums[k - 2] == nums[k - 1] and nums[k - 1] == nums[k]:
                i = k
                while i < n and nums[i] == nums[k]:
                    i += 1
                if i == n:
                    return k
                nums[k:k + n - i] = nums[i:n]
                n -= i - k
            k += 1
        return k


def test():
    nums = [1, 1, 1, 2, 2, 3]
    assert Solution().removeDuplicates(nums) == 5
    assert nums[:5] == [1, 1, 2, 2, 3]

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    assert Solution().removeDuplicates(nums) == 7
    assert nums[:7] == [0, 0, 1, 1, 2, 3, 3]
