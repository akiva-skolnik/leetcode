from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            best_profit = max(best_profit, price - min_price)
        return best_profit


def test_1():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5  # 6 - 1 = 5


def test_2():
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
