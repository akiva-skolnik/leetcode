# https://www.algoexpert.io/questions/product-sum
def productSum(array: list, depth: int = 1) -> int:
    """Write a function that takes in an array and returns its product sum,
        where nested arrays are multiplied by their depth"""
    return depth * sum(x if isinstance(x, int) else productSum(x, depth + 1)
                       for x in array)


def test():
    tests = [{'array': [5, 2, [7, -1], 3, [6, [-13, 8], 4]], 'expected': 12},
             {'array': [1, 2, 3, 4, 5], 'expected': 15}, {'array': [1, 2, [3], 4, 5], 'expected': 18},
             {'array': [[1, 2], 3, [4, 5]], 'expected': 27}, {'array': [[[[[5]]]]], 'expected': 600}, {
                 'array': [9, [2, -3, 4], 1, [1, 1, [1, 1, 1]], [[[[3, 4, 1]]], 8], [1, 2, 3, 4, 5, [6, 7], -7],
                           [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7],
                           [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]], -3],
                 'expected': 1351}]
    for test in tests:
        array, expected = test['array'], test['expected']
        assert productSum(array) == expected, f"expected {expected} for {array}"
test()