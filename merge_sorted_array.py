from typing import List

# https://leetcode.com/problems/merge-sorted-array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
            representing the number of elements in nums1 and nums2 respectively.

        Merge nums1 and nums2 into a single array sorted in non-decreasing order.
        """
        nums1_copy = nums1.copy()
        p1 = p2 = 0
        for i in range(m + n):
            if p1 < m and (p2 == n or nums1_copy[p1] <= nums2[p2]):
                nums1[i] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1


def test_merge_1():
    nums1 = [1, 0]  # m + n
    nums2 = [2]
    Solution().merge(nums1, 1, nums2, 1)
    assert nums1 == [1, 2]


def test_merge_2():
    nums1 = [2, 0]
    nums2 = [1]
    Solution().merge(nums1, 1, nums2, 1)
    assert nums1 == [1, 2]
