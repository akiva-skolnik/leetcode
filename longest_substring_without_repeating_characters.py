# https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Given a string s, find the length of the longest substring without repeating characters."""
        last_loc: dict = {}
        start: int = 0
        longest: int = 0
        for end in range(len(s)):
            c: str = s[end]
            if last_loc.get(c, -1) >= start:
                start = last_loc[c] + 1
            else:
                longest = max(longest, end - start + 1)
            last_loc[c] = end

        return longest


def test_1():
    s = "abcabcbb"
    assert Solution().lengthOfLongestSubstring(s) == 3


def test_2():
    s = "bbbbb"
    assert Solution().lengthOfLongestSubstring(s) == 1


def test_3():
    s = "pwwkew"
    assert Solution().lengthOfLongestSubstring(s) == 3
