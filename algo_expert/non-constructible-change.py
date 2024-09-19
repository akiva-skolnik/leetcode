# https://www.algoexpert.io/questions/non-constructible-change
def nonConstructibleChange(coins: list) -> int:
    """Given an array of positive integers representing the values of coins in your possession,
        write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create."""
    coins.sort()
    if not coins or coins[0] != 1:
        return 1

    partial_sum = 1
    for i in range(1, len(coins)):
        if partial_sum + 1 < coins[i]:
            return partial_sum + 1
        partial_sum += coins[i]

    return partial_sum + 1


def test():
    tests = [{'coins': [1, 1, 2, 3, 5, 7, 22], 'expected': 20}, {'coins': [1, 1, 1, 1, 1], 'expected': 6},
             {'coins': [1, 1, 1, 1, 5, 10, 15, 20, 100], 'expected': 55},
             {'coins': [1, 1, 4, 5, 6, 8, 9], 'expected': 3}, {'coins': [], 'expected': 1},
             {'coins': [87], 'expected': 1}, {'coins': [1, 1, 2, 3, 4, 5, 6, 9], 'expected': 32},
             {'coins': [1, 1, 2, 3, 5, 6, 43], 'expected': 19}, {'coins': [1, 1], 'expected': 3},
             {'coins': [2], 'expected': 1}, {'coins': [1], 'expected': 2},
             {'coins': [1, 1, 2, 4, 8, 16, 17, 18, 19, 109, 2000, 8765], 'expected': 87},
             {'coins': [1, 2, 3, 4, 5, 6, 7], 'expected': 29}]
    for test in tests:
        coins, expected = test['coins'], test['expected']
        assert nonConstructibleChange(coins) == expected, f"expected {expected} for {coins}"
