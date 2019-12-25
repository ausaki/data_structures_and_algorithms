# title: best-time-to-buy-and-sell-stock-ii
# detail: https://leetcode.com/submissions/detail/275063913/
# datetime: Fri Nov  1 19:40:13 2019
# runtime: 72 ms
# memory: 15.1 MB

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        deltas = [p1 - p0 for p0, p1 in zip(prices[:-1], prices[1:])]
        return sum(filter(lambda x: x > 0, deltas))
        