from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best_profit = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > best_profit:
                    best_profit = profit
        return best_profit


def test_1():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5  # 6 - 1 = 5


def test_2():
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
