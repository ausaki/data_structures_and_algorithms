# title: largest-sum-of-averages
# detail: https://leetcode.com/submissions/detail/410967159/
# datetime: Tue Oct 20 14:44:31 2020
# runtime: 208 ms
# memory: 15.6 MB

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        @lru_cache(None)
        def dp(i, k):
            if n - i < k or (n - i > 0 and k == 0):
                return -math.inf
            if i == n and k == 0:
                return 0
            if n - i == k:
                return sum(A[i:])
            s = 0
            avg = -math.inf
            for j in range(i, n):
                s += A[j]
                avg = max(avg, s / (j - i + 1) + dp(j + 1, k - 1))
            return avg
        
        n = len(A)
        return dp(0, K)
            