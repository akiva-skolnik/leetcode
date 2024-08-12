# https://leetcode.com/problems/add-binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Given two binary strings a and b, return their sum as a binary string."""
        return bin(int(a, 2) + int(b, 2))[2:]


def test_1():
    assert Solution().addBinary("11", "1") == "100"


def test_2():
    assert Solution().addBinary("1010", "1011") == "10101"
