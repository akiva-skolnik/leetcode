# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    def strStr2(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        return haystack.index(needle)


def test_1():
    haystack = "sadbutsad"
    needle = "sad"
    result = Solution().strStr(haystack, needle)
    assert result == 0


def test_2():
    haystack = "leetcode"
    needle = "leeto"
    result = Solution().strStr(haystack, needle)
    assert result == -1


def check_time():
    import timeit
    import random
    import string

    haystack = "".join(random.choices(string.ascii_lowercase, k=10 ** 5))
    needle = "".join(random.choices(string.ascii_lowercase, k=10 ** 2))
    print(timeit.timeit(lambda: Solution().strStr(haystack, needle), number=1000))
    print(timeit.timeit(lambda: Solution().strStr2(haystack, needle), number=1000))

    needle = haystack[10 ** 3:10 ** 3 + 10 ** 2]
    print(timeit.timeit(lambda: Solution().strStr(haystack, needle), number=1000))
    print(timeit.timeit(lambda: Solution().strStr2(haystack, needle), number=1000))


if __name__ == "__main__":
    check_time()
