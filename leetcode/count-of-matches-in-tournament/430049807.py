# title: count-of-matches-in-tournament
# detail: https://leetcode.com/submissions/detail/430049807/
# datetime: Sun Dec 13 10:34:25 2020
# runtime: 28 ms
# memory: 14.1 MB

class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            q, r = divmod(n, 2)
            res += q
            n = q + r
        return res