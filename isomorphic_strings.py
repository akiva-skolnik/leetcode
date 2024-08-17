# https://leetcode.com/problems/isomorphic-strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = dict(zip(t, s))
        if len(set(mapping.values())) != len(mapping):
            return False
        return s == "".join(mapping.get(c, "") for c in t)


def test_1():
    s = "egg"
    t = "add"
    assert Solution().isIsomorphic(s, t) is True


def test_2():
    s = "foo"
    t = "bar"
    assert Solution().isIsomorphic(s, t) is False


def test_3():
    s = "paper"
    t = "title"
    assert Solution().isIsomorphic(s, t) is True


def test_4():
    assert Solution().isIsomorphic("badc", "baba") is False


def test_5():
    assert Solution().isIsomorphic("abab", "baba") is True
