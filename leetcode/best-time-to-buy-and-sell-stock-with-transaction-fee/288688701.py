# title: best-time-to-buy-and-sell-stock-with-transaction-fee
# detail: https://leetcode.com/submissions/detail/288688701/
# datetime: Thu Dec 26 20:10:27 2019
# runtime: 760 ms
# memory: 19.4 MB

from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        a, b = 0, -prices[0]
        for i in range(1, len(prices)):
            a, b = max(a, b + prices[i] - fee), max(b, a - prices[i])
        return max(a, b)
