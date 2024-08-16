from typing import List


# https://leetcode.com/problems/search-a-2d-matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we can think of the matrix as a long 1d list
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m * n - 1
        while low <= high:
            mid = (low + high) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = n * row + col + 1
            else:
                high = n * row + col - 1
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        # find the row:
        low = 0
        high = len(matrix) - 1
        while low <= high:
            row = (low + high) // 2
            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            elif matrix[row][-1] < target:
                low = row + 1
            else:
                high = row - 1

        # Find within the row
        nums = matrix[row]
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


def test_1():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert Solution().searchMatrix(matrix, 3) is True
    assert Solution().searchMatrix(matrix, 13) is False
