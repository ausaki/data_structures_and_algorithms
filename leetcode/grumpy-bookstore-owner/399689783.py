# title: grumpy-bookstore-owner
# detail: https://leetcode.com/submissions/detail/399689783/
# datetime: Wed Sep 23 22:29:38 2020
# runtime: 304 ms
# memory: 15.9 MB

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        t = 0
        w = 0
        m = 0
        for i in range(X):
            if grumpy[i] == 1:
                w += customers[i]
            else:
                t += customers[i]
        m = max(m, w)
        for i in range(X, len(grumpy)):
            if grumpy[i]:
                w += customers[i]
            else:
                t += customers[i]
            if grumpy[i - X]:
                w -= customers[i - X]
            m = max(m, w)
        return t + m