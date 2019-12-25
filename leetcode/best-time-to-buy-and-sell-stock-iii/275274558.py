# title: best-time-to-buy-and-sell-stock-iii
# detail: https://leetcode.com/submissions/detail/275274558/
# datetime: Sat Nov  2 17:04:56 2019
# runtime: 132 ms
# memory: 21.7 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        K = 2
        if K > N - 1:
            K = N - 1
        max_profit = [
            [[0, 0] for k in range(K)] for i in range(N)
        ]
        for k in range(K):
            max_profit[0][k][0] = 0
            max_profit[0][k][1] = -prices[0]
        for i in range(1, N):
            for k in range(K):
                max_profit[i][k][0] = max(max_profit[i - 1][k][0], max_profit[i - 1][k][1] + prices[i])
                if k == 0:
                    max_profit[i][k][1] = max(max_profit[i - 1][k][1], - prices[i])    
                else:
                    max_profit[i][k][1] = max(max_profit[i - 1][k][1], max_profit[i - 1][k - 1][0] - prices[i])
    
        m = max_profit[N - 1]
        result = 0
        for k in range(K):
            if m[k][0] > result:
                result = m[k][0]
            if m[k][1] > result:
                result = m[k][1]
        return result