# https://leetcode.com/problems/palindrome-number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Given an integer x, return true if x is a palindrome, and false otherwise."""
        s = str(x)
        return all(s[i] == s[-i - 1] for i in range(len(s)))


def test_1():
    assert Solution().isPalindrome(121) is True


def test_2():
    assert Solution().isPalindrome(-121) is False


def test_3():
    assert Solution().isPalindrome(10) is False
