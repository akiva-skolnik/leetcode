from typing import List


# https://leetcode.com/problems/combination-sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.target = target
        self.result = []
        self.combinationSumRec(0, 0, [])
        return self.result

    def combinationSumRec(self, i: int, s: int, candidate: List[int]) -> None:
        if i == len(self.candidates) or s > self.target:
            return

        new_s = s + self.candidates[i]
        updated_candidate = candidate + [self.candidates[i]]

        if new_s == self.target:
            if updated_candidate not in self.result:
                self.result.append(updated_candidate)
        elif new_s < self.target:
            self.combinationSumRec(i, new_s, updated_candidate)

        self.combinationSumRec(i + 1, s, candidate)  # Skip the current candidate


def test_1():
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]


def test_2():
    assert Solution().combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


def test_3():
    assert Solution().combinationSum([2], 1) == []


def test_4():
    assert Solution().combinationSum([3, 5, 8], 11) == [[3, 3, 5], [3, 8]]


def test_5():
    assert Solution().combinationSum([4, 2, 8], 8) == [[4, 4], [4, 2, 2], [2, 2, 2, 2], [8]]
