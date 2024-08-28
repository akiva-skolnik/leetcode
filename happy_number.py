# https://leetcode.com/problems/happy-number
class Solution:
    def isHappy(self, n: int) -> bool:
        """Write an algorithm to determine if a number n is happy.
        A happy number is a number defined by the following process:

            Starting with any positive integer, replace the number by the sum of the squares of its digits.
            Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
            Those numbers for which this process ends in 1 are happy.

        Return true if n is a happy number, and false if not."""
        seen = set()
        while n > 1:
            n = self.get_next(n)  # or self.get_next2(n)
            if n in seen:
                return False
            seen.add(n)
        return n == 1

    @staticmethod
    def get_next(number: int) -> int:
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    @staticmethod
    def get_next2(number: int) -> int:
        return sum(int(d) ** 2 for d in str(number))


def test_solution():
    assert Solution().isHappy(19) is True
    assert Solution().isHappy(2) is False
    assert Solution().isHappy(7) is True
