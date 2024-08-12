from typing import List
import random


# https://leetcode.com/problems/kth-largest-element-in-an-array
class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        """Given an integer array nums and an integer k, return the kth largest element in the array."""
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, k)

    @staticmethod
    def quick_select(nums: List[int], left: int, right: int, k: int) -> int:
        if left == right:
            return nums[left]

        pivot = Solution.partition(nums, left, right)
        # Now nums[left...pivot-1] >= nums[pivot] >= nums[pivot+1...right]
        n = pivot - left + 1  # number of elements on the left side (including pivot)
        if n == k:
            return nums[pivot]
        elif n > k:  # k-th largest is on the left side
            return Solution.quick_select(nums, left, pivot - 1, k)
        else:
            return Solution.quick_select(nums, pivot + 1, right, k - n)

    @staticmethod
    def partition(nums: List[int], left: int, right: int) -> int:
        pivot = random.randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot]
        pivot = right
        i = left - 1
        for j in range(left, right):
            if nums[j] >= nums[pivot]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[pivot] = nums[pivot], nums[i + 1]
        return i + 1


def test_solution():
    s = Solution()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    assert s.findKthLargest(nums, 4) == 4
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
test_solution()