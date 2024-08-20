# https://leetcode.com/problems/palindrome-number
class Solution:
    def isPalindrome(self, x: int) -> bool:  # slowest
        """Given an integer x, return true if x is a palindrome, and false otherwise."""
        s = str(x)
        return all(s[i] == s[-i - 1] for i in range(len(s)))

    def isPalindrome2(self, x: int) -> bool:  # middle
        s = str(x)
        return s == s[::-1]

    def isPalindrome3(self, x: int) -> bool:  # fastest
        s = str(x)
        if len(s) == 1:
            return True
        m = len(s) // 2
        return s[:m] == s[-m:][::-1]


def test_1():
    assert Solution().isPalindrome(121) is True


def test_2():
    assert Solution().isPalindrome(-121) is False


def test_3():
    assert Solution().isPalindrome(10) is False


def test_4():
    assert Solution().isPalindrome(11) is True


def test_5():
    assert Solution().isPalindrome(0) is True
