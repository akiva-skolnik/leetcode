from typing import List


# https://leetcode.com/problems/valid-sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        empty = "."
        for i in range(9):
            col_vals = set()
            row_vals = set()
            box_vals = set()
            for j in range(9):
                col_val = board[j][i]
                row_val = board[i][j]
                box_val = board[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3]  # i is the box index
                if (col_val != empty and col_val in col_vals) or \
                        (row_val != empty and row_val in row_vals) or \
                        (box_val != empty and box_val in box_vals):
                    return False
                col_vals.add(col_val)
                row_vals.add(row_val)
                box_vals.add(box_val)

        return True


def test_1():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert Solution().isValidSudoku(board) is True


def test_2():
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert Solution().isValidSudoku(board) is False
