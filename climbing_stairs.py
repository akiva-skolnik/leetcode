# https://leetcode.com/problems/climbing-stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * n
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                cache[i] = 1
            elif i == n - 2:
                cache[i] = 2
            else:
                cache[i] = cache[i + 1] + cache[i + 2]
        return cache[0]


def test_solution():
    s = Solution()
    assert s.climbStairs(1) == 1
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(4) == 5
    assert s.climbStairs(5) == 8
    assert s.climbStairs(6) == 13
