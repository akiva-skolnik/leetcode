# https://leetcode.com/problems/length-of-last-word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rsplit(maxsplit=1)[-1])


def test_1():
    s = "Hello World"
    result = Solution().lengthOfLastWord(s)
    assert result == 5


def test_2():
    s = "   fly me   to   the moon  "
    result = Solution().lengthOfLastWord(s)
    assert result == 4


def test_3():
    s = "luffy is still joyboy"
    result = Solution().lengthOfLastWord(s)
    assert result == 6
