# title: best-time-to-buy-and-sell-stock-ii
# detail: https://leetcode.com/submissions/detail/288679991/
# datetime: Thu Dec 26 18:55:02 2019
# runtime: 56 ms
# memory: 13.9 MB

from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # fee = 0
        # @lru_cache(None)
        # def buy(i, k):
        #     if i == len(prices):
        #         return 0 if k < 0 else -prices[k]
        #     if k < 0:
        #         return max(buy(i + 1, k), buy(i + 1, i))
        #     return max(buy(i + 1, k),
        #                prices[i] - prices[k] - fee + buy(i + 1, -1),
        #                prices[i] - prices[k] - fee + buy(i + 1, i))
        # return buy(0, -1)
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1] 
        return res
            