from typing import List


# https://leetcode.com/problems/summary-ranges
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
            That is, each element of nums is covered by exactly one of the ranges,
                and there is no integer x such that x is in one of the ranges but not in nums.
        Each range [a,b] in the list should be output as:
        "a->b" if a != b, and "a" if a == b
        :param nums: a sorted integer array without duplicates"""
        if not nums:
            return []
        ranges = []
        first_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                ranges.append(f"{first_num}->{nums[i - 1]}" if nums[i - 1] != first_num else str(first_num))
                first_num = nums[i]

        ranges.append(f"{first_num}->{nums[-1]}" if nums[-1] != first_num else str(first_num))
        return ranges


def test_1():
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]


def test_2():
    assert Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
