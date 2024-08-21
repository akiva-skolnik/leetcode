from collections import Counter


# https://leetcode.com/problems/maximum-number-of-balloons
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as
            possible. You can use each character in text at most once. Return the maximum number of instances that can be
            formed."""
        if not text:
            return 0
        target_count = Counter("balloon")
        input_count = Counter(text)
        return min(input_count.get(k, 0) // v for k, v in target_count.items())


def test_1():
    assert Solution().maxNumberOfBalloons("nlaebolko") == 1


def test_2():
    assert Solution().maxNumberOfBalloons("loonbalxballpoon") == 2


def test_3():
    assert Solution().maxNumberOfBalloons("leetcode") == 0


def test_4():
    assert Solution().maxNumberOfBalloons("") == 0
