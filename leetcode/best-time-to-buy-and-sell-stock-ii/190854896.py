# title: best-time-to-buy-and-sell-stock-ii
# detail: https://leetcode.com/submissions/detail/190854896/
# datetime: Wed Nov 21 14:11:55 2018
# runtime: 60 ms
# memory: N/A

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if days == 0 or days == 1:
            return 0
        
        in_price = None
        max_profit = 0
        i = 0
            
        while i < days - 1:
            price = prices[i]
            next_price = prices[i + 1]
            if in_price is not None and price >= next_price:
                max_profit += price - in_price
                in_price = None
            if in_price is None and price < next_price:
                in_price = price
            i += 1  
        
        if in_price is not None and prices[i] > in_price:
            max_profit += prices[i] - in_price
        return max_profit
        