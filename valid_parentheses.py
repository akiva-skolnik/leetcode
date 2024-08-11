# https://leetcode.com/problems/valid-parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid."""
        stack = []
        match = {"}": "{", "]": "[", ")": "("}
        for c in s:
            if c in "([{":
                stack.append(c)
            elif stack and stack[-1] == match[c]:
                stack.pop()
            else:
                return False
        return not stack


def test_1():
    assert Solution().isValid("()") is True


def test_2():
    assert Solution().isValid("()[]{}") is True


def test_3():
    assert Solution().isValid("(]") is False
