# title: regular-expression-matching
# detail: https://leetcode.com/submissions/detail/343382144/
# datetime: Sat May 23 14:31:05 2020
# runtime: 32 ms
# memory: 14.2 MB

from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N = len(s)
        M = len(p)
        
        @lru_cache(None)
        def match(i, j):
            # print(i, j)
            if j == M:
                return i == N
            m = i < N and (p[j] == '.' or s[i] == p[j])
            if j + 1 >= M or p[j + 1] != '*':
                return m and match(i + 1, j + 1)
            if m and match(i + 1, j):
                return True
            return match(i, j + 2)
        
        return match(0, 0)