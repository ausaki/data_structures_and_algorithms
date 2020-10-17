# title: online-stock-span
# detail: https://leetcode.com/submissions/detail/405228009/
# datetime: Tue Oct  6 18:51:49 2020
# runtime: 456 ms
# memory: 18.6 MB

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.days = 0
        
    def next(self, price: int) -> int:
        self.days += 1
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        span = self.days
        if self.stack:
            span -= self.stack[-1][1]
        self.stack.append([price, self.days])
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)