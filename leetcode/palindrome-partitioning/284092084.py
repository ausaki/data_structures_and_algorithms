# title: palindrome-partitioning
# detail: https://leetcode.com/submissions/detail/284092084/
# datetime: Fri Dec  6 15:21:30 2019
# runtime: 68 ms
# memory: 17.4 MB

from functools import lru_cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @lru_cache(None)
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
                