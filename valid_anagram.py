from collections import Counter


# https://leetcode.com/problems/valid-anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)  # O(n)

    def isAnagram1(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if by rearranging the letters of s, it can be made equal to t."""
        return sorted(s) == sorted(t)  # O(n log n)


def test_solution():
    assert Solution().isAnagram("anagram", "nagaram") is True
    assert Solution().isAnagram("rat", "car") is False
    assert Solution().isAnagram("a", "a") is True
    assert Solution().isAnagram("a", "b") is False
    assert Solution().isAnagram("a", "ab") is False
    assert Solution().isAnagram("ab", "a") is False
    assert Solution().isAnagram("ab", "ba") is True
    assert Solution().isAnagram("abc", "bca") is True
