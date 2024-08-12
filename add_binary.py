# https://leetcode.com/problems/add-binary
class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        """Given two binary strings a and b, return their sum as a binary string."""
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary(self, a: str, b: str) -> str:
        """Given two binary strings a and b, return their sum as a binary string."""
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return "".join(result[::-1])


def test_1():
    assert Solution().addBinary("11", "1") == "100"


def test_2():
    assert Solution().addBinary("1010", "1011") == "10101"
