# title: pizza-with-3n-slices
# detail: https://leetcode.com/submissions/detail/385601670/
# datetime: Mon Aug 24 17:50:56 2020
# runtime: 404 ms
# memory: 82.9 MB

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j, k):
            if k == 0:
                return 0
            if i > j:
                return 0
            return max(dp(i + 1, j, k), slices[i] + dp(i + 2, j, k - 1))
            
        n = len(slices)
        # slices.sort()
        return max(dp(0, n - 2, n // 3), dp(1, n - 1, n // 3))