# https://www.algoexpert.io/questions/validate-subsequence

def isValidSubsequence(array: list, sequence: list) -> bool:
    """Given two non-empty arrays of integers,
        write a function that determines whether the second array is a subsequence of the first one."""
    i = 0
    for num in array:
        if i == len(sequence):
            return True
        if sequence[i] == num:
            i += 1
    return i == len(sequence)


def test():
    tests = [{'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [1, 6, -1, 10], 'expected': True},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [5, 1, 22, 25, 6, -1, 8, 10], 'expected': True},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [5, 1, 22, 6, -1, 8, 10], 'expected': True},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [22, 25, 6], 'expected': True},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [1, 6, 10], 'expected': True},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [5, 1, 22, 10], 'expected': True},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [5, -1, 8, 10], 'expected': True},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [25], 'expected': True},
             {'array': [1, 1, 1, 1, 1], 'sequence': [1, 1, 1], 'expected': True},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [5, 1, 22, 25, 6, -1, 8, 10, 12], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [4, 5, 1, 22, 25, 6, -1, 8, 10], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [5, 1, 22, 23, 6, -1, 8, 10], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [5, 1, 22, 22, 25, 6, -1, 8, 10], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [5, 1, 22, 22, 6, -1, 8, 10], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [1, 6, -1, -1], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [1, 6, -1, -1, 10], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [1, 6, -1, -2], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [26], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [5, 1, 25, 22, 6, -1, 8, 10], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [5, 26, 22, 8], 'expected': False},
             {'array': [1, 1, 6, 1], 'sequence': [1, 1, 1, 6], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [1, 6, -1, 10, 11, 11, 11, 11], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [5, 1, 22, 25, 6, -1, 8, 10, 10], 'expected': False},
             {'array': [5, 1, 22, 25, 6, -1, 8, 10], 'sequence': [1, 6, -1, 5], 'expected': False}]

    for test in tests:
        array, sequence, expected = test['array'], test['sequence'], test['expected']
        assert isValidSubsequence(array, sequence) == expected, f"expected {expected} for {array}, {sequence}"
