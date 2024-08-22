from typing import List


# https://leetcode.com/problems/longest-common-prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Write a function to find the longest common prefix string amongst an array of strings."""
        return next((strs[0][:i]
                     for i in range(min(len(s) for s in strs), 0, -1)
                     if all(s.startswith(strs[0][:i]) for s in strs)), "")


def test_1():
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


def test_2():
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
