from typing import List


# https://leetcode.com/problems/spiral-matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Given an m x n matrix, return all elements of the matrix in spiral order."""
        output = []
        first_row = first_col = 0
        last_row = len(matrix) - 1
        last_col = len(matrix[0]) - 1

        while first_row <= last_row and first_col <= last_col:
            if first_row == last_row and first_col == last_col:
                output.append(matrix[first_row][first_col])
                break
            output.extend(matrix[first_row][first_col:last_col + 1])
            output.extend([matrix[i][last_col] for i in range(first_row + 1, last_row + 1)])
            if first_row < last_row:  # otherwise already done
                output.extend([matrix[last_row][i] for i in range(last_col - 1, first_col - 1, -1)])
            if first_col < last_col:  # otherwise already done
                output.extend([matrix[i][first_col] for i in range(last_row - 1, first_row, -1)])
            first_row += 1
            first_col += 1
            last_row -= 1
            last_col -= 1

        return output


def test_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert Solution().spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_2():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert Solution().spiralOrder(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def test_3():
    matrix = [[6, 9, 7]]
    assert Solution().spiralOrder(matrix) == [6, 9, 7]


def test_4():
    matrix = [[3], [2]]
    assert Solution().spiralOrder(matrix) == [3, 2]
