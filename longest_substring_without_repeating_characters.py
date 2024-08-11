# https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Given a string s, find the length of the longest substring without repeating characters."""
        last_loc = {}
        if s:
            last_loc[s[0]] = 0
        start = 0
        end = 1
        longest = 0 if not s else 1
        while end < len(s):
            if last_loc.get(s[end], -1) >= start:
                i = last_loc[s[end]]
                longest = max(longest, i - start)
                start = i + 1
            else:
                longest = max(longest, end - start + 1)
            last_loc[s[end]] = end
            end += 1

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
