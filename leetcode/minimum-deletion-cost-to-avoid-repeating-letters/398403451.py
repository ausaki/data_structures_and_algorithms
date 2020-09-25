# title: minimum-deletion-cost-to-avoid-repeating-letters
# detail: https://leetcode.com/submissions/detail/398403451/
# datetime: Mon Sep 21 02:28:59 2020
# runtime: 1212 ms
# memory: 24.4 MB

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s += '*'
        n = len(s)
        result = 0
        m = 0
        t = 0
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                m = max(m, cost[i])    
                t += cost[i]
            else:
                if m:
                    m = max(m, cost[i])
                    t += cost[i]
                    result += t - m
                m = 0
                t = 0
        return result