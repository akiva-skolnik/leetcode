from typing import List, Dict, Tuple


# https://leetcode.com/problems/number-of-islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Given an 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically."""

        def erase_island(i: int, j: int) -> None:
            if not (0 <= i < len(grid)) or not (0 <= j < len(grid[i])) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            erase_island(i - 1, j)
            erase_island(i, j - 1)
            erase_island(i + 1, j)
            erase_island(i, j + 1)

        n_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    n_islands += 1
                    erase_island(i, j)
        return n_islands

    def numIslands2(self, grid: List[List[str]]) -> int:
        indices: Dict[Tuple[int, int], bool] = {(i, j): True for i in range(len(grid)) for j in range(len(grid[i]))}

        def erase_island(i: int, j: int) -> None:
            if not (0 <= i < len(grid)) or not (0 <= j < len(grid[i])) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            indices[(i, j)] = False  # don't recheck the same cell
            erase_island(i - 1, j)
            erase_island(i, j - 1)
            erase_island(i + 1, j)
            erase_island(i, j + 1)

        n_islands = 0
        for (i, j) in indices:
            if indices[(i, j)] and grid[i][j] == '1':
                n_islands += 1
                erase_island(i, j)

        return n_islands


def test_1():
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    assert Solution().numIslands(grid) == 1


def test_2():
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    assert Solution().numIslands(grid) == 3


def test_3():
    grid = [["1", "0", "1", "1", "0", "1", "1"]]
    assert Solution().numIslands(grid) == 3


def test_4():
    grid = [["0", "1", "0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "1", "0", "1"],
            ["1", "0", "1", "0", "0", "1", "1", "0", "0", "1", "0", "1", "0", "1", "0", "1", "1", "0", "0", "0"],
            ["0", "1", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0", "1"],
            ["1", "1", "0", "0", "0", "1", "1", "0", "0", "0", "1", "1", "1", "0", "0", "1", "0", "1", "1", "0"],
            ["0", "1", "0", "1", "1", "0", "1", "0", "0", "0", "1", "0", "0", "1", "0", "0", "0", "0", "0", "1"],
            ["1", "0", "0", "1", "0", "1", "0", "0", "0", "1", "1", "0", "1", "0", "0", "1", "0", "0", "0", "0"],
            ["1", "0", "0", "0", "1", "1", "0", "0", "0", "0", "0", "1", "0", "0", "1", "0", "0", "0", "0", "1"],
            ["1", "0", "0", "0", "1", "0", "1", "1", "1", "0", "1", "0", "1", "1", "1", "1", "0", "0", "0", "1"],
            ["1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "1"],
            ["0", "0", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0", "1", "0"],
            ["1", "0", "1", "0", "1", "0", "0", "1", "1", "1", "0", "1", "1", "0", "0", "1", "1", "0", "0", "0"],
            ["0", "1", "0", "0", "1", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "1", "0"],
            ["1", "0", "0", "0", "1", "1", "1", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "0", "1"],
            ["0", "0", "0", "0", "1", "0", "1", "1", "0", "1", "0", "1", "0", "1", "1", "1", "1", "0", "0", "0"],
            ["0", "1", "1", "0", "0", "0", "0", "1", "0", "0", "1", "1", "1", "0", "0", "1", "1", "0", "1", "0"],
            ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "0", "0", "1", "0", "0", "0", "1"],
            ["1", "0", "0", "0", "1", "0", "1", "0", "0", "1", "0", "1", "0", "0", "1", "0", "0", "1", "1", "1"],
            ["0", "0", "1", "0", "0", "0", "0", "1", "0", "0", "1", "1", "0", "1", "1", "1", "0", "0", "0", "0"],
            ["0", "0", "1", "0", "0", "0", "0", "0", "0", "1", "1", "0", "1", "0", "1", "0", "0", "0", "1", "1"],
            ["1", "0", "0", "0", "1", "0", "1", "1", "1", "0", "0", "1", "0", "1", "0", "1", "1", "0", "0", "0"]]

    assert Solution().numIslands(grid) == 55
