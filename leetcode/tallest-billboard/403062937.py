# title: tallest-billboard
# detail: https://leetcode.com/submissions/detail/403062937/
# datetime: Thu Oct  1 18:18:44 2020
# runtime: 868 ms
# memory: 14.4 MB

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @lru_cache(None)
        def dp(i, d):
            if i == n:
                return 0 if d == 0 else -1
            result = -1
            a = dp(i + 1, rods[i] + d)
            if a >= 0: result = max(result, a + rods[i])
            a = dp(i + 1, d - rods[i])
            if a >= 0: result = max(result, a)
            a = dp(i + 1, d)
            if a >= 0: result = max(result, a)
            return result
        
        n = len(rods)
        rods.sort()
        prefixsum = [0]
        for i in rods:
            prefixsum.append(prefixsum[-1] + i)
        s = prefixsum[-1]
        dp = [-1] * (s + 1) * 2
        dp[s] = 0
        for i in range(n - 1, -1, -1):
            new_dp = [-1] * (s + 1) * 2
            for d in range(-prefixsum[i], prefixsum[i] + 1):
                m = -1
                if dp[rods[i] + d + s] >= 0:
                    m = max(m, dp[rods[i] + d + s] + rods[i])
                if dp[d - rods[i] + s] >= 0:
                    m = max(m, dp[d - rods[i] + s])
                if dp[d + s] >= 0:
                    m = max(m, dp[d + s])
                new_dp[d + s] = m
            dp = new_dp
        return dp[s]
            