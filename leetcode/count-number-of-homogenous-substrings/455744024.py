# title: count-number-of-homogenous-substrings
# detail: https://leetcode.com/submissions/detail/455744024/
# datetime: Sun Feb 14 10:40:49 2021
# runtime: 236 ms
# memory: 16.7 MB

class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        g = []
        for c in s:
            if not g or c != g[-1][0]:
                g.append([c, 1])
            else:
                g[-1][1] += 1
        res = 0
        for c, k in g:
            res = (res + k * (k + 1) // 2) % MOD
        return res
        