from itertools import product
from typing import List


# https://leetcode.com/problems/letter-combinations-of-a-phone-number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Given a string containing digits from 2-9 inclusive,
            return all possible letter combinations that the number could represent."""
        if not digits:
            return []
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        return ["".join(x) for x in product(*[keyboard[d] for d in digits])]


def test_1():
    assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


def test_2():
    assert Solution().letterCombinations("") == []


def test_3():
    assert Solution().letterCombinations("2") == ["a", "b", "c"]
