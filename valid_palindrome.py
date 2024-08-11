import string


# https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(c for c in s if c in string.ascii_lowercase or c.isdigit())
        return all(s[i] == s[-i - 1] for i in range(len(s) // 2))


def test_1():
    assert Solution().isPalindrome("A man, a plan, a canal: Panama")


def test_2():
    assert not Solution().isPalindrome("race a car")


def test_3():
    assert Solution().isPalindrome(" ")
