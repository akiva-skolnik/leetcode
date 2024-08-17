# https://leetcode.com/problems/is-subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0
        for t_i in range(len(t)):
            if s_i == len(s):
                return True
            if s[s_i] == t[t_i]:
                s_i += 1
        return s_i == len(s)


def test_is_subsequence():
    s = Solution()
    assert s.isSubsequence("abc", "ahbgdc")
    assert not s.isSubsequence("axc", "ahbgdc")
    assert s.isSubsequence("", "ahbgdc")
    assert s.isSubsequence("", "")
    assert not s.isSubsequence("abc", "")
    assert s.isSubsequence("abc", "abc")
    assert not s.isSubsequence("abc", "cab")
