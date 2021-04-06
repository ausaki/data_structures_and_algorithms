# title: maximum-value-at-a-given-index-in-a-bounded-array
# detail: https://leetcode.com/submissions/detail/470403876/
# datetime: Sun Mar 21 11:14:24 2021
# runtime: 44 ms
# memory: 14.2 MB

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def check(m):
            s = m
            if m - 1 >= index:
                s += index * (m - index + m - 1) // 2
            else:
                s += m * (m - 1) // 2 + index - (m - 1)
            k = n - index - 1
            if m - 1 >= k:
                s += k * (m - k + m - 1) // 2
            else:
                s += m * (m - 1) // 2 + k - (m - 1)
            # print(m, s)
            return s <= maxSum
        
        l, r = 1, maxSum
        while l <= r:
            m = (l + r) // 2
            if check(m):
                l = m + 1
            else:
                r = m - 1
        # print(l, r)
        return r