# https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Given a string s, find the length of the longest substring without repeating characters."""
        start = 0
        end = 1
        longest = 0 if len(s) != 1 else 1
        while end < len(s):
            for i in range(start, end):
                if s[i] == s[end]:
                    longest = max(longest, i - start + 1)
                    start = end = i + 1
                    break
                else:
                    longest = max(longest, i - start + 2)
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
