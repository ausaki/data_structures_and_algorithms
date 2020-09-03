# title: final-prices-with-a-special-discount-in-a-shop
# detail: https://leetcode.com/submissions/detail/380808843/
# datetime: Fri Aug 14 22:33:30 2020
# runtime: 56 ms
# memory: 14.1 MB

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        new_prices = [0] * n
        for i, p in enumerate(prices):
            while stack and p <= prices[stack[-1]]:
                j = stack.pop()
                new_prices[j] = prices[j] - p
            stack.append(i)
        for i in stack:
            new_prices[i] = prices[i]
        return new_prices