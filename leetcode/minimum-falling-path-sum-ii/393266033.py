# title: minimum-falling-path-sum-ii
# detail: https://leetcode.com/submissions/detail/393266033/
# datetime: Wed Sep  9 20:59:20 2020
# runtime: 7920 ms
# memory: 31.7 MB

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        @lru_cache(None)
        def dp(i, j):
            if i == n:
                return 0
            return min(dp(i + 1, j_) + arr[i][j_] for j_ in range(n) if j_ != j)
        
        return dp(0, -1)