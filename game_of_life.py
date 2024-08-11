from copy import deepcopy
from typing import List


# https://leetcode.com/problems/game-of-life
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state,
where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state."""
        copy = deepcopy(board)
        m = len(board)  # >=1
        n = len(board[0])  # <=25

        for i in range(m):
            for j in range(n):
                n_neighbors = len(tuple(copy[i1][j1]
                                        for i1, j1 in ((i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
                                                       (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1))
                                        if 0 <= i1 < m and 0 <= j1 < n and copy[i1][j1]))

                if board[i][j]:
                    board[i][j] = int(n_neighbors in (2, 3))
                elif n_neighbors == 3:
                    board[i][j] = 1


def test_1():
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution().gameOfLife(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]


def test_2():
    board = [[1, 1], [1, 0]]
    Solution().gameOfLife(board)
    assert board == [[1, 1], [1, 1]]
