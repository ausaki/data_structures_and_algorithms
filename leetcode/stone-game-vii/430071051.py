# title: stone-game-vii
# detail: https://leetcode.com/submissions/detail/430071051/
# datetime: Sun Dec 13 11:23:25 2020
# runtime: 3928 ms
# memory: 14.4 MB

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        # @lru_cache(None)
        # def dp(i, j):
        #     if i == j:
        #         return 0
        #     p = n - (j - i)
        #     if p % 2:
        #         # bob
        #         d1 = dp(i + 1, j)
        #         d1 -= prefix[j] - prefix[i + 1]
        #         d2 = dp(i, j - 1)
        #         d2 -= prefix[j - 1] - prefix[i]
        #         return min(d1, d2)
        #     #alice
        #     d1 = dp(i + 1, j)
        #     d1 += prefix[j] - prefix[i + 1]
        #     d2 = dp(i, j - 1)
        #     d2 += prefix[j - 1] - prefix[i]
        #     return max(d1, d2)
        
        prefix = [0]
        for st in stones:
            prefix.append(prefix[-1] + st)
        n = len(stones)
        # return dp(0, n)
    
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                p = n - (j - i) 
                if p % 2:
                    d1 = dp[j] - (prefix[j] - prefix[i + 1])
                    d2 = dp[j - 1] - (prefix[j - 1] - prefix[i])
                    dp[j] = min(d1, d2)
                else:
                    d1 = dp[j] + (prefix[j] - prefix[i + 1])
                    d2 = dp[j - 1] + prefix[j - 1] - prefix[i]
                    dp[j] = max(d1, d2)
        return dp[n]
