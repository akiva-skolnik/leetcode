from collections import defaultdict


# https://leetcode.com/problems/ransom-note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """Given two strings ransomNote and magazine,
            return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
        Each letter in magazine can only be used once in ransomNote"""
        available_chars = defaultdict(int)
        for c in magazine:
            available_chars[c] += 1

        for c in ransomNote:
            if available_chars[c]:
                available_chars[c] -= 1
            else:
                return False
        return True


def test_1():
    assert Solution().canConstruct("a", "b") is False


def test_2():
    assert Solution().canConstruct("aa", "ab") is False


def test_3():
    assert Solution().canConstruct("aa", "aab") is True
