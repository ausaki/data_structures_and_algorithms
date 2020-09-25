# title: grumpy-bookstore-owner
# detail: https://leetcode.com/submissions/detail/399691225/
# datetime: Wed Sep 23 22:34:10 2020
# runtime: 304 ms
# memory: 16.1 MB

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        t = w = m = x = 0
        for i in range(len(grumpy)):
            if grumpy[i]:
                w += customers[i]
            else:
                t += customers[i]
            x += 1
            if x > X and grumpy[i - X]:
                w -= customers[i - X]
            m = max(m, w)
        return t + m