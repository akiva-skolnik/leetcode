from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(prices[i] - prices[i - 1]
                   for i in range(1, len(prices))
                   if prices[i] > prices[i - 1])


def test_1():
    prices = [7, 1, 5, 3, 6, 4]
    result = Solution().maxProfit(prices)
    assert result == 7


def test_2():
    prices = [1, 2, 3, 4, 5]
    result = Solution().maxProfit(prices)
    assert result == 4


def test_3():
    prices = [7, 6, 4, 3, 1]
    result = Solution().maxProfit(prices)
    assert result == 0
