from typing import List


# https://leetcode.com/problems/kth-largest-element-in-an-array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Given an integer array nums and an integer k, return the kth largest element in the array."""
        return sorted(nums, reverse=True)[k - 1]


def test_solution():
    s = Solution()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert s.findKthLargest([1], 1) == 1
    assert s.findKthLargest([1, 2], 2) == 1
    assert s.findKthLargest([2, 1], 2) == 1
    assert s.findKthLargest([2, 1], 1) == 2
    assert s.findKthLargest([2, 1, 3], 2) == 2
    assert s.findKthLargest([2, 1, 3], 1) == 3
    assert s.findKthLargest([2, 1, 3], 3) == 1
    assert s.findKthLargest([2, 1, 3, 4], 2) == 3
    assert s.findKthLargest([2, 1, 3, 4], 1) == 4
    assert s.findKthLargest([2, 1, 3, 4], 3) == 2
    assert s.findKthLargest([2, 1, 3, 4], 4) == 1
    assert s.findKthLargest([2, 1, 3, 4, 5], 2) == 4
    assert s.findKthLargest([2, 1, 3, 4, 5], 1) == 5
    assert s.findKthLargest([2, 1, 3, 4, 5], 3) == 3
    assert s.findKthLargest([2, 1, 3, 4, 5], 4) == 2
    assert s.findKthLargest([2, 1, 3, 4, 5], 5) == 1
