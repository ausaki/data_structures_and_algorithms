# title: minimum-difficulty-of-a-job-schedule
# detail: https://leetcode.com/submissions/detail/390875402/
# datetime: Fri Sep  4 17:33:19 2020
# runtime: 972 ms
# memory: 14.9 MB

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        M = 1e6
        
        @lru_cache(None)
        def dp(i, j):
            if i == n and j == d:
                return 0
            if i == n or j == d:
                return M
            
            diff = -1
            result = M
            for k in range(i, n):
                diff = max(diff, jobDifficulty[k])
                result = min(result, diff + dp(k + 1, j + 1))
            return result
        
        result = dp(0, 0)
        return result if result < M else -1