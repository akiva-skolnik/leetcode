# https://leetcode.com/problems/powx-n
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Implement pow(x, n), which calculates x raised to the power n (i.e., x^n)."""
        if x == 0:
            return 0
        if n < 0:
            x = 1 / x

        res = 1
        for i in range(abs(n)):
            res *= x
        return res


def test_1():
    assert Solution().myPow(2.00000, 10) == 1024.00000


def test_2():
    assert round(Solution().myPow(2.1, 3), 3) == 9.261


def test_3():
    assert Solution().myPow(2.00000, -2) == 0.25000
