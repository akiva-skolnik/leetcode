# https://www.algoexpert.io/questions/nth-fibonacci
def getNthFib(n: int) -> int:
    """return the nth Fibonacci number [fib(n) = fib(n-1) + fib(n-2), fib(1) = 0, fib(2) = 1]"""
    if n <= 2:
        return n - 1

    n1 = 0
    n2 = 1

    for i in range(3, n + 1):
        n1, n2 = n2, n1 + n2

    return n2


def test():
    tests = [{'n': 6, 'expected': 5}, {'n': 1, 'expected': 0}, {'n': 2, 'expected': 1}, {'n': 3, 'expected': 1},
             {'n': 4, 'expected': 2}, {'n': 5, 'expected': 3}, {'n': 7, 'expected': 8}, {'n': 8, 'expected': 13},
             {'n': 9, 'expected': 21}, {'n': 10, 'expected': 34}, {'n': 11, 'expected': 55}, {'n': 12, 'expected': 89},
             {'n': 13, 'expected': 144}, {'n': 14, 'expected': 233}, {'n': 15, 'expected': 377},
             {'n': 16, 'expected': 610}, {'n': 17, 'expected': 987}, {'n': 18, 'expected': 1597}]
    for test in tests:
        n, expected = test['n'], test['expected']
        assert getNthFib(n) == expected, f"expected {expected} for {n}"
