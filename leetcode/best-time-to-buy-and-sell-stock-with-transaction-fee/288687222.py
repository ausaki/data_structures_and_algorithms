# title: best-time-to-buy-and-sell-stock-with-transaction-fee
# detail: https://leetcode.com/submissions/detail/288687222/
# datetime: Thu Dec 26 19:57:25 2019
# runtime: 1012 ms
# memory: 21.7 MB

from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        max_profit = [[0, -prices[0]] for _ in range(len(prices))]
        for i in range(1, len(prices)):
            max_profit[i][0] = max(max_profit[i - 1][0], max_profit[i - 1][1] + prices[i] - fee)
            max_profit[i][1] = max(max_profit[i - 1][1], max_profit[i - 1][0] - prices[i])
        return max(max_profit[len(prices) - 1])
