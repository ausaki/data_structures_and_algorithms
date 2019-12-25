# title: palindrome-partitioning
# detail: https://leetcode.com/submissions/detail/284092243/
# datetime: Fri Dec  6 15:22:17 2019
# runtime: 60 ms
# memory: 15.6 MB

from functools import lru_cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(i, j):
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            return i >= j
        
        @lru_cache(None)
        def dfs(i):
            if i >= N:
                return [[]]
            j = i
            res = []
            while j < N:
                if ispalindrome(i, j):
                    part = dfs(j + 1)
                    p0 = s[i: j + 1]
                    for p in part:
                        res.append([p0] + p)
                j += 1
            return res
        
        N = len(s)
        return dfs(0)
                