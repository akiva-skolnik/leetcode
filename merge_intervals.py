from typing import List


# https://leetcode.com/problems/merge-intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # optimize space
        intervals.sort()
        i = 1
        while i < len(intervals):
            if intervals[i - 1][0] <= intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1
        return intervals

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        # optimize time
        intervals.sort()
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            elif merged[-1][1] < intervals[i][1]:
                merged[-1][1] = intervals[i][1]
        return merged


def test_1():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert Solution().merge(intervals) == [[1, 6], [8, 10], [15, 18]]


def test_2():
    intervals = [[1, 4], [4, 5]]
    assert Solution().merge(intervals) == [[1, 5]]
