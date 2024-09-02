from typing import List


# https://leetcode.com/problems/jump-game
# Some great solutions here: https://leetcode.com/problems/jump-game/solutions
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums[:-1]:
            return True

        tested = set()
        stack = {0}
        while stack:
            i = stack.pop()
            if i + nums[i] >= len(nums) - 1:
                return True
            tested.add(i)
            stack.update({j for j in range(i + 1, i + nums[i] + 1) if j not in tested})
        return False


def test():
    assert Solution().canJump([2, 3, 1, 1, 4]) is True
    assert Solution().canJump([3, 2, 1, 0, 4]) is False
    assert Solution().canJump([0]) is True
    assert Solution().canJump([1]) is True
    assert Solution().canJump([0, 1]) is False
    assert Solution().canJump([1, 0]) is True
    assert Solution().canJump([1, 0, 1]) is False
    assert Solution().canJump([2, 0, 0]) is True
    assert Solution().canJump([1, 1, 2, 2, 0, 1, 1]) is True
