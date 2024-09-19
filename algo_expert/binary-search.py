# https://www.algoexpert.io/questions/binary-search
def binarySearch(array: list, target: int) -> int:
    """Implement binary search algorithm (search for target in a sorted array efficiently)"""
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def test():
    tests = [{'array': [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 'target': 33, 'expected': 3},
             {'array': [1, 5, 23, 111], 'target': 111, 'expected': 3},
             {'array': [1, 5, 23, 111], 'target': 5, 'expected': 1},
             {'array': [1, 5, 23, 111], 'target': 35, 'expected': -1},
             {'array': [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 'target': 0, 'expected': 0},
             {'array': [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 'target': 1, 'expected': 1},
             {'array': [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 'target': 21, 'expected': 2},
             {'array': [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 'target': 45, 'expected': 4},
             {'array': [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 'target': 61, 'expected': 6},
             {'array': [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 'target': 71, 'expected': 7},
             {'array': [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 'target': 72, 'expected': 8},
             {'array': [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 'target': 73, 'expected': 9},
             {'array': [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 'target': 70, 'expected': -1},
             {'array': [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 'target': 355, 'expected': 10},
             {'array': [0, 1, 21, 33, 45, 45, 61, 71, 72, 73, 355], 'target': 354, 'expected': -1},
             {'array': [1, 5, 23, 111], 'target': 120, 'expected': -1},
             {'array': [5, 23, 111], 'target': 3, 'expected': -1},
             {'array': [5], 'target': 5, 'expected': 0},
             {'array': [5], 'target': 3, 'expected': -1},
             {'array': [5], 'target': 100, 'expected': -1},
             {'array': [], 'target': 100, 'expected': -1}]

    for test in tests:
        array, target, expected = test['array'], test['target'], test['expected']
        assert binarySearch(array, target) == expected, f"expected {expected} for {array}, {target}"
