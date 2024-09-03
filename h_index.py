from typing import List


# https://leetcode.com/problems/h-index
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """Given an array of integers citations where citations[i] is the number of citations a researcher
            received for their ith paper, return the maximum value of h such that the given researcher has published at
            least h papers that have each been cited at least h times."""
        citations.sort(reverse=True)
        return next((i+1 for i in reversed(range(len(citations))) if citations[i] >= i+1), 0)

    def hIndex2(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        return max((i for i, c in enumerate(citations, 1) if c >= i), default=0)

def test_1():
    citations = [3, 0, 6, 1, 5]
    result = Solution().hIndex(citations)
    assert result == 3


def test_2():
    citations = [1, 3, 1]
    result = Solution().hIndex(citations)
    assert result == 1


def test_3():
    citations = [100]
    result = Solution().hIndex(citations)
    assert result == 1


def test_n():
    tests = {(1,): 1,
             (1, 1, 1, 1): 1,
             (3, 1, 1): 1,
             (3, 3, 2, 2, 2, 1, 1, 1, 1): 2,
             (5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1): 4,
             (6, 5, 3, 1, 0): 3,
             (6, 6, 5, 5, 3, 3, 1, 1, 0, 0): 4,
             (7, 7, 7, 7): 4,
             (8, 8, 7, 7, 7): 5,
             (8, 8, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 1, 1, 1, 0, 0): 6,
             (9, 9, 8, 8, 7, 7, 6, 6, 5): 6,
             (9, 9, 9, 9, 9, 9, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0): 7}

    for citations, expected in tests.items():
        result = Solution().hIndex(list(citations))
        assert result == expected
