from collections import Counter


def firstNonRepeatingCharacter(string: str) -> int:
    counter = Counter(string)
    for i, c in enumerate(string):
        if counter[c] == 1:
            return i
    return -1


def test():
    tests = [{'string': 'abcdcaf', 'expected': 1}, {'string': 'faadabcbbebdf', 'expected': 6},
             {'string': 'a', 'expected': 0}, {'string': 'ab', 'expected': 0}, {'string': 'abc', 'expected': 0},
             {'string': 'abac', 'expected': 1}, {'string': 'ababac', 'expected': 5},
             {'string': 'ababacc', 'expected': -1},
             {'string': 'lmnopqldsafmnopqsa', 'expected': 7},
             {'string': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy', 'expected': 25},
             {'string': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', 'expected': -1},
             {'string': '', 'expected': -1}, {'string': 'ggyllaylacrhdzedddjsc', 'expected': 10},
             {'string': 'aaaaaaaaaaaaaaaaaaaabbbbbbbbbbcccccccccccdddddddddddeeeeeeeeffghgh', 'expected': -1},
             {'string': 'aabbccddeeff', 'expected': -1}]

    for i, test in enumerate(tests):
        x = firstNonRepeatingCharacter(test['string'])
        assert x == test['expected'], f'Test {i} - Expected: {test["expected"]}, got {x}'
