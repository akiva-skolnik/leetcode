# https://leetcode.com/problems/roman-to-integer
class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = romans[s[0]]
        for i in range(1, len(s)):
            if romans[s[i - 1]] < romans[s[i]]:
                result += romans[s[i]] - 2 * romans[s[i - 1]]
            else:
                result += romans[s[i]]
        return result


def test_1():
    s = "III"
    result = Solution().romanToInt(s)
    assert result == 3


def test_2():
    s = "LVIII"
    result = Solution().romanToInt(s)
    assert result == 58


def test_3():
    s = "MCMXCIV"
    result = Solution().romanToInt(s)
    assert result == 1994


def test_4():
    s = "IV"
    result = Solution().romanToInt(s)
    assert result == 4
