# title: best-time-to-buy-and-sell-stock-ii
# detail: https://leetcode.com/submissions/detail/275265169/
# datetime: Sat Nov  2 15:43:56 2019
# runtime: 112 ms
# memory: 17.3 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = [[0, -prices[0]] for _ in range(len(prices))]
        for i in range(1, len(prices)):
            max_profit[i][0] = max(max_profit[i - 1][0], max_profit[i - 1][1] + prices[i])
            max_profit[i][1] = max(max_profit[i - 1][1], max_profit[i - 1][0] - prices[i])
        m = max_profit[len(prices) - 1]
        if m[0] > m[1]:
            return m[0]
        return m[1]