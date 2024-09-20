# https://www.algoexpert.io/questions/longest-peak
def longestPeak(array: list) -> int:
    """returns the length of the longest peak in the array.
    A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip
        (the highest value in the peak), at which point they become strictly decreasing (at least 3 forming a peak)."""
    if len(array) < 3:
        return 0
    peak = temp_peak = 1
    is_up = None

    for i in range(1, len(array)):
        if is_up is None and array[i] > array[i - 1]:
            is_up = True

        if is_up and array[i] < array[i - 1]:
            is_up = False
        elif not is_up and array[i] >= array[i - 1]:
            if is_up is not None:
                peak = max(temp_peak, peak)
            is_up = True
            temp_peak = 1

        if array[i] == array[i - 1]:
            is_up = None
            temp_peak = 1
        if is_up is not None:
            temp_peak += 1

    if array[-1] < array[-2]:
        peak = max(temp_peak, peak)
    return 0 if peak < 3 else peak


def test():
    tests = [{'array': [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3], 'expected': 6},
             {'array': [], 'expected': 0},
             {'array': [1, 3, 2], 'expected': 3},
             {'array': [1, 2, 3, 4, 5, 1], 'expected': 6},
             {'array': [5, 4, 3, 2, 1, 2, 1], 'expected': 3},
             {'array': [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10], 'expected': 5},
             {'array': [5, 4, 3, 2, 1, 2, 10, 12], 'expected': 0},
             {'array': [1, 2, 3, 4, 5, 6, 10, 100, 1000], 'expected': 0},
             {'array': [1, 2, 3, 3, 2, 1], 'expected': 0},
             {'array': [1, 1, 3, 2, 1], 'expected': 4},
             {'array': [1, 2, 3, 2, 1, 1], 'expected': 5},
             {'array': [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1],
              'expected': 9},
             {'array': [1, 2, 3, 3, 4, 0, 10], 'expected': 3}]

    for test in tests:
        array, expected = test['array'], test['expected']
        r = longestPeak(array)
        assert r == expected, f"expected {expected} but got {r}"
