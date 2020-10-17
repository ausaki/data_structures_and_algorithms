# title: flip-string-to-monotone-increasing
# detail: https://leetcode.com/submissions/detail/403997359/
# datetime: Sun Oct  4 01:19:33 2020
# runtime: 68 ms
# memory: 14.8 MB

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        p = [0]
        for c in S:
            p.append(p[-1] + int(c))
        n = len(S)
        return min(p[i] + n - i - (p[-1] - p[i]) for i in range(n + 1))
            
        