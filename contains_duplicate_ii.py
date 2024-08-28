from typing import List


# https://leetcode.com/problems/contains-duplicate-ii
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index_per_num = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in last_index_per_num and abs(last_index_per_num[num] - i) <= k:
                return True

            last_index_per_num[num] = i
        return False


def test_solution():
    assert Solution().containsNearbyDuplicate([1, 2, 3, 1], 3) is True
    assert Solution().containsNearbyDuplicate([1, 0, 1, 1], 1) is True
    assert Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
