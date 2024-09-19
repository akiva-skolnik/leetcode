# https://www.algoexpert.io/questions/two-number-sum
def twoNumberSum(array: list, targetSum: int) -> list:
    """Given an array of integers, return a pair of numbers that sum up to the target sum."""
    s = set(array)
    for num in array:
        diff = targetSum - num
        if num != diff and diff in s:
            return [num, diff]
    return []


def test():
    tests = [{'array': [3, 5, -4, 8, 11, 1, -1, 6], 'targetSum': 10, 'expected': [11, -1]},
             {'array': [4, 6], 'targetSum': 10, 'expected': [4, 6]},
             {'array': [4, 6, 1], 'targetSum': 5, 'expected': [4, 1]},
             {'array': [4, 6, 1, -3], 'targetSum': 3, 'expected': [6, -3]},
             {'array': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'targetSum': 17, 'expected': [8, 9]},
             {'array': [1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 'targetSum': 18, 'expected': [3, 15]},
             {'array': [-7, -5, -3, -1, 0, 1, 3, 5, 7], 'targetSum': -5, 'expected': [-5, 0]},
             {'array': [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 'targetSum': 163, 'expected': [210, -47]},
             {'array': [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 'targetSum': 164, 'expected': []},
             {'array': [3, 5, -4, 8, 11, 1, -1, 6], 'targetSum': 15, 'expected': []},
             {'array': [14], 'targetSum': 15, 'expected': []}, {'array': [15], 'targetSum': 15, 'expected': []}]
    for test in tests:
        array, targetSum, expected = test['array'], test['targetSum'], test['expected']
        assert twoNumberSum(array, targetSum) == expected, f"expected {expected} for {array}, {targetSum}"
