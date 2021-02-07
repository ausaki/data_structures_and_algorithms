# title: maximum-score-from-removing-stones
# detail: https://leetcode.com/submissions/detail/453003135/
# datetime: Sun Feb  7 10:57:12 2021
# runtime: 304 ms
# memory: 14.3 MB

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        res = a + min(b, c - a)
        for i in range(1, a + 1):
            res = max(res, a - i + min(c - (a - i), b - i) + i)
        return res
        