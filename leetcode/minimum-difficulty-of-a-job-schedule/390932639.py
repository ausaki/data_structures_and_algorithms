# title: minimum-difficulty-of-a-job-schedule
# detail: https://leetcode.com/submissions/detail/390932639/
# datetime: Fri Sep  4 21:57:54 2020
# runtime: 796 ms
# memory: 15.2 MB

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        M = 1e6
        @lru_cache(None)
        def dp(i, d):
            if i == n and d == 0:
                return 0
            if i == n or d == 0:
                return M
            if d == 1:
                return max(jobDifficulty[i:])
            if d == n - i:
                return sum(jobDifficulty[i:])
            if d > n - i:
                return M
            diff = -1
            result = M
            for k in range(i, n):
                diff = max(diff, jobDifficulty[k])
                result = min(result, diff + dp(k + 1, d - 1))
            return result
        
        result = dp(0, d)
        return result if result < M else -1
        