from typing import List


# https://leetcode.com/problems/delete-columns-to-make-sorted
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """Return the number of columns that are not sorted lexicographically.
        - All strs are of the same length."""
        return len([i for i in range(len(strs[0])) if any(strs[j][i] > strs[j + 1][i] for j in range(len(strs) - 1))])


def test_1():
    assert Solution().minDeletionSize(["cba", "daf", "ghi"]) == 1


def test_2():
    assert Solution().minDeletionSize(["a", "b"]) == 0


def test_3():
    assert Solution().minDeletionSize(["zyx", "wvu", "tsr"]) == 3
