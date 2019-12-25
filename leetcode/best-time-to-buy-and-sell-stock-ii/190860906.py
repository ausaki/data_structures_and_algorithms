# title: best-time-to-buy-and-sell-stock-ii
# detail: https://leetcode.com/submissions/detail/190860906/
# datetime: Wed Nov 21 14:44:57 2018
# runtime: 44 ms
# memory: N/A

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.maxProfit2(prices)
    
    def maxProfit1(self, prices):
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

    def maxProfit2(self, prices):
        length = len(prices)
        if length == 0 or length == 1:
            return 0
        max_profit = 0
        valley = prices[0]
        peak = prices[0]
        
        i = 0
        while i < length - 1:
            while i < length - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < length - 1 and prices[i] < prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit += (peak - valley)
        return max_profit
                
            
        
        