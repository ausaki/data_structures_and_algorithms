# title: palindrome-partitioning
# detail: https://leetcode.com/submissions/detail/284088403/
# datetime: Fri Dec  6 15:02:28 2019
# runtime: 88 ms
# memory: 13 MB

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(i, j):
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            return i >= j
        
        def dfs(i):
            if i >= N:
                return [[]]
            j = i
            res = []
            while j < N:
                if ispalindrome(i, j):
                    part = dfs(j + 1)
                    for p in part:
                        p.insert(0, s[i: j + 1])
                        res.append(p)
                j += 1
            return res
        
        N = len(s)
        return dfs(0)
                