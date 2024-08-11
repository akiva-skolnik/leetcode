from typing import List

# https://leetcode.com/problems/median-of-two-sorted-arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Given two sorted arrays nums1 and nums2 of size m and n respectively,
            return the median of the two sorted arrays."""
        merged = self.merge_sorted(nums1, nums2)

        mid = len(merged) // 2
        if len(merged) % 2 == 1:
            return merged[mid]
        else:
            return (merged[mid] + merged[mid-1]) / 2

    @staticmethod
    def merge_sorted(nums1: List[int], nums2: List[int]) -> List[int]:
        merged = []
        i1 = i2 = 0
        while i1 < len(nums1) or i2 < len(nums2):
            if i2 == len(nums2) or (i1 < len(nums1) and nums1[i1] < nums2[i2]):
                merged.append(nums1[i1])
                i1 += 1
            else:
                merged.append(nums2[i2])
                i2 += 1
        return merged


def test_1():
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.00000

def test_2():
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.50000