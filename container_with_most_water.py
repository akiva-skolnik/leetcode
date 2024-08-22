from typing import List


# https://leetcode.com/problems/container-with-most-water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Return the maximum amount of water a container can store.
        Each integer represents the height of a vertical line on the x-axis."""
        low = 0
        high = len(height) - 1
        max_water = 0
        while low < high:
            max_water = max(max_water, (high - low) * min(height[high], height[low]))

            # we can stop considering one side, as we decrease the width,
            #   and we may get a better result only if the height increases
            if height[high] < height[low]:
                high -= 1
            else:
                low += 1
        return max_water


def test_1():
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_2():
    assert Solution().maxArea([1, 1]) == 1
