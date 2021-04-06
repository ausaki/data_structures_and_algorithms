# title: maximum-value-at-a-given-index-in-a-bounded-array
# detail: https://leetcode.com/submissions/detail/470440329/
# datetime: Sun Mar 21 12:34:25 2021
# runtime: 56 ms
# memory: 14.4 MB

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def check(m):
            s = m
            k = min(index, m - 1)
            s += k * (m - k + m - 1) // 2 + index - k
            k = min(n - index - 1, m - 1)
            s += k * (m - k + m - 1) // 2 + n - index - 1 - k
            return s <= maxSum
        
        l, r = 1, maxSum
        while l <= r:
            m = (l + r) // 2
            if check(m):
                l = m + 1
            else:
                r = m - 1
        return r