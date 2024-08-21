# https://leetcode.com/problems/greatest-common-divisor-of-strings
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) < len(str1):
            # make str1 the shorter one
            str1, str2 = str2, str1

        def is_substring_match(prefix: str, i: int, s: str) -> bool:
            return len(s) % i == 0 and all(prefix == s[i * k:i * (k + 1)] for k in range(len(s) // i))

        for i in range(len(str1), 0, -1):
            prefix = str1[:i]
            if is_substring_match(prefix, i, str1) and is_substring_match(prefix, i, str2):
                return prefix
        return ""


def test_1():
    assert Solution().gcdOfStrings("ABCABC", "ABC") == "ABC"


def test_2():
    assert Solution().gcdOfStrings("ABABAB", "ABAB") == "AB"


def test_3():
    assert Solution().gcdOfStrings("LEET", "CODE") == ""


def test_4():
    assert Solution().gcdOfStrings("EFGABC", "ABC") == ""


def test_5():
    s = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    assert Solution().gcdOfStrings(s, s) == s
