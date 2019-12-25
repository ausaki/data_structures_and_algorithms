# title: best-time-to-buy-and-sell-stock
# detail: https://leetcode.com/submissions/detail/190687050/
# datetime: Tue Nov 20 16:51:36 2018
# runtime: 24 ms
# memory: N/A

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            d = price - min_price
            if d < 0:
                min_price = price
            elif d > max_profit:
                max_profit = d
        return max_profit