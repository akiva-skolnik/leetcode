# https://www.algoexpert.io/questions/river-sizes
def river_size(matrix: list, i: int, j: int) -> int:
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]) and matrix[i][j] == 1:
        matrix[i][j] = 0
        return 1 + river_size(matrix, i - 1, j) + \
            river_size(matrix, i + 1, j) + \
            river_size(matrix, i, j - 1) + \
            river_size(matrix, i, j + 1)
    else:
        return 0


def riverSizes(matrix: list) -> list:
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                result.append(river_size(matrix, i, j))
    return result


def test():
    tests = [{'matrix': [[1, 0, 0, 1, 0],
                         [1, 0, 1, 0, 0],
                         [0, 0, 1, 0, 1],
                         [1, 0, 1, 0, 1],
                         [1, 0, 1, 1, 0]],
              'expected': [2, 1, 5, 2, 2]},

             {'matrix': [[0]], 'expected': []},

             {'matrix': [[1]], 'expected': [1]},

             {'matrix': [[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]], 'expected': [3, 2, 1]},

             {'matrix': [[1, 0, 0, 1],
                         [1, 0, 1, 0],
                         [0, 0, 1, 0],
                         [1, 0, 1, 0]],
              'expected': [2, 1, 3, 1]},

             {'matrix': [[1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
                         [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
                         [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
                         [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
                         [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]],
              'expected': [2, 1, 21, 5, 2, 1]},

             {'matrix': [[1, 0, 0, 0, 0, 0, 1],
                         [0, 1, 0, 0, 0, 1, 0],
                         [0, 0, 1, 0, 1, 0, 0],
                         [0, 0, 0, 1, 0, 0, 0],
                         [0, 0, 1, 0, 1, 0, 0],
                         [0, 1, 0, 0, 0, 1, 0],
                         [1, 0, 0, 0, 0, 0, 1]],
              'expected': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]},

             {'matrix': [[1, 0, 0, 0, 0, 0, 1],
                         [0, 1, 0, 0, 0, 1, 0],
                         [0, 0, 1, 0, 1, 0, 0],
                         [0, 0, 1, 1, 1, 0, 0],
                         [0, 0, 1, 0, 1, 0, 0],
                         [0, 1, 0, 0, 0, 1, 0],
                         [1, 0, 0, 0, 0, 0, 1]],
              'expected': [1, 1, 1, 1, 7, 1, 1, 1, 1]},

             {'matrix': [[0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0]],
              'expected': []},

             {'matrix': [[1, 1, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1, 1, 1],
                         [1, 1, 1, 1, 1, 1, 1]],
              'expected': [49]},

             {'matrix': [[1, 1, 0, 0, 0, 0, 1, 1],
                         [1, 0, 1, 1, 1, 1, 0, 1],
                         [0, 1, 1, 0, 0, 0, 1, 1]],
              'expected': [3, 5, 6]},

             {'matrix': [[1, 1, 0],
                         [1, 0, 1],
                         [1, 1, 1],
                         [1, 1, 0],
                         [1, 0, 1],
                         [0, 1, 0],
                         [1, 0, 0],
                         [1, 0, 0],
                         [0, 0, 0],
                         [1, 0, 0],
                         [1, 0, 1],
                         [1, 1, 1]],
              'expected': [10, 1, 1, 2, 6]}]
    for test in tests:
        matrix, expected = test['matrix'], test['expected']
        assert sorted(riverSizes(matrix)) == sorted(expected), f"expected {expected} for {matrix}"
