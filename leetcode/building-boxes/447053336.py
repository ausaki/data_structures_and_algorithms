# title: building-boxes
# detail: https://leetcode.com/submissions/detail/447053336/
# datetime: Sun Jan 24 13:43:07 2021
# runtime: 280 ms
# memory: 14.3 MB

class Solution:
    def minimumBoxes(self, n: int) -> int:
        
        def check(k):
            x = int((math.sqrt(1 + 8 * k) - 1) / 2)
            k = k - x * (1 + x) // 2
            t = 0
            s = 0
            for i in range(1, x + 1):
                s += i
                t += s
            t += k * (1 + k) // 2
            return t
            
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            s = check(m)
            if s == n:
                return m
            elif s > n:
                r = m - 1
            else:
                l = m + 1
        return l