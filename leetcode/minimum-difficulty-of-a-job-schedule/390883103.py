# title: minimum-difficulty-of-a-job-schedule
# detail: https://leetcode.com/submissions/detail/390883103/
# datetime: Fri Sep  4 18:09:08 2020
# runtime: 792 ms
# memory: 15.1 MB

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        # if d == 1: 
        #     return max(jobDifficulty)
        # if n == d:
        #     return sum(jobDifficulty)
        # if n < d:
        #     return -1
        M = 1e6
        @lru_cache(None)
        def dp(i, j):
            if i == n and j == d:
                return 0
            if i == n or j == d:
                return M
            if d - j == 1:
                return max(jobDifficulty[i:])
            if d - j == n - i:
                return sum(jobDifficulty[i:])
            if d - j > n - i:
                return M
            
            diff = -1
            result = M
            for k in range(i, n):
                diff = max(diff, jobDifficulty[k])
                result = min(result, diff + dp(k + 1, j + 1))
            return result
        
        result = dp(0, 0)
        return result if result < M else -1
        