# title: maximize-score-after-n-operations
# detail: https://leetcode.com/submissions/detail/470182920/
# datetime: Sat Mar 20 23:26:17 2021
# runtime: 1804 ms
# memory: 25 MB

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) //  2
        
        @lru_cache(None)
        def dp(i, mask):
            if i == n:
                return 0
            idx = [j for j in range(n * 2) if mask & (1 << j)]
            res = 0
            for j, k in itertools.combinations(idx, 2):
                sub = mask & ~((1 << j) | (1 << k))
                val = (i + 1) * math.gcd(nums[j], nums[k]) + dp(i + 1, sub)
                res = max(res, val)
            return res
        
        return dp(0, (1 << (2 * n)) - 1)