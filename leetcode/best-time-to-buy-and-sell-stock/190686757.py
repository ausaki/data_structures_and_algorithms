# title: best-time-to-buy-and-sell-stock
# detail: https://leetcode.com/submissions/detail/190686757/
# datetime: Tue Nov 20 16:49:04 2018
# runtime: 28 ms
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
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit