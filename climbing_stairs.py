# https://leetcode.com/problems/climbing-stairs
class Solution:
    def climbStairs1(self, n: int) -> int:
        """You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""
        cache = [0] * n
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                cache[i] = 1
            elif i == n - 2:
                cache[i] = 2
            else:
                cache[i] = cache[i + 1] + cache[i + 2]
        return cache[0]

    def climbStairs(self, n: int) -> int:
        # Fibonacci sequence
        if n == 1:
            return 1
        if n == 2:
            return 2
        n1 = 1
        n2 = 2
        for _ in range(n - 2):
            n1, n2 = n2, n1 + n2

        return n2


def test_solution():
    s = Solution()
    assert s.climbStairs(1) == 1
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(4) == 5
    assert s.climbStairs(5) == 8
    assert s.climbStairs(6) == 13
