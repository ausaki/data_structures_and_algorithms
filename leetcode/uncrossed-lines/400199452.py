# title: uncrossed-lines
# detail: https://leetcode.com/submissions/detail/400199452/
# datetime: Fri Sep 25 01:20:34 2020
# runtime: 172 ms
# memory: 21.3 MB

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        pos = collections.defaultdict(list)
        for i, j in enumerate(B):
            pos[j].append(i)
        @lru_cache(None)
        def dp(i, j):
            if i == m or j == n:
                return 0
            a = dp(i + 1, j)
            b = 0
            if A[i] in pos:
                idx = pos[A[i]]
                k = bisect.bisect_left(idx, j)
                if k < len(idx):
                    b = 1 + dp(i + 1, idx[k] + 1)
            return max(a, b)
        
        return dp(0, 0)
                    