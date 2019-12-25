# title: best-time-to-buy-and-sell-stock-ii
# detail: https://leetcode.com/submissions/detail/190695904/
# datetime: Tue Nov 20 18:21:23 2018
# runtime: 72 ms
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
        prev_price = prices[0]
        max_profit = 0
        i = 1
        
        if prices[0] < prices[1]:
            in_price = prices[0]
            
        while i < days - 1:
            prev_price = prices[i - 1]
            price = prices[i]
            next_price = prices[i + 1]
            if price > prev_price and price >= next_price:
                max_profit += price - in_price
                print(max_profit)
                in_price = None
            if price <= prev_price and price < next_price:
                in_price = price
            i += 1  
        if in_price is not None and prices[i] > in_price:
                max_profit += prices[i] - in_price
        return max_profit
        